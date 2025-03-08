%TSP trayecto parcial mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 

% Introducir el codigo a partir de aqui ------------------------------------------

array [City] of var City: succ;

constraint circuit(succ);
constraint forall(i in City)(distance[i, succ[i]] != -1);
constraint forall(i in City)(distance[i, succ[i]] <= maxAllowedEdge);
var int: mayor = max([distance[i, succ[i]] | i in City]);

solve minimize mayor;

output["succ = array1d(1..\(numCities), \(succ)\n maxEdge=\(mayor)"];
