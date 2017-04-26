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
        self.pickleAndDumpIps(self.ipDict,'top_blacklisted_ip.json')
        self.unpickleAndLoad('top_blacklisted_ip.json')


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
        ip_f=open('top_blacklisted_ip.json','rb')
        ip_dict={}
        ip_j = json.load(ip_f)
        for item in ip_j:
            item=item['ip']
            if item.get('threatfeeds'):
                ip = item['number']
                firstseen = item['mindate']
                lastseen=item['maxdate']
                asn = item['as']
                ip_obj = IP(ip, asn, '', '', firstseen,lastseen)
                ip_obj.setNetBlock()
                ip_obj.setRank()
                ip_obj.isMalicious=True
                ip_obj.setInfectionRate(True)
                ip_dict.update({ip: ip_obj})



        print 'ip_dict calculated. size is: ',len(ip_dict)
        print 'dict: ',ip_dict
        print 'pickle start'
        self.pickleAndDumpIps(ip_dict,'blacklisted_ip.ser')





    def pickleAndDumpIps(self,ip_dict,file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(ip_dict, f)

    def unpickleAndLoad(self,file_name):
        with open(file_name, 'rb') as f:
            ob = pickle.load(f)
            ip_dict=ob
        return ip_dict








obj=BlackListedIP()
# #obj.get_ip()
obj.get_ip_info()
# ip_dict =obj.unpickleAndLoad('blacklisted_ip.ser')
# count=0
#
# for k,val in ip_dict.iteritems():
#     print 'key: ',k,val.getRank(),val.getAsn(),val.getFirstSeen(),val.getLastSeen(),val.getNetBlock()
#     count+=1
#     if count==10:
#         break
#
#             # if val.getAsn()!=0:
#             #     count += 1
#     print 'Non zero asn: ',count


