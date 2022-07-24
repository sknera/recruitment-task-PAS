"""def get_first_right(domino, start, changes_right):
    for i in range(start, len(domino)):
        if domino[i] == '/':
            pass
        elif domino[i] == '\\':
            break
        elif domino[i] == '|':
            changes_right.append(i)
            break


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
"""


def iteration(domino):
    len_domino = len(domino)
    changes_right = list()
    changes_left = list()
    bckw_domino = domino[::-1]

    flagRight = False
    for i in range(len_domino):
        if flagRight and domino[i] == '\\':
            flagRight = False
        elif flagRight and domino[i] == '|':
            changes_right.append(i)
            flagRight = False
            break
        elif domino[i] == '/':
            flagRight = True

    flagLeft = False
    for i in range(len_domino):
        if flagLeft and bckw_domino[i] == '/':
            flagLeft = False
        elif flagLeft and bckw_domino[i] == '|':
            changes_left.append(i)
            flagLeft = False
            break
        elif bckw_domino[i] == '\\':
            flagLeft = True

    # found in backward domino, now set indexes that will be referenced in original
    changes_left = [len_domino - x - 1 for x in changes_left]
    intersection = list(set(changes_left) & set(changes_right))
    changes_left = [x for x in changes_left if x not in intersection]
    changes_right = [x for x in changes_right if x not in intersection]

    print(changes_left)
    print(changes_right)

    list_domino = list(domino)
    for i in changes_left:
        list_domino[i] = "\\"
    for i in changes_right:
        list_domino[i] = "/"

    return "".join(list_domino)
