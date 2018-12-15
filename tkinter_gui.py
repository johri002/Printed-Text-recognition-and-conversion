import sys
import cv2
import os
import time
# from text2speech import textPlay
from PIL import Image as Img
from PIL import ImageTk
from tkinter import filedialog
from ocr import perform_ocr
import gtts as gTTS
from tkinter import *
# from tkinter import Tk, Label, Button, BOTTOM, LEFT, X


class Window:

	global imageWindow
	def __init__(self, master):
		# frame = Frame(master, width=600, height=600)
		# frame.pack()
		
		# imageWindow = Label()
		# imageWindow.pack(side=TOP, padx=10, pady=10, anchor=S)
		master.title("Optical Character Recognition")
		master.configure(background='black')
		master.geometry("800x800+500+300")
		self.imageWindow = None

		self.load_button = Button(master, text="Load image", command=self.select_image, bg="orange", relief=RAISED)
		self.load_button.pack(side=TOP, anchor=E)

		self.extract_button = Button(master, text="Extract text", bg="orange", relief=RAISED)
		self.extract_button.pack(side=TOP, anchor=E, expand="yes")

		self.playText_button = Button(master, text="Play text", bg="orange", relief=RAISED)
		self.playText_button.pack(side=TOP, anchor=E)

		self.quit_button = Button(master, text="Quit", command=master.quit, bg="orange", relief=RAISED)
		self.quit_button.pack(side=TOP, anchor=E, expand="yes")

	def select_image(self):

		path = filedialog.askopenfilename()
		# imageWindow
		if len(path) > 0:
			image = cv2.imread(path)
			image = cv2.resize(image, (500, 600))

			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			image = Img.fromarray(image)

			image = ImageTk.PhotoImage(image)

		if self.imageWindow is None:
			self.imageWindow = Label(image=image)
			self.imageWindow.image = image
			self.imageWindow.pack(side=LEFT)

		else:
			self.imageWindow.configure(image=image)
			self.imageWindow.image = image


root = Tk()

b = Window(root)
root.mainloop()
