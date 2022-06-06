E ={
    'Staromestska': {'Mustek'},
    'Mustek': {'Staromestska', 'Muzeum', 'Namesti Republiky', 'Narodni trida'},
    'Narodni trida': {'Mustek'},
    'Namesti Republiky': {'Mustek', 'Florenc'},
    'Florenc': {'Namesti Republiky', 'Hlavni nadrazi'},
    'Hlavni nadrazi': {'Florenc', 'Muzeum'},
    'Muzeum': {'Mustek', 'Hlavni nadrazi'}
}

def if_adjacent(station1, station2, E):
    if station1 in E[station2]: 
        print('Yes') 
    else: 
        print('No')

if_adjacent('Muzeum', 'Staromestska', E)
if_adjacent('Hlavni nadrazi', 'Florenc', E)