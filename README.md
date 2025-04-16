# amenity-access-analysis-London.
Code for spatial analysis of amenity access in London.
# Amenity Access Analysis in London (2021 Census + OSM)

This repository contains all Python code used for the spatial analysis and figure generation in the report:

**“To what extent is walkable access to key daily amenities (schools, cafés, parks, and groceries) equitably distributed across London, and how do spatial scale and clustering influence our understanding of access inequality and planning justice?”**

## Overview

This project explores spatial inequality in walkable access to key daily amenities across London. It combines data from the 2021 UK Census, OpenStreetMap (OSM), and official administrative boundaries to produce a multi-scalar spatial analysis. The research applies a range of geospatial techniques taught in the 5SSG2060 Principles of Spatial Data Science module at King’s College London.

Methods used include:
- Spatial joins and amenity point counts
- Composite scoring of walkability
- Kernel Density Estimation (KDE)
- Global and Local Moran’s I (LISA)
- Quantile-based choropleth mapping
- Cluster analysis
- Critical engagement with the Modifiable Areal Unit Problem (MAUP)

## Key Outputs

- **Figure 1**: Amenity Locations Map  
- **Figure 2**: Borough-Level Composite Access Choropleth  
- **Figure 3**: Ranked Bar Chart of Borough Amenity Scores  
- **Figure 4**: KDE Heatmaps for Schools, Parks, Cafés, and Groceries  
- **Figure 5**: Local Moran’s I (LISA) Cluster Map  
- **Figure 6**: Boxplot of Amenity Scores by Borough  
- **Figure 7**: Scatterplot of Park Count vs. Health (HealthVG21)

All maps were generated in Python and exported at high resolution.

## Installation

To run the analysis, install the required packages using pip:

```bash
pip install geopandas osmnx contextily matplotlib seaborn libpysal splot
Data Sources

This project uses the following datasets:
	•	2021 Census Data (HealthVG21) – Nomis / ONS
	•	London Borough and LSOA Boundaries – ONS Geoportal
	•	OpenStreetMap Amenity Data – Downloaded using OSMnx

Amenity tags used:
	•	"amenity": "school"
	•	"leisure": "park"
	•	"amenity": "cafe"
	•	"shop": ["supermarket", "grocery"]

Note: Due to size and licensing restrictions, raw data is not included in this repository. You will need to download these datasets manually and update file paths in the scripts to match your local setup.

How to Run
	1.	Clone or download this repository.
	2.	Obtain the datasets listed above and store them locally.
	3.	Open the Python script (analysis.py) or Jupyter notebook (if provided).
	4.	Update all file paths to match your local machine.
	5.	Run each block to:
	•	Load and clean spatial data
	•	Calculate spatial statistics
	•	Generate high-quality maps and visualisations

All outputs will be saved to the /figures directory.

Author

Lina Abrahams
BSc Geography, King’s College London
Course: 5SSG2060 – Principles of Spatial Data Science
Email: lina.abrahams@kcl.ac.uk

## License

This project is licensed under the MIT License. You are welcome to use, adapt, or cite it with appropriate credit.
