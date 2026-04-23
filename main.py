from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.validate import validate_data
from scripts.utils import setup_logger, log_info, log_error

setup_logger()

log_info("Pipeline Started")

if __name__ == "__main__":

    data_path = "data"
    data = extract_data(data_path)

if data:
    
    log_info("Data Extracted Successfully")
    sales, product, customer, store, calendar = data

    fact, dim_p, dim_c, dim_s, dim_d = transform_data(sales, product, customer, store, calendar)

    log_info("Transformation Done") 

    validate_data(fact)

    load_data(fact, dim_p, dim_c, dim_s, dim_d)

    log_info("Pipeline Completed")   

else:
    log_error("Extraction Failed")   

