int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí

array[ITEMS] of var 0..1: taken;

var int: total_value = sum(i in ITEMS where taken[i] == 1)(value[i]);

constraint sum(i in ITEMS where taken[i] == 1)(weight[i]) <= capacity;

solve maximize total_value;

output["taken = \(taken)\n", "Total Value = \(total_value)"];
