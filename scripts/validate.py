def validate_data(fact_sale):

    if fact_sale.isnull().sum().sum() > 0:
        print("Warning: Null Values Found")

    if "quantity" in fact_sale.columns:
        if (fact_sale["quantity"] < 0).any():
            print("Warning: Negative Quantity Found")

    if "revenue" in fact_sale.columns:
        if (fact_sale["revenue"] < 0).any():
            print("Warning: Negative Revenue Found")     

    print("Data Validation Completed")        

