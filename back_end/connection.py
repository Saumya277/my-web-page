'''Algorithm
1. importing mysql connector to  connect with database
2. making class named DbConnection
3. using init method
4. explaning diffrent variables such as insert, select to connect the function with database
'''
import mysql.connector

class DbConnection():
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='saumyalohani',
                                         database='web_data')
        self.cursor=self.con.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def insert(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.cursor.execute(query, values)
        self.con.commit()

    def delete(self,query,values):
        self.cursor.execute(query, values)
        self.con.commit()

    def select(self,query):
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        self.con.commit()
        return records

    def search(self,query,values):
        self.cursor.execute(query,values)
        records = self.cursor.fetchall()
        self.con.commit()
        return records



