import win32api as wapi
import win32con

keyList = {win32con.VK_UP: "UP", win32con.VK_DOWN: "DOWN"}


def key_check():
    keys = []
    for key in keyList.keys():
        if wapi.GetAsyncKeyState(key):
            keys.append(key)
            return keys
    return keys
