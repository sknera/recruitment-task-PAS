def get_first_right(domino, start, changes_right):
    for i in range(start, len(domino)):
        if domino[i] == '/':
            pass
        elif domino[i] == '\\':
            break
        elif domino[i] == '|':
            changes_right.append(i)
            break
    return i


def get_first_left(domino, start, changes_left):
    bckw_domino = domino[::-1]
    for i in range(start, len(domino)):
        if bckw_domino[i] == '\\':
            pass
        elif bckw_domino[i] == '/':
            break
        elif bckw_domino[i] == '|':
            changes_left.append(i)
            break
    return i


def iteration(domino):
    len_domino = len(domino) - 1
    changes_right = list()
    changes_left = list()
    bckw_domino = domino[::-1]

    for i in range(len(domino)):
        if domino[i] == '/':
            get_first_right(domino, i, changes_right)

    for i in range(len(domino)):
        if bckw_domino[i] == '\\':
            get_first_left(domino, i, changes_left)
    changes_left = [len_domino - x for x in changes_left]
    intersection = list(set(changes_left) & set(changes_right))
    changes_left = [x for x in changes_left if x not in intersection]
    changes_right = [x for x in changes_right if x not in intersection]

    list_domino = list(domino)
    for i in changes_left:
        list_domino[i] = "\\"
    for i in changes_right:
        list_domino[i] = "/"

    return "".join(list_domino)

