#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion Tools/point_shp_to_geotiff.py
Description:   This code converts point Shapefile to GeoTIFF file.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import numpy as np

try:
    import gdal
except ImportError:
    from osgeo import gdal

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr


#to find the nearest item in numpy array
def find_nearest(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

#an example shapefile file
shp_file = "../static_files/shapefile/populated_places/ne_50m_populated_places.shp"

#open shapefile
shp_datasource = ogr.Open(shp_file)

#get number of layers in shapefile
layer_number = shp_datasource.GetLayerCount()

for each in range(layer_number):
    #get Shapefile layer
    layer = shp_datasource.GetLayerByIndex(each)
    #get number of features
    features_number = layer.GetFeatureCount()
    #get Shapefile layer extent
    layer_extent = layer.GetExtent()
    #set the pixel resolution, for example 0.5
    resolution = .5
    #create range of longitudes
    longs_range = np.arange(layer_extent[0], layer_extent[1], resolution)
    #create range of latitudes
    lats_range = np.arange(layer_extent[2], layer_extent[3], resolution)
    #create zero numpy array to store raster values
    raster_values = np.zeros(((lats_range.shape)[0], (longs_range.shape)[0]), dtype=np.int)

    for i in range(features_number):
        #get each feature
        feature = layer.GetFeature(i)
        #get feature point
        point = feature.GetGeometryRef().GetPoint()
        y = np.where(lats_range == find_nearest(lats_range, point[1]))[0][0]
        x = np.where(longs_range == find_nearest(longs_range, point[0]))[0][0]
        raster_values[y][x] = 255

#define GeoTIFF format
gtif_format = "GTiff"
#set the driver
driver = gdal.GetDriverByName(gtif_format)
#output GeoTIFF file name
dst_filename = 'point_rasterized.tif'
band = 1
#create GeoTIFF raster dataset
dst_ds = driver.Create(dst_filename, longs_range.shape[0], lats_range.shape[0], band, gdal.GDT_Byte)
#set GeoTIFF geo transform
dst_ds.SetGeoTransform([layer_extent[0], resolution, 0, layer_extent[2], 0, resolution])
#set GeoTIFF projection
srs = osr.SpatialReference()
#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84 Zone 11
srs.ImportFromEPSG(4326)
dst_ds.SetProjection(srs.ExportToWkt())
#write pixel values in GeoTIFF dataset
dst_ds.GetRasterBand(1).WriteArray(raster_values)
