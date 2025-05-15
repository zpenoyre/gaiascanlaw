# gaiascanlaw
 nominal scanning law for full gaia mission (based on 6th level healpix grid) from late 2014 to early 2025

---

 install via:
    
    pip install gaiascanlaw

---

 usage - returns numpy arrays of scan times and angles:
    
    times,angles=gaiascanlaw.scanlaw(ra,dec,tstart=gaiascanlaw.tstart,tend=gaiascanlaw.tdr5)

 where ra and dec are in degrees, scan angles are in radians, and all times are in decimal year (between mid 2014 and early 2025) - the start of the mission and the end time of particular data releases are recorded (e.g. gaiascanlaw.tdrN) for convenience, such that you can access the scanlaw for other data releases by changing tend)

 ---

 optional arguments:
 
    times,angles,ccds=gaiascanlaw.scanlaw(ra,dec,ccd_row=True)
 will also return which ccd row (1-7) is used, with positive values corresponding to the preceeding field of view, and negative values the following (https://www.cosmos.esa.int/web/gaia/focal-plane)

    times,angles=gaiascanlaw.scanlaw(ra,dec,obstype='astrometric')

 will cut out known gaps in the data corresponding to the particular type of observation ('astrometric', 'photometric' or 'spectroscopic') - gap data from https://www.cosmos.esa.int/web/gaia/dr3-data-gaps

 ---
 
 because this is the nominal (i.e. planned) scan law the real data will usually contain less entries - underlying data is collected from the gaia GOST tool (https://gaia.esac.esa.int/gost/index.jsp), where you can also query the observed scan laws from existing data releases
