# Sentinel 2

Back to main gallery:

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/stac/stac_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>STAC</strong><br>
    <div style="margin:4px 0 8px 0;">Back to main gallery.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="stac.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

## Read Sentinel-2 data from remote location

```python
from pystac.extensions.eo import EOExtension as eo
import pystac_client
import planetary_computer
from rich.console import Console
console = Console()

catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)
```


```python
time_range = "2023-09-01/2023-09-21"

# GEOJSON can be created on geojson.io
area_of_interest = {
  "coordinates": [
          [
            [
              14.631570827879642,
              48.95580055524857
            ],
            [
              14.631570827879642,
              48.495695436823524
            ],
            [
              15.727627794927486,
              48.495695436823524
            ],
            [
              15.727627794927486,
              48.95580055524857
            ],
            [
              14.631570827879642,
              48.95580055524857
            ]
          ]
        ],
        "type": "Polygon"
}
```


```python
search = catalog.search(
    collections=["sentinel-2-l2a"],
    intersects=area_of_interest,
    datetime=time_range,
    query={"eo:cloud_cover": {"lt": 10},
           "s2:nodata_pixel_percentage": {"lt": 20}},
)

# Check how many items were returned
items = search.item_collection()
console.print(f"Returned {len(items)} Items")
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Returned <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span> Items
</pre>




```python
least_cloudy_item = min(items, key=lambda item: eo.ext(item).cloud_cover)

console.print(
    f"Choosing {least_cloudy_item.id} from {least_cloudy_item.datetime.date()}"
    f" with {eo.ext(least_cloudy_item).cloud_cover}% cloud cover"
)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Choosing S2A_MSIL2A_20230907T100031_R122_T33UWQ_20230907T211348 from <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2023</span>-<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">09</span>-<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">07</span> with <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.000488</span>% cloud cover
</pre>




```python
asset_href = least_cloudy_item.assets["visual"].href
```


```python
asset_href = items[10].assets["visual"].href
```


```python
import rasterio
from rasterio import windows,features, warp, crs

import numpy as np
from PIL import Image

with rasterio.open(asset_href) as ds:
    aoi_bounds = features.bounds(area_of_interest)
    warped_aoi_bounds = warp.transform_bounds(crs.CRS.from_epsg(4326), ds.crs, *aoi_bounds)
    aoi_window = windows.from_bounds(transform=ds.transform, *warped_aoi_bounds)
    band_data = ds.read(window=aoi_window)
```


```python
img = Image.fromarray(np.transpose(band_data, axes=[1, 2, 0]))
w = img.size[0]
h = img.size[1]
aspect = w / h
target_w = 800
target_h = (int)(target_w / aspect)
img.resize((target_w, target_h), Image.Resampling.BILINEAR)
```




    
![png](Sentinel-2_files/Sentinel-2_8_0.png)
    




```python

```
