def unique_occurences(values):
    map = {}

    for i in set(values):
        map[i] = 0

    for i in values:
        if i in map.keys():
            map[i] += 1

    print(map)

    # print(f"a: {map.values()}, b: {set(map.values())}")

    comp_list = []
    for i in map.values():
        comp_list.append(i)

    print(sorted(comp_list))
    # print(list(set(comp_list)))
    print(sorted(set(comp_list)))

    if sorted(comp_list) == sorted(set(comp_list)):
        return True
    else:
        return False


if __name__ == "__main__":
    # values = [1, 2, 2, 1, 1, 3]
    values = [-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]
    print(unique_occurences(values))