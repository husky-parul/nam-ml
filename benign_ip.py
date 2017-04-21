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
            #print ips
            for service in result['matches']:
                if service.get('asn'):
                    ipObj.ip = service['ip_str']
                    ipObj.asn = service['asn']
                    ips.update({ipObj.getIp(): ipObj})


            if len(ips)<total:
                count+=1
                query='port&page='+str(count)
                if (count%10)==0:
                    print 'before sleep',time.ctime()
                    time.sleep(30)
                    print 'after sleep', time.ctime()
                result = self.api.search(query)
                print total, len(ips)
            else:
                print total,len(ips)
                self.ipDict=ips
                self.pickleAndDumpIps(self.ipDict)
                break

    def pickleAndDumpIps(self,ipDict):
        with open('ips', 'wb') as f:
            for key,val in ipDict.iteritems():
                pickle.dump(val, f)

    def unpickleAndLoad(self):
        ipDict={}
        with open('ips', 'rb') as f:
            ob = pickle.load(f)
            ipDict.update({ob.getIp():ob})
        print len(ipDict)
        return ipDict








obj=BenignIP()
obj.get_ip()


