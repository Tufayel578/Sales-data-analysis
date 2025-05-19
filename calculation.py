# calculation.py
# This module contains logic for calculating total revenue, cost, and profit
# based on sales data provided in dictionary format (from CSV).

def calculate_all_totals(data):
    """
    Calculates total revenue and profit for each sales record in the dataset.
    
    Parameters:
        data (list of dict): List of sales records where each record is a dictionary
            that must contain 'Quantity', 'UnitPrice', and 'CostPrice' keys.

    Returns:
        list of dict: Modified list with new fields added: 'TotalRevenue', 'TotalCost', and 'Profit'.
    """

    # Iterating over each row (sales record) in the dataset
    for row in data:
        try:
            # Extracting and convert necessary fields from the row
            quantity = int(row.get('Quantity', 0))  # Number of items sold
            unit_price = float(row.get('UnitPrice', 0))  # Price at which item was sold
            cost_price = float(row.get('CostPrice', 0))  # Price at which item was purchased

            # Performing financial calculations
            total_revenue = quantity * unit_price  # Total revenue = Qty * Selling Price
            total_cost = quantity * cost_price     # Total cost = Qty * Purchase Price
            profit = total_revenue - total_cost    # Profit = Revenue - Cost

            # Storing results back in the row, rounding to 2 decimal places
            row['TotalRevenue'] = round(total_revenue, 2)
            row['TotalCost'] = round(total_cost, 2)
            row['Profit'] = round(profit, 2)

        except (ValueError, TypeError):
            # If data conversion fails, record an error in the respective fields
            row['TotalRevenue'] = 'Error'
            row['TotalCost'] = 'Error'
            row['Profit'] = 'Error'

    # Returning the modified dataset with added calculation columns
    return data
