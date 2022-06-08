from email.errors import InvalidMultipartContentTransferEncodingDefect


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
    elif parent.id < child.id:
        parent.right = insert(parent.right, child, parent.depth+1)
    else:
        parent.left = insert(parent.left, child, parent.depth+1)
    return parent

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
            country = data[4].replace("'","").replace('"','').replace('`','').upper()
            try:
                population = int(data[9].replace('"',''))
            except ValueError:
                population = -1
            node = City(city_ascii, country, population)
            #print(line_number, city_ascii)
            bst = insert(bst,node)
        return bst

file_name = 'worldcities.csv'
bst = load_file(file_name)
print(bst)