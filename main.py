#if we don't want to use the UI, then put the filename here.

from ocr import perform_ocr

perform_ocr("DSC_0511.jpg")

import os
import subprocess, sys

if sys.platform == "win32":
	os.startfile("output.txt")
else:
	opener ="open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, "output.txt"])

