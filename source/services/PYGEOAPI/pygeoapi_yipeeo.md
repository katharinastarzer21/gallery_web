# PyGeoApi: YIPEEO

Back to main gallery:

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/pygeoapi/pygeoapi_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>pyGeoApi Yipeeo</strong><br>
    <div style="margin:4px 0 8px 0;">Back to main gallery.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="pygeoapi.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>


## Connect to PyGeoApi service

The YIPEEO vector data is exposed as [OGC API - 
Features](https://ogcapi.ogc.org/features/) accessible via
[EODC's PyGeoApi](https://features.services.eodc.eu/). 

### Available YIPEEO collections

| Data set ID | Description | Access Level  |
|------------------------|-------------------------------------------------|-----------|
| pub_yipeeo_yield_fl    | Yield estimation and prediction at field level. | Public    |
| pub_yipeeo_yield_nuts2 | Yield estimation and prediction at NUTS2 level. | Public    |
| prv_yipeeo_yield_field | Yield estimation and prediction at field level. | Protected |
| prv_yipeeo_yield_nuts1 | Yield estimation and prediction at NUTS1 level. | Protected |
| prv_yipeeo_yield_nuts2 | Yield estimation and prediction at NUTS2 level. | Protected |
| prv_yipeeo_yield_nuts3 | Yield estimation and prediction at NUTS3 level. | Protected |
| prv_yipeeo_yield_nuts4 | Yield estimation and prediction at NUTS4 level. | Protected |
| prv_yipeeo_fertilize   | Data on fertilizer use at field level.          | Protected |
| prv_yipeeo_irrigate    | Data on irrigation use at field level.          | Protected |


The protected collections are only accessible using an EODC account.
This tutorial demonstates the use of the OGC API - Features making use to the
[owslib](https://owslib.readthedocs.io/en/latest/index.html) Python client and
the [EODC SDK](https://pypi.org/project/eodc/) for authentication.


```python
import geopandas as gpd
import contextily as cx
from rich.console import Console

# EODC SDK
from eodc.auth import DaskOIDC

# OWSLIB
from owslib.ogcapi.features import Features

# EODC OGC API URL
EODC_OGCAPI_URL = 'https://features.services.eodc.eu/'

console = Console()
```

## Without Authentication

Without Authentication, we can still list all available feature collections, as
well as all features from collections which are not protected. But we are not
able to read features from protected collections.


```python
# create eodc_ogcapi object without authentication header
eodc_ogcapi = Features(EODC_OGCAPI_URL)
feature_collections = eodc_ogcapi.feature_collections()
console.print(feature_collections)
```

Try to get items of a protected collection.


```python
collection_id = 'prv_yipeeo_yield_field'

# This will fail with an '401 Authorization required' error code
items = eodc_ogcapi.collection_items(collection_id)
```

## With Authentication

To read features from protected collections, you need to authenticate with your EODC
credentials. Enter your username, typically the email address you used to sign
up at EODC. A password prompt will be opened automatically.

After sucessful authentication, the access token will be used as HTTP header for
all future requests using OWSLIB. 


```python
# Enter your username, typically the
# email address you used to sign up at EODC
username = "firstname.lastname@eodc.eu" 

conn = DaskOIDC(username)

headers = {
    "Authorization": f"Bearer {conn.token['access_token']}"
}

# add HTTP headers to eodc_ogcapi object
eodc_ogcapi = Features(EODC_OGCAPI_URL, headers=headers)
```

Print properties of the first item of the given feature collection


```python
items = eodc_ogcapi.collection_items(collection_id)
console.print(items['features'][0]['properties'])
```

## Run a query to extract certain features
Query collection **prv_yipeeo_yield_field** for
 - common winter wheat (C1111)
 - winter barley (C1310), and 
 - for a given bounding box near Brno
 
 and we only want to have a subset of all attributes (properties)
 


```python
bbox = [16.229703926693578,48.713318232352485,17.472665146572798,49.4680057323523]

selected_props = "crop_type,crop_id,yield,c_year"

cql_filter = "crop_type='common winter wheat' OR crop_type='winter barley'"

# get all items in the yipeeo_yield_fl collection
field_items = eodc_ogcapi.collection_items(
    collection_id=collection_id,
    bbox=bbox,
    limit=2000,
    properties=selected_props,
    filter=cql_filter,
)
console.print(f"We found {len(field_items['features'])} items matching the query criteria.")
```

## Convert features into Geopandas DataFrame


```python
df = gpd.GeoDataFrame.from_features(field_items["features"], crs="EPSG:4326")
df 
```

## Plot geometries


```python
ax = df[["geometry"]].plot(
    facecolor="none", figsize=(12, 6)
)
cx.add_basemap(ax, crs=df.crs.to_string(), source=cx.providers.OpenStreetMap.Mapnik)
```
