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
	for item in items:
		filename = base_path+str(item[csv_structure["label"]])+".md"
		markd = Markdown()
		# Metadata
		markd.add_text("---")
		markd.add_text(page_structure["metadata"][1]+item[csv_structure["label"]])
		markd.add_text("---")
		# Description
		markd.add_header(page_structure["headings"][0]["label"],page_structure["headings"][0]["depth"])
		markd.add_text(item[csv_structure["description"]])
		markd.add_header(page_structure["headings"][1]["label"],page_structure["headings"][1]["depth"])
		markd.add_header(page_structure["headings"][2]["label"],page_structure["headings"][2]["depth"])
		# add iframe path
		markd.add_text("""<iframe src="https://nicholascorniaorpheus.github.io/decastrophizing-failure-through-playfulness/assets/networks/"""+str(item[csv_structure["label"]])+""".html" height="400" width="400"></iframe>""")
		markd.add_header(page_structure["headings"][3]["label"],page_structure["headings"][3]["depth"])
		# add dice roller
		markd.add_text("""<iframe src="https://nicholascorniaorpheus.github.io/decastrophizing-failure-through-playfulness/assets/roll.html" height="300" width="400" title="Dice Roller"></iframe>""")
		markd.add_header(page_structure["headings"][4]["label"],page_structure["headings"][4]["depth"])
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
	"layout: page",
	"title:",
	"categories:", 
	"tags:" 
	],
	"headings": [
	{"label": "Description","depth": 1},
	{"label": "Statements","depth": 1},
	{"label": "Knowledge Graph","depth": 1},
	{"label": "Dice Roller","depth": 2},
	{"label": "References","depth": 1}

	]
}

generate_markdown_pages(items["items"],csv_structure,page_structure)

