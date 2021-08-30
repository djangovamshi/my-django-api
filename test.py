import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#         'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource()


def create_resource():
    new_Student={
    'roll_number':107,
    'name':'Mr.Amar',
    'dob': '1997-01-28',
    'marks':90,
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_Student))
    print(resp.status_code)
    print(resp.json())
create_resource()
#
def Update_resource(id):
    new_emp={
    'id':id,
    'eno':700,

    'esal':60000.00,
    'eaddr':'Hyderabad',
    }

    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
