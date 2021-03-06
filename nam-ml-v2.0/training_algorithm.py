

class Intution:
    def __init__(self,black_listed_ips={},benign_ips={}):
        self.black_listed_ips=black_listed_ips
        self.benign_ips=benign_ips
        self.evilModels={}
        self.benignModels={}
        self.nbr={}


    def getModels(self):
        evil_models=self.computeNetBlockRank(self.black_listed_ips)
        benign_models = self.computeNetBlockRank(self.benign_ips)

        return evil_models,benign_models



    def computeNetBlockRank(self,ip_dict):

        visited_ipo={}

        for key,ip_obj in ip_dict.iteritems():
            x=(ip_obj.getAsn(),ip_obj.getNetBlock())
            if x in visited_ipo:
                if ip_obj.isMalicious:
                    new_score =visited_ipo.get(x)[1] + ip_obj.getNetBlockRank()
                    new_score=new_score+pow(new_score%10,2)

                else:
                    new_score = visited_ipo.get(x)[1] + ip_obj.getNetBlockRank()

                model = (x, new_score)
                visited_ipo.update({x:model})
                ip_obj.netblockRank = new_score
            else:
                if ip_obj.isMalicious:
                    new_score=ip_obj.getNetBlockRank()
                    new_score=new_score+pow(new_score%10,2)
                else:
                    new_score = ip_obj.getNetBlockRank()
                model = (x, new_score)
                visited_ipo.update({x: model})
                ip_obj.netblockRank = new_score
        visited_ipo=self.normalizeScore(visited_ipo)

        return visited_ipo

    def convert_dict_to_list(self,dict):
        models=[]
        for k,model in dict.iteritems():
            models.append(model)

        return models

    def normalizeScore(self,ipo_dict):
        new_ipo_dict={}
        for key,model in ipo_dict.iteritems():
            score = model[1]
            score = float(score) / 16.0
            new_ipo_dict.update({key:(model[0],score)})

        return new_ipo_dict

    def getDataSet(self):
        x=[]
        y=[]
        self.evilModels=self.computeNetBlockRank(self.black_listed_ips)
        self.benignModels=self.computeNetBlockRank(self.benign_ips)
        for k,o in self.black_listed_ips.iteritems():
            m=(o.getAsn(),o.getNetBlock())
            val=self.evilModels.get(m)
            x.append([o.getInfectionRate(),o.getRank(),val[1]])
            y.append(1)

        for k,o in self.benign_ips.iteritems():
            m = (o.getAsn(), o.getNetBlock())
            val = self.benignModels.get(m)
            x.append([o.getInfectionRate(), o.getRank(), val[1]])
            y.append(0)

        return x,y

    def getDataSetWithOneFeature(self):
        x,y=self.getDataSet()
        X=[]
        for item in x:
            X.append(item[0])
        return X,y

    def getDataSetWithTwoFeatures(self):
        x,y=self.getDataSet()
        X=[]
        for item in x:
            X.append([item[0],item[1]])
        return X,y





