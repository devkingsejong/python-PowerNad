class CampaignAddObject:
    
    def __init__(self, customerId, campaignTp, name):
        self.customerId = customerId
        self.campaignTp = campaignTp
        self.dailyBudget = None
        self.deliveryMethod = None
        self.name = name
        self.periodEndDt = None
        self.periodStartDt = None
        self.trackingMode = None
        self.trackingUrl = None
        self.useDailyBudget = None
        self.usePeriod = None
        self.userLock = None