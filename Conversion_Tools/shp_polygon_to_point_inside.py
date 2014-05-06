#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_polygon_to_point_inside.py
Description:   This code converts shapfile polygon to shapefile point inside the polygon.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os
import numpy as np

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example of shapefile polygon file
polygon_shp_file = "../static_files/shapefile/land_boundaries/land_boundaries.shp"

#open the polygon shapefile
polygon_datasource = ogr.Open(polygon_shp_file)

#set driver to shapefile to be able to create a point shapefile file
driver = ogr.GetDriverByName('ESRI Shapefile')

#output point shapefile file name
point_shp_file = 'points.shp'

#output point shapefile file layer name
layer_name = 'point_layer'

#create point shapefile data_source(file)
if os.path.exists(point_shp_file):
    driver.DeleteDataSource(point_shp_file)
point_datasource = driver.CreateDataSource(point_shp_file)

#get number of layers on polygon shapefile
layer_count = polygon_datasource.GetLayerCount()

for layer in range(layer_count):
    #get polygon shapefile layer
    layer = polygon_datasource.GetLayerByIndex(layer)
    #get polygon shapefile spatial reference system
    srs = layer.GetSpatialRef()

    #create point shapefile with same spatial reference as polygon shapefile
    point_shp_layer = point_datasource.CreateLayer(layer_name, srs, ogr.wkbPoint)
    #get layer extent of polygon shapefile
    extent = layer.GetExtent()
    min_lat = extent[2]
    max_lat = extent[3]
    min_long = extent[0]
    max_long = extent[1]

    #get range of latitude and logitude of polygon shapefile
    #in this example, 3 has been choosen for steps
    long_range = np.arange(min_long, max_long, 3)
    lat_range = np.arange(min_lat, max_lat, 3)

    #get number of features from polygon shapefile's layer
    feature_count = layer.GetFeatureCount()
    for each in range(feature_count):
        #get polygon feature
        polygon_feature = layer.GetFeature(each)
        #get geometry of polygon feature
        feature_geom = polygon_feature.GetGeometryRef()

        #to store all desire points
        points = []

        #loop over all point inside polygon
        for lon in long_range:
            for lat in lat_range:
                #define point geometry
                point_geom = ogr.Geometry(ogr.wkbPoint)
                #add point to point geometry
                point_geom.AddPoint(lon, lat)
                #if point is inside the polygon or in border of polygon, it is a desire point
                if point_geom.Within(feature_geom) or point_geom.Touches(feature_geom):
                    #add a desire point to list of points
                    points.append(point_geom)

        for point in points:
            #define feature for point shapefile
            point_feature = ogr.Feature(point_shp_layer.GetLayerDefn())
            #add point to feature
            point_feature.SetGeometry(point)
            #add feature to layer
            point_shp_layer.CreateFeature(point_feature)
