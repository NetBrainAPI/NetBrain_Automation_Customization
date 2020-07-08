import requests
import json
import csv
import networkx as nx
import sys

######### MAIN ###########
csvfile = open('nb_topo.csv', 'r')
# resultFileHandle = open('debug_island.json', 'w')

fieldnames = ("dev_type_site","ipv4_nbr1","ipv4_nbr2","ipv4_nbr3","l2_nbr","vpn_nbr")
reader = csv.DictReader(csvfile, fieldnames)

retDic = {}
bSkip = True
for row in reader:
    if bSkip:
        bSkip = False
        continue
    
    try:
        retVal1 = eval(row["ipv4_nbr1"].strip("=").strip('"'))
        if not isinstance(retVal1, list):
            print("Not a list.", row["dev_type_site"])
            continue
        
        retVal2 = eval(row["ipv4_nbr2"].strip("=").strip('"'))
        if not isinstance(retVal2, list):
            print("Not a list.", row["dev_type_site"])
            continue

        retVal3 = eval(row["ipv4_nbr3"].strip("=").strip('"'))
        if not isinstance(retVal3, list):
            print("Not a list.", row["dev_type_site"])
            continue

        retVal4 = eval(row["l2_nbr"].strip("=").strip('"'))
        if not isinstance(retVal4, list):
            print("Not a list.", row["dev_type_site"])
            continue

        retVal5 = eval(row["vpn_nbr"].strip("=").strip('"'))
        if not isinstance(retVal5, list):
            print("Not a list.", row["dev_type_site"])
            continue

        retDic[row["dev_type_site"]] = retVal1 + retVal2 + retVal3 + retVal4 + retVal5
    except:
        print("Single cell read error.", row["dev_type_site"])

print(retDic)
# resultFileHandle.write(json.dumps(retDic))
# resultFileHandle.close()

dataInput = retDic
g_mapTable  = []
result = {}
# Map DeviceName to Index
def GetDevId(devName):
    if devName in g_mapTable:
        return g_mapTable.index(devName)

    g_mapTable.append(devName)
    return len(g_mapTable) - 1

def GetDevNameById(devId):
    return g_mapTable[devId]

def Subgraph(data):
    G = nx.Graph(data)
    i = 1
    for c in sorted(nx.connected_components(G), key=len, reverse=False):
        nodeSet = G.subgraph(c).nodes()
        list = []
        for node in nodeSet:
            list.append(GetDevNameById(node))
        result[i]=list
        i += 1
    return result

graph_data = {}
for devName in dataInput:
    devId = GetDevId(devName)
    nbrDevs = dataInput[devName]
    if len(nbrDevs) <= 0:
        graph_data[devId] = []
    else:
        for nbrDev in nbrDevs:
            if devId not in graph_data:
                graph_data[devId] = []
            graph_data[devId].append(GetDevId(nbrDev))

island_result = Subgraph(graph_data)
with open('island_result.json', 'w') as json_file:
    print(json.dumps(island_result, sort_keys=True, indent=4), file=json_file)

with open('island_result.json') as inputFile:
   input_data = json.load(inputFile)

l = []
for i in input_data:
   for j in input_data[i]:
      d = {}
      d["island#"]=i
      d["device"]=j
      l.append(d)
print(l)

with open("island_result.csv", "w", newline='') as outfile:
   f2 = csv.writer(outfile)
   f2.writerow(l[0].keys())
   for i in l:
      f2.writerow([i["island#"],i["device"]])