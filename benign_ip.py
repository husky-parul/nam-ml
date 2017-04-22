import time,datetime,ConfigParser
import shodan
import sys,pickle
from ip import IP

class BenignIP(object):

    def __init__(self,ipDict={}):
        d = datetime.date.today().isoformat()
        self.config = ConfigParser.RawConfigParser()
        self.config.read('ConfigFile.properties')
        self.url=self.config.get('shodan','shodan.url')
        self.apikey=self.config.get('shodan','shodan.apikey')
        self.api = shodan.Shodan(self.apikey)
        self.ipDict=ipDict


    def get_ip(self):
        query='port'
        result=self.api.search(query)
        total=result['total']
        ips={}
        count=1
        ipObj = IP()

        while True:
            self.ipDict = ips
            for service in result['matches']:
                if service.get('asn'):
                    ipObj.ip = service['ip_str']
                    ipObj.asn = service['asn']
                    ips.update({ipObj.getIp(): ipObj})


            if (count*10)<total:
                count+=1
                query='port&page='+str(count)
                if (count%10)==0:
                    print 'before sleep',time.ctime()
                    time.sleep(30)
                    print 'after sleep', time.ctime()
                result = self.api.search(query)
                self.ipDict = ips
                print total, len(self.ipDict),count

            else:
                print total,len(ips)
                self.ipDict=ips
                self.pickleAndDumpIps(self.ipDict)
                break

    def pickleAndDumpIps(self,ip_dict,file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(ip_dict, f)

    def unpickleAndLoad(self,file_name):
        ip_dict={}
        with open(file_name, 'rb') as f:
            ip_dict = pickle.load(f)
        print len(ip_dict)
        return ip_dict







# try:
#     obj=BenignIP()
#     obj.get_ip()
#
# except Exception as e:
#         print 'Time out error occured: '
#         obj.pickleAndDumpIps(obj.ipDict)
#         new_dict=obj.unpickleAndLoad()
#         print 'Error: %s' % e
#         sys.exit(1)
obj=BenignIP()
new_dict=obj.unpickleAndLoad('benign_ips')
ip_dict={}
ip_obj=IP()
for key,val in new_dict.iteritems():
    ip_obj.ip=key
    ip_obj.asn=val.getAsn()[2:]
    ip_obj.rank=0.0
    ip_obj.setNetBlock()
    ip_dict.update({key:ip_obj})
print len(new_dict)
print len(ip_dict)
obj.pickleAndDumpIps(ip_dict,'full_benign_ip')
print len(obj.unpickleAndLoad('full_benign_ip'))


