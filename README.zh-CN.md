# 平行簇的不可压生成曲面复形

对由非平凡二桥结、环面结经有限次连通和与取缆得到的每个结，**任意整数框架、任意正条数、任意取向的平行簇**，其完整循环复形与原论文几何不交复形都强形变收缩到 taut 循环复形，从而可缩。同一结论还覆盖任意非平凡纤维结的**所有整数框架、取向和非零的平行簇**，以及**所有整数框架的两条反向平行**。

[English](README.md) · [主定理与一般对象](proof/main-theorem.md) · [范围](proof/scope.md) · [文献版本和页码](sources/bibliography.md) · [复核状态及 SHA-256](sources/review-status.md)

## 定理与证明

设 $`L_f(K;\epsilon_1,\ldots,\epsilon_n)`$ 为斜率 $`\lambda+f\mu`$ 的 $`n\ge1`$ 条带标签平行分量，取向和为 $`d=\sum_i\epsilon_i`$。上述范围内有

```math
X(L)\subseteq Y(L),\qquad
|Y(L)|\searrow |X(L)|\searrow |MS(L)|.
```

两箭头都是强形变收缩；$`MS(L)`$ 指 Przytycki–Schultens 的 taut **循环**复形。递归类或任意纤维结分支若 $`fd\ne0`$，更有 $`X=Y=MS(L)`$，但不一定只有一个顶点。$`K_{4/15}`$ 的同向、框架一、两条平行簇有不同的亏格二顶点。

- [零框架任意平行簇](proof/zero-framed-clusters.md)：单边界片的圆周上包络；非平行、多边界系统的腔室路径；普通根、完整闭包与逐面相容棱柱。
- [任意整数框架](proof/framed-clusters.md)：含链接修正的实际生成斜率、非零纤维取值、平衡非零斜率、普通横向返回，以及环面结的环带例外。
- [递归类与纤维结](proof/recursive-and-fibred.md)：整个系统的反射结构在连通和、取缆下闭合；非零类纤维分支直接紧致提升每个不交分量，只读取边界数和亏格，不下投覆盖空间同痕。
- [递归类任意框架与纤维结平衡双拷贝](proof/framed-recursive-and-fibred.md)：完整有限斜率系统、非平行子片的取缆合并、平衡双拷贝的压缩屏障与连通分支交换，以及任意平衡零框架纤维簇的精确分离分支约化。

顶点为紧致、定向、逐分量不可压、无闭分量的生成系统的普通环境同痕类；每个实际带标签边界环面使用一次。允许不连通与任意亏格，边界可在其环面上移动，同痕从恒等开始。$`X`$ 使用一个总链接类覆盖中**整个开补域**的最小宽度一给边，再取旗完成；$`Y`$ 要求完整代表同时不交，定义中不补旗。框架非零时实际边界须含链接修正，详见[主定理](proof/main-theorem.md)。

第一箭头引用公开数学结果 [CW, Part 7, Theorem D](https://github.com/iamwangxi/apex-p01-seifert-fibred-links/blob/f6f44253f2ed539a74bf4cfdc99fed299e386546/proof/part7.md#1-objects-and-statements)，固定提交 `f6f44253f2ed539a74bf4cfdc99fed299e386546`。各证明页核对非分裂性、完整顶点、覆盖和边界约定。该比较本身不提供可缩性；先把 $`X`$ 收缩到已识别的 taut 终点，再使用 PS Theorem 1.1。拼接全程固定 $`MS(L)`$。

## 与原论文的关系

目标为 Apex Intelligence 官方比赛版本 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*，2026 年 9 月 11 日，48 页。[公开 PDF](https://math.apexin.net/papers/seifert-surfaces.pdf)。SHA-256：`34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`。

印刷第 2 页的 Theorems A、D 处理结和满足链接不可分解条件的链环。至少两条零框架平行簇的两两链接数为零，超出该链接条件。论文指出，一般链环的不同顶点可共享整分量类，使 Lemma 4.9 的前提失效。本结果允许不连通生成系统，并得到原始几何复形的结论。一条平行分量、部分非零框架情形与原论文范围重合，不把所有参数都说成新增情形。CW 的 Theorem D 与原论文同号定理不同。

## 两条反向平行的精细结构

原有[对象页](proof/objects.md)、[定理 12.4–12.5](proof/main-theorem.md)及后续带高、Farey 树、三角化圆盘结构，专门描述**两条反向、零框架平行**的 $`X`$。三族无限例有[全参数符号证明](proof/infinite-family.md)。两终端障碍排除的多边界伴随片可以出现在更多条数的平行簇；任意簇证明保留并处理这些片。精细结构不被外推为所有 $`Y`$ 单形的分类。

## 复跑与范围边界

Python 3.8 及以上，仅标准库。在仓库根目录运行：

```sh
python3 -B scripts/verify_package.py
```

该入口**只读**：先核对现有清单，再实际执行全部十三套诊断并比对确定性结果（JSON 报告比较全部字段，文本快照逐字比较，清单核对保存文件的字节），最后再验清单。它不在核验前修复清单。仅运行算术诊断可用 `python3 -B scripts/run_all.py`。单项诊断加 `--check` 只读；去掉参数仅生成 `scripts/` 内相邻结果。清单生成另行执行。[诊断说明](scripts/README.md)列出范围与证据边界。

任意平衡零框架纤维簇可强形变收缩到完整分离伴随分支；但四条及以上、超出已证子类时，该分支的可缩性仍未闭合。分离分支中的不连通顶点和共享整分量均予保留，不能直接套用双拷贝屏障。一般 Montesinos/arborescent 中超出递归类或已证纤维范围的情形也未覆盖。不宣称任意链环可缩。全偶底整数闭式商、三维产品识别软件与形式化也未完成。

## AI 声明与复核状态

**状态：经一路全新上下文 AI 对抗复核成立。** [复核记录](sources/review-status.md)列出各源稿、复核和补证的 SHA-256，区分源稿与修补后证明页。

GPT-6.1 Sol 在人类指导下完成二桥结循环证明、零框架任意簇、整数框架分支、计算及本轮整合，将已复核的递归类任意框架与纤维平衡双拷贝扩展并入投稿包；另由全新 GPT-6.1 Sol 上下文完成所记录的对抗复核。**此前零框架递归类与非平衡纤维结一稿由 GPT-6 Astra 完成**，Astra 也提供过方向建议。Claude 参与早期两平行工作的规划、文献核对和审阅。整合已落实整个系统纯性的补证、静止事件排序及高度，并将新稿中的坐标术语修正为 HT plumbing 参数。本轮进行了本地一致性和诊断检查，没有另起全新上下文复核整合包；无人类专家认证或形式化证明。

## 许可

原创文字与计算数据采用 CC BY 4.0；可执行代码采用 MIT License。见 [LICENSE](LICENSE)。外部文献仅引用，不打包。
