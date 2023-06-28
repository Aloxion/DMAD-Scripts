def reflective_closure(rel):
    elements = set(x for x, _ in rel) | set(y for _, y in rel)
    return set(rel) | {(x, x) for x in elements}

def symmetric_closure(rel):
    return set(rel) | {(y, x) for x, y in rel}

def transitive_closure(rel):
    closure = set(rel)
    while True:
        new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)

        closure_until_now = closure | new_relations

        if closure_until_now == closure:
            break

        closure = closure_until_now

    return sorted(list(closure))

R = {('a','a'),('a','b'),('b','a'),('b','c')}

refl_closure = reflective_closure(R)
symm_closure = symmetric_closure(R)
trans_closure = transitive_closure(R)

print('Reflective closure:', sorted(list(refl_closure)))
print('Symmetric closure:', sorted(list(symm_closure)))
print('Transitive closure:', sorted(list(trans_closure)))
