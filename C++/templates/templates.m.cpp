#include <iostream>


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
    std::cout <<  GetMax(1,2,"s","s") << std::endl;
    mysequence <int,5> myints;
    mysequence <double,5> myfloats;
    myints.setmember (0,100);
    myfloats.setmember (3,3.1416);
    using namespace std;
    {
        cout << myints.getmember(0) << '\n';
        cout << myfloats.getmember(3) << '\n';
    } // namespace std::

    return 0;
}
