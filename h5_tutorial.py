import h5pyd
import numpy as np


def data_save(dataset, power):
    # h5.svr - domain name
    # public - folder in h5ser/data
    # db - db.h5 in public folder
    f = h5pyd.File("db.public.h5.svr", "a", endpoint="http://h5.svr:5000")
    # this is the root group uuid
    # dset = f['default']
    # dset[1,1] = 99999
    data = np.linspace(0., 100.,  power, dtype='f8')
    dset = f.create_dataset(dataset, shape=(power,), maxshape=(None, ), dtype='f8')
    for i in range(30):
        print(f'i={i}')
        dset[i*power:(i+1)*power] = data
        dset.resize(((i+2)*power,))
        f.flush()
    f.close()


def data_read(dataset):
    f = h5pyd.File("db.public.h5.svr", "r", endpoint="http://h5.svr:5000")
    print(
        f.id.uuid,
        f.keys(),
        f[dataset]
    )
    print(f[dataset][:])

    # g = f.create_group('Base_Group3')
    # print(g)
    # g.attrs['workers'] = 4


if __name__ == '__main__':
    # data_save('big_data30', 1024*1024)
    data_read('big_data30')
