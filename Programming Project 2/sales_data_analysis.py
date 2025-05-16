import pandas as pd
import sqlite3

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def create_sqlite_db(products, sales, db_name='sales_data.db'):
    conn = sqlite3.connect(db_name)
    products.to_sql('Products', conn, if_exists='replace', index=False)
    sales.to_sql('Sales', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data saved to {db_name} successfully.")


def join_tables(db_name='sales_data.db'):
    conn = sqlite3.connect(db_name)
    query = """
    SELECT 
        Sales.sale_id,
        Products.category,
        Products.price,
        Sales.quantity,
        Sales.sale_date
    FROM Sales
    JOIN Products ON Sales.product_id = Products.product_id
    """
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def calculate_total_sales_per_category(data):
    # Calculate total sales amount per row
    data['TotalSales'] = data['quantity'] * data['price']
    # Group by category and sum the total sales
    total_sales = data.groupby('category')['TotalSales'].sum().reset_index()
    # Filter categories with total sales > 10000
    total_sales = total_sales[total_sales['TotalSales'] > 10000]
    return total_sales

def display_table(data):
    print(data.to_string(index=False))

#     ███╗   ███╗ █████╗ ██╗███╗   ██╗
#     ████╗ ████║██╔══██╗██║████╗  ██║
#     ██╔████╔██║███████║██║██╔██╗ ██║
#     ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#     ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

def main():
    # Load data from CSV file
    products = load_data("./csv/products.csv")
    sales = load_data("./csv/sales.csv")

    if products is not None and sales is not None:
        # Create SQLite database and save data
        create_sqlite_db(products, sales)
        
        # Join tables in the SQLite database
        joined_data = join_tables()
        
        # Calculate total sales per category
        total_sales = calculate_total_sales_per_category(joined_data)
        
        # Display the result
        display_table(total_sales)

if __name__ == "__main__":
    main()