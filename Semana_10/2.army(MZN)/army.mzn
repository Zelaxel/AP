%Escribir aquí la solución
int: presupuesto = 10000;

var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

constraint (F*13+L*21+Z*17+J*100) <= presupuesto;

solve maximize (F*6+L*10+Z*8+J*40);

output["F = \(F)\n",
       "L = \(L)\n",
       "Z = \(Z)\n",
       "J = \(J)\n",];
