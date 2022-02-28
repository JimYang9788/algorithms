#include <iostream>
#include <vector>
using namespace std;

class Animal
{
public:
    virtual void print() = 0;

    void type() { std::cout << "I am an animal" << std::endl; }

private:
    int height = 0;
};

class Piggy : public Animal
{
public:
    void print() { std::cout << "I am a Piggy" << std::endl; }
};

int main()
{
    Piggy p = Piggy();
    p.print();
    p.type();
    std::cout
        << "hello world" << std::endl;
}
