import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.MasterReport.MasterReportObject import MasterReportObject
from powernad.Object.MasterReport.RequestObject.CreateMasterReportObject import CreateMasterReportObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List

MasterReportObjectList = List[MasterReportObject]


class MasterReport: #광고정보일괄다운로드탭

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_master_report_list(self) -> MasterReportObjectList:
        result = self.r.get('/master-reports')
        
        mreport_list = []
        for arr in result:
            mreport = MasterReportObject(arr)
            mreport_list.append(mreport)

        return mreport_list

    def get_master_report_by_id(self, id: str) -> MasterReportObject:
        result = self.r.get('/master-reports/' + id)
        
        result = MasterReportObject(result)
        return result

    def create_master_report(self, CreateMasterReportObject: CreateMasterReportObject) -> MasterReportObject:
        data = jsonpickle.encode(CreateMasterReportObject, unpicklable=False)
        data = json.loads(data)       
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.post('/master-reports', data_str)
        result = MasterReportObject(result)

        return result

    def delete_master_report_all(self):
        self.r.delete('/master-reports')
        return True

    def delete_master_report_by_id(self, id: str):
        self.r.delete('/master-reports', {'id': id})
        return True
