# Amenity Access Analysis in London (2021 Census + OSM)
# Author: Lina Abrahams
# Course: 5SSG2060 – Principles of Spatial Data Science
# This script contains all spatial analysis and figure generation code used in the project.

Amenity Access Analysis in London (2021 Census + OSM)
Author: Lina Abrahams
Course: 5SSG2060 – Principles of Spatial Data Science

This script contains all spatial analysis and figure generation code used in the project.
# Amenity Access Analysis in London (2021 Census + OSM)
# Author: Lina Abrahams
# Course: 5SSG2060 – Principles of Spatial Data Science
# This script contains all spatial analysis and figure generation code used in the project.


# =====================
# LIBRARIES & SETTINGS
# =====================
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import osmnx as ox
import contextily as cx
import warnings
from shapely import wkt
from scipy.stats import pearsonr
from matplotlib_scalebar.scalebar import ScaleBar
from libpysal import weights
from pysal.explore import esda
from splot.esda import lisa_cluster

warnings.filterwarnings("ignore")

import os
os.makedirs("figures", exist_ok=True)

# =====================
# LOAD DATA
# =====================

# Load census data
df = pd.read_csv("data/UKCensus-21-11-London.csv")
df['geometry'] = df['geometry'].apply(wkt.loads)
census_gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:27700")

# Load borough shapefile
boroughs = gpd.read_file("data/boroughs.shp").to_crs(epsg=27700)

# Get OSM boundary
place = "London, UK"
boundary_gdf = ox.geocode_to_gdf(place)
boundary_polygon = boundary_gdf.geometry.unary_union

# Download OSM amenities
school_tags = {"amenity": "school"}
cafe_tags = {"amenity": "cafe"}
park_tags = {"leisure": "park"}
grocery_tags = {"shop": ["supermarket", "grocery"]}

schools = ox.geometries_from_polygon(boundary_polygon, school_tags).to_crs(epsg=27700)
cafes = ox.geometries_from_polygon(boundary_polygon, cafe_tags).to_crs(epsg=27700)
parks = ox.geometries_from_polygon(boundary_polygon, park_tags).to_crs(epsg=27700)
groceries = ox.geometries_from_polygon(boundary_polygon, grocery_tags).to_crs(epsg=27700)

# =====================
# COUNT AMENITIES PER LSOA
# =====================

def count_amenities(amenity_gdf, census_gdf, amenity_name):
    if not amenity_gdf.geom_type.isin(["Point"]).all():
        amenity_gdf["geometry"] = amenity_gdf.centroid
    join_gdf = gpd.sjoin(amenity_gdf, census_gdf, how="inner", predicate="within")
    counts = join_gdf.groupby("LSOA21CD").size().rename(amenity_name + "_count")
    return counts

for name, gdf in zip(["schools", "cafes", "parks", "groceries"], [schools, cafes, parks, groceries]):
    count = count_amenities(gdf, census_gdf, name)
    census_gdf = census_gdf.merge(count, on="LSOA21CD", how="left")
    census_gdf[name + "_count"] = census_gdf[name + "_count"].fillna(0).astype(int)

# =====================
# FIGURE 1 – AMENITY LOCATIONS
# =====================
fig, ax = plt.subplots(figsize=(12, 12))
boroughs.plot(ax=ax, color='whitesmoke', edgecolor='black', linewidth=0.5)
schools.plot(ax=ax, color='blue', markersize=8, label='Schools')
cafes.plot(ax=ax, color='green', markersize=8, label='Cafés')
parks.plot(ax=ax, color='orange', markersize=8, label='Parks')
groceries.plot(ax=ax, color='red', markersize=8, label='Groceries')
ax.set_title("Figure 1: Locations of Key Amenities in London", fontsize=14)
ax.axis("off")
plt.legend()
plt.tight_layout()
plt.savefig("figures/Figure1_Amenity_Locations.png", dpi=300)
plt.show()

# =====================
# FIGURE 2 – COMPOSITE AMENITY SCORE (CHOROPLETH)
# =====================
census_gdf["composite_access"] = (
    census_gdf["schools_count"] + census_gdf["cafes_count"] +
    census_gdf["parks_count"] + census_gdf["groceries_count"]
)

boroughs_counts = census_gdf.dissolve(by="LAD22NM", aggfunc="sum").reset_index()
boroughs_counts = boroughs_counts.to_crs(epsg=27700)

fig, ax = plt.subplots(figsize=(12, 12))
choropleth = boroughs_counts.plot(
    column="composite_access", ax=ax, cmap="YlOrRd", linewidth=0.8,
    edgecolor="black", scheme="Quantiles", k=5, legend=True,
    legend_kwds={'title': "Composite Amenity Access Score", 'fmt': '{:.0f}'}
)
ax.set_title("Figure 2: Composite Amenity Count by Borough", fontsize=16, fontweight="bold")
ax.axis("off")
scalebar = ScaleBar(1, location='lower left', box_alpha=0, font_properties={'size': 12})
ax.add_artist(scalebar)
plt.tight_layout()
plt.savefig("figures/Figure2_Composite_Choropleth.png", dpi=300)
plt.show()


# =====================
# FIGURE 3 – BOROUGH RANKED AMENITY SCORES (BAR CHART)
# =====================
boroughs_sorted = boroughs_counts.sort_values("composite_access", ascending=False)

plt.figure(figsize=(10, 10))
plt.barh(boroughs_sorted["LAD22NM"], boroughs_sorted["composite_access"], color="steelblue")
plt.xlabel("Amenity Score", fontsize=12, fontweight="bold")
plt.ylabel("Borough", fontsize=12, fontweight="bold")
plt.title("Figure 3: Borough-Level Composite Amenity Scores", fontsize=14)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("figures/Figure3_Borough_Amenity_Scores.png", dpi=300)
plt.show()

# =====================
# FIGURE 4 – KDE HEATMAPS
# =====================
xmin, ymin, xmax, ymax = boroughs.total_bounds
fig, axs = plt.subplots(2, 2, figsize=(16, 16))
amenity_dict = {
    "Schools": (schools, "Blues"),
    "Cafés": (cafes, "Greens"),
    "Parks": (parks, "Oranges"),
    "Groceries": (groceries, "Reds")
}
for ax, (name, (gdf, cmap)) in zip(axs.flatten(), amenity_dict.items()):
    boroughs.plot(ax=ax, color="none", edgecolor="black", linewidth=0.5)
    x = gdf.geometry.x
    y = gdf.geometry.y
    sns.kdeplot(x=x, y=y, ax=ax, cmap=cmap, fill=True, thresh=0.05, alpha=0.6)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_title(f"{name} (500m KDE)", fontsize=14, fontweight="bold")
    ax.axis("off")
fig.suptitle("Figure 4: KDE Heatmaps for Amenity Density", fontsize=18, y=0.95)
plt.tight_layout()
plt.savefig("figures/Figure4_KDE_Heatmaps.png", dpi=300)
plt.show()

# =====================
# FIGURE 5 – LISA CLUSTER MAP
# =====================
if census_gdf.crs is None:
    census_gdf.set_crs(epsg=4326, inplace=True)
census_gdf = census_gdf.to_crs(epsg=27700)

knn_weights = weights.KNN.from_dataframe(census_gdf, k=8, ids=census_gdf["LSOA21CD"])
knn_weights.transform = "R"
moran_local = esda.Moran_Local(census_gdf["composite_access"], knn_weights, permutations=999)

census_gdf["local_I"] = moran_local.Is
census_gdf["local_p"] = moran_local.p_sim

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
lisa_cluster(moran_local, census_gdf, p=0.05, ax=ax)
ax.set_title("Figure 5: Local Moran's I (LISA) Cluster Map", fontsize=14)
plt.savefig("figures/Figure5_LISA_Cluster.png", dpi=300)
plt.show()

# =====================
# FIGURE 6 – BOXPLOT BY BOROUGH
# =====================
plt.figure(figsize=(14, 8))
sns.boxplot(x="LAD22NM", y="composite_access", data=census_gdf, palette="Set3")
plt.xticks(rotation=90)
plt.xlabel("Borough")
plt.ylabel("Composite Access Score")
plt.title("Figure 6: Boxplot of Composite Access Scores by Borough")
plt.tight_layout()
plt.savefig("figures/Figure6_Boxplot.png", dpi=300)
plt.show()

# =====================
# FIGURE 7 – SCATTERPLOT: PARK COUNT VS. HEALTH
# =====================
if "HealthVG21" in census_gdf.columns:
    plt.figure(figsize=(10, 6))
    sns.regplot(x="parks_count", y="HealthVG21", data=census_gdf,
                scatter_kws={"alpha": 0.6}, ci=None, color="darkgreen")
    plt.xlabel("Parks Count")
    plt.ylabel("Self-reported Health (HealthVG21)")
    plt.title("Figure 7: Parks Count vs. Self-reported Health")
    plt.tight_layout()
    plt.savefig("figures/Figure7_Health_Scatterplot.png", dpi=300)
    plt.show()
else:
    print("HealthVG21 variable not found.")
