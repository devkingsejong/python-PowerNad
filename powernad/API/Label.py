import json
import jsonpickle
from powernad.Connector.restapi import RestApi
from powernad.Object.Label.LabelObject import LabelObject
from powernad.Object.Label.LabelRefObject import LabelRefObject
from powernad.Object.Label.RequestObject.UpdateLabelObject import UpdateLabelObject
from powernad.Object.Label.RequestObject.UpdateLabelRefObject import UpdateLabelRefObject
from powernad.Common.CommonFunctions import CommonFunctions
from typing import List
LabelRefObjectList = List[LabelRefObject]
LabelObjectList = List[LabelObject]


class Label: #즐겨찾기

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_label_list(self) -> LabelObjectList:
        result = self.r.get('/ncc/labels')

        label_list = []
        for arr in result:
            label = LabelObject(arr)
            label_list.append(label)

        return label_list

    def update_label(self, UpdateLabelObject: UpdateLabelObject) -> LabelObject:
        data = jsonpickle.encode(UpdateLabelObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.delete_null_dict_items(data)
        data_str = json.dumps(data)

        result = self.r.put('/ncc/labels', data_str)

        result = LabelObject(result)

        return result

    def update_label_ref(self, UpdateLabelRefObject: UpdateLabelRefObject) -> LabelRefObjectList:
        data = jsonpickle.encode(UpdateLabelRefObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.delete_null_dict_items(data)
        data = [data]
        data_str = json.dumps(data)

        result = self.r.put('/ncc/label-refs/', data_str)

        labelref_list = []
        for arr in result:
            labelref = LabelRefObject(arr)
            labelref_list.append(labelref)

        return labelref_list
