# Bucket Policies
<!--
1. [EODC CephAdapter](#eodc-cephadapter)
    1. [Configure s3 CEPH](#configure-s3-ceph)
    2. [Retrieve bucket policy CEPH](#retrieve-bucket-policy-ceph)
    3. [Set Policy CEPH](#set-policy-ceph)
2. [s3cmd](#s3cmd)
    1. [Configure s3cmd](#configure-s3cmd)
    2. [Retrieve bucket policy s3cmd](#retrieve-bucket-policy-s3cmd)
    3. [Set Policy s3cmd](#set-policy-s3cmd)
        1. [Grant permissions to an AWS account](#grant-permissions-to-an-aws-account)
        2. [Grant permissions to an IAM user](#grant-permissions-to-an-iam-user)
        3. [Grant permissions to an anonymous user](#grant-permissions-to-an-anonymous-user)
        4. [Read Access](#read-access)
        5. [Write Access](#write-access)
    4. [Delete Policy s3cmd](#delete-policy-s3cmd)
    5. [Example](#example-s3cmd)

3. [boto3](#boto3)
    1. [Configure s3 client](#configure-s3-client)
    2. [Retrieve bucket policy boto3](#retrieve-bucket-policy-boto3)
    3. [Set Policy boto3](#set-policy-boto3)
-->


## EODC CephAdapter

### Configure s3 CEPH

```python
import os
from eodc.workspace import CephAdapter

url = "https://objectstore.eodc.eu:2222"
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET = "test-ceph-adapter"

s3 = CephAdapter(url, ACCESS_KEY, SECRET_KEY)
```

### Retrieve bucket policy Ceph

```python
s3.describe_workspace_policy(workspace_name=BUCKET)
```

### Set Policy Ceph

```python
s3.set_workspace_public_readonly_access(workspace_name=BUCKET, object_names=['*'])
```

[S3cmd](https://s3tools.org/s3cmd)

### Configure s3cmd

For configuring s3cmd follow these [instructions](https://git.eodc.eu/eodc/knowledgebase/-/blob/objectstorage/source/EODC_Cloud/Object_storage/s3cmd_basics.md?ref_type=heads)

### Retrieve bucket policy

```sh
s3cmd info s3://BUCKET
```

### Set Policy 

When setting a policy on a s3 bucket you will grant permissions to specific aws users. The following covers the most suitable access policy permissions for READ and WRITE access. 

#### Grant permissions to an AWS account

To grant permissions to an AWS account, identify the account using the following format.

```JSON
"Principal":{"AWS":"arn:aws:iam::AccountIDWithoutHyphens:root"}
```

#### Grant permissions to an IAM user

To grant permission to an IAM user within your account, you must provide an "AWS":"user-ARN" name-value pair.

```JSON
"Principal":{"AWS":"arn:aws:iam::account-number-without-hyphens:user/username"}
```

#### Grant permissions to an anonymous user

```JSON
"Principal":"*"
```

#### Read-Access

```JSON
"Action": [
    "s3:ListBucket",
    "s3:GetObject"
],
```

#### Write-Access

```JSON
"Action": [
    "s3:ListBucket",
    "s3:GetObject",
    "s3:PutObject"
],
```

### Delete Policy

```sh
s3cmd delpolicy s3://BUCKET
```

### Example S3cmd

The following example sets a bucket policy for an anonymous User to READ.

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicBucket",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET-NAME"
            ]
        }
    ]
}
```

```sh
s3cmd setpolicy acl.json s3://BUCKET
```
```sh
s3cmd info s3://BUCKET
```

<!--
## [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) <a name="boto3"></a>

### Configure s3 client

```python
import boto3

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
REGION_NAME = "US"
ENDPOINT_URL = "https://objectstore.eodc.eu:2222"
BUCKET = "bucket-name"

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY,
                             region_name=REGION_NAME, endpoint_url=ENDPOINT_URL)

```

### Retrieve bucket policy boto3

```python
result = s3.get_bucket_policy(Bucket='BUCKET_NAME')
print(result['Policy'])
```

### Set Policy boto3 

```python
import json

# Create a bucket policy
bucket_name = 'BUCKET_NAME'
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicBucket",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET-NAME"
            ]
        }
    ]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
```




### Set Bucket acl's to Public-Read

```sh
s3cmd setacl s3://bucket --acl-public
```

With this command anyone can list the bucket. It is important to mention that at this stage the downloading of Objects is still prohibited.
If you want to set the Contents to Public as well, you will have to set the Acl for each object individually.

```cmd
s3cmd setacl s3//bucket/object-key --acl-public
```
"""
-->
