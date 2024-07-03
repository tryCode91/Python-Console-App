import sqlite3
def DatabaseConnection():
    con = sqlite3.connect("../../database/home.db")
    cur = con.cursor()
    return cur, con