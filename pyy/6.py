class grandfather:
    def show(self):
        print("grandFather")
class father(grandfather):
    def show(self):
        super().show()
        print("Father")
class mother(grandfather):
    def show(self):
        super().show()
        print("Mother")        
class child(father,mother):
    def show(self):
        super().show()
        print("Child")  

c=child()
c.show()   