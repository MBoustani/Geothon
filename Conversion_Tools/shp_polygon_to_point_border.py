#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_polygon_to_point_border.py
Description:   This code converts shapfile polygon to shapefile point border of polygon.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example of shapefile data
polygon_shp_file = "../static_files/shapefile/land_boundaries/land_boundaries.shp"

#open polygon shapefile
polygon_datasource = ogr.Open(polygon_shp_file)

#set driver to shapefile to be able to create point shapefile file
driver = ogr.GetDriverByName('ESRI Shapefile')

#output point shapefile file name
point_shp_file = 'points.shp'

#output point shapefile file layer name
layer_name = 'point_layer'

#create point shapefile data_source(file)
if os.path.exists(point_shp_file):
    driver.DeleteDataSource(point_shp_file)
point_datasource = driver.CreateDataSource(point_shp_file)

#get number of layers in polygon shapefile
layer_count = polygon_datasource.GetLayerCount()
for layer in range(layer_count):
    #get layer from polygon shapefile
    layer = polygon_datasource.GetLayerByIndex(layer)
    #get spatial reference from polygon shapefile
    srs = layer.GetSpatialRef()

    #create point shapefile layer with same polygon shapefile's reference
    point_shp_layer = point_datasource.CreateLayer(layer_name, srs, ogr.wkbPoint)

    #get number of features in polygon shapefile
    feature_count = layer.GetFeatureCount()
    for feature in range(feature_count):
        #get polygon shapefile's feature
        polygon_feature = layer.GetFeature(feature)
        #get polygon shapefile's feature geometry
        feature_geom = polygon_feature.GetGeometryRef()

        for geom in feature_geom:
            #get feature geometry type by name
            gtype = geom.GetGeometryName()
            #if geometry type is Linearring then get points
            if gtype == "LINEARRING":
                points = geom.GetPoints()
            #if geometry type is not Linearring, it is Polygon Geometry,
            #   then get Linearring geometry from Polygon geometry and then
            #   get points.
            else:
                points = geom.GetGeometryRef(0).GetPoints()
            #create point features from points and add to point shapefile's layer
            for point in points:
                point_geom = ogr.Geometry(ogr.wkbPoint)
                point_geom.AddPoint(point[0], point[1])
                point_feature = ogr.Feature(point_shp_layer.GetLayerDefn())
                point_feature.SetGeometry(point_geom)
                point_shp_layer.CreateFeature(point_feature)
