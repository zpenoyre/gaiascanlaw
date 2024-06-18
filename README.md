# gaiascanlaw
 nominal scanning law for full gaia mission (based on 6th level healpix grid)

 install via
    pip install gaiascanlaw

 usage
    times,angles=gaiascanlaw.scanlaw(ra,dec,tstart=gaiascanlaw.tstart,tend=gaiascanlaw.tdr3)

 where ra and dec are in degrees, scan angles are in radians, and all times are in decimal year (between mid 2014 and early 2025) - the start of the mission and the end time of particular data releases are recorded (e.g. gaiascanlaw.tdrN) for convenience, such that you can access the scanlaw for other data releases by changing tend)

 because this is the nominal (i.e. planned) scan law the real data will necesarilly contain less entries (though most sources will see few/no lost scans) - data is collected from the gaia gost tool, where you can also query the observed scan laws from existing data releases