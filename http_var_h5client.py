import requests
import json

def check_root():
    domain = 'h5.svr'
    headers = {'host': domain}
    endpoint = "http://192.168.88.192:5000"
    req = endpoint + '/'

    print("REQ", req)
    print("RSP")
    rsp = requests.get(req, headers=headers)
    print(rsp)
    domain_json = rsp.json()
    print(json.dumps(rsp.json(), indent=2))


    # root_uuid = domain_json['root']
    root_uuid = "53de1cf9-0154-11e9-96a8-080027809a89"
    print(f'root uid = {root_uuid}')
    req = endpoint + '/datasets/' + root_uuid + '/value'
    print("REQ", req)
    print("RSP")
    rsp = requests.get(req, headers=headers)
    print(rsp)
    link_json = rsp.json()
    print(json.dumps(rsp.json(), indent=2))
    print(rsp.json()['value'])

if __name__ == '__main__':
    # domain = '192.168.88.192/groups"'
    check_root()
