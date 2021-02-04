import os
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

hops = []
hop = trace_file.readline()
while hop:
    hop = hop.rstrip('\n')
    print("Hop:", hop)
    hops.append(hop)
    hop = trace_file.readline()



