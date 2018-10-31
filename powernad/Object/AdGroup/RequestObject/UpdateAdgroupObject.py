class UpdateAdgroupObject:
    def __init__(self, bidAmt = None, userLock = None, useKeywordPlus = None, networkBidWeight = None, 
    targetLocation = None, targetTime = None, targetMedia = None):
        self.bidAmt = bidAmt
        self.userLock = userLock
        self.useKeywordPlus = useKeywordPlus
        self.useCntsNetworkBidAmt = networkBidWeight
        #self.target = self.make_target_obj(targetLocation, targetTime, targetLocation)
        self.targetLoaction = targetLocation
        self.targetTime = targetTime
        self.targetMedia = targetMedia
    

    def make_target_obj(self,nccTargetId, ownerId,  targetLocation, targetTime, targetLoaction):
        target_obj = []
        if targetLoaction != None:
            target_obj.append(targetLoaction) 
        if targetTime != None:
            target_obj.append(targetTime)
        if targetLoaction != None:
            targetLoaction.append(targetLoaction)

        return targetLoaction
        
