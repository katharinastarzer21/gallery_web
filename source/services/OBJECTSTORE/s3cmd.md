# s3cmd

Back to main gallery:

<div class="notebook-card" data-tags="" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;margin-bottom:20px">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="../../_static/object_storage/ceph_logo.png" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>Object Storage</strong><br>
    <div style="margin:4px 0 8px 0;">Back to main gallery.</div>
    <div style="margin:6px 0 10px 0;"></div>
    <a href="objectstore.md" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>

## s3cmd Basic Usage


There are various clients that can be used to interact with the object storage at EODC.
We can offer only limited support and guidance on using third party tools.

These clients make use of the S3 interface to the EODC Object storage.

It is expected that you have already generated your EC2 Credentials.
For more details, see the introduction to Object Storage page.

### Getting Started
s3cmd is a popular powerful python based open source CLI utility for interacting with object storage.
It is available in the default repository for most Linux distributions and also available for Mac.

Install it in the appropriate way for your environment
https://github.com/s3tools/s3cmd

First s3cmd must be configured for the environment
Be sure to have your EC2 credentials at hand!
This can be handled interactively:
```bash
[host] $ s3cmd --configure
 # Follow the prompts - Your settings will look similar

New settings:
  Access Key: $accessKey
  Secret Key: $secretKey
  Default Region: US
  S3 Endpoint: objectstore.eodc.eu:2222
  DNS-style bucket+hostname:port template for accessing a bucket: objectstore.eodc.eu:2222
  Encryption password: $optional
  Path to GPG program: /usr/bin/gpg
  Use HTTPS protocol: True
  HTTP Proxy server name:
  HTTP Proxy server port: 0
```

Alternatively create your own s3cfg file with the following template
```
[default]
access_key = $access
host_base = objectstore.eodc.eu:2222
host_bucket = objectstore.eodc.eu:2222
use_https = true
secret_key = $secret
```

```s3cmd -c s3cfg $command```

Now that s3cmd is configured, we can explore some basic usage

### Basic Usage

#### To list all available buckets
```
[host] $ s3cmd ls
2023-12-14 21:48  s3://Example
2023-12-15 16:20  s3://Example1
2023-12-05 12:08  s3://Example2
2023-12-20 17:11  s3://Example3
```

#### To list contents of a bucket
```
[host] $ s3cmd ls s3://bucket
2023-12-20 17:44            0  s3://bucket/example.file
```


#### To make a new bucket
```
[host] $ s3cmd mb s3://bucket
Bucket 's3://bucket/' created

[host] $ s3cmd ls
2023-12-14 21:48  s3://Example
2023-12-15 16:20  s3://Example1
2023-12-05 12:08  s3://Example2
2023-12-20 17:11  s3://Example3
2023-12-20 17:42  s3://bucket
```

#### To put a file in a bucket
```
[host] $ s3cmd put example.file s3://bucket
upload: 'example.file' -> 's3://bucket/example.file'  [1 of 1]
 0 of 0     0% in    0s     0.00 B/s  done
```

#### To delete a file in a bucket
```
[host] $ s3cmd ls s3://bucket
2023-12-20 17:44            0  s3://bucket/example.file
[host] $ s3cmd del s3://bucket/example.file
delete: 's3://bucket/example.file'
[host] $ s3cmd ls s3://bucket
[host] $
```

#### To remove a bucket
Note that a bucket must be empty before it can be removed.
```
[host] $ s3cmd rb s3://bucket
Bucket 's3://bucket/' removed
```




References
https://doc.swift.surfsara.nl/en/latest/Pages/Advanced/advanced_usecases.html
https://clouddocs.web.cern.ch/object_store/s3cmd.html

https://openmetal.io/docs/manuals/openstack-admin/swift-s3-api-access-with-s3cmd



## s3cmd Advanced Usage

s3cmd is a popular powerful python based open source CLI utility for interacting with object storage.
It is available in the default repository for most Linux distributions and also available for Mac.

This page assumes that you already have configured s3cmd for usage at EODC.
For further details, see the "Getting Started with s3cmd"


### Bucket Lifecycle - Expiration

Buckets can be configured with an lifecycle or expiration policy.
This policy allows for automatic removal of objects based on desired criteria.
These policies can be configured on a per-bucket or per-object basis.

#### Example Policy

Relative:
Here a policy is set that objects are automatically expired 14 days after they are created.

```
[host]$ s3cmd expire s3://bucket --expiry-days 14
Bucket 's3://bucket/': expiration configuration is set.

[host]$ s3cmd getlifecycle s3://bucket
<?xml version="1.0" ?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Rule>
                <ID>4sgzpl003evke1w66xl6czjixxq0wfvq7vhq89mu72v273tb</ID>
                <Prefix/>
                <Status>Enabled</Status>
                <Expiration>
                        <Days>14</Days>
                </Expiration>
        </Rule>
</LifecycleConfiguration>
```


Note that attempting to view the policy of a bucket without a configured policy will return a 404.

```
[host] $  s3cmd -c clouddemo getlifecycle s3://bucket
ERROR: S3 error: 404 (NoSuchLifecycleConfiguration)
```


Alternative and additional options for automatic expiration:

```
       --expiry-date=EXPIRY_DATE
              Indicates when the expiration rule takes effect. (only for [expire] command)

       --expiry-days=EXPIRY_DAYS
              Indicates the number of days after object creation the expiration rule takes effect. (only for [expire] command)

       --expiry-prefix=EXPIRY_PREFIX
              Identifying one or more objects with the prefix to which the expiration rule applies. (only for [expire] command)
```


#### Advanced Policies

Lifecycle Policies can be much more advanced 

See which actions are possible [here](https://docs.ceph.com/en/quincy/radosgw/bucketpolicy/).

[https://creodias.docs.cloudferro.com/en/latest/s3/Bucket-sharing-using-s3-bucket-policy-on-Creodias.html](https://creodias.docs.cloudferro.com/en/latest/s3/Bucket-sharing-using-s3-bucket-policy-on-Creodias.html)
