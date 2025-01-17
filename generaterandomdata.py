#12272024
#generate random 
import os
import numpy as np
import pandas as pd
print("Current working directory:", os.getcwd())
rows, cols = 70, 7
# Generate random data
j = int(input("enter number of data sets"))
columns = [f'Column_{i}' for i in range(1, cols + 1)]
for i in range(j):
    data = np.random.randint(low = 0, high = 100, size = (rows, cols))
    #print(data)
    sn = "".join(["random_data_", str(i+1)])
    sn = "".join([sn, ".csv"])
    print(sn)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(sn, index=False)
print("program finished")
