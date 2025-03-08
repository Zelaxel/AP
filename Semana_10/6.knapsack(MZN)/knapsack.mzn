int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí

array[ITEMS] of var 0..2: taken;

var int: total_value = sum(i in ITEMS)(value[i]*taken[i]);

constraint sum(i in ITEMS)(weight[i]*taken[i]) <= capacity;

solve maximize total_value;

output["taken = \(taken)\n", "Total Value = \(total_value)"];
