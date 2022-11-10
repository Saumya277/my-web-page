'''Algorithm
1. importing unittest
2. making class Test_learners with variable unittest.TestCase
3. unittesting of the code is done to find whether it is right or it needs any changes
'''
import unittest
from back_end.connection import *
import front_end.Web
from model.model_class import *

class Test_learners(unittest.TestCase):
    def setUp(self):
        self.s=Student(101,"Shiksha Kandel","Maitidevi","14-02-2001","Female","9845672345","shiksha@gmail.com")
        self.con=DbConnection()
        pass
    def test_get_ID(self):
        self.assertEqual(101,self.s.get_ID())
    def test_get_Name(self):
        self.assertEqual("Shiksha Kandel",self.s.get_Name())
    def test_set_ID(self):
        self.s.set_ID(2)
        self.assertEqual(2,self.s.get_ID())
    def test_set_Name(self):
        self.s.set_Name("Pallabi")
        self.assertEqual("Pallabi",self.s.get_Name())
    def test_get_Address(self):
        self.assertEqual("Maitidevi", self.s.get_Address())
    def test_get_DOB(self):
        self.assertEqual("14-02-2001", self.s.get_DOB())
    def test_set_Address(self):
        self.s.set_Address("Chitwan")
        self.assertEqual("Chitwan", self.s.get_Address())
    def test_set_DOB(self):
        self.s.set_DOB("12-12-2001")
        self.assertEqual("12-12-2001", self.s.get_DOB())
    def test_insert(self):
        query='insert into learners values(%s,%s,%s,%s,%s,%s,%s);'
        values=(105,"Ashraya K.C","Sinamangal","12-04-2000","Male","9808562357","ashraya@hotmail.com")
        self.con.insert(query,values)
        query='select * from learners where ID=%s;'
        values=(105,)
        actual=self.con.search(query,values)
        expect=[(105,"Ashraya K.C","Sinamangal","12-04-2000","Male","9808562357","ashraya@hotmail.com"),]
        self.assertEqual(actual,expect)
    def test_delete(self):
        query='delete from learners where ID=%s;'
        values=(105,)
        self.con.insert(query,values)
        query='select * from learners where ID=%s;'
        values=(105,)
        actual=self.con.search(query,values)
        expect=[]
        self.assertEqual(actual,expect)
    def test_update(self):
        query = 'update learners set Name=%s,Address=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
        values = ("Yangchen Lama","Bouddha","21-11-1999","Female","9856347823","yamgchen@hotmail.com",103)
        self.con.insert(query, values)
        query = 'select * from learners where ID=%s;'
        values = (103,)
        actual = self.con.search(query, values)
        expect = [(103,"Yangchen Lama","Bouddha","21-11-1999","Female","9856347823","yamgchen@hotmail.com")]
        self.assertEqual(actual, expect)
    def test_linear_search(self):
        records=["Sujita KC","Shiksha Kandel"]
        Name="Sujita KC"
        self.assertTrue(front_end.Web.linear_search(records,Name))

    def tearDown(self):
        self.s = None
        self.con = None
if __name__ == "__main__":
    unittest.main()
