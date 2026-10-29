# Customer Churn Analysis

## Project Overview
An end-to-end data analytics project investigating customer churn in the telecommunications industry using Python, SQL, and Power BI.

## Business Objectives
- Measure the overall customer churn rate.
- Identify customer segments with higher churn rates.
- Analyze relationships between contract types, tenure, payment methods, and technical support.
- Develop data-driven customer retention recommendations.

## Tools & Technologies
- **Python:** Pandas, NumPy, Matplotlib, Seaborn
- **SQL:** MySQL
- **Power BI:** Interactive dashboards and KPI reporting
- **Git & GitHub:** Version control and project documentation

## Dataset
IBM Telco Customer Churn dataset:  
https://github.com/IBM/Customer-Churn

The dataset contains customer demographics, services, contracts, billing information, and churn status.

## Data Cleaning
- Inspected 7,043 customer records and 21 columns.
- Checked duplicate records and customer identifiers.
- Converted `TotalCharges` to a numeric data type.
- Investigated 11 blank `TotalCharges` values associated with zero-tenure customers.
- Treated those values as zero accumulated charges as a documented assumption.

## Preliminary Findings
- Overall churn rate: **26.54%**
- Month-to-month contract churn rate: **42.71%**
- Churn rate among customers with 0–12 months of tenure: **47.44%**
- Electronic-check payment churn rate: **45.29%**
- Churn rate among customers without tech support: **41.64%**

These are descriptive findings, not proof of causation.

## Project Status
- [x] Dataset inspection
- [x] Initial data cleaning
- [x] Exploratory data analysis
- [ ] SQL business analysis
- [ ] Power BI dashboard
- [ ] Final business recommendations

## Repository Structure
- `Data/` — Raw and processed data, excluded from Git
- `Notebooks/` — Python inspection, cleaning, and EDA scripts
- `Sql/` — SQL analysis scripts
- `Powerbi/` — Power BI report
- `Reports/` — Business insights and documentation
- `Screenshots/` — Project visuals

## Disclaimer
This project is for educational and portfolio purposes. Findings and recommendations are based on analysis of the supplied dataset.
