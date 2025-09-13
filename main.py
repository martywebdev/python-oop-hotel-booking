# import csv
from numpy import number
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


class CreditCard:

    def __init__(self, credit_number, cards_file="cards.csv"):
        self.credit_number = credit_number
        self.df = pd.read_csv(cards_file, dtype=str).to_dict(
            orient='records')  # list of objects structure all string

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.credit_number,
                     "expiration": expiration, "holder": holder, "cvc": cvc}
        return card_data in self.df


while True:
    print(df)
    try:

        hotel_id = input("Enter the id of the hotel: ")
        if hotel_id == 'q':
            break
        hotel = Hotel(hotel_id)

        if hotel.available():
            # get user's credit card info

            credit_card_input = input("Enter credit card number: ")
            credit_card = CreditCard(
                credit_number=credit_card_input)

            # print(credit_card.__dict__) show object properties
            # print(dir(CreditCard)) show attributes

            # print(credit_card.validate(expiration="12/26", holder='JOHN SMITH', cvc="123"))

            if credit_card.validate(expiration="12/26", holder='JOHN SMITH', cvc="123"):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                print(reservation_ticket.generate())
            else:
                print('An error occured on your credit card ')
        else:
            print('Not available')
    except (IndexError, ValueError) as e:
        print(e)
