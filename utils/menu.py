from __future__ import print_function
import sys
import os


# hacky input func to handle Python 2
if sys.version_info[0] < 3:
    from compat import input


# keep the clutter down
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')


# grab email/phone, pwd, group id
def get_data():
    data={}
    print("Welcome to Facebook Admin Tools bulk post approval/\n"
          "deletion tool.")
    print()
    email = input("What is your Facebook email or phone number?")
    data['email'] = email
    clear_term()
    print("Thank you")
    print()
    password = input("What is your Facebook password?\n"
                     "It will not be stored.")
    data['password'] = password
    clear_term()
    print("Thank you")
    print()
    url = input("What is the id of your group?\n"
                "ex: facebook.com/groups/999999999999999/\n"
                "The id would just be the numbers after ...groups/")
    data['url'] = "http://www.facebook.com/groups/{}".format(url)

    return data


def login(browser, data):
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(data['email'])
    pass_input = browser.find_element_by_name('pass')
    pass_input.send_keys(data['password'])
    pass_input.submit()

    return print("Login Successful")