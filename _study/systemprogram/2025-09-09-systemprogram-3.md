---
title: "[System Programming] 03 Pointer"
date: 2025-09-09
permalink: /study/2025-09-09-systemprogram-3
categories: SystemProgramming
tags: 
  - SystemProgramming


---

In this post, 03 System Programming lecture is introuduced. 



# More on Pointer

## Pointer Arithmetic

If `p` points to `a[i]`, then, `p+j` points to `a[i+j]`. 

```c
int a[10], *p, *q, i;
p = &a[2]; // a[2] 의 address 저장.
q = p + 3; // int type array 이므로, (p에 저장된 address) + (4 * 3) 의 주소 값이 저장됨.
```

- `p + q` 와 같은 연산은 불가하다.

If `p` and `q` point to `a[i]` and `a[j]` , `p-q` is eqaul to `i - j`

```c
p = &a[5];
q = &a[1];
i = p - q; // i == 4
i = q - p ; // i == -4
```

- 계산의 결과가 `4 (size of int) * (i - j)` 가 아님에 유의하자
- 다음의 경우 undefined behavior 가 나타난다.
  - Peforming pointer arithmetic that doesn't point to an array element
  - Subtracting pointers unless both point to elements of the same array (컴파일러가 포인터가 같은 array를 가리키는지 체크하는 것은 일반적으로 어려우므로 컴파일 에러가 나지는 않음)

## Array and Pointer Relationship

이에 관한 내용은 <a href = "https://arcstone09.github.io/study/2025-09-03-java-5"> 여기 </a> 참고 바람.

Array 이름은 array 의 첫번째 원소를 가리키는 pointer로 사용할 수 있다.

```c
int a[10];
*a = 7; // stores 7 in a[0]
*(a+1) = 12; // stores 12 in a[1]
```

- `a+i` 는 `&a[i]` 와 같다.
- `*(a+i)` 는 `a[i]` 와 같다.
- `a` 의 type은 분명히 pointer 가 아닌 array of 10 integers (int[10]) 이다. 하지만 많은 경우, pointer 행동한다. (a's type is array of 10 integers, but decays to int* most time)

array의 이름이 pointer가 아니라는 사실을 pointer와 다른 동작을 하는 지점이 있음을 의미한다.

- `sizeof()` 의 결과로, 포인터의 크기 8 byte 가 아닌, array의 크기가 나온다. (위 예시의 경우 40)
- & 관한 예외 (slide 25)
- initialization 관한 예외  (slide 25)

- array name cannot be assigned a new value

  ```c
  while (*a != 0)
  	a++; // compile error
  ```

  대신, 이렇게 쓸 수 있다.

  ```c
  int *p = a;
  while (*p != 0)
    p++;
  ```

## Array Arguments

아래 내용을 이해하기 위해 `const` 키워드에 대한 이해가 필요하다.

- `const` 가 `*` 앞에 붙는 경우

  ```c
  const int *p;
  int const *p;   // 같은 의미
  ```

  해석: "`p`가 가리키는 대상(int)은 **const**" 즉, **가리키는 값은 수정 불가**, 주소는 바꿀 수 있음.

  ```c
  int x = 10, y = 20;
  const int *p = &x;
  
  *p = 15;   // 불가능 (값 수정 불가)
  p = &y;    // 가능 (주소 변경 가능)
  ```

- `const` 가 `*` 뒤에 붙는 경우

  ```c
  int * const p = &x;
  ```

  해석: "`p`라는 포인터 변수는 **const**" 즉, **포인터가 저장하는 주소값은 불변**, 하지만 가리키는 값은 수정 가능.

  ```c
  int x = 10, y = 20;
  int * const p = &x;
  
  *p = 15;   // 가능 (값 수정 가능)
  p = &y;    // 불가능 (주소 변경 불가)
  ```



Array name 이 함수의 argument 로 전달될 때, 포인터처럼 주소가 전달되는데 그 결과로 다음의 영향이 있다.

- <u>Array argument isn't protected against change in its element</u>

  함수 내부에서 인자로 받은 array name 을 이용해 array 의 원소를 바꿔버릴 수 있다.

  이를 막으려면 `const` 를 이용한다. Compiler 는 `a` 의 원소 값이 바뀌면 컴파일 에러를 낸다.

  ```c
  int func(const int a[]){
    a[0] = 3; // compile error
  }
  ```

- <u> The time required to pass an array to a function doesn't depend on the size of the array</u>

  There is no penalty for passing a large array, since no copy of the array is made

- <u>An array parameter can be declared as a pointer if desired</u>

  ```c
  int func(int *a){
    ...
  }
  
  int func(int a[])
  ```

  위 두 표현은 identical 하다. 함수 argument로 array name을 넘겨주면 내부적으로 `int *a` 로 치환한다. 따라서, 이 함수 내부에서 `sizeof(a)` 를 계산하면 위에서 보았던 것처럼 40 (array size) 가 나오는 것이 아니라 8이 나온다.

- <u> A function with an array parameter can be passed an array "slice" - a sequence of consecutive elements</u>



## Crash

```c
int a[10];
*a = 0; // no crash (trivial)

int *a;
*a = 0; // it may crash (if a stores address that exceeds the procedure's memory range)
```



## Double Pointer

...



## Complex Pointer Declarations

- rule : `()` > `[]` > `*`  is the order of priority

  ```c
  int *p[10]; // p is an array. of what? 10 integer pointers
  int (*p)[10]; // p is an pointer. of waht? pointing array of 10 integers
  int *(*p)[10]; // p is an pointer. of what? pointing array of 10 int pointers
  ```

  `int p[10];` 과 `int (*p)[10];` 의 차이는 <a href = "https://arcstone09.github.io/study/2025-09-03-java-5"> 여기 </a> 참고. `int p[10];` 의 메모리 구조에서 오해하는 파트의 설명 내용이 `int (*p)[10];` 에 해당.

  이어서 다음 예시를 보자. 함수에 대해서도 pointer 선언이 가능하다. 

  ```c
  #include <stdio.h>
  
  int hello(void) {
      printf("Hello!\n");
      return 42;
  }
  
  int main() {
      int (*pf)(void);  // 함수 포인터 선언
      pf = hello;       // 함수 이름은 함수의 주소로 decay
      // pf = &hello;   // 이렇게 써도 같음
  
      int result = pf(); // 함수 포인터를 통해 호출
      printf("%d\n", result);  // 42
  }
  ```

  ```c
  int (*pf) (void); // pf is a pointer. of what? pointing a function returning int w/o parameter
  int *pf(void); // pf is a function. of waht? returining int pointer, and have no parameter
  int (*pf[10]) (void); // pf is an array. of what? 10 pointers. of what? pointing a function returning int w/o parameter
  int pf[] (void); // pf is an array. of what? functions returining int w/o parameter. ILLEGAL
  ```

  마지막 예시와 관련해서 C 표준에서는 **배열의 원소가 함수일 수 없다.**배열 원소는 반드시 **객체 타입(object type)** 이어야 하는데, 함수는 객체가 아니다. 따라서 **“함수들의 배열” 선언은 불가능**하다.



## Pointer Exercise

```c
#include <stdio.h>

int main(void) {
    int A1[3] = {1, 2, 3};
    int *A2[3];
    int arr[3] = {10, 20, 30};
    int (*A3)[3] = &arr;

    // === An ===
    A1;                                  // 1. A1 컴파일 여부
    int x1 = A1[0];                      // 2. A1 런타임 접근
    printf("%zu\n", sizeof(A1));         // 3. A1 sizeof

    A2;                                  // 4. A2 컴파일 여부
    int *p2 = A2[0];                     // 5. A2 런타임 접근 (미초기화 시 위험)
    printf("%zu\n", sizeof(A2));         // 6. A2 sizeof

    A3;                                  // 7. A3 컴파일 여부
    int (*p3)[3] = A3;                   // 8. A3 런타임 접근
    printf("%zu\n", sizeof(A3));         // 9. A3 sizeof

    // === *An ===
    *A1;                                 // 10. *A1 컴파일 여부
    int x4 = *A1;                        // 11. *A1 런타임 접근
    printf("%zu\n", sizeof(*A1));        // 12. *A1 sizeof

    *A2;                                 // 13. *A2 컴파일 여부
    int *p4 = *A2;                       // 14. *A2 런타임 접근
    printf("%zu\n", sizeof(*A2));        // 15. *A2 sizeof

    *A3;                                 // 16. *A3 컴파일 여부
    int x5 = (*A3)[0];                   // 17. *A3 런타임 접근
    printf("%zu\n", sizeof(*A3));        // 18. *A3 sizeof

    // === **An ===
    **A1;                                // 19. **A1 컴파일 여부 (컴파일 에러)
    int x6 = **A1;                       // 20. **A1 런타임 접근 (불가능)
    printf("%zu\n", sizeof(**A1));       // 21. **A1 sizeof (불가능)

    **A2;                                // 22. **A2 컴파일 여부
    int x7 = **A2;                       // 23. **A2 런타임 접근 (미초기화 시 위험)
    printf("%zu\n", sizeof(**A2));       // 24. **A2 sizeof

    **A3;                                // 25. **A3 컴파일 여부
    int x8 = **A3;                       // 26. **A3 런타임 접근
    printf("%zu\n", sizeof(**A3));       // 27. **A3 sizeof

    return 0;
}

```

위와 같이 3개의 변수를 선언했을 때 다음 표를 채워보자.

|              |          |                  An                  |        |          |                 *An                  |        |          |                 **An                 |        |
| :----------: | :------: | :----------------------------------: | :----: | :------: | :----------------------------------: | :----: | :------: | :----------------------------------: | :----: |
|              | Compiles | Potential runtime error in accessing | sizeof | Compiles | Potential runtime error in accessing | sizeof | Compiles | Potential runtime error in accessing | sizeof |
|  int A1[3]   |    O     |                  X                   |   12   |          |                                      |        |          |                                      |        |
|  int *A2[3]  |          |                                      |        |          |                                      |        |          |                                      |        |
| int (*A3)[3] |          |                                      |        |          |                                      |        |          |                                      |        |















