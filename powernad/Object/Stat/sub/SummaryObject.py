import json

class SummaryObject:
    def __init__(self, json_def):
        
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.dateEnd = None if 'dateEnd' not in s else s['dateEnd']
        self.dateStart = None if 'dateStart' not in s else s['dateStart']
