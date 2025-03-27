class Cookie:
    def __init__(self, color): 
        #self - instance of class , access attributes of class  
        # __init__ - constructor
        self.color = color

    def getColor(self):
        return self.color 
    
    def setColor(self, color):
        self.color = color

cookie1 = Cookie("green")
cookie2 = Cookie("red") 

print('Cookie1 is ', cookie1.getColor())
print('Cookie2 is ', cookie2.getColor()) 

cookie1.setColor('black')

print('Cookie1 is now ', cookie1.getColor())
print('Cookie2 is still ', cookie2.getColor()) 