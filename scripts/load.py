from sqlalchemy import create_engine

def load_data(fact_sales, dim_product, dim_customer, dim_store, dim_calendar):

    try:
        from scripts.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(connection_string)

        fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)
        dim_product.to_sql("dim_product", engine, if_exists="replace", index=False)
        dim_customer.to_sql("dim_customer", engine, if_exists="replace", index=False)
        dim_store.to_sql("dim_store", engine, if_exists="replace", index=False)
        dim_calendar.to_sql("dim_calendar", engine, if_exists="replace", index=False)

        print("Data Loaded Successfully")

    except Exception as e:
        print("Error in loading data:", e)    
