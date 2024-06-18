from astropy.table import Table, Column
import numpy as np
import astropy
import healpy as hp
import os

local_dir = os.path.dirname(__file__)
data_path_1=local_dir+'/data/gost_simple_1.fits'
data_path_2=local_dir+'/data/gost_simple_2.fits'

gaiatimes=astropy.time.Time(["2014-07-25T10:31:25.554960001",
                            "2015-09-16T16:21:27.121893186",
                            "2016-05-23T11:36:27.459006034",
                            "2017-05-28T08:46:28.954612431",
                            "2020-01-20T22:01:30.250520158",
                            "2025-01-15T00:00:00"], format='isot', scale='tcb').decimalyear
tstart=gaiatimes[0]
tdr1=gaiatimes[1]
tdr2=gaiatimes[2]
tdr3=gaiatimes[3]
tdr4=gaiatimes[4]
tdr5=gaiatimes[5]

data1=astropy.table.Table.read(data_path_1, format="fits")
data2=astropy.table.Table.read(data_path_2, format="fits")
data=astropy.table.vstack([data1,data2])

healpixels=data['healpixel']
times=data['scan time [decimal year]']
angles=data['scan angle [radian]']

def scanlaw(ra,dec,tstart=tstart,tend=tdr3):
    healpix=hp.ang2pix(2**6,ra,dec,lonlat=True,nest=True)
    entries=np.flatnonzero((healpixels==healpix) & (times>tstart) & (times<tend))
    return np.array(times[entries]),np.array(angles[entries])
