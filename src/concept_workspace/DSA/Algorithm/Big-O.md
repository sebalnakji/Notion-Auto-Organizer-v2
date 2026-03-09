# Big-O 표기법 (Big-O Notation)

---

## Why — 왜 필요한가?

컴퓨터 과학에서 알고리즘의 성능을 측정할 때 **실행 시간(초)** 을 직접 비교하면 문제가 생긴다. 같은 코드라도 CPU 속도, 캐시 상태, 운영체제 스케줄러, 컴파일러 최적화 수준에 따라 결과가 달라지기 때문이다.

1860년대 수학자 Paul Bachmann과 Edmund Landau가 정립한 **점근 표기법(Asymptotic Notation)** 은 이 문제를 해결한다. 핵심 아이디어는 두 가지다:

- **입력 크기 `n`** 을 기준으로 성능을 표현한다 → 하드웨어 독립적
- **상수 계수와 하위 차수 항을 무시**한다 → 성장 패턴의 본질에 집중

Big-O는 점근 표기법 중 **상한(upper bound)** 을 나타낸다. "이 알고리즘은 최악의 경우에도 이 속도보다 느려지지 않는다"를 수학적으로 보장하는 도구다.

---

## Where — 어디서 쓰이는가?

### 시나리오 1: API 서버의 검색 기능 설계

사용자 10만 명의 데이터베이스에서 특정 사용자를 찾는 API를 개발한다고 가정하자. 순차 탐색(O(n))으로 구현하면 사용자가 늘어날수록 응답 시간이 선형으로 증가한다. 인덱스 기반 해시 탐색(O(1))이나 B-Tree 인덱스(O(log n))를 선택하면 10만 명이 1억 명으로 늘어도 응답 시간은 거의 변하지 않는다. **Big-O는 "지금은 괜찮지만 규모가 커지면 무너지는 코드"를 사전에 식별하는 언어다.**

### 시나리오 2: 코드 리뷰와 기술 부채 관리

중첩 for 루프가 있는 코드를 리뷰할 때 "이거 느릴 것 같은데"는 주관적 판단이다. "이 로직은 O(n²)이고 `n`이 상품 목록 크기인데, 현재 카탈로그 크기(~50만 개)에서는 약 1250억 번의 비교가 발생합니다"는 객관적 근거다. **Big-O는 성능 문제를 팀 내에서 정확하게 소통하는 공통 언어다.**

---

## What — 정확한 정의와 내부 메커니즘

### 수학적 정의

> 함수 `f(n)`에 대해, `f(n) = O(g(n))`이라 할 때:
> 충분히 큰 모든 `n`에 대해 `f(n) ≤ c · g(n)`을 만족하는 양의 상수 `c`와 `n₀`가 존재한다.

즉, Big-O는 **함수의 성장률에 대한 상한**을 정의한다. `n`이 무한히 커질 때 `f(n)`이 `g(n)`보다 "본질적으로 빠르게 성장하지 않는다"는 의미다.

### 핵심 성질: 점근적 동치

Big-O 분석에서 다음 두 가지를 버린다:

1. **상수 계수 제거**: `5n` → `O(n)` (실제 하드웨어가 상수를 흡수함)
2. **하위 차수 항 제거**: `n² + 1000n + 50` → `O(n²)` (n이 커지면 n²이 지배함)

### 주요 복잡도 클래스 (빠른 순서)

| 표기법 | 이름 | 예시 |
|--------|------|------|
| O(1) | 상수 | 해시맵 조회, 배열 인덱싱 |
| O(log n) | 로그 | 이진 탐색, B-Tree 탐색 |
| O(n) | 선형 | 배열 순회, 선형 탐색 |
| O(n log n) | 선형로그 | 병합 정렬, 힙 정렬 |
| O(n²) | 이차 | 버블 정렬, 중첩 루프 비교 |
| O(2ⁿ) | 지수 | 부분집합 열거, 피보나치 재귀 |
| O(n!) | 팩토리얼 | 순열 완전 탐색 |

### 보조 표기법 (Big-O와 함께 알아야 할 것들)

- **Ω(g(n)) — Big-Omega**: 하한(lower bound). 최선의 경우도 이보다 빠르지 않음
- **Θ(g(n)) — Big-Theta**: 상한과 하한이 같음. 정확한 점근적 성장률. `O`이면서 `Ω`
- **실무 관점**: "O(n log n)"은 상한이므로 실제 성능은 더 좋을 수도 있다. 정확한 분석엔 Θ가 필요하다.

### 공간 복잡도도 Big-O로 표현

시간 복잡도만이 아니다. 알고리즘이 **추가로 사용하는 메모리**도 Big-O로 표현한다. 재귀 함수의 호출 스택(O(n) 공간), 해시맵 캐시(O(n) 공간) 등이 그 예다.

---

## How — 단계별 분석 방법과 실전 예제

### 분석 절차

1. **입력 크기 `n`을 정의한다** — 배열의 길이, 노드의 수, 문자열의 길이 등
2. **기본 연산(primitive operation)을 식별한다** — 비교, 할당, 산술 연산 등 O(1) 단위 연산
3. **`n`에 따른 연산 횟수 `T(n)`을 수식으로 작성한다**
4. **상수와 하위 차수 항을 제거해 Big-O를 도출한다**

---

### 실전 예제 1: 두 포인터로 합 쌍 찾기

**문제**: 정렬된 배열에서 합이 `target`인 쌍의 개수를 구하라.

```python
# 나이브한 접근 — O(n²)
def count_pairs_naive(arr, target):
    count = 0
    n = len(arr)
    # ※ 중복 원소가 없는 정렬된 배열을 가정
    for i in range(n):          # n번 반복
        for j in range(i+1, n): # 최대 n-1번 반복
            if arr[i] + arr[j] == target:
                count += 1
    return count
# T(n) = n*(n-1)/2 = (n²-n)/2 → 상수·하위항 제거 → O(n²)

# 최적화 — O(n)
def count_pairs_two_pointer(arr, target):
    count = 0
    left, right = 0, len(arr) - 1
    # ※ 중복 원소 처리는 생략하고 핵심 로직만 간소화
    while left < right:         # 최대 n번 반복
        s = arr[left] + arr[right]
        if s == target:
            count += 1
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return count
# T(n) = n → O(n)
```

**n = 10만일 때 비교 횟수 차이:**
- O(n²): 약 50억 번 (n*(n-1)/2 ≈ 5,000,000,000)
- O(n): 약 10만 번
- **차이: 약 5만 배**

---

### 실전 예제 2: 재귀 함수의 복잡도 분석

```python
# 피보나치 — 나이브 재귀
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**트리 구조로 분석:**
- `fib(n)`은 `fib(n-1)`과 `fib(n-2)`를 호출 → 호출 횟수가 2배씩 증가
- 트리의 깊이: `n` → 총 노드 수: 약 `2ⁿ` → **O(2ⁿ)**

```python
# 메모이제이션 — O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)
# 각 n에 대해 한 번만 계산 → T(n) = n → O(n)
```

---

### 실전 예제 3: 복합 연산의 분석

```python
def process(items):
    items.sort()                          # O(n log n)
    seen = set()
    for item in items:                    # O(n)
        if item not in seen:              # O(1) 평균 — 해시셋
            seen.add(item)                # O(1) 평균

# 전체 T(n) = O(n log n) + O(n) * O(1)
#           = O(n log n) + O(n)
# 지배항: n log n > n → 최종 O(n log n)
```

**규칙**: 순차 실행 시 더 큰 복잡도를 가진 연산이 전체를 지배한다.

---

## Pitfall — 흔한 실수와 오해

### Pitfall 1: O(1)을 "빠르다"로 오해하기

O(1)은 **입력 크기와 무관하게 일정하다**는 의미이지, 빠르다는 의미가 아니다.

```python
# 이 함수는 O(1)이지만 10억 번의 연산을 수행한다
def constant_but_slow():
    result = 0
    for i in range(1_000_000_000):  # 상수 반복
        result += i
    return result
```

실무에서 캐시 미스, 메모리 접근 패턴, 분기 예측 실패는 Big-O에 포함되지 않지만 실제 성능에 크게 영향을 준다. **O(n)이 O(1)보다 실제로 빠른 경우도 흔하다** (예: 캐시 친화적 배열 순회 vs 포인터 체이싱 해시맵).

### Pitfall 2: 최악의 경우만 고려하는 편향

Big-O는 **최악의 경우 상한**이지만, 실무에서는 평균 복잡도(Average-case)와 최선의 경우(Best-case)도 중요하다.

- **퀵 정렬**: 최악 O(n²), 평균 O(n log n) → 실제론 병합 정렬보다 자주 빠름
- **해시맵 조회**: 최악 O(n) (충돌), 평균 O(1) → 실무에서는 평균을 기준으로 설계

분석할 때는 "**이 알고리즘의 최악 시나리오가 실제로 발생할 가능성이 있는가?**"를 함께 고려해야 한다.

---

## Tips — 실전 노하우

### Tip 1: 언어/라이브러리 내장 함수의 복잡도를 암기하라

```python
# Python 예시
list.append()      # O(1) 분할상환
list.insert(0, x)  # O(n) — 앞에 삽입 = 전체 이동
list.pop()         # O(1)
list.pop(0)        # O(n) — 앞에서 제거 = 전체 이동
dict[key]          # O(1) 평균
set.__contains__   # O(1) 평균
sorted()           # O(n log n) — Timsort
```

`list.insert(0, x)` 대신 `collections.deque`의 `appendleft()`(O(1))를 쓰는 것처럼, **내장 자료구조의 복잡도 특성을 알아야 올바른 선택이 가능하다.**

### Tip 2: 분할상환 분석(Amortized Analysis)을 이해하라

동적 배열(Python list, Java ArrayList)의 `append`는 가끔 O(n) 리사이징이 발생하지만, 전체 n번의 append를 놓고 보면 **평균 O(1)**이다. 이를 **분할상환 O(1)**이라 한다.

```
총 비용: n + n/2 + n/4 + ... ≈ 2n = O(n)
n번 수행했으므로 평균: O(n)/n = O(1)
```

이 개념을 모르면 루프 안에서 append를 쓰는 코드를 O(n²)으로 오분석할 수 있다.

### Tip 3: 공간-시간 트레이드오프를 Big-O로 명시적으로 표현하라

최적화 제안을 할 때 숫자를 구체적으로 제시하면 설득력이 높아진다:

```
# 명확하지 않은 표현
"메모이제이션을 쓰면 빠릅니다"

# Big-O로 표현한 트레이드오프
"시간: O(2ⁿ) → O(n), 공간: O(1) → O(n).
 n=40 기준 약 10억 배 빠르고, 메모리는 수백 바이트 추가 사용"
```

---

## Reference

- **Cormen et al., "Introduction to Algorithms" (CLRS)** — 3장: Growth of Functions. Big-O의 수학적 정의와 점근 표기법의 표준 교재
- **MIT OpenCourseWare 6.006** — Introduction to Algorithms 강의 (공개 무료): https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- **Big-O Cheat Sheet** — 주요 자료구조와 알고리즘의 복잡도 요약: https://www.bigocheatsheet.com
- **Python Time Complexity (공식 문서)** — Python 내장 자료구조의 공식 복잡도: https://wiki.python.org/moin/TimeComplexity
- **Java Collections Framework 복잡도** — OpenJDK 공식 문서 내 각 컬렉션의 Javadoc 참고
