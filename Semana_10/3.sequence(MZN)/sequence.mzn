int: n= 5;

%Introduzca el código a partir de esta línea

array[1..n] of var 0..3: arr;

constraint arr[1] == 0;
constraint arr[n] == 3;
constraint forall(i in 1..n-1)(arr[i] + arr[i+1] <= 3);
constraint forall(i in 1..n where (i mod 3) == 0)(arr[i] >= 2);

solve maximize (sum(i in arr)(i));

output["x = \(arr)"];