from plane_class import *
from passenger_class import *

class Flight(Plane):
    def __init__(self,plane_id,flight_number,flight_day,flight_time, destination, plane_model = 'Boeing 777X'):
        super().__init__(plane_id,plane_model)
        self.flight_number = flight_number
        self.flight_day = flight_day
        self.flight_time = flight_time
        self.destination = destination
        self.__passengers_list = []

    def flight_details(self):
        return f"Flight {self.flight_number} leaves on {self.flight_day} at {self.flight_time} to {self.destination}"


    def add_passengers(self, *passengers):
        for passenger in passengers:
            self.__passengers_list.append(passenger.name_and_passport())

    def get_flight_passengers(self): #getter
        return self.__passengers_list

    def create_passenger(self):
        f_name = input('First Name?').capitalize()
        l_name = input('Last Name?').capitalize()
        passport_number = input('Passport Number?')
        input_passenger = Passenger(self.plane_id,self.flight_number,self.flight_day,self.flight_time,self.destination, f_name, l_name, passport_number)
        self.add_passengers(input_passenger)


