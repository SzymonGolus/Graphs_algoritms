V = ['mouse', 'keyboard', 'computer', 'monitor', 'printer']
E = [{0,2}, {1,2}, {2,3}, {2,4}]

def translate_to_matrix(V, E):
    matrix=[]
    for v1 in range(len(V)):
        matrix.append([ 1 if {v1, v2} in E else 0 for v2 in range(len(V))])
    return matrix

my_matrix = translate_to_matrix(V, E)
for row in my_matrix:
    print(row)