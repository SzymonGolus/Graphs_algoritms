graph = {
    'Ciudad Polacca': {'Santo Subito': 15, 'Senderos': 10},
    'Senderos': {'Dos Rios': 20},
    'Santo Subito': {'Dos Rios': 5, 'Al Pacino': 50},
    'Dos Rios': {'Frontera': 20, 'Arboleda': 5},
    'Frontera': {'Al Pacino': 10},
    'Arboleda': {'Al Pacino': 10},
    'Al Pacino': {}
}

def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None

    for name, cost in costs_dict.items():
        if name not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name

    return cheapest_key

costs={}
parents={}

for name in graph.keys():
    costs[name] = float('inf')

processed = []

current_node = 'Ciudad Polacca'
costs[current_node] = 0
parents[current_node] = None

while current_node:
    for neighbour in graph[current_node]:
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node

    processed.append(current_node)
    current_node = get_cheapest_node(costs, processed)

for d,c in costs.items():
    print(f'The cost for {d} is {c}')

    current_d = d
    while parents[current_d]:
        print(current_d)
        current_d = parents[current_d]
    else:
        print(current_d)