#include <iostream>
#include <vector>
#include <unordered_map>

int main (){
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
    
    
    map ["jim"] = 5;
    


}