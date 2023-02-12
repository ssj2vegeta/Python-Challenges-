parent(david, serena)
parent(david, tina)
ancestor(A, B) :-				/* The Base Case */
parent(A, B).
ancestor(A, B) :-				/* The General Case */
parent(A, X),
ancestor(X, B).
