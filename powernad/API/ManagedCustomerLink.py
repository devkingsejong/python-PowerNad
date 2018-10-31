from powernad.Connector.restapi import RestApi
from powernad.Object.ManagedCustomerLink.ManagedCustomerLinkObject import ManagedCustomerLinkObject

from typing import List
ManagedCustomerLinkObjectList = List[ManagedCustomerLinkObject]


class ManagedCustomerLink:

    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.r = RestApi(base_url, api_key, secret_key, customer_id)
    
    def get_managed_customer_link_list(self, rel_type: str = None) -> ManagedCustomerLinkObjectList:
        query = {'type': rel_type}
        result = self.r.get('/customer-links', query)
        customer_list = []
        for arr in result:
            customer = ManagedCustomerLinkObject(arr)
            customer_list.append(customer)

        return customer_list
