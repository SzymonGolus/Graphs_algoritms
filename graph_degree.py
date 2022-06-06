E ={
    'Staromestska': {'Mustek'},
    'Mustek': {'Staromestska', 'Muzeum', 'Namesti Republiky', 'Narodni trida'},
    'Narodni trida': {'Mustek'},
    'Namesti Republiky': {'Mustek', 'Florenc'},
    'Florenc': {'Namesti Republiky', 'Hlavni nadrazi'},
    'Hlavni nadrazi': {'Florenc', 'Muzeum'},
    'Muzeum': {'Mustek', 'Hlavni nadrazi'}
}

graphDegree = max([len(E[start]) for start in E])
print(graphDegree)

for start in E:
    if len(E[start]) == graphDegree:
        print(start)
