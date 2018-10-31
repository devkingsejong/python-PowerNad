import json

class ManagedCustomerLinkObject:
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.clientCustomerDelFlag = None if 'clientCustomerDelFlag' not in s else s['clientCustomerDelFlag']
        self.clientCustomerId = None if 'clientCustomerId' not in s else s['clientCustomerId']
        self.clientEnable = None if 'clientEnable' not in s else s['clientEnable']
        self.clientLoginId = None if 'clientLoginId' not in s else s['clientLoginId']
        self.clientPenaltySt = None if 'clientPenaltySt' not in s else s['clientPenaltySt']
        self.customerLinkId = None if 'customerLinkId' not in s else s['customerLinkId']
        self.description = None if 'description' not in s else s['description']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.isProxyAgency = None if 'isProxyAgency' not in s else s['isProxyAgency']
        self.linkStatus = None if 'linkStatus' not in s else s['linkStatus']
        self.managerCompanyName = None if 'managerCompanyName' not in s else s['managerCompanyName']
        self.managerCustomerDelFlag = None if 'managerCustomerDelFlag' not in s else s['managerCustomerDelFlag']
        self.managerCustomerId = None if 'managerCustomerId' not in s else s['managerCustomerId']
        self.managerEnable = None if 'managerEnable' not in s else s['managerEnable']
        self.managerName = None if 'managerName' not in s else s['managerName']
        self.managerPenaltySt = None if 'managerPenaltySt' not in s else s['managerPenaltySt']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.roleId = None if 'roleId' not in s else s['roleId']