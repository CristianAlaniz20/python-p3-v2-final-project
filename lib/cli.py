# lib/cli.py
import ipdb

from helpers import (
    exit_program,
    list_clients,
    select_client_by_enumerate_number,
    update_client,
    delete_client
)

def invalid_input_message():
    print("invalid input")

def main():
    while True:
        print("Program started!")
        main_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "v":
            view_client_menu()
        elif choice == "s":
            search_client_by_name()
        else:
            invalid_input_message()

def view_client_menu():
    list_clients()
    view_all_clients_menu()
    choice = input("> ")
    if choice == "exit" or choice == "e":
            exit_program()
    else:
        if select_client_by_enumerate_number(choice):
            print(select_client_by_enumerate_number(choice))
            client_menu()
        else:
            print("Hi from inside else statement")

def client_menu():
    client_view_menu()
    choice = input("> ")
    if choice == "e":
            exit_program()
    elif choice == "u":
        update_client()
    elif choice == "d":
        delete_client()
    elif choice == "v":
        pass
    else:
        invalid_input_message()
        client_menu()

def main_menu():
    print("Please select an option:")
    print("Enter 'exit' or 'e' to exit the program")
    print("Enter 'view' or 'v' to view all clients")
    print("Enter 'select' or 's' to search for a client")

def view_all_clients_menu():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'e' to exit the program")
    print("Or select a client by entering their corresponding number")

def client_view_menu():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'e' to exit the program")
    print("Enter 'u' to update client details")
    print("Enter 'd' to delete this client")
    print("Enter 'v' to view all the trailers this client has rented")

if __name__ == "__main__":
    main()
