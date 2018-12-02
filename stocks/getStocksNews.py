try:
	from bs4 import BeautifulSoup
except ImportError:
	import pip
	pip.main(['install', 'beautifulsoup4'])
	from bs4 import BeautifulSoup
import urllib.request
import sys


def getHTMLcontent(url):
	url = urllib.request.urlopen(url)
	htmldata = BeautifulSoup(url, 'html.parser')
	return htmldata

def getelementbyid(htmldata, elementid):
	if type(htmldata) == BeautifulSoup:
		element = htmldata.find(id=elementid)
		return element
	else:
		print('Invalid html data for parsing')
		return None

if __name__ == "__main__":
	print('Welcome! Happy Trading!!')
	user_input = 0
	while user_input is not -1 :
		scrip_name = input('Enter scrip name to fetch current trading price or exit : ')
		scrip_name = scrip_name.upper()

		if scrip_name == 'EXIT':
			user_input = -1
			continue

		scripDict = {}
		scripDict['AL'] = 'http://www.moneycontrol.com/india/stockpricequote/auto-lcvs-hcvs/ashokleyland/AL'
		scripDict['DMART'] = 'http://www.moneycontrol.com/india/stockpricequote/retail/avenuesupermarts/AS19'

		try:
			if scripDict[scrip_name] is None:
				print('Please ensure that you have added ' + scrip_name + ' to your portfolio.')
				continue
		except KeyError:
			print('Please ensure that you have added ' + scrip_name + ' to your portfolio.')
			continue

		scripURL = scripDict[scrip_name]
		NSE_DIV_ID = 'content_nse'
		NSE_PRICE_DIV_ID = 'Nse_Prc_tick_div'
		NSE_PRICE_CHANGE_DIV_ID = 'n_changetext'

		scripData = getHTMLcontent(scripURL)
		#nseDiv = getelementbyid(scripData, NSE_DIV_ID)
		nsePriceDiv = getelementbyid(scripData, NSE_PRICE_DIV_ID)
		#print(nsePriceDiv)
		currentPrice = nsePriceDiv.text
		print('current price for scrip '+ scrip_name + ' : ' + currentPrice)
		print('===========================================================')
