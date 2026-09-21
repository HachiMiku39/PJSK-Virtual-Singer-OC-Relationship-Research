# 星乃一歌与六位虚拟歌手：V3 日文正文首轮评估

更新：2026-09-21。状态：日文正文首轮试评。

[返回项目首页](../../README.md) · [成长评分](growth.md) · [成长与情感比较](README.md) · [下载评分工作簿](ichika-matrix.xlsx)

本次只依据本地保存的日语剧情正文，量化虚拟歌手在一歌成长叙事中的可观察结构性重要程度。分数不表示感情深浅、好感度或配对关系。

这是全库检索后的重点精读结果，尚不是全库人工审计的最终定稿。分数是按明确口径作出的研究判断，并非文本自带的客观测量值。

## 结果

比较顺序为 K → S → C → T → B，逐项比较，同值并列。展示指数 I 不单独决定名次。

|VS|名次|K|独立强线数|C|S|T|B|I|置信度|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|4|4+|10|4|3|4|100.00|A|
|巡音流歌|2|3|3|9|3|2|4|77.67|B|
|KAITO|2|3|3|9|3|2|4|77.67|B|
|MEIKO|4|3|2|7|3|2|4|74.67|B|
|镜音铃|5|3|2|7|2|2|3|68.42|B|
|镜音连|5|3|2|7|2|2|3|68.42|B|

Miku 的 100 来自五项都达到本模型上限，没有把第一名强行归一化。它也不表示“关系完美”或“其他人不重要”。小数只是公式输出，不代表证据能精确到小数点后两位。

## 规则与此次使用的边界

- **K**：0 无有效证据，1 具体帮助，2 改变行动或决定，3 影响核心困惑、自我认识、重要关系或创作方向，4 进入人生起点、核心身份或长期道路。此次把已经被回顾确认的根基性作用和仍在展开的一次职业取舍区分开，后者不自动升 K4。
- **C**：只数 K2 及以上的独立成长线。0、1、2、3、4 条以上分别为 0、4、7、9、10。同一问题的后续回忆、重复感谢、不同章节不另算一条。
- **S**：0 无明确表达，1 感谢或信任，2 明确归因具体改变，3 归因重大成长或结果，4 显式特殊关系定位。共同归因可以成立，但必须核实谁在该场景实际参与，不能把“大家”“Miku 他们”自动扩成六人。
- **T**：0 单一时期，1 两个时期，2 三个时期，3 长期跨年。为避免把发行年份当作剧情经过的年份，五位 SEKAI 伙伴统一暂取三阶段覆盖的 T2：乐队起步与早期原创、面向外部听众的磨炼、职业与个人创作发展。Miku 有小学、中学到当前的明确回顾，取 T3。
- **B**：不同功能类别计数，最多 4。类别依据列在各人条目，不能把同一功能的近义描述重复累计。它只占指数的 5%，分类边界仍须后续统一复核。

I = 50×K/4 + 20×S/4 + 15×C/10 + 10×T/3 + 5×B/4。

保留 A+～F 置信度体系，不把置信度乘入分数。这里 Miku 的第一位判断为 A，其余暂为 B，尤其是相邻名次仍取决于独立线划分和归因强度的复核。没有赋予任何一项 A+。矩阵状态保留“核查中”，允许后续补充和修订。

## 每位歌手的判定

### 初音未来：(4,10,4,3,4)，I = 100.00

人生起点和持续创作方向都有直接文本支撑。

本轮计入的独立强线：

1. 小学因 Miku 萌生组乐队的想法。
2. 主线中承认重聚愿望并采取行动。
3. 克服公开演唱的畏惧。
4. 从憧憬者成长为用音乐连接他人的创作者。

日文证据：[E01 《This moment with you！》第3话：小学时因 Miku 萌生组乐队的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-03%20%E3%81%82%E3%81%AE%E5%AD%90%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L80)；[E02 同活动第5话：回顾组乐队的起点与中学时期的支撑](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-05%20%E3%83%9F%E3%82%AF%E3%81%8C%E3%81%8F%E3%82%8C%E3%81%9F%E3%82%82%E3%81%AE.txt#L64)；[E03 同活动第6话：一歌明确定位朋友、前辈与重要存在](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[E04 Leo/need 主线第17话：帮助一歌承认想和朋友重聚的愿望](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L18)；[E05 《君と歌う、桜舞う世界で》相关活动第18号第2话：街头演唱建议](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-02%20%E3%81%B2%E3%81%A8%E3%82%8A%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%AE%E8%B7%AF%E4%B8%8A.txt#L36)；[E06 活动第18号第4话：路演后的明确感谢](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-04%20%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E6%8B%8D%E6%89%8B.txt#L79)；[E07 《つなぐ、星の歌》第5话：认识到自己也能用音乐连接别人](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L65)。

功能类别：音乐与创作起点、情绪支撑、伙伴关系、面向听众的表达。

判定限制：Miku 按基础角色身份汇总，包含一歌在现实世界听见的歌曲、使用的歌声，以及 SEKAI 中的 Miku；并非只给 School Miku 的面对面指导评分。

### 巡音流歌：(3,9,3,2,4)，I = 77.67

早期关系修复与后期创作成长都有因果证据。

本轮计入的独立强线：

1. 主线重聚与对穗波心意的理解。
2. 为发生隔阂的听众姐妹写出能传达心意的歌曲。
3. 协调共同创作者的意图。

日文证据：[E12 主线第17话：Luka 的提醒让一歌继续寻找穗波的心意](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L39)；[E13 一歌卡0003前篇：把关系与生活重新动起来归因于咲希、Miku、Luka](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)；[E14 《Live with memories》第6话：把完成歌词明确归因于 Luka 的建议](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/056%20Live%20with%20memories%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/056-06%20%E5%B9%B8%E3%81%9B%E3%81%AA%E6%80%9D%E3%81%84%E5%87%BA.txt#L83)；[E15 《Parallel Harmonies》第7话：学习接纳共同创作者的意图](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-07%20%E5%8F%97%E3%81%91%E6%AD%A2%E3%82%81%E3%81%A6%E3%80%81%E9%9F%B3%E3%81%AB.txt#L57)；[E16 同活动第8话：把出道曲的完成归因于 MEIKO、Miku 等人的帮助](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-08%20%E4%BA%A4%E3%82%8F%E3%82%8B%E9%9F%B3.txt#L66)。

功能类别：创作方法、自我认识、伙伴与共同创作关系、听众沟通。

判定限制：S3 包含具名的共同归因。若只接受完全个别化的重大成长归因，应下调 S，不能隐去这一判断边界。

### KAITO：(3,9,3,2,4)，I = 77.67

表达自我的长期变化有非常直接的回顾归因。

本轮计入的独立强线：

1. 相信并坦率表达自己的想法。
2. 把音乐传播方式从现场演出扩展到 MV。
3. 识别并协调合奏中各人的表达意图。

日文证据：[E08 《Knock the Future!!》第6话：让一歌相信自己的歌词与想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L67)；[E09 KAITO 2023 纪念卡前篇：一歌明确回顾持久的表达变化](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L75)；[E10 区域对话：一歌明确感谢 KAITO 提供制作 MV 的契机](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_076.txt#L25)；[E11 《導く勇気、優しさを胸に》第5话：指出合奏需要协调各自意图](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-05%20%E3%83%90%E3%83%A9%E3%83%90%E3%83%A9%E3%81%AA%E9%9F%B3.txt#L62)。

功能类别：创作方法、自我肯定、合作协调、音乐传播。

判定限制：2023 纪念卡与早期表达剧情属于同一成长线，只增强 S 与 T，不重复增加 C。合奏诊断也不等于独占穗波的成长功劳。

### MEIKO：(3,7,3,2,4)，I = 74.67

两条强线都有一歌的明确归因，影响并不只限于技术指导。

本轮计入的独立强线：

1. 接纳咲希的创作意图并完成共同作品。
2. 公开 WITH 并认识自己的创作价值。

日文证据：[E15 《Parallel Harmonies》第7话：学习接纳共同创作者的意图](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-07%20%E5%8F%97%E3%81%91%E6%AD%A2%E3%82%81%E3%81%A6%E3%80%81%E9%9F%B3%E3%81%AB.txt#L57)；[E16 同活动第8话：把出道曲的完成归因于 MEIKO、Miku 等人的帮助](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-08%20%E4%BA%A4%E3%82%8F%E3%82%8B%E9%9F%B3.txt#L66)；[E17 活动第182号第6话：一歌明确归因作品公开的决定](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L81)；[E18 同话：MEIKO 提醒作品的力量也来自一歌本人](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L85)。

功能类别：创作与演奏方法、共同创作关系、公开作品、自我价值认识。

判定限制：早期关于职业乐队的谈话、强敌焦虑与代打鼓练习只作支持证据，尚不另外计 K2+ 独立线。

### 镜音铃：(3,7,2,2,3)，I = 68.42

最新职业选择剧情中有重要参与，已经超过日常帮助。

本轮计入的独立强线：

1. 受伤后改变练习方法。
2. 厘清个人音乐活动与 Leo/need 的优先顺序。

日文证据：[E19 一歌卡0494后篇：受伤后改用 Rin 代奏、自己分析的练习方法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0494_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E3%81%B2%E3%82%89%E3%82%81%E3%81%8D%E3%82%92%E5%BE%85%E3%81%A3%E3%81%A6%20%28event_69%29.txt#L146)；[E20 《Echo of a Prayer》第7话：与 Rin、Len 谈话后拒绝个人事务所签约](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L61)；[E21 同话：一歌明确感谢两人帮助厘清自己的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L58)；[E22 同活动第8话：尊重一歌自己的决定，但朋友仍担心她压抑个人愿望](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-08%20%E6%B3%A2%E7%B4%8B%E3%81%AF%E5%BA%83%E3%81%8C%E3%81%A3%E3%81%A6.txt#L82)。

功能类别：练习支持、情绪与自我梳理、职业选择。

判定限制：与 Len 共同帮助一歌梳理，决定属于一歌本人。后续仍有遗憾与新变数，暂不升 K4 或 S3。

### 镜音连：(3,7,2,2,3)，I = 68.42

有独立的回顾提示作用，也共同参与重大职业困惑。

本轮计入的独立强线：

1. 通过回顾 Miku 经历寻找歌声使用与创作方针的答案。
2. 厘清个人音乐活动与 Leo/need 的优先顺序。

日文证据：[E23 《This moment with you！》第2话：Len 提议从过去寻找创作困惑的线索](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-02%20%E3%81%97%E3%82%85%E3%82%8F%E3%81%97%E3%82%85%E3%82%8F%E3%81%A8%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4.txt#L83)；[E03 同活动第6话：一歌明确定位朋友、前辈与重要存在](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[E20 《Echo of a Prayer》第7话：与 Rin、Len 谈话后拒绝个人事务所签约](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L61)；[E21 同话：一歌明确感谢两人帮助厘清自己的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L58)；[E22 同活动第8话：尊重一歌自己的决定，但朋友仍担心她压抑个人愿望](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-08%20%E6%B3%A2%E7%B4%8B%E3%81%AF%E5%BA%83%E3%81%8C%E3%81%A3%E3%81%A6.txt#L82)；[E24 Len 卡1437后篇：模拟对邦演出，帮助一歌预想现场](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1437_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28Ln%29_R3%20%E3%81%9D%E3%81%AE%E9%81%B8%E6%8A%9E%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_212%29.txt#L103)。

功能类别：创作与排练支持、自我梳理、职业选择。

判定限制：创作答案的关键点拨也来自咲希。模拟演出暂按具体帮助 K1，不再增加强剧情线。

## 时间覆盖怎样核实

Miku 的童年起点见 [E01 《This moment with you！》第3话：小学时因 Miku 萌生组乐队的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-03%20%E3%81%82%E3%81%AE%E5%AD%90%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L80)，中学孤独期的明确支撑见 [E25 一歌卡0416前篇：Miku 的歌曲帮助她度过中学孤独期](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0416_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E8%80%83%E3%81%88%E3%82%8B%E3%82%88%E3%82%8A%E5%85%88%E3%81%AB%20%28event_56%29.txt#L95)，当前的关系定位见 [E03 同活动第6话：一歌明确定位朋友、前辈与重要存在](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)。

其余五位使用相同的三阶段口径。Rin 从早期作词应援，经受伤练习方法调整，到个人签约选择；Len 从早期新曲共同排练、MV 阶段的演奏反馈，到回顾提示与签约谈话；Luka 从主线重聚、为听众姐妹作词，到合作出道曲；MEIKO 从职业乐队谈话、针对演出与强敌的练习支持，到共同创作与公开 WITH；KAITO 从早期作词、MV，到职业阶段合奏协调。早期或中期的 K1 具体帮助可以证明关系持续存在，但不因此进入 C 的 K2+ 强线计数。

这些是叙事阶段，不是三年。尚未建立统一剧情日历前，不因现实连载跨年给五人 T3。如果把其中两阶段合并，相关 T 会从 2 降到 1，I 降约 3.33，但不能据此直接改变由更前维度决定的排序。

## 没有额外计分的内容

- 同框、发言次数、群体寒暄只用于检索候选，不产生分数。
- 一歌使用 Miku 歌声、听 Miku 歌曲属于正剧中明确描写的经历。声优经历、商业宣传、外部元叙事都未纳入。
- 一织对歌词的指导、心羽对街头演唱的帮助、奏提供的作曲知识、咲希的点拨、新堂的指导仍归各自角色。VS 的参与不能覆盖这些具体因果环节。
- KAITO 被多次回忆的“表达自己”只算一条。Luka 在协调共同创作者意图上的多次帮助合并处理。MEIKO 在同一共同创作故事中的召集、倾听与建议也只算一条。
- Len 帮助穗波或咲希的剧情，不转记成对一歌的强线。模拟对邦的实际练习支持暂取 K1，生日慰问、画画建议、饼干应援不单独增加强线。
- Rin、Len 的签约谈话保留一歌的自主决定。结尾对她是否仍有遗憾的疑问，不被写成已经确定的成功人生结果。

## 哪些名次还不稳定

Miku 的最高层级和显式关系定位在这六组中最稳固。中间五位暂不强行拉开很大的数值差距。

1. **MEIKO 的 C**：若进一步证明早期职业反思或强敌焦虑确实形成另一条独立 K2+ 改变，C 可由 7 升至 9，I 增 3，便与当前 Luka、KAITO 同向量并列。
2. **Luka 的 S**：当前 S3 接受有明确参与者的共同重大归因；若统一要求完全个别化的重大成长归因，S2 会使 I 减 5，且由于 S 优先比较，名次也会变化。
3. **Len 的 C**：若将模拟对邦认定为改变演出准备行为的独立 K2 线，C 可由 7 升至 9，I 增 3，此时在同 K、同 S 下超过 Rin。本轮采用较保守的具体排练支持判定。
4. **B 的分类**：相邻功能是否合并可能改变 1 档，对 I 的影响是 1.25；不能为了预设名次拆分功能。

因此，当前排序应读作“按已写明口径得到的首轮顺序”，不能把 77.67 与 74.67 当成已经证明的精确重要度差。

## 来源和覆盖

使用本地日文库的 4,082 个文档，以一歌的发言、具名提及和共同片段筛选候选，再精读影响成长的主线、活动和卡牌正文。候选库中有 1,841 条一歌–VS 配对候选记录，覆盖 737 个去重片段；配对记录与片段数均不是独立剧情线数，也不代表已经逐段完成人工审计。

文本来自 ci-ke/ProjectSekai-story 的固定快照 `fdfbd5de4f28f21a326d031439feb9b0491111a5`。它是游戏剧情的第三方文本整理，不是官方发布的数据库。本轮结论未经过游戏客户端画面逐句复核，也未使用中文译文、旧版数值、社区观点或声优资料补足因果。

下面保留定位用日文短句。每条链接固定到该快照的原文行，完整上下文应从链接进入查看。

## 日文证据索引

- **E01** [《This moment with you！》第3话：小学时因 Miku 萌生组乐队的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-03%20%E3%81%82%E3%81%AE%E5%AD%90%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L80)

  幼い一歌 (一歌): 私達で、ミクの曲を演奏しない！？

- **E02** [同活动第5话：回顾组乐队的起点与中学时期的支撑](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-05%20%E3%83%9F%E3%82%AF%E3%81%8C%E3%81%8F%E3%82%8C%E3%81%9F%E3%82%82%E3%81%AE.txt#L64)

  一歌: ミクのおかげでバンドをやるようになって、 毎日がキラキラして……すごく楽しかったな

- **E03** [同活动第6话：一歌明确定位朋友、前辈与重要存在](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)

  一歌: だから今は——好きとか、憧れとかだけじゃなくて、 友達として、先輩として……大切な存在だって思ってるんだ

- **E04** [Leo/need 主线第17话：帮助一歌承认想和朋友重聚的愿望](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L18)

  一歌: でも私は……何もできてない。 みんなで一緒にいたいって思ってるのに、何も行動できてない

- **E05** [《君と歌う、桜舞う世界で》相关活动第18号第2话：街头演唱建议](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-02%20%E3%81%B2%E3%81%A8%E3%82%8A%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%AE%E8%B7%AF%E4%B8%8A.txt#L36)

  ミク (Ln): それなら、路上ライブはどうかな？

- **E06** [活动第18号第4话：路演后的明确感谢](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-04%20%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E6%8B%8D%E6%89%8B.txt#L79)

  一歌: うん。 ミクのおかげだよ、ありがとう

- **E07** [《つなぐ、星の歌》第5话：认识到自己也能用音乐连接别人](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L65)

  一歌: ……私、できてたんだ。 ミクみたいに……誰かをつなげること……

- **E08** [《Knock the Future!!》第6话：让一歌相信自己的歌词与想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L67)

  KAITO: 恥ずかしいとも、つまらないとも思う必要ない。 ……これは、大事な一歌の想いだ

- **E09** [KAITO 2023 纪念卡前篇：一歌明确回顾持久的表达变化](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L75)

  一歌: あの言葉のおかげで、自分の想いを信じて、 恥ずかしがらずに表現できるようになったんだ

- **E10** [区域对话：一歌明确感谢 KAITO 提供制作 MV 的契机](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_076.txt#L25)

  一歌: カイト、この前はMVを作るきっかけをくれてありがとう

- **E11** [《導く勇気、優しさを胸に》第5话：指出合奏需要协调各自意图](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-05%20%E3%83%90%E3%83%A9%E3%83%90%E3%83%A9%E3%81%AA%E9%9F%B3.txt#L62)

  KAITO (Ln): ……一度、演奏する際のみんなの想いを すり合わせる必要があるんじゃないかな

- **E12** [主线第17话：Luka 的提醒让一歌继续寻找穗波的心意](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L39)

  ルカ: ここはあなた達の想いでできたセカイよ。 きっと、穂波の想いもここにある

- **E13** [一歌卡0003前篇：把关系与生活重新动起来归因于咲希、Miku、Luka](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)

  一歌: （いろいろなことが動き始めたのは、 きっと咲希やミクやルカのおかげだろうな……）

- **E14** [《Live with memories》第6话：把完成歌词明确归因于 Luka 的建议](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/056%20Live%20with%20memories%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/056-06%20%E5%B9%B8%E3%81%9B%E3%81%AA%E6%80%9D%E3%81%84%E5%87%BA.txt#L83)

  一歌: （ルカのアドバイスのおかげだな。 よかった……）

- **E15** [《Parallel Harmonies》第7话：学习接纳共同创作者的意图](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-07%20%E5%8F%97%E3%81%91%E6%AD%A2%E3%82%81%E3%81%A6%E3%80%81%E9%9F%B3%E3%81%AB.txt#L57)

  一歌: みんなのおかげで、大事なことに気づけたよ

- **E16** [同活动第8话：把出道曲的完成归因于 MEIKO、Miku 等人的帮助](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-08%20%E4%BA%A4%E3%82%8F%E3%82%8B%E9%9F%B3.txt#L66)

  一歌: この曲は……メイコやミク…… セカイのみんながいなかったら できてなかったと思うから

- **E17** [活动第182号第6话：一歌明确归因作品公开的决定](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L81)

  一歌: 曲をみんなにも聴いてもらおうって思えたのは、 あの時、メイコ達が背中を押してくれたからだよ

- **E18** [同话：MEIKO 提醒作品的力量也来自一歌本人](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L85)

  MEIKO (Ln): 『この曲を作ったのは一歌だし、 アオイさんは、一歌の曲を聴いて心を動かされたんだから』

- **E19** [一歌卡0494后篇：受伤后改用 Rin 代奏、自己分析的练习方法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0494_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E3%81%B2%E3%82%89%E3%82%81%E3%81%8D%E3%82%92%E5%BE%85%E3%81%A3%E3%81%A6%20%28event_69%29.txt#L146)

  一歌: そうだね。こんなケガくらいで立ち止まっていられない。 力を貸して、リン

- **E20** [《Echo of a Prayer》第7话：与 Rin、Len 谈话后拒绝个人事务所签约](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L61)

  一歌: ——事務所の話は、やっぱり断るよ

- **E21** [同话：一歌明确感谢两人帮助厘清自己的想法](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L58)

  一歌: ……ありがとう、ふたりとも。 おかげで、なんだかすっきりしたな

- **E22** [同活动第8话：尊重一歌自己的决定，但朋友仍担心她压抑个人愿望](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-08%20%E6%B3%A2%E7%B4%8B%E3%81%AF%E5%BA%83%E3%81%8C%E3%81%A3%E3%81%A6.txt#L82)

  志歩: ……一歌が、自分でそう決めたんでしょ

- **E23** [《This moment with you！》第2话：Len 提议从过去寻找创作困惑的线索](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-02%20%E3%81%97%E3%82%85%E3%82%8F%E3%81%97%E3%82%85%E3%82%8F%E3%81%A8%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4.txt#L83)

  レン (Ln): ただの興味もあるけど、 もしかしたら、それがヒントにつながるかもしれないだろ？

- **E24** [Len 卡1437后篇：模拟对邦演出，帮助一歌预想现场](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1437_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28Ln%29_R3%20%E3%81%9D%E3%81%AE%E9%81%B8%E6%8A%9E%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_212%29.txt#L103)

  一歌: おかげで、本番の空気をしっかりイメージできそうだよ

- **E25** [一歌卡0416前篇：Miku 的歌曲帮助她度过中学孤独期](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0416_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E8%80%83%E3%81%88%E3%82%8B%E3%82%88%E3%82%8A%E5%85%88%E3%81%AB%20%28event_56%29.txt#L95)

  一歌: ……私にはミクの曲があったから、 寂しさを乗り越えられたんだろうな
