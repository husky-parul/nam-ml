import json
import urllib2
import ConfigParser
import datetime

class BlackListedIPs(object):

	'''
	[{"ip":"150.164.075.187","attacks":415345,"count":1434666,"firstseen":"2017-01-20","lastseen":"2017-01-31"}]
	Count: (also reports or records) total number of packets blocked from this IP
 	Attacks: (also targets) number of unique destination IP addresses for these packets
 	
	'''
	ip_list=[]
	url=''
	num_of_ips=''
	
	def __init__(self,url,num='100'):
		d=datetime.date.today().isoformat()
		self.url=url+num+d+'?json'
		self.num_of_urls=num
		
	def get_ips(self):
		self.ip_list=json.load(urllib2.urlopen(self.url))
		print self.ip_list
		
	
		
def main():
	print 'inside main'
	config = ConfigParser.RawConfigParser()
	config.read('ConfigFile.properties')
	num='100'
	
	url=config.get('urls', 'url.attack')
	
	

	obj=BlackListedIPs(url,num)
	print obj.url
	obj.get_ips()
	print obj.ip_list

if __name__=='__main__':
	main()