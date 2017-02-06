import json
import urllib2
# nam-ml.py
# ---------

'''
	    
	You are free to use or extend this projects provided that 
    (1) you provide clear attribution to Parul Singh, singh.p@husky.neu.edu
	including a link to https://github.com/husky-parul/nam-ml and 
	(2) you retain this notice
	
	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    

 
'''

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