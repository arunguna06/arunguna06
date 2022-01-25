import pymongo
import re
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://arunsp10206:dare2win@cluster0.iefl6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("Login_records")
records = db.usernameandpassword
user_choice = int(input("Please enter- 1 to Register, 2 to Login, 3 to find your password  "))


def check_email_address(address):
  is_valid = re.search("^\w+@\w+.\w+$", address)
  if is_valid:
      print("The given username is valid")
      return address
  else:
    print('It looks that provided mail is not in correct format. \n'
          'Please make sure that you have "@" and "." in your address \n'
          'and the length of your mail is at least 6 characters long')
    return address


def check_password(password):
    is_valid = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password)
    if is_valid:
        print("The given password is valid")
        return password
    else:
        print('It looks that provided password is not in correct format. \n'
                'Please make sure that you have "@" and "." in your address \n'
                'and the length of your mail is at least 6 characters long')
        return password


if user_choice == 1:
    Username_Email = input("Please enter your Username or Email address- ")
    print(check_email_address(Username_Email))
    Password = input("Please choose a password")
    print(check_password(Password))
    Login_id = {"_id": Username_Email,
                "User Name": Username_Email,
                "Password": Password}
    print(Login_id)
    records.insert_one(Login_id)

elif user_choice == 2:
    user_name = input("Please enter your user name")
    my_query = {"_id":user_name}
    for i in records.find(my_query):
        passs = i["Password"]
        password_1 = input("Please enter the password ")
        if password_1 == passs:
            print("Welcome back {0}".format(user_name))

elif user_choice == 3:
    user_input = input("Please enter your user name without mistakes....")
    my_search = {"_id":user_input}
    for x in records.find(my_search):
        user_name = x["User Name"]
        password = x["Password"]
        if user_input in user_name:
            print("The username is {0} and the password is {1}".format(user_name, password))
            print("Please do not forget next time......")