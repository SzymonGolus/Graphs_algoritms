E = {
    'RS': {'M': 1.5, 'T': 1.0, 'U': 9.0},
    'M': {'U': 1.5},
    'T': {'S': 1.0},
    'S': {'U': 1.0}
    }

my_route = ['RS', 'T', 'S', 'U']

sum = 0
start = my_route[0]

for destination in my_route[1:]:
    sum += E[start][destination]
    start = destination

print(sum)
print(3*sum)
print(E['RS']['U'])