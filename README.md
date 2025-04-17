
# Amenity Access Analysis in London (2021 Census + OSM)

**Author**: Lina Abrahams  
**Course**: 5SSG2060 – Principles of Spatial Data Science  


This repository contains all spatial analysis and figure generation code used in the report:

> **“To what extent is walkable access to key daily amenities (schools, cafés, parks, and groceries) equitably distributed across London, and how do spatial scale and clustering influence our understanding of access inequality and planning justice?”**

---

##  Overview

This project investigates spatial inequality in access to daily amenities across London. The analysis combines:

- UK **2021 Census** data  
- **OpenStreetMap (OSM)** amenity data  
- **London Borough** and **LSOA boundaries**

The workflow applies spatial data science techniques from the module, including:

- Spatial joins & composite scoring  
- Kernel Density Estimation (KDE)  
- Global & Local Moran’s I (LISA)  
- Choropleth mapping  
- Cluster and outlier analysis

---

## Research Question

> To what extent is walkable access to key amenities equitably distributed across London, and how do spatial scale and spatial autocorrelation affect interpretations of planning justice?

---

## Key Figures

| Figure | Description |
|--------|-------------|
| **Figure 1** | Amenity locations across London (Schools, Cafés, Parks, Groceries) |
| **Figure 2** | Composite amenity access choropleth by borough |
| **Figure 3** | Ranked boroughs by total amenity access score |
| **Figure 4** | KDE heatmaps showing spatial density of each amenity |
| **Figure 5** | LISA cluster map (Local Moran's I) of access inequality |
| **Figure 6** | Boxplot of composite access scores across boroughs |
| **Figure 7** | Scatterplot – Park count vs. self-reported health (HealthVG21) |

---

## 🛠️ How to Reproduce

To run this project:
1. Clone this repository
2. Ensure your **input datasets** are placed in a folder named `/data`
3. Run `amenity_access_analysis_london.py`  
4. Output figures will be saved to a folder named `/figures`


---

##  Notes

- All code is written in Python using packages such as GeoPandas, OSMnx, PySAL, Seaborn, and Matplotlib.
- This project was developed as part of the 5SSG2060 module at King's College London.

---

## Contact

For any academic queries:  
**Lina Abrahams** – [GitHub Profile](https://github.com/LinaAbrahams)

---
