int:n;                    % numero maximo de items
int: capacity;            % capacidad de la mochila

set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

set of ITEMS: limitation;
int:m;                    % Numero maximo de items a elegir dentro del 
                          % conjuto limitation

% Escribe el código a partir de aquí ----------------------------------

var set of ITEMS: taken;
var int: val = sum(i in taken)(value[i]);
var int: wei = sum(i in taken)(weight[i]);

constraint card(taken intersect limitation) <= m;
constraint wei <= capacity;

solve maximize val;

output["\(taken)\n","\(val)"];