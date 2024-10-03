# lib/helpers.py

from models.client import Client
from models.trailer import Trailer

def add_spacing():
    spacing = "-----------------------------"
    print(spacing)

def create_db_tables():
    Client.create_table()
    Trailer.create_table()

def exit_program():
    print("Program closed, goodbye!")
    exit()

def invalid_input_message():
    print("Invalid input. Please try again.")

def print_list(lst):
    for item in lst:
        if isinstance(item, Client):
            show_client_info(item)
        elif isinstance(item, Trailer):
            show_trailer_info(item)
        else:
            print("Error: items in list are not valid input")

def is_empty(lst):
    return len(lst) == 0

def show_client_info(client):
    print(f"Client #: {client.id}")
    print(f"Client Name: {client.first_name} {client.last_name}")
    print(f"Phone Number: {client.phone_number}")

def list_clients(clients=None):
    if clients == None:
        clients = Client.get_all()
        list_name = "Clients List:"
    else:
        list_name = "Search Results:"
    print(list_name)
    print_list(clients)

def select_client_by_number(choice):
    try:
        client = Client.find_by_id(choice)
        show_client_info(client)
        return client
    except:
        print(f"Error: no client found for {choice}")

def update_client(client):
    print("HINT: first name as 'first_name', last name as 'last_name', or phone number as 'phone_number'")
    attribute = input("Enter the client detail to update: ")
    if attribute == "first_name" or attribute == "last_name" or attribute == "phone_number":
        new_value = input("Enter the new name or phone number: ")
        try:  
            setattr(client, attribute, new_value)
            client.update()
            print("Succesfully updated!")
            show_client_info(client)
        except Exception as exc:
            print(f"Error: ", exc)
    else:
        print("Seems you had a typo typing in the client detail to update. Please try again.")
        
def delete_client(client):
    print("""
    Are you sure you want to delete this client?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        client.delete()
        print(f"Client: {client.first_name} {client.last_name} succesfully deleted")
    elif _input == "no":
        print("Client NOT deleted")
        show_client_info(client)
    else:
        invalid_input_message()

def add_client():
    print("HINT: Capitalize first letter of each name and enter phone number with XXX-XXX-XXXX format.")
    first_name = input("Enter the new client's first name: ")
    last_name = input("Enter the new client's last name: ")
    phone_number = input("Enter the new client's phone number: ")
    try:
        new_client = Client.create(first_name, last_name, phone_number)
        print("Client successfully added!")
        show_client_info(new_client)
    except Exception as exc:
        print("Error: ", exc)

def search_for_client():
        print("Capitalize first letter of each name and enter phone number with XXX-XXX-XXXX format.")
        print("HINT: To skip entry leave blank and press enter.")
        first_name = input("Enter client's first name: ")
        last_name = input("Enter client's last name: ")
        phone_number = input("Enter client's phone number: ")

        if not first_name and not last_name and not phone_number:
            print("No clients found. At least one field must not be empty.")
        elif first_name or last_name or phone_number:
            clients = Client.get_all()
            results = []
            for client in clients:
                if (not first_name or client.first_name == first_name) and \
                    (not last_name or client.last_name == last_name) and \
                    (not phone_number or client.phone_number == phone_number):
                    results.append(client)
            if results:
                return results
            else:
                print(f"Error: Check spelling or phone number format. No client found for {first_name} {last_name} {phone_number}")

def show_trailer_info(trailer):
    print(f"Trailer #: {trailer.id}") 
    if trailer.client_renting_trailer:
        select_client_by_number(trailer.client_renting_trailer)
    else:
        print("Client Renting Trailer: Nobody")

def list_trailers(condition=None):
    trailer_list = []
    if condition:
        [trailer_list.append(trailer) for trailer in Trailer.get_all() if condition(trailer)]
        return trailer_list
    else:
        [trailer_list.append(trailer) for trailer in Trailer.get_all()]
        return trailer_list

def search_for_trailer():
    trailer_number = input("Type in trailer number: ")
    if trailer_number:
        if (trailer := Trailer.find_by_id(int(trailer_number))):
            show_trailer_info(trailer)
            return trailer
        else:
            print(f"Error: No trailer found matching {trailer_number} number.")
    else:
        invalid_input_message()

def check_for_exisiting_client(first_name, last_name, phone_number):
    existing_client = None
    for client in Client.get_all():
        if client.first_name == first_name and client.last_name == last_name and client.phone_number == phone_number:
            existing_client = client
    return existing_client

def change_client_from_trailer(trailer):
    print("Enter the client's information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")

    existing_client = check_for_exisiting_client(first_name, last_name, phone_number)

    if existing_client:
        try:
            setattr(trailer, "client_renting_trailer", existing_client.id)
            setattr(trailer, "available", trailer.available)
            trailer.update()
            print("Succesfully updated!")
            show_trailer_info(trailer)
        except Exception as exc:
            print(f"Error: ", exc)
    else:
        print(f"No client found matching {first_name} {last_name} {phone_number}")


def remove_client_from_trailer(trailer):
    try:
        setattr(trailer, "client_renting_trailer", None)
        setattr(trailer, "available", trailer.available)
        trailer.update()
        print("Succesfully updated!")
        show_trailer_info(trailer)
    except Exception as exc:
        print(f"Error: ", exc)


def delete_trailer(trailer):
    print("""
    Are you sure you want to delete this trailer?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        trailer.delete()
        print(f"Trailer succesfully deleted")
    elif _input == "no":
        print("Trailer NOT deleted")
        show_trailer_info(trailer)
    else:
        invalid_input_message()

def add_trailer():
    try:
        new_trailer = Trailer.create()
        print("Trailer successfully added!")
        show_trailer_info(new_trailer)
    except Exception as exc:
        print("Error: ", exc)

#Compare Client id with trailer client_renting_trailer number and return all matching trailers
    #Step 1: Grab id of client
def filter_trailers_by_client(client):
    empty_trailer_list = []
    for trailer in Trailer.get_all():
        if client.id == trailer.client_renting_trailer:
            empty_trailer_list.append(trailer)
    return empty_trailer_list

def create_trailer_with_client(client):
    new_trailer = Trailer.create()
    setattr(new_trailer, "client_renting_trailer", client.id)
    new_trailer.update()
    show_trailer_info(new_trailer)    