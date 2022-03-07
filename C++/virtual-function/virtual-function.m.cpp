#include <iostream>
#include <vector>
using namespace std;

class Animal
{
private:
    virtual void print() = 0;
    void type() { std::cout << "I am an animal" << std::endl; }

    int height = 0;
};

class Piggy : protected Animal
{
public:
    void print() { std::cout << "I am a Piggy" << std::endl; }
};

class Dog : public Animal
{
public:
    void print() { std::cout << "I am a Dog" << std::endl; }
};

int main()
{
    // Animal *a = new Piggy(); // ptr size -> 8 bytes;
    // Animal *b = new Dog();
    Piggy p = Piggy();
    p.print();
    // Animal &d = p;
    // d.print();
}

//  * ClassName|function name
//  * ------------------------
//  * Piggy    | d_piggy_print
//  * Dog      | d_doggy_print
//  *
//  *
