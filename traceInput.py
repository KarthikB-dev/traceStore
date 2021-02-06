import os
import subprocess
import re
import requests

domain = input("What's the domain? ")

#TCP scans will be implemented later on
'''
tcp = input("Would you like to conduct a TCP based traceroute? y for yes, n for no")
while tcp != 'y' and tcp != 'n':
    tcp = input("Please enter a valid answer. y for yes, n for no"
'''

#setting a maximum number of hops
diff_num_hops = input("Would you like a number of hops different than the default of 30? y for yes, n for no. ")
while diff_num_hops != 'y' and diff_num_hops != 'n':
    diff_num_hops = input("Please enter a valid answer. y for yes, n for no. ")
max_hops = ""
if diff_num_hops == 'y':
    max_hops = input("How many hops would you like to have? Pick a number between 0 and 255. ")
    while (not max_hops.isnumeric()) or int(max_hops) > 255:
        max_hops = input("Enter a number between 0 and 255. ")
    max_hops = "-m " + max_hops + " "
#performing the traceroute command
traceroute_command = "traceroute " +  max_hops + domain + " > trace.txt"
os.system(traceroute_command)

#defining the hop class that stores information about each hop
class hop:
    def __init__(self, full_name, index, IPs):
        self.full_name = full_name
        self.index = index
        self.IPs = IPs
    #there are no mutators for the hop class since information 
    #about each hop should not be modified
    
    #functions to retrieve information about each curr_hop
    def get_index(self):
        return self.index
    def get_IPs(self):
        return self.IPs
    def get_full_name(self):
        return self.full_name
    #tostring
    def __str__(self):
        out_str = "all info: " + self.get_full_name() + '\n'
        out_str += "index: " + self.get_index() + '\n'
        out_str += "IP addresses:" + str(self.get_IPs()) + '\n'
        return out_str
        
#start reading from the file
trace_file = open("trace.txt")
traceroute_info = trace_file.readline()
print("Traceroute info:", traceroute_info)

hop_list = []
curr_hop = trace_file.readline()

def getIPs(hop):
    #IPs stores all IP addresses within a hop, and removes duplicates
    IPs = set(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", hop))
    if len(IPs) == 0:
        return None
    return IPs

def extract_index(hop):
    if hop[0] != ' ':
        return hop[0:2]
    return hop[1]

while curr_hop:
    curr_hop = curr_hop.rstrip('\n')
    #uses the information in curr_hop to create a new hop object
    hop_obj = hop(curr_hop, extract_index(curr_hop), getIPs(curr_hop))
    #add this new hop object to the list of hop objects, hop_list
    hop_list.append(hop_obj)
    curr_hop = trace_file.readline()

#display the information about each hop
for hop in hop_list:
    print(hop)

#perform geolocation on the IP addresses of all hops
hop_locations = []
#stores information about each IP address in a JSON object
for hop in hop_list:
    currLocs = []
    IPs = hop.get_IPs()
    if IPs:
        for IP in IPs:
            url = 'https://geolocation-db.com/json/' + IP + '&position=true'
            currLocs.append(requests.get(url).json())
    hop_locations.append(currLocs)
#printing out the contents of all the JSON objects that store locations
print(hop_locations)