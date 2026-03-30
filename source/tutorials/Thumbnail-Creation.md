# Titiler Overview

## Preview Images (Thumbnails-STAC)

<!--
1. [Titiler](#Preview-Images-thumbnails-stac)
1. [Titiler API](#titiler-api)
2. [Query Parameters](#query-parameters)
3. [Example Thumbnail](#example-thumbnail)
    1. [Output](#output)
    2. [Create Asset](#create-asset)

-->

The following Documentation is a step by step guide for how to create stac-thumbnails with [Titiler](https://titiler.services.eodc.eu/). 

## Titiler API

You can test the [Titiler API](https://titiler.services.eodc.eu/api.html#/Cloud%20Optimized%20GeoTIFF/preview_cog_preview_get).

## Query Parameters

The Query parameters are documented under this [link](https://developmentseed.org/titiler/endpoints/cog/#preview).

## Example Thumbnail

In this example a thumbnail will be created from a GeoTIFF in output format PNG.
Furthermore, the GeoTIFF will be reprojected to a different CRS.

```python
import requests
from pyproj import CRS

# Define the endpoint
endpoint = "https://titiler.services.eodc.eu/cog/preview"

# Define the url of the GeoTIFF
url = "https://objectstore.eodc.eu:2222/88346baf22914e828ad2c1763e5e01ff:greenness-austria/2022/greenness_max_id66904_2022.tiff"

# Define input and output CRS
crs_input = CRS.from_epsg(3035).to_wkt()
crs_output = CRS.from_epsg(4326).to_wkt()

# Define the query parameters as a dictionary

# Define "rescale": min, max (min, max values of a Band, e.g. with rasterio --> .min(), .max()) 
# --> rescale is used to normalize image bands, e.g.: bidx: 1, ranges from 0-19, which is not color encoded. 
# Titiler uses this rescaling information to normalize the band values from their original range (0-19) to the 0-255 range, 
# making the image ready for proper visualization.

# Define "nodata": str, int, float (Overwrite internal Nodata value.)
# Define "colormap_name": rio-tiler color map name
# Define "dst_crs": wkt
# Define "coord_crs": wkt

query_parameters = {
    "format": "png", 
    "url": url, #required
    "rescale": "1,19",
    "nodata": "-9999",
    "colormap_name": "greens_r",
    "dst_crs": crs_output,
    "coord_crs": crs_input
}

# Create a Request object
request = requests.Request('GET', endpoint, params=query_parameters)

# Prepare the request
href = request.prepare()

# Print the full URL with the query parameters
print(href.url)
```

### Output
[output-url](https://titiler.services.eodc.eu/cog/preview?format=png&url=https%3A%2F%2Fobjectstore.eodc.eu%3A2222%2F88346baf22914e828ad2c1763e5e01ff%3Agreenness-austria%2F2022%2Fgreenness_max_id66904_2022.tiff&rescale=1%2C19&colormap_name=greens_r&dst_crs=PROJCRS%5B%22ETRS89-extended+%2F+LAEA+Europe%22%2CBASEGEOGCRS%5B%22ETRS89%22%2CENSEMBLE%5B%22European+Terrestrial+Reference+System+1989+ensemble%22%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1989%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1990%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1991%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1992%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1993%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1994%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1996%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1997%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2000%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2005%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2014%22%5D%2CELLIPSOID%5B%22GRS+1980%22%2C6378137%2C298.257222101%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CENSEMBLEACCURACY%5B0.1%5D%5D%2CPRIMEM%5B%22Greenwich%22%2C0%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CID%5B%22EPSG%22%2C4258%5D%5D%2CCONVERSION%5B%22Europe+Equal+Area+2001%22%2CMETHOD%5B%22Lambert+Azimuthal+Equal+Area%22%2CID%5B%22EPSG%22%2C9820%5D%5D%2CPARAMETER%5B%22Latitude+of+natural+origin%22%2C52%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%2CID%5B%22EPSG%22%2C8801%5D%5D%2CPARAMETER%5B%22Longitude+of+natural+origin%22%2C10%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%2CID%5B%22EPSG%22%2C8802%5D%5D%2CPARAMETER%5B%22False+easting%22%2C4321000%2CLENGTHUNIT%5B%22metre%22%2C1%5D%2CID%5B%22EPSG%22%2C8806%5D%5D%2CPARAMETER%5B%22False+northing%22%2C3210000%2CLENGTHUNIT%5B%22metre%22%2C1%5D%2CID%5B%22EPSG%22%2C8807%5D%5D%5D%2CCS%5BCartesian%2C2%5D%2CAXIS%5B%22northing+%28Y%29%22%2Cnorth%2CORDER%5B1%5D%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CAXIS%5B%22easting+%28X%29%22%2Ceast%2CORDER%5B2%5D%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CUSAGE%5BSCOPE%5B%22Statistical+analysis.%22%5D%2CAREA%5B%22Europe+-+European+Union+%28EU%29+countries+and+candidates.+Europe+-+onshore+and+offshore%3A+Albania%3B+Andorra%3B+Austria%3B+Belgium%3B+Bosnia+and+Herzegovina%3B+Bulgaria%3B+Croatia%3B+Cyprus%3B+Czechia%3B+Denmark%3B+Estonia%3B+Faroe+Islands%3B+Finland%3B+France%3B+Germany%3B+Gibraltar%3B+Greece%3B+Hungary%3B+Iceland%3B+Ireland%3B+Italy%3B+Kosovo%3B+Latvia%3B+Liechtenstein%3B+Lithuania%3B+Luxembourg%3B+Malta%3B+Monaco%3B+Montenegro%3B+Netherlands%3B+North+Macedonia%3B+Norway+including+Svalbard+and+Jan+Mayen%3B+Poland%3B+Portugal+including+Madeira+and+Azores%3B+Romania%3B+San+Marino%3B+Serbia%3B+Slovakia%3B+Slovenia%3B+Spain+including+Canary+Islands%3B+Sweden%3B+Switzerland%3B+T%C3%BCrkiye+%28Turkey%29%3B+United+Kingdom+%28UK%29+including+Channel+Islands+and+Isle+of+Man%3B+Vatican+City+State.%22%5D%2CBBOX%5B24.6%2C-35.58%2C84.73%2C44.83%5D%5D%2CID%5B%22EPSG%22%2C3035%5D%5D&coord_crs=GEOGCRS%5B%22WGS+84%22%2CENSEMBLE%5B%22World+Geodetic+System+1984+ensemble%22%2CMEMBER%5B%22World+Geodetic+System+1984+%28Transit%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G730%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G873%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1150%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1674%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1762%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G2139%29%22%5D%2CELLIPSOID%5B%22WGS+84%22%2C6378137%2C298.257223563%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CENSEMBLEACCURACY%5B2.0%5D%5D%2CPRIMEM%5B%22Greenwich%22%2C0%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CCS%5Bellipsoidal%2C2%5D%2CAXIS%5B%22geodetic+latitude+%28Lat%29%22%2Cnorth%2CORDER%5B1%5D%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CAXIS%5B%22geodetic+longitude+%28Lon%29%22%2Ceast%2CORDER%5B2%5D%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CUSAGE%5BSCOPE%5B%22Horizontal+component+of+3D+system.%22%5D%2CAREA%5B%22World.%22%5D%2CBBOX%5B-90%2C-180%2C90%2C180%5D%5D%2CID%5B%22EPSG%22%2C4326%5D%5D)


![Created PNG](https://titiler.services.eodc.eu/cog/preview?format=png&url=https%3A%2F%2Fobjectstore.eodc.eu%3A2222%2F88346baf22914e828ad2c1763e5e01ff%3Agreenness-austria%2F2022%2Fgreenness_max_id66904_2022.tiff&rescale=1%2C19&colormap_name=greens_r&dst_crs=PROJCRS%5B%22ETRS89-extended+%2F+LAEA+Europe%22%2CBASEGEOGCRS%5B%22ETRS89%22%2CENSEMBLE%5B%22European+Terrestrial+Reference+System+1989+ensemble%22%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1989%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1990%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1991%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1992%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1993%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1994%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1996%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+1997%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2000%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2005%22%5D%2CMEMBER%5B%22European+Terrestrial+Reference+Frame+2014%22%5D%2CELLIPSOID%5B%22GRS+1980%22%2C6378137%2C298.257222101%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CENSEMBLEACCURACY%5B0.1%5D%5D%2CPRIMEM%5B%22Greenwich%22%2C0%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CID%5B%22EPSG%22%2C4258%5D%5D%2CCONVERSION%5B%22Europe+Equal+Area+2001%22%2CMETHOD%5B%22Lambert+Azimuthal+Equal+Area%22%2CID%5B%22EPSG%22%2C9820%5D%5D%2CPARAMETER%5B%22Latitude+of+natural+origin%22%2C52%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%2CID%5B%22EPSG%22%2C8801%5D%5D%2CPARAMETER%5B%22Longitude+of+natural+origin%22%2C10%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%2CID%5B%22EPSG%22%2C8802%5D%5D%2CPARAMETER%5B%22False+easting%22%2C4321000%2CLENGTHUNIT%5B%22metre%22%2C1%5D%2CID%5B%22EPSG%22%2C8806%5D%5D%2CPARAMETER%5B%22False+northing%22%2C3210000%2CLENGTHUNIT%5B%22metre%22%2C1%5D%2CID%5B%22EPSG%22%2C8807%5D%5D%5D%2CCS%5BCartesian%2C2%5D%2CAXIS%5B%22northing+%28Y%29%22%2Cnorth%2CORDER%5B1%5D%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CAXIS%5B%22easting+%28X%29%22%2Ceast%2CORDER%5B2%5D%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CUSAGE%5BSCOPE%5B%22Statistical+analysis.%22%5D%2CAREA%5B%22Europe+-+European+Union+%28EU%29+countries+and+candidates.+Europe+-+onshore+and+offshore%3A+Albania%3B+Andorra%3B+Austria%3B+Belgium%3B+Bosnia+and+Herzegovina%3B+Bulgaria%3B+Croatia%3B+Cyprus%3B+Czechia%3B+Denmark%3B+Estonia%3B+Faroe+Islands%3B+Finland%3B+France%3B+Germany%3B+Gibraltar%3B+Greece%3B+Hungary%3B+Iceland%3B+Ireland%3B+Italy%3B+Kosovo%3B+Latvia%3B+Liechtenstein%3B+Lithuania%3B+Luxembourg%3B+Malta%3B+Monaco%3B+Montenegro%3B+Netherlands%3B+North+Macedonia%3B+Norway+including+Svalbard+and+Jan+Mayen%3B+Poland%3B+Portugal+including+Madeira+and+Azores%3B+Romania%3B+San+Marino%3B+Serbia%3B+Slovakia%3B+Slovenia%3B+Spain+including+Canary+Islands%3B+Sweden%3B+Switzerland%3B+T%C3%BCrkiye+%28Turkey%29%3B+United+Kingdom+%28UK%29+including+Channel+Islands+and+Isle+of+Man%3B+Vatican+City+State.%22%5D%2CBBOX%5B24.6%2C-35.58%2C84.73%2C44.83%5D%5D%2CID%5B%22EPSG%22%2C3035%5D%5D&coord_crs=GEOGCRS%5B%22WGS+84%22%2CENSEMBLE%5B%22World+Geodetic+System+1984+ensemble%22%2CMEMBER%5B%22World+Geodetic+System+1984+%28Transit%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G730%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G873%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1150%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1674%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G1762%29%22%5D%2CMEMBER%5B%22World+Geodetic+System+1984+%28G2139%29%22%5D%2CELLIPSOID%5B%22WGS+84%22%2C6378137%2C298.257223563%2CLENGTHUNIT%5B%22metre%22%2C1%5D%5D%2CENSEMBLEACCURACY%5B2.0%5D%5D%2CPRIMEM%5B%22Greenwich%22%2C0%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CCS%5Bellipsoidal%2C2%5D%2CAXIS%5B%22geodetic+latitude+%28Lat%29%22%2Cnorth%2CORDER%5B1%5D%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CAXIS%5B%22geodetic+longitude+%28Lon%29%22%2Ceast%2CORDER%5B2%5D%2CANGLEUNIT%5B%22degree%22%2C0.0174532925199433%5D%5D%2CUSAGE%5BSCOPE%5B%22Horizontal+component+of+3D+system.%22%5D%2CAREA%5B%22World.%22%5D%2CBBOX%5B-90%2C-180%2C90%2C180%5D%5D%2CID%5B%22EPSG%22%2C4326%5D%5D)


### Create Asset
Finally add the created titiler url to an asset and add the asset to an item.

```python
import pystac

asset = pystac.Asset(
    href=href,
    media_type=pystac.MediaType.PNG,
    roles=["overview"]
)

item.add_asset(key=asset, asset=asset)
```