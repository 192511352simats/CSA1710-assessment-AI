edge(a, b, 2).
edge(a, c, 4).
edge(b, d, 3).
edge(c, d, 1).
edge(d, e, 2).

best(X, X, [X]).
best(X, Y, [X|Path]) :-
    edge(X, Z, _),
    best(Z, Y, Path).

search(X, Y) :-
    best(X, Y, Path),
    write('Path: '), write(Path).