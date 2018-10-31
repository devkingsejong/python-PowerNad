import json

class MasterReportObject:
    def __init__(self, json_def):
        
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.clientCustomerId = None if 'clientCustomerId' not in s else s['clientCustomerId']
        self.downloadUrl = None if 'downloadUrl' not in s else s['downloadUrl']
        self.fromTime = None if 'fromTime' not in s else s['fromTime']
        self.id = None if 'id' not in s else s['id']
        self.item = None if 'item' not in s else s['item']
        self.managerCustomerId = None if 'managerCustomerId' not in s else s['managerCustomerId']
        self.managerLoginId = None if 'managerLoginId' not in s else s['managerLoginId']
        self.registTime = None if 'registTime' not in s else s['registTime']
        self.status = None if 'status' not in s else s['status']
        self.updateTime = None if 'updateTime' not in s else s['updateTime']