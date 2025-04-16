# Amenity Access Analysis in London (2021 Census + OSM)

This repository contains all Python code used for the spatial analysis and figure generation in the report:

“To what extent is walkable access to key daily amenities (schools, cafés, parks, and groceries) equitably distributed across London, and how do spatial scale and clustering influence our understanding of access inequality and planning justice?”

## Overview

This project explores spatial inequality in walkable access to key daily amenities across London using data from the 2021 UK Census and OpenStreetMap. Techniques include KDE, Moran's I, LISA, and composite scoring using spatial joins and GeoDataFrames.

## Requirements

Install packages:

```bash
pip install geopandas osmnx contextily matplotlib seaborn libpysal splot
```

## How to Use

- Place your input data in a folder called `data/`
- Run `amenity_access_analysis_london.py`
- Outputs will be saved to a folder called `figures/`

## Author

Lina Abrahams  
King's College London – 5SSG2060  
