import csv
import os
tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 4},
    {'number': 3, 'seats': 6},
    {'number': 4, 'seats': 8},
    {'number': 5, 'seats': 10},
]

reservations_file = 'reservation_file.csv'


def view_tables(tables):
    for table in tables:
        print(table)

view_tables(tables)

def make_reservation(tables,reservation):
    name = input("Enter your name:") 
    contact = input("Enter your contact number:")
    party_size = int(input("Enter number of people:"))
    date = input("Enter reservation date(YYYY-MM-DD):")
    start_time = input("Enter reservation start time(HH:MM):")
    end_time = input("Enter reservation end time (HH:MM)")

    available_tables = [table for table in tables if table['seats'] >= party_size]
    if not available_tables:
     print("No available tables for your party size.")
     return
    print("available tables")
    for table in available_tables:
       print(f"Table {table['number']} - seats: {table['seats']}")

    #table to reserve from available list
    table_number = int(input("Enter table number to reserve:"))

    if table_number not in [table['number'] for table in available_tables]:
        print("invalid table number.")
        return
    
    new_row = [table_number, name, contact, party_size, date, start_time, end_time]
    file_exists = os.path.isfile(reservations_file)
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
            if not file_exists:
                writer.writerow(["table number", "name", "party size"])
            writer.writerow(new_row)
        print(f"table {table_number} reserved successfully for {name} on {date} from {start_time} to {end_time}.")
    except Exception as e:
        print(f"Error saving reservation:{e}")

    # reservation = {'name': name, 'party_size': party_size}

    # print(f"Table {table_number} reserved successfully for {name}.")

def cancel_reservation(reservations):
    for reservation in reservations:
        print("reservation has been cancelled")
    
def view_reservations(reservations):
    pass

make_reservation(tables,reservations_file)
   