import pandas as pd

# Load the data
data = pd.read_csv('patients_data.csv')

# Check the first few rows of the dataset to understand its structure
print(data.head())

# Group by 'City' and count the number of patients in each city
city_counts = data['City'].value_counts()

# Get the top 5 most common cities
top_5_cities = city_counts.head(5).index

# Filter the data to only include patients from the top 5 cities
filtered_data = data[data['City'].isin(top_5_cities)]

# For each city in the top 5, find the most common disease
most_common_diseases = {}
for city in top_5_cities:
    city_data = filtered_data[filtered_data['City'] == city]
    most_common_disease = city_data['Disease'].value_counts().idxmax()
    most_common_diseases[city] = most_common_disease

# Output the most common diseases for the top 5 cities
for city, disease in most_common_diseases.items():
    print(f"The most common disease in {city} is {disease}.")
