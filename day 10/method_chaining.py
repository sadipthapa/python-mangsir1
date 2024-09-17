class pizza:
    
    def dough(self):
        print("dough")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
    def cheese(self):
       print("cheese")
       return self
   
   
pizza=pizza()
pizza.dough().sauce().cheese()

