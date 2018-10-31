import json
from ..BusinessChannel.sub.BusinessInfo import BusinessInfo
class BusinessChannelObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.adultStatus = None if 'adultStatus' not in s else s['adultStatus']
        self.blackStatus = None if 'blackStatus' not in s else s['blackStatus']
        self.businessInfo = None if 'businessInfo' not in s else BusinessInfo(s['businessInfo'])
        self.channelKey = None if 'adultStatus' not in s else s['adultStatus']
        self.channelTp = None if 'adultStatus' not in s else s['adultStatus']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.enabled = None if 'enabled' not in s else s['enabled']
        self.firstChargeTm = None if 'firstChargeTm' not in s else s['firstChargeTm']
        self.inspectTm = None if 'inspectTm' not in s else s['inspectTm']
        self.mobileInspectStatus = None if 'mobileInspectStatus' not in s else s['mobileInspectStatus']
        self.name = None if 'name' not in s else s['name']
        self.nccBusinessChannelId = None if 'nccBusinessChannelId' not in s else s['nccBusinessChannelId']
        self.pcInspectStatus = None if 'pcInspectStatus' not in s else s['pcInspectStatus']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
