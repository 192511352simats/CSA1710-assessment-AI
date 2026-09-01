parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, alice).
parent(mary, bob).

male(john).
male(tom).
male(bob).

female(susan).
female(mary).
female(alice).

father(X,Y) :-
    parent(X,Y), male(X).

mother(X,Y) :-
    parent(X,Y), female(X).

sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X \= Y.

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).