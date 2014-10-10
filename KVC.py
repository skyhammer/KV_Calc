__author__ = 'David Cartwright'

import os


def menu_choices():
    """
    Starts by clearing the screen, and the prints a menu of available options for the user to select.
    User must press 'q' or 'Q' to exit the program.
    """

    #This line needs to be commented out when testing. It only works when run from the terminal.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("KV Calculator")
    print("*"*13)
    print("\nPlease make a choice from the following options:\n")
    print("[1] Compute Average Flow Times")
    print("[2] Calculate New Tube Constant")
    print("[3] Reverse-Calculate KV")
    print("[4] Calculate Difference From Known KV Result")
    print("[Q] Quit")

    choice = input("\nSelection: ")

    return choice


def average_flow():
    """
    This function will ask for the number of flow times that are needed to be entered, and then will ask for the
    flow times. If the number of flow times is equal to a number less than or equal to 1, a message is shown to inform
    the user that a number greater than 1 is needed to calculate an average
    """

    # Variable declarations
    flow_times = 0
    i = 0

    number_of_flows = int(input("How many flow times do you wish to enter? "))

    while number_of_flows <= 1:
        print("You need to enter a positive number that is greater than 1 to calculate an average.")
        number_of_flows = int(input("How many flow times do you wish to enter? "))

    while i < number_of_flows:
        time = float(input("Please enter the flow time [{}]: ".format(i+1)))
        flow_times += time
        i += 1

    return round(float(flow_times / number_of_flows), 5)


def tube_constant():
    """
    This function will calculate the tube constant after providing the average flow time and the expected KV result
    """
    average_flow_time = average_flow()
    expected_kv = float(input("What is the expected KV result? "))
    return round(float(expected_kv / average_flow_time), 5)


def reverse_calc_kv():
    """
    This function will reverse calculate the KV result when provided with the corrected flow times and the new constant value.
    """
    average_flow_time = average_flow()
    tube_constant = float(input("What is the tube constant to be used? "))

    return round(float(average_flow_time * tube_constant), 4)


def kv_difference():
    """
    This function will calculate the difference, as a percentage, of the measured KV valve and the expected KV value
    """
    measured_kv = float(input("What is the measured KV result? "))
    expected_kv = float(input("What is the expected KV result? "))

    return round(float(abs(expected_kv - measured_kv) / expected_kv * 100), 2)


selection = menu_choices()
while selection != "q" or selection != "Q":
    if selection == "1":
        print("\nThe average flow time is: {} seconds".format(average_flow()))
        input("\nPress enter key to continue...")
    elif selection == "2":
        print("\nThe calculated tube constant is: {}".format(tube_constant()))
        input("\nPress enter key to continue...")
    elif selection == "3":
        print("\nThe calculated KV result is: {}".format(reverse_calc_kv()))
        input("\nPress enter key to continue...")
    elif selection == "4":
        print("\nThe difference between the measured and expected KV is: {}%".format(kv_difference()))
        input("\nPress enter key to continue...")
    elif selection == "q" or selection =="Q":
        print(selection)
        break
    else:
        print("{} is not a valid selection".format(selection))

    selection = menu_choices()



