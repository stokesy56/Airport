from objects import *
from plane_class import *
from passenger_class import *
from flight_class import *

plane1.add_flight(flight1,flight2,flight3,flight4)
from passenger_class import *

#assigning passenger list to a flight
flight1.add_passengers(passenger1,passenger2,passenger3)
flight2.add_passengers(passenger4,passenger5,passenger6,passenger7)
flight3.add_passengers(passenger8,passenger9,passenger10,passenger11)
flight4.add_passengers(passenger12,passenger13,passenger14)


user_input = input('Welcome to the Filipe Paiva Airport for the super rich. \nType 1 to list flights. \nType 2 to list all passengers on a flight. \nType 3 to add a new passenger to a flight. \nType exit to exit \n')
while user_input != 'exit':
    if user_input == '1':
        print(*plane1.get_flight_list(), sep = '\n')

    elif user_input == '2':
        user_input2 = int(input('Which flight do you want see? Type the flight number \n'))
        if user_input2 == 1:
            print(*flight1.get_flight_passengers(), sep = '\n')
        elif user_input2 == 2:
            print(*flight2.get_flight_passengers(), sep = '\n')
        elif user_input2 == 3:
            print(*flight3.get_flight_passengers(), sep = '\n')
        elif user_input2 == 4:
            print(*flight4.get_flight_passengers(), sep = '\n')
        else:
            print('Flight number is not valid')

    elif user_input == '3':
        user_input3 = int(input('Which flight would you like to add a passenger to? Type the flight number \n'))
        if user_input3 == 1:
            flight1.create_passenger()
            print(*flight1.get_flight_passengers(), sep = '\n')
        elif user_input3 == 2:
            flight2.create_passenger()
            print(*flight2.get_flight_passengers(), sep = '\n')
        elif user_input3 == 3:
            flight3.create_passenger()
            print(*flight3.get_flight_passengers(), sep ='\n')
        elif user_input3 == 4:
            flight4.create_passenger()
            print(*flight4.get_flight_passengers(), sep ='\n')
        else:
            print('Flight number is not valid')
    user_input = input('What would you like to do now? \nType 1 to list flights. \nType 2 to list all passengers on a flight. \nType 3 to add a new passenger to a flight. \nType exit to exit')
else:
    print('You have exited the the database')