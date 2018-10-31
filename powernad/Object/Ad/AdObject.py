import json
from ..Ad.sub.AdFieldObject import AdFieldObject
class AdObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.ad = None if 'ad' not in s else AdFieldObject(s['ad'])
        self.adattr = None if 'adattr' not in s else s['adattr']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectRequestMsg = None if 'inspectRequestMsg' not in s else s['inspectRequestMsg']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.nccAdId = None if 'nccAdId' not in s else s['nccAdId']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.type = None if 'type' not in s else s['type']
        self.userLock = None if 'userLock' not in s else s['userLock']