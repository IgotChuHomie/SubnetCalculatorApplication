
class voiture:
    name = None
    age = None
    type = None

    def __init__(self,name,type,age):
        self.name = str(name)
        self.age = int(age)
        self.type = str(type)

    def getage(self):
        if (age != None and type != None and name != None) :
            return f"the age is {self.age} and the name is {self.name} and the type is {self.type} "



quitequite = voiture("r4","rr4",13)

print(quitequite.getage())









# string =  "oussama/abdoune/Meknes/BtsDsi"
# splitedString = string.split("/")
#
# print("=====================")
# for element in splitedString :
#     print(element)
# print("=====================")
# string2 = "oussama"
# if string2 in splitedString :
#     print(f"{string2} is in the list {splitedString}")


