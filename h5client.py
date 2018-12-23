import h5pyd
import numpy as np
import json


def get_all(name):
   print(name)

# domain = "/datasets/f5d7f2fc-0147-11e9-96a8-080027809a89"
domain = ''
endpoint = "http://h5.svr:5000"

f = h5pyd.File(domain, mode='r', endpoint=endpoint, username='test_user1', password='test')
print(f.id.uuid)
arr = np.array([1,2,3,4])
# f['value']
# g = f.create_group('Base_Group3')
# g.attrs['workers'] = 4
NUM = 1200
# create the dataset
# dset = g.create_dataset('pts', (), dtype='f8')
# f['home']
# f.visit(get_all)
# g = f['myfile.h5']
# for k in g.attrs.keys():
#     print(k)

# ds_local = f["0"]
# dset = f.create_dataset('dset', dims, dtype='int8')


dims = [16, 16, 16]
filename = 'db.hdf5'
f = h5pyd.File(filename, "w")

print("create dataset")


dset = f.create_dataset('dset', dims, dtype='int8')