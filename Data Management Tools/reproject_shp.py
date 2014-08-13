#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/reproject_shp.py
Description:   This code reprojects Shapefile.
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

#an example input shapefile file.
in_shp_file = '../static_files/shapefile/rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp'

#set the driver to ESRI Shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

#open input shapefile
in_shp_datasource = driver.Open(in_shp_file)

#get input shapefile layer
in_layer = in_shp_datasource.GetLayerByIndex(0)

#get input shapefile geometry
in_geom_type = in_layer.GetGeomType()

#get input shapefile spatial reference
source = in_layer.GetSpatialRef()

#create spatial reference for output shapefile
target = osr.SpatialReference()
#in this case NAD83(HARN) / California zone 4
target.ImportFromEPSG(2873)

#create a trasnform from source to target
transform = osr.CoordinateTransformation(source, target)

#output shapefile name
out_shp = 'reprojected.shp'
#output shapefile layer name
out_layer_name = 'shp_layer'

#create output shapefile data_source(file)
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)
data_source = driver.CreateDataSource(out_shp)

#define output shapefile layer
out_layer = data_source.CreateLayer(out_layer_name, target, in_geom_type)

#get input shapefile layer definition
in_layer_defn = in_layer.GetLayerDefn()
num_field_col = in_layer_defn.GetFieldCount()

for each in range(num_field_col):
    field = in_layer_defn.GetFieldDefn(each)
    out_layer.CreateField(field)

#get input shapefile number of features
in_num_feature = in_layer.GetFeatureCount()

for feature in range(in_num_feature):
    in_feature = in_layer.GetFeature(feature)
    in_geom = in_feature.GetGeometryRef()
    in_geom.Transform(transform)
    feature = ogr.Feature(out_layer.GetLayerDefn())
    feature.SetGeometry(in_geom)
    out_layer.CreateFeature(feature)
