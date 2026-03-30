# Adding a new process to the openEO processing dask

Back to main gallery:

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/openeo/openeo_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>pyGeoApi Yipeeo</strong><br>
    <div style="margin:4px 0 8px 0;">Back to main gallery.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="openeo_gallery.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

## Overview 

EODC's openEO backend can be extended with community processes. This documentation explains the steps you need to follow if you want to add your own process. There is also an [official guide](https://github.com/Open-EO/openeo-processes-dask/blob/main/.github/CONTRIBUTING.md) in the [openEO-processes-dask github](https://github.com/Open-EO/openeo-processes-dask).

## 1. Example Process

The process by which the procedure is described is a process to detect deep moist convection. Deep moist convection (DC) is associated with dangerous weather phenomena such as torrential rain, flash floods, large hail and tornadoes. The release of latent heat inside deep convective clouds often plays a crucial role. Studies have shown that DC and overshooting cloud tops penetrate into the lowest stratosphere and enable the exchange of gases from the troposphere deep into the stratosphere. The Sentinel satellites offer the possibility to monitor DC around the globe, independent of the emissivity of the ground. Detecting Deep Moist Convection (DDMC) is a combination of Deep Moist Convection, low- and mid-level cloudiness.
The template for the process comes from Stavros Dafis and can be found on [sentinelhub](https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/deep_moist_convection/).


## 2. Preparation

To add your own process to openeo, three different files must be prepared. One is the .py file with the process, one .py file with tests and the other is a .json file with all the information about the process.


### Python process file

With the Python file for the process, it is important that it really only contains the relevant code and no tests or other implementations. The process should also be written in one function if possible. Apart from the function, the file should contain all the required (openeo) libraries and small labels or explanations of the procedure.
You find examples for python scripts in the [openEO-processes-dask github](https://github.com/Open-EO/openeo-processes-dask/tree/main/openeo_processes_dask).

To add the process to the list of processes, you need to add your process to the `openeo_processes_dask/process_implementations/__init__.py` file.

All example files for DDMC can be found at the bottom of this document. 

### Python test file

The process must be sufficiently tested before it can be integrated into the production system. A test file must therefore be created. All possible errors and problems must be tested here using abstract data. Possible problems are incorrect input or coding errors, for example.

### JSON file

So that others can find and use the new process, it must be described in a JSON file. Information about the use case and the input and output of the process is recorded here. Examples can also be found in a [github repository](https://github.com/eodcgmbh/openeo-processes).


## 3. Pushing the process into the openEO processes dask

First you need to create a fork of both GitHub repositories, [openeo-processes-dask](https://github.com/Open-EO/openeo-processes-dask) and [openeo-processes](https://github.com/eodcgmbh/openeo-processes/tree/master).

The repositories can then be cloned to the local system.
`git clone https://github.com/<YOUR USER NAME>/openeo-processes-dask.git`

With `poetry install --all-extras`, all versions of libraries currently used on openEO can be downloaded.
If you want to add a new dependency run: `poetry add some_new_dependency`

All changes must be committed and pushed into a new branch of your openeo-processes-dask fork. Then a pull request can be created to merge the fork into the openeo/openeo-processes-dask. 
However, the following points should be noted beforehand:
- Add comments and documentation for your code
- Make sure your tests still run through and add additional tests
- Format your code nicely automatically after every commit - `run poetry run pre-commit install` and `pre-commit run --all-files` once, then it'll work for every commit 
- Add a descriptive comment to your commit and push your code to your openeo-processes-dask fork
- Create a PR with a descriptive title for your changes

To add the .json file to eodcgmbh/openeo-processes, you need to push your file into a branch in your fork and create a pull request.

After you requested a pull request, you need to wait for an approval from one of the repository-maintainers. They either approve your pull request or request changes.

## 4. Example code

The .py process file for ddmc looks like this:

```
from openeo_processes_dask.process_implementations.arrays import array_element
from openeo_processes_dask.process_implementations.cubes.general import add_dimension
from openeo_processes_dask.process_implementations.cubes.merge import merge_cubes
from openeo_processes_dask.process_implementations.cubes.reduce import reduce_dimension
from openeo_processes_dask.process_implementations.data_model import RasterCube

__all__ = ["ddmc"]


def ddmc(
    data: RasterCube,
    nir08="nir08",
    nir09="nir09",
    cirrus="cirrus",
    swir16="swir16",
    swir22="swir22",
    gain=2.5,
    target_band=None,
):
    dimension = data.openeo.band_dims[0]
    if target_band is None:
        target_band = dimension

    # Mid-Level Clouds
    def MIDCL(data):
        # B08 = array_element(data, label=nir08, axis = axis)

        B08 = data.sel(**{dimension: nir08})

        # B09 = array_element(data, label=nir09, axis = axis)

        B09 = data.sel(**{dimension: nir09})

        MIDCL = B08 - B09

        MIDCL_result = MIDCL * gain

        return MIDCL_result

    # Deep moist convection
    def DC(data):
        # B10 = array_element(data, label=cirrus, axis = axis)
        # B12 = array_element(data, label=swir22, axis = axis)

        B10 = data.sel(**{dimension: cirrus})
        B12 = data.sel(**{dimension: swir22})

        DC = B10 - B12

        DC_result = DC * gain

        return DC_result

    # low-level cloudiness
    def LOWCL(data):
        # B10 = array_element(data, label=cirrus, axis = axis)
        # B11 = array_element(data, label=swir16, axis = axis)
        B10 = data.sel(**{dimension: cirrus})
        B11 = data.sel(**{dimension: swir16})

        LOWCL = B11 - B10

        LOWCL_result = LOWCL * gain

        return LOWCL_result

    # midcl = reduce_dimension(data, reducer=MIDCL, dimension=dimension)
    midcl = MIDCL(data)
    midcl = add_dimension(midcl, name=target_band, label="midcl", type=dimension)

    # dc = reduce_dimension(data, reducer=DC, dimension=dimension)
    dc = DC(data)
    # dc = add_dimension(dc, target_band, "dc")
    dc = add_dimension(dc, target_band, label="dc", type=dimension)

    # lowcl = reduce_dimension(data, reducer=LOWCL, dimension=dimension)
    lowcl = LOWCL(data)
    lowcl = add_dimension(lowcl, target_band, label="lowcl", type=dimension)

    # ddmc = merge_cubes(merge_cubes(midcl, dc), lowcl)
    ddmc1 = merge_cubes(midcl, lowcl)
    ddmc1.openeo.add_dim_type(name=target_band, type=dimension)
    ddmc = merge_cubes(dc, ddmc1, overlap_resolver=target_band)

    # return a datacube
    return ddmc

```

The .py test file for ddmc looks like this:

```
from functools import partial

import numpy as np
import pytest
import xarray as xr
from openeo_pg_parser_networkx.pg_schema import BoundingBox, ParameterReference, TemporalInterval

from openeo_processes_dask.process_implementations.cubes.load import load_stac
from openeo_processes_dask.process_implementations.cubes.reduce import (
    reduce_dimension,
    reduce_spatial,
)
from openeo_processes_dask.process_implementations.ddmc import ddmc
from openeo_processes_dask.process_implementations.exceptions import ArrayElementNotAvailable
from tests.general_checks import general_output_checks
from tests.mockdata import create_fake_rastercube


@pytest.mark.parametrize("size", [(30, 30, 20, 5)])
@pytest.mark.parametrize("dtype", [np.float32])
def test_ddmc_instance_dims(temporal_interval: TemporalInterval, bounding_box: BoundingBox, random_raster_data):
    input_cube = create_fake_rastercube(
        data=random_raster_data,
        spatial_extent=bounding_box,
        temporal_extent=temporal_interval,
        bands=["nir08", "nir09", "cirrus", "swir16", "swir22"],
        backend="dask",
    )

    data = ddmc(input_cube)

    assert isinstance(data, xr.DataArray)
    assert set(input_cube.dims) == set(data.dims)

@pytest.mark.parametrize("size", [(30, 30, 20, 5)])
@pytest.mark.parametrize("dtype", [np.float32])
def test_ddmc_target_band(temporal_interval: TemporalInterval, bounding_box: BoundingBox, random_raster_data):
    input_cube = create_fake_rastercube(
        data=random_raster_data,
        spatial_extent=bounding_box,
        temporal_extent=temporal_interval,
        bands=["nir08", "nir09", "cirrus", "swir16", "swir22"],
        backend="dask",
    )

    data_band = ddmc(data=input_cube, target_band="ddmc")
    assert "ddmc" in data_band.dims

@pytest.mark.parametrize("size", [(30, 30, 20, 5)])
@pytest.mark.parametrize("dtype", [np.float32])
def test_ddmc_input_cube_exception(temporal_interval: TemporalInterval, bounding_box: BoundingBox, random_raster_data):
    input_cube_exception = create_fake_rastercube(
        data=random_raster_data,
        spatial_extent=bounding_box,
        temporal_extent=temporal_interval,
        bands=["b04", "nir09", "cirrus", "swir16", "swir22"],
        backend="dask",
    )

    with pytest.raises(KeyError):
        data = ddmc(input_cube_exception)

```

The .json description file for ddmc looks like this:

```
{
    "id": "ddmc",
    "summary": "Detecting Deep Moist Convection",
    "description": "Deep moist convection (DC) is associated with dangerous weather phenomena such as torrential rain, flash floods, large hail and tornadoes. The release of latent heat inside deep convective clouds often plays a crucial role. Studies have shown that DC and overshooting cloud tops penetrate into the lowest stratosphere and enable the exchange of gases from the troposphere deep into the stratosphere. The Sentinel satellites offer the possibility to monitor DC around the globe, independent of the emissivity of the ground. Detecting Deep Moist Convection is a combination of Deep Moist Convection, low- and mid-level cloudiness. \nThe `data` parameter expects a raster data cube with a dimension, by the default of the type `band` or otherwise another `target_band ` must be specified. By default, the dimension must have at least five bands with the common names `nir08`, `nir09`, `cirrus`, `swir16` and `swir22` assigned. Otherwise, the user has to specify the parameters. The common names for each band are specified in the collection's band metadata and are *not* equal to the band names.\n\nBy default, the dimension of type `bands` is renamed by this process. To keep the dimension, specify a new band name in the parameter `target_band`. This adds a new dimension label with the specified name to the dimension, which can be used to access the computed values.",
    "categories": [
        "cubes",
        "math > indices",
        "disaster management and prevention algorithms"
    ],
    "parameters": [
        {
            "name": "data",
            "description": "A raster data cube with five bands that have the common names `nir08`, `nir09`, `cirrus`,  `swir16` and `swir22` assigned.",
            "schema": {
                "type": "object",
                "subtype": "datacube",
                "dimensions": [
                    {
                        "type": "spatial",
                        "axis": [
                            "x",
                            "y"
                        ]
                    },
                    {
                        "type": "bands"
                    }
                ]
            }
        },
        {
            "name": "nir08",
            "description": "The name of the NIR band. Defaults to the band that has the common name `nir` assigned.\n\nEither the unique band name (metadata field `name` in bands) or one of the common band names (metadata field `common_name` in bands) can be specified. If the unique band name and the common name conflict, the unique band name has a higher priority.",
            "schema": {
                "type": "string",
                "subtype": "band-name"
            },
            "default": "nir08",
            "optional": true
        },
	{
            "name": "nir09",
            "description": "The name of the Water vapour band. Defaults to the band that has the common name `nir09` assigned.\n\nEither the unique band name (metadata field `name` in bands) or one of the common band names (metadata field `common_name` in bands) can be specified. If the unique band name and the common name conflict, the unique band name has a higher priority.",
            "schema": {
                "type": "string",
                "subtype": "band-name"
            },
            "default": "nir09",
            "optional": true
        },
        {
            "name": "cirrus",
            "description": "The name of the SWIR – Cirrus band. Defaults to the band that has the common name `cirrus` assigned.\n\nEither the unique band name (metadata field `name` in bands) or one of the common band names (metadata field `common_name` in bands) can be specified. If the unique band name and the common name conflict, the unique band name has a higher priority.",
            "schema": {
                "type": "string",
                "subtype": "band-name"
            },
            "default": "cirrus",
            "optional": true
        },
	{
            "name": "swir16",
            "description": "The name of the SWIR (ca 1600 nm) band. Defaults to the band that has the common name `swir16` assigned.\n\nEither the unique band name (metadata field `name` in bands) or one of the common band names (metadata field `common_name` in bands) can be specified. If the unique band name and the common name conflict, the unique band name has a higher priority.",
            "schema": {
                "type": "string",
                "subtype": "band-name"
            },
            "default": "swir16",
            "optional": true
        },
	{
            "name": "swir22",
            "description": "The name of the SWIR (ca 2200 nm) band. Defaults to the band that has the common name `swir22` assigned.\n\nEither the unique band name (metadata field `name` in bands) or one of the common band names (metadata field `common_name` in bands) can be specified. If the unique band name and the common name conflict, the unique band name has a higher priority.",
            "schema": {
                "type": "string",
                "subtype": "band-name"
            },
            "default": "swir22",
            "optional": true
        },
        {
            "name": "target_band",
            "description": "By default, the dimension is the band dimension. You can specify a new dimension name in this parameter so that a new dimension label with the specified name will be added for the computed values.",
            "schema": [
                {
                    "type": "string",
                    "pattern": "^\\w+$"
                },
                {
                    "type": "null"
                }
            ],
            "default": "band",
            "optional": true
        },
	{
            "name": "gain",
            "description": "The value by which the indices are to be multiplied. By default, gain is 2.5.",
            "schema": [
                {
                    "type": "double",
                    "pattern": "^\\w+$"
                },
                {
                    "type": "null"
                }
            ],
            "default": 2.5,
            "optional": true
        }
    ],
    "returns": {
        "description": "A raster data cube containing the computed DDMC values. The structure of the data cube differs depending on the value passed to `target_band`:\n `target_band` is a string: The data cube keeps the same dimensions. The dimension properties remain unchanged, but the number of dimension labels for the dimension of type `bands` increases by one. The additional label is named as specified in `target_band`.",
        "schema": {
            "type": "object",
            "subtype": "datacube",
            "dimensions": [
                {
                    "type": "spatial",
                    "axis": [
                        "x",
                        "y"
                    ]
                }
            ]
        }
    },
    "links": [
        {
            "rel": "about",
            "href": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/deep_moist_convection/",
            "title": "DDMC explained by sentinelhub"
        },
        {
            "rel": "about",
            "href": "https://earthobservatory.nasa.gov/features/MeasuringVegetation/measuring_vegetation_2.php",
            "title": "NDVI explained by NASA"
        }
    ]
}
```
