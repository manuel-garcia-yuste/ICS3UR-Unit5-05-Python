#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program print an address formatted nicely


def mailing_address(first_name, last_name, address, city,
                    province, postal_code, apartment=None):

    # Process
    if apartment is not None:
        post_address = first_name + " " + last_name + "\n" + apartment + \
            " " + address + "\n" + city + " " + province + "  " + postal_code
    else:
        post_address = first_name + " " + last_name + "\n" + address + "\n" + \
            city + " " + province + " " + postal_code

    return post_address


def main():
    # This function gets the details of the person recieving MAIL

    # Variables
    apartment = None

    # Input
    first_name = input("Enter the recipient's first name: ")
    last_name = input("Enter the recipient's last name: ")
    address = input("Enter the recipient's address : ")
    apt_checker = input("Does the recipient live in an apartment (yes/no): ")
    if apt_checker.upper() == "Y" or apt_checker.upper() == "YES":
        apartment = input("Enter the recipient's apartment number: ")
    city = input("Enter the recipient's city: ")
    province = input("Enter the recipient's province or territory: ")
    postal_code = input("Enter the recipient's postal code: ")

    # Process
    if apartment is not None:
        post_address = mailing_address(first_name, last_name, address,
                                       city, province,
                                       postal_code, apartment)
    else:
        post_address = mailing_address(first_name, last_name, address,
                                       city, province,
                                       postal_code)

    # Output
    print("")
    print(post_address)


if __name__ == "__main__":
    main()
