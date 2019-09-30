class Passenger():
    def __init__(self,plane_id, flight_number,flight_day,flight_time, destination, f_name,l_name,passport_number,plane_model = 'Boeing 777X'):
        #super().__init__(plane_id,flight_number,flight_day,flight_time, destination, plane_model = 'Boeing 777X')
        self.flight_number = flight_number
        self.flight_day = flight_day
        self.flight_time = flight_time
        self.destination = destination
        self.f_name = f_name
        self.l_name = l_name
        self.passport_number = passport_number

    def name_and_passport(self):
        return f"{self.f_name} {self.l_name} - {self.passport_number}"




