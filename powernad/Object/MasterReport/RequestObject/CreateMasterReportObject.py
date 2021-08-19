from datetime import datetime
from pytz import timezone

class CreateMasterReportObject:
    def __init__(self, item, fromTime, timeZone='Asia/Seoul'):
        self.item = item
        
        if fromTime is None:
            self.fromTime = None
        elif type(fromTime) == datetime:
            self.fromTime = fromTime.replace(tzinfo=timezone(timeZone)).isoformat(timespec='seconds')
        else:
            raise Exception('type of fromTime should be None or datetime')