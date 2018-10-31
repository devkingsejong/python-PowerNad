import json
class BusinessInfo:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def

        self.isMobileNaverLogin = None if 'isMobileNaverLogin' not in s else s['isMobileNaverLogin']
        self.isMobileNaverPay = None if 'isMobileNaverPay' not in s else s['isMobileNaverPay']
        self.isMobileNaverTalkTalk = None if 'isMobileNaverTalkTalk' not in s else s['isMobileNaverTalkTalk']
        self.isNaverLogin = None if 'isNaverLogin' not in s else s['isNaverLogin']
        self.isNaverPay = None if 'isNaverPay' not in s else s['isNaverPay']
        self.isNaverTalkTalk = None if 'isNaverTalkTalk' not in s else s['isNaverTalkTalk']
        self.isStoreFarm = None if 'isStoreFarm' not in s else s['isStoreFarm']
        self.mobileCertStatus = None if 'mobileCertStatus' not in s else s['mobileCertStatus']
        self.naAccountId = None if 'naAccountId' not in s else s['naAccountId']
        self.naAccountType = None if 'naAccountType' not in s else s['naAccountType']
        self.originalPath = None if 'originalPath' not in s else s['originalPath']
        self.site = None if 'site' not in s else s['site']
        self.thumbnailPath = None if 'thumbnailPath' not in s else s['thumbnailPath']
        self.useNaverPayNaScript = None if 'useNaverPayNaScript' not in s else s['useNaverPayNaScript']
        self.useSaNaScript = None if 'useSaNaScript' not in s else s['useSaNaScript']
        self.useStoreFarmNaScript = None if 'useStoreFarmNaScript' not in s else s['useStoreFarmNaScript']

