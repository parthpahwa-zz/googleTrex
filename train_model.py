import numpy as np
from alexnet import alexnet

WIDTH = 180
HEIGHT = 100
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'chrome-tRex-{}-{}-{}-epochs.model'.format(LR, 'alexnetv3', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('training_data_v3.npy')
crucial_data = np.load('crucial_data.npy')
print(len(train_data))
train = train_data[:-750]
test = train_data[-750:]
crucialData = crucial_data[:1500]
test = np.concatenate((test, crucial_data), axis=0)

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
model.save(MODEL_NAME)
print("MODEL SAVED")