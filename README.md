Sales Data Analysis
This Python program processes sales data stored in a CSV file. It calculates key financial metrics—Total Revenue, Total Cost, and Profit—for each sales record. It uses modular design, error handling, and clean file I/O operations to ensure robustness and clarity.

Features
Reads sales records from sales_data.csv

Calculates:

Total Revenue = Quantity × Unit Price

Total Cost = Quantity × Cost Price

Profit = Total Revenue − Total Cost

Handles invalid data using try-except blocks

Saves results to result.csv

Modular code using main.py and calculation.py

Simple CLI integration with informative output messages

File Structure

├── main.py             # Controls the program workflow
├── calculation.py      # Contains the financial computation logic
├── sales_data.csv      # Input data file (user-supplied)
├── result.csv          # Output data file (generated)
└── README.md           # Project documentation
Requirements
Python 3.x

No external libraries required.

Usage
Place your sales_data.csv in the same directory.

Run the program:


python main.py
Output will be saved as result.csv in the same directory.
