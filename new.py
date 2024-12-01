import pandas as pd

# Make sure to replace 'survey_data.csv' with the actual path to your CSV file
df = pd.read_csv('survey_data.csv')

# Now, you can proceed with the analysis
mean_screen_time = df['screen_time'].mean()
median_screen_time = df['screen_time'].median()
mode_brand = df['brand'].mode()[0]

# Variance and Standard Deviation
variance = df['screen_time'].var()
std_dev = df['screen_time'].std()

print(f"Mean: {mean_screen_time}, Median: {median_screen_time}, Mode: {mode_brand}")
print(f"Variance: {variance}, Standard Deviation: {std_dev}")
