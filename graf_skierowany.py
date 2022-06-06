V = ['Berlin', 'Paris', 'Rome', 'Madrid', 'Warsaw', 'Praque', 'Wien']
E = [
    ('Madrid', 'Paris'),
    ('Paris', 'Berlin'),
    ('Berlin', 'Warsaw'),
    ('Warsaw', 'Praque'),
    ('Praque','Wien'),
    ('Wien', 'Rome'),
    ('Berlin', 'Wien'),
    ('Rome', 'Praque'),
    ('Praque', 'Warsaw')
]
def where_to_go(city, E):
    print([y for (x,y) in E if x == city])
    
def where_from(city, E):
    print([x for (x,y) in E if y == city])
    

where_to_go("Berlin", E)
where_from('Warsaw', E)