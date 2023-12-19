# %%
import pandas as pd

file_path = 'predicted_test_yosef.csv'  
df = pd.read_csv(file_path)

df = df[['ID', 'rating']]  

# %%
df.head()

# %%
for id_num in range(1, 1001):
    if id_num not in df['ID'].values:
        # Append a new row with the missing id and rating = 1
        df = pd.concat([df, pd.DataFrame([{'ID': id_num, 'rating': 1}])], ignore_index=True)

# %%
output_file_path = 'submission_tpu_yosef.csv' 
df.to_csv(output_file_path, index=False)



