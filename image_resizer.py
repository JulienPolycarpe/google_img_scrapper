from PIL import Image
import glob, os

size = 1080, 1080
number = 0

for infile in glob.glob("images/*"):
	file, ext = os.path.splitext(infile)
	im = Image.open(infile)
	im.thumbnail(size)
	im.save("after/"+ str(number) + ".jpg", "JPEG")
	number += 1

for infile in glob.glob("images/*"):
	os.remove(infile)