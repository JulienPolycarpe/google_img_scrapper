from PIL import Image
import glob, os

size = 2048, 2048
number = 0

for infile in glob.glob("images/*"):
    file, ext = os.path.splitext(infile)
    for image in glob.glob(infile + "/*"):
        im = Image.open(image)
        #im.thumbnail(size)
        im.save("renamed_images/"+ str(number) + ".jpg", "JPEG")
        number += 1
        
"""
for infile in glob.glob("streetart/*"):
	os.remove(infile)

print("done")
"""
