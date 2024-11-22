from pyvis.network import Network
import networkx as nx
import json

def json2dict(fn):
	#Import json file
	with open(fn, 'r') as f:
		json_file = json.load(f)
		#print(json_file)
		return json_file

def test():
	net = nx.Graph()

	net.add_node("I am a node with a link", title="<a href=\'http://www.google.com\'>google</a>")

	net.add_node('? akk in maat? [hoeveel accoorden in een maat?]',
		label = '? akk in maat? [hoeveel accoorden in een maat?]',
		color= "#c14834",
		value=10,
		title="""
		<body>
		<a href=\'https://koha.orpheusinstituut.be/cgi-bin/koha/authorities/detail.pl?authid=27669'>? akk in maat? [hoeveel accoorden in een maat?]</a>
		</body>
		"""
	)
	return net

def ingest_nodes(dict_list,net):
	#this function creates a new node from a dictionary
	for item in dict_list:
		url = "<a href=\'"+item["base_url"]+str(item["id"])+"""'>"""+str(item["label"])+"</a>"

		net.add_node(item["id"],
			label = item["label"],
			color= item["color"],
			value=item["value"],
			title="<body>"+url+" </body>"

			)
	return net


def ingest_edges(dict_list,net):
	for item in dict_list:
		for link in item["links_ids"]:
			pos = dict_list.index(next(filter(lambda x: x.get('id') == link,dict_list )))
			result = dict_list[pos]["id"]
			net.add_edge(item["id"],result, weight =10)

def pyvis_visualization(net):
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
	visualization.show('example.html',notebook=False)
	#visualization.write_html(name='example.html',notebook=False,open_browser=False)
	visualization.save_graph("example.html")
# INPUTS

input_json_filename = "input_test.json"
input_json = json2dict(input_json_filename)
full_graph_filename = "network.json"
full_graph_file = open(full_graph_filename,'w')

net = nx.Graph()
ingest_nodes(input_json["items"],net)
ingest_edges(input_json["items"],net)


# Save graph in JSON format
full_graph = nx.node_link_data(net)
full_graph_file = open(full_graph_filename,'w')
json.dump(full_graph,full_graph_file, indent=2)

pyvis_visualization(net)



