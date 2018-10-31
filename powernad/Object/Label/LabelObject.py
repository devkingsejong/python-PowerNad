import json

class LabelObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.color = None if 'color' not in s else s['color']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.name = None if 'name' not in s else s['name']
        self.nccLabelId = None if 'nccLabelId' not in s else s['nccLabelId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.editTm = None if 'editTm' not in s else s['editTm']
        