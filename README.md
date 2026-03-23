# E-commerce ETL Pipeline & Analytics Dashboard

## Project Overview

This project demonstrates an end-to-end **ETL pipeline** built using Python and MySQL, along with an interactive **Power BI dashboard** for business insights.

The pipeline processes raw e-commerce datasets, performs data cleaning and transformation, and loads structured data into a relational database for analysis and visualization.

---

## 🏗️ Architecture

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
- Reads batch CSV files from source folder

### 2. Transform
- Handles missing values
- Removes duplicates
- Converts data types
- Creates new features (e.g., total_price)

### 3. Load
- Inserts data into MySQL tables
- Implements primary and foreign key constraints

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
- Seller Performance
- Order Trends

### 📸 Dashboard Preview

![Dashboard](dashboard/dashboard_screenshot.png)

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
Run sql/schema.sql


