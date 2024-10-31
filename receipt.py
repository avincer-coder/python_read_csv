import pandas as pd

def read_dictionary(filename, key_column_index):
        product_csv = pd.read_csv(filename)
        dict_product = product_csv.set_index(product_csv.columns[key_column_index]).T.to_dict("list")
        return(dict_product)
        




def main():
        products_dict = read_dictionary("products.csv", 0)
        print(products_dict)
        with open("request.csv", mode="r") as file:
                next(file)
                request_summary = {}
                for request_line in file:
                        file_request_format = request_line.strip().split(",")
                        product_code = file_request_format[0]
                        product_price = products_dict[product_code][1] 
                        product_name = products_dict[product_code][0] 
                        product_quantity = int(file_request_format[1])
                        print(f"{product_name} {product_quantity} ${product_price}") 
                        if product_code in request_summary: 
                                request_summary[product_code]+=product_quantity
                        else:
                                request_summary[product_code]=product_quantity
                         
                # for product_code in request_summary: 
                #         if product_code in products_dict:
                #                 product_name = products_dict[product_code][0]
                #                 product_price = products_dict[product_code][1]
                #                 total_quantity = request_summary[product_code]
                #                 # print(f", {product_name}: {total_quantity} @ ${product_price:.2f} each")
                #         else:
                #                 # print(f"Product {product_code} not found in products list.") 
                        
                        
        
if __name__ == "__main__":
    main()