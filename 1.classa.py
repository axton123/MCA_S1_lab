class car:
    car_name=""

class model(car):
    car_model=input("enter car model")
    car_name=input("enter car name")
    print("Car Details")
    print(car_name,car_model)

c=model()
c