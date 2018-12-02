try:
	from bs4 import BeautifulSoup
except ImportError:
	import pip
	pip.main(['install', 'beautifulsoup4'])
	from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import os.path
import time
import shutil

def getHTMLcontent(url):
	url = urllib.request.urlopen(url)
	htmldata = BeautifulSoup(url, 'html.parser')
	return htmldata

def downloadImagesForURL():
    

if __name__ == "__main__":
    fhPxLandscapeURL = 'https://500px.com/editors/landscapes'
    fhPxNatureURL = 'https://500px.com/editors/nature'

    #Add local disk path here LOCAL_PATH
	# Example : C:\\Users\\john.doe\\Desktop\\HDWallpapers
	localpath = 'C:\\Users\\virajkumar.patel\\Desktop\\HDWallpapers'
	localpathnew = ''
	if localpath.endswith("\\"):
		localpathnew = localpath + "redditdailyearthp0rn"
	else:
		localpathnew = localpath + "\\redditdailyearthp0rn"

	if os.path.exists(localpathnew):
		shutil.rmtree(localpathnew)
		os.makedirs(localpathnew)
	else:
		os.makedirs(localpathnew)
