def transitive_closure(rel):
    closure = set(rel)
    while True:
        new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)

        closure_until_now = closure | new_relations

        if closure_until_now == closure:
            break

        closure = closure_until_now

    return sorted(list(closure))

R = {('a','b'),('a','c'),('b','b'),('c','d'),('d','e')}
closure = transitive_closure(R)

print(closure)
