
def unify(e1, e2):

    if e1[0] != e2[0] or len(e1) != len(e2):
        return None

    subs = {}

    for a, b in zip(e1[1:], e2[1:]):

        if a == b:
            continue

        if a.islower():
            subs[a] = b

        elif b.islower():
            subs[b] = a

        else:
            return None

    return subs


# Main program

e1 = ("Eats", "x", "Apple")
e2 = ("Eats", "Riya", "y")

result = unify(e1, e2)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")

    for x, y in result.items():
        print(x, "=", y)

    print("Unified Expression: Eats(Riya, Apple)")
