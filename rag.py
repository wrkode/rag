import os
from kubernetes import client, config
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
import warnings
from prettytable import PrettyTable
from termcolor import colored

# Suppress only the single warning from urllib3 needed.
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

def main():
    # Kubernetes API client
    config.load_kube_config(os.getenv('KUBECONFIG'))

    v1 = client.CoreV1Api()

    print("Listing nodes with their IPs:")
    nodes = v1.list_node()
    for node in nodes.items:
        print("Node Name: %s" % node.metadata.name)
        for address in node.status.addresses:
            if address.type == 'InternalIP' or address.type == 'ExternalIP':
                print("IP: %s" % address.address)


    # Rancher API client
    rancher_server_url = os.getenv('RANCHER_SERVER_URL')
    rancher_token_key = os.getenv('RANCHER_TOKEN_KEY')
    
    headers = {
        'Authorization': 'Bearer ' + rancher_token_key,
        'Content-Type': 'application/json',
    }

    # Get clusters
    response = requests.get(rancher_server_url + '/v3/clusters', headers=headers, verify=False)
    clusters = json.loads(response.text)['data']
    
    # Loop over clusters
    for cluster in clusters:
        # Initialize table
        cluster_table = PrettyTable(['Node Name', 'Node IP'])
        print("Cluster Name: %s, Cluster ID: %s, Kubernetes Version: %s, Provider: %s" % 
          (colored(cluster['name'], 'red'), 
           colored(cluster['id'], 'green'), 
           colored(cluster['version']['gitVersion'], 'yellow'), 
           colored(cluster['provider'], 'blue')))

        # Get nodes for each cluster
        response = requests.get(rancher_server_url + '/v3/nodes', headers=headers, params={'clusterId': cluster['id']}, verify=False)
        nodes = json.loads(response.text)['data']
        
        # Loop over nodes and add them to table
        for node in nodes:
            cluster_table.add_row([node['hostname'], node['ipAddress']])

        # Print table
        print(cluster_table)

if __name__ == '__main__':
    main()