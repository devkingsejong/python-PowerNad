import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.Estimate.EstimateAvgObject import EstimateAvgObject
from powernad.Object.Estimate.EstimateMedianObject import EstimateMedianObject
from powernad.Object.Estimate.EstimateExposureMiniObject import EstimateExposureMiniObject
from powernad.Object.Estimate.EstimatePerformanceObject import EstimatePerformanceObject
from powernad.Object.Estimate.RequestObject.GetAvgPositionBidObject import GetAvgPositionBidObject
from powernad.Object.Estimate.RequestObject.GetExposureMiniBidObject import GetExposureMiniBidObject
from powernad.Object.Estimate.RequestObject.GetMedianBidObject import GetMedianBidObject
from powernad.Object.Estimate.RequestObject.GetPerformanceObject import GetPerformanceObject
from powernad.Common.CommonFunctions import CommonFunctions

from typing import List
EstimateAvgObjectList = List[EstimateAvgObject]
EstimateMedianObjectList = List[EstimateMedianObject]
EstimateExposureMiniObjectList = List[EstimateExposureMiniObject]
EstimatePerformanceObjectList = List[EstimatePerformanceObject]
GetPerformanceObjectList = List[GetPerformanceObject]


class Estimate:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_avg_position_bid_list(self, type, GetAvgPositionBidObject: GetAvgPositionBidObject) -> EstimateAvgObjectList:
        
        data = jsonpickle.encode(GetAvgPositionBidObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/estimate/average-position-bid/' + type, data_str)
        result = result['estimate']
        estimate_list = []
        for arr in result:
            estimate = EstimateAvgObject(arr)
            estimate_list.append(estimate)

        return estimate_list

    def get_median_bid_list(self, type: str, GetMedianBidObject: GetMedianBidObject) -> EstimateMedianObjectList:
        data = jsonpickle.encode(GetMedianBidObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/estimate/median-bid/' + type, data_str)
        result = result['estimate']
        estimate_list = []
        for arr in result:
            estimate = EstimateMedianObject(arr)
            estimate_list.append(estimate)

        return estimate_list

    def get_exposure_mini_bid_list(self, type: str, GetExposureMiniBidObject: GetExposureMiniBidObject) -> EstimateExposureMiniObjectList:
        data = jsonpickle.encode(GetExposureMiniBidObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/estimate/exposure-minimum-bid/' + type, data_str)
        result = result['estimate']
        estimate_list = []
        for arr in result:
            estimate = EstimateExposureMiniObject(arr)
            estimate_list.append(estimate)

        return estimate_list

    def get_performance_list(self, type: str, GetPerformanceObject: GetPerformanceObject) -> EstimatePerformanceObjectList:
        data = jsonpickle.encode(GetPerformanceObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/estimate/performance/' + type, data_str)
        result = result['estimate']
        
        estimate_list = []
        for arr in result:
            estimate = EstimatePerformanceObject(arr)
            estimate_list.append(estimate)

        return estimate_list

    def get_performance_list_many(self, type: str, GetPerformanceObjectList: GetPerformanceObjectList):
        data = jsonpickle.encode(GetPerformanceObjectList, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/estimate/performance/' + type, data_str)
        result = result['estimate']
        
        estimate_list = []
        for arr in result:
            estimate = EstimatePerformanceObject(arr)
            estimate_list.append(estimate)

        return estimate_list
