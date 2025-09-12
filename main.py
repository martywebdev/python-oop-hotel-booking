# import csv
import pandas as pd

df = pd.read_csv('hotels.csv')
# with open('hotels.csv', 'r', newline='', encoding='utf-8') as f:
#     hotels = csv.DictReader(f)


class Hotel:
    def __init__(self, hotel_id):
        # store it as an attribute
        # self.data = df.loc[df['id'] == int(hotel_id)].iloc[0]
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df['id'] == int(self.hotel_id), 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        # return  self.data['available'] == 'yes'
        return df.loc[df['id'] == int(self.hotel_id), 'available'].squeeze() == 'yes'


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        row = df.loc[df['id'] == int(
            self.hotel_object.hotel_id)].iloc[0]
        content = f'{self.customer_name} on {row['name']}'
        return content


while True:
    print(df)
    try:

        hotel_id = input("Enter the id of the hotel: ")
        if hotel_id == 'q':
            break
        hotel = Hotel(hotel_id)

        if hotel.available():
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print('Not available')
    except (IndexError, ValueError) as e:
        print(e)
        