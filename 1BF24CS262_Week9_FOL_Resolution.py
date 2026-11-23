def is_variable(x):
    return len(x) == 1 and x.islower()


def substitute(x, subs):
    while is_variable(x) and x in subs:
        x = subs[x]
    return x


def unify(a, b, subs):
    a = substitute(a, subs)
    b = substitute(b, subs)

    if a == b:
        return True

    if is_variable(a):
        subs[a] = b
        return True

    if is_variable(b):
        subs[b] = a
        return True

    return False


def apply_sub(lit, subs):
    neg, pred, args = lit
    return (neg, pred, tuple(substitute(x, subs) for x in args))


def resolve(c1, c2):

    for i, l1 in enumerate(c1):
        for j, l2 in enumerate(c2):

            if l1[0] != l2[0] and l1[1] == l2[1]:

                subs = {}

                if all(unify(a, b, subs)
                       for a, b in zip(l1[2], l2[2])):

                    result = [
                        apply_sub(x, subs)
                        for k, x in enumerate(c1) if k != i
                    ]

                    result += [
                        apply_sub(x, subs)
                        for k, x in enumerate(c2) if k != j
                    ]

                    return result, subs

    return None, None


def display(clause):
    if not clause:
        return "{}"

    result = []

    for neg, pred, args in clause:
        sign = "~" if neg else ""
        result.append(sign + pred + "(" + ", ".join(args) + ")")

    return " OR ".join(result)


# Negated Query
C1 = [(True, "Likes", ("John", "Peanuts"))]

# Clause 1: ~Food(x) OR Likes(John,x)
C2 = [
    (True, "Food", ("x",)),
    (False, "Likes", ("John", "x"))
]

# Clause 2: ~Eats(x,y) OR Killed(x) OR Food(y)
C3 = [
    (True, "Eats", ("x", "y")),
    (False, "Killed", ("x",)),
    (False, "Food", ("y",))
]

# Fact: Eats(Anil, Peanuts)
C4 = [(False, "Eats", ("Anil", "Peanuts"))]

# Clause: ~Alive(x) OR ~Killed(x)
C5 = [
    (True, "Alive", ("x",)),
    (True, "Killed", ("x",))
]

# Fact: Alive(Anil)
C6 = [(False, "Alive", ("Anil",))]


# Resolution Steps

R1, S1 = resolve(C1, C2)
print("Step 1:", display(R1), S1)

R2, S2 = resolve(R1, C3)
print("Step 2:", display(R2), S2)

R3, S3 = resolve(R2, C4)
print("Step 3:", display(R3), S3)

R4, S4 = resolve(R3, C5)
print("Step 4:", display(R4), S4)

R5, S5 = resolve(R4, C6)
print("Step 5:", display(R5))

if R5 == []:
    print("\nEmpty clause found.")
    print("Query Proved Successfully!")
else:
    print("Query Cannot Be Proved")
