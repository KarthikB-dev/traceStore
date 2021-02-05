# traceStore

# What is traceStore?
traceStore is a  program that takes a user input(either an IP address or a domain name that will be resolved to an IP address) and then executes the traceroute command. The output of this will be stored in two places. The first is a file called ```trace.txt```. The second is in traceInput.py, where each hop is an object, and there
is a list of these hops.

# How do you use traceStore?
Change the path ```input_script_path``` in the traceInput.py file so that it matches the file path on your computer. Then, in your terminal, type:


```python3 traceInput.py```


Open ```trace.txt``` to find all the traceroute information. Information about each hop
is contained in the ```hop_list``` in traceInput.py.


Note that no input validation has been implemented as of yet
for the domain name. If you enter an incorrect IP address or domain
name, the program will simply fail.