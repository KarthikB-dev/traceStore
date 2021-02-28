# traceStore

## What is traceStore?
traceStore is a  program that takes a user input(either an IP address or a domain name that will be resolved to an IP address) and then executes the [traceroute command](https://www.wikiwand.com/en/Traceroute). The output of this will be stored in two places. The first is a file called ```trace.txt```. The second is in ```traceInput.py```, where each hop is an object, and there
is a list of these hops. The location of each hop is stored in the ```hop_locations``` list. This includes information like latitude and longitude, city, country, and more. If a certain part of the location not be determined, the JSON object will simply have 'Not found' listed for the country.


## How do you use traceStore?
In your terminal, type:


```python3 traceInput.py```


Open ```trace.txt``` to find all the traceroute information. Information about each hop
is contained in the ```hop_list``` in ```traceInput.py```. Location information is found in
```hop_locations```.


MD5 hash value for ```traceInput.py```: ec81412758470026153974f21cd86949 


Note that no input validation has been implemented as of yet
for the domain name. If you enter an incorrect IP address or domain
name, the program will simply fail.

## What can we expect from traceStore in the future?
Support for more types of ```traceroute```
commands being executed, instead of just TCP or ICMP.
Essentially, the traceroute command accepts a variety of arguments,
and we will give support to more over time.
A GUI(likely using Tkinter will be added). This could be used
to specify the IP address/domain name, the type of packets, etc.
to make it possible to interact with this project without ever opening the command line

