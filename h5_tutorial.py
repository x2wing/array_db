import h5pyd
import numpy as np

# public - folder in h5ser/data
# db - db.h5 in public folder
f = h5pyd.File("db.public.h5.svr", "r+", endpoint="http://h5.svr:5000")
# this is the root group uuid
dset = f['default']
dset[1,1] = 99999
print(
    f.id.uuid,
    f.keys(),
    f['default'][:]
)

# g = f.create_group('Base_Group3')
# print(g)
# g.attrs['workers'] = 4
