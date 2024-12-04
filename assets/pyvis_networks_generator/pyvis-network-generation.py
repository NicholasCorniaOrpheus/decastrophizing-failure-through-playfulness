from pyvis.network import Network
import networkx as nx
import json
import csv

def json2dict(fn):
	#Import json file
	with open(fn, 'r') as f:
		json_file = json.load(f)
		#print(json_file)
		return json_file


def ingest_nodes(dict_list,net):
	#this function creates a new node from a dictionary
	base_url = "https://nicholascorniaorpheus.github.io/decastrophizing-failure-through-playfulness/kg/"
	for item in dict_list:
		url = "<a href=\'"+base_url+str(item["id"])+"""'>"""+str(item["label"])+"</a>"

		net.add_node(item["id"],
			label = item["label"],
			color= '#f8f7f4',
			value= 10,
			title="<body>"+url+" </body>"

			)
	return net


def ingest_edges(dict_list,net):
	for item in dict_list:
		links = item["related_concepts_id"].split("|")
		for link in links:
			pos = dict_list.index(next(filter(lambda x: x.get('id') == link,dict_list )))
			result = dict_list[pos]["id"]
			if (item["id"],result) in net.edges():
				pass
			else:
				net.add_edge(item["id"],result, weight =10)

def pyvis_visualization(net,path):
	layout = nx.spring_layout(net)
	visualization=Network(height="400px", width="400px", bgcolor="#1C1A19", font_color="#f8f7f4", directed=False,select_menu=False,filter_menu=False,notebook=False)
	visualization.from_nx(net)
	#visualization.toggle_physics(False)
	#visualization.show_buttons(filter_=['nodes','physics'])
	for i in visualization.nodes:
			node_id = i["id"]
			if node_id in layout:
				i["x"], i["y"] = layout[node_id][0]*1000, layout[node_id][1]*1000
	options = """
			var options = {
   					"configure": {
						"enabled": false
   							},
  					"edges": {
					"color": {
	  				"inherit": true
						},
					"smooth": false
  					},
  					"physics": {
					"barnesHut": {
	  				"gravitationalConstant": -12050
					},
					"minVelocity": 0.75
  					}
					}
				"""
	visualization.set_options(options)
	#visualization.show('example.html',notebook=False)
	#visualization.write_html(name='example.html',notebook=False,open_browser=False)
	visualization.save_graph(path+".html")

def csv2dictionary_list(csv_filename):
	f = open(csv_filename,'r')
	reader = csv.DictReader(f)
	d = {"items": []}
	for row in reader:
		d["items"].append(row)
	return d

# INPUTS

date = "2024-12-03"
input_csv_filename = "../pages_generator/DFTP-"+date+".csv"
input_network = csv2dictionary_list(input_csv_filename)
full_graph_filename = "MONADS_network.json"
full_graph_file = open(full_graph_filename,'w')

net = nx.Graph()
ingest_nodes(input_network["items"],net)
ingest_edges(input_network["items"],net)


# Save graph in JSON format
full_graph = nx.node_link_data(net)
full_graph_file = open(full_graph_filename,'w')
json.dump(full_graph,full_graph_file, indent=2)

# Generate subnetworks and visualizations
def generate_distance_matrix(net,max_dist):
	print("Distance matrix operations...")
	distances = dict(nx.all_pairs_shortest_path_length(net,cutoff=max_dist))
	return distances

def pyvis_visualization_local(center_node,net,distances,base_path):
	sub_net_nodes = []
	print("Generating subgraph...")
	# reduce big subgraphs!
	if len(distances[center_node]) < 10:
		#normal generation
		for node in distances[center_node]:
			sub_net_nodes.append(node)
	else:
		#reduced generation
		print("Reduced version of the network...")
		treshold = 1
		for node in distances[center_node]:
			if distances[center_node][node] <= treshold:
				sub_net_nodes.append(node)

	sub_net = net.subgraph(sub_net_nodes)
	print("Render visualization...")
	pyvis_visualization(sub_net,base_path+str(center_node))





print("Generating distance matrix...")
distances = generate_distance_matrix(net,2)

base_path = "../networks/"

for node in net.nodes():
	pyvis_visualization_local(node,net,distances,base_path)

