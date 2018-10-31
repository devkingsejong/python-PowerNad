# pylint: disable=C0103
# pylint: disable=E0401

import json
from ..AdGroup.sub.target import target
from ..AdGroup.sub.targetSummaryObject import targetSummaryObject
from ..AdGroup.sub.adgroupAttrJson import adgroupAttrObject
class AdgroupObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.adgroupAttrJson = None if 'adgroupAttrJson' not in s else self.__match_group_attr(s['adgroupAttrJson'])
        self.bidAmt = None if 'bidAmt' not in s else s['bidAmt']
        self.budgetLock = None if 'budgetLock' not in s else s['budgetLock']
        self.contentsNetworkBidAmt = None if 'contentsNetworkBidAmt' not in s else s['contentsNetworkBidAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.dailyBudget = None if 'dailyBudget' not in s else s['dailyBudget']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.expectCost = None if 'expectCost' not in s else s['expectCost']
        self.keywordPlusWeight = None if 'keywordPlusWeight' not in s else s['keywordPlusWeight']
        self.migType = None if 'migType' not in s else s['migType']
        self.mobileChannelId = None if 'mobileChannelId' not in s else s['mobileChannelId']
        self.mobileChannelKey = None if 'mobileChannelKey' not in s else s['mobileChannelKey']
        self.mobileNetworkBidWeight = None if 'mobileNetworkBidWeight' not in s else s['mobileNetworkBidWeight']
        self.name = None if 'name' not in s else s['name']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.pcChannelId = None if 'pcChannelId' not in s else s['pcChannelId']
        self.pcChannelKey = None if 'pcChannelKey' not in s else s['pcChannelKey']
        self.pcNetworkBidWeight = None if 'pcNetworkBidWeight' not in s else s['pcNetworkBidWeight']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.targets = None if 'targets' not in s else self.__match_target(s['targets'])
        self.targetSummary = None if 'targetSummary' not in s else self.__match_target_summary(s['targetSummary'])
        self.useCntsNetworkBidAmt = None if 'useCntsNetworkBidAmt' not in s else s['useCntsNetworkBidAmt']
        self.useDailyBudget = None if 'useDailyBudget' not in s else s['useDailyBudget']
        self.useKeywordPlus = None if 'useKeywordPlus' not in s else s['useKeywordPlus']
        self.userLock = None if 'userLock' not in s else s['userLock']


    def __match_target(self, sarray):
        target_list = []
        for arr in sarray:
            target_item = target(arr)
            target_list.append(target_item)

        return target_list

    def __match_target_summary(self, sarray):
       summary = targetSummaryObject(sarray)
       return summary

    def __match_group_attr(self, sarray):
        attr = adgroupAttrObject(sarray)
        return attr