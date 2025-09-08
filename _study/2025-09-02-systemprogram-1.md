---
title: "[System Programming] 01 Intro"
date: 2025-09-02
permalink: /study/2025-09-02-systemprogram-1
categories: SystemProgramming
tags: 
  - SystemProgramming


---

In this post, 01 System Programming lecture is introuduced. 



# C

- **Dennis Ritchie** is a creator of C and Unix.

- C 코드를 컴파일시, gcc 대신 gcc800을 많이 사용한다.

  ```shell
  gcc800 hello.c // gcc -Wall -Werror - pedantic -std=c99 와 동치
  ```

  gcc800은 다음 기능을 하는 매크로이다.

  - `-Wall` : 모든 일반적인 경고 메시지 출력
  - `-Werror` : 경고를 오류로 취급 (컴파일 실패)
  - `-pedantic` : C 표준에 맞지 않는 확장 사용 시 경고/에러
  - `-std=c99` : C 표준을 C99 모드로 설정

  gcc를 사용하면 여러 프로그램들이 순차적으로 실행되고 가장 먼저 **Preprocessor**가 실행된다. #으로 시작하는 모든 구문을 처리한다. Preprocess의 output은 여전히 C 소스코드이다. 이후, C 컴파일러가 실행된다. 

  
  
  ## Constant
  
  C에서 Constant는 아래의 세 가지 방법으로 만들 수 있다. 
  
  ```c
  #define MAX 10
  const int MAX = 10;
  enum {MAX = 10};
  ```
  
  
  
  ## sizeof
  
  sizeof는 함수가 아니라 C에서 정의된 연산자로, 컴파일 타임에 계산된다.
  
  ```c
  double pi[5][2];
  sizeof(pi); // 8*5*2=80bytes
  int *p;
  void *k;
  sizeof(p); // 8
  sizeof(*p); // 4
  sizeof(k); // 8
  sizeof(*k); // compile error
  ```
  
  
  
  ## String
  
  C에서 문자열은 collection of characters 로 만든다. 이 때, char 형 포인터 변수를 이용하여 만드는 방법과 char 형 배열을 이용하여 만드는 방법이 있는데 메모리와 값의 변경 가능 여부에 대한 차이는 <a href="https://arcstone09.github.io/study/2025-09-03-java-5"> 여기 </a>를 참고.
  
  문자열에 대해서, `sizeof`는 `\0`을 포함한 크기를 나타내고, `strlen` 은 `\0` 을 제외한 길이를 반환한다.
  
  ```c
  char *s = "hello world\n";
  char k[20] = "SNU CSE00800";
  sizeof(s) // 8
  strlen(s) // 12
  sizeof(k) // 20
  strlen(k) // 12
  ```
  
  
  
  ## Assignment
  
  expression 은 값을 evaluation 한다. 대입 연산자 = 도 expression으로써, 값을 저장하는 효과와 더불어 그 값을 evaluation 값으로 가진다. 
  
  ```c
  int i = 0;
  int j = 1;
  i = j = 2; // i==2, j==2
  ```
  
  위 예제에서 먼저 j는 2로 설정되고 그 evaluation 값 2가 i에 대입된다\.
  
  
