### c++ 写题细节

1. Sorting 

   ``sort（a.begin(),a.end(),comparator)`` 是sort vector的常规方法，记得comparator function需要return boolean, 并需要是一个``static function `` 

   (A **static function** is a member function of a class that can be called even when an object of the class is not initialized. A static function cannot access any variable of its class except for **static variables**.)

     

2. String 

   ``string.length ()`` 查string length 

   

3. Vector ()

   ``vector <int> subset``

   常用： 

   ``vector.push_back (num)``



4. map 

   ``map <char, int>::iterator it;``

   ``for (it = map.begin(); it != map.end(); it ++){ cout << it.first << it.second}`` 取信息

   ``if (map.find (element) != map.end())`` 检查在不在里面

   

