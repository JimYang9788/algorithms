#include <iostream>
#include "template.h"

// Template function 
template <class T, class B>
bool GetMax (T a, T b, B x, B y) {
    bool comp = x > y;
    std::cout << comp << std::endl; 
    return (a>b?a:b);
}

template <class T, int N>
class mysequence {
    T memblock [N];
  public:
    void setmember (int x, T value);
    T getmember (int x);
};

template <class T, int N>
void mysequence<T,N>::setmember (int x, T value) {
  memblock[x]=value;
}

template <class T, int N>
T mysequence<T,N>::getmember (int x) {
  return memblock[x];
}

int main (){
    Print(1);
    Array<5> array;
    std::cout << array.get_size() << std::endl;
    return 0;
}
