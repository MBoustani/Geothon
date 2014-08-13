#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_convex_hull.py
Description:   This code generates convex hull shapefile for point, line and polygon shapefile
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

#set driver to shapefile to be able to create a convex hull shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

#three point, line and polygon example shapefile
point_shp = "../static_files/shapefile/populated_places/ne_50m_populated_places.shp"
line_shp = "../static_files/shapefile/rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp"
polygon_shp = "../static_files/shapefile/land_boundaries/land_boundaries.shp"

files = {'point':point_shp, 'line': line_shp, 'polygon': polygon_shp}

for each in files:
    #open the shapefile
    datasource = ogr.Open(files[each])
    #output shapefile name (convex hull)
    convex_hull_shp = '{0}_convex_hull.shp'.format(each)
    #output shapefile layer name
    layer_name = 'convex_hull_layer'

    #create convex hull shapefile datasource
    if os.path.exists(convex_hull_shp):
        driver.DeleteDataSource(convex_hull_shp)
    convex_hull_datasource = driver.CreateDataSource(convex_hull_shp)

    #get number of layers of input shapefile
    layer_count = datasource.GetLayerCount()

    for layer in range(layer_count):
        #get layer of input shapefile
        shp_layer = datasource.GetLayerByIndex(layer)
        #get spatial reference of input shapefile
        srs = shp_layer.GetSpatialRef()

        #create convex hull layer
        convex_hull_layer = convex_hull_datasource.CreateLayer(layer_name, srs, ogr.wkbPolygon)

        #get number of features of input shapefile
        shp_feature_count = shp_layer.GetFeatureCount()

        #define convex hull feature
        convex_hull_feature = ogr.Feature(convex_hull_layer.GetLayerDefn())

        #define multipoint geometry to store all points
        multipoint = ogr.Geometry(ogr.wkbMultiPoint)

        for each_feature in range(shp_feature_count):
            #get feature from input shapefile
            shp_feature = shp_layer.GetFeature(each_feature)
            #get input feature geometry
            feature_geom = shp_feature.GetGeometryRef()
            #if geometry is MULTIPOLYGON then need to get
            #   POLYGON then LINEARRING to be able to get points
            if feature_geom.GetGeometryName() == 'MULTIPOLYGON':
                for polygon in feature_geom:
                    for linearring in polygon:
                        points = linearring.GetPoints()
                        for point in points:
                            point_geom = ogr.Geometry(ogr.wkbPoint)
                            point_geom.AddPoint(point[0], point[1])
                            multipoint.AddGeometry(point_geom)
            #if geometry is POLYGON then need to get
            #   LINEARRING to be able to get points
            elif feature_geom.GetGeometryName() == 'POLYGON':
                for linearring in feature_geom:
                    points = linearring.GetPoints()
                    for point in points:
                        point_geom = ogr.Geometry(ogr.wkbPoint)
                        point_geom.AddPoint(point[0], point[1])
                        multipoint.AddGeometry(point_geom)
            #if geometry is MULTILINESTRING then need to get
            #   LINESTRING to be able to get points
            elif feature_geom.GetGeometryName() == 'MULTILINESTRING':
                for multilinestring in feature_geom:
                    for linestring in multilinestring:
                        points = linestring.GetPoints()
                        for point in points:
                            point_geom = ogr.Geometry(ogr.wkbPoint)
                            point_geom.AddPoint(point[0], point[1])
                            multipoint.AddGeometry(point_geom)
            #if geometry is MULTIPOINT then need to get
            #   POINT to be able to get points
            elif feature_geom.GetGeometryName() == 'MULTIPOINT':
                for multipoint in feature_geom:
                    for each_point in multipoint:
                        points = each_point.GetPoints()
                        for point in points:
                            point_geom = ogr.Geometry(ogr.wkbPoint)
                            point_geom.AddPoint(point[0], point[1])
                            multipoint.AddGeometry(point_geom)
            #if the geomerty is POINT or LINESTRING then get points
            else:
                points = feature_geom.GetPoints()
            for point in points:
                point_geom = ogr.Geometry(ogr.wkbPoint)
                point_geom.AddPoint(point[0], point[1])
                multipoint.AddGeometry(point_geom)
        #convert multipoint to convex hull geometry
        convex_hull = multipoint.ConvexHull()
        #set the geomerty of convex hull shapefile feature
        convex_hull_feature.SetGeometry(convex_hull)
        #add the feature to convex hull layer
        convex_hull_layer.CreateFeature(convex_hull_feature)
