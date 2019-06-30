import ctypes
import os

def apply_wallpaper(fn):
    return ctypes.windll.user32.SystemParametersInfoW( 20 , 0 , os.path.abspath( fn ) , 0 )