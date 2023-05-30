# Rancher Assessment Generator (RAG)

Very early work for a report/assessment Rancher tool.
RAG is currently able to connect to Rancher and list all managed clusters and limited details of the associated nodes (hostname, IPs)

## Requirements

install the python requirements:
```pip3 install -r requirements.txt```

## Set Environment Variables

RAG requires the following environment variables to be set ahead of running:

- ```KUBECONFIG```: Path to rancher kubeconfig file
- ```RANCHER_SERVER_URL```: URL of the rancher server
- ```RANCHER_TOKEN_KEY```: Bearer token key for rancher UI (the user must be authorized to list details of all managedd clusters in Rancher.)

## Run

simply run ```python3 rag.py```
The output will be displayed as follows:

```Listing nodes with their IPs:```
```Node Name: rmsmig1```
```IP: 172.16.56.231```
```Node Name: rmsmig2```
```IP: 172.16.56.232```
```Node Name: rmsmig3```
```IP: 172.16.56.233```
```Cluster Name: fwutil```
```Node Name: fwutil-srv-2c4513c3-xwkqk, Node IP: 172.16.56.77```
```Node Name: fwutil-agnt-2df2ff2c-nh8nc, Node IP: 172.16.56.50```
```Node Name: fwutil-agnt-2df2ff2c-5tcdv, Node IP: 172.16.56.78```
```Node Name: fwutil-agnt-2df2ff2c-rg2s9, Node IP: 172.16.56.30```
```Cluster Name: local```
```Node Name: rmsmig3, Node IP: 172.16.56.233```
```Node Name: rmsmig1, Node IP: 172.16.56.231```
```Node Name: rmsmig2, Node IP: 172.16.56.232```