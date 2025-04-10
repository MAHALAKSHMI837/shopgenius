import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, '..', 'data')

    customers_path = os.path.join(data_dir, 'customer_data_collection.csv')
    products_path = os.path.join(data_dir, 'product_recommendation_data.csv')

    customers = pd.read_csv(customers_path)
    products = pd.read_csv(products_path)

    return customers, products
