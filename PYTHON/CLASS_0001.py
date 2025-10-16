

class hem:
    def std(n,name,rno,city):
        n.name=name
        n.rno=rno
        n.city=city

    def show(n):
        print(n.name,n.rno,n.city)


d1=hem()
d1.std('HMEU',241,'ANANTAPURAMU')


d1.show()



class hem:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno

    def dis(self):
        print(self.name,self.rno)

d=hem('akhil',265001)
d1=hem('akhil',265001)

d1.dis()
d.dis()


        

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")


# Example usage
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model 28", 2023)

car1.display_info()
car2.display_info()
