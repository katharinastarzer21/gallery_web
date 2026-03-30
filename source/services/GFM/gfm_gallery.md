# GFM 

GFM ([Global Flood Monitoring](https://global-flood.emergency.copernicus.eu/technical-information/glofas-gfm/)) is part of the Copernicus Emergency Management Service (CEMS).
It provides near real-time global flood maps derived from Sentinel-1 radar data, automatically detecting flooded areas anywhere in the world — day or night, in any weather.

EODC supports GFM by offering the cloud infrastructure to store and process these datasets.
Through the EODC platform, you can access GFM data via STAC, and use tools like Dask or openEO to analyse and visualize flood products directly in the cloud — without downloading data.

<div id="gallery" style="display:flex;flex-direction:column;gap:20px;max-width:900px;">
<div class="notebook-card" data-tags="GFM" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Save GFM results in cloud object store</strong><br>
    <div style="margin:4px 0 8px 0;">In this demo we will show you how to remotely process data on the EODC cluster using dask and save the result in a cloud object store.</div>
    <a href="gfm_dask_objectstorage.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

<div class="notebook-card" data-tags="GFM filter" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Refine STAC query using filters</strong><br>
    <div style="margin:4px 0 8px 0;">In this notebook, we demonstrate how to refine the query against the GFM STAC catalogue using the filter STAC API extension</div>
    <a href="gfm_filter.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="GFM DASK" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>EODC Dask Tutorial</strong><br>
    <div style="margin:4px 0 8px 0;">In this notebook we demonstrate the basics of using Dask on the EODC cluster.</div>
    <a href="gfm_maximum_flood_extent_dask.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="GFM STAC" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>GFM maximum flood extent with STAC</strong><br>
    <div style="margin:4px 0 8px 0;">This notebook will demonstrate how to find data using STAC, load it into a xarray object and calculate a result.</div>
    <a href="gfm_maximum_flood_extent_local.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="GFM STAC" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Computation of GFM Maximum Flood Extent for a specific area and time of interest</strong><br>
    <div style="margin:4px 0 8px 0;">With this notebook we demonstrate how STAC can be used to find GFM data (ensemble_flood_extent) and derive the maximum flood extent from it.</div>
    <a href="gfm_maximum_flood_extent_simple_plot.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="GFM STAC" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Compute maximum flood extent utilizing STAC</strong><br>
    <div style="margin:4px 0 8px 0;">With this notebook, we want to demo how STAC can be used to find GFM ensemble_flood_extent data and derive the maximum flood extent from it.</div>
    <a href="gfm_maximum_flood_extent_stac.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="GFM" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="https://european-flood.emergency.copernicus.eu/efas_frontend/assets/img/wms/GFM.svg" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Plot GFM flood scene</strong><br>
    <div style="margin:4px 0 8px 0;">This tutorial will show how to plot a part of a flooded GFM scene using an OpenStreetMap basemap as background.</div>
    <a href="gfm_plot_flood_scene.ipynb" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
</div>