import json

class target:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.nccTargetId = None if 'nccTargetId' not in s else s['nccTargetId']
        self.ownerId = None if 'ownerId' not in s else s['ownerId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.target = None if 'target' not in s else s['target']
        self.targetTp = None if 'targetTp' not in s else s['targetTp']
