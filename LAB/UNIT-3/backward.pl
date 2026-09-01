fact(bird).
fact(has_wings).

can_fly :-
    fact(bird),
    fact(has_wings).
