#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

print(os.getcwd())
print(os.path.isfile("markdown_generator/pubs.bib"))

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "journal":{
        "file": "markdown_generator/pubs.bib",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                try:
                    # Handle cases where first_names or last_names might be empty
                    first_name = author.first_names[0] if author.first_names else ""
                    last_name = author.last_names[0] if author.last_names else ""
                    if first_name or last_name:
                        citation = citation + " " + first_name + " " + last_name + ","
                except IndexError:
                    # If we can't get the name, just continue to the next author
                    continue
            
            # Remove trailing comma and add space
            citation = citation.rstrip(",") + " "

            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            try:
                venue = publist[pubsource]["venue-pretext"]
                if publist[pubsource]["venuekey"] in b.keys():
                    venue += b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")
                else:
                    # If journal is not found, use publisher or default to "Preprint"
                    venue += b.get("publisher", "Preprint").replace("{", "").replace("}","").replace("\\","")
            except KeyError:
                venue = b.get("publisher", "Preprint").replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\n"
            md += f'title: "{html_escape(b["title"])}"\n'
            md += "collection: publications\n"
            
            # Create a simple slug from the title
            simple_slug = b["title"].split()[0].lower()
            md += f"permalink: /publication/{simple_slug}\n"
            
            # Add date
            md += f"date: {pub_date}\n"
            
            # Add venue
            md += f'venue: "{html_escape(venue)}"\n'
            
            # Format authors with your name in bold
            authors = ""
            for author in bibdata.entries[bib_id].persons["author"]:
                try:
                    name = str(author)
                    if "D'Ambrogio" in name:  # Highlight your name
                        authors += f"<b>{name}</b>, "
                    else:
                        authors += f"{name}, "
                except:
                    continue
            authors = authors.rstrip(", ")  # Remove trailing comma
            md += f'authors: "{authors}"\n'
            
            # Add paper URL if exists
            if "url" in b.keys():
                md += f'paperurl: "{b["url"]}"\n'
            
            md += "---\n"

            
            
            md_filename = os.path.basename(md_filename)

            output_dir = "_publications"  # Remove the "../" 
            
            # Create the full path and write the file
            output_path = os.path.join(output_dir, md_filename)
            with open(output_path, 'w', encoding="utf-8") as f:
                f.write(md)
            print(f'SUCCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
