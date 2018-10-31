import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.BusinessChannel.BusinessChannelObject import BusinessChannelObject
from powernad.Object.BusinessChannel.RequestObject.CreateBusinessChannelObject import CreateBusinessChannelObject
from powernad.Object.BusinessChannel.RequestObject.UpdateBusinessChannelObject import UpdateBusinessChannelObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

BusinessChannelObjectList = List[BusinessChannelObject]
BusinessChannelIdList = List[str]


class BusinessChannel:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_business_channel_list(self) -> BusinessChannelObjectList:
        result = self.r.get('/ncc/channels')

        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)

        return business_channel_list
    
    def get_business_channel_list_by_type(self, tp: str) -> BusinessChannelObjectList:
        result = self.r.get('/ncc/channels', {'channelTp': tp})

        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)

        return business_channel_list

    def get_business_channel_list_by_ids(self, ids: BusinessChannelIdList) -> BusinessChannelObjectList:
        ids = ",".join(ids)
        query = {'ids': ids}
        result = self.r.get('/ncc/channels', query)

        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)
        return business_channel_list

    def get_business_channel(self, businessChannelId) -> BusinessChannelObject:
        result = self.r.get('/ncc/channels/'+businessChannelId)
        result = BusinessChannelObject(result)

        return result

    def create_business_channel(self, CreateBusinessChannelObj: CreateBusinessChannelObject) -> BusinessChannelObject:
        
        data = jsonpickle.encode(CreateBusinessChannelObj, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.post('/ncc/channels', data_str)
        result = BusinessChannelObject(result)
        return result

    def update_business_channel(self, fields, UpdateBusinessChannelObj: UpdateBusinessChannelObject) -> BusinessChannelObject:
        data = jsonpickle.encode(UpdateBusinessChannelObj, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.put('/ncc/channels', data_str, fields)
        result = BusinessChannelObject(result)
        return result

    def delete_business_channel(self, businessChannelId: str):
        self.r.delete('/ncc/channels/'+businessChannelId)
        return True

    def delete_business_channel_by_ids(self, ids: BusinessChannelIdList):
        ids = ",".join(ids)
        query = {'ids': ids}
        self.r.delete('/ncc/channels', query)
        return True
