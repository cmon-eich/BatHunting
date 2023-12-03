import sqlite3
import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('batcallsv14.db')
cursor = conn.cursor()

# Retrieve the image data as a byte array
query = "SELECT arr, target FROM batcalls WHERE call < 10"


df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()


# Function to convert binary data to NumPy array
def convert_to_array(binary_data):
    return np.frombuffer(binary_data, dtype=np.int16)

# Apply the conversion function to the entire column
df['SpectrogramData'] = df['arr'].apply(convert_to_array)
df = df.drop('arr', axis=1)
df_spectorgram = df['SpectrogramData'].apply(pd.Series)

# Concatenate the split columns with the original DataFrame
df = pd.concat([df, df_spectorgram], axis=1).drop('SpectrogramData', axis=1)

# Display the DataFrame
print(df)






