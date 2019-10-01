# shp2pg
load some shp-files to PostgreSQL+PostGIS 

#02_shp_prj_srid_identify.py
02_shp_prj_srid_identify.py  - scan all SHP files and makes csv file with columns: FILENAME, PRJ, SRID, METADATA

##Statistic  

|FILENAME|PRJ|SRID|METADATA|CODEPAGE|
|----------|:----:|:---:|:------:|:---:|
|c:\test\Izuch\sta.shp|YES|4024|YES |ANSI 1251|
|c:\test\Izuch\stb.shp|NO|NO|NO |NO|
|c:\test\Izuch\sts.shp|YES|4326|NO |UTF-8|
|c:\test\Izuch\stq.shp|YES|4024|YES |UTF-8|
