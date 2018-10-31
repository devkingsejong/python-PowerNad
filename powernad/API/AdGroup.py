# pylint: disable=C0103
# pylint: disable=E0401
from powernad.Connector.restapi import RestApi
from powernad.Object.AdGroup.RestrictedKeyword import RestrictedKeyword
from powernad.Object.AdGroup.RequestObject.RestrictedKeywordsObject import RestrictedKeywordsObject
from powernad.Object.AdGroup.RequestObject.UpdateEntireAdgroupObject import UpdateEntireAdgroupObject
from powernad.Object.AdGroup.RequestObject.CreateAdgroupObject import CreateAdgroupObject
from powernad.Object.AdGroup.RequestObject.UpdateAdgroupObject import UpdateAdgroupObject
from powernad.Object.AdGroup.AdgroupObject import AdgroupObject
from powernad.Common.CommonFunctions import CommonFunctions
import json
import jsonpickle
from typing import List

RestrictedKeywordsAddObject = List[RestrictedKeywordsObject]
RestrictedKeywordList = List[RestrictedKeyword]
AdGroupList = List[AdgroupObject]
AdGroupIdList = List[str]
RestrictedKeywordIdList = List[str]
ChangeFieldsList = List[str]


class AdGroup:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)
    
    def get_restricted_keyword(self, adgroupId: str) -> RestrictedKeywordList:
        query = {'type': 'KEYWORD_PLUS_RESTRICT'}
        result = self.r.get('/ncc/adgroups/' + adgroupId + "/restricted-keywords", query);
        restricted_list = []
        for arr in result:
            restricted_keyword = RestrictedKeyword(arr)
            restricted_list.append(restricted_keyword)

        return restricted_list
    
    def get_adgroup_list(self, nccCampaignId: str = None, baseSearchId: str = None,
                                                            recordSize: int = None, selector: str = None) -> AdGroupList:

        query = {'nccCampaignId' : nccCampaignId, 'baseSearchId' : baseSearchId,
                 'record_size': recordSize, 'selector' : selector}
        result = self.r.get('/ncc/adgroups', query)
        
        adgroup_list = []
        for arr in result:
            camp = AdgroupObject(arr)
            adgroup_list.append(camp)

        return adgroup_list
    
    def get_adgroup_list_by_ids(self, ids: AdGroupIdList) -> AdGroupList:
        ids = ",".join(ids)
        query = {'ids' : ids}
        result = self.r.get('/ncc/adgroups', query)
        adgroup_list = []
        for arr in result:
            camp = AdgroupObject(arr)
            adgroup_list.append(camp)

        return adgroup_list

    def get_adgroup_by_adgroupid(self, adgroupId: str) -> AdgroupObject:
        result = self.r.get('/ncc/adgroups/'+adgroupId)
        adgroup = AdgroupObject(result)
        return adgroup

    def create_restricted_keyword(self, adgroupId: str, restricted_keywords_object: RestrictedKeywordsAddObject) -> RestrictedKeyword:
        data = jsonpickle.encode(restricted_keywords_object, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = [data]
        data_str = json.dumps(data_str);
        result = self.r.post('/ncc/adgroups/%s/restricted-keywords' % str(adgroupId), data_str)
        restrict_keyword = RestrictedKeyword(result)

        return restrict_keyword

    def create_adgroup(self, create_adgroup_object: CreateAdgroupObject):
        data = jsonpickle.encode(create_adgroup_object, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.post('/ncc/adgroups', data_str)
        result = AdgroupObject(result)
        return result
    
    def update_adgroup(self, adgroupId: str, fields: ChangeFieldsList, UpdateAdgroupObject: UpdateAdgroupObject):
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        data = jsonpickle.encode(UpdateAdgroupObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.put('/ncc/adgroups/' + adgroupId, data_str, query)
        result = AdgroupObject(result)
        return result
    
    def update_adgroup_entire(self, adgroupId: str, UpdateEntireAdgroupObject: UpdateEntireAdgroupObject):
        data = jsonpickle.encode(UpdateEntireAdgroupObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.put('/ncc/adgroups/' + adgroupId, data_str)
        result = AdgroupObject(result)
        return result

    def delete_group_restricted_keyword(self, adgroupId: str, res_keyword_ids: RestrictedKeywordIdList):
        res_keyword_ids = ",".join(res_keyword_ids)
        query = {'ids': res_keyword_ids}
        result = self.r.delete('/ncc/adgroups/%s/restricted-keywords' % str(adgroupId), query)
        return True

    def delete_adgroup(self, adgroupId: str):
        result = self.r.delete('/ncc/adgroups/' + adgroupId)
        return True