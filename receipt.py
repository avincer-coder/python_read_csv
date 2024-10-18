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
                        print(request_line)
        
        print(dict_product_from_read["D215"])

main()