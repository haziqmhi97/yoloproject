import numpy as np
import pandas as pd

# Read raw data from output.txt
with open('output.txt', 'r') as file:
    raw_data = np.array(eval(file.read()))

# Reshape the data to have 3 values (x, y, confidence) for each keypoint
reshaped_data = raw_data.reshape(-1, 3)

# Create a DataFrame with reshaped data
df = pd.DataFrame(reshaped_data, columns=['X', 'Y', 'Confidence'])

# Add a column for keypoint numbers
df['Keypoint'] = np.tile(np.arange(17), len(raw_data) // 17)

# Reorder columns
df = df[['Keypoint', 'X', 'Y', 'Confidence']]

# Save to Excel file
df.to_excel('output.xlsx', index=False)
