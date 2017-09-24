import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
import time
import cv2
import _thread

# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def grab_screen(region=None):
	hwin = win32gui.GetDesktopWindow()

	if region:
		left, top, x2, y2 = region
		width = x2 - left + 1
		height = y2 - top + 1
	else:
		width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
		height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
		left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
		top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

	hwindc = win32gui.GetWindowDC(hwin)
	srcdc = win32ui.CreateDCFromHandle(hwindc)
	memdc = srcdc.CreateCompatibleDC()
	bmp = win32ui.CreateBitmap()
	bmp.CreateCompatibleBitmap(srcdc, width, height)
	memdc.SelectObject(bmp)
	memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

	signedIntsArray = bmp.GetBitmapBits(True)
	img = np.fromstring(signedIntsArray, dtype='uint8')
	img.shape = (height, width, 4)

	srcdc.DeleteDC()
	memdc.DeleteDC()
	win32gui.ReleaseDC(hwin, hwindc)
	win32gui.DeleteObject(bmp.GetHandle())
	return img

# time.sleep(4)
# last_time = time.time()
#
# text = "-1"
# img = ImageGrab.grab(bbox=(480, 80, 590, 150))
# score = -1
#
# def get_score():
# 	global text
# 	global img
# 	global score
# 	while not img:
# 		pass
#
# 	while 1 > 0:
# 		text = pytesseract.image_to_string(img, config='outputbase digits')
# 		print( text)
# 		try:
# 			score = int(text)
# 			print("Score = {}",text)
# 		except:
# 			pass
# 	return
#
#
# try:
# 	_thread.start_new_thread(get_score, ( ))
# except:
# 	print("Error: unable to start thread")

# while True:
	# chrome window size 720 * 220
	# score Screen (450, 90, 580, 130)
	# trex gameplay screen (0, 95, 600, 270)
	# hiScore_img = screen[480:590, 80:150]
	# cv2.imshow('window',  np.array(imgTemp))
	# img = ImageGrab.grab(bbox=(450, 90, 580, 130))
	# print('Frame took {} seconds & number  = {}'.format(time.time() - last_time, score))
	# last_time = time.time()

	# hiScore_img = np.array(screen[480:590, 80:150])
	# print(type(ImageGrab.grab(bbox=(480, 80, 590, 150))))
	# screen = np.array(ImageGrab.grab(bbox=(0, 80, 600, 270)))
	# cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))


	# screen = grab_screen((0, 95, 600, 270))
	# cv2.imshow('window', screen)
	# if cv2.waitKey(25) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()
	# 	break

	# screen = cv2.resize(screen, (160,120))

def main():
	while (True):
		# 600x175 windowed mode
		screen = grab_screen(region=(0, 95, 600, 270))
		screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
		# resize to something a bit more acceptable for a CNN
		screen = cv2.resize(screen, (180, 100))
		cv2.imshow('window', screen)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
