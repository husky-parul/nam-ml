import time,datetime,ConfigParser
import shodan
import sys,pickle,json,urllib2,os
from ip import IP

class BlackListedIP(object):

    def __init__(self,ipDict={}):
        d = datetime.date.today().isoformat()
        self.config = ConfigParser.RawConfigParser()
        self.config.read('ConfigFile.properties')
        self.url=self.config.get('dshield','url.attack')
        self.ipDict=ipDict


    def get_ip(self):
        d = datetime.date.today().isoformat()
        print d
        url = self.url + str(10000)+'/'+ d + '?json'
        print url
        ipObj = IP()
        ips={}
        top_ips = json.load(urllib2.urlopen(url))
        # count=0
        # earlier = datetime.datetime.now()

        print len(top_ips)
        for i in top_ips:
            ip=i['ip']
            ipObj.ip=ip
            ips.update({ip:ipObj})

        self.ipDict=ips
        self.pickleAndDumpIps(self.ipDict)
        self.unpickleAndLoad()
            # if len(ips)!=11000:
            #     count+=1
            #     DD = datetime.timedelta(days=365)
            #     today = earlier
            #     print 'today', today
            #     earlier = today - DD
            #     print 'earlier: ',earlier
            #     earlier_str = earlier.strftime("%Y-%m-%d")
            #     url = self.url + str(10000) + '/' + earlier_str + '?json'
            #     top_ips = json.load(urllib2.urlopen(url))
            #     print 'count: ',count
            # else:
            #     print count
            #     break

    def get_ips(self):
        ip_dict = self.unpickleAndLoad()
        with open('top_blacklisted_ip.json', 'w') as outfile:
            outfile.write('[')
            for k, val in ip_dict.iteritems():
                ip_info_url = self.config.get('dshield', 'url.ip')
                ip_info_url = ip_info_url + k + '?json'
                print ip_info_url
                ip_info = json.load(urllib2.urlopen(ip_info_url))
                json.dump(ip_info, outfile)
                outfile.write(',')

        with open('top_blacklisted_ip.json', 'rb+') as outfile:
            outfile.seek(-1, os.SEEK_END)
            outfile.truncate()

        with open('top_blacklisted_ip.json', 'ab+') as outfile:
            outfile.write(']')

    def get_ip_info(self):
        ip_dict=self.unpickleAndLoad()
        for k,val in ip_dict.iteritems():
            ip_info_url=self.config.get('dshield','url.ip')
            ip_info_url=ip_info_url+k+'?json'
            print ip_info_url
            ip_info=json.load(urllib2.urlopen(ip_info_url))
            print '1111',ip_info
            print '2222', type(ip_info)
            for k,val in ip_info.iteritems():
                print 'item',k,val

        for k,val in ip_dict.iteritems():
            print val.getAsn()




    def pickleAndDumpIps(self,ip_dict):
        with open('black_ips', 'wb') as f:
            pickle.dump(ip_dict, f)

    def unpickleAndLoad(self):
        with open('black_ips', 'rb') as f:
            ob = pickle.load(f)
            ip_dict=ob
        return ip_dict








obj=BlackListedIP()
#obj.get_ip()
obj.get_ips()


