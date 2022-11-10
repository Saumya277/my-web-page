'''Algorithm
1. making of a class named student
2. using init method
3. using instance variable ti define set and get method
 '''
class Student:
    def __init__(self,ID,Name,Address,DOB,Gender,Contact,Email):
        self.ID=ID
        self.Name=Name
        self.Address = Address
        self.DOB= DOB
        self.Gender = Gender
        self.Contact = Contact
        self.Email = Email

    def set_ID(self,ID):
        self.ID=ID
    def get_ID(self):
        return self.ID

    def set_Name(self,Name):
        self.Name=Name
    def get_Name(self):
        return self.Name

    def set_Address(self, Address):
        self.Address = Address
    def get_Address(self):
        return self.Address

    def set_DOB(self, DOB):
        self.DOB = DOB
    def get_DOB(self):
        return self.DOB

    def set_Gender(self,Gender):
        self.Gender = Gender
    def get_Gender(self):
        return self.Gender

    def set_Contact(self,Contact):
        self.Contact =Contact
    def get_Contact(self):
        return self.Contact

    def set_Email(self,Email):
        self.Email=Email
    def get_Email(self):
        return self.Email



