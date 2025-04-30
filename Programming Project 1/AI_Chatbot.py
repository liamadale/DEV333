import re
import time
import shutil
from datetime import datetime

# INPUT VALIDATION FUNCTIONS

def validate_email(email: str) -> bool:
    # Basic email pattern: local@domain.tld
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    # Accepts formats like (123) 456-7890, 123-456-7890, 1234567890
    pattern = r'^(\(\d{3}\)\s*|\d{3}[-\s]?)?\d{3}[-\s]?\d{4}$'
    return re.match(pattern, phone) is not None


# EXAMPLE VALID CREDIT CARD NUMBERS:
# 4111 1111 1111 1111 (Visa)
# 5500 0000 0000 0004 (MasterCard)
# 3400 0000 0000 009 (American Express)
# 6011 0000 0000 0004 (Discover)
def validate_credit_card_number(card_number: str) -> bool:
    # Simple Luhn algorithm check
    card_number = re.sub(r'\D', '', card_number)
    def luhn_checksum(num):
        total = 0
        reverse_digits = num[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    return len(card_number) in [13, 15, 16] and luhn_checksum(card_number)

def validate_expiration_date(exp: str) -> bool:
    # Accepts MM/YY format
    try:
        exp_date = datetime.strptime(exp, "%m/%y")
        now = datetime.now()
        return exp_date.replace(day=1) >= now.replace(day=1)
    except ValueError:
        return False

def validate_zip_code(zip_code: str) -> bool:
    # Accepts 5-digit ZIP codes or ZIP+4
    pattern = r'^\d{5}(-\d{4})?$'
    return re.match(pattern, zip_code) is not None

# FUNCTIONS FOR USER INTERACTION

def get_user_info(session):
    # User Data Collection
    while True:
        session['email'] = input("Please enter your email address: ")
        if validate_email(session['email']):
            break
        else:
            print("Invalid email address. Please try again.")
    while True:
        session['phone_number'] = input("Please enter your phone number: ")
        if validate_phone(session['phone_number']):
            break
        else:
            print("Invalid phone number. Please try again.")
    while True:
        try:
            session['num_licenses'] = int(input("How many licenses would you like to purchase? "))
            if session['num_licenses'] > 0:
                break
            else:
                print("Number of licenses must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def gold_support(session):
    # Gold Support Plan
    print("Would you be interested in purchasing the optional Gold Support plan which gets you priority support?")
    session['gold_supp_price'] = 0
    if 1 <= session['num_licenses'] <= 50:
        print("With the number of licenses you purchased the Gold Support plan is $500/year.")
        session['gold_supp_price'] = 500
    elif 51 <= session['num_licenses'] <= 99:
        print("With the number of licenses you purchased the Gold Support plan is $350/year.")
        session['gold_supp_price'] = 350
    elif session['num_licenses'] >= 100:
        print("With the number of licenses you purchased the Gold Support plan is $250/year.")
        session['gold_supp_price'] = 250
    session['gold_supp_query'] = input("Would you like to purchase the Gold Support plan? (yes/no): ")

def calculate_totals(session):
    # Calculating Total Cost
    base_total = session['num_licenses'] * 75
    print(f"The total cost for {session['num_licenses']} licenses is ${base_total}.")
    if session['gold_supp_query'].lower() == "yes":
        print(f"You chose the Gold Support plan. At ${session['gold_supp_price']}/year. Adding this to the total cost.")
        base_total += session['gold_supp_price']
        print(f"The total cost for {session['num_licenses']} licenses with Gold Support is ${base_total}.")
    print("Tax for this product is 10%")
    tax = base_total * 0.10
    session['price_total'] = base_total + tax
    print(f"The total cost including tax is ${session['price_total']}.")

def collect_payment_info():
    # Payment Information
    while True:
        credit_card_num = input("Please provide a credit card number to complete the purchase: ")
        if validate_credit_card_number(credit_card_num):
            break
        else:
            print("Invalid credit card number. Please try again.")
    while True:
        credit_card_exp = input("Please provide the expiration date of your credit card (MM/YY): ")
        if validate_expiration_date(credit_card_exp):
            break
        else:
            print("Invalid expiration date. Please try again.")
    while True:
        credit_card_cvc = input("Please provide the CVC of your credit card (numbers on the back): ")
        if credit_card_cvc.isdigit() and len(credit_card_cvc) in [3, 4]:
            break
        else:
            print("Invalid CVC. Please try again.")
    while True:
        zip_code = input("Please provide your zip code: ")
        if validate_zip_code(zip_code):
            break
        else:
            print("Invalid zip code. Please try again.")

def generate_receipt(session):
    # Receipt Generation
    for _ in range(3):
        for dots in [".", "..", "..."]:
            print(f"\rGenerating receipt{dots}   ", end="", flush=True)
            time.sleep(0.5)
    print("\nReceipt generated successfully!")
    print("Receipt:")
    print(f"Name: {session['first_name']} {session['last_name']}")
    print(f"Email: {session['email']}")
    print(f"Phone Number: {session['phone_number']}")
    print(f"Number of Licenses: {session['num_licenses']}")
    print(f"Gold Support Plan: {session['gold_supp_query']}")
    print(f"Total Cost: ${session['price_total']:.2f}")
    print("Thank you for your purchase!")

def print_fancy_title():
    title_lines = [
        "░█▀▀░█▀█░▀█▀░█▀▀░█▀█░▀█▀",
        "░█░░░█▀█░░█░░█░█░█▀▀░░█░",
        "░▀▀▀░▀░▀░░▀░░▀▀▀░▀░░░░▀░"
    ]
    
    # Get terminal width for centering
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    border = "═" * max(len(line) for line in title_lines)
    padding = (terminal_width - len(border)) // 2
    print("\n" + "═" * terminal_width + "\n")
    print(" " * padding + "╔" + border + "╗")
    for line in title_lines:
        print(" " * padding + "║" + line + "║")
    print(" " * padding + "╚" + border + "╝")
    print(" "* (padding - 15) + 'CatGPT – Answers when it wants to. Otherwise, it’s naptime.')
    print("\n" + "═" * terminal_width + "\n")

# Main Program Loop

while True:
    session = {}
    session['first_name'] = input("Enter your first name: ")
    session['last_name'] = input("Enter your last name: ")

    print(f"Hello {session['first_name']} {session['last_name']}, welcome to the CatGPT!")

    print_fancy_title()

    while True:
        purchase_query = input("Would you like to make a purchase? (yes/no): ").strip().lower()
        if purchase_query in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
    if purchase_query == "yes":
        print("Great! Let's proceed with your purchase.")
        
        get_user_info(session)

        gold_support(session)

        calculate_totals(session)

        collect_payment_info()
    
        generate_receipt(session)

    else:
        print("No problem! If you have any other questions, feel free to ask.")
    while True:
        continue_query = input("Would you like to continue? (yes/no): ").strip().lower()
        if continue_query in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
    if continue_query == "no":
        print("Thank you for using the CatGPT! Goodbye!")
        break
    else:
        print("Let's continue!")