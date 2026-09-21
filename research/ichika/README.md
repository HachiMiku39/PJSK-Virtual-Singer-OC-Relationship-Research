# 星乃一歌：加入情感维度后的评分

更新：2026-09-21。状态：日文正文首轮试评。

[返回项目首页](../../README.md) · [成长评分](growth.md) · [成长与情感比较](README.md) · [下载评分工作簿](ichika-matrix.xlsx)

本次沿用上一轮的日语剧情库，增加“一歌对各位 VS 表现出的情感关系深度”。原 V3 仍量化 VS 对一歌成长的结构性作用。两组结果并列，不相加、不替换，也没有按旧成长名次设定情感名次。

评分对象是文本表现，不是无法直接观察的内心强度。没有使用声优关系、社区观点、中文译文或配对推测。姓名共现和发言次数仅用于找候选。现在仍是首轮试评分，不是全剧情逐段人工审计。

## 结果

|VS|情感名次|情感表达|信任与袒露|主动投入|关系定位|情感指数|原成长指数|情感置信度|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|4|4|4|4|100.00|100.00|A|
|巡音流歌|2|3|3|3|2|68.75|77.67|B|
|KAITO|2|3|3|3|2|68.75|77.67|B|
|镜音铃|2|3|3|3|2|68.75|68.42|B|
|MEIKO|5|2|3|2|2|56.25|74.67|B|
|镜音连|5|2|3|2|2|56.25|68.42|B|

四维顺序为：情感表达、信任与袒露、主动投入、关系定位。每项 0～4，等权换算：情感指数 = 100 × 四项之和 / 16。每改变一档，指数变化 6.25；小数来自换算，不代表细至百分之一的判断精度。

目前情感顺序为：Miku ＞ Luka＝KAITO＝Rin ＞ MEIKO＝Len。这是粗粒度的文本编码顺序。中间五人的差距只有一两档的量级，不能将并列理解为感情完全相同，也不宜强行拆出第二到第六名。

Miku 的 100 来自四项到顶，未做第一名归一化。原成长排序仍为 Miku ＞ Luka＝KAITO ＞ MEIKO ＞ Rin＝Len，按原先 K→S→C→T→B 比较，未改用情感指数裁决。

## 此次采用的判定尺度

- 0：核查范围内未找到有效证据。未核查留空，不写 0。
- 1：一般性的友好、感谢、礼貌或信任。
- 2：明确、具体的个人情感证据。
- 3：涉及深层感受，或者在不同情境中持续表现；需要说明走的是哪一条证据路径。
- 4：深层且持续，足以支持关系中的稳定特征。不能只凭一次强烈台词或很多次谢谢。

情感表达看一歌对这个人的感受；信任看她是否把自己难以表达的部分交给对方；主动投入看她为关系和对方做了什么；关系定位看她怎样赋予对方个人意义。日常分享足以支持主动投入 2，个别化且跨情境的关心可支持 3；持续照顾对方深层愿望才考虑 4。

五位非 Miku 的关系定位都保守取 2，因为支持者或伙伴的个人意义已有表现，但还不足以从功能推成强烈的显式特殊关系定位。称呼“先辈”或感谢帮助本身不自动升档。

置信度沿用 A+～F，不进入分数。这里只给 Miku A，其他 B，尚无 A+。这些置信度针对情感试评分；原成长置信度保持不变。

## 每组关系的依据

### 初音未来：[4, 4, 4, 4]，情感指数 100.00

情感上同样最突出，证据包括双向关系中的主动照顾，而不只是受到帮助。

- **情感表达 4**：明确说 Miku 是重要存在、与她共处的景色特别；不只表达对歌曲的喜爱。这种感情在不同阶段都有直接表述。
- **信任与袒露 4**：从夜里找她说出对失去朋友的恐惧，到紧张的创作交流时请她同行，深层信任跨情境延续。
- **主动投入 4**：主动邀她赏花、唱歌传情、考虑如何让她快乐，并以共同演出回应她想感受连接的心愿。
- **关系定位 4**：明确定位朋友、前辈、重要存在，并在与其他 Miku 相遇时维护 School Miku 的个人位置。

证据：[A01](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-07%20%E3%81%B5%E3%81%9F%E3%82%8A%E3%81%A7%E8%A6%8B%E3%82%8B%E6%A1%9C.txt#L15)；[A02](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0004_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E5%A4%9C%E6%98%8E%E3%81%91%E5%89%8D%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84.txt#L39)；[A03](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L86)；[A04](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L140)；[A05](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/1375_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%EF%BC%94%E4%BA%BA%E3%81%AE%E3%83%9F%E3%82%AF%E9%81%94%20%28event_202%29.txt#L126)；[A06](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[A07](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/076%20Echo%20my%20melody%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/076-08%20%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E9%9F%B3%E8%89%B2.txt#L19)。

判定边界：100 是四项均达本次尺度上限，不代表完美、排他或恋爱。不同 Miku 的语境须分别识别。

### 巡音流歌：[3, 3, 3, 2]，情感指数 68.75

长期师友信任与日常主动关心并存。

- **情感表达 3**：对 Luka 的安心、欣赏及希望分享美好事物的情感在不同情境中具体表现，暂支持持续的 3 档，未达到深层且稳定的 4 档。
- **信任与袒露 3**：会袒露重要朋友之间的冲突和自己的无措，后期仍能向她承认演出前不安。
- **主动投入 3**：主动拍照分享作品、想让她看见樱花，并按个人印象制作卡片，具有多种主动关心。
- **关系定位 2**：具名承认她的个人意义，并表现对她的信任；未找到与 Miku 相当的明确、深层关系定位，因此取 2。

证据：[A08](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_14%20%E5%A4%A7%E5%88%87%E3%81%A0%E3%81%8B%E3%82%89.txt#L11)；[A09](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1292_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R3%20%E7%9B%AE%E3%82%92%E4%BC%8F%E3%81%99%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%81%9D%E3%81%B0%E3%81%AB%20%28event_188%29.txt#L33)；[A10](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_056.txt#L63)；[A11](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1129_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%82%88%E3%81%97%E3%82%88%E3%81%97%E3%83%8E%E3%83%BC%E3%82%B5%E3%83%B3%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%20%28event_159%29.txt#L110)；[A12](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/054%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%A1%9C%E3%80%81%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E6%83%B3%E3%81%84%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-N25%29/054-05%20%E6%95%99%E5%AE%A4%E3%80%81%E6%A1%9C%E8%89%B2%E3%81%AE%E5%BD%BC%E5%A5%B3%E3%81%AF.txt#L51)；[A13](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)。

判定边界：情感表达的 3 档依赖跨情境的持续证据，若要求更强的直接情感宣言，可降为 2。

### KAITO：[3, 3, 3, 2]，情感指数 68.75

对理解自己、肯定自己的人的持久感谢和信任较突出。

- **情感表达 3**：主动、具体地珍视他曾说过的话，在早期谈话与后续纪念日再次表达，并非只统计谢谢的次数。
- **信任与袒露 3**：愿意承认作词中的羞耻、自我怀疑与不足，也明确希望今后继续向他咨询。
- **主动投入 3**：主动找他谈话、参与专门赠票、邀请分享食物，交往超出一次技术求助。
- **关系定位 2**：已经体现为愿意持续求助的个人支持者，但尚未找到深层关系定位的明确表述，取 2。

证据：[A14](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L33)；[A15](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0280_KAITO%20%28Ln%29_R4%20%E9%9F%B3%E3%81%A7%E8%AA%9E%E3%82%8B%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%20%28event_34%29.txt#L82)；[A16](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L60)；[A17](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L105)；[A18](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_173.txt#L86)。

判定边界：情感表达 3 不来自作词影响重大，而来自一歌主动保存并再次表达这份个人感谢；仍有 2/3 档边界。

### 镜音铃：[3, 3, 3, 2]，情感指数 68.75

加入情感后，铃的回礼、关心与陪伴证据比原成长指数更容易显现。

- **情感表达 3**：不只口头谢谢：用同样有文字的饼干回应应援，又在另一情境中明确说理解并珍惜 Rin 的心意。
- **信任与袒露 3**：能在职业取舍中说出自己真正害怕的事情，并承认两人的陪伴使自己能笑出来。
- **主动投入 3**：主动约见回礼、记得带漫画，愿意理解并回应 Rin 的愿望，支持跨情境的主动投入。
- **关系定位 2**：有个人感谢和伙伴式陪伴意义，但没有据此认定更高的特殊、稳定关系定位。

证据：[A19](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0283_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R2%20%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%BC%E3%83%AB%20%28event_34%29.txt#L154)；[A20](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1236_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%83%A1%E3%83%AA%E3%83%BC%E3%82%B4%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E3%81%A7%E3%81%84%E3%81%88%E3%83%BC%E3%81%84%EF%BC%81%20%28event_179%29.txt#L137)；[A21](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_128.txt#L129)；[A22](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L47)；[A23](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L80)。

判定边界：与 Luka、KAITO 同分只表示四档编码相同。若不把这些关心视为足够持续，情感表达或主动投入可各降 1 档。

### MEIKO：[2, 3, 2, 2]，情感指数 56.25

能够信赖并愿意回报的前辈伙伴；成长作用的强度不能直接换成情感分。

- **情感表达 2**：有具体的感谢和亲近，但目前较强的原文主要说明帮助与成长归因，暂不把它改写成深厚依恋。
- **信任与袒露 3**：面对职业抉择的不安时能够谈自己的疑惑，支持深层袒露的 3 档。
- **主动投入 2**：主动参与纪念日筹备、询问并回应她的愿望；个人主动投入成立，但本轮尚缺更充分的跨情境个别证据。
- **关系定位 2**：有具名的支持者意义与信任，未发现高档显式定位。

证据：[A26](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/25%20VS_MEIKO/0211_MEIKO%20%28Ln%29_R2%20%E7%AD%94%E3%81%88%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28event_20%29.txt#L24)；[A27](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/25%20VS_MEIKO/0784_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L68)；[A28](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L79)；[A29](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0699_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L24)。

判定边界：2 档是目前文本支持程度，不是断言感情较浅；主动投入再补到跨情境稳定证据后可上调。

### 镜音连：[2, 3, 2, 2]，情感指数 56.25

信任与袒露已有强证据，主动投入和关系定位暂采用保守值。

- **情感表达 2**：会觉得 Len 温柔，也明确感受到与两人谈话后心情变轻；个别化的持续情感表达暂不如前三组充分。
- **信任与袒露 3**：与 Rin 同场承接职业抉择的内心冲突，同样支持 3；不因两人共同在场而折半，也不升为排他信任。
- **主动投入 2**：有赠拨片、分享漫画等明确行为，但暂按具体日常分享取 2，不仅凭出现多次就认定稳定深层投入。
- **关系定位 2**：体现出可以说心事的伙伴意义，尚无强显式关系定位。

证据：[A24](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_128.txt#L137)；[A25](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_110.txt#L95)；[A22](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L47)；[A23](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L80)；[A29](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0699_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L24)。

判定边界：主动投入的 2/3 档尤其不稳：若统一把这类跨场景日常分享判为持续投入，指数会增加 6.25。

## 怎样处理共同场景、版本和重复证据

同一谈话可以证明一歌向 Rin、Len 都袒露过心事，因为两人确实共同参与并获得她的回应。但两人的关心不能自动充当一歌的主动投入；必须另找一歌的行动。

一歌在生日谈话中明确向在场六人表达“想见大家”，可以支持群体亲近的共同基础。这句不能把所有关系提升到同一深度，也不与六条个人专属告白等同。

《友情キューピッド》中一歌说“今后也希望好好相处”的对象是宁宁，不是同场的 Rin，已排除。咲希对一歌说“大好き”也不能倒记为一歌对 Rin 的表白。赏樱故事里咲希的“大好きな人”同样不是一歌的台词。

Miku 的基础身份仍覆盖一歌在正剧中听到的歌声及各 SEKAI 形象，但此轮情感满档的核心证据主要来自一歌与 School Miku 的直接关系。《４人のミク達》的“一番”在不同 Miku 之间作比较，不推成“比所有 OC、VS 都重要”，也不据此认定恋爱或独占关系。Len 的评分没有把他对其他 OC 的作用移给一歌。

生日卡中的具体行动可以用来评主动投入，但节日庆祝本身不是高分证据。没有根据生日卡的发行年份虚构经历了几年。

同一片段可为不同观察问题提供证据，例如共同演出既改变成长路径，也体现照顾对方愿望。但不把情感指数与 V3 相加，避免把相同证据在一个总分里重复奖励。

## 稳定性与后续修订

Miku 与另外五组的差异最明确，其余次序对 2/3 档边界敏感。Luka、KAITO、Rin 的情感表达若保守降一档，各为 62.50；MEIKO、Len 的主动投入若补足并升一档，各为 62.50。因此更可靠的结论是“铃的情感证据值得明显提高关注，而其余中间名次尚不足以严格区分”。这些只是规则敏感性示例，不是统计置信区间。

本轮没有改变原 V3 五项、证据账本或原始日语文件。新评分单独存放，可分别复核、撤回或修订。

## 日文来源定位

来源为 ci-ke/ProjectSekai-story 固定快照 `fdfbd5de4f28f21a326d031439feb9b0491111a5`，属于游戏剧情的第三方文本整理。本轮未逐句对照游戏画面。下列日文短句用于定位，判定依据包含所在章节完整上下文。

- **A01** [18-7 ふたりで見る桜](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-07%20%E3%81%B5%E3%81%9F%E3%82%8A%E3%81%A7%E8%A6%8B%E3%82%8B%E6%A1%9C.txt#L15)：主动邀请 Miku 看樱花、唱歌表达心意；景色因重要的人在场而特殊。

  定位短句：ミクは私にとって大切な存在

- **A02** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0004_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E5%A4%9C%E6%98%8E%E3%81%91%E5%89%8D%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84.txt#L39)：重聚后仍害怕关系再次破裂，夜里主动找 Miku 袒露难以向朋友说明的不安。

  定位短句：もしかして、ミクなら

- **A03** [101-5 憧れだけじゃなくて](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L86)：从自己的感谢转向考虑怎样让 Miku 感到快乐，筹划特别的回报。

  定位短句：もっとミクに喜んでもらえるようなこと

- **A04** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L140)：邀请 Miku 同台，让她实际感受到与大家的连接；目的包含照顾 Miku 的感受。

  定位短句：ミクに感じてほしいんだ

- **A05** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/1375_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%EF%BC%94%E4%BA%BA%E3%81%AE%E3%83%9F%E3%82%AF%E9%81%94%20%28event_202%29.txt#L126)：面对其他 SEKAI 的 Miku 时，明确安抚 School Miku 的关系位置。比较语境是不同 Miku，不据此推成对所有角色的排他宣言。

  定位短句：私の一番の先輩で、友達なのは

- **A06** [143-6 モヤモヤの正体](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)：跨越憧憬，明确定位朋友、前辈和重要存在。

  定位短句：大切な存在

- **A07** [76-8 届けたい音色](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/076%20Echo%20my%20melody%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/076-08%20%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E9%9F%B3%E8%89%B2.txt#L19)：在紧张的创作交流场合主动请 Miku 同行，事后承认她在场带来的支持。

  定位短句：今日ミクに一緒に来てもらって

- **A08** [leo_01_14 大切だから](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_14%20%E5%A4%A7%E5%88%87%E3%81%A0%E3%81%8B%E3%82%89.txt#L11)：主动向 Luka 袒露两位重要朋友的愿望冲突以及自己不知如何是好。

  定位短句：ルカ、聞いてもらっても

- **A09** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1292_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R3%20%E7%9B%AE%E3%82%92%E4%BC%8F%E3%81%99%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%81%9D%E3%81%B0%E3%81%AB%20%28event_188%29.txt#L33)：演出前承认紧张，并明确表示 Luka 的话让自己安心。

  定位短句：ルカにそう言ってもらえると、安心する

- **A10** [4 1413:areatalk_ev_band_08_004](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_056.txt#L63)：看到 Luka 的作品宣传，急忙拍照带给她，并主动约定分享 CD。

  定位短句：ルカに見せたいなって思って

- **A11** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1129_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%82%88%E3%81%97%E3%82%88%E3%81%97%E3%83%8E%E3%83%BC%E3%82%B5%E3%83%B3%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%20%28event_159%29.txt#L110)：按自己对 Luka 的个人印象制作夜空卡片，亲手赠送。

  定位短句：ルカはいつも落ち着いててかっこいい

- **A12** [54-5 教室、桜色の彼女は](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/054%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%A1%9C%E3%80%81%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E6%83%B3%E3%81%84%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-N25%29/054-05%20%E6%95%99%E5%AE%A4%E3%80%81%E6%A1%9C%E8%89%B2%E3%81%AE%E5%BD%BC%E5%A5%B3%E3%81%AF.txt#L51)：为让 Luka 亲自看见樱花而寻找、安排共同赏花。咲希的“大好きな人”不是一歌的台词，不转记。

  定位短句：ルカに実際の桜を見てもらいたい

- **A13** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)：早期已把 Luka 列为生活重新动起来的具名帮助者，只支持个人意义，不自动当情感满分。

  定位短句：咲希やミクやルカのおかげ

- **A14** [34-6 恥ずかしがらずに](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L33)：向 KAITO 展示歌词并承认表达自身想法的羞耻感；需读完整对话，不以标题判定。

  定位短句：恥ずかしい

- **A15** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0280_KAITO%20%28Ln%29_R4%20%E9%9F%B3%E3%81%A7%E8%AA%9E%E3%82%8B%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%20%28event_34%29.txt#L82)：特意早到与 KAITO 谈话，坦白不足，并希望今后继续向他倾诉、咨询。

  定位短句：これからも相談とかに乗ってくれたら嬉しい

- **A16** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L60)：纪念日主动回顾珍视的话语，向 KAITO 表达具体且持久的感谢。

  定位短句：カイトに伝えたいこともあった

- **A17** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L105)：一歌参与将特别处理的演出票赠给 KAITO，并明确希望他留着；属于群体赠礼中的个人表达。

  定位短句：カイトに持っていてほしい

- **A18** [6 2709:areatalk_monthly2508_001](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_173.txt#L86)：主动邀请 KAITO 分享自己喜爱的食物，超出技能求助。

  定位短句：カイトがよければ、一緒に食べない

- **A19** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0283_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R2%20%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%BC%E3%83%AB%20%28event_34%29.txt#L154)：特意约咲希、Rin 到场，回赠拼有感谢字样的饼干；咲希说的大好き不是一歌对 Rin 的台词。

  定位短句：私から、ふたりへのお礼

- **A20** [<サイドストーリー（後編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1236_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%83%A1%E3%83%AA%E3%83%BC%E3%82%B4%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E3%81%A7%E3%81%84%E3%81%88%E3%83%BC%E3%81%84%EF%BC%81%20%28event_179%29.txt#L137)：理解 Rin 想与伙伴分享快乐的心意，并亲口回应；不把 Rin 的单方面热情当一歌的感情。

  定位短句：リンの気持ちはすごく嬉しかった

- **A21** [8 2298:areatalk_monthly2406_001](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_128.txt#L129)：记得 Rin 的请求，带漫画续卷供她阅读。

  定位短句：リンに頼まれてたマンガの続きを

- **A22** [212-7 大事にしたいのは](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L47)：向 Rin、Len 说出职业取舍背后的恐惧与优先事项；同一谈话可分别证明向两人袒露。

  定位短句：みんなと全力で活動できなくなるのが

- **A23** [212-7 大事にしたいのは](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L80)：一歌自己的内心独白确认两人的陪伴意义；不将重大的职业话题直接等同于更深感情。

  定位短句：ひとりじゃ、こんなふうに笑えなかった

- **A24** [8 2298:areatalk_monthly2406_001](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_128.txt#L137)：一歌对 Len 体贴举动的个人评价；只是具体好感，未直接宣告深层依恋。

  定位短句：レンって優しいな

- **A25** [6 2047:areatalk_monthly2311_001](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/area/talk_event_110.txt#L95)：主动赠予适合 Len 的拨片，并想听他演奏；拨片原为杂志附赠，不夸大成特意购置的礼物。

  定位短句：このピックもらってくれない

- **A26** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/25%20VS_MEIKO/0211_MEIKO%20%28Ln%29_R2%20%E7%AD%94%E3%81%88%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28event_20%29.txt#L24)：向 MEIKO 说明职业抉择前的焦虑与尚未想明白的内心；中间对 Miku 的一句问话是回忆，不误认为本场对话对象。

  定位短句：実は、明日

- **A27** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/25%20VS_MEIKO/0784_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L68)：提前参与筹备纪念日，询问并尊重 MEIKO 的愿望，愿意帮她完成。

  定位短句：メイコがやりたいならなんでも手伝う

- **A28** [182-6 届く、繋がる](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L79)：具体感谢 MEIKO 推动作品公开。首先是成长归因，不凭这句把情感表达升到高档。

  定位短句：それに、メイコもありがとう

- **A29** [<サイドストーリー（前編）>](https://github.com/ci-ke/ProjectSekai-story/blob/fdfbd5de4f28f21a326d031439feb9b0491111a5/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0699_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L24)：在六位 VS 均明确在场的生日谈话中主动表示想见大家。支持群体亲近，不能证明六组关系同样深。

  定位短句：私がみんなに会いたいから
