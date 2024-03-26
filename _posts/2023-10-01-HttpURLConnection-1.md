---
title: HttpURLConnection을 활용한 요청
permalink: /posts/2023/10/HttpURLConnection-1/
date: 2023-10-01
tags:
   - HttpURLConnection
   - 웹 통신
---

## HttpURLConnection이란?
   HttpURLConnection은 Java에서 제공하는 API로, 웹 서버와의 연결을 위해 사용되는 클래스입니다.<br>
   커피숍에 비유하자면, 바리스타에게 주문을 전달하고 그 주문에 따른 커피를 받아오는 과정입니다.<br> 
   여기서 주문은 HTTP 요청, 바리스타는 웹 서버, 받아오는 커피는 응답 데이터에 해당합니다.<br>

## HttpURLConnection 사용 이유
HttpURLConnection을 사용하는 주된 이유는 웹 서버와의 통신을 간결하게 구현할 수 있기 때문입니다.

먼저 도서관에 비유를 해보면, <br>
도서관에 가면 수많은 책들이 있지만, 우리가 원하는 책을 찾기 위해서는 카탈로그 시스템(데이터 개체들에 대한 정의나 명세에 대한 정보가 수록)을 사용합니다. 카탈로그는 도서관에 있는 모든 책의 정보를 담고 있으며, 특정 책의 제목, 저자, 출판일 등을 통해 그 책의 정확한 위치를 알 수 있습니다.

이처럼 HttpURLConnection도 웹의 광대한 정보 중에서 우리가 필요로 하는 특정 정보, 즉 웹 페이지나 API의 응답을 찾아 가져오는 도구입니다.

Java에서는 HttpURLConnection을 표준 라이브러리로 제공하므로, 별도의 외부 라이브러리나 프레임워크를 추가하지 않고도 HTTP 요청과 응답을 처리할 수 있습니다.

또한, HttpURLConnection은 다양한 HTTP 메소드 (GET, POST, PUT, DELETE 등)를 지원하므로, 다양한 유형의 웹 요청을 손쉽게 구현할 수 있습니다. 특히 웹 API와의 통신에서는 이러한 HTTP 메소드의 지원이 필수적입니다.

하지만, 모든 것에는 장단점이 있듯이 HttpURLConnection도 마찬가지입니다. 복잡한 웹 요청이나 헤더, 쿠키 등의 처리, 멀티스레드 환경에서의 최적화 등을 필요로 하는 경우에는 다른 라이브러리의 사용을 고려해볼 수도 있습니다.<br>
- HttpClient: Apache에서 제공하는 API. 멀티스레드 환경에 최적화된 성능을 자랑합니다.
- OkHttp: Square에서 제공하는 API. 효율성과 성능이 뛰어나며, 웹소켓 지원 등 다양한 기능을 포함하고 있습니다.

### HttpURLConnection 특징
   1. Java 표준 라이브러리에 포함되어 있습니다.
   2. GET, POST, PUT, DELETE 등의 HTTP 메소드를 지원합니다.
   3. 헤더나 파라미터를 쉽게 추가할 수 있습니다.

### 사용예시
도서관에서 책을 검색하는 프로세스로 예시를 들어보겠습니다.

1. A 프로젝트는 도서관의 데이터베이스에서 책 정보를 검색하는 API를 제공합니다.
2. B 프로젝트는 사용자에게 책의 제목을 입력받아 A 프로젝트에 검색 요청을 보내고 결과를 보여주는 웹 페이지를 제공합니다.

#### BookVO 

```java
public class BookVO {
  private String title;
  private String author;
  private String isbn;
  private String publishedDate;
  private String genre;

  public BookVO(String title, String author, String isbn, String publishedDate, String genre) {
    this.title = title;
    this.author = author;
    this.isbn = isbn;
    this.publishedDate = publishedDate;
    this.genre = genre;
  }

  public String getTitle() { 
      return title; 
  }
  public void setTitle(String title) {
      this.title = title; 
  }
  public String getAuthor() { 
      return author; 
  }
  public void setAuthor(String author) { 
      this.author = author; 
  }
  public String getIsbn() { 
      return isbn; 
  }
  public void setIsbn(String isbn) { 
      this.isbn = isbn; 
  }
  public String getPublishedDate() { 
      return publishedDate; 
  }
  public void setPublishedDate(String publishedDate) { 
      this.publishedDate = publishedDate; 
  }
  public String getGenre() { 
      return genre; 
  }
  public void setGenre(String genre) { 
      this.genre = genre; 
  }

  @Override
  public String toString() {
    return "BookVO{" +
      "title='" + title + '\'' +
      ", author='" + author + '\'' +
      ", isbn='" + isbn + '\'' +
      ", publishedDate='" + publishedDate + '\'' +
      ", genre='" + genre + '\'' +
      '}';
  }
}
```

#### A프로젝트

```java
@RestController
@RequestMapping("/library")
public class AProjectController {

    private final List<BookVO> books;

    @Autowired
    public AProjectController() {
        books = Arrays.asList(
            new BookVO("Effective Java", "조슈아 블로크", "1234567890", "2020-01-01", "Programming"),
            new BookVO("토비의 스프링", "토비", "0987654321", "2021-05-15", "Framework"),
            new BookVO("자바 알고리즘 인터뷰", "박상길", "1122334455", "2019-08-12", "Algorithm"),
            new BookVO("자바 객체지향의 원리와 이해", "김종민", "5566778899", "2022-02-20", "Framework")
        );
    }

    @GetMapping("/search")
    public ResponseEntity<List<BookVO>> searchBooks(@RequestParam String title) {
        List<BookVO> foundBooks = books.stream()
            .filter(book -> book.getTitle().toLowerCase().contains(title.toLowerCase()))
            .collect(Collectors.toList());
        
        return ResponseEntity.ok(foundBooks);
    }
}

```

#### B프로젝트 서비스
```java
@Service
public class BProjectService {

  private static final String A_PROJECT_API_URL = "http://A-project.com/library/search";

  public List<BookVO> searchBooksInLibraryByTitle(String title) {
    String encodedTitle = URLEncoder.encode(title, StandardCharsets.UTF_8);
    String finalUrl = A_PROJECT_API_URL + "?title=" + encodedTitle;
    return searchBooksInLibrary(finalUrl, "GET", null);
  }

  public List<BookVO> searchBooksInLibraryByAttributes(Books info) {
    Map<String, String> attributes = new HashMap<>();
    attributes.put("title", info.getTitle());
    attributes.put("author", info.getAuthor());
    attributes.put("isbn", info.getIsbn());
    attributes.put("publishedDate", info.getPublishedDate());
    attributes.put("genre", info.getGenre());
    return searchBooksInLibrary(A_PROJECT_API_URL, "POST", attributes);
  }

  private List<BookVO> searchBooksInLibrary(String url, String method, Map<String, String> attributes) {
    HttpURLConnection conn = null;
    List<BookVO> resultBooks = new ArrayList<>();

    try {
      URL apiUrl = new URL(url);
      conn = (HttpURLConnection) apiUrl.openConnection();
      conn.setConnectTimeout(10000);
      conn.setRequestMethod(method);

      if ("POST".equals(method) && attributes != null) {
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

        StringBuilder postData = new StringBuilder();
        for (Map.Entry<String, String> entry : attributes.entrySet()) {
          if (postData.length() != 0) postData.append('&');
          postData.append(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8));
          postData.append('=');
          postData.append(URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        }

        try (OutputStream os = conn.getOutputStream()) {
          os.write(postData.toString().getBytes(StandardCharsets.UTF_8));
        }
      }

      int responseCode = conn.getResponseCode();

      if (responseCode == HttpURLConnection.HTTP_OK) {
        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8));
        String inputLine;
        StringBuffer responseBuffer = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
          responseBuffer.append(inputLine);
        }
        in.close();

        String response = responseBuffer.toString();

        // JSON 응답에서 도서 목록을 파싱하는 로직
        Gson gson = new Gson();
        Type bookListType = new TypeToken<ArrayList<BookVO>>(){}.getType();
        resultBooks = gson.fromJson(response, bookListType);

      } else {
        throw new RequestAPIException(APIErrorMessage.API_REQUEST_FAILURE.getMessage());
      }
    } catch (Exception e) {
      throw new RequestAPIException(APIErrorMessage.API_REQUEST_FAILURE.getMessage(), e);
    } finally {
      if (conn != null) {
        conn.disconnect();
      }
    }
    return resultBooks;
  }
}

```

#### B프로젝트 컨트롤러
```java
@RestController
@RequestMapping("/bookSearch")
public class BProjectController {

  private final BProjectService service;

  @Autowired
  public BProjectController(BProjectService service) {
    this.service = service;
  }

  @GetMapping
  public String searchForm() {
    return "searchForm";  // 검색 폼 페이지 반환
  }

  @AuditLog(actionCode = EnumActionCode.SEARCH_BY_TITLE, menuCode = EnumMenuCode.SEARCH)
  @GetMapping("/result")
  public ResponseEntity<List<BookVO>> searchResultByTitle(@RequestParam String title) {
    List<BookVO> books = service.searchBooksInLibraryByTitle(title);
    if (books == null || books.isEmpty()) {
      return ResponseEntity.noContent().build();
    }
    return ResponseEntity.ok(books);
  }

  @AuditLog(actionCode = EnumActionCode.SEARCH_BY_ATTRIBUTES, menuCode = EnumMenuCode.SEARCH)
  @PostMapping("/result")
  public ResponseEntity<List<BookVO>> searchResultByAttributes(@ModelAttribute("actionForm") Books info) {
    List<BookVO> books = service.searchBooksInLibraryByAttributes(info);
    if (books == null || books.isEmpty()) {
      return ResponseEntity.noContent().build();
    }
    return ResponseEntity.ok(books);
  }
}

```


HttpURLConnection은 Java에서 웹 서버와의 통신을 위한 간단한 도구입니다.<br>
커피숍에서 원하는 커피를 주문하거나 도서관에서 원하는 책을 찾는 것처럼<br>
원하는 데이터를 웹 서버에 요청하고 결과를 받아올 수 있습니다.<br>