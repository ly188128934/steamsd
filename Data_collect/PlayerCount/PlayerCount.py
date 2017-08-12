#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import requests
import json

r = requests.get('http://121.14.64.40:/cobbler/pub/test.json')
url_value = json.dumps(r.json())
url_value_loads = json.loads(url_value)
url_value_result = url_value_loads['response']
url_value_result_dumps = json.dumps(url_value_result)
url_value_result_loads = json.loads(url_value_result_dumps)
url_value_result_loads_keys = url_value_result_loads.keys()
url_value_result_loads

url = sys.argv[1]
curlurl(url)
