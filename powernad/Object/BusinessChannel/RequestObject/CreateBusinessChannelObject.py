class CreateBusinessChannelObject:
    def __init__(self, site_url, name):
        self.businessInfo = {'site' : site_url}
        self.channelTp = 'SITE'
        self.inspectRequestMsg = None
        self.name = name
