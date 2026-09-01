bird(sparrow).
bird(eagle).
bird(parrot).
bird(penguin).
bird(ostrich).

can_fly(sparrow).
can_fly(eagle).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).

flies(B) :-
    can_fly(B),
    write(B), write(' can fly.').

flies(B) :-
    cannot_fly(B),
    write(B), write(' cannot fly.').