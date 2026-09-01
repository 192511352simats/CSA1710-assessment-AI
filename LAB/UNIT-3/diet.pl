diet(diabetes, 'low sugar, vegetables, whole grains').
diet(bp, 'low salt, fruits, vegetables').
diet(obesity, 'low fat, vegetables, fruits').
diet(anemia, 'iron rich foods, spinach, beans').

suggest(Disease) :-
    diet(Disease, Food),
    write('Suggested diet: '), write(Food).