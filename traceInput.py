import os
import re

#replace input_script_path with the path to the shell script on your machine
input_script_path = "/home/impacable/Documents/traceStore/domain_input.sh"
inputCommand = "sh " + input_script_path
runDomainInput = os.system(inputCommand)
runDomainInput

#start reading from the file
trace_file = open("trace.txt")
traceroute_info = trace_file.readline()
print("Traceroute info:", traceroute_info)

hop_list = []
curr_hop = trace_file.readline()

class hop:
    index = 0
    IPs = set()
    full_name = ""
    def __init__(self, full_name, index, IPs):
        self.full_name = full_name
        self.index = index
        self.IPs = IPs
    #functions to retrieve information about each curr_hop
    def get_index(self):
        return self.index
    def get_IPs(self):
        return self.IPs
    def get_full_name(self):
        return self.full_name

def getIPs(hop):
    #IPs stores all IP addresses within a hop, and removes duplicates
    IPs = set(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", hop))
    if len(IPs) == 0:
        return None
    return IPs

while curr_hop:
    curr_hop = curr_hop.rstrip('\n')
    #uses the information in curr_hop to create a new hop object
    hop_obj = hop(curr_hop, curr_hop[0], getIPs(curr_hop))
    #add this new hop object to the list of hop objects, hop_list
    hop_list.append(hop_obj)
    curr_hop = trace_file.readline()