# amenity-access-analysis-London.
Code for spatial analysis of amenity access in London.
# Amenity Access Analysis in London (2021 Census + OSM)

This repository contains all Python code used for the spatial analysis and figure generation in the report:

**“To what extent is walkable access to key daily amenities (schools, cafés, parks, and groceries) equitably distributed across London, and how do spatial scale and clustering influence our understanding of access inequality and planning justice?”**

## Overview

The project explores spatial inequality in walkable access to daily amenities across London, using a combination of:
- 2021 UK Census data
- OpenStreetMap (OSM) amenity data
- London borough and LSOA boundaries

It applies techniques from the Principles of Spatial Data Science module, including:
- Spatial joins and composite scoring
- Kernel Density Estimation (KDE)
- Global and Local Moran’s I (LISA)
- Quantile-based choropleth mapping
- Cluster analysis
- Critical evaluation of the Modifiable Areal Unit Problem (MAUP)

## Key Outputs

- Figure 1: Amenity Locations Map  
- Figures 2–3: Composite Amenity Access Choropleths and Bar Charts  
- Figure 4: KDE Heatmaps (Schools, Cafés, Parks, Groceries)  
- Figure 5: LISA Cluster Map (Local Moran’s I)  
- Figure 6: Boxplot of Amenity Access by Borough  
- Figure 7: Scatterplot – Parks vs. Self-reported Health (HealthVG21)

## Project Structure
