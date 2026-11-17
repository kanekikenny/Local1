# 3000题项目：测试错误与修正案例

各类按固定测试顺序取前两个。属于目的性展示，不代表错误类型频率。ARC没有为所有题提供人工推导，本文件不编造参考推理。

## 监督头修正：arc_Mercury_SC_405710

Which describes a chemical change?

A. sugar dissolving in tea
B. scissors cutting paper into pieces
C. acid in the stomach digesting food
D. sunshine warming a sidewalk

发布者答案：C。
本地原模型：A，四候选条件置信度0.907。
监督答题头：C，四候选条件置信度0.586。
检索双示例：C，四候选条件置信度0.516。

## 监督头修正：arc_Mercury_7270515

Which of these questions cannot be answered scientifically?

A. Which frequencies can be heard by children but not by adults?
B. Which musical notes can be perceived by the human ear?
C. Which musical notes combine to be the most beautiful?
D. Which frequencies can be produced by human vocal cords?

发布者答案：C。
本地原模型：A，四候选条件置信度0.452。
监督答题头：C，四候选条件置信度0.550。
检索双示例：C，四候选条件置信度1.000。

## 监督头改错：arc_Mercury_7004008

The relationship between ticks and a dog can best be described as

A. mutualism.
B. parasitism.
C. commensalism.
D. competition.

发布者答案：B。
本地原模型：B，四候选条件置信度0.969。
监督答题头：C，四候选条件置信度0.525。
检索双示例：B，四候选条件置信度0.988。

## 监督头改错：arc_Mercury_184240

Which event below involves a constructive force?

A. wind storm
B. earthquake
C. flood
D. volcanic eruption

发布者答案：D。
本地原模型：D，四候选条件置信度0.793。
监督答题头：A，四候选条件置信度0.513。
检索双示例：D，四候选条件置信度1.000。

## 检索示例改错：arc_Mercury_7263060

Which theory of the origin of the Moon proposes that Earth's Moon formed by the same process that formed Mars, Jupiter, and Neptune?

A. The Fission Theory
B. The Coaccretion Theory
C. The Giant Impact Theory
D. The Capture Theory

发布者答案：B。
本地原模型：B，四候选条件置信度1.000。
监督答题头：B，四候选条件置信度0.941。
检索双示例：C，四候选条件置信度1.000。

训练示例1（arc_Mercury_7146090）：Approximately 59% of the Moon is visible from Earth because the Moon rotates and revolves in the same period. Which most likely causes this phenomenon?
训练示例答案：the gravitational pull of Earth。

训练示例2（arc_Mercury_401657）：Which characteristic is shared by Earth and the Moon?
训练示例答案：an orbit created by the force of gravity。
同时出现检索示例和错误不证明该示例是唯一原因；本例仅展示检索条件相对零示例的观测变化。

## 检索示例改错：arc_ACTAAP_2013_5_13

Which is the correct order of the planets from the Sun?

A. Mercury, Earth, Mars, Venus, Saturn, Jupiter, Neptune, Uranus
B. Mercury, Venus, Earth, Saturn, Uranus, Jupiter, Mars, Neptune
C. Mercury, Venus, Mars, Earth, Jupiter, Uranus, Saturn, Neptune
D. Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

发布者答案：D。
本地原模型：D，四候选条件置信度1.000。
监督答题头：D，四候选条件置信度0.799。
检索双示例：A，四候选条件置信度0.864。

训练示例1（arc_MCAS_1998_4_17）：Which is the correct order of the metamorphosis of a butterfly?
训练示例答案：egg, larva, pupa, adult。

训练示例2（arc_Mercury_SC_LBS10244）：Which list gives the correct order of substances from the lowest melting point to the highest?
训练示例答案：oxygen, water, iron。
同时出现检索示例和错误不证明该示例是唯一原因；本例仅展示检索条件相对零示例的观测变化。

