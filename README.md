# Automated Data Profiling System

## Project Overview
The Automated Data Profiling System is a web-based application designed to
generate automated and detailed data profiling reports from CSV datasets.
The system uses YData Profiling for analysis and the Anvil Web Framework
to provide a simple and user-friendly web interface.

This project helps users quickly understand datasets by identifying
statistics, missing values, correlations, and data quality issues without
writing complex analysis code.

---

## Key Features
- Upload CSV datasets through a web interface
- Automated data profiling using YData Profiling
- Generation of detailed HTML and PDF reports
- Analysis of missing values, correlations, and data distributions
- Simple and user-friendly Anvil-based UI

---

## Technologies Used
- Python
- YData Profiling
- Anvil Web Framework
- Google Colab (Backend Execution)

---

## Backend Execution (Important)
The backend logic for data profiling is implemented using **Google Colab**.

To generate profiling reports:
- The Colab notebook/script must be executed separately
- The backend code is provided as a file in this repository
- The Colab code handles dataset processing and report generation using YData Profiling

This approach is used for ease of development, testing, and demonstration
of the data profiling logic.

---

## Live Project Link
The project is deployed as a live web application on Anvil:

https://darling-composed-crack.anvil.app/

---

## Usage
1. Open the live project link
2. Upload a CSV dataset
3. Run the backend Colab file provided in this repository
4. Generate the profiling report
5. Download the report in HTML or PDF format

---

## Academic Note
This project is developed as an academic project to demonstrate
automated data profiling, exploratory data analysis, and the integration
of Python data analytics with a web-based application.

---

## Author
Kartik Kasana
