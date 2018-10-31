from powernad.Connector.restapi import RestApi
from powernad.Object.Bizmoney.BizmoneyObject import BizmoneyObject
from powernad.Object.Bizmoney.BizmoneyCostObject import BizmoneyCostObject
from typing import List

BizmoneyCostObjectList = List[BizmoneyCostObject]


class Bizmoney:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)

    def get_biz_money(self) -> BizmoneyObject:
        result = self.r.get('/billing/bizmoney')
        result = BizmoneyObject(result)

        return result

    def get_biz_money_cost(self, statDt: str) -> BizmoneyCostObjectList:
        result = self.r.get('/billing/bizmoney/cost/' + statDt)
        cost_list = []
        for arr in result:
            cost = BizmoneyCostObject(arr)
            cost_list.append(cost)

        return cost_list
