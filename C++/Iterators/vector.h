#include <vector>
// Very similar to the standard library vector 

// scoreMap::const_iterator it = map.begin()

template <typename Vector>
class VectorIterator 
{
    // using ValueType = typemame std::vector::ValueType;
    // using PointerType = ValueType*;
    // using ReferenceType = ValueType&;
    // VectorIterator()
    VectorIterator operator--(int)
    {
        VectorIterator iterator = *this;
        --(*this);
        return iterator;
    }

    VectorIterator operator++(int)
    {
        VectorIterator iterator = *this;
        ++(*this);
        return iterator;
    } 
    private:
    // PointerType m_Ptr;
};

template <typename T>
class Vector {
        public:
        Vector():d_size(0),d_capacity(2),d_data(new T[2])
        {
            // Allocate 2 elements 
        };

        ~Vector ()
        {
            delete[] d_data;
        }

        template<typename... Args>
        T& emplace_back(Args&&... args)
        {
            if (d_size >= d_capacity){reallocate();}
            new (d_data[d_size]) T(std::forward<Args>(args)...); // instead of creating it on the stack, you can use new inplace.
            // d_data[d_size] = T(std::forward<Args>(args)...);
            return d_data[d_size++];
        }

        void push_back(const T& element)
        {
            if (d_size >= d_capacity)
            {
                reallocate();
            }  
            assert (d_size < d_capacity);
            // d_size < d_capacity
            d_data[d_size] = element;
            d_size ++;
        };

        void push_back(T&& element)
        {
        // if we have a temporary value, we do move instead of copy 
        if (d_size >= d_capacity)
            {
                reallocate();
            }  
            d_data[d_size] = std::move (element);
            d_size++;
        }

        const T& operator [](unsigned int index) const
        {
            if (index >= d_size){
                // fuck you 
            }
            return d_data[index]; 
        }

        unsigned int size() {return d_size;}
        
        void pop_back (){
            // [1,2,3], pop_back() -> [1,2], removed (size_t - 1)
            if (d_size == 0) {
                return;
            }
            d_size --;
            d_data[d_size].~T();
        }

        void print ()
        {
            for (int i = 0; i < d_size; i ++){
                std::cout << d_data[i] << " ";
            }
            std::cout << std::endl;
        }

        private: 

        void reallocate (){
            // initialize a temp 
            T * temp = new T[d_capacity * 2];
            // copy over 
            // 为啥这里不用memcpy?因为有时候memcpy不会trigger的copy constructor
            for (int i = 0; i < d_capacity; i++)
            {  
                temp[i] =  std::move (d_data[i]);
            }
            delete [] d_data;
            d_data = temp;
            d_capacity *= 2;
        }

        T * d_data = nullptr;
        unsigned int d_size;
        unsigned int d_capacity;
};