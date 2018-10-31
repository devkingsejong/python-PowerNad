import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.Target.TargetObject import TargetObject
from powernad.Object.Target.RequestObject.UpdateTargetObject import UpdateTargetObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List
TargetObjectList = List[TargetObject]
TypesList = List[str]
OwnerIdList = List[str]


class Target:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_target_list(self, ownerId: str, types: TypesList) -> TargetObjectList:
        result = self.r.get('/ncc/targets', {'ownerId': ownerId, 'types': types})
        
        target_list = []
        for arr in result:
            target = TargetObject(arr)
            target_list.append(target)

        return target_list

    def get_target_lists(self, ownerId: OwnerIdList, types: TypesList) -> TargetObjectList:
        result = self.r.get('/ncc/targets', {'ownerId': ownerId, 'types': types})

        target_list = []
        for arr in result:
            target = TargetObject(arr)
            target_list.append(target)

        return target_list

    def update_target(self, targetId: str, UpdateTargetObject: UpdateTargetObject) -> TargetObject:

        data = jsonpickle.encode(UpdateTargetObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.put('/ncc/targets/'+targetId, data_str)

        result = TargetObject(result)
        return result
