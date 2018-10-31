import json

class AdKeywordObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.bidAmt = None if 'bidAmt' not in s else s['bidAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.nccKeywordId = None if 'nccKeywordId' not in s else s['nccKeywordId']
        self.nccQi = None if 'nccQi' not in s else s['nccQi']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.useGroupBidAmt = None if 'useGroupBidAmt' not in s else s['useGroupBidAmt']
        self.userLock = None if 'userLock' not in s else s['userLock']

    