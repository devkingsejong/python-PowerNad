import json
from ..AdKeyword.sub.ManagedKeywordInfoObject import ManagedKeywordInfoObject

class ManagedKeywordObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.keyword = None if 'keyword' not in s else s['keyword']
        self.managedKeyword = None if 'managedKeyword' not in s else ManagedKeywordInfoObject(s['managedKeyword'])
    

