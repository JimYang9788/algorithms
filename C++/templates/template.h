#include <iostream>
#include <string>

// using template for actual argument (the way how to define a class)
template <int T>
class Array
{
public:
    int get_size (){return T;}
private:
    int d_array[T];
};

template <typename T>
void Print(T value)
{
    std::cout << value << std::endl;
}