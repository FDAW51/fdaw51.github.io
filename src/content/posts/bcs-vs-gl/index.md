---
title: "超导的两种语言：BCS 与 Ginzburg-Landau"
published: 2026-06-20
description: "超导现象有微观和宏观两种描述语言。BCS 理论解释「为什么有超导」，Ginzburg-Landau 理论解释「超导做什么」。本文对比两种理论的视角、回答的问题与互补关系。"
tags: ["BCS Theory", "Ginzburg-Landau Theory", "Cooper Pair", "Superconductivity", "Coherence Length", "Penetration Depth", "Type I and Type II Superconductors", "Meissner Effect"]
category: 凝聚态物理/超导
draft: false
---

# 超导的两种语言：BCS 与 Ginzburg-Landau

超导现象是 20 世纪物理学最迷人的发现之一。但在理解超导的过程中，物理学家们发展出了两种看似完全不同、实则深度互补的理论语言。本文试图回答：它们各自说了什么？如何构成完整的超导图景？

## 两种视角

| 维度 | BCS 理论 (1957) | GL 理论 (1950) |
|------|----------------|----------------|
| **视角** | 微观（从电子和声子出发） | 宏观（从自由能和序参量出发） |
| **核心概念** | Cooper 对、电子-声子耦合、能隙 | 序参量 $\psi(\mathbf{r})$、自由能泛函、对称性破缺 |
| **核心方程** | BCS 基态波函数、能隙方程 | GL 自由能泛函 $F[\psi]$、GL 方程 |
| **回答的问题** | 为什么电子会配对？能隙从哪来？ | 超导态的宏观行为是什么？磁场如何穿透？ |
| **数学工具** | 量子多体理论、二次量子化 | 变分法、Landau 相变理论 |
| **适用范围** | 低温超导体（传统超导体） | 所有超导体（包括高温超导） |
| **给出** | 能隙、$T_c$、电子比热等微观量 | $\xi$（相干长度）、$\lambda$（穿透深度）、$\kappa = \lambda/\xi$ |
| **不能给出** | 涡旋结构、界面能 | 配对机制、能隙微观起源 |

## BCS：微观起源

BCS 理论回答了超导最根本的问题：**电子为什么不再排斥，反而相互吸引？**

想象一个电子在晶格中穿行。它带负电，会把周围带正电的离子实吸引过来。这些笨重的离子实移动缓慢，在电子身后留下一个局域的正电荷富集区。第二个路过的电子被这个正电区域吸引——间接地，两个电子之间产生了净吸引。

这种"电子-声子耦合"机制在费米面附近最为有效。Cooper 在 1956 年证明：只要存在微弱的吸引，费米海就是**不稳定的**（Cooper Instability）——电子会自发两两配对，形成总自旋为零（单态）、总动量为零的 **Cooper 对**。这个配对态的能量低于两个独立电子的能量，因此系统发生相变，进入超导态。

BCS 理论的成功在于它从一个简单的物理图像出发，定量预测了转变温度 $T_c$、能隙大小、电子比热等可观测量——这些后来都被实验精确验证。

## GL：宏观行为

Landau 的相变哲学是：**你不需要知道微观细节，序参量就足够描述一切。**

Ginzburg 和 Landau 将这一哲学应用于超导。他们引入复序参量 $\psi(\mathbf{r})$，其模方 $|\psi|^2$ 等于超导电子的局域密度（即 Cooper 对密度）。在正常态，$\psi = 0$；在超导态，$\psi \neq 0$——序参量从零变为非零，是一种**自发对称性破缺**。

超导体的自由能展开为序参量的形式：

$$
F_s = F_n + \alpha|\psi|^2 + \frac{\beta}{2}|\psi|^4 + \frac{1}{2m}\left|\left(-i\hbar\nabla - \frac{2e\mathbf{A}}{c}\right)\psi\right|^2 + \frac{|\mathbf{H} - \mathbf{H}_a|^2}{8\pi}
$$

其中 $\alpha \propto (T - T_c)$：温度高于 $T_c$ 时 $\alpha > 0$，自由能最低点在 $\psi = 0$（正常态）；温度低于 $T_c$ 时 $\alpha < 0$，自由能最低点在 $\psi \neq 0$（超导态）。

通过对 $\psi^*$ 和 $\mathbf{A}$ 分别变分，得到两个 GL 方程。从 GL 方程可以自然导出超导的两个特征长度：

- **相干长度 $\xi$**：序参量受扰动后恢复到平衡的距离。$\xi$ 小 → 超导体"软"（像弹性物体，表面吸收能量阻止扰动传播）；$\xi$ 大 → 超导体"硬"（扰动像波一样传播）。
- **穿透深度 $\lambda$**：磁场在超导体中的衰减距离。$\lambda$ 越大，磁场越容易穿透。

## 两类超导体：$\kappa = \lambda / \xi$ 的物理

定义 GL 参数 $\kappa = \lambda / \xi$。从表面能的竞争可以理解：

- 表面能 $E_S = E_C - E_B$
- 凝聚能损失 $E_C \sim \xi \times$（损失的 Cooper 对能量）
- 磁场能收益 $E_B \sim \lambda \times$（获得的磁场能）

当 $\kappa < 1/\sqrt{2}$（$\xi > \lambda$，相干长度主导）：表面能为正 → **I 类超导体**，只有一个临界磁场 $H_c$。
当 $\kappa > 1/\sqrt{2}$（$\xi < \lambda$，穿透深度主导）：表面能为负 → **II 类超导体**，有两个临界磁场 $H_{c1}$ 和 $H_{c2}$。在 $H_{c1}$ 到 $H_{c2}$ 之间为**混合态**，磁场以量子化的**磁通涡旋**形式穿透——这正是 Abrikosov 预言的涡旋晶格。

## 互补而非对立

BCS 和 GL 不是竞争关系，而是互补的：

- **BCS 告诉你"为什么"**——电子-声子耦合 → Cooper 对 → 能隙
- **GL 告诉你"干什么"**——Meissner 效应、涡旋、磁通量子化
- 通过 **Gor'kov 推导**，BCS 的微观参数可以输入 GL 理论，两者在数学上是等价的
- $\kappa = \lambda/\xi$ 的分类由 BCS 微观机制决定，但分类本身是 GL 宏观框架的产物

大自然的描述语言不止一种。微观与宏观，就像两种不同的坐标系，描写同一个物理实在的不同侧面。

## 相关概念

- [[BCS Theory]] — 电子-声子耦合导致 Cooper 对形成的微观理论
- [[Ginzburg-Landau Theory]] — 基于序参量与自由能极小化的超导唯象理论
- [[Cooper Pair]] — 费米面附近两个电子通过晶格畸变形成的束缚态
- [[Meissner Effect]] — 超导体对磁场的完全排斥
- [[Coherence Length]] — 序参量受扰动后恢复的特征长度 $\xi$
- [[Penetration Depth]] — 磁场在超导体中的衰减特征长度 $\lambda$
- [[Type I and Type II Superconductors]] — 由 $\kappa = \lambda/\xi$ 区分的两类超导体
- [[Magnetic Flux Vortex]] — II 类超导体中磁通穿透的量子化涡旋
- [[Flux Quantization]] — 磁通量子 $\Phi_0 = hc/2e$

> 本文基于 Wiki 综合页 [[synthesis/BCS 理论与 GL 理论对比]] 改写。
