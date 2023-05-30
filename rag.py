import os
from kubernetes import client, config
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
import warnings

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
        print("Cluster Name: %s" % cluster['name'])
        
        # Get nodes for each cluster
        response = requests.get(rancher_server_url + '/v3/nodes', headers=headers, params={'clusterId': cluster['id']}, verify=False)
        nodes = json.loads(response.text)['data']
        
        # Loop over nodes
        for node in nodes:
            print("Node Name: %s, Node IP: %s" % (node['hostname'], node['ipAddress']))

if __name__ == '__main__':
    main()
