import json
import ipaddress

def get_properties(inputs):
    inputs = inputs.get("endpoint", inputs)
    properties_list = inputs["endpointProperties"].get("properties", [])
    properties_list = json.loads(properties_list)
    properties = {}
    for prop in properties_list:
        properties[prop["prop_key"]] = prop["prop_value"]

    return properties

def get_first_ip(cidr):
    n = ipaddress.IPv4Network(cidr)
    return str(n[0])

def get_last_ip(cidr):
    n = ipaddress.IPv4Network(cidr)
    return str(n[-1])

def get_gateway(cidr):
    n = ipaddress.IPv4Network(cidr)
    return str(n[1])

def get_prefix(cidr):
    n = ipaddress.IPv4Network(cidr)
    return str(n.prefixlen)

#Input a dict passed in that is the network range representation from OpUtils
#Output a dict representing what VRA expects of a newtork range representation
def oputils_range_to_vra(inrange):
    outrange = {  
             #"id": inrange['subnetid'],
             "id": get_first_ip(inrange['subnet-address-cidr']),
             "name": inrange['subnet-name'],
             "startIPAddress": get_first_ip(inrange['subnet-address-cidr']),
             "endIPAddress": get_last_ip(inrange['subnet-address-cidr']),
             "description": inrange['subnet-description'],
             "ipVersion": "IPv4",
             "addressSpaceId": "default",
             "subnetPrefixLength": get_prefix(inrange['subnet-address-cidr']),
             "gatewayAddress": get_gateway(inrange['subnet-address-cidr']),
             "domain": "nypd.finest"
        }
    return outrange
    
    