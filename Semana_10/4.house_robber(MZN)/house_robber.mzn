int: n;
array[1..n] of int: value;

%Introduzca el código a partir de esta línea

array[1..n] of var 0..1: taken;

var int: total_value = sum(i in 1..n where taken[i] == 1)(value[i]);

constraint forall(i in 1..n-1 where taken[i] == 1)(taken[i+1] == 0);

solve maximize total_value;

output["taken= \(taken)\n", "total_value= \(total_value)"];
