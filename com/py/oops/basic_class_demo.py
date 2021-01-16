class FlightInformation:

    def __init__(self, flight_number):
        self.flight_number = flight_number

    def fetch_flight_details(self):
        print(f'hello welcome aboard on flight : {self.flight_number}')


f1 = FlightInformation('123')
f1.fetch_flight_details()
