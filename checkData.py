import numpy as np

train_data = np.load('training_data_v3.npy')
count = 0
for line in train_data:
	if line[1] ==[1,0,0]:
		count += 1
for line in train_data:
	print(line[1])
print(count)