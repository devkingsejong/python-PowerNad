class CreateAdExtensionObject:

    def __init__(self, pcChannelId, mobileChannelId, ownerId, type, userLock):
        
        self.pcChannelId = pcChannelId
        self.mobileChannelId = mobileChannelId
        self.ownerId = ownerId
        self.schedule = None
        self.type = type
        self.userLock = userLock