import json

class ManagedKeywordInfoObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.PCPLMaxDepth = None if 'PCPLMaxDepth' not in s else s['PCPLMaxDepth']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.isAdult = None if 'isAdult' not in s else s['isAdult']
        self.isBrand = None if 'isBrand' not in s else s['isBrand']
        self.isLowSearchVolume = None if 'isLowSearchVolume' not in s else s['isLowSearchVolume']
        self.isRestricted = None if 'isRestricted' not in s else s['isRestricted']
        self.isSeason = None if 'isSeason' not in s else s['isSeason']
        self.isSellProhibit = None if 'isSellProhibit' not in s else s['isSellProhibit']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.regTm = None if 'regTm' not in s else s['regTm']