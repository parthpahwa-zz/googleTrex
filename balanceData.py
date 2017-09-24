import numpy as np

from random import shuffle

train_data = np.load('training_data.npy')

ups = []
downs = []
noOp = []
i = 2
count = 0
while i < (len(train_data) - 2):
    temp = train_data[i]
    if temp[1] == [1, 0, 0]:
        for j in range(i-2, i+2):
            print(i,j)
            data = train_data[j]
            data[1] = [1, 0, 0]
            train_data[j] = data
            count += 1
        i = i + 3
    else: i += 1

shuffle(train_data)
print(len(train_data), count)
np.save('training_data_v3.npy', train_data)
