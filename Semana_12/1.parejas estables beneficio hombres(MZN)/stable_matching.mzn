include "globals.mzn";

enum Women;
enum Men;

array[Women, Men] of int: wrank;
array[Men, Women] of int: mrank;

%Escribir el código a partir de aquí

array[Men] of var Women: wife;
array[Women] of var Men: husband;
var int: obj_men = sum(m in Men where mrank[m,wife[m]] == 1)(1);
var int: obj_women = sum(w in Women where wrank[w,husband[w]] == 1)(wrank[w,husband[w]]);

constraint inverse(wife, husband);
constraint forall(m in Men, w in Women)
                    (mrank[m,w] < mrank[m,wife[m]] -> wrank[w,husband[w]] < wrank[w,m]);
constraint forall(m in Men, w in Women)
                    (wrank[w,m] < wrank[w,husband[w]] -> mrank[m,wife[m]] < mrank[m,w]);

solve maximize obj_men;

output["wife:\(wife)\n","husband:\(husband)\n","obj_men:\(obj_men)\n","obj_women:\(obj_women)"];
