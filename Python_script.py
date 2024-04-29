import pandas as pd
import matplotlib.pyplot as plt

def read_sales_data(file_path):
    # Read the CSV file into a DataFrame
    sales_data = pd.read_csv(file_path)
    
    # Display the first few rows of the DataFrame
    print("First few rows of the sales data:")
    print(sales_data.head())
    
    return sales_data

def clean_sales_data(sales_data):
    # Check for missing values
    print("\nChecking for missing values:")
    print(sales_data.isnull().sum())
    
    # Convert date column to datetime format
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])
    
    # Display data types of columns
    print("\nData types of columns:")
    print(sales_data.dtypes)
    
    return sales_data

# Path to the CSV file containing sales data
file_path = "sales_data.csv"

# Read sales data from the CSV file
sales_data = read_sales_data(file_path)

# Perform data cleaning and preparation
cleaned_sales_data = clean_sales_data(sales_data)

def calculate_total_sales(sales_data):
    total_sales = sales_data['Amount'].sum()
    return total_sales

def calculate_average_sales_per_month(sales_data):
    # Group by month and calculate the mean sales for each month
    average_sales_per_month = sales_data.groupby(sales_data['Date'].dt.to_period('M'))['Amount'].mean()
    return average_sales_per_month

def identify_top_selling_products(sales_data, n=5):
    # Group by product and sum the sales for each product
    product_sales = sales_data.groupby('Product')['Amount'].sum()
    
    # Sort products based on sales and get the top-selling products
    top_selling_products = product_sales.sort_values(ascending=False).head(n)
    return top_selling_products

# Calculate total sales
total_sales = calculate_total_sales(cleaned_sales_data)
print("\nTotal Sales:", total_sales)

# Calculate average sales per month
average_sales_per_month = calculate_average_sales_per_month(cleaned_sales_data)
print("\nAverage Sales per Month:")
print(average_sales_per_month)

# Identify top-selling products
top_selling_products = identify_top_selling_products(cleaned_sales_data)
print("\nTop Selling Products:")
print(top_selling_products)


def select_time_frame():
    while True:
        time_frame = input("Select the time frame for analysis (monthly/quarterly): ").strip().lower()
        if time_frame in ['monthly', 'quarterly']:
            return time_frame
        else:
            print("Invalid input. Please enter 'monthly' or 'quarterly'.")

def generate_sales_trend_chart(sales_data, time_frame):
    if time_frame == 'monthly':
        # Group by month and sum the sales for each month
        sales_trend = sales_data.groupby(sales_data['Date'].dt.to_period('M'))['Amount'].sum()
        title = 'Monthly Sales Trend Over Time'
        xlabel = 'Month'
    elif time_frame == 'quarterly':
        # Group by quarter and sum the sales for each quarter
        sales_trend = sales_data.groupby(sales_data['Date'].dt.to_period('Q'))['Amount'].sum()
        title = 'Quarterly Sales Trend Over Time'
        xlabel = 'Quarter'

    # Plot the line plot
    sales_trend.plot(kind='line', marker='o', color='orange')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Ask user to select the time frame for analysis
time_frame = select_time_frame()

# Generate sales trend chart based on the selected time frame
generate_sales_trend_chart(cleaned_sales_data, time_frame)
