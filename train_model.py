import numpy as np
from Utils.alexnet import alexnet

WIDTH = 200
HEIGHT = 70
LR = 1e-3
EPOCHS = 15
MODEL_NAME = 'chrome-tRex-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('finalData.npy')
val_data = np.load('crucial_data.npy')

train = train_data
test = val_data

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]
test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME, batch_size=256)
model.save(MODEL_NAME)

print("MODEL SAVED")
