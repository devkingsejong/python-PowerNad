import json

class EstimateMedianObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)

        s = json_def

        self.bid = None if 'bid' not in s else s['bid']
        self.keyword = None if 'keyword' not in s else s['keyword']