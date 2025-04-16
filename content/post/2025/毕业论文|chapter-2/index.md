---

title: "毕业论文|chapter 2"
slug: "毕业论文|chapter 2"
description: 
date: "2025-04-16T16:39:44+08:00"
lastmod: "2025-04-16T16:39:44+08:00"
image: 
math: true
license: 
hidden: false
draft: false 
categories: ["毕业论文"]
tags: [""]


---
# 量子纠缠的验证

## Bell不等式

要验证量子纠缠态的存在性，我们首先要证明隐变量理论的矛盾性，这样就证明了非局域性是量子力学的本质特征。前面EPR论文提出了量子力学的不完备性，而应该由额外的变量来补充的论据。这些变量试图去恢复理论中的局域性（**一个系统上的测量结果不受过去与之相互作用且遥远系统的影响**）和因果性。在之后的一段时间里，有许多试图去完善隐变量理论的工作，但是均已失败告终。

Bell通过将隐变量理论数学化并加入局域性假设，证明了其与量子力学的统计预测不相容（具有矛盾），即非局域性是量子力学的典型特征。

### 斯特恩-格拉赫实验

**（斯特恩-格拉赫实验可以展开说）**

考虑一对自旋为$\frac{1}{2}$的粒子，整个系统处于自旋单态（总自旋为0），两个粒子自由地朝反方向运动。自旋单态的表达式为：

$$
\ket{\psi} = \frac{1}{\sqrt{2}}(\ket{\uparrow \downarrow} - \ket{\downarrow \uparrow})
$$

式中$\ket{\uparrow\downarrow}$表示两粒子系统的状态，也可写成$\ket{\uparrow} \otimes \ket{\downarrow}$（左边为粒子1的自旋状态），$\ket{\uparrow}$表示单个粒子自旋向上，$\ket{\downarrow}$表示自旋向下。

定义粒子1和2的自旋算符$\vec{\sigma_1}$和$\vec{\sigma_2}$（Pauli算符形式，自旋算符与Pauli算符的关系为$\vec{S} = \frac{\hbar}{2}\vec{\sigma}$）。通过斯特恩-格拉赫实验测量某个方向（例如$\vec{a}$为粒子1的测量方向）的自旋分量。

测量粒子1的$\vec{\sigma_1} \cdot \vec{a}$可能得到$+1$或$-1$。由于系统反对称性（**可补充解释**），此时测量粒子2的$\vec{\sigma_2} \cdot \vec{a}$结果必然与粒子1相反（$-1$或$+1$）。

---

### 隐变量理论的数学化

Bell通过以下两个假设引出隐变量原理：

1. **局域性假设**：若两粒子自旋的测量在空间分离的方向进行，则一个磁铁的方向（测量粒子1的方向）不会影响另一个磁铁的测量结果。
2. **因果性假设**：通过测量$\sigma_1$的某个方向分量，可预测对应方向粒子2的自旋分量结果。

假设1指定了隐变量理论的局域性；假设2说明测量结果可被提前预测，对应隐变量$\lambda$的存在性（$\lambda$可以是单变量、一组变量或函数）。测量结果满足：

$$
A(\vec{a}, \lambda) = \pm 1, \quad B(\vec{b}, \lambda) = \pm 1
$$

隐变量理论的期望值为：

$$
P(\vec{a}, \vec{b}) = \int d\lambda \, \rho(\lambda) A(\vec{a}, \lambda) B(\vec{b}, \lambda)
$$

而量子力学对自旋单态的期望值为：

$$
\langle \vec{\sigma}_1 \cdot \vec{a} \; \vec{\sigma}_2 \cdot \vec{b} \rangle = -\vec{a} \cdot \vec{b}
$$

---

### 主要证明

Bell不等式的推导步骤如下：

1. **归一化条件**：$\int d\lambda \, \rho(\lambda) = 1$
2. **测量结果限制**：$A(\vec{a}, \lambda), B(\vec{b}, \lambda) = \pm 1$
3. **引入新方向$\vec{c}$**，计算差值：

$$
P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c}) = \int d\lambda \, \rho(\lambda) A(\vec{a}, \lambda) A(\vec{b}, \lambda) \left[ A(\vec{b}, \lambda) A(\vec{c}, \lambda) - 1 \right]
$$

4. **取绝对值并利用积分性质**，最终得到Bell不等式：

$$
|P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c})| \leq 1 + P(\vec{b}, \vec{c})
$$

---

### 验证实例

取$\vec{a} = (0,0,1)$, $\vec{b} = (1,0,0)$, $\vec{c} = (1/\sqrt{2}, 0, 1/\sqrt{2})$：

- $P(\vec{a}, \vec{b}) = 0$
- $P(\vec{a}, \vec{c}) = -1/\sqrt{2}$
- $|P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c})| = 1/\sqrt{2} \approx 0.707$
- $1 + P(\vec{b}, \vec{c}) = 1 - 1/\sqrt{2} \approx 0.293$

显然$0.707 > 0.293$，违反Bell不等式，说明隐变量理论无法解释量子力学预测。

---

### 结论

通过证明Bell不等式在量子力学中不成立，表明非局域性是量子力学的本质特征，从而验证了量子纠缠的合理性。

## 附录

### 参考文献

### 版权信息

本文原载于 [quantum51.top](https://quantum51.top)，遵循 CC BY-NC-SA 4.0 协议，复制请保留原文出处。
