move(state(floor, floor, no), state(floor, floor, yes)) :-
    write('Monkey takes banana'), nl.

move(state(floor, Pos, no), state(chair, Pos, no)) :-
    write('Monkey climbs chair'), nl.

move(state(chair, Pos, no), state(floor, Pos, no)) :-
    write('Monkey climbs down'), nl.

get_banana(state(_, _, yes)) :-
    write('Monkey got the banana!').

get_banana(State) :-
    move(State, NewState),
    get_banana(NewState).
    