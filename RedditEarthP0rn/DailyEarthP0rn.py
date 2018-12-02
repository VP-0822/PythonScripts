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

#method to get BeautifulSoup object from html data
def parsehtmldata(html):
	if type(html) == str:
		return BeautifulSoup(html, 'html.parser')
	else:
		print('invalid html data to create BeautifulSoup object.')
		return None

def appendslash(url):
	if type(url) == str:
		if url.endswith('/') == false:
			url += '/'

def getelementbyid(htmldata, elementid):
	if type(htmldata) == BeautifulSoup:
		element = htmldata.find(id=elementid)
		return element
	else:
		print('Invalid html data for parsing')
		return None

def getelementbyclass(htmldata, elementtype ,elementclass):
	if type(htmldata) == BeautifulSoup and type(element) == str and type(elementclass) == str:
		element = htmldata.findAll(elementtype , {"class" : elementclass})
		if type(element) == BeautifulSoup:
			return element
		else:
			return None
	else:
		print('Invalid html data for parsing')
		return None

#def getAllElements(htmldata)

#def getallimageurls(htmldata):
#	if type(htmldata) == BeautifulSoup:
#		images =
#	else:
#		print('Invalid html data for parsing.')
#		return None

def isRedditUrl(url):
	if url.startswith('http'):
		return false
	return true

def saveDataOnDisk(url, destination):
	filename = getFilenameFromURL(url)
	urllib.request.urlretrieve(url, destination+ '/' + filename)
	if os.path.isfile(destination+'/'+ filename):
		print('File from url ' + url + ' downloaded successfully.')

def getFilenameFromURL(url):
	urlparts = url.split('/')
	length = len(urlparts)
	return urlparts[length-1]

def downloadImagesFromEarthPorn(url, localpathnew,threshold = 10000):
	earthporndata = getHTMLcontent(url)
	imagesdiv = getelementbyid(earthporndata,'siteTable')
	#imagedivbs = parsehtmldata(imagesdiv)

	downloadCount = 0
	lastdivid = ''

	if imagesdiv is None:
		return downloadCount,lastdivid

	#find all image urls
	allurldivs = imagesdiv.select("div")


	#for each div find image to download
	for urldiv in allurldivs:
		#divclass = urldiv.get('class') #divclass is list
		#if divclass is not None :
			#find actual file div class
		#	if len(divclass) > 1 and (divclass[1] == 'thing' or (len(divclass) > 2 and (divclass[2] is not None and divclass[2].startswith ('id-')))):
				#find page url div from div

		divid = urldiv.get('id') #divclass is list
		if divid is not None :
			#find page url div from div
			if divid.startswith('thing_t3'):
				#add your filter criteria
				lastfulldivid = urldiv.get('id')
				lastdivid = lastfulldivid.split('thing_')[1]
				if threshold < int(urldiv.get('data-score')):
					imageurl = urldiv.get('data-url')
					time.sleep(5)
					try:
						saveDataOnDisk(imageurl, localpathnew)
					except HTTPError:
						#retry after 5 seconds
						time.sleep(5)
						try:
							saveDataOnDisk(imageurl, localpathnew)
						except HTTPError:
							print('Not able to download from  ' + imageurl)

					downloadCount += 1
	return downloadCount,lastdivid

if __name__ == "__main__":
	redditHome = 'https://www.reddit.com'
	earthpornhome = redditHome + '/r/EarthPorn'

	downloadCount = 0
	lastAccessedImage = ''
	tempdownloadCount = 0

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

	#scans hot 250 posts
	for i in range(10):
		count  = i*25
		if count != 0:
			url = earthpornhome + "/?count="+str(count)+'&after='+lastAccessedImage
		else:
			url = earthpornhome
		try:
			#Add upvote or score thresold here UPVOTE_THRESOLD in second parameter
			temptempdownloadCount,templastAccessedImage = downloadImagesFromEarthPorn(url,localpathnew,10000)
			if temptempdownloadCount > 0 or templastAccessedImage != '':
				tempdownloadCount,lastAccessedImage = temptempdownloadCount,templastAccessedImage
		except HTTPError:
			#wait 5 more seconds
			time.sleep(5)
			try:
				#Add upvote or score thresold here UPVOTE_THRESOLD in second parameter
				tempdownloadCount,lastAccessedImage = downloadImagesFromEarthPorn(url,localpathnew)
			except HTTPError:
				print('Not able to connect to url ' + url)
				print('scanning next page')
				i -= 1
		downloadCount += tempdownloadCount

	if(downloadCount > 0):
		print('"In only c<>de we trust."')
	else:
		print('Oh, Snap! Wait for good stuff...')
