class Person:
    def __int__(self,name,age,password):
        self.name=name
        self.age=age
        self._password=password
        
    @property
    def password(self):
            return self.__password
        
    @password.setter
    def password(self,password):
     self.__password=password
            
            
person=Person('ram',12,'passw123')
print(person.name)
print(person._age)
#person.set_password('123')
person.password=123
print(person.password)