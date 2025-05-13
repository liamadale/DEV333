import sqlite3
import pandas as pd

# Check if SQLite is available
def check_sqlite():
    try:
        sqlite3_version = sqlite3.sqlite_version
        print(f"SQLite is available, version: {sqlite3_version}")
    except ImportError:
        print("SQLite is not installed or not available in this Python environment")

# Initialize the database with sample data
def initialize_database():
    # Create a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email_address TEXT NOT NULL UNIQUE,               
        phone_number TEXT NOT NULL,
        street_address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL
    )
    """)
    print("Table created successfully")
    
    # Sample DataFrame
    data = {
        "first_name": ["Diana", "Ethan", "Fiona", "Gavin", "Hannah", "Isaac", "Jasmine", "Kevin", "Lila", "Miles", "Nina", "Oscar", "Paige", "Quentin", "Ruby"],
        "last_name": ["Reynolds", "Sullivan", "Bennett", "Chambers", "Dawson", "Ellis", "Foster", "Gibson", "Hughes", "Ingram", "Jacobs", "Keller", "Lawson", "Morris", "Nash"],
        "email_address": [
            "diana.reynolds@example.com", "ethan.sullivan@example.com", "fiona.bennett@example.com", "gavin.chambers@example.com",
            "hannah.dawson@example.com", "isaac.ellis@example.com", "jasmine.foster@example.com", "kevin.gibson@example.com",
            "lila.hughes@example.com", "miles.ingram@example.com", "nina.jacobs@example.com", "oscar.keller@example.com",
            "paige.lawson@example.com", "quentin.morris@example.com", "ruby.nash@example.com"
        ],
        "phone_number": [
            "555-0191", "555-0192", "555-0193", "555-0194", "555-0195", "555-0196", "555-0197", "555-0198",
            "555-0199", "555-0200", "555-0201", "555-0202", "555-0203", "555-0204", "555-0205"
        ],
        "street_address": [
            "123 Oak St", "456 Pine Rd", "789 Maple Ave", "101 Birch Ln", "202 Cedar Blvd", "303 Walnut Dr", "404 Elm St",
            "505 Ash Ct", "606 Spruce Way", "707 Cherry Cir", "808 Willow Pkwy", "909 Poplar Pl", "111 Fir St", "222 Redwood Trl", "333 Beech Ter"
        ],
        "city": [
            "Springfield", "Madison", "Riverton", "Franklin", "Greenville", "Fairview", "Clinton", "Georgetown", "Salem",
            "Ashland", "Centerville", "Milton", "Oakdale", "Arlington", "Newport"
        ],
        "state": [
            "CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "NC", "MI", "AZ", "WA", "CO", "OR", "NV"
        ],
        "zip_code": [
            "90001", "73301", "10001", "33101", "60601", "19104", "44101", "30301", "27501", "48201",
            "85001", "98101", "80201", "97201", "89501"
        ]
    }

    df = pd.DataFrame(data)

    # Connect to SQLite database
    connection = sqlite3.connect("my_database.db")
    # Insert DataFrame into database table "employees"
    df.to_sql("employees", connection, if_exists="replace", index=False) #replace
    print("Data inserted successfully")

# Display the table to verify initalization of data
def verify_table_creation():
    # Verify insertion by querying the table
    result = pd.read_sql("SELECT * FROM employees", connection)
    print(result)

# Fetch all data from the table
def fetch_all_data():
    # Fetch all rows and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# List all user's first and last names
def list_user_names():
    cursor.execute("SELECT first_name, last_name FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Creates a contact list of all employees
def create_contact_list():
    cursor.execute("SELECT first_name, last_name, email_address FROM employees")
    rows = cursor.fetchall()
    contact_list = []
    for row in rows:
        contact_list.append({
            "first_name": row[0],
            "last_name": row[1],
            "email_address": row[2]
        })
    return contact_list

# Loads table into a DataFrame
def load_data_into_dataframe():
    # Load data into a DataFrame
    df = pd.read_sql_query("SELECT * FROM employees", connection)
    print(df.head())

def main():

    check_sqlite()

    connection = sqlite3.connect("my_database.db")

    # Create a cursor object
    cursor = connection.cursor()

    try:
        connection = sqlite3.connect("my_database.db")
        cursor = connection.cursor()
        # Perform operations
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")

    initialize_database()

    verify_table_creation()

    fetch_all_data()

    list_user_names()

    create_contact_list()

    load_data_into_dataframe()

if __name__ == "__main__":
    main()
