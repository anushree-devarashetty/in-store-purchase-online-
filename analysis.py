import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random  # Import the random module

# Generate sample data for in-store and online purchases
data = {
    'Date': [],
    'Product': [],
    'Price': [],
    'Quantity': [],
    'Location': [],
}

locations = ['In-Store', 'Online']

for _ in range(100):
    data['Date'].append((datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'))
    data['Product'].append(f'Product_{random.randint(1, 10)}')
    data['Price'].append(round(random.uniform(10, 100), 2))
    data['Quantity'].append(random.randint(1, 5))
    data['Location'].append(random.choice(locations))

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month from the 'Date' column
df['Month'] = df['Date'].dt.month

# Calculate total sales for in-store and online purchases
total_sales = df.groupby('Location')['Price'].sum().reset_index()

# Plot a bar graph
plt.figure(figsize=(8, 6))
sns.barplot(x='Location', y='Price', data=total_sales, palette='viridis')
plt.title('Total Sales for In-Store and Online Purchases')
plt.xlabel('Location')
plt.ylabel('Total Sales')
plt.show()
