class UpdateAdObject:
    def __init__(self, adAttr, nccAdId):
        self.adAttr = adAttr
        self.inspectRequestMsg = None
        self.nccAdId = nccAdId
        self.userLock = None