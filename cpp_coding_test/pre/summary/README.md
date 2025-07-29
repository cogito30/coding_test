# Data Structure

| 자료구조 | 접근 | 탐색 | 삽입 | 삭제 |
| array |  |  |  |  |
| doubly linked list |  |  |  |  |
| stack |  |  |  |  |
| queue |  |  |  |  |
| hash table |  |  |  |  |
| binary search tree |  |  |  |  |
| AVL tree |  |  |  |  |
| Red-Black tree |  |  |  |  |

## STL(자료구조)
- 정적/동적 배열
- std::array
- std::vector: 동적 배열
- std::forward_list
- std::list
- std::stack: LIFO
- std::queue: FIFO
- std::deque: 양방향 큐
- std::priority_queue
- std::unordered_set: 해시 기반 set, 정렬 없음
- std::unordered_map: 해시 기반 map
- std::set: 중복없는 정렬된 집합
- std::map: key-value, key 기준 정렬
- std::pair: 두 개의 값을 저장

## STL(알고리즘)
- std::sort(시작위치, 끝위치, 비교함수)
- std::reverse(시작위치, 끝위치)
- std::min_element(시작위치, 끝위치)
- std::max_element(시작위치, 끝위치)
- std::lower_bound(시작위치, 끝위치, 값): 이진 탐색, 정렬 필수
- std::upper_bound(시작위치, 끝위치, 값): 이진 탐색, 정렬 필수
- std::next_permutation(시작위치, 끝위치): 순열 생성