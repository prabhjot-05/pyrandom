class no:
    def __init__(self,value1):
        self.value1=value1

    def __add__(self,value2):
        return no(self.value1+value2.value1)
    
    def __sub__(self,value2):
        return no(self.value1-value2.value1)
    
    def __mul__(self,value2):
        return no(self.value1*value2.value1)
    
    def show(self):
        print(self.value1)

n1=no(10)
n2=no(20)

ans=n1+n2
ans.show()
ans2=n1-n2
ans2.show()
ans3=n1*n2
ans3.show()



