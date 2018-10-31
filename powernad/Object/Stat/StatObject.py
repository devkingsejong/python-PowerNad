import json
from ..Stat.sub.StatDataObject import StatDataObject
from ..Stat.sub.SummaryObject import SummaryObject
class StatObject:
    
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.data = None if 'data' not in s else self.match_data(s['data']) #list
        self.summary = None if 'data' not in s else SummaryObject(s['data'])

    def match_data(self, s):

        stat_list = []
        for arr in s:
            stat = StatDataObject(arr)
            stat_list.append(stat)

        return stat_list