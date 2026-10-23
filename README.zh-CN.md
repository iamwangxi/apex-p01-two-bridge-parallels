# 二桥结零框架两平行链环的循环复形可缩性

对每个非平凡二桥结，其反向定向零框架两平行链环的完整循环距离旗复形均可缩。复形由全偶锥与有限多个按奇载体、奇带标签划分的可缩部分在环带锥顶相接而成。覆盖全部亏格和扭转值，允许不连通生成曲面。

[English](README.md) · [对象与陈述](proof/objects.md) · [主定理 12.4 与证明图](proof/main-theorem.md) · [文献版本](sources/bibliography.md) · [范围](proof/scope.md)

## 对象与结论

顶点为定向、逐分量不可压、无闭分量的生成曲面的环境同痕类，边界可在有标签的实际边界环面移动。边由完整开补集在循环覆盖中的最小宽度为一确定，再取旗完成。本结论针对明确的循环距离对象，不宣称原始几何不交复形的同一结论。

主定理 12.4 给出

```math
X(L)=\mathcal B_E\cup_{\{a\}}
\bigcup_{\beta\in O(C)}\ \bigcup_{\mathbf z\in Z_\beta}X_{\beta,\mathbf z},
\qquad \mathcal B_E=a*Y_E.
```

$`a`$ 为标准环带类；不同部分除根外无交点、无跨边。全偶底 $`Y_E`$ 不必是一个点，其同痕与邻接由命题 4.2 的有限几何判据处理。定理 13.2 证明，多边界本质伴随片虽真实存在，却不能出现在任何合法定向全局顶点中。§12 的累计带高保留多个参数块的耦合，给出完整整数顶点与边判据；按奇带标签分区后，定理 12.3 在每个有限输入的有限扩充内逐次作邻域支配收缩。

**条件 (P) 保留为更明确的结构推论 1.3：** 每个非全偶零斜率 HT 展开恰有一个系数绝对值大于二时，所有奇载体部分都是在 $`a`$ 处相接的 Farey 树。全偶载体不受限制，奇零载体可以不唯一。树的非根顶点为既约奇分子分数 $`p/k`$，边满足 $`\lvert pk'-p'k\rvert=1`$。

三族无限例均有全参数的符号穷尽证明：

```math
C_m=K_{(6m+1)/(16m+3)},\quad m\ge1;
\qquad D_m=K_{8m/(20m-1)},\quad m\ge2;
\qquad B_m=K_{(8m^2+2m+2)/(16m^2+8m+5)},\quad m\ge1.
```

$`C_m`$ 满足 (P)，但具有不与环带相邻的顶点。$`D_2=K_{16/39}`$ 的奇部分为二维三角化圆盘体系：标记分母 $`k`$ 上有 $`4k+1`$ 个顶点组成的路径，根边上有四三角形扇，非根边上有 $`4(k+k')`$ 个三角形。$`B_1=K_{12/29}`$ 的奇部分为三棵 Farey 树在根处相接。

## 与目标论文的关系

目标为 Apex Intelligence 的官方比赛版本 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*，2026 年 9 月 11 日，48 页。[公开 PDF](https://math.apexin.net/papers/seifert-surfaces.pdf)。SHA-256：`34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`。

印刷第 2 页的 Theorems A、D 分别处理结及满足链接不可分解条件的链环。本题两分量链接数为零，处于 Theorem D 范围之外。该页指出一般链环中不同顶点可共享分量类，使 Lemma 4.9 的不交前提失效。本仓库允许不连通生成系统，独立证明指定循环复形的边与单形关系。

## 阅读与复跑

先读[对象与陈述](proof/objects.md)和[主定理证明图](proof/main-theorem.md)，再读[累计带高](proof/band-heights.md)、[有限收缩](proof/finite-contraction.md)与[三族无限例](proof/infinite-family.md)。本质装配、完整补集、载体纯性、返回与标记弧比较的全部依赖均在仓库内，具体编号及文件见英文导览。HT 印刷 p.230 聚合计数旁述与完整移动定理的冲突见[书目 Remark](sources/bibliography.md)；本证明直接使用 Theorem 1(e) 并证明有界轨道，不用该旁述。

Python 3.8 及以上，仅标准库。在仓库根目录运行：

```sh
python3 -B scripts/check.py --check
python3 -B scripts/check_general.py --check
python3 -B scripts/check_single_odd.py --check
python3 -B scripts/check_coupled_single.py --check
python3 -B scripts/check_multiple_odd.py --check
shasum -a 256 -c MANIFEST.sha256
```

`--check` 只重算比对，不写文件；去掉该参数只生成 `scripts/` 内相邻 JSON。两路复核的独立实现与删点证书均已纳入。[计算说明](scripts/README.md)列出有限范围。算术核验不代替几何证明和无限情形。尚未完成的独立事项为：全偶部分整数闭式商、不贡献顶点的多边界系统取向返回稳定子、形式化及三维产品识别软件。一般二桥结可缩性本身已证明。

## AI 声明

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews and a novelty check against the cited literature. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. GPT-6 Astra, also in OpenAI Codex, advised on research direction and submission scope. No human expert has certified the work.

## 许可

原创文字与计算数据采用 CC BY 4.0；`scripts/` 可执行代码采用 MIT License。见 [LICENSE](LICENSE)。外部文献仅引用，不打包。
