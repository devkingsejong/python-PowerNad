import json
class BizmoneyCostObject:
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.adjustedNonRefundableAmt = None if 'adjustedNonRefundableAmt' not in s else s['adjustedNonRefundableAmt']
        self.adjustedRefundableAmt = None if 'adjustedRefundableAmt' not in s else s['adjustedRefundableAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.date = None if 'date' not in s else s['date']
        self.device = None if 'device' not in s else s['device']
        self.networkType = None if 'networkType' not in s else s['networkType']
        self.nonRefundableAmt = None if 'nonRefundableAmt' not in s else s['nonRefundableAmt']
        self.productCode = None if 'productCode' not in s else s['productCode']
        self.refundableAmt = None if 'refundableAmt' not in s else s['refundableAmt']