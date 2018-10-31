import json

class StatDataObject:
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.avgRnk = None if 'avgRnk' not in s else s['avgRnk']
        self.ccnt = None if 'ccnt' not in s else s['ccnt']
        self.clkCnt = None if 'clkCnt' not in s else s['clkCnt']
        self.cpc = None if 'cpc' not in s else s['cpc']
        self.ctr = None if 'ctr' not in s else s['ctr']
        self.dateEnd = None if 'dateEnd' not in s else s['dateEnd']
        self.dateStart = None if 'dateStart' not in s else s['dateStart']
        self.drtCrto = None if 'drtCrto' not in s else s['drtCrto']
        self.impCnt = None if 'impCnt' not in s else s['impCnt']
        self.salesAmt = None if 'salesAmt' not in s else s['salesAmt']