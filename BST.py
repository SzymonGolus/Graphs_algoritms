class City:

    def __init__(self, id, country, population) -> None:
        self.id = id 
        self.country = country
        self.population = population
        self.left = None
        self.right = None
        self.depth = None
    
    def __repr__(self) -> str:
        return f"<{self.id}/{self.depth}>"

def insert(parent, child, depth=0):
    if parent is None:
        child.depth = depth
        return child
    elif parent.id == child.id:
        return parent
    elif child.id > parent.id:
        parent.right = insert(parent.right, child, parent.depth+1)
    else:
        parent.left = insert(parent.left, child, parent.depth+1)
    return parent

def build_bst(nodes_list, first_id, last_id, depth=0):
    if first_id > last_id:
        return None
    middle_id = (first_id + last_id) // 2
    middle_node = nodes_list[middle_id]
    middle_node.left = build_bst(nodes_list, first_id, middle_id -1, depth+1)
    middle_node.right = build_bst(nodes_list, middle_id+1, last_id, depth+1)
    middle_node.depth = depth

    return middle_node

def rebuilt_bst(bst):
    nodes_list = []
    get_ordered_list(bst, nodes_list)
    first_id = 0
    last_id = len(nodes_list) - 1

    return build_bst(nodes_list, first_id, last_id)

def load_file(file_name):
    bst = None
    with open(file_name, 'r', encoding='utf-8') as file:
        line = file.readline()
        line_number = 0

        while True:
            line = file.readline()
            if not line:
                break
            data = line.split(",")
            line_number +=1
            city_ascii = data[1].replace("'","").replace('"','').replace('`','').upper()
            city_ascii = city_ascii[1:] if city_ascii[0] == " " else city_ascii
            country = data[4].replace("'","").replace('"','').replace('`','').upper()
            try:
                population = int(data[9].replace('"',''))
            except ValueError:
                population = -1
            node = City(city_ascii, country, population)
            #print(line_number, city_ascii)
            bst = insert(bst,node)
        return bst

def max_depth(node):
    if node is None:
        return 0
    else:
        right_depth = max_depth(node.right) + 1
        left_depth = max_depth(node.left) + 1
        return max(right_depth, left_depth)

def count(node):
    if node is None:
        return 0
    else:
        count_left = count(node.left)
        count_right = count(node.right)
        return count_left + count_right + 1

def get_ordered_list(parent, nodes_list):
    if not parent:
        return
    get_ordered_list(parent.left, nodes_list)
    nodes_list.append(parent)
    get_ordered_list(parent.right, nodes_list)


file_name = 'worldcities.csv'
bst = load_file(file_name)

print(max_depth(bst), max_depth(bst.left), max_depth(bst.right))

print(count(bst), count(bst.left), count(bst.right))

sorted_list = []
get_ordered_list(bst, sorted_list)
print(sorted_list[:10])
print(sorted_list[-10:])

bst = rebuilt_bst(bst)

print(max_depth(bst), max_depth(bst.left), max_depth(bst.right))

print(count(bst), count(bst.left), count(bst.right))