from re import I
import sqlite3
import hashlib
from blockchain import user

con = sqlite3.connect('transactions.db')
cur = con.cursor()
cur.execute(f"CREATE TABLE IF NOT EXISTS `transactions` (id INTEGER PRIMARY KEY autoincrement, hash text, uid int, uid2 int, uname, uname2, amount bigint)")
con.commit()
con.close()

class transactions():
    def create_transaction(id: int, idTo: int, amount: int):
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS `transactions` (id INTEGER PRIMARY KEY autoincrement, hash text, uid int, uid2 int, uname, uname2, amount bigint)")
        con.commit()
        cur.execute(f"SELECT id FROM `transactions` WHERE id = (SELECT MAX(id) FROM transactions)")
        lastTransactionId = cur.fetchone()

        toHash=str(lastTransactionId)+str(id)+str(idTo)+str(amount)
        hash=hashlib.sha224(toHash.encode('utf-8'))

        cur.execute(f"INSERT INTO `transactions` (uid, uid2, uname, uname2, hash, amount) VALUES ({id},{idTo},'{user.users.username(id)}','{user.users.username(idTo)}' ,'{hash}',{amount})")
        con.commit()
        con.close()

    def get_transaction(id: int):
        pass

    def get_user_transactions(user_id: int):
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM `transactions` WHERE uid={user_id} OR uid2={user_id}")
        transactions = cur.fetchall()
        transaction_list = []

        for i in transactions:
            str(transaction_list.append(i))

        print(transaction_list)
        return transaction_list
