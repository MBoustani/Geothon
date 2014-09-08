#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/zonal_statistics.py
Description:   This code calculates statistics of GeoTIFF with polygon Shapefile
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import numpy as np

try:
    import ogr
except ImportError:
    from osgeo import ogr
    
try:
    import gdal
except ImportError:
    from osgeo import gdal

from gdalconst import GA_ReadOnly

gtif_file = "/path/to/tif"
gtif_dataset = gdal.Open(gtif_file, GA_ReadOnly)

shp_file = '/path/to/shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_datasource = driver.Open(shp_file)
#layer_num = shp_datasource.GetLayerCount()
layer = shp_datasource.GetLayer()

transform = gtif_dataset.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]

features_number = layer.GetFeatureCount()


f=open('table.txt','w')
f.write('ID, mean\n')

for each_feature in range(features_number):
    feature = layer.GetFeature(each_feature)
    feature_geom = feature.GetGeometryRef()
    pointsX = []
    pointsY = []
    feature_geom_type = feature_geom.GetGeometryName()

    #we need to get points from each feature
    #   so if it is Multipolygon we should get polygon
    #   first, ring from polygon after and points data
    #   from ring geometry
    if (feature_geom_type == 'MULTIPOLYGON'):
        num_geoms = feature_geom.GetGeometryCount()
        for geom in range(num_geoms):
            geomInner = feature_geom.GetGeometryRef(geom)
            ring = geomInner.GetGeometryRef(0)

    elif (feature_geom_type == 'POLYGON'):
        ring = feature_geom.GetGeometryRef(0)
    
    else:
        sys.exit("ERROR: Feature geometry needs to be either Polygon or Multipolygon")

    numpoints = ring.GetPointCount()
    for point in range(numpoints):
       lon, lat, z = ring.GetPoint(point)
       pointsX.append(lon)
       pointsY.append(lat)

    #calculate feature spatial extent
    xmin = min(pointsX)
    xmax = max(pointsX)
    ymin = min(pointsY)
    ymax = max(pointsY)
    
    #get feature ID (first column in shapefile attribute table)
    ID = feature.GetFieldAsInteger(1)

    xoff = int((xmin - xOrigin)/pixelWidth)
    yoff = int((yOrigin - ymax)/pixelWidth)
    xcount = int((xmax - xmin)/pixelWidth)+1
    ycount = int((ymax - ymin)/pixelWidth)+1

    banddataraster = gtif_dataset.GetRasterBand(1)
    if xoff < 0:
        xoff = 0
    if yoff< 0:
        yoff =0
    dataraster = banddataraster.ReadAsArray(xoff, yoff, xcount, ycount)#.astype(np.float)
    mean = np.mean(dataraster)
    f.write('{0}, {1}\n'.format(ID, mean))