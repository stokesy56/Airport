class Plane():
    def __init__(self,plane_id,plane_model = 'Boeing 777X'):
        self.plane_id = plane_id
        self.plane_model = plane_model
        self.__flights = []

    def add_flight(self, *flights):
        for flight in flights:
            self.__flights.append(flight.flight_details())

    def get_flight_list(self):  # getter
        return self.__flights