# Chap01 리스트, 스택, 큐

## Keyword
- std::array, std::vector, std::array_list, std::list, std::deque
- std::stack, std::queue, std::priority_que
- 컨테이너 어댑터

## 선형 자료구조
- 연속된 구조 + 연결된 구조
- 시간복잡도: 특정 작업을 수행하는데 걸리는 시간을 데이터 크기에 대한 수식으로 표현
- 배열(연속된 자료구조): 모든 원소를 단일 메모리 chunk에 저장. cache locality 속성이 있음. 접근시 O(1)
- lined list(연결된 자료구조): node라는 여러 개의 메모리 chunk에 데이터를 저장. 서로 다른 메모리 위치에 데이터가 저장. 접근시 O(n). 삽입, 삭제시 O(1)

## C 스타일 배열 제약
- memory leak 위험성
- []에서 크기 검사를 하지 않음
- deep copy는 수동으로 구현해야 함

## 배열
```cpp
type arr1[size];
type* arr2 = (type*)malloc(size * sizeof(type));
type* arr3 = new type[size];
```

## std::array
- 메모리 자동할당 해제
- 함수에 객체 전달시 깊은 복사로 동작. const, &로 방지
```cpp
std::array<type, size> arr1;
std::array<type, size> arr2 = {1, 2, 3, 4};

arr[index];
arr.at(index);
try {
    arr.at(index);
} catch (const std::cout_of_range& ex) {
    std::cerr << ex.what() << std::endl;
}

arr1.size();

arr1.front();
arr1.back();
*(arr1.data() + 1);   // 메모리 버퍼를 가리키는 포인터
```

```cpp
for (auto it = arr.begin(); it != arr.end(); ++it) {
    auto element = *it;
    std::cout << element << std::endl;
}
```