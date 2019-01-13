from powernad.Connector.restapi import RestApi
from powernad.Object.RelKwdStat.RelKwdStatObject import RelKwdStatObject
from typing import List
RelKwdStatObjectList = List[RelKwdStatObject]


class RelKwdStat:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_rel_kwd_stat_list(self, siteId: str = None, biztpId: int = None, hintKeywords: str = None, event: int = None,
                              month: int = None, showDetail: int = None) -> RelKwdStatObjectList:

        query = {'siteId': siteId, 'biztpId': biztpId, 'hintKeywords': hintKeywords,
                                                             'event': event, 'month': month, 'showDetail': showDetail}
        result = self.r.get('/keywordstool', query)
        result = result['keywordList']
        relstat_list = []

        for arr in result:
            relstat = RelKwdStatObject(arr)
            relstat_list.append(relstat)

        return relstat_list
