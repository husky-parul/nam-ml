class IP(object):
    def __int__(self,ip,asn,asname,netblock):
        self.ip=ip
        self.asn=asn
        self.asname=asname
        self.netblock=netblock

    def getIp(self):
        return self.ip

    def getAsn(self):
        return self.asn

    def getAsnName(self):
        return self.asname

    def getNetBlock(self):
        return self.netblock