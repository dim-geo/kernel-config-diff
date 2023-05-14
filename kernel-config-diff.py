#!/usr/bin/env python3

from anytree import Node, RenderTree,AbstractStyle,findall_by_attr
import sys,re

def generate_tree(filename):
    top=mother=Node(filename)
    dataset=set()
    with open(filename,"r") as file1:
        for line in file1:
            if (m := re.match(r"^((?!CONFIG_).)*$",line)):
                if m.group(0) != m.group(1) and m.group(0)!="":
                    category=m.group(0).strip('#').strip()
                    #print(category,mother.name)
                    if "end of" in category:
                      while True:
                        if "end of "+ mother.name == category:
                            mother=mother.parent
                            break
                        else:
                            mother=mother.parent
                    else:
                        mother=Node(category,parent=mother)
            elif (m := re.match(r"^.*(CONFIG_[^=\s]+).(.+)$",line)):
                key=m.group(1)
                value=m.group(2)
                dataset.add((key,value))
                new_node=Node(key,parent=mother,value=value)
    return top,dataset

def delete_node(key,tree):
    nodes=findall_by_attr(tree,key)
    for node in nodes:
        node.parent=None

def write_tree_to_file(myfile,tree):
 style=AbstractStyle("|  ","|- ","+- ")
 with open(myfile,'w') as f:
  for pre, fill, node in RenderTree(tree,style=style):
    try:
        print("%s%s:%s" % (pre, node.name,node.__dict__['value']),file=f)
    except:
        print("%s%s" % (pre, node.name),file=f)

tree1,dataset1=generate_tree(sys.argv[1])
tree2,dataset2=generate_tree(sys.argv[2])
common_dataset=dataset1 & dataset2
#print(common_dataset)
for item in common_dataset:
    key,_=item
    delete_node(key,tree1)
    delete_node(key,tree2)
write_tree_to_file(sys.argv[3],tree1)
write_tree_to_file(sys.argv[4],tree2)
