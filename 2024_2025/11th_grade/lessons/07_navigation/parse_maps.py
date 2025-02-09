import xml.etree.ElementTree as ET
import json
from math import radians, sin, cos, sqrt, atan2

# get distance between two points using herveisne formula
def haversine(lat1, lon1, lat2, lon2):
    
    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c * 1000 # in meters

def parse_xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {
        "nodes": {},
        "edges": []
    }

    # Extract nodes
    for node in root.findall("node"):
        node_data = {
            "id": node.get("id"),
            "lat": node.get("lat"),
            "lon": node.get("lon"),
            "name": node.find("tag[@k='name:he']").get("v") if node.find("tag[@k='name:he']") is not None else None
        }
        data["nodes"][node_data["id"]] = node_data

    # Extract ways
    for way in root.findall("way"):
        drivable_roads = ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential", "service",
                          "living_street"]
        if way.find("tag[@k='highway']") is None or not way.find("tag[@k='highway']").get("v") in drivable_roads:
            continue

        prev_node = None
        for node in way.findall("nd"):
            if prev_node is None:
                prev_node = node
                continue

            prev_id = prev_node.get("ref")
            node_id = node.get("ref")
           
            edge_data = {
                "source": prev_id,
                "target": node_id,
                "distance": haversine(float(data["nodes"][prev_id]["lat"]), float(data["nodes"][prev_id]["lon"]),
                                    float(data["nodes"][node_id]["lat"]), float(data["nodes"][node_id]["lon"]))
            }

            data["edges"].append(edge_data)
            prev_node = node
       
    # Save as JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Example usage
parse_xml_to_json("map.osm", "map.json")
