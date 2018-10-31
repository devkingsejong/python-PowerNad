import json

class IpExclusionObject:
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.customerId = None if 'customerId' not in s else s['customerId']
        self.filterIp = None if 'filterIp' not in s else s['filterIp']
        self.ipFilterId = None if 'ipFilterId' not in s else s['ipFilterId']
        self.memo = None if 'memo' not in s else s['memo']
        self.regTm = None if 'regTm' not in s else s['regTm']