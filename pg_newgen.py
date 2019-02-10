import psycopg2
import psycopg2.extras
import numpy as np

dbname = 'geosim'
user = 'postgres'
host = '192.168.88.192'
password = '1'





def upload(conn):
    #upload file
    with conn:
        with conn.cursor() as curs:
            loid =conn.lobject(0,'r', 0, 'db.hdf5')
            print('oid', loid.oid)
def download(conn):
    # download file
    with conn:
        with conn.cursor() as curs:
            lobj = conn.lobject(16389, 'n')
            lobj.export('testopen.hdf5')


def upload_from_numpy(conn):
    dim = (10, 10, 10)
    arr = np.random.rand(*dim)

    with conn:
        with conn.cursor() as curs:
            lobj = conn.lobject()
            np.save(lobj, arr, allow_pickle=False)
            print(lobj.oid)

def download_to_numpy(conn):
    with conn:
        with conn.cursor() as curs:
            lobj = conn.lobject(16410, 'wb')
            data = np.load(lobj, allow_pickle=False)
            print(lobj.oid, data.shape)
            return data




if __name__ == '__main__':
    conn = psycopg2.connect(dbname=dbname,
                            user=user,
                            host=host,
                            password=password,
                            cursor_factory=psycopg2.extras.DictCursor)

    SQL = 'select data from pg_largeobject where loid=16389'

    array = download_to_numpy(conn)
    print(array)





    conn.close()
