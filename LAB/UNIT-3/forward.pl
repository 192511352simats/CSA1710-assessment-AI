fact(sunny).
fact(warm).

rule(good_day) :-
    fact(sunny),
    fact(warm).

forward :-
    rule(X),
    write('Derived fact: '), write(X).