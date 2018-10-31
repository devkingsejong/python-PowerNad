import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.IpExclusion.IpExclusionObject import IpExclusionObject
from powernad.Object.IpExclusion.RequestObject.CreateIpExclusionObject import CreateIpExclusionObject
from powernad.Object.IpExclusion.RequestObject.UpdateIpExclusionObject import UpdateIpExclusionObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

ExclusionIdList = List[str]


class IpExclusion:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_ip_exclusion(self):
        result = self.r.get('/tool/ip-exclusions')

        ip_exclusion_list = []
        for arr in result:
            ipex = IpExclusionObject(arr)
            ip_exclusion_list.append(ipex)

        return ip_exclusion_list

    def create_ip_exclusion(self, CreateIpExclusionObject: CreateIpExclusionObject) -> IpExclusionObject:
        data = jsonpickle.encode(CreateIpExclusionObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/tool/ip-exclusions', data_str)
        result = IpExclusionObject(result)

        return result

    def update_ip_exclusion(self, UpdateIpExclusionObject: UpdateIpExclusionObject) -> UpdateIpExclusionObject:
        data = jsonpickle.encode(UpdateIpExclusionObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.put('/tool/ip-exclusions', data_str)
        result = IpExclusionObject(result)

        return result

    def delete_ip_exclusion(self, id: str):
        result = self.r.delete('/tool/ip-exclusions/' + id)
        result = IpExclusionObject(result)

        return result

    def delete_ip_exclusion_many(self, id_array: ExclusionIdList):
        query = {'ids' : id_array}
        self.r.delete('/tool/ip-exclusions', query)

        return True
