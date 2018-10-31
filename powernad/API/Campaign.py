# pylint: disable=C0103
# pylint: disable=E0401
from powernad.Connector.restapi import RestApi
from powernad.Object.Campaign.CampaignObject import CampaignObject
from powernad.Object.Campaign.RequestObject.CampaignAddObject import CampaignAddObject
from powernad.Object.Campaign.RequestObject.CampaignUpdateObject import CampaignUpdateObject
import json
import jsonpickle
from typing import List
from powernad.Common.CommonFunctions import CommonFunctions

CampaignList = List[CampaignObject]
CampaignIdList = List[str]
ChangeFieldsList = List[str]


class Campaign:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_campaign_list(self, campaignType: str =None, baseSearchId: str=None, recordSize: int=None, selector: str=None) -> CampaignList:
        
        query = {'campaignType' : campaignType, 'baseSearchId' : baseSearchId, 'recordSize' : recordSize, 'selector' : selector}
        result = self.r.get('/ncc/campaigns', query)

        camp_list = []
        for arr in result:
            camp = CampaignObject(arr)
            camp_list.append(camp)

        return camp_list

    def get_campaign_list_by_ids(self, ids: CampaignIdList) -> CampaignList:
        ids = ",".join(ids)
        query = {'ids' : ids}

        result = self.r.get('/ncc/campaigns', query)
        
        camp_list = []
        for arr in result:
            camp = CampaignObject(arr)
            camp_list.append(camp)

        return camp_list

    def get_campaign(self, campaignId: str) -> CampaignObject:
        result = self.r.get('/ncc/campaigns/'+ campaignId)
        camp = CampaignObject(result)
        return camp

    def create_campaign(self, campaign_add_object: CampaignAddObject):
        
        data = jsonpickle.encode(campaign_add_object, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)
        result = self.r.post('/ncc/campaigns', data_str)
        camp = CampaignObject(result)
        return camp

    def update_campaign(self, campaign_update_object: CampaignUpdateObject, campaignId: str, fields: ChangeFieldsList) -> CampaignList:
        fields = ",".join(fields)
        fields = {'fields': fields}
        data = jsonpickle.encode(campaign_update_object, unpicklable=False)
        result = self.r.put('/ncc/campaigns/' + str(campaignId), data, fields) #userLock, budget, period
        camp = CampaignObject(result)
        return camp