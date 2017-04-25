import datetime
from datetime import date

class IP(object):
    def __init__(self, ip='', asn='',asname='',netblock='',firstseen='',lastseen=''):
        self.ip = ip
        self.asn = asn
        self.asname = asname
        self.netblock = netblock
        self.firstseen = firstseen
        self.rank=0.0 #attenuated score
        self.netblockRank=1.0
        self.infectionRate=0.0
        self.lastseen=lastseen
        self.isMalicious=False

    def setInfectionRate(self,is_malicious=True):
        if is_malicious:
            self.infectionRate=10.0
        else:
            self.infectionRate=0.0

    def getInfectionRate(self):
        return self.infectionRate

    def setNetblockRank(self):
        self.netblockRank=1.0

    def getNetBlockRank(self):
        return self.netblockRank

    def getLastSeen(self):
        return self.lastseen

    def getIp(self):
        return self.ip

    def getAsn(self):
        return self.asn

    def getAsnName(self):
        return self.asname

    def getFirstSeen(self):
        return self.firstseen

    def setNetBlock(self):
        i= self.ip.rfind('.')
        self.netblock=self.ip[:i]+'.0'


    def getNetBlock(self):
        return self.netblock

    def setRank(self):
        import math
        if self.isMalicious:
            diff = self.getDateDiff(self.getFirstSeen(),self.getLastSeen())
            rank =1.0*diff
            today= datetime.date.today().isoformat()
            diff=self.getDateDiff(self.getLastSeen(),today)
            rank=rank*pow(.89,diff)
            self.rank=round(rank,6)
        else:
            self.rank=1

    def getRank(self):
        return self.rank

    def getDateDiff(self,stat_date,end_date):

        d = end_date.split('-')
        y = d[0]
        m = d[1]
        days = d[2]
        d = date(int(y), int(m), int(days))

        today = stat_date.split('-')
        ty = today[0]
        tm = today[1]
        tdays = today[2]
        today = date(int(ty), int(tm), int(tdays))

        earlier = d - today
        # print 'today:',today
        # print 'd: ',d
        # print 'days gap: ',earlier.days
        return earlier.days




# x = IP('10.10.10.10')
# print x.ip, x.asn
# print x.getNetBlock()
# print x.get_rank()


# class IP(object):
#     def __init__(self, ip='', asn='',asname='',netblock='',firstseen=''):
#         self.ip = ip
#         self.asn = asn
#         self.asname = asname
#         self.netblock = netblock
#         self.rank=0.0
#         self.firstseen=''

# ((ASN,NET),2)
