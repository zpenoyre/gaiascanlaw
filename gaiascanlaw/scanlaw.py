from astropy.table import Table, Column
import numpy as np
import astropy
import healpy as hp
import os

local_dir = os.path.dirname(__file__)
data_path_1=local_dir+'/data/gost_simple_1.fits'
data_path_2=local_dir+'/data/gost_simple_2.fits'
data_path_gaps=local_dir+'/data/data_gaps.fits'

gaiatimes=astropy.time.Time(["2014-07-25T10:31:25.554960001",
                            "2015-09-16T16:21:27.121893186",
                            "2016-05-23T11:36:27.459006034",
                            "2017-05-28T08:46:28.954612431",
                            "2020-01-20T22:01:30.250520158",
                            "2025-01-15T06:16:32.690905256"], format='isot', scale='tcb').decimalyear

gaiaepochs=np.array([2015,2015.5,2016,2017,2020]) # apart from DR2 and DR3 these are guesses!
# if someone can provide a source it would be much appreciated

tstart=gaiatimes[0]
tdr1=gaiatimes[1]
tdr2=gaiatimes[2]
tdr3=gaiatimes[3]
tdr4=gaiatimes[4]
tdr5=gaiatimes[5]

# time of transition from Ecliptic Pole Scanning law to nominal
tEPSL=astropy.time.Time("2014-08-22T21:01:25.599970336", format='isot', scale='tcb').decimalyear

data1=astropy.table.Table.read(data_path_1, format="fits")
data2=astropy.table.Table.read(data_path_2, format="fits")
data=astropy.table.vstack([data1,data2])

# gaps data from https://www.cosmos.esa.int/web/gaia/dr3-data-gaps
gaps=astropy.table.Table.read(data_path_gaps, format="fits")
gstarts=gaps['start [decimal year]']
gends=gaps['end [decimal year]']
gtypes=gaps['type']

healpixels=data['healpixel']
times=data['scan time [decimal year]']
angles=data['scan angle [radian]']
ccdrows=data['ccd row']

def scanlaw(ra,dec,tstart=tstart,tend=tdr3,ccd_row=False,obstype=None):
    healpix=hp.ang2pix(2**6,ra,dec,lonlat=True,nest=True)
    if (obstype=='astrometry') & (tstart<tEPSL):
        tstart=tEPSL # no astrometric data taken in EPSL period
    entries=np.flatnonzero((healpixels==healpix) & (times>tstart) & (times<tend))
    if obstype!=None:
        data_gaps=np.flatnonzero(gtypes==obstype)
        for dgap in data_gaps:
            entries=entries[(times[entries]<gstarts[dgap]) | (times[entries]>gends[dgap])]

    if ccd_row==True:
        return np.array(times[entries]),np.array(angles[entries]),np.array(ccdrows[entries])
    else:
        return np.array(times[entries]),np.array(angles[entries])
