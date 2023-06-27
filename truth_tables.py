import ttg
print(ttg.Truths(['p', 'q', 'r'])) #
print(ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r']))


#Operators and their representations:
    #negation: 'not', '-', '~'
    #logical disjunction: 'or'
    #logical nor: 'nor'
    #exclusive disjunction: 'xor', '!='
    #logical conjunction: 'and'
    #logical NAND: 'nand'
    #material implication: '=>', 'implies'
    #logical biconditional: '='
