import numpy as np
from getScreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import win32con


file_name = 'training_data.npy'
crucial_name = 'crucial_data.npy'
if os.path.isfile(file_name):
	print('File exists, loading previous data!')
	training_data = list(np.load(file_name))
	crucial_data = list(np.load(crucial_name))
else:
	print('File does not exist, starting fresh!')
	training_data = []
	crucial_data = []


def keys_to_output(keys):
	'''
	Convert keys to a ...multi-hot... array

	[UP,DOWN,NOOP] boolean values.
	'''
	output = [0, 0, 0]

	if win32con.VK_UP in keys:
		output[0] = 1
	elif win32con.VK_DOWN in keys:
		output[1] = 1
	else:
		output[2] = 1
	return output


def main():
	for i in list(range(4))[::-1]:
		print(i + 1)
		time.sleep(1)

	while (True):
		# 600x175 windowed mode
		screen = grab_screen(region=(0, 95, 600, 270))
		screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
		# resize to something a bit more acceptable for a CNN
		screen = cv2.resize(screen, (180, 100))
		cv2.imshow('window', screen)
		keys = key_check()
		output = keys_to_output(keys)
		training_data.append([screen, output])
		if output == [1, 0, 0] or output == [0, 1, 0]:
			crucial_data.append([screen, output])
		if len(training_data) % 500 == 0:
			print(len(training_data), len(crucial_data))
			np.save(file_name, training_data)
			np.save(crucial_name, crucial_data)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break


main()



