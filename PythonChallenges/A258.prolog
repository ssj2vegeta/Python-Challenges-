hero(goku)
villian(frieza)
hero(vegeta)
enemy(cell)
fight(goku, frieza)
fight(vegeta, frieza)
fight(goku, cell)
fight(vegeta, cell)
fight(cell, frieza)
fight(frieza, vegeta)
fight(frieza, goku)
fight(frieza, cell)
fight(cell, goku)
fight(cell, vegeta)
hate(X,Y) :-
    fight(X,Y),
    fight(Y,X)
