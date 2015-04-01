import requests
import sys
from lxml import etree
import lxml.html
import re

def getYearTable(XMLTree, tableID):
	years = []
	tab = XMLTree.get_element_by_id(tableID, None)
	print tab.tag
	for link in tab.iter("a"):
		link_text = link.text_content().strip()
		if re.match(r'^\d{4}$', link_text):
			years.append({link_text : link.get("href").strip()})
	return years

def scrapeRegXMLs(start_url, outputDir):
	startpage = requests.get(start_url).text
	startXML = lxml.html.fromstring(startpage)
	years = getYearTable(startXML, 'bulkdata')
	print years
	


if __name__ == "__main__":
	scrapeRegXMLs(sys.argv[1], sys.argv[2])