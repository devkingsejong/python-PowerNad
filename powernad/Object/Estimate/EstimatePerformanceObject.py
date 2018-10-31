import json

class EstimatePerformanceObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)

        s = json_def

        self.bid = None if 'bid' not in s else s['bid']
        self.clicks = None if 'clicks' not in s else s['clicks']
        self.cost = None if 'cost' not in s else s['cost']
        self.impressions = None if 'impressions' not in s else s['impressions']