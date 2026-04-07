import csv
import random
from datetime import datetime, timedelta

# -------- Helper functions --------
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# -------- Generate Customers --------
customers_file = "customers.csv"

countries = ["India", "USA", "UK", "Canada", "Australia"]

customer_ids = []

with open(customers_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["customer_id", "country", "signup_date"])
    
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 4, 1)
    
    for i in range(1, 1001):
        customer_id = f"C{str(i).zfill(3)}"
        customer_ids.append(customer_id)
        
        country = random.choice(countries)
        signup_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
        
        writer.writerow([customer_id, country, signup_date])

# -------- Generate Orders --------
orders_file = "orders.csv"

statuses = ["delivered", "pending", "cancelled"]

with open(orders_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "customer_id", "amount_cents", "status", "created_at"])
    
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2024, 4, 30)
    
    for i in range(1, 1001):
        order_id = i
        customer_id = random.choice(customer_ids)
        amount_cents = random.randint(500, 10000)  # ₹5 to ₹100 approx
        status = random.choice(statuses)
        created_at = random_date(start_date, end_date).strftime("%Y-%m-%d")
        
        writer.writerow([order_id, customer_id, amount_cents, status, created_at])

print("CSV files generated: orders.csv and customers.csv")