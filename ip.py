import datetime
from datetime import date

class IP:
    def __init__(self, ip='', asn='',asname='',netblock='',firstseen=''):
        self.ip = ip
        self.asn = asn
        self.asname = asname
        self.netblock = netblock
        self.firstseen = firstseen

    def getIp(self):
        return self.ip

    def getAsn(self):
        return self.asn

    def getAsnName(self):
        return self.asname

    def getNetBlock(self):
        i= self.ip.rfind('.')
        return self.ip[:8]+'.0'

    def get_rank(self):
        diff=self.getDateDiff('2017-03-21')
        rank=1.0
        for i in range(1,diff):
            rank*=0.89
        return rank

    def getDateDiff(self,firstseen):
        d = datetime.date.today().isoformat().split('-')
        print 'd', d
        y = d[0]
        m = d[1]
        days = d[2]
        d = date(int(y), int(m), int(days))
        print 'd: ', d

        today = firstseen.split('-')
        print today
        ty = today[0]
        tm = today[1]
        tdays = today[2]
        today = date(int(ty), int(tm), int(tdays))
        print 'today', today

        earlier = d - today

        return earlier.days




x = IP('10.10.10.10')
print x.ip, x.asn
print x.getNetBlock()
print x.get_rank()


