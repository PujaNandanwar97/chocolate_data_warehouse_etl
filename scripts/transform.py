import pandas as pd

def transform_data(sales, product, customer, store, calendar):

    sales.columns = sales.columns.str.strip().str.lower()
    product.columns = product.columns.str.strip().str.lower()
    customer.columns = customer.columns.str.strip().str.lower()
    store.columns = store.columns.str.strip().str.lower()
    calendar.columns = calendar.columns.str.strip().str.lower()


    if "order_date" in sales.columns:
        sales["order_date"] = pd.to_datetime(sales["order_date"], errors='coerce')

    if "join_date" in customer.columns:
        customer["join_date"] = pd.to_datetime(customer["join_date"], errors='coerce')

    if "date" in calendar.columns:
        calendar["date"] = pd.to_datetime(calendar["date"], errors='coerce')


    sales = sales.dropna()
    product = product.dropna()
    customer = customer.dropna()
    store = store.dropna()
    calendar = calendar.dropna()


    if "quantity" in sales.columns:
        sales = sales[sales["quantity"] > 0]      

    if "revenue" in sales.columns:
        sales = sales[sales["revenue"] > 0]     


    dim_product = product.drop_duplicates().reset_index(drop=True)
    dim_customer = customer.drop_duplicates().reset_index(drop=True)
    dim_store = store.drop_duplicates().reset_index(drop=True)
    dim_calendar = calendar.drop_duplicates().reset_index(drop=True)    

    fact_sales = sales.copy()

    fact_sales["product_id"] = fact_sales["product_id"].astype(str)
    fact_sales["customer_id"] = fact_sales["customer_id"].astype(str)
    fact_sales["store_id"] = fact_sales["store_id"].astype(str)

    dim_product["product_id"] = dim_product["product_id"].astype(str)
    dim_customer["customer_id"] = dim_customer["customer_id"].astype(str)
    dim_store["store_id"] = dim_store["store_id"].astype(str)

    return fact_sales, dim_product, dim_customer, dim_store, dim_calendar  


