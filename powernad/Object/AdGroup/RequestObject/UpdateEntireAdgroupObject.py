class UpdateEntireAdgroupObject:
    def __init__(self, bidAmt, contentsNetworkBidAmt, dailyBudget, keywordPlusWeight, mobileNetworkBidWeight, nccAdgroupId,
                    pcNetworkBidWeight, useCntsNetworkBidAmt, useDailyBudget, useKeywordPlus, userLock):
     self.bidAmt = bidAmt
     self.budgetLock = None
     self.contentsNetworkBidAmt = contentsNetworkBidAmt
     self.dailyBudget = dailyBudget
     self.keywordPlusWeight = keywordPlusWeight
     self.mobileChannelId = None
     self.mobileNetworkBidWeight = mobileNetworkBidWeight
     self.name = None
     self.nccAdgroupId = nccAdgroupId
     self.nccCampaignId = None
     self.pcNetworkBidWeight = pcNetworkBidWeight
     #self.targts = None
     self.useCntsNetworkBidAmt = useCntsNetworkBidAmt
     self.useDailyBudget = useDailyBudget
     self.useKeywordPlus = useKeywordPlus
     self.userLock = userLock