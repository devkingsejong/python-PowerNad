import json

class adgroupAttrObject:
    def __init__(self, json_def=None):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.campaignTp = None if 'campaignTp' not in s else s['campaignTp']