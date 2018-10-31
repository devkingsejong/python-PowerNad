import base64
import hmac
import hashlib
import time
import urllib.parse
import json
import requests
import jsonpickle

 
class RestApi:
    def __init__(self, base_url, api_key, secret_key, customer_id):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id

    
    def generate_signature(self, timestamp, method, path):
        sign =  "%s.%s.%s" % (timestamp, method, path)
        # signature = hmac.new(self.secret_key.encode(), sign.encode(), hashlib.sha256).hexdigest()
        signature = hmac.new(self.secret_key.encode(), sign.encode(), hashlib.sha256).digest()
        return base64.b64encode(signature).decode()


    def get_timestamp(self):
        return round(time.time() * 1000)


    def get_header(self, method, uri):
        timestamp = self.get_timestamp() 
        header = {}
        header['Content-Type'] = 'application/json; charset=UTF-8'
        header['X-Timestamp'] = str(timestamp)
        header['X-API-KEY'] = self.api_key
        header['X-Customer'] = str(self.customer_id)
        header['X-Signature'] = self.generate_signature(timestamp, method, uri)

        return header

    def build_http_query(self, query):
        if query:
            query_list = []
            
            for key, value in query.items():
                
                if value != None:
                    q = "%s=%s" % ( urllib.parse.quote_plus(key), urllib.parse.quote_plus(value) )
                else:
                    continue
                query_list.append(q)
            return '&'.join(query_list)
        else:
            return ''

    
    def get_transaction_id(self, headers):
        if "X-Transaction-ID" in headers:
            return headers["X-Transaction-ID"]
        else:
            return "unknown"

    
    def parse_response(self, response):
        if response:
            header = response.headers
            body = response.text
            transaction_id = self.get_transaction_id(header)
            json_body = json.loads(body)

            return {'transaction_id': transaction_id, 'json': json_body}
            
        return {}


    def get(self, uri, query={}):
        url = "%s%s%s%s" % ( self.base_url, uri, '' if query=={} else '?', self.build_http_query(query))
        headers = self.get_header('GET', uri) 

        try:
            r = requests.get(url, headers=headers)         
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: %s" % r.status_code)

            return response['json']
        except:
            print("failed to request")


    def post(self, uri, data, query={}):
        url = "%s%s%s%s" % ( self.base_url, uri, '' if query=={} else '?', self.build_http_query(query))
        data_str = data
        headers = self.get_header('POST', uri)
        
        try:
            r = requests.post(url, data=data_str, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: %s" % r.status_code)
                
            return response['json']
        except:
            print("failed to request")


    def delete(self, uri, query={}):
        url = "%s%s%s%s" % ( self.base_url, uri, '' if query=={} else '?', self.build_http_query(query))
        headers = self.get_header('DELETE', uri)
        
        try:
            r = requests.delete(url, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: %s" % r.status_code)

            return response['json']
        except:
            print("failed to request")



    def put(self, uri, data, query={}):
        url = "%s%s%s%s" % ( self.base_url, uri, '' if query=={} else '?', self.build_http_query(query))
        data_str = data        
        headers = self.get_header('PUT', uri)

        try:
            r = requests.put(url, data=data_str, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: %s" % r.status_code)

            return response['json']
        except:
            print("failed to request")


    def download(self, url, localpath):
        return None

    def null_dict(self, input_dict):
        real = dict()
        for now in input_dict:
            if input_dict[now] != None:
                real.update({now :input_dict[now]})
        return real
