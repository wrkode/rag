# Rancher Assessment Generator

Very early work for a report/assessment Rancher tool.
RAG is currently able to connect to Rancher and list all managed clusters and limited details of cluster and associated nodes.

## Requirements

install the python requirements:
```pip3 install -r requirements.txt```

## Set Environment Variables

RAG requires the following environment variables to be set ahead of running:

- ```KUBECONFIG```: Path to rancher kubeconfig file
- ```RANCHER_SERVER_URL```: URL of the rancher server
- ```RANCHER_TOKEN_KEY```: Bearer token key for rancher UI (the user must be authorized to list details of all managed clusters in Rancher.)

## Run

simply run ```python3 rag.py```
The output will be displayed as follows:

~~~
Listing nodes with their IPs:
Node Name: rmsmig1
IP: 172.16.56.231
Node Name: rmsmig2
IP: 172.16.56.232
Node Name: rmsmig3
IP: 172.16.56.233
Cluster Name: edge-south, Cluster ID: c-m-85v2d64d, Kubernetes Version: v1.25.9+k3s1, Provider: k3s
+----------------------------------------+--------------+
|               Node Name                |   Node IP    |
+----------------------------------------+--------------+
| edge-south-southsrvedge-3f048a35-9tmfl | 172.16.56.60 |
+----------------------------------------+--------------+
Cluster Name: edge-north, Cluster ID: c-m-m92glq6g, Kubernetes Version: v1.25.9+k3s1, Provider: k3s
+-----------------------------------+--------------+
|             Node Name             |   Node IP    |
+-----------------------------------+--------------+
| edge-north-srvedge-bbca0fad-ksdgs | 172.16.56.67 |
+-----------------------------------+--------------+
Cluster Name: fwutil, Cluster ID: c-m-pkh4mdtn, Kubernetes Version: v1.24.13+rke2r1, Provider: rke2
+----------------------------+--------------+
|         Node Name          |   Node IP    |
+----------------------------+--------------+
| fwutil-srv-2c4513c3-xwkqk  | 172.16.56.77 |
| fwutil-agnt-2df2ff2c-nh8nc | 172.16.56.50 |
| fwutil-agnt-2df2ff2c-5tcdv | 172.16.56.78 |
| fwutil-agnt-2df2ff2c-rg2s9 | 172.16.56.30 |
+----------------------------+--------------+
Cluster Name: edge-east, Cluster ID: c-m-xq46scp2, Kubernetes Version: v1.24.13+k3s1, Provider: k3s
+---------------------------------+--------------+
|            Node Name            |   Node IP    |
+---------------------------------+--------------+
| edge-east-east01-f144cf88-5wnrh | 172.16.56.64 |
+---------------------------------+--------------+
Cluster Name: local, Cluster ID: local, Kubernetes Version: v1.24.4+rke2r1, Provider: rke2
+-----------+---------------+
| Node Name |    Node IP    |
+-----------+---------------+
|  rmsmig3  | 172.16.56.233 |
|  rmsmig1  | 172.16.56.231 |
|  rmsmig2  | 172.16.56.232 |


~~~

## TO-DO

Lots more :) .
