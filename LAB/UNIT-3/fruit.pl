fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(mango, yellow).

show(Fruit, Color) :-
    fruit(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl,
    fail.

show(_, _).