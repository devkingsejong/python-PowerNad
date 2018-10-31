from ..sub.target import target

class CreateAdgroupObject:
    def __init__(self, ncc_campaign_id, name, pc_channel_id, mobile_channel_id):
        self.adgroupAttrJson = {'contentsType' : 'PRODUCT'}
        self.bidAmt = None
        self.budgetLock = None
        self.contentsNetworkBidAmt = None
        self.dailyBudget = None
        self.keywordPlusWeight = None
        self.mobileChannelId = mobile_channel_id
        self.mobileNetworkBidWeight = None
        self.name = name
        self.nccCampaignId = ncc_campaign_id
        self.pcChannelId = pc_channel_id
        self.pcNetworkBidWeight = None
        self.targets = None #target object
        self.useCntsNetworkBidAmt = None
        self.useDailyBudget = None
        self.useKeywordPlus = None
        self.userLock = None
