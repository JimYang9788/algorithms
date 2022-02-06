## 2.1 C++ Language Feature in Competitive Progamming



1. Library uses and Compiler

`<bits/stdc++.h>` includes all the standard libraries such as iostream, vector and algorithm to the code (takes more time to compile but saves the needs to include multiple things)

```c++
#include <bits/stdc++.h>
```

Uses 

```c++
g++ -std=c++11 -O2 -Wall test.cpp -o test
```

2. Input / Output 

**Question 1**: 为什么 << '\n' 要比  << endl 好？ 

**Answer： **`endl` 在执行的过程中，是一定会触发一个flush的过程的,相当于

```c++
<< "\n" << flush;
```

flush的实际作用是将缓冲(buffer)里面的数据write out (forces any buffered output bits to be written out). 如果在buffer还没有满的情况下，就直接强制flush，会导致过多的读取(相比"\n" 可以读更少的内容)

