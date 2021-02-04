import os
import re
"""
input_script_path = "/home/impacable/Documents/traceStore/domain_input.sh"
inputCommand = "sh " + input_script_path
runDomainInput = os.system(inputCommand)
runDomainInput
"""
#start reading from the file
trace_file = open("trace.txt")
destination_info = trace_file.readline()
print("Desination info:", destination_info)

curr_hops = []
curr_hop = trace_file.readline()

class hop:
    index = 0
    IPs = set()
    full_name = ""
    def __init__(self, index, IPs, full_name):
        self.index = index
        self.IPs = IPs
        self.full_name = full_name
    #functions to retrieve information about each curr_hop

def getIPs(hop):
    return set(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", hop))

while curr_hop:
    curr_hop = curr_hop.rstrip('\n')
    print("curr_Hop:", curr_hop)
    curr_hops.append(curr_hop)
    print("IP address:", getIPs(curr_hop))
    curr_hop = trace_file.readline()




