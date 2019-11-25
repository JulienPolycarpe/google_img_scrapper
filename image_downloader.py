from google_images_download import google_images_download #SEE https://github.com/hardikvasa/google-images-download FOR DOCUMENTATION
from PIL import Image
import glob,os,shutil
from timeit import default_timer as timer

def download(dict_args):
	response = google_images_download.googleimagesdownload()
	response.download(dict_args)

def resize(size, keywords):
	for folder in keywords.split(","):
		start = timer()
		print("Starting to resize images from " + folder + "/")
		for infile in glob.glob("images/" + folder + "/*"):
			file, ext = os.path.splitext(infile)
			im = Image.open(infile)
			im.thumbnail(size)
			if not os.path.exists("resized_images/"+ folder):
				os.makedirs("resized_images/"+ folder)
			im.save("resized_images/"+ folder + "/" + infile.split('\\')[1], "JPEG")
		shutil.rmtree("images/" + folder, ignore_errors=True)
		time = "{0:.2f}".format(timer()-start)
		print(f"Folder {folder}/ images resized successfully ({time}s)\n")

def main():
	KEYWORDS = "streetart"
	LIMIT_PER_KEYWORD = 100
	USAGE_RIGHTS = "labeled-for-reuse"
	args = {"keywords":KEYWORDS, "limit":LIMIT_PER_KEYWORD, "output_directory":"images", "print_urls":False, "print_size":False, "format": "jpg", "size":">4MP"}
	#args = {"keywords":KEYWORDS, "limit":LIMIT_PER_KEYWORD, "usage_rights":USAGE_RIGHTS, "output_directory":"images", "print_urls":False, "print_size":False, "format": "jpg"}
	#https://google-images-download.readthedocs.io/en/latest/arguments.html FOR DOCUMENTATION
	size = 1080, 1080

	download(args)
	#resize(size, KEYWORDS)

if __name__ == '__main__':
    main()
