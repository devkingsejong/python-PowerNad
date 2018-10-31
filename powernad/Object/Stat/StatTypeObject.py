import json


class StatTypeObject:

    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.clkCnt = None if 'clkCnt' not in s else s['clkCnt']
        self.drtCrto = None if 'drtCrto' not in s else s['drtCrto']
        self.salesAmt = None if 'salesAmt' not in s else s['salesAmt']
        self.schKeyword = None if 'schKeyword' not in s else s['schKeyword']

