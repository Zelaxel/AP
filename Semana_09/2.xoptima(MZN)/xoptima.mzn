var 0..10: x;

constraint (x mod 4) == 0;

solve minimize pow(x-7,2);

output ["x= \(x)\n",
        "obj=\(pow(x-7,2))"];
