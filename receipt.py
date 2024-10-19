import pandas as pd

def read_dictionary(filename, key_column_index):
        product_csv = pd.read_csv(filename)
        # print(product_csv)
        dict_product=product_csv.set_index(key_column_index).T.to_dict("list")
        # print(dict_product)
        return(dict_product)
        




def main():
        dict_product_from_read = read_dictionary("products.csv", "Product #")
        # print(dict_product_from_read)

        with open("request.csv", mode="r") as file:
                next(file)

                for request_line in file:
                        file_request_format = request_line.strip().split(",")
                        product_code = file_request_format[0]
                        product_quantity = int(file_request_format[1])
                        product_price = dict_product_from_read[product_code][1]
                        product_name = dict_product_from_read[product_code][0]
                        
                        print(f"{product_name} {product_quantity} ${product_price}")

                        if product_code in file_request_format:
                                print(f"se repite el producto {product_name}")
                        
                        print()
main()