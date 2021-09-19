import sqlite3
from sqlite3 import connect

class users():
    def get_id(username: str):
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        cur.execute(f"SELECT id FROM `users` WHERE username='{username}'")
        id = cur.fetchone()
        for i in id:
            id = i
        con.commit()
        con.close()
        return id

    def username(id: int):
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        cur.execute(f"SELECT username FROM `users` WHERE id='{id}'")
        name = cur.fetchone()
        for i in name:
            name = i
        con.commit()
        con.close()
        return name
    
    def surname():
        pass
    def wallet_add(amount: int, id: int):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute(f"SELECT wallet FROM `users` WHERE id={id}")
        defamount = cur.fetchone()
        for i in defamount:
            defamount = int(i)
        
        uamount = int(defamount)
        cur.execute(f"UPDATE `users` SET wallet={uamount} + {amount} WHERE id={id}")
        con.commit()
        con.close()

    def wallet_remove(amount: int, id: int):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute(f"SELECT wallet FROM `users` WHERE id={id}")
        defamount = cur.fetchone()
        for i in defamount:
            defamount = i
        cur.execute(f"UPDATE `users` SET wallet={int(defamount)} - {amount} WHERE id={id}")
        con.commit()
        con.close()
    def get_wallet(id: int):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute(f"SELECT wallet FROM `users` WHERE id={id}")
        amount = cur.fetchone()
        for i in amount:
            amount = i
        con.close()
        return amount
    def password():
        pass
    
    def create_user(username: str, surname: str, password: str):
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        cur.execute(f"CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY autoincrement,username text, surname text, password text, wallet bigint)")
        cur.execute(f"INSERT INTO `users` (username, surname, password, wallet) VALUES ('{username}','{surname}','{password}', 0)")
        con.commit()
        con.close()
    
    def is_user_exists(username: str):
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        cur.execute(f"CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY autoincrement,username text, surname text, password text, wallet bigint)")
        cur.execute(f"SELECT id FROM `users` WHERE username='{username}'")
        isExists = cur.fetchone()
        if isExists == None:
            con.commit()
            con.close()
            return False
        else:
            con.commit()
            con.close()
            return True
