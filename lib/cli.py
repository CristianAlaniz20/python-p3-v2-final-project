# lib/cli.py

from helpers import (
    create_db_tables,
    exit_program,
    list_clients,
    select_client_by_number,
    update_client,
    delete_client,
    add_client,
    search_for_client,
    search_for_trailer,
    update_trailer_client,
    delete_trailer,
    list_trailers,
    add_trailer,
    is_empty,
    print_list
)

def invalid_input_message():
    print("Invalid input. Please try again.")

def main():
    create_db_tables()
    while True:
        main_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "vc":
            view_client_menu()
        elif choice == "sc":
            search_client_menu()
        elif choice == "vt":
            list_trailers_menu()
        elif choice == "st":
            search_for_trailer_menu()
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
            list_clients(filtered_clients)
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

def search_for_trailer_verification_menu():
    while True:
        search_for_trailer_verification_options()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "y":
            search_for_trailer_menu()
        else:
            invalid_input_message()

def search_for_trailer_menu():
    (searched_trailer := search_for_trailer())
    if searched_trailer:
        while True:
            search_for_trailer_options()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif choice == "u":
                update_trailer_client(searched_trailer)
            elif choice == "d":
                delete_trailer(searched_trailer)
                main()
            else:
                invalid_input_message()

#Should A. Give option to select type of list. / B. Be able to select a trailer from the list. / C. Give action options for trailer chosen.
def list_trailers_menu():
    while True:
        #If no trailers in db, redirect to empty_trailer_list_menu
        trailer_list = list_trailers()
        if is_empty(trailer_list):
            empty_trailer_list_menu()
        #Else execute code underneath
        else:
            list_trailers_options()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif choice == "all":
                print_list(trailer_list)
                search_for_trailer_verification_menu()
            elif choice == "rented":
                is_rented = lambda trailer: trailer.client_renting_trailer is not None
                filtered_trailer_list = list_trailers(is_rented)
                if is_empty(filtered_trailer_list):
                    print("There are no trailers currently being rented")
                    list_trailers_menu()
                else:
                    print_list(filtered_trailer_list)
                    search_for_trailer_verification_menu()
            elif choice == "available":
                is_available = lambda trailer: trailer.available is not False
                filtered_trailer_list = list_trailers(is_available)
                if is_empty(filtered_trailer_list):
                    print("There no trailers currently available")
                    list_trailers_menu()
                else:
                    print_list(filtered_trailer_list)
                    search_for_trailer_verification_menu()
            elif choice == "add":
                add_trailer()
            else:
                invalid_input_message()

def empty_trailer_list_menu():
    while True:
        empty_trailer_list_options()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "a":
            add_trailer()
        else:
            invalid_input_message()

#Issues
    #If list is empty, show message to say that
    #Add previous option


def main_menu():
    print("Welcome, please select an option:")
    print("Enter 'e' to exit the program")
    print("Enter 'vc' to view list of clients")
    print("Enter 'sc' to search for a client")
    print("Enter 'vt' to view list of trailers")
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

def search_for_trailer_verification_options():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'y' if you want to search for a trailer")

def search_for_trailer_options():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'e' to exit the program")
    print("Enter 'u' to update client renting this trailer")
    print("Enter 'd' to delete this trailer")

def list_trailers_options():
    print("Enter 'p' to go to the previous menu")
    print("Enter 'e' to exit the program")
    print("Enter 'all' to view a list of all trailers")
    print("Enter 'rented' to view a list of trailers being rented")
    print("Enter 'available' to view a list of trailers available")
    print("Enter 'add' to add a trailer")

def empty_trailer_list_options():
    print("HINT: It appears there are no trailers. Please select an option:")
    print("Enter 'p' to go to the previous menu")
    print("Enter 'a' to add a trailer")

if __name__ == "__main__":
    main()
