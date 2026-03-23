class car():
    def __init__(self,model,color,fuel,company):
        self.model = model
        self.color = color
        self.fuel = fuel
        self.company = company

    def start(self):
        print("car has started")    

    def stop(self):
        print("car has stopped")


lexus  =  car("RX350","white","deisel","Toyota")
print(lexus.model)
print(lexus.color)
print(lexus.fuel)
print(lexus.company)
lexus.start()


honda = car("Civic","black","petrol","Honda")
print(honda.model)
print(honda.color)
print(honda.fuel)
print(honda.company)
honda.start()



lamborghini = car("Aventador","yellow","petrol","Lamborghini")
print(lamborghini.model)   
print(lamborghini.color)
print(lamborghini.fuel)     
print(lamborghini.company)
lamborghini.start()


