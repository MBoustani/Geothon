#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/shp_info.py
Description:   This code gives shapefile information.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

#example shapefile file.
shp_file = '../static_files/shapefile/populated_places/ne_50m_populated_places.shp'

#set the driver to ESRI Shapefiel
driver = ogr.GetDriverByName('ESRI Shapefile')
#open shapefile
shp_datasource = driver.Open(shp_file)

#get shapefile name
shp_name = shp_datasource.GetName()

#get driver name
driver_name = shp_datasource.GetDriver().GetName()

#get number of layer
layer_num = shp_datasource.GetLayerCount()

#store layer info
layer_info = {}
layer_table = {}

if layer_num > 0:
    for i in range(layer_num):
        #get shapefile layer
        layer = shp_datasource.GetLayerByIndex(i)
        #get layer name
        layer_name = layer.GetName()
        layer_info['name'] = layer_name
        #get layer type
        geom_type = layer.GetGeomType()
        #convert layer type to geometry name
        geom_name = ogr.GeometryTypeToName(geom_type)
        layer_info['geometry'] = geom_name
        #get number of features in layer
        num_feature = layer.GetFeatureCount()
        layer_info['number of features'] = num_feature
        #get layer extent
        layer_extent = layer.GetExtent()
        layer_info['extent'] = layer_extent
        #get layer spatial reference (projection info)
        layer_spatial_ref = layer.GetSpatialRef()
        spatial_ref_name = layer_spatial_ref.ExportToWkt()
        layer_info['spatial reference'] = spatial_ref_name
        #get layer unit
        layer_unit = layer_spatial_ref.GetLinearUnitsName()
        layer_info['unit'] = layer_unit
        #get layer number of columns in shp attribute table
        layer_defn = layer.GetLayerDefn()
        num_field_col = layer_defn.GetFieldCount()
        layer_info['number of fields'] = num_field_col
        for field in range(num_field_col):
            field_name = layer_defn.GetFieldDefn(field).GetName()
            field_width = layer_defn.GetFieldDefn(field).GetWidth()
            field_code = layer_defn.GetFieldDefn(field).GetType()
            field_type = layer_defn.GetFieldDefn(field).GetFieldTypeName(field_code)
            layer_table[field_name] = [field_type, field_width]

#print all shapefile information
print "Shapefile Name: {0}".format(shp_name)
print "Driver Name: {0}".format(driver_name)
print "Number of Layer: {0}".format(layer_num)
print "     Layer Name: {0}".format(layer_info['name'])
print "     Geometry: {0}".format(layer_info['geometry'])
print "     Number of Features: {0}".format(layer_info['number of features'])
print "     Layer Extent: {0}".format(layer_info['extent'])
print "     Spatial Reference: {0}".format(layer_info['spatial reference'])
print "     Unit: {0}".format(layer_info['unit'])
print "     Number of Fields: {0}".format(layer_info['number of fields'])
print "         <Name>: <Type>(<width>)"
for field in layer_table:
    print "         {0}: {1}({2})".format(field, layer_table[field][0], layer_table[field][1])
