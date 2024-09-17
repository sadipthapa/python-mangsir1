class Grandfather(object):
    house="luxerxy House"
    
    def _int_(self) -> None:
        print("grandfather")
        
    def get_house(self):
        return self.house
    
    
    
class Grandmother:
    def _int_(self) -> None:
        print("Grandmother")
    jewellery="sunn wala diamond"
    
class Father(Grandfather,Grandmother):
    
    car="Mercedes"
    
    def get_house(self):
        print(super().get_house())
        return"jhan ramro ghar"
    
class son(Father):
    console="PS5"
    
father=Father()


print(father.get_house())