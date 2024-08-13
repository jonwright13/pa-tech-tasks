from src.question_1.classes import Aircraft, Motorised

print("Part 1:")
ford = Motorised(make="Ford", wheels=4)


print("\nPart 2:")
boeing = Aircraft(make="Boeing", wheels=3, typeOfEngine="kerosene")
boeing.switchOn()
boeing.takeOff()
