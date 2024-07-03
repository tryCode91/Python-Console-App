# cursor = cursorsor
# con = connection
# res = result

# Used solemnly for the terminal program
from db import DatabaseConnection

class database:
    
    def CreateUser(name, age, password):    
        data = [(name, age, password)]
        connection = DatabaseConnection()    
        cursor = connection[0]
        connect = connection[1]
        cursor.executemany("INSERT INTO users(name, age, password) VALUES(?, ?, ?)", data)
        connect.commit()
        connect.close()

    def ShowAllUsers():
        connection = DatabaseConnection()
        cursor = connection[0]
        connect = connection[1]
        result = cursor.execute("SELECT rowid, name, age, password FROM users")
        return_result = result.fetchall()
        
        for rows in range(len(return_result)):
            print(rows, end=" ")
            print(return_result[rows])

        connect.close()

    
    def showOneUser(rowid):
        connection = DatabaseConnection()
        cursor = connection[0]
        connect = connection[1]
        response = cursor.execute("SELECT rowid, name, age, password FROM users WHERE rowid = '" + rowid + "';")
        
        result = response.fetchone()
        
        if result:
            
            print(f'Name: {result[1]} | Age: {result[2]} | Password: {result[3]} | ID: {result[0]}')
        
        connect.commit()
        connect.close()
        
    def CheckRows():
        
        connection = DatabaseConnection()
        cursor = connection[0]
        connect = connection[1]
        result = cursor.execute("SELECT Count(*) FROM users")
        return_result = result.fetchall()

        if return_result is None:
            return_result = 0
        else:
            return int(return_result[0][0])
            
        connect.close()

    def UserExists(name, password):
        connection = DatabaseConnection()
        cursor = connection[0]
        connect = connection[1]
        response = cursor.execute("SELECT rowid, name, age, password FROM users WHERE name = '" + name + "' AND password = '" + password + "';")
        
        result = response.fetchone()

        if result:
            server_response = result[0]
        else:
            server_response = 0

        connect.commit()
        connect.close()
        return server_response