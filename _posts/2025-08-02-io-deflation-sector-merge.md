---
title: "投入产出表价格平减与部门合并：统一 11 部门口径的数据处理流程"
date: 2025-08-02
permalink: /posts/2025/08/io-deflation-sector-merge/
tags:
  - 投入产出
  - 价格平减
  - 部门合并
  - 数据处理
  - MATLAB
excerpt: "本文整理一个投入产出表价格平减和部门合并项目，说明如何将不同年份、不同部门口径的中国投入产出表转换为以 2010 年为基期的统一 11 部门表。"
---

这篇笔记整理自一个投入产出表数据处理项目。项目目标不是直接估计某个最终经济模型，而是先完成一项基础但很关键的数据工程：把不同年份、不同部门口径的中国投入产出表进行价格平减，并合并为统一的 11 部门口径表，为后续投入产出、R&D、产业结构或碳排放测算提供一致的数据基础。

需要特别说明的是，项目中的 `tex/模型20250730.tex` 标题写作“生产结构、收入分配与宏观效率论文复现测算说明”，文件后半部分也保留了一些与三部类表、工资-利润曲线相关的草稿内容。但从实际可运行代码看，`code/main20250731.m` 做的是投入产出表价格调平、价格指数匹配和部门合并。因此本文标题和正文以 MATLAB 主程序及其函数为准。

项目代码和数据包：

- [io-deflator-code-20250730.zip]({{ "/files/io-deflator-code-20250730.zip" | relative_url }})
- [io-deflator-data-literature-20250730.zip]({{ "/files/io-deflator-data-literature-20250730.zip" | relative_url }})

项目结构
======

核心流程位于 `code/` 目录：

| 文件或目录 | 内容 |
|---|---|
| `code/main20250731.m` | 主程序，串联数据导入、价格平减、部门合并和结果导出 |
| `code/source/IOT/` | 各年份原始投入产出表 |
| `code/source/deflator/` | 各类价格指数原始表 |
| `code/source/模型附件.xlsx` | 部门合并匹配表、价格指数匹配表和整理后的价格指数 |
| `code/import_ciot_raw.m` | 按年份读取不同格式的原始投入产出表 |
| `code/import_deflator.m` | 读取并整理价格指数，将环比指数转换为以 2010 年为基期的指数 |
| `code/io_price_adjust.m` | 根据价格指数对投入产出表各部分进行价格平减 |
| `code/cio_merge.m` | 将原始部门合并为 11 个统一部门 |
| `code/outshow_io.m` | 按固定格式导出合并后的投入产出表 |
| `code/output/IOT_adj1.xlsx` | 最终输出：价格平减后、统一 11 部门口径的投入产出表 |

主程序设定的年份为：

```matlab
pre.year = [2002,2005,2007,2010,2012,2015,2017,2018,2020];
pre.folder = "source";
pre.N = 11;
```

原始投入产出表的部门数量并不一致：

| 年份 | 原始部门数 |
|---|---:|
| 2002 | 122 |
| 2005 | 42 |
| 2007 | 135 |
| 2010 | 41 |
| 2012 | 139 |
| 2015 | 42 |
| 2017 | 149 |
| 2018 | 153 |
| 2020 | 153 |

因此，项目的关键问题是两个：第一，如何把各年份名义投入产出表调整到同一价格基期；第二，如何把不同年份的原始部门映射到统一的 11 个部门。

模型说明：投入产出表的数据块
======

对任一年份 \(y\)，原始投入产出表可以拆成几个矩阵或向量：

$$
Z^{(y)} \in \mathbb{R}^{n_y \times n_y}
$$

表示中间投入矩阵，其中 \(n_y\) 是该年份原始投入产出表的部门数。

$$
F^{(y)} \in \mathbb{R}^{n_y \times f_y}
$$

表示最终需求矩阵，包括居民消费、政府消费、资本形成等分项。项目中不同年份的最终需求列位置不完全一致，因此在 `import_ciot_raw.m` 中按年份分别设置 `idx_f_all`。

另外还有：

$$
EX^{(y)}, IM^{(y)}, ERR^{(y)}, X^{(y)} \in \mathbb{R}^{n_y \times 1}
$$

分别表示出口、进口、误差项和总产出，以及：

$$
VA^{(y)} \in \mathbb{R}^{v_y \times n_y}
$$

表示增加值矩阵。

按照投入产出表的行平衡和列平衡关系，有：

$$
X^{(y)}
=
Z^{(y)}\mathbf{1}_{n_y}
+
F^{(y)}\mathbf{1}_{f_y}
+
EX^{(y)}
-
IM^{(y)}
+
ERR^{(y)}
$$

以及：

$$
{X^{(y)}}^\top
=
\mathbf{1}_{n_y}^\top Z^{(y)}
+
\mathbf{1}_{v_y}^\top VA^{(y)}
$$

其中 $\mathbf{1}_{n_y}$、$\mathbf{1}_{f_y}$、$\mathbf{1}_{v_y}$ 分别是对应维度的全 1 向量。代码在读取时用这两个式子进行核验：

```matlab
X_row = sum(Z,2)+sum(F,2)+EX-IM+ERR;
X_col = sum(Z,1)'+sum(VA,1)';
X_check = [X,X_row,X_col];
```

如果行列平衡误差在容许范围内，程序会输出“行列平衡均满足”。

价格指数转基期
======

原始价格指数大多是“上年 = 100”的环比指数。项目首先将它们转换为以 2010 年为基期的定基指数。设第 \(k\) 个价格指标在年份 \(t\) 的环比指数为：

$$
r_{k,t} = \frac{P_{k,t}}{P_{k,t-1}}
$$

代码中先把百分数形式除以 100：

```matlab
D_mat = cell2mat(D_raw(2:end,5:end))./100;
```

令基期为 \(b=2010\)。对于基期之前的年份 \(t<b\)，以 2010 年为基期的价格指数可写为：

$$
\delta_{k,t}^{(b)}
=
\frac{P_{k,t}}{P_{k,b}}
=
\left(
\prod_{s=t+1}^{b} r_{k,s}
\right)^{-1}
$$

对于基期年份：

$$
\delta_{k,b}^{(b)} = 1
$$

对于基期之后的年份 \(t>b\)：

$$
\delta_{k,t}^{(b)}
=
\frac{P_{k,t}}{P_{k,b}}
=
\prod_{s=b+1}^{t} r_{k,s}
$$

这对应 `import_deflator.m` 中的核心操作：

```matlab
year_base = 2010;
[~,yb_idx] = ismember(year_base,year_raw);

D_b = D_mat(:,1:yb_idx);
D_b1 = fliplr(D_b);
D_b2 = 1./cumprod(D_b1,2);
D_b3 = D_b2(:,1:end-1);
D_bi = fliplr(D_b3);

D_f = D_mat(:,yb_idx+1:end);
D_f1 = cumprod(D_f,2);
D_fi = D_f1(:,1:end-1);

D_adj = [D_bi,ones(size(D_b,1),1),D_fi];
```

这里得到的 \(\delta_{k,t}^{(2010)}\) 是价格指数，而后续价格平减需要使用它的倒数。

价格指数与原始部门的匹配
======

各年份投入产出表的部门划分不同，因此每个原始部门需要先匹配到一个价格指数。设年份 \(y\) 的原始部门数为 \(n_y\)，价格指标集合为 \(k=1,\ldots,K\)。项目用 `模型附件.xlsx` 中的“价格指数匹配”表给出映射：

$$
\mu^{(y)}
=
\begin{bmatrix}
\mu_1^{(y)}\\
\mu_2^{(y)}\\
\vdots\\
\mu_{n_y}^{(y)}
\end{bmatrix}
$$

其中 \(\mu_i^{(y)}\) 表示年份 \(y\) 中第 \(i\) 个原始投入产出部门对应的价格指数编号。

于是可以得到部门层面的价格指数向量：

$$
d^{(y)}
=
\begin{bmatrix}
\delta_{\mu_1^{(y)},y}^{(2010)}\\
\delta_{\mu_2^{(y)},y}^{(2010)}\\
\vdots\\
\delta_{\mu_{n_y}^{(y)},y}^{(2010)}
\end{bmatrix}
\in \mathbb{R}^{n_y \times 1}
$$

并构造价格平减矩阵：

$$
D^{(y)}
=
\operatorname{diag}
\left(
\frac{1}{d_1^{(y)}},
\frac{1}{d_2^{(y)}},
\ldots,
\frac{1}{d_{n_y}^{(y)}}
\right)
$$

代码实现如下：

```matlab
d_merge = D_m((1:N)+1,y);
d_m = zeros(N,1);

for n = 1:N
    idx_n = d_merge{n};
    d_m(n) = Idx(idx_n);
end

d_hat = 1./d_m;
d_hat(isnan(d_hat)|isinf(d_hat)) = 1;
```

模型说明：价格平减的矩阵形式
======

投入产出表按产品部门行列组织。价格平减时，中间投入、最终需求、出口、进口、误差项和总产出均按“产品行”进行平减；增加值矩阵则按“部门列”进行平减。

令 \(D^{(y)}\) 为上面的对角平减矩阵，则价格平减后的投入产出表为：

$$
\widetilde{Z}^{(y)}
=
D^{(y)} Z^{(y)}
$$

$$
\widetilde{F}^{(y)}
=
D^{(y)} F^{(y)}
$$

$$
\widetilde{EX}^{(y)}
=
D^{(y)} EX^{(y)}
$$

$$
\widetilde{IM}^{(y)}
=
D^{(y)} IM^{(y)}
$$

$$
\widetilde{ERR}^{(y)}
=
D^{(y)} ERR^{(y)}
$$

$$
\widetilde{X}^{(y)}
=
D^{(y)} X^{(y)}
$$

对增加值矩阵：

$$
\widetilde{VA}^{(y)}
=
VA^{(y)}D^{(y)}
$$

对应代码为：

```matlab
IO.Z = diag(d_hat)*D.Z;
IO.F = diag(d_hat)*D.F;
IO.EX = diag(d_hat)*D.EX;
IO.ERR = diag(d_hat)*D.ERR;
IO.X = diag(d_hat)*D.X;
IO.IM = diag(d_hat)*D.IM;
IO.VA = D.VA*diag(d_hat);
```

这里不把公式简化成一个总矩阵乘法，是因为每个块的经济含义不同：`Z`、`F`、`EX`、`IM`、`ERR`、`X` 是按产品行平减，而 `VA` 反映各部门增加值项目，需要按部门列平减。

模型说明：部门合并矩阵
======

价格平减完成后，项目把各年份原始部门合并为统一的 11 个部门。令合并后的部门数为 \(m=11\)，构造部门合并矩阵：

$$
S^{(y)}
=
\begin{bmatrix}
s_{11}^{(y)} & s_{12}^{(y)} & \cdots & s_{1n_y}^{(y)}\\
s_{21}^{(y)} & s_{22}^{(y)} & \cdots & s_{2n_y}^{(y)}\\
\vdots & \vdots & \ddots & \vdots\\
s_{m1}^{(y)} & s_{m2}^{(y)} & \cdots & s_{mn_y}^{(y)}
\end{bmatrix}
\in \{0,1\}^{m \times n_y}
$$

其中：

$$
s_{ji}^{(y)}
=
\begin{cases}
1, & \text{若年份 }y\text{ 的原始部门 }i\text{ 被归入合并部门 }j\\
0, & \text{否则}
\end{cases}
$$

例如 `模型附件.xlsx` 的“部门合并匹配”表中，`M1` 到 `M11` 给出了各年份对应的原始部门索引。代码中用如下方式构造 \(S^{(y)}\)：

```matlab
MS = zeros(N_new,N_all(y));

for n = 1:N_new
    idx_n = D_cell{n,y};
    if ischar(idx_n)
        idx_n = str2num(idx_n);
    end
    MS(n,idx_n) = 1;
end
```

合并后的矩阵公式
======

将平减后的投入产出表合并为 11 部门口径，矩阵形式为：

$$
Z_m^{(y)}
=
S^{(y)}\widetilde{Z}^{(y)}{S^{(y)}}^\top
$$

$$
F_m^{(y)}
=
S^{(y)}\widetilde{F}^{(y)}
$$

$$
EX_m^{(y)}
=
S^{(y)}\widetilde{EX}^{(y)}
$$

$$
IM_m^{(y)}
=
S^{(y)}\widetilde{IM}^{(y)}
$$

$$
ERR_m^{(y)}
=
S^{(y)}\widetilde{ERR}^{(y)}
$$

$$
X_m^{(y)}
=
S^{(y)}\widetilde{X}^{(y)}
$$

增加值部分按列合并：

$$
VA_m^{(y)}
=
\widetilde{VA}^{(y)}{S^{(y)}}^\top
$$

将价格平减和部门合并连起来看，中间投入矩阵的完整变换为：

$$
Z_m^{(y)}
=
S^{(y)}D^{(y)}Z^{(y)}{S^{(y)}}^\top
$$

最终需求、进出口和总产出则分别为：

$$
F_m^{(y)}
=
S^{(y)}D^{(y)}F^{(y)}
$$

$$
EX_m^{(y)}
=
S^{(y)}D^{(y)}EX^{(y)}
$$

$$
IM_m^{(y)}
=
S^{(y)}D^{(y)}IM^{(y)}
$$

$$
X_m^{(y)}
=
S^{(y)}D^{(y)}X^{(y)}
$$

增加值矩阵的完整变换为：

$$
VA_m^{(y)}
=
VA^{(y)}D^{(y)}{S^{(y)}}^\top
$$

对应 `cio_merge.m`：

```matlab
IO.Z = MS*D.Z*MS';
IO.F = MS*D.F;
IO.EX = MS*D.EX;
IO.ERR = MS*D.ERR;
IO.X = MS*D.X;
IO.IM = MS*D.IM;
IO.VA = D.VA*MS';
```

代码说明：完整主流程
======

项目由 `main20250731.m` 驱动：

```matlab
% 该程序用于进行IO表的价格调平以及相关指标测算
cd("E:\Work\20250730\code");
clc; clear; close all;

pre = struct;
pre.year = [2002,2005,2007,2010,2012,2015,2017,2018,2020];
pre.year_p = [2002,2020];
pre.folder = "source";
pre.N = 11;

IOT_raw = import_ciot_raw(pre);
Index_raw = import_deflator(IOT_raw,pre);

IOT_d = io_price_adjust(IOT_raw,Index_raw,pre);
IOT_m = cio_merge(IOT_d,pre);

Tab_IO = outshow_io(IOT_m,pre);
```

这条流程可以概括为：

1. 读取原始投入产出表；
2. 读取并整理价格指数；
3. 将环比价格指数转换为 2010 年基期指数；
4. 按部门匹配价格指数；
5. 对投入产出表进行价格平减；
6. 按 11 部门标准合并；
7. 导出统一格式的投入产出表。

结果输出
======

最终输出文件是：

```text
code/output/IOT_adj1.xlsx
```

每个年份对应一个 sheet。`outshow_io.m` 会先复制 `source/IOT格式参照.xlsx` 作为模板，再把计算结果写入每个年份 sheet 的指定区域：

```matlab
file_out = "output\IOT_adj1.xlsx";

if exist(file_out,"file")
    delete(file_out);
    copyfile(fullfile("source","IOT格式参照.xlsx"),file_out);
else
    copyfile(fullfile("source","IOT格式参照.xlsx"),file_out);
end

writematrix(Tab_out,file_out,"Sheet",num2str(year(y)),...
    "Range","C3","PreserveFormat",true);
```

导出的表保留了投入产出表常见结构：中间使用、最终需求、出口、进口、误差项、总产出、增加值和列合计等。对于 2017 年以后没有误差项的表，程序会按年份自动调整输出列结构。

几点实现细节
======

1. 原始表读取必须按年份单独设置行列位置。不同年份表头结构不同，所以 `import_ciot_raw.m` 中有 `idx_rf_all`、`idx_cf_all`、`idx_f_all`、`idx_ex_all` 等索引配置。
2. 2018 年投入产出表读取的是 `生产价投入产出表` 这个 sheet，其他年份默认读取第一个 sheet。
3. 对价格指数缺失值进行了两次填补：先用同一文件中较完整的指标补，再用合并后的第一行指标补。
4. 平减时对异常倒数进行处理：如果出现 `NaN` 或 `Inf`，令对应平减系数为 1。
5. 部门合并矩阵是 0-1 矩阵。它不仅可以用于中间投入矩阵，也可以用于最终需求、进出口、误差项、总产出和增加值矩阵。

小结
======

这个项目的价值在于把“年份不同、部门口径不同、价格水平不同”的投入产出数据整理成一个可横向比较的统一数据集。矩阵上看，核心就是两个变换：

$$
\text{价格平减：}\quad
\widetilde{Z}^{(y)}=D^{(y)}Z^{(y)}
$$

以及：

$$
\text{部门合并：}\quad
Z_m^{(y)}=S^{(y)}\widetilde{Z}^{(y)}{S^{(y)}}^\top
$$

但在实际数据处理中，真正耗时的是价格指标匹配、年份表头差异处理、部门索引统一和输出格式修复。整理完成后的 `IOT_adj1.xlsx` 可以作为后续投入产出分析、产业结构分析、R&D 相关测算或碳排放核算的基础投入表。
