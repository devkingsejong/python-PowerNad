class UpdateBusinessChannelObject:
    def __init__(self, nccBusinessChannelId, site_url, name):
        self.businessInfo = {'site' : site_url}
        self.channelTp = 'SITE'
        self.inspectRequestMsg = None
        self.name = name
        self.nccBusinessChannelId = nccBusinessChannelId
