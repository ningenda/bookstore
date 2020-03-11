import sqlite3

class Database:
        def __init__(self,db):
                self.conn=sqlite3.connect(db)
                self.cur=self.conn.cursor()
                self.cur.execute("CREATE TABLE IF NOT EXISTS booky (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
                self.conn.commit()


        def insert(self,title,author,year,isbn):

                self.cur.execute("INSERT INTO booky VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
                self.conn.commit()

        def view(self):

                self.cur.execute("SELECT * FROM booky")
                rows=self.cur.fetchall()
                return rows

        def search(self,title="",author="",year="",isbn=""):

                self.cur.execute("SELECT * FROM booky WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
                rows=self.cur.fetchall()
                return rows

        def delete(self,id):

                self.cur.execute("DELETE FROM booky WHERE id=?",(id,))
                swlf.conn.commit()

        def update(self,id,title,author,year,isbn):

                self.cur.execute("UPDATE booky SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
                self.conn.commit()
                self.conn.close()

        def __del__(self):
                self.conn.close()



#connect()
#insert("The Air","John Smith",1908,87913241444)
#delete(5)
#update(4,"The Moon","John Legend Smith",1910,684645)
#print(search(author="John Smith"))
