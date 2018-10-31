class CampaignUpdateObject:
    def __init__(self, lock, budget =None, period=None):
        if lock != None:
            self.userLock = bool(lock)        
        if budget != None:
            self.useDailyBudget = bool(budget)
        if period != None:
            self.usePeriod = bool(period)
