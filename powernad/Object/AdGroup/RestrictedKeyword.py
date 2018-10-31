import json
class RestrictedKeyword:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccAdgroupRestrictKwdId = None if 'nccAdgroupRestrictKwdId' not in s else s['nccAdgroupRestrictKwdId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.type = None if 'type' not in s else s['type']