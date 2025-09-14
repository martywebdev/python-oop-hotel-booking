from abc import ABC, abstractmethod
import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})

print(df)


class Hotel:
    # class variables
    watermarks = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == int(self.hotel_id), 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        selection = df.loc[df['id'] == int(self.hotel_id), 'available']
        if selection.empty:
            return False  # hotel not found
        return selection.iloc[0] == 'yes'

    # class methods are not related to instance
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # this are dunder methods native to python you can overwrite it
    def __eq__(self, hotel):  # eq is checking if 2 values are equal
        return self.hotel_id == hotel.hotel_id

    def __str__(self):
        return 'This is a test'

# abstract methods


class Ticket(ABC):  # ABC is module abstract base class

    @abstractmethod
    def generate(self):  # this method is mandatory now to the child class
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        row = df.loc[df['id'] == self.hotel_object.hotel_id, "name"].squeeze()
        content = f'''
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel Name:{row}'''
        return content

    @property  # serves as a property of the class
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod  # this are helper methods
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    pass
    # def generate(self):
    #     return "updated shit"


if __name__ == '__main__':
    hotel1 = Hotel(hotel_id="134")
    hotel2 = Hotel(hotel_id="188")

    # print(hotel2.name)
    # print(hotel1.get_hotel_count(df))
    # print(Hotel.get_hotel_count(df))

    # ticket = ReservationTicket('marty umlas', hotel1)

    # print(ticket.the_customer_name)  # this will behave like propety
    # print(ticket.generate())

    # CONVERTED = ReservationTicket.convert(123)

    # print(CONVERTED)

    ticket = ReservationTicket(customer_name='Kulapo', hotel_object=hotel1)
    print(ticket.generate())
    df = DigitalTicket()
    # dg = DigitalTicket('kulapo', hotel1)
    # print(dg.generate())
