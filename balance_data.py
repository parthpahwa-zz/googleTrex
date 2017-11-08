import numpy as np

train_data = np.load('training_data.npy')
crucial_data = np.load('crucial_data.npy')

i = 0
j = 0
negArray = []

# Under sample training data as majority of input belong to NOOP Class
while j < int(1.6*len(crucial_data)) and i < len(train_data):
    temp = train_data[i]
    if temp[1] == [0]:
        negArray.append(temp)
        j += 1
        i += 1
    else:
        i += 15

train_data = np.concatenate((crucial_data, negArray), axis=0)
np.random.shuffle(train_data)
np.save("finalData.npy", train_data)
