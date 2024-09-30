# lib/helpers.py

from models.client import Client
from models.trailer import Trailer

spacing = "-----------------------------"

def create_db_tables():
    Client.create_table()
    Trailer.create_table()

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
    print("HINT: Capitalize first letter of each name and enter phone number with XXX-XXX-XXXX format.")
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

def show_trailer_info(trailer):
    print(f"Trailer #: {trailer.id}") 
    if trailer.client_renting_trailer:
        select_client_by_number(trailer.client_renting_trailer)
    else:
        print("Client Renting Trailer: Nobody")
    print(f"Available: {trailer.available}")
    print(spacing)

def list_trailers(condition=None):
    if condition:
        return [show_trailer_info(trailer) for trailer in Trailer.get_all() if condition(trailer)]
    else:
        return [show_trailer_info(trailer) for trailer in Trailer.get_all()]

def search_for_trailer():
    print(spacing)
    trailer_number = input("Type in trailer number: ")
    if trailer_number:
        if (trailer := Trailer.find_by_id(int(trailer_number))):
            show_trailer_info(trailer)
            return trailer
        else:
            print(f"Error: No trailer found matching {trailer_number} number.")
            print(spacing)
    else:
        print("Error: Must enter a trailer number.")
        print(spacing)

#If client already exists, assign client to trailer
#Else 1. Say client does not exist and 2. Ask/give option to create the new client with information that was already put in.
def update_trailer_client(trailer):
    print("""
    If you would like change trailer client to another client enter: change
    If you would like the trailer to have NO client enter: remove
    """)
    _input = input("> ")
    if _input == "remove":
        try:
            setattr(trailer, "client_renting_trailer", None)
            setattr(trailer, "available", trailer.available)
            trailer.update()
            print("Succesfully updated!")
            show_trailer_info(trailer)
            print(spacing)
        except Exception as exc:
            print(f"Error: ", exc)
            print(spacing)
    elif _input == "change":
        print("Enter the rentor's information:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        print(spacing)
        #Search for client with fullmatching first name, last name, and phone number
        existing_client = None
        clients = Client.get_all()
        for client in clients:
            if client.first_name == first_name and client.last_name == last_name and client.phone_number == phone_number:
                existing_client = client

        if existing_client:
            try:
                setattr(trailer, "client_renting_trailer", existing_client.id)
                setattr(trailer, "available", trailer.available)
                trailer.update()
                print("Succesfully updated!")
                show_trailer_info(trailer)
                print(spacing)
            except Exception as exc:
                print(f"Error: ", exc)
                print(spacing)
        else:
            print(f"No client found matching {first_name} {last_name} {phone_number}")
            print(spacing)
    else:
        print("Invalid input. Please try again.")
        print(spacing)

def delete_trailer(trailer):
    print("""
    Are you sure you want to delete this trailer?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        trailer.delete()
        print(f"Trailer succesfully deleted")
    elif _input == "no":
        print(spacing)
        print("Trailer NOT deleted")
        show_trailer_info(trailer)
        print(spacing)
    else:
        print("Invalid input. Please try again.")
        print(spacing)

def add_trailer():
    try:
        new_trailer = Trailer.create()
        print(spacing)
        print("Trailer successfully added!")
        print(f"Trailer# {new_trailer.id}")
        show_trailer_info(new_trailer)
        print(spacing)
    except Exception as exc:
        print("Error: ", exc)
        print(spacing)

#CLIENTS
    #After search client results, even if client is not on the results list, if id entered, client is selected. FIX bug 

#TRAILERS
    #Attempt to assign client to trailer
    #If client does not exist, give message that client does not exist, THEN
    #Give option to create new Client
    #Give client option to assign a trailer to them

#Test Commit for new machine
    #Hello From Macbook