---
title: "Raspberry PiのGPIOをデジタル入出力できる回路シミュレータ"
excerpt: "高専での教育実習の一環で作った"
collection: portfolio
---

[Access from here](https://github.com/getpa/CircuitJs-GPIOModwithWebIOPi)

# なにこれ
Raspberry Pi 4のGPIOをデジタル入出力として利用し，CircuitJsのシミュレーションと連動させることのできるシステムです．

## 開発動機
豊田高専での実務訓練の一環として，2年生向けの工学実験のテーマを2週分担当させていただきました．
このとき，論理回路を実現するテーマをメインに考えていました．
しかし，大規模な論理回路をブレッドボード上に実現させるのは難しいし，かといって小さくても面白みがないと考えました．

豊田高専 情報工学科の2年生は，（2023年現在）全員がRaspberry Piを所持しています．
また，CircuitJsを使った回路シミュレーションを学科でやったことがあるという話でした．
これは回路シミュレーションと実機とを組み合わせたら面白そうだ，と考えて色々調べてみたのですが，自分の調べた範囲ではそういったソフトウェアは発見できませんでした．

ならばと，自分でチョチョイと作ってみたものがこちらです．

# 実験資料からの抜粋

{% for filename in (1..9)%}
<img src="{{ s.image | prepend: "/images/" | prepend: base_path }}.jpg" />
{% endfor %}

# 実装したところ
[index.html](https://github.com/getpa/CircuitJs-GPIOModwithWebIOPi/blob/main/htdocs/index.html)と，[main.js](https://github.com/getpa/CircuitJs-GPIOModwithWebIOPi/blob/main/htdocs/main.js)だけです．
そのほかのコードは借り物です．

# 杜撰なところ
WebIOPi APIにPollingしているので，激おもです．
そもそも，CircuitJsはJavaで書かれたシミュレータのJS移植版ですし，まともな実装をするなら，JavaでRaspberry PiのGPIOを直接制御するようにCircuitJsのオリジナルJava版をmodifyするべきな気がします．
Javaで書く方針なら，もしかするとアナログインプットやPWMもうまく使えるかもしれません．
しらんけど．