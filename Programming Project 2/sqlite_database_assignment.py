import sqlite3
import pandas as pd

#   ███████╗ ██████╗ ██╗         ██╗███╗   ██╗██╗████████╗
#   ██╔════╝██╔═══██╗██║         ██║████╗  ██║██║╚══██╔══╝
#   ███████╗██║   ██║██║         ██║██╔██╗ ██║██║   ██║   
#   ╚════██║██║▄▄ ██║██║         ██║██║╚██╗██║██║   ██║   
#   ███████║╚██████╔╝███████╗    ██║██║ ╚████║██║   ██║   
#   ╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   

# Check if SQLite is available
def check_sqlite():
    """
    Checks if SQLite is available in the Python environment and prints the current version.
    """
    try:
        sqlite3_version = sqlite3.sqlite_version
        print(f"SQLite is available, version: {sqlite3_version}")
    except ImportError:
        print("SQLite is not installed or not available in this Python environment")

# Initialize the database with sample data
def create_and_populate_table(cursor, connection):
    """
    Creates the employees table if it doesn't exist and populates it with sample employee records using a pandas DataFrame.    """
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

    # Insert DataFrame into database table "employees"
    df.to_sql("employees", connection, if_exists="replace", index=False) #replace
    print("Data inserted successfully")

# Display the table to verify initalization of data
def verify_table_creation(connection):
    """
    Queries the employees table and prints the full dataset using pandas to confirm successful creation and insertion.
    """
    # Verify insertion by querying the table
    result = pd.read_sql("SELECT * FROM employees", connection)
    print(result)

# Fetch all data from the table
def fetch_all_data(cursor):
    """
    Executes a SELECT * query to fetch and print all employee records from the database.
    """
    cursor.execute("SELECT * FROM employees")
    # Fetch all rows and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#    ██████╗  █████╗ ████████╗ █████╗                
#    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗               
#    ██║  ██║███████║   ██║   ███████║               
#    ██║  ██║██╔══██║   ██║   ██╔══██║               
#    ██████╔╝██║  ██║   ██║   ██║  ██║               
#    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝               
#     █████╗  ██████╗ ██████╗███████╗███████╗███████╗
#    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
#    ███████║██║     ██║     █████╗  ███████╗███████╗
#    ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║
#    ██║  ██║╚██████╗╚██████╗███████╗███████║███████║
#    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝

# List all user's first and last names
def list_names(cursor):
    """
    Returns a list of all employee first and last names from the database.
    """
    cursor.execute("SELECT first_name, last_name FROM employees")
    return cursor.fetchall()

# Creates a contact list of all employees
def create_contact_list(cursor):
    """
    Returns a list of dictionaries with each employee's first name, last name, and email address.
    """
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

def count_employees_by_state(cursor):
    """
    Returns a list of tuples with the number of employees grouped and ordered by U.S. state.
    """
    cursor.execute("""
        SELECT state, COUNT(*) as employee_count
        FROM employees
        GROUP BY state
        ORDER BY employee_count DESC
    """)
    return cursor.fetchall()


#     ███╗   ███╗ █████╗ ██╗███╗   ██╗
#     ████╗ ████║██╔══██╗██║████╗  ██║
#     ██╔████╔██║███████║██║██╔██╗ ██║
#     ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#     ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

def main():
    check_sqlite()
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    try:
        print("Populatiing database with sample data...")
        create_and_populate_table(cursor, connection)
        print("\n--- Verifying table creation ---\n")
        verify_table_creation(connection)
        print("\n--- Fetching all data ---\n")
        print(fetch_all_data(cursor))
        print("\n" + "*" * 24)
        print("~~~ Unique Functions ~~~")
        print("*" * 24 + "\n")
        print("\n--- Names List ---\n")
        all_names = list_names(cursor)
        for name in all_names:
            print(name)
        print("\n--- Contact List ---\n")
        contact_list = create_contact_list(cursor)        
        for contact in contact_list:
            print(contact)
        print("\n--- Employees by State ---\n")
        employees_by_state = count_employees_by_state(cursor)
        for state, count in employees_by_state:
            print(f"{state}: {count}")
    finally:
        connection.close()
        print("SQLite connection closed")

if __name__ == "__main__":
    main()
