import json

class StatReportObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.downloadUrl = None if 'downloadUrl' not in s else s['downloadUrl']
        self.loginId = None if 'loginId' not in s else s['loginId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.reportJobId = None if 'reportJobId' not in s else s['reportJobId']
        self.reportTp = None if 'reportTp' not in s else s['reportTp']
        self.statDt = None if 'statDt' not in s else s['statDt']
        self.status = None if 'status' not in s else s['status']
        self.updateTm = None if 'updateTm' not in s else s['updateTm']