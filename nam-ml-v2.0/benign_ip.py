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
        size=0
        try:
            while True:
                self.ipDict = ips
                size+=len(result['matches'])
                for service in result['matches']:
                    ipObj = IP()
                    ipObj.ip = service['ip_str']
                    if service.get('asn'):
                        ipObj.asn = service['asn']
                    else:
                        ipObj.asn=0
                    print ipObj.getAsn(),'   ',ipObj.getIp()
                    ipObj.rank=0.0
                    ips.update({ipObj.getIp(): ipObj})


                if size<=total:
                    count+=1
                    query='port&page='+str(count)
                    if (count%10)==0:
                        print 'before sleep',time.ctime()
                        time.sleep(30)
                        print 'after sleep', time.ctime()
                    result = self.api.search(query)
                    self.ipDict = ips
                    print total, len(self.ipDict),count,size
                    self.pickleAndDumpIps(self.ipDict, '22AprShodan')

                else:
                    print total,len(ips)
                    self.ipDict=ips
                    self.pickleAndDumpIps(self.ipDict,'22AprShodan')
                    break
        except Exception as e:
            print 'Time out error occured: '
            self.pickleAndDumpIps(self.ipDict,'22AprShodan')
            new_dict=self.unpickleAndLoad('22AprShodan')
            print new_dict
            print 'Error: %s' % e
            sys.exit(1)


    def pickleAndDumpIps(self,ip_dict,file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(ip_dict, f)

    def unpickleAndLoad(self,file_name):
        ip_dict={}
        with open(file_name, 'rb') as f:
            ip_dict = pickle.load(f)
        #print len(ip_dict)
        return ip_dict

    def get_shodan(self):
        query='port'
        result=self.api.search(query)
        total=result['total']
        ips={}
        count=1
        ipObj = IP()
        with open('shodandump','ab+') as f:
            dump=''
            try:
                for s in result['matches']:
                    print s['ip_str'],'    ',s['asn']


            except Exception as e:
                print 'Time out error occured: '
                f.write(dump)
                f.write('\n')
                print 'complete'









obj=BenignIP()
#new_dict=obj.get_ip()
ip_dict={}
# new_dict=obj.unpickleAndLoad('22AprShodan')
#
# for key,val in new_dict.iteritems():
#     ip_obj = IP()
#     ip_obj.ip=key
#     if val.getAsn()!=0:
#         ip_obj.asn=val.getAsn()[2:]
#     else:
#         ip_obj.asn = str(val.getAsn())
#     ip_obj.rank=0.0
#     ip_obj.setInfectionRate(False)
#     ip_obj.isMalicious = False
#     ip_obj.setNetBlock()
#     ip_dict.update({ip_obj.ip:ip_obj})
#
# print 'new_dict', len(ip_dict)
# obj.pickleAndDumpIps(ip_dict,'22AprShodan_full.ser')
# ip_dict1=obj.unpickleAndLoad('22AprShodan_full.ser')
#
# print len(ip_dict1)
# with open('merged_benign','wb+') as f:
#     for k, val in ip_dict1.iteritems():
#         o=IP()
#         o=val
#         print 'key: ', o.getIp()+' '+str(o.getRank())+' '+str(o.getInfectionRate())+' '+o.getAsn()+' '+str(o.getNetBlockRank())+' '+o.getNetBlock()
#         f.write(o.getIp()+' '+str(o.getRank())+' '+str(o.getInfectionRate())+' '+str(o.getAsn())+' '+str(o.getNetBlockRank())+' '+o.getNetBlock())
#         f.write('\n')
# print '------------------------------------'



