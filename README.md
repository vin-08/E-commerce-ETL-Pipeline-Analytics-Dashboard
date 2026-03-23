# E-commerce ETL Pipeline & Analytics Dashboard

## Project Overview

This project demonstrates an end-to-end **ETL pipeline** built using Python and MySQL, along with an interactive **Power BI dashboard** for business insights.

The pipeline processes raw e-commerce datasets, performs data cleaning and transformation, and loads structured data into a relational database for analysis and visualization.

---

## ⚙️ Tech Stack

- **Programming:** Python
- **Data Processing:** Pandas, NumPy
- **Database:** MySQL
- **SQL:** Joins, Aggregations, Window Functions
- **Visualization:** Power BI
- **Other:** ETL Pipeline Design, Batch Processing

---

## 🔄 ETL Pipeline

### 1. Extract
- Reads incoming batch CSV files from the `data/source/` folder
- Simulates real-time data ingestion by processing files released at timed intervals

### 2. Transform
- Handles missing values and inconsistent data
- Removes duplicate records to maintain data quality
- Converts data types for accurate analysis (e.g., timestamps, numeric fields)
- Performs feature engineering (e.g., calculates `total_price`)
- Validates data before loading

### 3. Load
- Loads transformed data into MySQL tables
- Maintains relational integrity using primary and foreign keys
- Prevents duplicate inserts and ensures consistent data storage

---

## 📦 Data Pipeline Features

- Simulated **real-time batch ingestion**
- Automated ETL workflow
- Data validation and cleaning
- Relational schema design
- SQL-based analytics layer

---

## 🗄️ Database Design

- **Customers (Dimension Table)**
- **Products (Dimension Table)**
- **Sellers (Dimension Table)**
- **Orders (Dimension Table)**
- **Order Items (Fact Table)**

---

## 📈 SQL Analytics

Example insights generated:

- Top selling products
- Revenue by seller
- Customer spending patterns
- Order trends over time

---

## 📊 Dashboard

Power BI dashboard includes:

- Total Revenue KPI
- Top Products
- Average order price
- Delivered v/s Non-delivered orders
- Seller Performance
- Order Trends
- Customers by geography on a world map

### 📸 Dashboard Preview

![Dashboard Page 1](dashboard/Visualizatiions_1.png)

![Dashboard Page 2](dashboard/Visualizatiions_2.png)

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ecommerce-etl-pipeline.git
cd ecommerce-etl-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL
Create database: ecommerce

### 4. Environment Setup
Before running the project, update MySQL credentials in the following files:

🔹 File: .env
Replace:
```bash
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=ecommerce
```
With your own MySQL username and password.







