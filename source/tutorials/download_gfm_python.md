# GFM data discovery and download

EODC catalogs several datasets using the [STAC](http://stacspec.org/)
(SpatioTemporal Asset Catalog) specification. By providing a [STAC API](https://stac.eodc.eu/api/v1) endpoint,
we enable users to search our datasets by space, time and more filter criterias
depending on the individual dataset.

In this notebook, we demonstrate how to query the [Global Flood Monitoring](https://extwiki.eodc.eu/en/GFM) (GFM) STAC collection using the Python library
[pystac_client](https://pystac-client.readthedocs.io/en/latest/index.html) and
download the data using built-in Python libraries as well as utilizing the command line tool [stac-asset](https://github.com/stac-utils/stac-asset).

You can install the pystac_client via pip:

    pip install pystac_client

In the STAC items the respective assets (=file) are linked. These links are
used to download the file to a specified folder on your machine.


```python
from datetime import datetime
from pystac_client import Client

# EODC STAC API URL
api_url = "https://stac.eodc.eu/api/v1"

eodc_catalog = Client.open(api_url)
```

## Gridding of the GFM data sets

The GFM service processes all observations from the Sentinel-1A/B (soon including
Sentinel-1C) satellites that are acquired over land in Interferometric Wide-swath mode and
Ground Range Detected at High resolution (Sentinel-1 IW GRDH).

The GFM service uses the [Equi7Grid](https://www.sciencedirect.com/science/article/pii/S0098300414001629) that employs
the equidistant azimuthal projection and divides the
Earth surface into seven continental zones. The Equi7Grid with a 20m pixel
spacing and a 300km gridding (T3 level) serves as efficient working grid
representation for all steps in the data processing workflow. Consequently, all
input datasets, including auxiliary datasets from external sources, must be
re-projected to the Equi7Grid beforehand. 

The spatial extent of a Sentinel-1 scene is too large to be represented on only
one Equi7Tile (=file). Therefore, a search query usually will result with
multiple items, even for the same timestamp of a single Sentinel-1 observation.

## Searching

We can use the STAC API to find items that match specific criteria. This may
include the date and time the item covers, its spatial extent, or any other
property saved in the item's metadata.

If a specific Sentinel-1 scene is of interest, it is also possible to directly
use the sensing date in the search query.

### Search with AOI and time range

In this example we are searching for GFM data which cover our area of interest
over South Pakistan in September 2022.

The area of interest can be specified as `bbox` using the Python library
`shapely` or, alternateively, as GeoJSON object.

The time range can be specified as tuples of datetime object or simply using
strings. 


```python
from shapely.geometry import box

# STAC collection ID
collection_id = "GFM"

# Time range
time_range = (datetime(2022, 9, 15, 0, 0, 0), datetime(2022, 9, 16, 23, 59, 59))
time_range = '2022-09-15/2022-09-16'

# Area of interest (South Pakistan)
aoi = box(63.0, 24.0, 73, 27.0)

aoi = {
    "type" : "Polygon",
    "coordinates": [
        [
            [73.0, 24.0],
            [73.0, 27.0],
            [63.0, 27.0],
            [63.0, 24.0],
            [73.0, 24.0],
        ]
    ],
}

search = eodc_catalog.search(
    max_items=1000,
    collections=collection_id,
    intersects=aoi,
    datetime=time_range
)

items_eodc = search.item_collection()
print(f"On EODC we found {len(items_eodc)} items for the given search query")
```

### Search with Sentinel-1 scene identifier

In this example we are using a single Sentinel-1 scene identifier to retrieve
the respective STAC items. Either use the following simple method to derive the
sensing date from the Sentinel-1 scene identifier or directly use the exact
datetime in the query.


```python
# Method to derive the sensing date from a Sentinel-1 scene identifier
def get_sensing_date(scene:str) -> datetime:
    parts = scene.split("_")
    return datetime.strptime(parts[4], "%Y%m%dT%H%M%S")
```


```python
# Define Sentinel-1 scene identifier and asset name to plot
scene_id = "S1A_IW_GRDH_1SDV_20220930T224602_20220930T224627_045240_056863"

api_url = "https://stac.eodc.eu/api/v1"
eodc_catalog = Client.open(api_url)

search = eodc_catalog.search(
    collections=["GFM"],
    datetime=get_sensing_date(scene_id),
)

items_eodc = search.item_collection()
print(f"On EODC we found {len(items_eodc)} items for the given search query")
```

## Some information about the found STAC items

We can print some more information like the available assets and their
description.  


```python
import rich.table
from rich.console import Console

console = Console()

first_item = items_eodc[0]

table = rich.table.Table(title="Assets in STAC Item")
table.add_column("Asset Key", style="cyan", no_wrap=True)
table.add_column("Description")
for asset_key, asset in first_item.assets.items():
    table.add_row(
        asset.title, 
        asset.description)

console.print(table)
```

## Download data with Python

You can download the desired assets by specifying their respective asset keys in
a list object. Then, iterate over all found items and specified asset keys to
download the data to a local directory. The HTTP link saved in the asset
references the actual file, which is downloaded using the Python library `urllib`. 


```python
import os
import urllib

# specify output directory
download_root_path = "./downloaded_data/"

# specify asset names to download
asset_names = ["ensemble_flood_extent", "tuw_flood_extent"]

for item in items_eodc[:2]:
    download_path = os.path.join(download_root_path, item.collection_id, item.id)
    
    os.makedirs(download_path, exist_ok=True)
    
    for asset_name in asset_names:
        asset = item.assets[asset_name]
        if "data" in asset.roles:
            fpath = os.path.join(download_path, os.path.basename(asset.href))
            print(f"Downlading {fpath}")
            urllib.request.urlretrieve(asset.href, fpath)

print("Download done!")
```

## Download data with stac-asset CLI

The command line tool [stac-asset](https://github.com/stac-utils/stac-asset)
provides another way to query STAC APIs and download found assets.

You can install `stac-asset` via pip:

    pip install 'stac-asset[cli]'

`stac-assets` expects the same input parameters as described above:
- STAC API URL      
  - https://stac.eodc.eu/api/v1
- Collection ID
  - GFM
- Bounding box      
  - 63.0, 24.0, 73.0, 27.0 (minX, minY, maxX, maxY)
- Time range        
  - 2022-09-15/2022-09-16

### List the number of matched STAC items


```python
!stac-client search https://stac.eodc.eu/api/v1 -c GFM --bbox 63 24 73 27 --datetime 2022-09-15/2022-09-16 --matched
```

### Save matched STAC items into a JSON file (items.json)


```python
!stac-client search https://stac.eodc.eu/api/v1 -c GFM --bbox 63 24 73 27 --datetime 2022-09-15/2022-09-16 --save items.json
```

### Download a specified asset of found STAC items into a given directory


```python
!mkdir -p ./stac_asset_download
!stac-asset download -i ensemble_flood_extent items.json ./stac_asset_download -q
```

### Pipe query results directly into the stac-asset download command


```python
!mkdir -p ./stac_asset_download
!cd stac_asset_download; stac-client search https://stac.eodc.eu/api/v1 -c GFM --bbox 63 24 73 27 --datetime 2022-09-15/2022-09-16 | stac-asset download -i ensemble_flood_extent -q
```
