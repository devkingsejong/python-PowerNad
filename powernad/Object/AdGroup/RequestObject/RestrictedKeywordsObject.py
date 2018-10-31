import json
import datetime

class RestrictedKeywordsObject:
    def __init__(self, keyword, description, nccAdgroupId):
        self.delFlag = False
        self.description = description 
        self.keyword = keyword 
        self.nccAdgroupId = nccAdgroupId 
        self.type = "KEYWORD_PLUS_RESTRICT" 