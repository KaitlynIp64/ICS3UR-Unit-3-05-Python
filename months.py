#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program identifies months


def main():
    # this function checks the month

    # input
    month_num = input("Enter month as a number(ex: 1, 2, ...): ")
    print("")

    # process & output
    match month_num:
        case "1":
            print("This month is: January.")
        case "2":
            print("This month is: February.")
        case "3":
            print("This month is: March.")
        case "4":
            print("This month is: April.")
        case "5":
            print("This month is: May.")
        case "6":
            print("This month is: June.")
        case "7":
            print("This month is: July.")
        case "8":
            print("This month is: August.")
        case "9":
            print("This month is: September.")
        case "10":
            print("This month is: October.")
        case "11":
            print("This month is: November.")
        case "12":
            print("This month is: December.")
        case _:
            print("Invalid month.")


if __name__ == "__main__":
    main()
