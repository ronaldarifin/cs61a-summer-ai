class Car:
    classAttribute = 0
    def __init__(self):
        #what is the difference between line 1 and 2?
        
        Car.classAttribute += 1
        self.classAttribute += 1
        # after everything. If I do print(a.mystery) will I see anything?
        self.thisIsAnInstanceAttribute = 0
        mystery = 1

a = Car()
b = Car()
c = Car()