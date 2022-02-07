#include <iostream>
#include <vector>
#include <unordered_map>

void vectorImplementation (){
    std::vector <int> values = {1,2,3,4};

    // standard way with i to iterate
    for (int i = 0; i < values.size(); i++){
        std::cout << values [i] << std::endl;
    }

    // A cleaner way (Range Based for Loop) if i is not needed 
    // This is a iterator 
    // Think range (0, 4) in python 
    for (int value: values){
        std:: cout << value << std::endl;
    }
    
    // Explicitly calling iterator 
    for (std::vector <int>::iterator it = values.begin(); it!= values.end (); it++){
        std:: cout << *it << std:: endl;
    } 
    // Question: why do you want to use it?
    // 1. maybe you want to insert something ? 

    // Here I used a using. This is equivalent of using typedef 
    using scoreMap = std::unordered_map<std::string, int>;
    scoreMap map;
    // Typedef 
    typedef std::unordered_map<std::string, int> ScoreMap;
    ScoreMap map2;
    map ["jim"] = 1;

    // Iterators are a generalization of pointers. So a pointer IS an iterator.
    //  But not necessarily the other way round. I
    for (scoreMap::const_iterator it = map.begin(); it != map.end(); it ++ ){
        auto & key = it->first;
        auto & value = it->second; 
        std::cout << key << ":" << value << std::endl;

    }

    // Using range based for loop
    for (auto& it : map ){
        auto & key = it.first;
        auto & value = it.second; 
        std::cout << key << ":" << value << std::endl;
    }

    // Even better, using binding from c++11
    for (auto&[k,v]: map){
        std::cout << k << ":" << v << std::endl;
    }

    
    map ["jim"] = 5;
    
}
int main (){



}