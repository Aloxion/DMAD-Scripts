import ttg
print(ttg.Truths(['p', 'q'], ['p or q']))  # One list is an input variable list


# With two lists, the second is an expression given the operators of the first list
print(ttg.Truths(['p', 'q'], ['(p = q) and (p xor q)']))


# Operators and their representations:
# ¬ negation: 'not', '-', '~'
# ∨ logical disjunction: 'or'
# logical nor: 'nor'
# ⊕ exclusive disjunction: 'xor', '!='
# ∧ logical conjunction: 'and'
# logical NAND: 'nand'
# => material implication: '=>', 'implies'
# <=> logical biconditional: '='
