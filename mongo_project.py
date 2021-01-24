import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "ciTutorialDB"
COLLECTION = "ciSampleData"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)        
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a Record")
    print("2. Find a Record")
    print("3. Edit a Record")
    print("4. Delete a Record")
    print("5. Exit")

    option = input("Enter an option: ")
    return option


def get_record():
    print("")
    first = input("Enter a first name > ")
    last = input("Enter a last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database!")

    if not doc:
        print("")
        print("Error! No matching results found.")

    return doc


def add_record():
    print("")
    first = input("Enter a first name > ")
    last = input("Enter a last name > ")
    dob = input("Enter a date of birth > ")
    gender = input("Enter a gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter an occupation > ")
    nationality = input("Enter a nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower()
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document successfully inserted!")
    except:
        print("Error accessing the database!")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid input option!")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
