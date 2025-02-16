from flask import Flask, json, request, send_from_directory, jsonify

app = Flask(__name__, static_folder='static')

data = None
with open('map.json', 'r') as f:
    map_data = f.read()
    data = json.loads(map_data)

# Hardcoded locations data
locations = [
    {"id": 1, "name": "New York", "lat": 40.7128, "lng": -74.0060},
    {"id": 2, "name": "Los Angeles", "lat": 34.0522, "lng": -118.2437},
    {"id": 3, "name": "Chicago", "lat": 41.8781, "lng": -87.6298},
    {"id": 4, "name": "Miami", "lat": 25.7617, "lng": -80.1918}
]

# calculate best route according to djikstra algorithm
def calculate_route(data, from_id, to_id):
    nodes = data['nodes']
    edges = data['edges']
    graph = {}
    for edge in edges:
        u = edge['source']
        v = edge['target']
        w = edge['distance']
        
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w
        if v not in graph:
            graph[v] = {}
        graph[v][u] = w
    
    dist = {node: float('inf') for node in nodes}
    dist[from_id] = 0
    prev = {node: None for node in nodes}
    q = set(nodes)
    while q:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)
        if u == to_id:
            break
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    route = []
    u = to_id
    while prev[u] is not None:
        route.append(u)
        u = prev[u]
    route.append(from_id)
    route.reverse()
    return route


@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/locations')
def get_locations():
    locations = []
    for node in data['nodes'].values():
        name = node['name']
        if name is None or name == 'null':
            continue
        locations.append({
            'id': node['id'],
            'name': node['name'],
            'lat': node['lat'],
            'lon': node['lon']
        })
    
    return jsonify(locations)

@app.route('/api/route')
def get_route():
    from_id = int(request.args.get('from'))
    to_id = int(request.args.get('to'))
    route = calculate_route(data, from_id, to_id)
    return jsonify(route)





if __name__ == '__main__':
    app.run(debug=True)
