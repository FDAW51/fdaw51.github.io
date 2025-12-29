---
title: "前置知识"
slug: "topoconmat|前置知识"
description: ""
image: ""
categories: ["TopoConMat"]
tags:
date: 2025-12-28T22:16:20+0800
draft: false
---

# Band Structure Theory 

拓扑物态中，主要研究的是对于不同结构（具有不同对称性的材料）的物体，其内部电子的能带结构与拓扑之间的关系。因此，物体中的电子的能级就显得尤为重要了。

首先，固体中的电子波函数遵循量子力学且受晶格周期性的影响（对称性也有）。

## 电子的量子力学：

量子力学的基本方程是薛定谔方程：
$$
i \hbar \frac { \partial \Psi } { \partial t } = H \Psi
$$
其中 $\Psi$是电子的波函数，H是电子的哈密顿量（能量函数）。

电子的H即它的能量为：
$$
H = \frac{p^2}{2m} + V(x)
$$
其中p为电子的动量，V(x)为电子在环境中所受的势能。

电子的波函数为 $\Psi(x,t)$ ,需要注意以下几点：

1. 波函数是一个Complex Number。
2. H是Hermitian的（$H^{\dagger} = H = \left( (H)^{T} \right)^{*}$）
3. $| \Psi | ^ { 2 } = \Psi ^ { * } \Psi \propto n _ { e }$（$n_e$ 表示电子的密度）
4. 如果有N个电子，这N个电子的系统的波函数：$\Psi_N = \psi_1 \otimes \psi_2 \otimes \psi_3 \otimes \cdots \otimes \psi_N$，并且其中任意两个波函数之间都是正交的（$\langle \psi_i | \psi_j \rangle = \delta_{ij}$）---这是由Pauli不相容原则保证的（Pauli 不相容原则：不可能存在两个处于相同状态的电子。）

如果假设电子的波函数满足：
$$
\Psi(x,t) = \sum_n e^{-i \frac{E_n t}{\hbar}} \psi_n(x)
$$
代入薛定谔方程得到定态薛定谔方程：
$$
H\psi_n(x) = E_n\psi_n(x)
$$
如果把H看成矩阵的话，$\psi_n$是H的特征值为En的特征向量，$E_n$是H的本征值。

## Tight Binding Model 

如果将固体内的电子当成主体的话，近自由电子模型将电子看作在整个晶格中自由奔跑的平面波。

紧束缚模型将电子在整个晶体中的波函数 $\psi_k(r)$看作在某一个原子附近的运动与不同原子之间的运动（平面波）的叠加：
$$
\psi_{\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{N}} \sum_{\mathbf{R}}  e^{i \mathbf{k} \cdot \mathbf{R}} \phi(\mathbf{r} - \mathbf{R})
$$
其中 $e^{i\mathbf{k\cdot R}}$是电子在原子间的周期性运动。这个周期性运动是由晶格的平移对称性保证的（平移对称性使得动量守恒，所以电子的波函数在原子间像一个自由的平面波， $p = \hbar k$，即波矢不变）。

那么电子在原子附近(在某一个原子中)的运动如何表达呢？ $\phi$

单原子附近有许多离散的轨道（如1s,2p等），TBM（Tight binding mode）假设电子在原子轨道内并不动，但是它有可能跳跃到相邻的轨道内。

通过求解电子在单原子内部的定态薛定谔方程，得到原子内轨道 $\{\ket{\psi_a}\}$,不同的下标a代表不同的轨道的电子波函数，在不同的轨道内电子的能量为 $E_a$。这些轨道构成了一组正交完备集，满足：
$$
\left\{
\begin{array}{l}
\langle \psi_a | \psi_b \rangle = \delta_{ab} \\
\sum\limits_a | \psi_a \rangle \langle \psi_a | = I
\end{array}
\right.
$$
那么对于任意的波函数 $\ket{\psi}$和H都可以展开成：
$$
|\psi\rangle = \sum_a c_a |\psi_a\rangle
$$
$$
H = \sum_{ab} H_{ab} |a\rangle\langle b|
$$

其中 $H_{ab} = \langle \psi_a | H | \psi_b \rangle$，表示H在这组基下的矩阵元。

Example：三角形的原子

假设电子运动在三个原子之间，每个原子都有一个轨道，记为： $\ket{0},\ket{1},\ket{2}$。首先电子的哈密顿量（能量是多少？），TBM假设了电子是在轨道之间跳跃，电子跳跃在原子之间就会形成化学键，形成化学键之后结构更稳定，体系的能量就越低。那么H可写为：
$$
H = -t \left( |0\rangle\langle 1| + |1\rangle\langle 2| + |2\rangle\langle 0| \right) + \text{h.c.}
$$
前面这个-t（t是一个跳跃的系数，负号为了保证电子发生跳跃的时候，系统的能量降低。）这一项代表了，电子从1跳到0，0跳到2，2跳到1，顺时针的情况，那么后面的h.c代表的就是逆时针的跳跃可能性（为了保证H的厄米性）

其中 $\ket{0}\bra{1}$为什么代表了电子从1跳到0呢？，解释如下：
	

如果此时电子处于轨道1（$\ket{1}$），将这一项作用上去有：
$$
|0\rangle\langle1|1\rangle = |0\rangle
$$
即输入是1，而输出的是0轨道，因此表示电子从1跳到0。

## Bloch Theorem For Bulk Electrons

有了上面的TBM的基础之后，我们将记号变得紧凑一些。

在固体物理中，晶格是可以由原胞通过周期性平移得到的。

![](https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/219/2016/08/09045711/CNX_Chem_10_06_UnitCell1.jpg)

Bloch Theorem给出，电子在整个晶格中的波函数可以写成原胞之间的平面波和在单个原胞内行为的叠加：
$$
\psi_{(l,n)} = e^{i k n} \cdot u_l
$$
$(l,n)$表示在第n个原胞内的电子在轨道l上的波函数（这里表示的是1维晶格的情况，可以把这个拓展到3维的情况，kn--> $\mathbf{k\cdot R_n}$,其中 $R_n = p\mathbf{a}+q\mathbf{b}+r\mathbf{c}$, a,b,c代表构成晶格原胞的基矢量）

k表示电子在晶体中的动量，范围是 $[-\pi,\pi]$，这个范围在晶格的倒空间中表示一个布里渊区。

那么在这个表示下的H的矩阵元为：
$$
H_{(l,m),(l',n)}= H_{(l,m-n),(l',0)}
$$
为什么这是成立的呢？因为晶格的周期性平移的特点，第二个参数m描述的是在第m个原胞上，所有的原胞在某种意义上等价。

首先实空间的波函数满足的定态薛定谔方程为：
$$
\sum_{l', m} H_{(l,n), (l',m)} \psi_{(l',m)} = E \psi_{(l,n)}
$$
代入bloch 定理下的波函数：
$$
\psi_{(l,n)} = e^{ikn} u_l(k)
$$
消去因子：
$$
\sum_{l', m} H_{(l,n), (l',m)} e^{ik(m-n)} u_{l'}(k) = E(k) u_l(k)
$$
整理求和项：
$$
\sum_{l'} \left[ \sum_{m} H_{(l,n), (l',m)} e^{ik(m-n)} \right] u_{l'}(k) = E(k) u_l(k)
$$
根据平移不变的假设：
$$
H_{(l,n), (l',m)} = H_{(l, n-m), (l', 0)}
$$
可以得到：
$$
H(k)_{ll'} = \sum_{m} H_{(l,-m), (l',0)} e^{-ikm}
$$
最后的形式是：
$$
\sum_{l'} H(k)_{ll'} u_{l'}(k) = E(k) u_l(k)
$$
矩阵形式：
$$
H(k) u(k) = E(k) u(k)
$$


Example：SSH model



## k.p Perturbation Theory

对于在倒空间的H(k)，如果只关心k = 0 附近的能量，或者Energy Gap（Energy Gap是定义在价带与导带之间的最小间隔）

可以对H(k)在 k = 0 附近做Taylor expansion：
$$
H(k) \approx \underbrace{H(k=0)}_{H_0(k)} + \underbrace{k H'(k=0) + \frac{k^2}{2} H''(k=0)}_{\text{Perturbation } V(k)}
$$
通过量子力学中的微扰论可以得到。

能量的一阶微扰修正是：
$$
E_1^{(n)} = \langle n | V(k) | n \rangle
$$
二阶微扰为：
$$
E_{2}^{(n)}(k) = \sum_{m \neq n} \frac{|\langle n | V | m \rangle|^{2}}{E_{0}^{(n)} - E_{0}^{(m)}}
$$
得出第n个本征态的能量为：
$$
E^{(n)}(k=0) \approx E_0^{(n)}(k=0) + \langle n | V(k=0) | n \rangle +\sum_{m \neq n} \frac{|\langle n | V | m \rangle|^{2}}{E_{0}^{(n)} - E_{0}^{(m)}}
$$
后面两项分别是1阶和2阶微扰。

在k = 0 处，电子波包在晶体中传播的速度为 $\mathbf{v}_g(\mathbf{k})$:
$$
\mathbf{v}_g(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} E(\mathbf{k})
$$
以及电子波包的有效质量 $m^*$:
$$
\left( \frac{1}{m^*} \right)_{ij} = \frac{1}{\hbar^2} \frac{\partial^2 E}{\partial k_i \partial k_j}
$$
代入对应的E，可以得到电子在第n个能级的传播速度 $v_n$ 和有效质量($m_n$)：
$$
V_n = \partial_k E^{(n)}(k) \big|_{k=0} = \langle n | H'(k=0) | n \rangle
$$

$$
m_n^{-1} = \partial_k^2 E^{(n)}(k) \big|_{k=0} = \langle n | H''(k=0) | n \rangle + 2 \sum_{m \neq n} \frac{|\langle n | H' | m \rangle|^2}{E_0^{(n)} - E_0^{(m)}}
$$

