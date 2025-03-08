%Planificacion temporal

include "cumulative.mzn";

int:n; % total programas

int:k; % numero total de programadores

int:max_tiempo; % limite superior de tiempo

array [1..n] of int: tiempo;
array [1..n] of int: prog;

output["Total: "++show(total)++"\n"]++[show(comienzo[i])++" " | i in 1..n];

%Introducir el codigo a partir de aqui

array [1..n] of var 0..max_tiempo: comienzo;

constraint cumulative(comienzo, tiempo, prog, k);

var int: total = max([tiempo[i] + comienzo[i] | i in 1..n]);

constraint total <= max_tiempo;

solve minimize total;
