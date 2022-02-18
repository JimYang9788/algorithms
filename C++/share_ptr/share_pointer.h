#ifndef SHARE_POINTER
#define SHARE_POINTER
#include <iostream>

template <typename T>
class SharePointer
{
public:
    // Constructor
    SharePointer<T>(T *ptr) : d_ptr(ptr), d_count(nullptr)
    {
        std::cout << "Constructor Called" << std::endl;
        d_count = new size_t;
        *d_count = 1;
    }
    SharePointer<T>() : d_ptr(nullptr), d_count(nullptr)
    {
        d_count = new size_t;
        *d_count = 1;
    }

    // Copy Constructor
    SharePointer<T>(SharePointer &sp) : d_ptr(sp.get_ptr()), d_count(sp.get_d_count())
    {
        (*d_count)++;
        std::cout << "Copy Constructor Called" << std::endl;
    }

    // Move Constructor
    SharePointer<T>(SharePointer &&sp) : d_ptr(sp.get_ptr()), d_count(sp.get_d_count())
    {
        (*d_count)++;
        std::cout << "Move Constructor Called" << std::endl;
    }

    // Copy Assignment
    SharePointer<T>& operator=(SharePointer &sp)
    {
        std::cout << "Copy Assignment" << std::endl;
        (*d_count)--;
        d_ptr = sp.get_ptr();
        d_count = sp.get_d_count();
        (*d_count)++;
        return *this;
    }


    // Copy Assignment
    SharePointer<T>& operator=(SharePointer &&sp)
    {
        std::cout << "Move Assignment" << std::endl;
        (*d_count)--;
        d_ptr = sp.get_ptr();
        d_count = sp.get_d_count();
        (*d_count)++;
        return *this;
    }

    // Deleter
    ~SharePointer()
    {
        (*d_count)--;
        std::cout << "Destructor Called. Count Remaining: " << *d_count << std::endl;

        if (*d_count == 0)
        {
            delete d_ptr;
            delete d_count;
        }
    }

    T *get_ptr()
    {
        return d_ptr;
    }
    size_t *get_d_count()
    {
        return d_count;
    }
    size_t use_count()
    {
        return *d_count;
    }

private:
    T *d_ptr;        // Underlying Pointer
    size_t *d_count; //
};

#endif
