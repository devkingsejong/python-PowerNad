from powernad.Connector.restapi import RestApi
from powernad.Object.Stat.StatObject import StatObject
from powernad.Object.Stat.StatTypeObject import StatTypeObject
from typing import List

StatIdList = List[str]


class Stat:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_stat_by_id(self, id: str, fields: str, timeRange: str, dataPreset: str = None, timeIncrement: str = None,
                                                                                    breakdown: str = None) -> StatObject:
        query = {'id': id, 'fields': fields, 'timeRange': timeRange, 'dataPreset': dataPreset,
                     'timeIncrement': timeIncrement, 'breakdown': breakdown}
        result = self.r.get('/stats', query)
        result = StatObject(result)

        return result
        
    def get_stat_by_ids(self, ids: StatIdList, fields: str, timeRange: str, dataPreset: str= None,
                                                        timeIncrement: str = None, breakdown: str = None) -> StatObject:

        query = {'ids': ids, 'fields': fields, 'timeRange': timeRange, 'dataPreset': dataPreset,
                     'timeIncrement': timeIncrement, 'breakdown': breakdown}
        result = self.r.get('/stats', query)
        result = StatObject(result)

        return result

    def get_stat_by_type(self, id: str, statType: str) -> StatTypeObject:
        query = {'id' :id, 'statType' : statType}
        result = self.r.get('/stats', query)
        result = StatTypeObject(result)
        return result