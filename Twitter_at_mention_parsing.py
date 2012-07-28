from xml.etree import ElementTree
import re
import csv

def CSVexport(tweetData):
	#Save to CSV
	myfile = open("output.csv", "wb")
	w = csv.writer(myfile)
	for t in tweetData:
		for mention in t['mentions']:
			w.writerow([t['source'], mention])
	myfile.close()

def tweetParse(tree):
	#Parse Tweets
	tweetData= []
	for node in tree.iter():
		name = node.attrib.get('Username')
		tweet = node.attrib.get('Status')
		if name and tweet:

			#Regular expression for getting @mentions
			mentions = re.findall(r'@[\w]+', tweet)

			#Save to list of dictionaries containing user name and @mentions
			tweetData += [{'source': name, 'mentions': mentions}]
	return CSVexport(tweetData)

def maketree(xmlfile):
	with open(xmlfile, 'rt') as f:
		tree = ElementTree.parse(f)
		return tweetParse(tree)
	
maketree('test.xml')