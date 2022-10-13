def unpack():
    file = open("resources/input.txt", "r")
    lines = file.readlines()
    pairs_num = lines[0].strip('\n')
    pairs_count = [list(map(int, row.split())) for row in lines[1:]]
    return pairs_num, pairs_count


number_of_pairs, pairs = unpack()


def divide_by_tribes(start_pos, pairs):
    tribes = []
    visited = {person: False for person in all_people}

    queue = [start_pos]
    while queue:
        current_person = queue.pop(0)
        tribes.append(current_person)

        if not visited[current_person]:
            neighbours = []
            for people in pairs:
                if current_person in people:
                    neighbours.extend(person for person in people if person != current_person)
            queue.extend(neighbour for neighbour in neighbours if not visited[neighbour])
            visited[current_person] = True

    return tribes


def get_possible_pairs(tribes):
    possible_pairs = []
    pairs_counter = 0

    for other_tribe in tribes:
        if other_tribe is not tribe:

            girls = [person for person in tribe if person % 2 == 0]
            boys = [person for person in tribe if person % 2 == 1]
            other_tribe_boy = [person for person in other_tribe if person % 2 == 1]
            other_tribe_girl = [person for person in other_tribe if person % 2 == 0]

            for girl in girls:
                for boy in other_tribe_boy:
                    potential_pair = [boy, girl]
                    if potential_pair not in possible_pairs:
                        possible_pairs.append(potential_pair)
                        pairs_counter += 1

            for boy in boys:
                for girl in other_tribe_girl:
                    potential_pair = [boy, girl]
                    if potential_pair not in possible_pairs:
                        possible_pairs.append(potential_pair)
                        pairs_counter += 1

    return pairs_counter, possible_pairs


all_people = []
for people in pairs:
    for person in people:
        if person in all_people:
            continue
        all_people.append(person)

tribes = []
while all_people:
    tribe = divide_by_tribes(all_people[0], pairs)
    for person in tribe:
        all_people.remove(person)
    tribes.append(tribe)

print(get_possible_pairs(tribes))
