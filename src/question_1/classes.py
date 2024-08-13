class Vehicle:
    def __init__(self, make: str):
        self.make = make


class Wheeled(Vehicle):
    def __init__(self, make: str, wheels: int):
        Vehicle.__init__(self, make)
        self.wheels = wheels

    def get_count_of_wheels(self):
        print(f"Number of wheels: {self.wheels}")
        return self.wheels


class Motorised(Wheeled):
    def __init__(self, make: str, wheels: int, typeOfEngine: str = "petrol"):
        Wheeled.__init__(self, make, wheels)
        self.typeOfEngine = typeOfEngine
        print(f"Wroom! {self.make} has been instantiated")

    def switchOn(self):
        print(f"{self.make} switched on")


class Aircraft(Motorised):

    def __init__(self, make: str, wheels: int, typeOfEngine: str):

        # Initialize Motorised part of the Aircraft
        Motorised.__init__(self, make, wheels, typeOfEngine)

    def takeOff(self):
        print(
            f"\nAircraft Make: {self.make}\nCount of Wheels:{self.wheels}\nType of Engine: {self.typeOfEngine}"
        )
        print("\nAircraft taking off...")
