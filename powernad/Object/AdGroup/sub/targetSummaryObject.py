import json

class targetSummaryObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.media = None if 'media' not in s else s['media']
        self.pcMobile = None if 'pcMobile' not in s else s['pcMobile']
        self.region = None if 'region' not in s else s['region']
        self.time = None if 'time' not in s else s['time']
        self.week = None if 'week' not in s else s['week']
