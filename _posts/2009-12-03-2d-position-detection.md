---
layout: post
title: "2D position detect method"
date: 2009-12-03
category: ["science", "computer", "microscope", "physics"]
author: "Sung-Cheol Kim"

---

어제 찬우랑 식사중에 이야기를 듣고서 좋은 아이디어가 생각이 났다. 결국 2D image상의 패턴에서 위치를 찾아내는 함수는 이상적인 function을 만들고 그것을 2D상에서 이리저리 굴려서 가장 실제 결과에 가까운 함수를 찾아내면 되는 것이다. 이 경우 위치뿐만이 아니라 radius의 관한 정보도 얻을수 있게 된다. 즉

$$ Variation = Integral(|I(x,y) – airydisc(x,y;x_0, y_0, r)|^2) $$

을 구해서 이 값이 최소가 되는 airy disc를 찾아내면 그 함수로부터 x_0, y_0와 r을 구할수 있게 된다.

하지만 이 경우 다음과 같은 어려움이 있다. 첫번째는 우리는 위의 세가지 변수(x_0, y_0, r)에 의존하는 functional을 다루어야 하고 이 각각의 함수에 대해서 Variation을 계산해야 하고 그 최소값은 찾아야 한다. matlab에는 강력한 함수들이 있는데 그중 fitting을 위한 함수중 내가 사용할수 있는 것이 있을 것이다.

또 다른 문제로는 focus에 따라 결과값의 pattern이 달라진다는 것이다. 가장 좋은 focus일때에는 airy disc로 근사할수 있도록 1번째 밝은 링과 1번째 어두운 링이 보이지만 focus가 맞지 않게 되면 그냥 어두운 링 혹은 밝은 점, 어두운 링등의 다른 pattern이 나타나 일치시키는 ideal한 함수가 airy disc가 아니게 된다. 우리 실험의 경우 bead의 크기가 1um정도인데, glass slide로 인해 만들어지는 공간의 크기는 3~5 um 정도가 된다. 따라서 bead 가 2um 이상의 높이로 움직이게 되는데, 우리가 가지고 있는 60x objective lens의 경우 1um bead의 상단, 중단, 하단의 경우 각각 다른 pattern을 보여주기때문에 움직이는 bead의 경우 이 문제를 피할 수 없게 된다. 우선은 고정된 bead에 의한 그리고 최적의 focus인 경우로 한정해서 문제를 생각하자. 지금 파악하고자 하는 것은 내 시스템 자체가 가지고 있는 error 가 어느정이 인가이다.
