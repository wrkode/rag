import os
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
from termcolor import colored
import warnings
from prettytable import PrettyTable

# Suppress only the single warning from urllib3 needed.
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

def main():

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
        
        kubernetes_version = cluster['version']['gitVersion'] if 'version' in cluster and 'gitVersion' in cluster['version'] else 'N/A'
        
        print("Cluster Name: %s, Cluster ID: %s, Kubernetes Version: %s, Provider: %s, State: %s" % 
              (colored(cluster['name'], 'red'), 
               colored(cluster['id'], 'green'), 
               colored(kubernetes_version, 'yellow'), 
               colored(cluster['provider'], 'blue'),
               colored(cluster['state'], 'magenta')))

        # Get nodes for each cluster if it is in active state
        if cluster['state'] == 'active':
            response = requests.get(rancher_server_url + '/v3/nodes', headers=headers, params={'clusterId': cluster['id']}, verify=False)
            nodes = json.loads(response.text)['data']
            
            # Loop over nodes and add them to table
            for node in nodes:
                cluster_table.add_row([node['hostname'], node['ipAddress']])

        # Print table
        print(cluster_table)

if __name__ == '__main__':
    main()
