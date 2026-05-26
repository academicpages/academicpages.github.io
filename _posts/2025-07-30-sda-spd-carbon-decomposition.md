---
title: "SDA 与 SPD：基于投入产出表的碳排放变化测算"
date: 2025-07-30
permalink: /posts/2025/07/sda-spd-carbon-decomposition/
tags:
  - 投入产出
  - 结构分解分析
  - 结构路径分解
  - 碳排放
  - MATLAB
excerpt: "本文整理一个基于投入产出表和部门碳排放强度的 SDA 与 SPD 测算项目，说明模型设定、数据结构、MATLAB 代码流程和结果输出。"
---

这篇笔记整理自一个投入产出测算项目，目标是用部门投入产出表和碳排放强度数据，分解 2002 年到 2020 年碳排放变化的来源，并进一步把变化量拆解到不同生产层级和产业链路径上。

项目完整代码包可以下载：[sda-spd-code-20250730.zip]({{ "/files/sda-spd-code-20250730.zip" | relative_url }})

项目结构
======

项目的核心目录是 `code/`，其中包含输入数据、计算脚本和输出结果：

| 文件或目录 | 内容 |
|---|---|
| `code/main20250730.m` | 主程序，设置年份、部门数、输入目录，并调用 SDA/SPD 计算函数 |
| `code/source/IOT.xlsx` | 投入产出表，包含 2002、2005、2007、2010、2012、2015、2017、2018、2020 年数据 |
| `code/source/强度.xlsx` | 11 个部门在各年份的碳排放强度 |
| `code/import_ciot.m` | 读取投入产出表中的中间投入、最终需求、进出口、误差项、总产出和增加值 |
| `code/import_eco.m` | 读取部门碳排放强度 |
| `code/caculate_sda.m` | 计算部门层面的结构分解分析结果 |
| `code/caculate_spd.m` | 计算不同生产层级的结构路径分解结果 |
| `code/caculate_spd_detail_nonF.m` | 展开到具体产业链路径，不区分最终需求类别 |
| `code/caculate_spd_detail_f.m` | 展开到具体产业链路径，并区分消费、投资和净出口 |
| `code/output/输出结果.xlsx` | 汇总输出，包含 `SDA` 和 `SPD` 两个工作表 |
| `code/output/SPD_path2002年-2020年.csv` | 具体路径层面的 SPD 输出 |
| `code/output/SPDf_path2002年-2020年.csv` | 区分最终需求类别的路径层面 SPD 输出 |

主程序中设定部门数为 11 个，年份序列为：

```matlab
pre.year = [2002,2005,2007,2010,2012,2015,2017,2018,2020];
pre.year_p = [2002,2020];
pre.N = 11;
```

其中 `pre.year_p` 是本次分解的起止年份。如果希望做分阶段分解，可以把它改成相邻年份或多个节点，例如 `[2002,2005,2007,2010,2012,2015,2017,2018,2020]`。

模型设定
======

投入产出模型从基本关系开始：

$$
X = AX + F
$$

其中，\(X\) 为总产出向量，\(A\) 为直接消耗系数矩阵，\(F\) 为最终需求。由此可以得到 Leontief 逆矩阵：

$$
L=(I-A)^{-1}
$$

在代码中，直接消耗系数矩阵通过中间投入矩阵 \(Z\) 和总产出 \(X\) 得到：

```matlab
X_hat = 1./IO.X;
A = IO.Z*diag(X_hat);
I = eye(N);
L = (I-A)\I;
```

本项目实际运行的 SDA/SPD 测算采用四因素分解。碳排放可以写成：

$$
Q = C L U H
$$

其中：

| 符号 | 含义 | 代码变量 |
|---|---|---|
| \(C\) | 部门碳排放强度 | `EC` 或 `diag(EC)` |
| \(L\) | Leontief 逆矩阵或生产层级矩阵 | `L` |
| \(U\) | 最终需求结构 | `Y1 = F./sum(F,1)` |
| \(H\) | 最终需求规模 | `Y2 = sum(F,1)` |

SDA：四因素结构分解
======

SDA 用于回答一个总体问题：从基期到报告期，碳排放变化究竟来自排放强度变化、产业关联变化、最终需求结构变化，还是最终需求规模变化？

设基期为 \(0\)，报告期为 \(t\)，则四个效应分别为：

$$
\Delta Q = D_C + D_L + D_U + D_H
$$

代码采用两极分解法，也就是将“以报告期为权重”和“以基期为权重”的两种分解结果取平均。例如排放强度效应为：

$$
D_C = \frac{1}{2}
\left[
(C^t-C^0)L^tU^tH^t
+
(C^t-C^0)L^0U^0H^0
\right]
$$

其余三项类似：

$$
D_L = \frac{1}{2}
\left[
C^0(L^t-L^0)U^tH^t
+
C^t(L^t-L^0)U^0H^0
\right]
$$

$$
D_U = \frac{1}{2}
\left[
C^0L^0(U^t-U^0)H^t
+
C^tL^t(U^t-U^0)H^0
\right]
$$

$$
D_H = \frac{1}{2}
\left[
C^0L^0U^0(H^t-H^0)
+
C^tL^tU^t(H^t-H^0)
\right]
$$

在 `caculate_sda.m` 中，这四项对应 `D1` 到 `D4`：

```matlab
D1 = 1/2*((S1{2}-S1{1})*S2{2}*S3{2}*S4{2}+...
    (S1{2}-S1{1})*S2{1}*S3{1}*S4{1});

D2 = 1/2*(S1{1}*(S2{2}-S2{1})*S3{2}*S4{2}+...
    S1{2}*(S2{2}-S2{1})*S3{1}*S4{1});

D3 = 1/2*(S1{1}*S2{1}*(S3{2}-S3{1})*S4{2}+...
    S1{2}*S2{2}*(S3{2}-S3{1})*S4{1});

D4 = 1/2*(S1{1}*S2{1}*S3{1}*(S4{2}-S4{1})+...
    S1{2}*S2{2}*S3{2}*(S4{2}-S4{1}));
```

输出表中的 `效应1` 到 `效应4` 分别对应：

| 输出列 | 含义 |
|---|---|
| `效应1` | 排放强度效应 |
| `效应2` | 产业结构或投入产出关联效应 |
| `效应3` | 最终需求结构效应 |
| `效应4` | 最终需求规模效应 |

SPD：把变化量拆到生产层级
======

结构路径分解（Structural Path Decomposition, SPD）把 SDA 与结构路径分析结合起来。其关键是利用 Leontief 逆矩阵的级数展开：

$$
L=(I-A)^{-1}=I+A+A^2+A^3+\cdots
$$

其中：

| 层级 | 解释 |
|---|---|
| \(I\) 或 \(A^0\) | 直接满足最终需求的生产 |
| \(A^1\) | 第一轮中间投入 |
| \(A^2\) | 第二轮中间投入 |
| \(A^3\) 及以上 | 更长的产业链间接路径 |

在 `caculate_spd.m` 中，程序计算 \(A^0\) 到 \(A^8\)，并额外计算完整 Leontief 逆矩阵 `L-all`：

```matlab
exponential = 0:8;

for n = 1:ne
    if n==ne
        I = eye(N);
        L = I/(I-A);      % L-all
    else
        L = A^(exponential(n));
    end

    Y1 = F./sum(F,1);
    Y2 = sum(F,1);
    S1{t}=EC';
    S2{t}=L;
    S3{t}=Y1;
    S4{t}=Y2';
end
```

这样可以比较不同生产层级对碳排放变化的贡献。例如 `SPD` 工作表中的 `L-0`、`L-1`、`L-2` 等行，分别表示不同层级的四个效应；`L-all` 表示完整产业链关联下的总分解结果。

具体路径展开
======

在总层级之外，项目还进一步展开具体产业链路径。`caculate_spd_detail_nonF.m` 计算不区分最终需求类别的路径贡献，输出格式为：

| 字段 | 含义 |
|---|---|
| `L-0` 到 `L-3` | 路径上的部门编号；未使用的位置记为 0 |
| `效应1` 到 `效应4` | 该路径对应的四个分解效应 |

例如 `L-0=1, L-1=2, L-2=3, L-3=0` 可以理解为一条展开到第二轮中间投入的路径。

核心做法是把某一条路径对应的矩阵元素保留下来，其余位置置零，再调用同一个 SDA 子函数：

```matlab
for n1 = 1:N
    for n2 = 1:N
        for n3 = 1:N
            L2{1} = zeros(N);
            L2{2} = zeros(N);
            L2{1}(n1,n2) = S2{1}(n1,n2)*S2{1}(n2,n3);
            L2{2}(n1,n2) = S2{2}(n1,n2)*S2{2}(n2,n3);
            sda = sub_c_sda(S1,L2,S3,S4);
        end
    end
end
```

`caculate_spd_detail_f.m` 则在路径之外继续区分最终需求类别。代码先把原始最终需求合并为三类：

```matlab
M_m = zeros(6,3);
M_m(1:3,1) = 1;   % 消费类需求
M_m(4:5,2) = 1;   % 投资类需求
M_m(6,3) = 1;     % 净出口
F = F0*M_m;
```

因此 `SPDf_path2002年-2020年.csv` 比普通路径输出多了一个 `f` 字段：

| `f` | 含义 |
|---|---|
| 1 | 消费类最终需求 |
| 2 | 投资类最终需求 |
| 3 | 净出口 |

主程序
======

整个测算由 `main20250730.m` 串联。运行前需要把工作路径切换到 `code/` 目录：

```matlab
% 该程序用于SDA和SPD的函数实例
cd("E:\Work\20250729\code");
clc; clear; close all;

pre = struct;
pre.year = [2002,2005,2007,2010,2012,2015,2017,2018,2020];
pre.year_p = [2002,2020];
pre.folder = "source";
pre.N = 11;

IOT = import_ciot(pre);
ECO = import_eco(pre);

SDA = caculate_sda(IOT,ECO,pre);
SPD = caculate_spd(IOT,ECO,pre);
SPD_detail = caculate_spd_detail_nonF(IOT,ECO,pre);
SPD_detail_f = caculate_spd_detail_f(IOT,ECO,pre);

outshow(SDA,SPD,SPD_detail,SPD_detail_f,pre)
```

如果迁移到其他电脑，建议把第一行路径改成项目相对路径，或者在 MATLAB 当前目录中打开 `code/` 后直接运行主程序。

结果输出
======

运行完成后，`outshow.m` 会写出三类结果：

```matlab
file_out = fullfile("output","输出结果.xlsx");
writecell(SDA_all,file_out,"Sheet","SDA");
writecell(SPD_all,file_out,"Sheet","SPD");

writecell(Tab,fullfile("output",strcat("SPD_path",str_1,".csv")));
writecell(Tab,fullfile("output",strcat("SPDf_path",str_1,".csv")));
```

结果文件可以这样理解：

| 输出文件 | 适合回答的问题 |
|---|---|
| `输出结果.xlsx` 的 `SDA` sheet | 哪些部门的碳排放变化主要来自强度、产业结构、需求结构或需求规模？ |
| `输出结果.xlsx` 的 `SPD` sheet | 哪些生产层级对碳排放变化贡献更大？ |
| `SPD_path2002年-2020年.csv` | 具体产业链路径的贡献排序是什么？ |
| `SPDf_path2002年-2020年.csv` | 不同最终需求类别驱动了哪些路径上的变化？ |

复现实用提示
======

1. 检查 `pre.N` 是否与投入产出表和强度表中的部门数量一致。本项目为 11 个部门。
2. 检查 `pre.year` 是否与 `IOT.xlsx` 的 sheet 名完全一致。
3. 如果最终需求某列总和为 0，`F./sum(F,1)` 可能产生 `NaN` 或 `Inf`。当前 `caculate_spd_detail_f.m` 已经把这类值置为 0。
4. 路径展开计算量随部门数和层级数快速增长。当前详细路径展开到 `L-3`，如果部门数增加，建议设置阈值 `v_threshold` 过滤贡献很小的路径。
5. 文件名中 `caculate` 是代码原有命名，不影响运行；如果后续整理为公开项目，可以统一改成 `calculate`。

小结
======

这个项目形成了一条比较完整的投入产出碳排放分解流程：先用 SDA 将总变化分解为四类驱动因素，再用 SPD 将变化量放回生产层级和产业链路径中观察。SDA 更适合回答“变化来自什么因素”，SPD 更适合回答“变化沿哪些生产层和产业链路径发生”。两者结合后，可以同时保留因素解释和产业链结构解释。
