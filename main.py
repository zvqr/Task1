import csv

username = "admin"
password = "123admin123"

inputuser = input("Enter your Username: ")
inputpass = input("Enter your Password: ")

if not (username == inputuser and password == inputpass):
    print("Incorrect Username or Password! Please Try Again. ")
    exit()

file_name = "savedinfo.txt"
file1 = open(file_name, "a+")
file1.close()


def show_main_menu():

    print("\n             |Diary Program| \n" +
          "------------------------------------------\n" +
          "Enter 1 To Display All Of Your Inserted Records\n" +
          "Enter 2 To Insert a New Record\n" +
          "Enter 3 To Delete a Record\n" +
          "Enter 4 To Quit\n------------------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Diary is empty")
        else:
            print(file_contents)
        file1.close()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        '''delete_contact_record()'''
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "4":
        print("Exiting the program")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()


''' def delete_contact_record(): '''


def enter_contact_record():
    first = input('Enter Friends First Name: ')
    first = first.title()
    last = input('Enter Friends Last Name: ')
    last = last.title()
    favoritenumber = input('Enter their favorite number: ')
    hobby = input('Enter their hobby: ')
    favoritecolor = input('Enter their favorite color: ')
    contact = ("[" + first + " " + last + ", " + favoritenumber + ", " + hobby + ", " + favoritecolor + "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print("This person\n " + contact + "has been added successfully!")


show_main_menu()
