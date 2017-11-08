from Utils.getScreen import *
from Utils.getkeys import key_check
import cv2
import time
import os
import win32con

file_name = 'training_data.npy'
crucial_name = 'crucial_data.npy'
WIDTH = 200
HEIGHT = 70
screenRegion = (30, 130, 610, 250)

'''
Check if the training data already exists
	True: append new data
	False: create new files
'''
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
	Encode key press to binary format
	[UP] - 1
	[NOOP] - 0
	'''
	output = []

	if win32con.VK_UP in keys:
		output = [1]
	else:
		output = [0]
	return output


def main(verbose=0, showScreen=0):
	# Count down timer
	for i in list(range(4))[::-1]:
		print(i + 1)
		time.sleep(1)

	prevCount = 0               # keeps track of continuous UP key press
	last_time = time.time()

	while True:
		# Capture the required region of the screen and convert to greyscale
		screen = grab_screen(region=screenRegion)
		screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

		# resize to something a bit more acceptable for a CNN
		screen = cv2.resize(screen, (HEIGHT, WIDTH))

		# Check if key has been pressed
		keys = key_check()
		output = keys_to_output(keys)

		training_data.append([screen, output])
		trainLength = len(training_data)

		"""
		
		Code to handle latency between key press and the event being recorded
		The ideal time for key press is 2 frames before the actual frame where the event is registered.   
		
		"""
		if output == [1] and trainLength > 3:
			prevCount += 1
			if prevCount > 2:
				continue
			
			training_data[trainLength - 2][1] = [1]
			training_data[trainLength - 3][1] = [1]

			crucial_data.append([training_data[trainLength - 2][0], [1]])
			crucial_data.append([training_data[trainLength - 3][0], [1]])

		else:
			prevCount = 0

		if len(training_data) % 500 == 0:
			print(len(training_data), len(crucial_data))
			np.save(file_name, training_data)
			np.save(crucial_name, crucial_data)

		"""
		Print frame rate
		"""
		if verbose:
			print('loop took {} seconds'.format(time.time() - last_time))
			print('Frame rate: {} '.format(1.0/(time.time() - last_time)))
			last_time = time.time()

		if showScreen:
			cv2.imshow('window', screen)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break


main()
