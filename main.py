# main.py
# This script reads sales data from a CSV file, processes the data to calculate totals,
# and writes the results into a new CSV file. It is designed to be executed from the CLI.

import csv  # For handling CSV file reading and writing
from calculation import calculate_all_totals  # Import custom calculation function

def read_csv():
    """
    Reads sales data from a CSV file and returns a list of dictionaries.
    Each dictionary represents one row of data.
    """
    file_path = "sales_data.csv"  # Input file path (ensuring this file exists)
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Reading data as a list of dictionaries
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  # Displaying error if file is missing
        return []  # Return empty list if file is not found

def write_csv(data):
    """
    Writes processed sales data into a result CSV file.
    Adds calculated fields such as total revenue and profit.
    """
    output_file = "result.csv"  # Output file name
    if data:
        fieldnames = list(data[0].keys())  # Using keys from first row for column headers
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)  # Creating CSV writer
            writer.writeheader()  # Writting column headers
            writer.writerows(data)  # Writting all rows of processed data
        print(f"Results saved to '{output_file}'")  # Confirmation message
    else:
        print("No data to write.")  # Warning if input data is empty

def main():
    """
    Main function to control the workflow:
    - Reads input data
    - Processes the data
    - Writes the output to a CSV file
    """
    data = read_csv()  # Step 1: Reading input CSV file
    processed_data = calculate_all_totals(data)  # Step 2: Performing calculations
    write_csv(processed_data)  # Step 3: Save processed results

# Entry point for the script. This block ensures main() runs only when script is executed directly.
if __name__ == "__main__":
    main()
