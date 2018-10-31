import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.AdKeyword.AdKeywordObject import AdKeywordObject
from powernad.Object.AdKeyword.ManagedKeywordObject import ManagedKeywordObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

AdKeywordList = List[AdKeywordObject]
AdKeywordIdList = List[str]
KeywordsList = List[str]


class AdKeyword:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_adkeyword_list_by_label_id(self, nccLabelId: str) -> AdKeywordList:
        query = {'nccLabelId': nccLabelId}
        result = self.r.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list
    
    def get_adkeyword_list_by_ids(self, ids: AdKeywordIdList) -> AdKeywordList:
        ids = ",".join(ids)
        query = {'ids' : ids}
        result = self.r.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list
        

    def get_adkeyword_list_by_group_id(self, nccAdgroupId: str= None, baseSearchId:str =None,
                                                            recordSize: int = None, selector:str = None) -> AdKeywordList:

        query = {'nccAdgroupId' : nccAdgroupId, 'baseSearchId' : baseSearchId, 'recordSize' : recordSize,
                                                                                                'selector' : selector}
        result = self.r.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list

    
    def get_adkeyword(self, nccKeywordId) -> AdKeywordObject:
        result = self.r.get('/ncc/keywords/' + nccKeywordId)
        result = AdKeywordObject(result)
        return result

    def create_adkeyword(self, nccAdgroupId, CreateAdKeywordObject) -> AdKeywordObject:
        data = jsonpickle.encode(CreateAdKeywordObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data =  [data]
        data_str = json.dumps(data)

        result = self.r.post('/ncc/keywords', data_str, {'nccAdgroupId' : nccAdgroupId})
        result = AdKeywordObject(result)
        return result

    def update_adkeyrword(self, nccKeywordId, fields, UpdateAdKeywordObject) -> AdKeywordObject:
        data = jsonpickle.encode(UpdateAdKeywordObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        query = {'fields' : fields}

        result = self.r.put('/ncc/keywords/'+nccKeywordId, data_str, query)
        result = AdKeywordObject(result)

        return result

    def delete_adkeyword(self, nccKeywordId: str):
        self.r.delete('/ncc/keywords/' + nccKeywordId)
        return True

    def delete_adkeyword_many(self, ids: AdKeywordIdList):
        ids = ",".join(ids)
        query = {'ids' : ids}
        self.r.delete('/ncc/keywords', query)

    def managed_keyword_list(self, keywords: KeywordsList) -> ManagedKeywordObject:
        keywords = ",".join(keywords)
        query = {'keywords': keywords}
        result = self.r.get('/ncc/managedKeyword', query)

        managedkeyword_list = []
        for arr in result:
            managedkeyword = ManagedKeywordObject(arr)
            managedkeyword_list.append(managedkeyword)

        return managedkeyword_list