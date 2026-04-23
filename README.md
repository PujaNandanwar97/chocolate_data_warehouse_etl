## Chocolate Sales Data Warehouse ETL Pipeline

## Project Overview
This project demonstrates an end-to-end ETL pipeline built using Python and PostgreSQL to design a Data Warehouse using a Star Schema approach.

The pipeline extracts data from multiple CSV files, transforms it into structured format, validates data quality, and loads it into a PostgreSQL database.


##  Data Architecture

The project follows a **Star Schema Data Model**:

- **Fact Table:**
  - `fact_sales`

- **Dimension Tables:**
  - `dim_customer`
  - `dim_product`
  - `dim_store`
  - `dim_calendar`


##  Tech Stack

- Python (Pandas)
- PostgreSQL
- SQLAlchemy
- Logging (Python logging module)
- Git & GitHub


##  ETL Pipeline Flow

1. **Extract**
   - Load data from CSV files (Sales, Customer, Product, Store, Calendar)

2. **Transform**
   - Data cleaning (null handling, duplicates removal)
   - Data type conversion (dates, IDs)
   - Creation of fact and dimension tables

3. **Validate**
   - Null value checks
   - Negative value checks
   - Data consistency validation

4. **Load**
   - Load processed data into PostgreSQL using SQLAlchemy


##  Project Structure

chocolate_data_warehouse/ │ 
├── data/
├── scripts/ │  
     ├── extract.py │   
     ├── transform.py │   
     ├── load.py │    
     ├── validate.py │  
     ├── utils.py │   
     ├── config.py │
├── main.py


##  Key Features

- Modular ETL pipeline design
- Star Schema Data Warehouse
- Data validation layer
- Config-driven database connection
- Logging system for pipeline monitoring



##  Screenshots

###  Project Structure
[Structure](Project Folder.png)

###  Pipeline Output
[Output](Pipeline Output.png)

###  PostgreSQL Tables
[Database](PostgreSQL table.png)


 
##  Code Snippets

###  Data Transformation
```python
sales["order_date"] = pd.to_datetime(sales["order_date"], errors='coerce')
sales = sales[sales["quantity"] > 0]

dim_product = product.drop_duplicates().reset_index(drop=True)
fact_sales = sales.copy()

🔹 Data Loading

connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

🔹 Logging Setup

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


 How to Run

pip install pandas sqlalchemy psycopg2
python main.py



## Key Learnings

-Building scalable ETL pipelines

-Data Warehousing concepts (Fact & Dimension tables)

-Handling real-world data issues

-Implementing logging and validation

-Database integration with PostgreSQL


👩‍💻 Author

Pooja Namdeo Nandanwar
