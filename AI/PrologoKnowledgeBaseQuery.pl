

parent(john, mary).
parent(john, steve).
parent(mary, alice).
parent(mary, bob).
parent(alice, carol).
parent(alice, david).
parent(bob, emily).
parent(bob, frank).

parent(a, b).
parent(a, c).
parent(b, d).
parent(b, e).
parent(d, f).
parent(d, g).
parent(c, h).
parent(c, i).
parent(i, j).
parent(i, k).



male(john).
male(steve).
male(bob).
male(carol).
male(david).
male(frank).
male(a).
male(b).
male(e).
male(f).
male(g).
male(h).
male(i).
male(k).



female(mary).
female(alice).
female(emily).
female(c).
female(d).
female(j).



grandparent(GP, GC) :-
    parent(GP, P),
    parent(P, GC).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

uncle(Uncle, N) :-
    brother(Uncle, P),
    parent(P, N).

aunt(Aunt, N) :-
    sister(Aunt, P),
    parent(P, N).
