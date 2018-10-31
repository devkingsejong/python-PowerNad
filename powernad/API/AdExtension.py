import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.AdExtension.AdExtensionObject import AdExtensionObject
from powernad.Object.AdExtension.RequestObject.CreateAdExtensionObject import CreateAdExtensionObject
from powernad.Object.AdExtension.RequestObject.UpdateAdExtensionObject import UpdateAdExtensionObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

AdExtensionObjectList = List[AdExtensionObject]
IdList = List[str]
ChangeFieldsList = List[str]


class AdExtension: #확장소재

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_ad_extensions_list(self, ownerId: str) -> AdExtensionObjectList:
        result = self.r.get('/ncc/ad-extensions', {'ownerId': ownerId})
        adext_list = []
        for arr in result:
            camp = AdExtensionObject(arr)
            adext_list.append(camp)
        return adext_list

    def get_ad_extensions_list_by_ids(self, ids: IdList) -> AdExtensionObjectList:
        ids = ",".join(ids)
        ids = {'ids' : ids}
        result = self.r.get('/ncc/ad-extensions', ids)
        adext_list = []
        for arr in result:
            camp = AdExtensionObject(arr)
            adext_list.append(camp)
        return adext_list

    def get_ad_extensions(self, adExtensionId: str) -> AdExtensionObject:
        result = self.r.get('/ncc/ad-extensions/'+adExtensionId)
        result = AdExtensionObject(result)

        return result

    def create_ad_extensions(self, CreateAdExtensionObject: CreateAdExtensionObject) -> AdExtensionObject:
        
        data = jsonpickle.encode(CreateAdExtensionObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = data
        data_str = json.dumps(data_str)
        
        result = self.r.post('/ncc/ad-extensions', data_str)
        result = AdExtensionObject(result)
        return result

    def update_ad_extensions(self, adExtensionId: str, fields: ChangeFieldsList,
                                                    UpdateAdExtensionObject: UpdateAdExtensionObject) -> AdExtensionObject:
        
        data = jsonpickle.encode(UpdateAdExtensionObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = data
        data_str = json.dumps(data_str)
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        result = self.r.put('/ncc/ad-extensions/'+adExtensionId, data_str, query)
        result = AdExtensionObject(result)
        return result
    
    def delete_ad_extensions(self, adExtensionId: str):
        self.r.delete('/ncc/ad-extensions/'+adExtensionId)
        return True