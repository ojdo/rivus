import geopandas
import pandas as pd
import pandashp as pdshp
import shutil

# IN
buildings_filename = 'building' 
edge_filename = 'edge'

# OUT
to_edge_filename = 'to_edge'
blds_w_near_filename = 'building_w_nearest'

# DO
# read
buildings = geopandas.read_file(buildings_filename+'.shp')
edge = geopandas.read_file(edge_filename+'.shp')

# project to UTM zone 33N (=EPSG:32600 + zone number for north)
buildings = buildings.to_crs(epsg=32633)
edge = edge.to_crs(epsg=32633)

# find closest edge
to_edge = pdshp.find_closest_edge(buildings, edge, to_attr='Edge')
to_edge = geopandas.GeoDataFrame(to_edge)
to_edge.crs = edge.crs.copy()

# reproject back to geographic WGS 84 (EPSG:4326)
buildings = buildings.to_crs(epsg=4326)
edge = edge.to_crs(epsg=4326)
to_edge = to_edge.to_crs(epsg=4326)

# FINISH
to_edge.to_file(to_edge_filename+'.shp')
buildings.to_file(blds_w_near_filename+'.shp')
