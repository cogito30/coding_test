## 주요 라이브러리 및 메서드

#### 1. 문자열
```
str()
str[index]
str[start:end:step]
str[index].isupper()
str[index].islower()
str[index].upper()
str[index].lower()
str[index].isdecimal()
str[index].isalpha()
ord(str[index])
chr(ord('a'))
str.index(val)
str.replace(변경대상, 변경후 값)
str.find(val)
str.startswith()
str.endswith()
```

2. 리스트
```
lst = []
lst.append(val)
lst.pop()
lst[index]
lst[start:end:step]
lst.extend([val, ...])
```

3. 덱
```
from collections import deque

dq = deque()
dq.append(val)
dq.appendleft(val)
dq.popleft()
dq.pop()
dq[index]
```

4. 딕셔너리/해시/맵
```
hash = dict()
hash = {key: val, ...}
hash[key]
hash.get(key, None)
hash.items()
hash.keys()
hash.values()
```

5. 집합/셋
```
s = set()
s.add(val)
s.remove(val)
```