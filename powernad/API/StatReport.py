import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.StatReport.StatReportObject import StatReportObject
from powernad.Object.StatReport.RequestObject.CreateStatReportObject import CreateStatReportObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List
StatReportObjectList = List[StatReportObject]


class StatReport: #대용량 보고서

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_stat_report_list(self) -> StatReportObjectList:
        result = self.r.get('/stat-reports')
        stat_list = []
        for arr in result:
            stat = StatReportObject(arr)
            stat_list.append(stat)

        return stat_list

    def get_stat_report(self, reportJobId: str) -> StatReportObject:
        result = self.r.get('/stat-reports/' + reportJobId)
        result = StatReportObject(result)
        
        return result

    def create_stat_report(self, CreateStatReportObject: CreateStatReportObject) -> StatReportObject:
        
        data = jsonpickle.encode(CreateStatReportObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/stat-reports', data_str)
        result = StatReportObject(result)

        return result

    def delete_stat_reports(self, reportJobId: str):
        self.r.delete('/stat-reports/'+ reportJobId)
        return True
