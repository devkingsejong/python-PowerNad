import json
class AdFieldObject:
    def __init__(self, json_def = None):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        
        self.pc_display = None if 'pc' not in s else self.pc_display_easy(s['pc'])
        self.pc_final = None if 'pc' not in s else self.pc_final_easy(s['pc'])
        self.mobile_display =  None if 'mobile' not in s else self.mobile_display_easy(s['mobile'])
        self.mobile_final =  None if 'mobile' not in s else self.mobile_final_easy(s['mobile'])
        self.headline = None if 'headline' not in s else s['headline']
        self.description = None if 'description' not in s else s['description']


    def pc_final_easy(self, pc):
        return pc['final']

    def pc_display_easy(self, pc):
        return pc['display']

    def mobile_final_easy(self, mobile):
        return mobile['final']

    def mobile_display_easy(self, mobile):
        return mobile['display']
