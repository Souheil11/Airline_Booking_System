import random
import json
from datetime import datetime


class Passenger:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_passenger_details():
        """function to get values name, phone, email from user """
        name = input("Enter Passenger name: ")
        pn = True
        while pn is True:
            try:
                phone_number = int(input("Enter your Phone number: "))
                if type (phone_number) is int:
                    pn = False
                    break
                else:
                    raise ValueError   
            except ValueError:
                print("Only digits allowed for phone number field")
                
                
        email = input("Enter your Email address: ")
        return Passenger(name, phone_number, email)


    def get_fqtv_number():
        """function to get Frequent traveller card number from user"""
        fqtv_check = True
        while fqtv_check is True:
            try:
                fqtv = int(input("Enter your mileage card number: "))
                if type(fqtv) is int and len(str(fqtv)) == 16:
                    fqtv_check = False
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Wrong or missing input! Enter your 16 digits mileage card number")
                fqtv_check = True
        return fqtv

class Profile(Passenger):
    def __init__(self, address):
        Passenger.name
        Passenger.phone_number
        Passenger.email
        self.address = address

    def get_address():
        """function to get address from user"""
        address = input("Enter your home address: ")
        return address
        
    def generate_frequent_number():
        """function to generate new card number"""
        fqtv = []
        for item in range(16):
            fqtv.append(random.randint(0,9))
        fqtv = "".join(map(str, fqtv))
        return fqtv
    
    def create_profile():
        """This function prompts user whether he holds a mileage card, if yes he is asked to enter number, if no the function inherits values name, phone, email from class 'Passenger', adds value addres and generates card number """
        while True:
            try:
                choice = input("Do you have already a mileage card ? enter 'y' to enter the number or 'n' to complete your profile and generate a number.\nYou may press 's' key to skip the mileage program enrollment: ")
                if choice.lower() == "y":
                    fqtv = Passenger.get_fqtv_number()
                    return fqtv
                elif choice.lower() == 'n':
                    address = Profile.get_address()
                    fqtv = Profile.generate_frequent_number()
                    print(f"Your Frequent Traveller Card number is: {fqtv}")
                    data = {
                    'name': pax.name,
                    'mileage_card_number': fqtv,
                    'address' : address,
                    'phone_number': pax.phone_number,
                    'email': pax.email,
                    }
                    filename = 'database.json'
                    with open(filename, 'w') as f:
                        json.dump(data, f)
                    return fqtv
                elif choice.lower() == "s":
                    fqtv = "No mileage card available"
                    return fqtv
                else:
                    raise ValueError
            except ValueError:
                    print("\nWrong input. Please check your entry!")


def save_booking():
    """Export booking to external file"""
    check_saving_input = True
    while check_saving_input is True:
        try:
            save = input("Do you want to export the booking summary into a file (y/n)? ")
            if save.lower() == "y":
                with open("Booking Confirmation.txt", "w") as file:
                    file.write(booking_summary)
                print("Booking summary exported successfully.")
                check_saving_input = False
            elif save.lower() == "n":
                print("Booking summary not exported")
                check_saving_input = False
            else:
                raise ValueError
                
                
        except ValueError:
            print("Check your input!")

def seat_selection():
    """Function for seat selection"""
    seat =""
    advance_seat = input("Do you want to select your seat in advance (additional fee of 6000 Yen will be applied) (y/n)? ")
    if advance_seat.lower() == "y":
        flights[destination]["price"] += 6000
        print(f"Seat selection fee added. Total price: {flights[destination]['price']} Yen")
        while True:
            try:
                row = int(input("Enter the row number (1-26): "))
                seat = input("Enter the seat letter (A-F): ")
            
                if row > 0 and row <= 26 and seat.upper() in ["A", "B", "C", "D","E","F"]:
                    seat = f"{row}{seat.upper()}"
                    print(f"Seat {seat} successfully selected.")
                    break
                else:
                    raise ValueError
            except ValueError: 
                print("Seat not on seatmap, please check your entry")
    elif advance_seat.lower() == "n":
        seat = "No seat preselection - Seat will be assigned at the day of departure"
    else:
        print("Please check your entry!")
        seat_selection()
    return seat



# Dictionary of available flight destinations with prices
flights = {1: {"destination": "New York", "price": 120000},
           2: {"destination": "London", "price": 164000},
           3: {"destination": "Paris", "price": 149000}}

# Print list of destinations and ask user for a selection
def print_flights():
    """function to print list of flights from dictionary 'flights' """
    print("Available flight destinations:")
    for key, value in flights.items():
        print(f"{key}. {value['destination']} ({value['price']} Yen)")
print_flights()

# Validate the user's choice
while True:
    
    try: 
        destination = int(input("Select the number of the destination you want to travel to: "))
       
        if destination in flights:
            print(f"You have selected flight to {flights[destination]['destination']} ({flights[destination]['price']} Yen)")
            break    
        else:
            raise ValueError
    except ValueError:
            print("\nInvalid selection, please check your entry")
            print_flights()


seat = seat_selection()
pax = Passenger.get_passenger_details()
fqtv = Profile.create_profile()
today= datetime.now()
booking_summary = f"\n***** Booking summary *****\nPassenger name: {pax.name.title()}\nFrequent Traveller card number: {fqtv}\nPhone number: {pax.phone_number}\nEmail address: {pax.email}\nFlight Destination: {flights[destination]['destination']}\nTotal price: {flights[destination]['price']} Yen\nSeat: {seat}\n\nBooking created on {today.month}/{today.day}/{today.year}\n"
print(booking_summary)

save_booking()