#include <iostream>
#include <string>

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