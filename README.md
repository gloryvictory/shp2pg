# shp2pg
load some shp-files to PostgreSQL+PostGIS 

#02_shp_prj_srid_identify.py
01_shp_prj_srid_identify.py  - scan all SHP files and makes csv file with columns: FILENAME, PRJ, SRID, METADATA

##Statistic  


|FILENAME|PRJ|SRID|METADATA|CODEPAGE|HAS_DEFIS|DATA_CREATION|DATA_MODIFY|DATA_LASTACCESS|DATA_SCRIPT_RUN|PRJ_INFO|
|----------|:----:|:---:|:------:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
|c:\test\Izuch\sta.shp|YES|4024|YES |ANSI 1251|NO|2019-10-15|2019-09-30|2019-10-15|2019-10-15|"GEOGCS[""GCS_Krasovsky_1940"",DATUM[""D_Krasovsky_1940"",SPHEROID[""Krasovsky_1940"",6378245.0,298.3]],PRIMEM[""Greenwich"",0.0],UNIT[""Degree"",0.0174532925199433]]"|
|c:\test\Izuch\stb.shp|NO|NO|NO |NO|NO|2019-10-15|2019-09-30|2019-10-15|2019-10-15|"GEOGCS[""GCS_Clarke_1866"",DATUM[""D_Clarke_1866"",SPHEROID[""Clarke_1866"",6378206.4,294.9786982]],PRIMEM[""Greenwich"",0.0],UNIT[""Degree"",0.0174532925199433]]"|
|c:\test\Izuch\sts-dd.shp|YES|4326|NO |UTF-8|YES|2019-10-15|2019-09-30|2019-10-15|2019-10-15|"GEOGCS[""GCS_WGS_1984"",DATUM[""D_WGS_1984"",SPHEROID[""WGS_1984"",6378137.0,298.257223563]],PRIMEM[""Greenwich"",0.0],UNIT[""Degree"",0.0174532925199433]]"|
|c:\test\Izuch\stq.shp|YES|4024|YES |UTF-8|NO|2019-10-15|2019-09-30|2019-10-15|2019-10-15|"GEOGCS[""GCS_WGS_1984"",DATUM[""D_WGS_1984"",SPHEROID[""WGS_1984"",6378137.0,298.257223563]],PRIMEM[""Greenwich"",0.0],UNIT[""Degree"",0.0174532925199433]]"|

Description in Russian:
1. **FILENAME** - полный путь к файлу
2. **PRJ** - Есть ли *.PRJ файл (в это м файле храниться описание проекции для шейп-файла, без него не понятно в какой системе координат координаты данного шейп-файла)
3. **SRID** -  есть ли соответствие данной проекции в общей системе классификации систем координат EPSG (грубо говоря можем ли мы загрузить данный шейп в PostgreSQL + PostGIS)
4. **METADATA** - есть ли файл с описательной частью (метаданные) в формате XML (FGDC или  ISO)
5. **CODEPAGE** - есть ли файл *.cp  в котором указано в какой кодировке находятся данные в шейп-файле, а если точнее в DBF
6. **HAS_DEFIS** - указывает, что в имени файла присутствует знак "дефис", что не позволит создать таблицу в PostgreSQL (надо избавиться от знака "дефис")
7. **DATA_CREATION** - дата создания файла в формате ГОД-МЕСЯЦ-ДЕНЬ
8. **DATA_MODIFY** - дата изменения файла в формате ГОД-МЕСЯЦ-ДЕНЬ
9. **DATA_LASTACCESS** - дата последнего изменения файла в формате ГОД-МЕСЯЦ-ДЕНЬ
10. **DATA_SCRIPT_RUN** - дата запуска скрипта в формате ГОД-МЕСЯЦ-ДЕНЬ
11. **PRJ_INFO** - информация из *.prj

#02_csv2xlsx.py

02_csv2xlsx.py - script converts csv file to Excel file (*.xlsx)

#03_send_email.py

03_send_email.py - script send an EMAIL with attached  result Excel file (*.xlsx)

#04_shp2pg.py

04_shp2pg.py - script makes command lines for shp files  like: 
shp2pgsql -d -I -W "cp1251" -s 4024:4326  c:\test\stl.shp "TESTSCHEMA"."stl" -h 127.0.0.1 -u test |psql -d testdb -U test


