import sys
import cv2
import os
import time
from text2speech import textPlay
from PIL import Image as Img
from PIL import ImageTk
from tkinter import filedialog
from ocr import perform_ocr
import gtts as gTTS
from tkinter import *
import tkinter.messagebox


class Window:

	global imageWindow
	global path
	def __init__(self, master):
	
		master.title("Optical Character Recognition")
		master.configure(background='black')
		master.geometry("800x800+500+300")
		# image window
		self.imageWindow = None
		# input image path 
		self.path = ''

		# Load image button
		self.load_button = Button(master, text="Load image", command=self.select_image, bg="orange", relief=RAISED)
		self.load_button.pack(side=TOP, anchor=E)

		# Extract Text button
		self.extract_button = Button(master, text="Extract text", command=self.extract_text, bg="orange", relief=RAISED)
		self.extract_button.pack(side=TOP, anchor=E, expand="yes")

		# Play Text button
		self.playText_button = Button(master, text="Play text", command=self.play_text, bg="orange", relief=RAISED)
		self.playText_button.pack(side=TOP, anchor=E)

		# Quit Button
		self.quit_button = Button(master, text="Quit", command=master.quit, bg="orange", relief=RAISED)
		self.quit_button.pack(side=TOP, anchor=E, expand="yes")

	# function to extract text from input image
	def extract_text(self):
		perform_ocr(self.path)

		# pop-up to show extraction is completed and text file is saved
		tkinter.messagebox.showinfo('Success', 'Text file saved')

	def play_text(self):
		textPlay()

	# function to select and load image 
	def select_image(self):

		# get image path
		self.path = filedialog.askopenfilename()
		
		if len(self.path) > 0:
			image = cv2.imread(self.path) #read image
			image = cv2.resize(image, (500, 600)) #resize image
			cv2.imwrite("original_image.jpg", image) #save original image
			# swap channels
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			# convert image to PIL format
			image = Img.fromarray(image)

			# convert image to ImageTk format
			image = ImageTk.PhotoImage(image)

		# if the image window is None, initialize it
		if self.imageWindow is None:
			self.imageWindow = Label(image=image)
			self.imageWindow.image = image
			self.imageWindow.pack(side=LEFT)

		# otherwise, update the window
		else:
			self.imageWindow.configure(image=image)
			self.imageWindow.image = image

# initialize the app window
root = Tk()

b = Window(root)
root.mainloop()