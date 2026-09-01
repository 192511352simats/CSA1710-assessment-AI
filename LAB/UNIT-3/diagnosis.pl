symptom(fever).
symptom(cough).
symptom(cold).

diagnose(flu) :-
    symptom(fever),
    symptom(cough),
    write('Diagnosis: Flu').

diagnose(cold) :-
    symptom(cold),
    write('Diagnosis: Common Cold').