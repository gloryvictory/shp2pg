# shp2pg
load some shp-files to PostgreSQL+PostGIS 

#02_shp_prj_srid_identify.py
02_shp_prj_srid_identify.py  - scan all SHP files and makes csv file with columns: FILENAME, PRJ, SRID, METADATA

##Statistic  

|FILENAME|PRJ|SRID|METADATA|CODEPAGE|HAS_DEFIS|
|----------|:----:|:---:|:------:|:---:|:---:|
|c:\test\Izuch\sta.shp|YES|4024|YES |ANSI 1251|NO|
|c:\test\Izuch\stb.shp|NO|NO|NO |NO|NO|
|c:\test\Izuch\sts-dd.shp|YES|4326|NO |UTF-8|YES|
|c:\test\Izuch\stq.shp|YES|4024|YES |UTF-8|NO|
