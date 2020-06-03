import os
import re
import pprint
from jinja2 import Template



root_path = r"C:\Junaid\Work\GitHubLocal\NetBrain_Automation_Customization"
dir_ignore_list = [ ".git", "info", "logs", "objects", "refs"]
root_readme_template = """

# NetBrain Custom Repository
This repository contains the most common use cases and best practices in NetBrain.

## Resource Category by Network Features:

{% for feature in features %}
* [{{feature.name|upper}}]({{feature.name|replace(' ','%20')}}/) ({{feature.count}})
{%- endfor %}

"""

dir_tree = []


root_dir_list = os.listdir(root_path)
for root_dir in root_dir_list:
  root_dir_path = f"{root_path}/{root_dir}"
  if root_dir not in dir_ignore_list and os.path.isdir(root_dir_path):
    dir_tree_item = {}
    dir_tree_item['name']=root_dir
    dir_tree_item['count']=0
    dir_tree_item['list']=[]
    sub_dir_list = os.listdir(root_dir_path)
    for sub_dir in sub_dir_list:
      sub_dir_path = f"{root_dir_path}/{sub_dir}"
      if sub_dir not in dir_ignore_list and os.path.isdir(sub_dir_path):
        dir_tree_item['count'] += 1
        dir_tree_item['list'].append(sub_dir)
    dir_tree.append(dir_tree_item)

    
    
#print (dir_tree)

readme_template = Template(root_readme_template)
readme_txt = readme_template.render(features=dir_tree)
print (readme_txt)


with open('_README.MD','w') as f_readme:
  f_readme.write(readme_txt)