#if we don't want to use the UI, then put the filename here.

from ocr import perform_ocr

perform_ocr(".\image_samples\Test_.jpg")

import os
import subprocess, sys

if sys.platform == "win32":
	os.startfile("output.txt")
	print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\output.txt")
else:
	opener ="open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, "output.txt"])
	print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\output.txt")

