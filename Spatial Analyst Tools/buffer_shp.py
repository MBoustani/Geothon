#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/buffer_shp.py
Description:   This code generates buffer polygon around Shapefile.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

#an shapefile example
in_shp_file = '../static_files/shapefile/land_boundaries/land_boundaries.shp'

#create ESRI shapefile dirver
driver = ogr.GetDriverByName('ESRI Shapefile')

#get input shapefile datasource
in_shp_datasource = driver.Open(in_shp_file)

#get input shapefile layer
in_layer = in_shp_datasource.GetLayer()

#get number of feautres of input shapefile
num_feature = in_layer.GetFeatureCount()

#an output shapefile (buffer) name
out_shp_file = 'polygon.shp'
#an output shapefile (buffer) layer
layer_name = 'polygon_layer'

#buffer range, positive number for outside of shape
#   and negative number for buffer inside the shape
buffer_range = 10

#create shapefile data_source(file)
if os.path.exists(out_shp_file):
    driver.DeleteDataSource(out_shp_file)
out_shp_datasource = driver.CreateDataSource(out_shp_file)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#create shapefile layer as polygon data with wgs84 as spatial reference
out_layer = out_shp_datasource.CreateLayer(layer_name, srs, ogr.wkbMultiPolygon)

for each in range(num_feature):
    in_feature = in_layer.GetFeature(each)
    in_geom = in_feature.GetGeometryRef()
    bufer_geom = in_geom.Buffer(buffer_range)
    out_feature = ogr.Feature(out_layer.GetLayerDefn())
    out_feature.SetGeometry(bufer_geom)
    out_layer.CreateFeature(out_feature)
