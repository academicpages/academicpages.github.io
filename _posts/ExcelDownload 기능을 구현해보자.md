---
title: ExcelDownload 기능을 구현해보자
format: list
date: 2023-08-10
tags:
  - Excel
  - Apache POI
---

Apache POI 라이브러리를 활용해서 <br>
Excel파일을 다운로드 받는 기능을 요구사항을 하나씩 추가해가며 만들어보자!!

요구사항
0. 현재 통계표에 있는 내용을 엑셀로 다운받아서 보고 싶어요.
1. 엑셀을 다운받는 기능을 만들어주세요.
2. 웹 페이지에서 엑셀을 다운 받을 수 있게 해주세요.
3. 엑셀에는 일별, 월별, 년별 통계가 표기되어있어야해요.
4. 권한에따라 엑셀을 다운받는 기능이 추가되어야해요.
5. 권한에따라 엑셀에 쌓이는 통계데이터에 마스킹 처리가 필요해요.
6. 다운받는 엑셀에 비밀번호를 걸고싶어요.

### Maven Dependency 추가

``` java
<!-- Apache POI dependencies -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.0.0</version>
</dependency>

```

### 1. Model 생성

```java
public class Statistics {
  private Date date;
  private Integer dailyCount;
  private Integer monthlyCount;
  private Integer yearlyCount;

  public Statistics(Date date, Integer dailyCount, Integer monthlyCount, Integer yearlyCount) {
    this.date = date;
    this.dailyCount = dailyCount;
    this.monthlyCount = monthlyCount;
    this.yearlyCount = yearlyCount;
  }

  // Getter methods
  public Date getDate() {
    return date;
  }

  public Integer getDailyCount() {
    return dailyCount;
  }

  public Integer getMonthlyCount() {
    return monthlyCount;
  }

  public Integer getYearlyCount() {
    return yearlyCount;
  }

  // Setter methods
  public void setDate(Date date) {
    this.date = date;
  }

  public void setDailyCount(Integer dailyCount) {
    this.dailyCount = dailyCount;
  }

  public void setMonthlyCount(Integer monthlyCount) {
    this.monthlyCount = monthlyCount;
  }

  public void setYearlyCount(Integer yearlyCount) {
    this.yearlyCount = yearlyCount;
  }
}

```

### 2. Controller 생성
* 요구사항 1, 2 : 웹 페이지에서 사용자의 권한을 기반으로 엑셀 파일을 다운로드하는 기능

```java

@RestController
@RequestMapping("/statistics")
public class StatisticController {

  @Autowired
  private ExcelGenerator excelGenerator;

  /**
   * 주어진 사용자 권한에 따라 엑셀 형식의 통계를 다운로드합니다.
   * @param role 사용자 권한
   * @return 엑셀 파일 응답
   */
  @GetMapping("/download")
  public ResponseEntity<ByteArrayResource> downloadExcel(@RequestParam String role) {
    XSSFWorkbook workbook = excelGenerator.generateExcelForRole(role);
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    workbook.write(out);
    ByteArrayResource resource = new ByteArrayResource(out.toByteArray());

    return ResponseEntity.ok()
      .header(HttpHeaders.CONTENT_DISPOSITION, "attachment;filename=statistics.xlsx")
      .contentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
      .body(resource);

  }
}
```

### 3.Service 생성
* 요구사항 3: 엑셀에는 일별, 월별, 년별 통계가 표기됩니다.
* 요구사항 4: 사용자의 권한에 따라 엑셀 파일을 생성합니다.
* 요구사항 5: 'USER' 권한인 경우 민감한 데이터는 마스킹 처리됩니다.
* 요구사항 6: ADMIN 권한을 가진 사용자의 경우, 생성된 엑셀 파일에 비밀번호를 설정합니다.

```java

@Service
public class ExcelGenerator {

  @Autowired
  private StatisticService statisticService;

  /**
   * 주어진 사용자 권한에 따라 엑셀 워크북을 생성합니다.
   * @param role 사용자 권한
   * @return 생성된 엑셀 워크북
   */
  public XSSFWorkbook generateExcelForRole(String role) {
    XSSFWorkbook workbook = new XSSFWorkbook();
    XSSFSheet sheet = workbook.createSheet("Statistics");

    createHeaderRow(sheet);

    populateDataRows(sheet, role);

    // Set password protection
    if ("ADMIN".equals(role)) {
      sheet.protectSheet("adminPassword");
    }

    return workbook;
  }

  /**
   * 엑셀 시트에 헤더 행을 생성합니다.
   * @param sheet 통계 데이터를 포함할 엑셀 시트
   */
  private void createHeaderRow(XSSFSheet sheet) {
    XSSFRow headerRow = sheet.createRow(0);
    headerRow.createCell(0).setCellValue("Date");
    headerRow.createCell(1).setCellValue("Daily Count");
    headerRow.createCell(2).setCellValue("Monthly Count");
    headerRow.createCell(3).setCellValue("Yearly Count");
  }

  /**
   * 통계 데이터와 사용자 권한을 기반으로 엑셀 시트에 데이터 행을 채웁니다.
   * @param sheet 데이터를 채울 엑셀 시트
   * @param role 사용자 권한
   */
  private void populateDataRows(XSSFSheet sheet, String role) {
    List<Statistics> statistics = statisticService.getStatistics();
    int rowIndex = 1;
    for (Statistics stat : statistics) {
      XSSFRow row = sheet.createRow(rowIndex++);
      populateRowWithStatistics(row, stat, role);
    }
  }

  /**
   * 주어진 통계 데이터와 사용자 권한에 따라 엑셀 행에 데이터를 채웁니다.
   * 'USER' 권한인 경우 민감한 데이터는 마스킹 처리됩니다.
   * @param row 데이터를 채울 엑셀 행
   * @param stat 통계 데이터
   * @param role 사용자 권한
   */
  private void populateRowWithStatistics(XSSFRow row, Statistics stat, String role) {
    row.createCell(0).setCellValue(stat.getDate().toString());
    row.createCell(1).setCellValue(stat.getDailyCount());

    if (isNotUser(role)) {
      row.createCell(2).setCellValue(stat.getMonthlyCount());
      row.createCell(3).setCellValue(stat.getYearlyCount());
    } else {
      maskSensitiveData(row);
    }
  }

  /**
   * 사용자의 권한이 'USER'가 아닌지 확인합니다.
   * @param role 사용자 권한
   * @return 'USER'가 아니면 true, 그렇지 않으면 false
   */
  private boolean isNotUser(String role) {
    return !"USER".equals(role);
  }

  /**
   * 민감한 데이터를 마스킹 처리합니다. (N/A로 표시)
   * @param row 마스킹 처리할 엑셀 행
   */
  private void maskSensitiveData(XSSFRow row) {
    row.createCell(2).setCellValue("N/A");
    row.createCell(3).setCellValue("N/A");
  }
}

```


### Excel 출력 예시:

**'USER' 권한의 경우:**

|    Date    | Daily Count | Monthly Count | Yearly Count |
|:----------:|-------------|---------------|--------------|
| 2023-10-01 | 120         | N/A           | N/A          |
| 2023-10-02 | 130         | N/A           | N/A          |
| 2023-10-03 | 125         | N/A           | N/A          |
|    ...     | ...         | ...           | ...          |

> **Note:** 'USER' 권한의 경우, 'Monthly Count'와 'Yearly Count' 열의 데이터는 'N/A'로 마스킹 처리되어 있습니다.

**'ADMIN' 또는 'USER'가 아닌 다른 권한의 경우:**

|    Date    | Daily Count | Monthly Count | Yearly Count |
|:----------:|-------------|---------------|--------------|
| 2023-10-01 | 120         | 3500          | 42000        |
| 2023-10-02 | 130         | 3600          | 43500        |
| 2023-10-03 | 125         | 3550          | 43000        |
|    ...     | ...         | ...           | ...          |

> **Note:** 'ADMIN' 또는 'USER'가 아닌 권한의 경우, 모든 열의 데이터가 그대로 표시됩니다.


Apache POI를 사용하여 웹 페이지에서 Excel 파일을 다운로드하는 기능 요구사항에 맞추어 개발해보았습니다.👏👏👏<br>




