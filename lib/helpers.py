# lib/helpers.py

from models.client import Client
from models.trailer import Trailer

spacing = "-----------------------------"

def exit_program():
    print("Program closed, goodbye!")
    exit()

def show_client_info(client):
    print(f"Client Name: {client.first_name} {client.last_name}")
    print(f"Phone Number: {client.phone_number}")

def list_clients(clients=None):
    if clients == None:
        clients = Client.get_all()
        list_name = "Clients List:"
    else:
        list_name = "Search Results:"
    print(spacing)
    print(list_name)
    for client in clients:
        print(f"{client.id}. {client.first_name} {client.last_name}")
    print(spacing)

def select_client_by_number(choice):
    try:
        client = Client.find_by_id(choice)
        print(spacing)
        show_client_info(client)
        print(spacing)
        return client
    except:
        print(f"Error: no client found for {choice}")
        print(spacing)

def update_client(client):
    print("HINT: first name as 'first_name', last name as 'last_name', or phone number as 'phone_number'")
    attribute = input("Enter the client detail to update: ")
    if attribute == "first_name" or attribute == "last_name" or attribute == "phone_number":
        new_value = input("Enter the new name or phone number: ")
        try:  
            setattr(client, attribute, new_value)
            client.update()
            print(spacing)
            print("Succesfully updated!")
            show_client_info(client)
            print(spacing)
        except Exception as exc:
            print(f"Error: ", exc)
            print(spacing)
    else:
        print("Seems you had a typo typing in the client detail to update. Please try again.")
        print(spacing)
        
def delete_client(client):
    print("""
    Are you sure you want to delete this client?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        client.delete()
        print(f"Client: {client.first_name} {client.last_name} succesfully deleted")
    elif _input == "no":
        print(spacing)
        print("Client NOT deleted")
        show_client_info(client)
        print(spacing)
    else:
        print("Invalid input. Please try again.")
        print(spacing)

def add_client():
    first_name = input("Enter the new client's first name: ")
    last_name = input("Enter the new client's last name: ")
    phone_number = input("Enter the new client's phone number: ")
    try:
        new_client = Client.create(first_name, last_name, phone_number)
        print(spacing)
        print("Client successfully added!")
        show_client_info(new_client)
        print(spacing)
    except Exception as exc:
        print("Error: ", exc)
        print(spacing)

def search_for_client():
    print(spacing)
    print("Capitalize first letter of each name and enter phone number with XXX-XXX-XXXX format.")
    print("HINT: To skip entry leave blank and press enter.")
    first_name = input("Enter client's first name: ")
    last_name = input("Enter client's last name: ")
    phone_number = input("Enter client's phone number: ")

    if not first_name and not last_name and not phone_number:
            print("No clients found. At least one field must not be empty.")
            print(spacing)
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
            print(spacing)

def list_trailers():
    pass

def search_for_trailer():
    print(spacing)
    trailer_number = input("Type in trailer number: ")
    if trailer_number:
        trailers = Trailer.get_all()
        for trailer in trailers:
            if trailer.id == trailer_number:
                show_trailer_info(trailer)
            else:
                print(f"Error: No trailer found matching {trailer_number} number.")
    else:
        print("Error: Must enter a trailer number.")