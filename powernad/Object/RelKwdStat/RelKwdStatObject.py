import json

class RelKwdStatObject:
    def __init__(self, json_def):
        
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.relKeyword = None if 'relKeyword' not in s else s['relKeyword']
        self.monthlyPcQcCnt = None if 'monthlyPcQcCnt' not in s else s['monthlyPcQcCnt']
        self.monthlyMobileQcCnt = None if 'monthlyMobileQcCnt' not in s else s['monthlyMobileQcCnt']
        self.monthlyAvePcClkCnt = None if 'monthlyAvePcClkCnt' not in s else s['monthlyAvePcClkCnt']
        self.monthlyAveMobileClkCnt = None if 'monthlyAveMobileClkCnt' not in s else s['monthlyAveMobileClkCnt']
        self.monthlyAvePcCtr = None if 'monthlyAvePcCtr' not in s else s['monthlyAvePcCtr']
        self.monthlyAveMobileCtr = None if 'monthlyAveMobileCtr' not in s else s['monthlyAveMobileCtr']
        self.plAvgDepth = None if 'plAvgDepth' not in s else s['plAvgDepth']
        self.compIdx = None if 'compIdx' not in s else s['compIdx']