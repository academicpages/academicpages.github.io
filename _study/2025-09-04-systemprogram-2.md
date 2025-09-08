---
title: "[System Programming] 02 "
date: 2025-09-04
permalink: /study/2025-09-04-systemprogram-2
categories: SystemProgramming
tags: 
  - SystemProgramming


---

In this post, 02 System Programming lecture is introuduced. 



# Writing Good Code

## EX1 Alphabet, Number Counter

사용자의 표준 입력으로부터 # of Alphabet, # of number, # of other characters 를 구해 출력하는 C 프로그램을 생각해보자.

```c
#include <stdio.h>
int main(void){
  // EOF == (int) -1 == 0xFFFFFFFF
  int c;
  int alphaCount = 0;
  int digitCount = 0;
  int othersCount = 0;
  
  while ((c = getchar()) != EOF){
    if ((c >= 97 && c <= 122) || (c >=65 && c<=90))
      alphaCount++;
    else if (c >= 48 && c <= 57)
      digitCount++;
    else
      othersCount++
  }
  printf("# of alphabets: %d\n", alphaCount);
  printf("# of digits: %d\n", digitCount);
  printf("# of other characters: %d\n", othersCount);
  
  return 0;
}
```

`EOF`는 C 언어에서 입력 함수(`getchar`, `scanf`, `fgetc` …)가 더 이상 읽을 데이터가 없을 때 반환하는 특수한 신호 값이다. C 표준에서 `EOF`는 보통 **`-1`** 로 정의되어 있다. 리눅스 키보드 입력에서는 `Ctrl+D` 로 EOF를 발생시킬 수 있다.

- `getchar` 의 return 값은 1 byte인데 왜, 변수 `c` 의 type을 `char`가 아닌 `int` 로 해야만 할까?
  - ASCII 코드에는 0~255 번에 해당하는 character 가 정의되어 있다. 따라서, `char` 변수를 사용하게 되면 `char` 이 저장하는 8 비트의 값은 항상 어떤 character를 나타내게 될 뿐, -1 을 표현할 수 없게 된다. 

위 코드의 조건문에서 우리는 ASCII 코드를 일일이 확인해야 하는 번거로움이 있다. 대신, 다음과 같이 나타낼 수 있다.

```c
if ((c >= 'a' && c <= 'z') || (c >='A' && c<='Z'))
```

하지만 여전히, ASCII 코드에 종속적이라는 문제가 있다. 만약 유니코드를 사용한다면?

이러한 문제를 해결하기 위해서 함수를 사용할 수 있다.

```c
#include <stdio.h>
#include <ctype.h>

if (isalpha(c))
else if (isdigit(c))
```



## Word Counter

이번엔 단어의 개수를 세는 코드를 구현하자. 이를 위해, **state tracking** approach 를 한다. 

state1 : inside-a word, state : 2 outside-a-word 로 정의하면 # of words = # of times when program switches from state2 to state1 이 된다. 

```c
#include <stdio.h>
#include <ctype.h>

int main(void){
  int c, nWords = 0, state = 1;
  
  while ((c = getchar()) != EOF){
    switch(state){
      case 0:
        if (isspace(c)) state = 1;
        	break;
       case 1:
        if (!isspace(c)) {state = 0; nWords++;}
        	break;
    }
  }
}
```

하지만 여기서 0, 1과 같은 개발자만 알고 있는 magic number는 피하는 것이 좋다.

```c
enum DFAState {IN, OUT};

int main(void){
  enum DFAState state = OUT;
}
```

모든 switch-case 에는 default case를 넣는 Defensive programming 을 할 필요가 있다.

```c
default:
	assert(0);
	break;
```



# Pointer

No restrictions on referenced types.

```c
struct student *p; // points to a structure type
int **p; // points to pointers to integer
int (*p)[10]; // points to integer array of size 10
int *p[10]; // array of 10 integer pointers
```

`*` 는 `[]` 보다 낮은 우선순위를 가지므로 위와 같이 나타난다.



```c
int *p;
*p = 10; // crash
printf("%d", *p); // crash
printf("%p", p); // no crash
```

다음과 같이 포인터 변수를 선언만 한다면 Garbage 값이 들어가게 되고 OS에서 할당하지 않은 주소를 참조하게 되어 Segmantation Fault가 난다.

세그멘테이션 폴트(segfault)는 CPU 하드웨어가 트리거하는 예외이다.

- CPU가 특정 **가상 주소**를 읽거나 쓸 때,
- 그 주소가 **페이지 테이블에 매핑되어 있지 않거나**
- 매핑돼 있어도 **접근 권한(읽기/쓰기/실행)** 이 없을 때

→ 하드웨어가 **page fault 예외**를 내고, OS가 이를 처리하다가 “이건 프로그램 잘못”이라 판단하면 SIGSEGV(세그폴트)를 보낸다.



```c
int i;
scanf("%d", &i)l
```

`scanf` 는 표준 입력을 받아, ASCII String을 `%d` 이면 정수로 변환한다. 예를들어, 123을 입력하면 세 개의 ASCII 코드로부터 정수 123을 변환하여 변수에 저장한다. `scanf` 의 argument 로는 주소값이 들어가야 한다.

```c
int i, *p;
p = &i;
scanf("%d", p); // OK
scanf("%d", &p); // no crash, but not ok
```

마지막 줄을 보면, `p` 의 메모리 주소도 OS에서 할당된 영역이기 때문에 crash가 나지는 않지만 논리적으로 우리가 하려는 일과 맞지 않다.



## Pointer Arithmetic

If `p` points to `a[i]`, then, `p+j` points to `a[i+j]`. 
