facts = {
    ("Owns", "A", "T1"),
    ("Missile", "T1"),
    ("American", "Robert"),
    ("Enemy", "A", "America")
}

rules = [
    ([("Missile", "x")],
     ("Weapon", "x")),

    ([("Missile", "x"), ("Owns", "A", "x")],
     ("Sells", "Robert", "x", "A")),

    ([("Enemy", "x", "America")],
     ("Hostile", "x")),

    ([("American", "p"), ("Weapon", "q"),
      ("Sells", "p", "q", "r"), ("Hostile", "r")],
     ("Criminal", "p"))
]

variables = {"x", "p", "q", "r"}

proof = {}


def match(pattern, fact, subst):
    subst = subst.copy()

    if pattern[0] != fact[0] or len(pattern) != len(fact):
        return None

    for p, f in zip(pattern[1:], fact[1:]):
        if p in variables:
            if p in subst and subst[p] != f:
                return None
            subst[p] = f
        elif p != f:
            return None

    return subst


def find_substitutions(premises, index, subst, current_facts):
    if index == len(premises):
        yield subst
        return

    for fact in current_facts:
        new_subst = match(premises[index], fact, subst)

        if new_subst is not None:
            yield from find_substitutions(
                premises, index + 1, new_subst, current_facts
            )


def apply_substitution(expression, subst):
    return tuple(subst.get(x, x) for x in expression)


def forward_chaining():

    global facts

    while True:
        new_facts = set()
        current_facts = list(facts)

        for premises, conclusion in rules:

            substitutions = find_substitutions(
                premises, 0, {}, current_facts
            )

            for subst in substitutions:
                new_fact = apply_substitution(conclusion, subst)

                if new_fact not in facts:
                    new_facts.add(new_fact)

                    proof[new_fact] = [
                        apply_substitution(p, subst)
                        for p in premises
                    ]

        if not new_facts:
            break

        facts.update(new_facts)

        query = ("Criminal", "Robert")

        if query in facts:
            break

    return ("Criminal", "Robert") in facts


def print_proof(fact, level=0):
    print(" " * level + str(fact))

    if fact in proof:
        for parent in proof[fact]:
            print_proof(parent, level + 1)


query = ("Criminal", "Robert")

if forward_chaining():
    print("Query Proved Successfully!")
    print("\nForward Chaining Proof Tree:")
    print_proof(query)
else:
    print("Query Cannot Be Proved")
