#!/usr/bin/env bash

COLOMBIA_SHAPEFILE=https://data.humdata.org/dataset/50ea7fee-f9af-45a7-8a52-abb9c790a0b6/resource/da4a3090-43d7-4f0b-8b51-2de9718f69c4/download/col_admbnda_adm0-1-2.gdb.zip
COLOMBIA_ROADS_L=http://export.hotosm.org/downloads/36bc1e36-f6a4-4e33-a8b6-5c1b81b98ae5/hotosm_col_roads_lines_shp.zip
COLOMBIA_ROADS_P=http://export.hotosm.org/downloads/36bc1e36-f6a4-4e33-a8b6-5c1b81b98ae5/hotosm_col_roads_polygons_shp.zip
HEALTH_SITES=https://data.humdata.org/dataset/4ca96139-21c0-456d-9624-45e6474dd3ea/resource/9f451cd6-2669-4a0b-b5bb-2d5bd82228c2/download/colombia-shapefiles.zip

WGET_OPTIONS="-q --show-progress -c"
UNZIP_OPTIONS="-q -u -o"

echo "Downloading data..."
wget $WGET_OPTIONS $COLOMBIA_SHAPEFILE -O colombia_shapefile.zip
wget $WGET_OPTIONS $COLOMBIA_ROADS_P -O colombia_roads_polygons.zip
wget $WGET_OPTIONS $COLOMBIA_ROADS_L -O colombia_roads_lines.zip
wget $WGET_OPTIONS $HEALTH_SITES -O healthsites.zip
echo "Done!"

echo "Inflating zipfiles..."
unzip $UNZIP_OPTIONS colombia_shapefile.zip -d colombia_shapefile
unzip $UNZIP_OPTIONS colombia_roads_polygons.zip -d colombia_roads_polygons
unzip $UNZIP_OPTIONS colombia_roads_lines.zip -d colombia_roads_lines
unzip $UNZIP_OPTIONS healthsites.zip -d healthsites
echo "Done!"
