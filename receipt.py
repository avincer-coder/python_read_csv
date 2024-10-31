import pandas as pd
from datetime import datetime

current_date_and_time = datetime.now()

def read_dictionary(filename, key_column_index):
    product_csv = pd.read_csv(filename)
    dict_product = product_csv.set_index(product_csv.columns[key_column_index]).T.to_dict("list")
    return dict_product

def new_year_sale():
    today = datetime.now()
    new_year_sale_date = datetime(today.year + 1, 1, 1)
    days_until_sale = (new_year_sale_date - today).days
    print("\nThank you for your purchase!")
    print(f"Reminder: Only {days_until_sale} days until the New Year's Sale begins!")

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        print("Inkom Emporium")

        with open("request.csv", mode="r") as file: 
            next(file)
            request_summary = {}
            total_quantity = 0
            total_price = 0
            
            for request_line in file:
                file_request_format = request_line.strip().split(",")
                product_code = file_request_format[0]
                
                product_price = float(products_dict[product_code][1])
                product_name = products_dict[product_code][0]
                product_quantity = int(file_request_format[1])

                print(f"{product_name} {product_quantity} @ ${product_price}") 

                total_quantity += product_quantity
                sum_products_by_price = product_quantity * product_price
                total_price += sum_products_by_price

                if product_code in request_summary: 
                    request_summary[product_code] += product_quantity
                else:
                    request_summary[product_code] = product_quantity

        tax_price = round(total_price * 0.06, 2)
        total_price_tax = tax_price + total_price

        print(f"Number of Items: {total_quantity}")
        print(f"Subtotal: {round(total_price, 2)}")       
        print(f"Sales Tax: {tax_price}")       
        print(f"Total: {total_price_tax}")       
        print("Thank you for shopping at the Inkom Emporium.") 
        
    except FileNotFoundError:
        print("Error: missing file")
        print("[Error 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: Permission denied. You do not have the required permissions to access this file.")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file {e}")

    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))
    new_year_sale()

if __name__ == "__main__":
    main()
