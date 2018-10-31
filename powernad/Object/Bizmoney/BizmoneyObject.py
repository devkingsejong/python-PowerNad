import json

class BizmoneyObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.bizmoney = None if 'bizmoney' not in s else s['bizmoney']
        self.budgetLock = None if 'budgetLock' not in s else s['budgetLock']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.refundLock = None if 'refundLock' not in s else s['refundLock']