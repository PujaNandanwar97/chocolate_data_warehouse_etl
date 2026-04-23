import pandas as pd
import os

def extract_data(data_path):

    try:
        sales = pd.read_csv(os.path.join(data_path, "sales.csv"))
        product = pd.read_csv(os.path.join(data_path, "products.csv"))
        customer = pd.read_csv(os.path.join(data_path, "customers.csv"))
        store = pd.read_csv(os.path.join(data_path, "stores.csv"))
        calendar = pd.read_csv(os.path.join(data_path, "calendar.csv"))

        return sales, product, customer, store, calendar
    
    except Exception as e:
        print("Error in extracting data:", e)
        return None
