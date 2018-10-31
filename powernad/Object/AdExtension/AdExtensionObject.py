import json

class AdExtensionObject:

    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)

        s = json_def

        self.customerId = None if 'customerId' not in s else s['customerId']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.mobileChannelId = None if 'mobileChannelId' not in s else s['mobileChannelId']
        self.nccAdExtensionId = None if 'nccAdExtensionId' not in s else s['nccAdExtensionId']
        self.ownerId = None if 'ownerId' not in s else s['ownerId']
        self.pcChannelId = None if 'pcChannelId' not in s else s['pcChannelId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.type = None if 'type' not in s else s['type']
        self.userLock = None if 'userLock' not in s else s['userLock']