import pandas as pd
def read_dictionary(filename):
        product_csv = pd.read_csv(filename)
        print(product_csv)
read_dictionary("products.csv")
read_dictionary("request.csv")