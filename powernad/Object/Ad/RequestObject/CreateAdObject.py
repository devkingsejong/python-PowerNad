class CreateAdObject:
    def __init__(self, adObject, nccAdgroupId, type):
        self.ad = adObject
        self.inspectRequestMsg = None
        self.nccAdgroupId = nccAdgroupId
        self.type = type
        self.userLock = None