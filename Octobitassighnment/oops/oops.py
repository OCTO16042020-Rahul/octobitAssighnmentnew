# _author_='Rahul kharatmol'


# object

class language:
    def __init__(self, language1):
        self.language1 = language1


    def display(self):
        print(self.language1)


c1 = language("java")
c1.display()


# Creating Methods in Python
class language:

    # instance attributes
    def __init__(self, language1, feature):
        self.language1 = language1
        self.feature = feature

    # instance method
    def language(self, language1):
        return "language {} ".format(self.language1)

# instantiate the object
blu = language("java", "dependent")

# call our instance methods
print(blu.language("''"))



class Parents:

    def __init__(self):
        print("Parenet is ready")

    def whoisThis(self):
        print("Parents")

    def swim(self):
        print("Swim faster")
# child class
class child(Parents):

    def __init__(self):
        # call super() function
        super().__init__()
        print("child is ready")

    def whoisThis(self):
        print("child")
peggy = Parents()
peggy.whoisThis()
peggy.swim()

#Data Encapsulation in Python

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1200
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# Using Polymorphism in Python
class Crow:
     def fly(self):
        print("Crow can fly")


class dolphin:

    def fly(self):
        print("dolphin can't fly")


# common interfacedef
# instantiate objects

def flying_test(bird):
    bird.fly()

#instantiate objects
n1 = Crow()
n2 = dolphin()

# passing the object
flying_test(n1)
flying_test(n2)