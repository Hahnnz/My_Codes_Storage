import pandas as pd
import numpy as np

ratio = 10
n_data = 60
n_classes = 16

train_csv = list(pd.read_csv("activity.csv", header=None).as_matrix())
test_csv = list(list(["" if j==0 else 0 for j in range(len(train_csv[0]))] for i in range(len(train_csv)//ratio)))

test_indices = list()

for i in range(n_classes):
    samples = np.random.choice(range(i*n_data, (i+1)*n_data),6,replace=False)
    for sample in list(samples):
        test_indices.append(sample)
        
for i, idx in enumerate(list(reversed(sorted(test_indices)))):
    test_csv[i] = train_csv.pop(idx)

pd.DataFrame(np.array(test_csv)).to_csv("train.csv", sep=',', encoding='utf-8',index=False,header=None)
pd.DataFrame(np.array(test_csv)).to_csv("test.csv", sep=',', encoding='utf-8',index=False,header=None)
