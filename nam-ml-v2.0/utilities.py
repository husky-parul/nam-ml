import pickle

def getIpDict(file_name):
    ip_dict = unpickleAndLoad(file_name)
    return ip_dict

def pickleAndDumpIps(ip_dict,file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(ip_dict, f)

def unpickleAndLoad(file_name):
    with open(file_name, 'rb') as f:
        ob = pickle.load(f)
        ip_dict=ob
    return ip_dict