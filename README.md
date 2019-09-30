# shp2pg
load some shp-files to PostgreSQL+PostGIS 

#02_shp_prj_srid_identify.py
02_shp_prj_srid_identify.py  - scan all SHP files and makes csv file with columns: FILENAME, PRJ, SRID, METADATA

##Statistic  

|FILENAME|PRJ|SRID|METADATA|
|----------|:----:|:---:|------:|
|c:\test\Izuch\sta.shp|YES|4024|YES |
|c:\test\Izuch\stb.shp|NO|NO|NO |
|c:\test\Izuch\sts.shp|YES|4326|NO |
|c:\test\Izuch\stq.shp|YES|4024|YES |
