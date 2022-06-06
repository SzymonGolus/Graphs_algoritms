from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA


V = ['Princess', 'Dwarfs', 'Queen', 'King', 'Hunter']
E = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [2, 3],
    [2, 4],
    [3, 4],
]

def who_knows_person(person, E, V):
    friends=[]
    for p1, p2 in E:
        if V[p1] == person:
            friends.append(V[p2])
        elif V[p2] == person:
            friends.append(V[p1])
    return friends

print(who_knows_person('Princess', E, V))