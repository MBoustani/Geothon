#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/buffer_shp_point.py
Description:   This code generate buffer polygon around point shapefile
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import numpy as np

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr
    
try:
    import gdal
except ImportError:
    from osgeo import gdal

from gdalconst import GA_ReadOnly

gtif_file = "/Users/Mboustani/Documents/Data/ASO/ASO_2014/SWE/swe20140502/TB20140502_SUPERswe_50p0m_scale1p075_agg_EXPORT.tif"
gtif_dataset = gdal.Open(gtif_file, GA_ReadOnly)

shp_file = '/Users/Mboustani/Documents/Data/ASO/ASO_2014/GIS/shapefiles/CH+EL+HH_HRUBorders130228/HH_HRU_Rev_wgs_84.shp'
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
for i in range(features_number):
    feat = layer.GetFeature(i)
    geom = feat.GetGeometryRef()
    '''
    polygon = geom.ConvexHull()
    ring = polygon.GetGeometryRef(0)
    numpoints = ring.GetPointCount()
    pointsX = []; pointsY = []
    for p in range(numpoints):
        lon, lat, z = ring.GetPoint(p)
        pointsX.append(lon)
        pointsY.append(lat)
    '''
    if (geom.GetGeometryName() == 'MULTIPOLYGON'):
        count = 0
        pointsX = []; pointsY = []
        for polygon in geom:
            geomInner = geom.GetGeometryRef(count)
            ring = geomInner.GetGeometryRef(0)
            numpoints = ring.GetPointCount()
            for p in range(numpoints):
                    lon, lat, z = ring.GetPoint(p)
                    pointsX.append(lon)
                    pointsY.append(lat)
            count += 1
    elif (geom.GetGeometryName() == 'POLYGON'):
        ring = geom.GetGeometryRef(0)
        numpoints = ring.GetPointCount()
        pointsX = []; pointsY = []
        for p in range(numpoints):
                lon, lat, z = ring.GetPoint(p)
                pointsX.append(lon)
                pointsY.append(lat)
    
    else:
        sys.exit("ERROR: Geometry needs to be either Polygon or Multipolygon")
    
    xmin = min(pointsX)
    xmax = max(pointsX)
    ymin = min(pointsY)
    ymax = max(pointsY)
    
    ID = feat.GetFieldAsInteger(1)#ID
 
    xoff = int((xmin - xOrigin)/pixelWidth)
    ###########################################################################
    yoff = int((yOrigin - ymax)/pixelWidth)
    xcount = int((xmax - xmin)/pixelWidth)+1
    ycount = int((ymax - ymin)/pixelWidth)+1
    print "xmin: {0}".format(xmin)
    print "xmax: {0}".format(xmax)
    print "ymin: {0}".format(ymin)
    print "ymax: {0}".format(ymax)
    print "xoff: {0}".format(xoff)
    print "yoff: {0}".format(yoff)
    print "xcount: {0}".format(xcount)
    print "ycount: {0}".format(ycount)

    
    banddataraster = gtif_dataset.GetRasterBand(1)
    if xoff < 0:
        xoff = 0
    if yoff< 0:
        yoff =0
    dataraster = banddataraster.ReadAsArray(xoff, yoff, xcount, ycount)#.astype(np.float)
    mean = np.mean(dataraster)
    f.write('{0}, {1}\n'.format(ID, mean))
    
    '''
    format = "GTiff"
    driver = gdal.GetDriverByName( format )
    dst_ds = driver.Create( 'test_{0}.tif'.format(i), xcount, ycount, 1, gdal.GDT_Float32 )
    dst_ds.GetRasterBand(1).WriteArray( dataraster )
    #pixelHeight = -1 * pixelHeight
    #dst_ds.SetGeoTransform([xmin, pixelWidth, 0, ymin, 0, pixelHeight])
    dst_ds.SetGeoTransform([xmin, pixelWidth, 0, ymin - (ycount*pixelHeight), 0, pixelHeight])
    #dst_ds.SetProjection(srs.ExportToWkt())
    dst_ds.SetProjection(gtif_dataset.GetProjectionRef())
    dst_ds = None
    src_ds = None
    '''