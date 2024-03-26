---
title: Clean code
permalink: /posts/2023/10/Clean-code/
date: 2023-10-23
tags:
  - clean code
---

## 좋은코드?<br>
"좋은 코드를 짜야한다" <br>

### 좋은 코드란 무엇인가?
코딩은 소프트웨어 개발의 핵심적인 부분이며, 좋은 코드를 작성하는 것은 프로그래머에게 <br>
가장 중요한 능력 중 하나입니다. 그렇다면, 좋은 코드란 무엇일까요? <br>
좋은 코드의 특성과 중요성에 대해 알아보겠습니다.<br>

로버트 C. 마틴(Robert C. Martin)의 저서 "Clean Code: A Handbook of Agile Software Craftsmanship"<br>
이 책에서는 클린 코드에 대한 그의 관점과 원칙을 자세히 설명하고 있습니다.<br>

다음은 책에서 강조하는 주요 포인트들입니다 <br>

#### 의미 있는 이름 사용 
 - 변수, 함수, 클래스 등의 이름은 해당 항목의 목적과 역할을 명확하게 전달해야 합니다.
#### 함수는 한 가지 일만 해야 한다
 - 함수는 가능한 작게 만들어야 하며, 그 이름이 하는 일을 정확하게 반영해야 합니다.<br>
#### 함수의 인자 개수를 최소화
 - 함수가 많은 인자를 가질수록 이해하기 어려워지며, 수정하기도 복잡해집니다.<br>
#### 주석은 나쁜 코드를 설명하는 데 사용되어서는 안 된다
 - 좋은 코드는 주석 없이도 그 목적을 명확하게 전달해야 합니다.<br>
#### 중복은 피해야 한다 
 - 중복된 코드는 수정이나 확장 시 에러의 원인이 될 수 있으므로, 중복을 최대한 줄여야 합니다.<br>
#### 클래스와 객체 지향 원칙을 따라야 한다
 -  SOLID 원칙 등의 객체 지향 설계 원칙을 따르면서 코드를 구조화해야 합니다.<br>
#### 에러 처리도 중요하다
 - 예외 처리는 별도의 함수나 클래스로 분리하여, 비즈니스 로직과 명확하게 분리해야 합니다.<br>
#### 코드는 항상 최신 상태로 유지해야 한다
 - 기존 코드를 수정하거나 추가할 때는 항상 최신 상태로 유지하며, 필요 없는 코드는 제거해야 합니다.<br>

책에 나와있는 내용을 정리해 본다면
일반적으로 말하는 '좋은 코드 (clean code)'는 아래의 특성을 담고 있습니다. <br>

[가독성]
- 코드는 사람(**프로젝트를 처음 보는 팀원, 다른프로젝트를 시작하면 까먹게될 나**)에게 읽히기 위해 작성되는 것입니다.
- 따라서 코드는 깔끔하고, 구조적이며, 읽기 쉬워야 합니다.
- 변수나 함수의 이름은 해당 기능을 잘 나타내야 하며, 주석도 적절히 사용해야 합니다.

[유지보수성]
- 작성된 코드는 추후에 변경이나 확장이 용이해야 합니다.
- 복잡한 로직은 함수나 클래스로 분리하여 모듈화하는 것이 중요합니다.

[성능]
- 코드가 빠르게 실행,동작되는 것도 중요하지만, 무작정 성능을 위해 최적화를 추구하는 것은 아닙니다.
- 가독성과 유지보수성을 희생하여 성능을 추구하는 것은 바람직하지 않습니다.

[재사용성]
- 중복되는 코드는 최대한 줄이고, 재사용 가능한 코드를 작성하는 것이 좋습니다.
- 이를 위해 라이브러리나 프레임워크의 활용도 고려해볼만 합니다.

[안정성]
- 작성된 코드는 예상치 못한 상황에서도 안정적으로 동작해야 합니다.
- 이를 위해 **에러 처리나 예외 처리** 등의 기법을 활용하는 것이 중요합니다.

[테스트 가능성]
- 코드는 테스트하기 쉬워야 합니다.

좋은 코드는 단순히 동작하는 코드가 아니라,<br>
다른 개발자와 협업하거나 코드를 유지보수할 때도 효과적으로 활용될 수 있는 코드입니다.<br>
따라서, 좋은 코드를 작성하는 능력은 프로그래머의 기술력 뿐만 아니라, <br>
커뮤니케이션 능력과 프로젝트 관리 능력 등 여러 가지 요소와 관련이 있습니다.

그렇다면, 좋은코드(clean code)가 적용되어있는 코드를 한번 알아보겠습니다.

``` java
/**
 * 제품명과 가격 정보를 포함하는 제품 클래스.
 */
public class Product {
    private String name;
    private int price;  // 가격은 센트 단위의 정수로 표현됩니다.

    /**
     * 제품 객체 생성자.
     *
     * @param name  제품명
     * @param price 제품의 가격 (원 단위)
     */
    public Product(String name, int price) {
        this.name = name;
        this.price = price;
    }

    /**
     * 제품명을 반환합니다.
     *
     * @return 제품명
     */
    public String getName() {
        return name;
    }

    /**
     * 제품의 가격을 반환합니다.
     *
     * @return 제품 가격 (원 단위)
     */
    public int getPrice() {
        return price;
    }
}
```

``` java
/**
 * 제품 주문 정보를 관리하는 주문 클래스.
 */
public class Order {
    private List<Product> items = new ArrayList<>();
    private int total = 0;  // 총 가격은 원 단위의 정수로 표현됩니다.

    /**
     * 제품을 주문 목록에 추가합니다.
     *
     * @param product  주문할 제품
     * @param quantity 주문할 제품의 수량
     * @throws IllegalArgumentException 수량이 0 이하일 경우 발생
     */
    public void addProduct(Product product, int quantity) {
        if (quantity <= 0) {
            throw new IllegalArgumentException("수량은 0보다 커야 합니다.");
        }

        for (int i = 0; i < quantity; i++) {
            items.add(product);
            total += product.getPrice();
        }
    }

    /**
     * 주문 목록에서 특정 제품을 제거합니다.
     *
     * @param productName 제거할 제품의 이름
     * @throws IllegalArgumentException 주문 목록에 제품이 없을 경우 발생
     */
    public void removeProduct(String productName) {
        boolean productFound = false;

        Iterator<Product> iterator = items.iterator();
        while (iterator.hasNext()) {
            Product product = iterator.next();
            if (product.getName().equals(productName)) {
                total -= product.getPrice();
                iterator.remove();
                productFound = true;
            }
        }

        if (!productFound) {
            throw new IllegalArgumentException("주문 목록에 해당 제품이 없습니다.");
        }
    }

    /**
     * 주문의 총 가격을 반환합니다.
     *
     * @return 총 가격 (원 단위)
     */
    public int getTotalPrice() {
        return total;
    }
}

```

``` java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Order 클래스의 기능을 테스트하는 테스트 클래스입니다.
 */
public class OrderTest {
    private Product apple;
    private Product banana;
    private Order order;

    /**
     * 각 테스트 전에 공통으로 사용할 데이터를 설정합니다.
     */
    @BeforeEach
    public void setUp() {
        apple = new Product("Apple", 50);  // 50센트
        banana = new Product("Banana", 25);  // 25센트
        order = new Order();
    }

    /**
     * 제품 추가와 제거 기능을 테스트합니다.
     */
    @Test
    public void testAddAndRemoveProduct() {
        order.addProduct(apple, 4);
        order.addProduct(banana, 3);
        assertEquals(275, order.getTotalPrice());

        order.removeProduct("Apple");
        assertEquals(75, order.getTotalPrice());
    }

    /**
     * 잘못된 수량으로 제품을 추가하는 경우를 테스트합니다.
     */
    @Test
    public void testInvalidAddProduct() {
        assertThrows(IllegalArgumentException.class, () -> {
            order.addProduct(apple, -1);
        });
    }

    /**
     * 주문 목록에 없는 제품을 제거하려는 경우를 테스트합니다.
     */
    @Test
    public void testInvalidRemoveProduct() {
        assertThrows(IllegalArgumentException.class, () -> {
            order.removeProduct("Orange");
        });
    }
}
```
### 클린 코드의 특성
의미 있는 이름 사용: 
 - Product, Order, addProduct, removeProduct와 같은 이름은 해당 기능을 명확하게 표현합니다. 
 - 이름만 보더라도 각 메서드와 클래스의 역할을 알 수 있습니다.

함수는 한 가지 일만 해야 한다:
- addProduct는 제품을 추가하는 일만 하며, removeProduct는 제품을 제거하는 일만 합니다. 
- 각 함수는 명확한 하나의 책임을 가지고 있습니다.

예외 처리: 
- 수량이 0 이하일 때나 주문 목록에 없는 제품을 제거하려 할 때와 같은
- 예외 상황을 대비하여 예외 처리를 통해 명확한 에러 메시지를 제공합니다.

주석 사용: 
- 각 클래스와 메서드에는 그 기능을 설명하는 주석이 추가되어 있습니다. 
- 주석은 코드의 의도와 기능을 명확하게 전달하기 위해 사용되었습니다.

코드의 중복 최소화:
- 코드 내에서 중복되는 로직은 없습니다. 
- 중복을 최소화하여 유지보수가 용이하도록 했습니다.


### 마치며..
좋은 코드를 작성하는 능력은 오늘의 작업을 효과적으로 만드는 것뿐만 아니라,<br>
미래의 유지보수와 협업을 원활하게 만듭니다.

클린 코드의 원칙을 따르면서 개발을 진행하면, 처음에는 시간이 좀 더 걸릴 수도 있습니다. <br>
하지만 그 결과로 얻는 메리트는 큽니다.<br> 

좋은 코드는 시간과 경험을 통해 계속해서 발전해 나갈 수 있습니다.<br> 

제가 생각하는 좋은 코드(clean code)는<br>
**프로그래밍이라는 하드 스킬에 커뮤니케이션이라는 소프트스킬을 결합한 형태**가 아닐까 합니다.

