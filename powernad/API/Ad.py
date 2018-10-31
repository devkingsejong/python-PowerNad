import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.Ad.AdObject import AdObject
from powernad.Object.Ad.RequestObject.CreateAdObject import CreateAdObject
from powernad.Object.Ad.RequestObject.UpdateAdObject import UpdateAdObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

AdIdList = List[str]
AdObjectList = List[AdObject]
ChangeFieldsList = List[str]


class Ad: #광고 소재에 관한 API입니다.

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_ad_list_by_ids(self, ids: AdIdList) -> AdObjectList:
        ids = ",".join(ids)
        ids = {'ids' : ids}
        result = self.r.get('/ncc/ads', ids)
        ad_obj_list = []
        for arr in result:
            ad_obj = AdObject(arr)
            ad_obj_list.append(ad_obj)

        return ad_obj_list
        
    def get_ad_list(self, nccAdGroupId: str) -> AdObjectList:
        result = self.r.get('/ncc/ads', {'nccAdgroupId': nccAdGroupId})
        adobj_list = []
        for arr in result:
            ad_obj = AdObject(arr)
            adobj_list.append(ad_obj)

        return adobj_list

    def get_ad(self, adId: str) -> AdObject:
        result = self.r.get('/ncc/ads/' + adId)
        result = AdObject(result)
        return result

    def create_ad(self, CreateAdObject: CreateAdObject) -> AdObject:
        data = jsonpickle.encode(CreateAdObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = data
        data_str = json.dumps(data_str)
        result = self.r.post('/ncc/ads', data_str)
        result = AdObject(result)
        return result

    def update_ad(self, adId: str, fields: ChangeFieldsList, UpdateAdObject: UpdateAdObject) -> AdObject:
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        data = jsonpickle.encode(UpdateAdObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = data
        data_str = json.dumps(data_str)
        result = self.r.put('/ncc/ads/' + adId, data_str, query)
        result = AdObject(result)
        return result

    def delete_ad(self, adId: str):
        self.r.delete('/ncc/ads/' + adId)
        return True

    def copy_ad(self, adId: str, targetAdGroupId: str, userLock: bool) -> AdObject:
        query = {'ids' : adId, 'targetAdgroupId' : targetAdGroupId, 'userLock' : userLock}
        result = self.r.put('/ncc/ads', None, query)
        result = AdObject(result)
        return result
