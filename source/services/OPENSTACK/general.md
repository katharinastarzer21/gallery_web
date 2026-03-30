# General introduction

Back to main gallery:

<div class="notebook-card" data-tags="" 
     style="display:flex;align-items:flex-start;border:1px solid #cddff1;
            border-radius:6px;padding:14px 20px;background:#f9fbfe;
            box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;
              align-items:center;justify-content:center;background:#fff;
              border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;
              margin-right:24px;">
    <img src="../../_static/openstack/openstack_logo.png" 
         alt="Thumbnail" 
         style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Openstack Gallery</strong><br>
    <div style="margin:4px 0 8px 0;">Back to main Openstack Gallery page.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="openstack.md" 
       style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

### Images
Images for your virtual machine are essentially the operating system. Currently, our available images are:
- Ubuntu
- Rocky
- Debian

If you would like to work with another image, please send a request to <a href="mailto:support@eodc.eu">support@eodc.eu</a>.

### Flavors
Flavors are the resources that you can allocate to your virtual machine.
Their naming convention consists of the number of CPUs and RAM.

### Volumes
Volumes are where and how you store your data.

We offer six different volume types in the EODC Cloud.  
This is divided between two options for replication and three different performance profiles.

The figures below are based on a 10GB volume size:

speed    |desired bw    | max bw    | desired iops    | max iops    | 
| --- | --- | --- | --- | --- | 
slow    |    2GBps    | 5GBps        |    5000        |    10k        |  
medium    |    5GBps    | 10GBps    |    15k            |    30k        |  
ultra    |    20GBps    | 50GBps    |    100k        |     1M        |  


Depending on your specific use case, there are different options to consider. Find some suggestions below:
- We recommend using the default volume size (15GB) for boot devices.  
- For additional storage needs, we recommend using additional volumes. This affords much greater flexibility, including allowing for later dynamic size changes.
- For critical data, a replication factor of 3 is recommended.

Our default volume type is "med-3repl".  
We feel this offers the best balance between cost and performance while ensuring the highest level of data integrity.  
We're happy to change the default volume type in your openstack project, just reach out to <a href="mailto:support@eodc.eu">support@eodc.eu</a>.
