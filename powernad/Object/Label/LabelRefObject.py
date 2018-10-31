import json

class LabelRefObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.nccLabelId = None if 'nccLabelId' not in s else s['nccLabelId']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.refId = None if 'refId' not in s else s['refId']
        self.refTp = None if 'refTp' not in s else s['refTp']
        self.enable = None if 'enable' not in s else s['enable']