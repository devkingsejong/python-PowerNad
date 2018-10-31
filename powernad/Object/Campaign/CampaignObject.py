# pylint: disable=C0103

import json

class CampaignObject():
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)

        s = json_def

        self.campaignTp = None if 'campaignTp' not in s else s['campaignTp']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.dailyBudget = None if 'dailyBudget' not in s else s['dailyBudget']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.deliveryMethod = None if 'deliveryMethod' not in s else s['deliveryMethod']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.expectCost = None if 'expectCost' not in s else s['expectCost']
        self.migType = None if 'migType' not in s else s['migType']
        self.name = None if 'name' not in s else s['name']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.periodEndDt = None if 'periodEndDt' not in s else s['periodEndDt']
        self.periodStartDt = None if 'periodStartDt' not in s else s['periodStartDt']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.trackingMode = None if 'trackingMode' not in s else s['trackingMode']
        self.trackingUrl = None if 'trackingUrl' not in s else s['trackingUrl']
        self.useDailyBudget = None if 'useDailyBudget' not in s else s['useDailyBudget']
        self.usePeriod = None if 'usePeriod' not in s else s['usePeriod']
        self.userLock = None if 'userLock' not in s else s['userLock']
        
