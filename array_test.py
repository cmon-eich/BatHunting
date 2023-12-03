import sqlite3
import io
import numpy as np
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('batcallsv14.db')
cursor = conn.cursor()

# Retrieve the image data as a byte array
cursor.execute("SELECT arr FROM batcalls WHERE call = ?", (1,))
spectrogram_data = cursor.fetchone()[0]
array_data = np.frombuffer(spectrogram_data, dtype=np.int16)

plt.plot(array_data)
plt.title('Spectrogram')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

