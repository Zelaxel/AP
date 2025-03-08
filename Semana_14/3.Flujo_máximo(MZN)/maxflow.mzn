int: num_nodes;                          % número de nodos del grafo
int: num_edges;                          % número de aristas del grafo

1..num_nodes:source;                     % nodo fuente
1..num_nodes:sink;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges; % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity;    % capacidad de cada arista

var int: max_flow;                       % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

output
[ 
  "max flow =" ++ show(max_flow)
];

% Escribir el código a partir de aquí-----------------------------------------

constraint forall(e in 1..num_edges)(flow[e] <= capacity[e] /\ flow[e] >= 0);
constraint forall(n in 1..num_nodes where n != sink /\ n != source)(
                    sum(e in 1..num_edges where edges[e,1] == n)(flow[e]) ==
                    sum(e in 1..num_edges where edges[e,2] == n)(flow[e]));
constraint max_flow = sum(e in 1..num_edges where edges[e,2] == sink)(flow[e]);

solve maximize max_flow;
