# lib/cli.py

from helpers import (
    exit_program,
    list_clients,
    select_client_by_number,
    update_client,
    delete_client,
    add_client,
    search_for_client,
    search_for_trailer
)

def invalid_input_message():
    print("Invalid input. Please try again.")

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "v":
            view_client_menu()
        elif choice == "sc":
            search_client_menu()
        elif choice == "st":
            search_for_trailer()
        else:
            invalid_input_message()

def view_client_menu(filtered_clients=None):
    list_clients(filtered_clients)
    while True:
        if filtered_clients:
            search_clients_menu()
        else:
            view_all_clients_menu()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "e":
            exit_program()
        elif choice == 'a':
            add_client()
        elif (client := select_client_by_number(choice)):
            client_menu(client)
        else:
            invalid_input_message()
    
def search_client_menu():
    (client_search_results := search_for_client())
    if client_search_results:
        list_clients(client_search_results)
        while True:
            search_clients_menu()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif (client := select_client_by_number(choice)):
                client_menu(client, client_search_results)
            else:
                invalid_input_message()

def client_menu(client, filtered_clients=None):
    while True:
        client_view_menu()
        choice = input("> ")
        if choice == "p":
            view_client_menu(filtered_clients)
        elif choice == "e":
            exit_program()
        elif choice == "u":
            update_client(client)
        elif choice == "d":
            delete_client(client)
        elif choice == "v":
            pass
        else:
            invalid_input_message()

def main_menu():
    print("Welcome, please select an option:")
    print("Enter 'e' to exit the program")
    print("Enter 'v' to view all clients")
    print("Enter 'sc' to search for a client")
    print("Enter 'st' to search for a trailer")

def view_all_clients_menu():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'e' to exit the program")
    print("Enter 'a' to add a client")
    print("Or select a client by entering their corresponding number")

def search_clients_menu():
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
