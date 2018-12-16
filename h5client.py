import h5pyd
import numpy as np
import json


def get_all(name):
   print(name)

domain = "/home/test_user1/myfile"
endpoint = "http://192.168.88.192:5000"

f = h5pyd.File(domain, 'r', endpoint=endpoint, username='test_user1', password='test')
print(f.id.uuid)
# f.visit(get_all)
# g = f['myfile.h5']
# for k in g.attrs.keys():
#     print(k)

# ds_local = f["0"]
# dset = f.create_dataset('dset', dims, dtype='int8')
