## Array

## Description

## STL
#### 정적/동적 배열
- 
```cpp
type arr[size];
type arr[size] = {val, ...};

type* arr = (type*)malloc(size * sizeof(type));
type* arr = new type[size];

arr[index];
```

#### std::array
- 메모리를 자동으로 할당하고 해제
```cpp
#include <array>
std::array<type, size> arr;
std::array<type, size> arr = {val, ...};

arr[index];
arr.at(index);

arr.front();
arr.back();
*(arr.data() + index);
```

#### std::vector
- 
```cpp
#include <vector>
std::vector<type, size> vec;

```