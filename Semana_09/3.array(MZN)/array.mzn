int: n = 5;

%Introduzca el código a partir de esta línea

array[1..n] of var 1..9: x;

constraint sum(i in 1..n)(x[i]) == product(i in 1..n)(x[i]);
constraint forall(i in 1..n-1)(x[i] <= x[i+1]);

solve maximize sum(i in 1..n)(x[i]);

output["x = array1d(1..\(n), \(x)"];