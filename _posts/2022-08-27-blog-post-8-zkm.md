---
title: 'Markdwon转义字符语法'
date: 2022-08-27
permalink: /posts/2022/08/markdown-8-zkm/
tags:
  - cool posts
  - markdown
  - 转义字符
---

要显示原本用于格式化Markdown文档的字符，请在字符前面添加反斜杠字符`\`。  
```
\* 优秀的人 总能看到比自己更好的；而平庸的人 总能看到比自己更差的。
```
渲染效果如下：   

\* 优秀的人 总能看到比自己更好的；而平庸的人 总能看到比自己更差的。

# 可转义的字符  
|字符|名称|
|---|---|
|\\ | backslash|
|\` | backtick|
|\* | asterisk|
|\_ | underscore|
|\{\} | curly braces|
|\[\] | bracets|
|\(\) | parentheses|
|\# | pound sign|
|\+ | plus sign|
|\- | minus sign (hyphen)|
|\. | dot|
|\! | exclamation mark|
|\| | pipe|

# 自动转义字符  
Markdown允许你直接使用`<`和`&`，帮你自动转义字符。如果你使用`&`符号的作为HTML实体的一部分，那么它不会被转换，而在其他情况下，它则会被转换成`&amp;`。所以你如果要在文件中插入一个著作权的符号，可以这样写： 
```
&copy;usst
```
显示效果为：  
&copy;usst

