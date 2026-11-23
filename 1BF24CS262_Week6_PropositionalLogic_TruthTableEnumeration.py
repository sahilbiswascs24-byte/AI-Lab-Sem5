
from itertools import product

# Knowledge Base: (A OR C) AND (B OR NOT C)
# Query: A OR B

def KB(A, B, C):
    return (A or C) and (B or not C)

def Query(A, B, C):
    return A or B

symbols = [True, False]

result = True

print("A\tB\tC\tKB\tQuery")

for A, B, C in product(symbols, repeat=3):

    kb = KB(A, B, C)
    query = Query(A, B, C)

    print(A, B, C, kb, query, sep="\t")

    if kb and not query:
        result = False

if result:
    print("\nKB entails Query")
else:
    print("\nKB does not entail Query")
