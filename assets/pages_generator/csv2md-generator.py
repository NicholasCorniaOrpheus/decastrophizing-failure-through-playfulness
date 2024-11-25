from markd import Markdown
import csv

# This script generates a predefined Markdown page, given metadata coming from a csv file

def csv2dictionary_list(csv_filename):
	f = open(csv_filename,'r')
	reader = csv.DictReader(f)
	d = {"items": []}
	for row in reader:
		d["items"].append(row)
	return d

def generate_markdown_pages(items,csv_structure,page_structure):
	base_path = "./kg/"
	base_url_wikidata = "https://www.wikidata.org/wiki/"
	for item in items:
		filename = base_path+str(item[csv_structure["id"]])+".md"
		markd = Markdown()
		# Metadata
		markd.add_text("---")
		markd.add_text(page_structure["metadata"][0]+item[csv_structure["label"]])
		markd.add_text("---")
		# Title
		markd.add_header(item[csv_structure["label"]],page_structure["headings"][0]["depth"])
		# Description
		markd.add_header(page_structure["headings"][1]["label"],page_structure["headings"][1]["depth"])
		markd.add_text(item[csv_structure["description"]])
		# Identifiers
		markd.add_header(page_structure["headings"][2]["label"],page_structure["headings"][2]["depth"])
		if item[csv_structure["qid"]] != "":
			markd.add_list_item("Wikidata: ["+item[csv_structure["qid"]]+"]("+base_url_wikidata+item[csv_structure["qid"]]+")")
		# Statements
		markd.add_header(page_structure["headings"][3]["label"],page_structure["headings"][3]["depth"])
		# Knowledge Graph
		markd.add_header(page_structure["headings"][4]["label"],page_structure["headings"][4]["depth"])
		markd.add_text("""<iframe src="https://nicholascorniaorpheus.github.io/decastrophizing-failure-through-playfulness/assets/networks/"""+str(item[csv_structure["label"]])+""".html" height="400" width="400"></iframe>""")
		# Dice roller
		markd.add_header(page_structure["headings"][5]["label"],page_structure["headings"][5]["depth"])
		markd.add_text("""<iframe src="https://nicholascorniaorpheus.github.io/decastrophizing-failure-through-playfulness/assets/roll.html" height="300" width="400" title="Dice Roller"></iframe>""")
		# References
		markd.add_header(page_structure["headings"][6]["label"],page_structure["headings"][6]["depth"])
		# Help
		markd.add_header(page_structure["headings"][7]["label"],page_structure["headings"][7]["depth"])
		markd.add_text("If you have forgotten some aspect of the game's rules, please visit agin the [Rules](../game-rules.md) page.")
		markd.save(filename)
		break




# import data
print("Current date csv file: ")
date = input()
csv_filename = "DFTP-"+date+".csv"
items = csv2dictionary_list(csv_filename)

csv_structure = {
	"id": "id",
	"label": "label",
	"description": "description",
	"qid": "qid",
	"wd_description": "wd_description"
}

page_structure = {
	"metadata": [
	"title: ",
	"categories: ", 
	"tags: " 
	],
	"headings": [
	{"label": "", "depth":1},
	{"label": "Description","depth": 2},
	{"label": "Identifiers","depth": 2},
	{"label": "Statements","depth": 2},
	{"label": "Knowledge Graph","depth": 2},
	{"label": "Dice Roller","depth": 2},
	{"label": "References","depth": 2},
	{"label": "Help","depth": 2}


	]
}

generate_markdown_pages(items["items"],csv_structure,page_structure)

