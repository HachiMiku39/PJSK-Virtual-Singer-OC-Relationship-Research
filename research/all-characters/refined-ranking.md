# 全角色重新深入排序与1:1综合评分

截至2026-10-12。120组关系分别复核细分判断；20个角色内部的成长、情感、综合三套各六VS顺序均完整，未舍入值与两位小数显示均无同分。旧整数档和旧并列记录仍保留作为对照。

[交互图表](dashboard.html) · [原粗档核验与9维来源](README.md) · [120组细分判读输入](refinement-judgments.json) · [完整可复算数据](assessments.json) · [上一轮粗档并列比较](tie-review.md)

## 分数、归一与综合

**综合原平均＝（相对细分成长指数＋相对细分情感指数）÷2**，严格1:1。**综合相对分＝100×综合原平均÷该角色六VS最高综合原平均**。成长、情感、综合三套分别以各角色最高值为100；保留原平均及归一基准，使用未舍入值计算后才显示两位小数。综合展示分经过再次归一，不能直接用两个已显示单项的平均替代。归一只按该角色统一正比例缩放，不改变两项权重或原综合顺序。不同角色都可能有100，本次“无同分”限定每个角色内部。

原0–4整数档较粗，容易覆盖不同深度的关系。本轮在K、S及情感四维内部增加0/0.25/0.50/0.75子档；4档仍封顶4，C、T、B真实计数不改。每组子档由正文与实际关系内容逐对判读，不按目标名次加0.01、不按共现次数分配。先编码再检查同分，碰撞返回实际内容重新评价，算法不自动生成修正。

- 0：当前只充分支持本档的最低必要特征；结果/个人表达仍窄或依赖共同背景。
- 1：本人/对方实际行动或内容具体，但持续范围、核心程度、落实或关系意义仍有限。
- 2：本档内容较强；有清楚前后结果、本人具体认领、较深自我内容或较完整的实际主动回应。
- 3：本档上部；核心个人意义/结果与明确认领更强，或个別且有延续的实际回应更充分；仍缺下一整数档的必要条件。

细分成长原指数沿用 `50K细/4＋15C/10＋20S细/4＋10T/3＋5B/4`；细分情感原指数为四细档合计/16×100。默认成长名次按细分展示指数；旧K→S→C→T→B因果优先序保留在粗档附录，两者不是同一种排序。

**这些是有来源的研究估计。** 0.25子档不具有实验测量精度；唯一模型顺序不证明剧情客观上存在可确定的微小差距。没有人类或第二独立编码者复评。特别接近的顺序必须读作暂定，不用小数精度冒充判断把握。原核验的对象、方向、未交付行为、内心独白/口述和共同归因限制全部保留。

## 20角色综合顺序

|角色|综合顺序（左高右低）|首位综合分|
|---|---|---:|
|星乃一歌|初音未来 ＞ KAITO ＞ 巡音流歌 ＞ MEIKO ＞ 镜音铃 ＞ 镜音连|100.00|
|天马咲希|镜音铃 ＞ 巡音流歌 ＞ 镜音连 ＞ KAITO ＞ 初音未来 ＞ MEIKO|100.00|
|望月穗波|MEIKO ＞ 巡音流歌 ＞ 镜音连 ＞ 初音未来 ＞ 镜音铃 ＞ KAITO|100.00|
|日野森志步|镜音铃 ＞ 初音未来 ＞ 巡音流歌 ＞ 镜音连 ＞ KAITO ＞ MEIKO|100.00|
|花里实乃理|初音未来 ＞ 巡音流歌 ＞ 镜音铃 ＞ 镜音连 ＞ MEIKO ＞ KAITO|100.00|
|桐谷遥|MEIKO ＞ 巡音流歌 ＞ KAITO ＞ 初音未来 ＞ 镜音连 ＞ 镜音铃|100.00|
|桃井爱莉|镜音铃 ＞ KAITO ＞ 镜音连 ＞ MEIKO ＞ 巡音流歌 ＞ 初音未来|100.00|
|日野森雫|初音未来 ＞ 巡音流歌 ＞ KAITO ＞ MEIKO ＞ 镜音连 ＞ 镜音铃|100.00|
|小豆泽心羽|初音未来 ＞ 镜音铃 ＞ 镜音连 ＞ MEIKO ＞ KAITO ＞ 巡音流歌|100.00|
|白石杏|初音未来 ＞ 镜音铃 ＞ 巡音流歌 ＞ MEIKO ＞ KAITO ＞ 镜音连|100.00|
|东云彰人|镜音连 ＞ 巡音流歌 ＞ 镜音铃 ＞ MEIKO ＞ KAITO ＞ 初音未来|100.00|
|青柳冬弥|KAITO ＞ 初音未来 ＞ MEIKO ＞ 巡音流歌 ＞ 镜音铃 ＞ 镜音连|100.00|
|天马司|KAITO ＞ 巡音流歌 ＞ 初音未来 ＞ 镜音连 ＞ MEIKO ＞ 镜音铃|100.00|
|凤笑梦|MEIKO ＞ 镜音连 ＞ KAITO ＞ 镜音铃 ＞ 初音未来 ＞ 巡音流歌|100.00|
|草薙宁宁|巡音流歌 ＞ MEIKO ＞ 镜音铃 ＞ KAITO ＞ 镜音连 ＞ 初音未来|100.00|
|神代类|KAITO ＞ 巡音流歌 ＞ 初音未来 ＞ MEIKO ＞ 镜音铃 ＞ 镜音连|100.00|
|宵崎奏|初音未来 ＞ 镜音铃 ＞ 巡音流歌 ＞ KAITO ＞ 镜音连 ＞ MEIKO|100.00|
|朝比奈真冬|初音未来 ＞ 镜音铃 ＞ 镜音连 ＞ KAITO ＞ 巡音流歌 ＞ MEIKO|100.00|
|东云绘名|镜音铃 ＞ MEIKO ＞ 镜音连 ＞ KAITO ＞ 初音未来 ＞ 巡音流歌|100.00|
|晓山瑞希|MEIKO ＞ 巡音流歌 ＞ 镜音连 ＞ KAITO ＞ 初音未来 ＞ 镜音铃|100.00|

## 星乃一歌

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|KAITO|2|3|2|86.42|78.13|82.27|82.27|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|4|2|3|82.04|79.69|80.86|80.86|研究估计；来源有依据，仍需独立复评|
|MEIKO|3|5|4|82.17|65.63|73.90|73.90|暂定：综合差距不足2分，子档微调可能换位|
|镜音铃|6|4|5|69.67|76.56|73.11|73.11|研究估计；来源有依据，仍需独立复评|
|镜音连|5|6|6|72.79|60.94|66.86|66.86|该组末位；仍为研究估计|

### OC01_Miku · 初音未来

**成长细分判断：** 已确认音乐起点、长期创作身份和本人特殊归因，原上限保持。

**情感细分判断：** 深层、持续、主动回应和显式重要关系均已有证据，保留四项4。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|4,10,4,3,4|4,4,4,4|
|细档|4,10,4,3,4|4,4,4,4|

原粗档指数成长/情感 100.00 / 100.00；细分未归一原指数 100.00 / 100.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_Miku_TRIAL_G1 · 143-03 あの子との出会い.txt L80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-03%20%E3%81%82%E3%81%AE%E5%AD%90%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L80)；[OC01_Miku_TRIAL_G2 · 143-05 ミクがくれたもの.txt L64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-05%20%E3%83%9F%E3%82%AF%E3%81%8C%E3%81%8F%E3%82%8C%E3%81%9F%E3%82%82%E3%81%AE.txt#L64)；[OC01_Miku_TRIAL_G3 · 143-06 モヤモヤの正体.txt L25](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[OC01_Miku_TRIAL_G4 · leo_01_17 穂波の想い.txt L18](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L18)；[OC01_Miku_TRIAL_G5 · 018-02 ひとりぼっちの路上.txt L36](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-02%20%E3%81%B2%E3%81%A8%E3%82%8A%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%AE%E8%B7%AF%E4%B8%8A.txt#L36)；[OC01_Miku_TRIAL_G6 · 018-04 初めての拍手.txt L79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-04%20%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E6%8B%8D%E6%89%8B.txt#L79)；[OC01_Miku_TRIAL_G7 · 101-05 憧れだけじゃなくて.txt L65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L65)

**情感比较正文：** [OC01_Miku_TRIAL_A01 · 018-07 ふたりで見る桜.txt L15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/018%20%E5%90%9B%E3%81%A8%E6%AD%8C%E3%81%86%E3%80%81%E6%A1%9C%E8%88%9E%E3%81%86%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/018-07%20%E3%81%B5%E3%81%9F%E3%82%8A%E3%81%A7%E8%A6%8B%E3%82%8B%E6%A1%9C.txt#L15)；[OC01_Miku_TRIAL_A02 · 0004_星乃一歌_R4 夜明け前の語らい.txt L39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0004_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E5%A4%9C%E6%98%8E%E3%81%91%E5%89%8D%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84.txt#L39)；[OC01_Miku_TRIAL_A03 · 101-05 憧れだけじゃなくて.txt L86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/101%20%E3%81%A4%E3%81%AA%E3%81%90%E3%80%81%E6%98%9F%E3%81%AE%E6%AD%8C%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/101-05%20%E6%86%A7%E3%82%8C%E3%81%A0%E3%81%91%E3%81%98%E3%82%83%E3%81%AA%E3%81%8F%E3%81%A6.txt#L86)；[OC01_Miku_TRIAL_A04 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L140](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L140)；[OC01_Miku_TRIAL_A05 · 1375_星乃一歌_R4 ４人のミク達 (event_202).txt L126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/1375_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%EF%BC%94%E4%BA%BA%E3%81%AE%E3%83%9F%E3%82%AF%E9%81%94%20%28event_202%29.txt#L126)；[OC01_Miku_TRIAL_A06 · 143-06 モヤモヤの正体.txt L25](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[OC01_Miku_TRIAL_A07 · 076-08 届けたい音色.txt L19](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/076%20Echo%20my%20melody%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/076-08%20%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E9%9F%B3%E8%89%B2.txt#L19)

### OC01_KAITO · KAITO

**成长细分判断：** 034肯定个人表达，0594本人明确回顾持续变得能表达，核心变化和个别重大归因较直接。

**情感细分判断：** 一歌主动记住并再次向他表达感谢、谈羞耻与自我怀疑；个别关心成立，但赠票/分享部分为群体语境。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,3,2,4|3,3,3,2|
|细档|3.5,9,3.5,2,4|3.5,3.5,3.25,2.25|

原粗档指数成长/情感 77.67 / 68.75；细分未归一原指数 86.42 / 78.13。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_KAITO_TRIAL_G1 · 034-06 恥ずかしがらずに.txt L67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L67)；[OC01_KAITO_TRIAL_G2 · 0594_KAITO_RB Happy Anniversary！！2023.txt L75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L75)；[OC01_KAITO_TRIAL_G3 · talk_event_076.txt L25](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_076.txt#L25)；[OC01_KAITO_TRIAL_G4 · 121-05 バラバラな音.txt L62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-05%20%E3%83%90%E3%83%A9%E3%83%90%E3%83%A9%E3%81%AA%E9%9F%B3.txt#L62)；[OC01_KAITO_R1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L54–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L54)

**情感比较正文：** [OC01_KAITO_TRIAL_A14 · 034-06 恥ずかしがらずに.txt L33](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/034%20Knock%20the%20Future%21%21%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/034-06%20%E6%81%A5%E3%81%9A%E3%81%8B%E3%81%97%E3%81%8C%E3%82%89%E3%81%9A%E3%81%AB.txt#L33)；[OC01_KAITO_TRIAL_A15 · 0280_KAITO (Ln)_R4 音で語るセッション (event_34).txt L82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0280_KAITO%20%28Ln%29_R4%20%E9%9F%B3%E3%81%A7%E8%AA%9E%E3%82%8B%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%20%28event_34%29.txt#L82)；[OC01_KAITO_TRIAL_A16 · 0594_KAITO_RB Happy Anniversary！！2023.txt L60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L60)；[OC01_KAITO_TRIAL_A17 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L105)；[OC01_KAITO_TRIAL_A18 · talk_event_173.txt L86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_173.txt#L86)；[OC01_KAITO_R1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L54–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L54)

### OC01_Luka · 巡音流歌

**成长细分判断：** 早期重聚和后续合作/歌词有真实因果；0003早期重大归因是具名共同归因，取S3下部。

**情感细分判断：** 主线主动说朋友冲突，后期仍分享不安；照片、樱花与个人卡片覆盖多种非求助关心，同档持续性较强。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,3,2,4|3,3,3,2|
|细档|3.25,9,3.25,2,4|3.25,3.5,3.5,2.5|

原粗档指数成长/情感 77.67 / 68.75；细分未归一原指数 82.04 / 79.69。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_Luka_TRIAL_G1 · leo_01_17 穂波の想い.txt L39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_17%20%E7%A9%82%E6%B3%A2%E3%81%AE%E6%83%B3%E3%81%84.txt#L39)；[OC01_Luka_TRIAL_G2 · 0003_星乃一歌_R3 見上げる先に.txt L63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)；[OC01_Luka_TRIAL_G3 · 056-06 幸せな思い出.txt L83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/056%20Live%20with%20memories%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/056-06%20%E5%B9%B8%E3%81%9B%E3%81%AA%E6%80%9D%E3%81%84%E5%87%BA.txt#L83)；[OC01_Luka_TRIAL_G4 · 128-07 受け止めて、音に.txt L57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-07%20%E5%8F%97%E3%81%91%E6%AD%A2%E3%82%81%E3%81%A6%E3%80%81%E9%9F%B3%E3%81%AB.txt#L57)；[OC01_Luka_TRIAL_G5 · 128-08 交わる音.txt L66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-08%20%E4%BA%A4%E3%82%8F%E3%82%8B%E9%9F%B3.txt#L66)；[OC01_Luka_R1 · 0003_星乃一歌_R3 見上げる先に.txt L47–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L47)

**情感比较正文：** [OC01_Luka_TRIAL_A08 · leo_01_14 大切だから.txt L11](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_14%20%E5%A4%A7%E5%88%87%E3%81%A0%E3%81%8B%E3%82%89.txt#L11)；[OC01_Luka_TRIAL_A09 · 1292_巡音ルカ (Ln)_R3 目を伏すあなたのそばに (event_188).txt L33](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1292_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R3%20%E7%9B%AE%E3%82%92%E4%BC%8F%E3%81%99%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%81%9D%E3%81%B0%E3%81%AB%20%28event_188%29.txt#L33)；[OC01_Luka_TRIAL_A10 · talk_event_056.txt L63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_056.txt#L63)；[OC01_Luka_TRIAL_A11 · 1129_鏡音リン (Ln)_R4 よしよしノーサンキュー！ (event_159).txt L110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1129_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%82%88%E3%81%97%E3%82%88%E3%81%97%E3%83%8E%E3%83%BC%E3%82%B5%E3%83%B3%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%20%28event_159%29.txt#L110)；[OC01_Luka_TRIAL_A12 · 054-05 教室、桜色の彼女は.txt L51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/054%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%A1%9C%E3%80%81%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E6%83%B3%E3%81%84%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-N25%29/054-05%20%E6%95%99%E5%AE%A4%E3%80%81%E6%A1%9C%E8%89%B2%E3%81%AE%E5%BD%BC%E5%A5%B3%E3%81%AF.txt#L51)；[OC01_Luka_TRIAL_A13 · 0003_星乃一歌_R3 見上げる先に.txt L63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0003_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E8%A6%8B%E4%B8%8A%E3%81%92%E3%82%8B%E5%85%88%E3%81%AB.txt#L63)；[OC01_Luka_R2 · leo_01_14 大切だから.txt L1–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_14%20%E5%A4%A7%E5%88%87%E3%81%A0%E3%81%8B%E3%82%89.txt#L1)

### OC01_MEIKO · MEIKO

**成长细分判断：** 128共同创作与182公开WITH及自我价值都有本人清楚确认，核心创作结果的作用较直接。

**情感细分判断：** 0211主动来找她说明重要抉择不安，0784愿按她愿望帮筹备；比连多一条明确自发求助及愿望回应路径。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,3,2,4|2,3,2,2|
|细档|3.5,7,3.25,2,4|2.25,3.5,2.25,2.5|

原粗档指数成长/情感 74.67 / 56.25；细分未归一原指数 82.17 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_MEIKO_TRIAL_G1 · 128-07 受け止めて、音に.txt L57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-07%20%E5%8F%97%E3%81%91%E6%AD%A2%E3%82%81%E3%81%A6%E3%80%81%E9%9F%B3%E3%81%AB.txt#L57)；[OC01_MEIKO_TRIAL_G2 · 128-08 交わる音.txt L66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-08%20%E4%BA%A4%E3%82%8F%E3%82%8B%E9%9F%B3.txt#L66)；[OC01_MEIKO_TRIAL_G3 · 182-06 届く、繋がる.txt L81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L81)；[OC01_MEIKO_TRIAL_G4 · 182-06 届く、繋がる.txt L85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L85)

**情感比较正文：** [OC01_MEIKO_TRIAL_A26 · 0211_MEIKO (Ln)_R2 答えを探して (event_20).txt L24](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0211_MEIKO%20%28Ln%29_R2%20%E7%AD%94%E3%81%88%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28event_20%29.txt#L24)；[OC01_MEIKO_TRIAL_A27 · 0784_MEIKO_RB Happy Anniversary！！2023.txt L68](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0784_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L68)；[OC01_MEIKO_TRIAL_A28 · 182-06 届く、繋がる.txt L79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/182%20%E5%90%9B%E3%81%A8%E7%B9%8B%E3%81%90Heart%20Beat%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/182-06%20%E5%B1%8A%E3%81%8F%E3%80%81%E7%B9%8B%E3%81%8C%E3%82%8B.txt#L79)；[OC01_MEIKO_TRIAL_A29 · 0699_星乃一歌_RB Happy Birthday！！2023.txt L24](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0699_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L24)；[OC01_MEIKO_R1 · 0211_MEIKO (Ln)_R2 答えを探して (event_20).txt L8–50](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0211_MEIKO%20%28Ln%29_R2%20%E7%AD%94%E3%81%88%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28event_20%29.txt#L8)；[OC01_MEIKO_R2 · 0784_MEIKO_RB Happy Anniversary！！2023.txt L51–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0784_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L51)

### OC01_Rin · 镜音铃

**成长细分判断：** 受伤后替代练习实际落实；职业取舍仍共同梳理且有后续疑问，核心因果取K3下部。

**情感细分判断：** 饼干回礼和漫画为主动回应；212真实袒露但主要共同职业谈话，个人持续依靠定位仍较弱。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,3|3,3,3,2|
|细档|3,7,2.25,2,3|3.25,3.25,3.5,2.25|

原粗档指数成长/情感 68.42 / 68.75；细分未归一原指数 69.67 / 76.56。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_Rin_TRIAL_G1 · 0494_星乃一歌_R4 ひらめきを待って (event_69).txt L146](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0494_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E3%81%B2%E3%82%89%E3%82%81%E3%81%8D%E3%82%92%E5%BE%85%E3%81%A3%E3%81%A6%20%28event_69%29.txt#L146)；[OC01_Rin_TRIAL_G2 · 212-07 大事にしたいのは.txt L61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L61)；[OC01_Rin_TRIAL_G3 · 212-07 大事にしたいのは.txt L58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L58)；[OC01_Rin_TRIAL_G4 · 212-08 波紋は広がって.txt L82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-08%20%E6%B3%A2%E7%B4%8B%E3%81%AF%E5%BA%83%E3%81%8C%E3%81%A3%E3%81%A6.txt#L82)；[OC01_Rin_R2 · 0494_星乃一歌_R4 ひらめきを待って (event_69).txt L106–155](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0494_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E3%81%B2%E3%82%89%E3%82%81%E3%81%8D%E3%82%92%E5%BE%85%E3%81%A3%E3%81%A6%20%28event_69%29.txt#L106)；[OC01_Len_R3 · 212-07 大事にしたいのは.txt L15–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L15)

**情感比较正文：** [OC01_Rin_TRIAL_A19 · 0283_天馬咲希_R2 クッキー・エール (event_34).txt L154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0283_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R2%20%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%BC%E3%83%AB%20%28event_34%29.txt#L154)；[OC01_Rin_TRIAL_A20 · 1236_鏡音リン_R4 メリーゴーランドでいえーい！ (event_179).txt L137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1236_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%83%A1%E3%83%AA%E3%83%BC%E3%82%B4%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E3%81%A7%E3%81%84%E3%81%88%E3%83%BC%E3%81%84%EF%BC%81%20%28event_179%29.txt#L137)；[OC01_Rin_TRIAL_A21 · talk_event_128.txt L129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_128.txt#L129)；[OC01_Rin_TRIAL_A22 · 212-07 大事にしたいのは.txt L47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L47)；[OC01_Rin_TRIAL_A23 · 212-07 大事にしたいのは.txt L80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L80)；[OC01_Rin_R1 · 1236_鏡音リン_R4 メリーゴーランドでいえーい！ (event_179).txt L104–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1236_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%83%A1%E3%83%AA%E3%83%BC%E3%82%B4%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E3%81%A7%E3%81%84%E3%81%88%E3%83%BC%E3%81%84%EF%BC%81%20%28event_179%29.txt#L104)；[OC01_Rin_R3 · 0283_天馬咲希_R2 クッキー・エール (event_34).txt L133–169](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0283_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R2%20%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%BC%E3%83%AB%20%28event_34%29.txt#L133)；[OC01_Len_R3 · 212-07 大事にしたいのは.txt L15–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L15)

### OC01_Len · 镜音连

**成长细分判断：** 143先主动引出童年回顾，最终创作解释来自咲希；212连明确称个人活动也为大事な想い、提両立可能，并主动承诺以后随时相談。两次针对自我道路的具体梳理使K3内略前于铃的主要实务线，仍不独占决定。

**情感细分判断：** 职业深层咨询确实参与；拨片属具体分享，漫画先借提议未完成，个别投入不增加细分。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,3|2,3,2,2|
|细档|3.25,7,2.25,2,3|2.25,3.25,2,2.25|

原粗档指数成长/情感 68.42 / 56.25；细分未归一原指数 72.79 / 60.94。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC01_Len_TRIAL_G1 · 143-06 モヤモヤの正体.txt L25](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L25)；[OC01_Len_TRIAL_G2 · 212-07 大事にしたいのは.txt L61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L61)；[OC01_Len_TRIAL_G3 · 212-07 大事にしたいのは.txt L58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L58)；[OC01_Len_TRIAL_G4 · 212-08 波紋は広がって.txt L82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-08%20%E6%B3%A2%E7%B4%8B%E3%81%AF%E5%BA%83%E3%81%8C%E3%81%A3%E3%81%A6.txt#L82)；[OC01_Len_TRIAL_G5 · 143-02 しゅわしゅわとモヤモヤ.txt L83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-02%20%E3%81%97%E3%82%85%E3%82%8F%E3%81%97%E3%82%85%E3%82%8F%E3%81%A8%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4.txt#L83)；[OC01_Len_TRIAL_G6 · 1437_鏡音レン (Ln)_R3 その選択を見守って (event_212).txt L103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1437_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28Ln%29_R3%20%E3%81%9D%E3%81%AE%E9%81%B8%E6%8A%9E%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_212%29.txt#L103)；[OC01_Len_R1 · 143-02 しゅわしゅわとモヤモヤ.txt L56–88](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-02%20%E3%81%97%E3%82%85%E3%82%8F%E3%81%97%E3%82%85%E3%82%8F%E3%81%A8%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4.txt#L56)；[OC01_Len_R2 · 143-06 モヤモヤの正体.txt L1–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/143%20This%20moment%20with%20you%EF%BC%81%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/143-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%AE%E6%AD%A3%E4%BD%93.txt#L1)；[OC01_Len_R3 · 212-07 大事にしたいのは.txt L15–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L15)

**情感比较正文：** [OC01_Len_TRIAL_A24 · talk_event_128.txt L137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_128.txt#L137)；[OC01_Len_TRIAL_A25 · talk_event_110.txt L95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_110.txt#L95)；[OC01_Len_TRIAL_A22 · 212-07 大事にしたいのは.txt L47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L47)；[OC01_Len_TRIAL_A23 · 212-07 大事にしたいのは.txt L80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L80)；[OC01_Len_TRIAL_A29 · 0699_星乃一歌_RB Happy Birthday！！2023.txt L24](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0699_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L24)；[OC01_Len_Z1 · talk_event_110.txt L89–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_110.txt#L89)；[OC01_Len_Z2 · talk_event_128.txt L125–138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_128.txt#L125)；[OC01_Len_R3 · 212-07 大事にしたいのは.txt L15–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/212%20Echo%20of%20a%20Prayer%20%28Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/212-07%20%E5%A4%A7%E4%BA%8B%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%AF.txt#L15)

## 天马咲希

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|镜音铃|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|2|2|95.01|92.31|93.66|93.66|研究估计；来源有依据，仍需独立复评|
|镜音连|3|3|3|83.76|82.69|83.22|83.22|研究估计；来源有依据，仍需独立复评|
|KAITO|4|4|4|78.62|78.85|78.73|78.73|研究估计；来源有依据，仍需独立复评|
|初音未来|5|6|5|60.13|69.23|64.68|64.68|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|5|6|43.74|71.15|57.45|57.45|该组末位；仍为研究估计|

### OC02_Rin · 镜音铃

**成长细分判断：** 创作认知、合奏调整有独立作用，137对持续走到现在有具名共同重大回顾。

**情感细分判断：** 作曲困惑与恶评担忧在不同阶段真实交托；头饰、邀实现愿望是个别化回应。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,3,2,3|3,3,3,2|
|细档|3.5,9,3.5,2,3|3.5,3.5,3.5,2.5|

原粗档指数成长/情感 76.42 / 68.75；细分未归一原指数 85.17 / 81.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_Rin_G1 · 027-06 きらきら光る道しるべ.txt L10、16–17、23–37、40–44、47、50–68、71–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/027%20Unnamed%20Harmony%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/027-06%20%E3%81%8D%E3%82%89%E3%81%8D%E3%82%89%E5%85%89%E3%82%8B%E9%81%93%E3%81%97%E3%82%8B%E3%81%B9.txt#L10)；[OC02_Rin_G2 · 069-05 全力の音.txt L29–45、50–60、65–67、72–80、82–87、89、94–102、106–109、111–115、118–123、126–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-05%20%E5%85%A8%E5%8A%9B%E3%81%AE%E9%9F%B3.txt#L29)；[OC02_Rin_G3 · 121-02 嬉しいことから.txt L46–52、55–60、63–65、69–74、77–82、95–101、106–109、133–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-02%20%E5%AC%89%E3%81%97%E3%81%84%E3%81%93%E3%81%A8%E3%81%8B%E3%82%89.txt#L46)；[OC02_Rin_E6 · 137-02 不思議な感じ (天馬咲希).txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-02%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E6%84%9F%E3%81%98%20%28%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29.txt#L78)；[OC02_Rin_E4 · 1149_天馬咲希_R3 夢みたいに楽しい時間を (event_162).txt L61–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1149_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R3%20%E5%A4%A2%E3%81%BF%E3%81%9F%E3%81%84%E3%81%AB%E6%A5%BD%E3%81%97%E3%81%84%E6%99%82%E9%96%93%E3%82%92%20%28event_162%29.txt#L61)

**情感比较正文：** [OC02_Rin_G1 · 027-06 きらきら光る道しるべ.txt L10、16–17、23–37、40–44、47、50–68、71–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/027%20Unnamed%20Harmony%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/027-06%20%E3%81%8D%E3%82%89%E3%81%8D%E3%82%89%E5%85%89%E3%82%8B%E9%81%93%E3%81%97%E3%82%8B%E3%81%B9.txt#L10)；[OC02_Rin_E4 · 1149_天馬咲希_R3 夢みたいに楽しい時間を (event_162).txt L61–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1149_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R3%20%E5%A4%A2%E3%81%BF%E3%81%9F%E3%81%84%E3%81%AB%E6%A5%BD%E3%81%97%E3%81%84%E6%99%82%E9%96%93%E3%82%92%20%28event_162%29.txt#L61)；[OC02_Rin_E6 · 137-02 不思議な感じ (天馬咲希).txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-02%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E6%84%9F%E3%81%98%20%28%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29.txt#L78)；[OC02_Rin_E7 · 106-02 一緒に叶えよう.txt L9–13](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/106%20%E5%90%9B%E3%81%A8%E7%B4%A1%E3%81%90Precious%20memories%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/106-02%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%8F%B6%E3%81%88%E3%82%88%E3%81%86.txt#L9)；[OC02_Rin_E9 · 0245_鏡音リン (Ln)_R4 おてんばなメロディー (event_27).txt L92–96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0245_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%81%8A%E3%81%A6%E3%82%93%E3%81%B0%E3%81%AA%E3%83%A1%E3%83%AD%E3%83%87%E3%82%A3%E3%83%BC%20%28event_27%29.txt#L92)

### OC02_Luka · 巡音流歌

**成长细分判断：** 1承接失去时间的核心恐惧，后期重大共同回顾和个别安心归因互相补充。

**情感细分判断：** 本人请求以后私下相談、明确这样的先辈使安心，稳定求助意向比普通学习咨询更清楚。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,3,2,2|3,3,2,2|
|细档|3.5,7,3.5,2,2|3.5,3.5,2.25,2.75|

原粗档指数成长/情感 72.17 / 62.50；细分未归一原指数 80.92 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_Luka_G1 · 001-07 ゆっくり進もう.txt L52–54、59、61–76、78–80、83–87、90–91、112–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/001%20%E9%9B%A8%E4%B8%8A%E3%81%8C%E3%82%8A%E3%81%AE%E4%B8%80%E7%95%AA%E6%98%9F%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/001-07%20%E3%82%86%E3%81%A3%E3%81%8F%E3%82%8A%E9%80%B2%E3%82%82%E3%81%86.txt#L52)；[OC02_Luka_G2 · 069-03 集中特訓、開始.txt L29–31、40–42、122、125–127、130、145–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-03%20%E9%9B%86%E4%B8%AD%E7%89%B9%E8%A8%93%E3%80%81%E9%96%8B%E5%A7%8B.txt#L29)；[OC02_Luka_G3 · 069-04 不安を蹴散らして.txt L41–45、53–55、63–69、84–86、90–92、98–100、132–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-04%20%E4%B8%8D%E5%AE%89%E3%82%92%E8%B9%B4%E6%95%A3%E3%82%89%E3%81%97%E3%81%A6.txt#L41)；[OC02_Luka_E1 · 0110_巡音ルカ (Ln)_R4 黄昏の雨をぬぐって (event_1).txt L26–30](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0110_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E9%9B%A8%E3%82%92%E3%81%AC%E3%81%90%E3%81%A3%E3%81%A6%20%28event_1%29.txt#L26)；[OC02_Luka_E2 · 137-02 不思議な感じ (天馬咲希).txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-02%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E6%84%9F%E3%81%98%20%28%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29.txt#L78)；[OC02_Luka_E4 · 0110_巡音ルカ (Ln)_R4 黄昏の雨をぬぐって (event_1).txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0110_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E9%9B%A8%E3%82%92%E3%81%AC%E3%81%90%E3%81%A3%E3%81%A6%20%28event_1%29.txt#L35)

**情感比较正文：** [OC02_Luka_E1 · 0110_巡音ルカ (Ln)_R4 黄昏の雨をぬぐって (event_1).txt L26–30](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0110_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E9%9B%A8%E3%82%92%E3%81%AC%E3%81%90%E3%81%A3%E3%81%A6%20%28event_1%29.txt#L26)；[OC02_Luka_E2 · 137-02 不思議な感じ (天馬咲希).txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-02%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E6%84%9F%E3%81%98%20%28%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29.txt#L78)；[OC02_Luka_G1 · 001-07 ゆっくり進もう.txt L52–54、59、61–76、78–80、83–87、90–91、112–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/001%20%E9%9B%A8%E4%B8%8A%E3%81%8C%E3%82%8A%E3%81%AE%E4%B8%80%E7%95%AA%E6%98%9F%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/001-07%20%E3%82%86%E3%81%A3%E3%81%8F%E3%82%8A%E9%80%B2%E3%82%82%E3%81%86.txt#L52)；[OC02_Luka_E4 · 0110_巡音ルカ (Ln)_R4 黄昏の雨をぬぐって (event_1).txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0110_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E9%9B%A8%E3%82%92%E3%81%AC%E3%81%90%E3%81%A3%E3%81%A6%20%28event_1%29.txt#L35)；[OC02_Luka_E7 · talk_event_110.txt L129–133](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_110.txt#L129)

### OC02_Len · 镜音连

**成长细分判断：** 65直面住院记忆并形成创作方向，后续技艺改变归因清楚但尚非重大人生结果。

**情感细分判断：** 住院孤独与怕落后是真实本人袒露；带面包和伙伴意义具体，围绕自己的脆弱交流较集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,2,2|
|细档|3.5,7,2.25,1,2|2.25,3.5,2.5,2.5|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 71.33 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_Len_G1 · 069-04 不安を蹴散らして.txt L41–45、47–49、53–55、78、83–100、103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-04%20%E4%B8%8D%E5%AE%89%E3%82%92%E8%B9%B4%E6%95%A3%E3%82%89%E3%81%97%E3%81%A6.txt#L41)；[OC02_Len_G2 · 065-05 感情の不協和音.txt L17–19、23–25、28、34–42、44、47–48、50–54、57–63、77–84、86–88、90–100、112–118、120–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/065%20No%20seek%20No%20find%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/065-05%20%E6%84%9F%E6%83%85%E3%81%AE%E4%B8%8D%E5%8D%94%E5%92%8C%E9%9F%B3.txt#L17)；[OC02_Len_G3 · 065-07 この想い、出しきるまで.txt L28–34、36–38、56–58、63–65、77、79–80、106–114、117–119](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/065%20No%20seek%20No%20find%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/065-07%20%E3%81%93%E3%81%AE%E6%83%B3%E3%81%84%E3%80%81%E5%87%BA%E3%81%97%E3%81%8D%E3%82%8B%E3%81%BE%E3%81%A7.txt#L28)；[OC02_Len_E1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L88)；[OC02_Len_E3 · 1437_鏡音レン (Ln)_R3 その選択を見守って (event_212).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1437_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28Ln%29_R3%20%E3%81%9D%E3%81%AE%E9%81%B8%E6%8A%9E%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_212%29.txt#L100)

**情感比较正文：** [OC02_Len_E1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L88)；[OC02_Len_E2 · 069-04 不安を蹴散らして.txt L89–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-04%20%E4%B8%8D%E5%AE%89%E3%82%92%E8%B9%B4%E6%95%A3%E3%82%89%E3%81%97%E3%81%A6.txt#L89)；[OC02_Len_E3 · 1437_鏡音レン (Ln)_R3 その選択を見守って (event_212).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1437_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28Ln%29_R3%20%E3%81%9D%E3%81%AE%E9%81%B8%E6%8A%9E%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_212%29.txt#L100)；[OC02_Len_G2 · 065-05 感情の不協和音.txt L17–19、23–25、28、34–42、44、47–48、50–54、57–63、77–84、86–88、90–100、112–118、120–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/065%20No%20seek%20No%20find%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/065-05%20%E6%84%9F%E6%83%85%E3%81%AE%E4%B8%8D%E5%8D%94%E5%92%8C%E9%9F%B3.txt#L17)；[OC02_Len_G1 · 069-04 不安を蹴散らして.txt L41–45、47–49、53–55、78、83–100、103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-04%20%E4%B8%8D%E5%AE%89%E3%82%92%E8%B9%B4%E6%95%A3%E3%82%89%E3%81%97%E3%81%A6.txt#L41)；[OC02_Len_E7 · 0347_鏡音レン_RB Happy Anniversary！！.txt L41–45](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0347_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L41)

### OC02_KAITO · KAITO

**成长细分判断：** 65与121对表达/主题有具体诊断，作用清楚但与连等共同完成。

**情感细分判断：** 深层住院叙述真实听见；其后的主要关系行为为方法咨询与具名赠票，个别持续互动弱于连。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,1|2,3,2,2|
|细档|3.25,7,2.25,1,1|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 62.58 / 56.25；细分未归一原指数 66.96 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_KAITO_G1 · 065-05 感情の不協和音.txt L17–19、23–25、34–44、47–51、59–61、64–66、78–82、87–90、98–100、119–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/065%20No%20seek%20No%20find%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/065-05%20%E6%84%9F%E6%83%85%E3%81%AE%E4%B8%8D%E5%8D%94%E5%92%8C%E9%9F%B3.txt#L17)；[OC02_KAITO_G2 · 121-02 嬉しいことから.txt L49–52、55–60、63–66、69–72、74–82、88–100、107–109、130–132、136–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-02%20%E5%AC%89%E3%81%97%E3%81%84%E3%81%93%E3%81%A8%E3%81%8B%E3%82%89.txt#L49)；[OC02_KAITO_E1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L88)；[OC02_KAITO_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L13–17](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L13)

**情感比较正文：** [OC02_KAITO_E1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L88)；[OC02_KAITO_E2 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L63–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L63)；[OC02_KAITO_G1 · 065-05 感情の不協和音.txt L17–19、23–25、34–44、47–51、59–61、64–66、78–82、87–90、98–100、119–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/065%20No%20seek%20No%20find%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/065-05%20%E6%84%9F%E6%83%85%E3%81%AE%E4%B8%8D%E5%8D%94%E5%92%8C%E9%9F%B3.txt#L17)；[OC02_KAITO_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L13–17](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L13)；[OC02_KAITO_E7 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L93)

### OC02_Miku · 初音未来

**成长细分判断：** 本人确认组乐队帮助；职业觉悟仍未得到具体答案，K2保持具体行动层。

**情感细分判断：** 有演奏感谢和具体咨询，交留言卡多为应请求，定位是可求教者。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,2,2|
|细档|2.25,4,2.25,1,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 46.83 / 50.00；细分未归一原指数 51.21 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_Miku_E2 · leo_01_07 おしえてルカさん！.txt L8–12](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_07%20%E3%81%8A%E3%81%97%E3%81%88%E3%81%A6%E3%83%AB%E3%82%AB%E3%81%95%E3%82%93%EF%BC%81.txt#L8)；[OC02_Miku_G1 · 020-05 応えたい.txt L25–28、35–37、40–42、49–58、60–67、76–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/020%20Resonate%20with%20you%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/020-05%20%E5%BF%9C%E3%81%88%E3%81%9F%E3%81%84.txt#L25)；[OC02_Miku_E8 · talk_grade2.txt L187–191](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L187)；[OC02_Miku_E1 · 1455_初音ミク (Ln)_R2 久しぶりの学級会 (event_215).txt L116–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1455_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R2%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E5%AD%A6%E7%B4%9A%E4%BC%9A%20%28event_215%29.txt#L116)

**情感比较正文：** [OC02_Miku_E5 · leo_01_07 おしえてルカさん！.txt L14–18](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_07%20%E3%81%8A%E3%81%97%E3%81%88%E3%81%A6%E3%83%AB%E3%82%AB%E3%81%95%E3%82%93%EF%BC%81.txt#L14)；[OC02_Miku_G1 · 020-05 応えたい.txt L25–28、35–37、40–42、49–58、60–67、76–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/020%20Resonate%20with%20you%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/020-05%20%E5%BF%9C%E3%81%88%E3%81%9F%E3%81%84.txt#L25)；[OC02_Miku_E8 · talk_grade2.txt L187–191](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L187)；[OC02_Miku_E1 · 1455_初音ミク (Ln)_R2 久しぶりの学級会 (event_215).txt L116–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1455_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R2%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E5%AD%A6%E7%B4%9A%E4%BC%9A%20%28event_215%29.txt#L116)；[OC02_Miku_E2 · leo_01_07 おしえてルカさん！.txt L8–12](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_07%20%E3%81%8A%E3%81%97%E3%81%88%E3%81%A6%E3%83%AB%E3%82%AB%E3%81%95%E3%82%93%EF%BC%81.txt#L8)

### OC02_MEIKO · MEIKO

**成长细分判断：** 共同追问创作意图产生具体作用，最终新方法不独占给MEIKO。

**情感细分判断：** 化妆/可靠先辈的具体互动成立；帅气可靠称赞个别化，但暂无深层交托。 其中成为可靠先辈的自我疑问，比单纯技法咨询更个人化，信任细分取2.50。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,0,1|2,2,2,2|
|细档|2,4,1,0,1|2.25,2.5,2,2.5|

原粗档指数成长/情感 37.25 / 50.00；细分未归一原指数 37.25 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC02_MEIKO_F1 · 128-06 導かれる想い.txt L56–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/128%20Parallel%20Harmonies%20%28Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/128-06%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%82%8B%E6%83%B3%E3%81%84.txt#L56)；[OC02_MEIKO_E1 · talk_event_091.txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_091.txt#L59)；[OC02_MEIKO_E2 · talk_grade2.txt L228–232](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L228)

**情感比较正文：** [OC02_MEIKO_E5 · talk_grade2.txt L230–234](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L230)；[OC02_MEIKO_E1 · talk_event_091.txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_091.txt#L59)；[OC02_MEIKO_E2 · talk_grade2.txt L228–232](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L228)；[OC02_MEIKO_E4 · 0844_MEIKO (Ln)_R4 教えて！志歩先生 (event_117).txt L97–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0844_MEIKO%20%28Ln%29_R4%20%E6%95%99%E3%81%88%E3%81%A6%EF%BC%81%E5%BF%97%E6%AD%A9%E5%85%88%E7%94%9F%20%28event_117%29.txt#L97)

## 望月穗波

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|MEIKO|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|2|2|80.00|91.84|85.92|85.92|研究估计；来源有依据，仍需独立复评|
|镜音连|4|3|3|63.77|85.71|74.74|74.74|研究估计；来源有依据，仍需独立复评|
|初音未来|3|4|4|67.19|75.51|71.35|71.35|研究估计；来源有依据，仍需独立复评|
|镜音铃|5|5|5|63.27|73.47|68.37|68.37|暂定：综合差距不足2分，子档微调可能换位|
|KAITO|6|6|6|63.17|71.43|67.30|67.30|该组末位；仍为研究估计|

### OC03_MEIKO · MEIKO

**成长细分判断：** 自我排斥、队长责任与220谈话准备都触及持续核心问题，已核四线且多次具体勇气归因。

**情感细分判断：** 被排斥/恶评/队长负荷多次交托并回顾肯定，个人持续依靠证据较集中，回礼意向不算完成。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,10,2,2,3|3,3,2,2|
|细档|3.5,10,2.75,2,3|3.5,3.5,2.5,2.75|

原粗档指数成长/情感 72.92 / 62.50；细分未归一原指数 82.92 / 76.56。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_MEIKO_G1 · 010-05 優しさと勇気と.txt L7–35、66–86、94–96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/010%20%E6%8F%BA%E3%82%8C%E3%82%8B%E3%81%BE%E3%81%BE%E3%80%81%E3%81%A7%E3%82%82%E5%90%9B%E3%81%AF%E5%89%8D%E3%81%B8%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/010-05%20%E5%84%AA%E3%81%97%E3%81%95%E3%81%A8%E5%8B%87%E6%B0%97%E3%81%A8.txt#L7)；[OC03_MEIKO_G3 · 040-06 必要なケンカ.txt L23–25、39–40、46、55–61、68–72、79、81–88、92–94、99–106、108–113、123–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/040%20%E6%8F%BA%E3%82%8B%E3%81%8C%E3%81%AC%E6%83%B3%E3%81%84%E3%80%81%E4%BB%8A%E8%A8%80%E8%91%89%E3%81%AB%E3%81%97%E3%81%A6%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/040-06%20%E5%BF%85%E8%A6%81%E3%81%AA%E3%82%B1%E3%83%B3%E3%82%AB.txt#L23)；[OC03_MEIKO_G4 · 069-03 集中特訓、開始.txt L45–47、118、121–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-03%20%E9%9B%86%E4%B8%AD%E7%89%B9%E8%A8%93%E3%80%81%E9%96%8B%E5%A7%8B.txt#L45)；[OC03_MEIKO_X1 · 220-03 幼馴染みとして.txt L52–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-03%20%E5%B9%BC%E9%A6%B4%E6%9F%93%E3%81%BF%E3%81%A8%E3%81%97%E3%81%A6.txt#L52)；[OC03_MEIKO_X2 · 010-08 光を胸に.txt L32–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/010%20%E6%8F%BA%E3%82%8C%E3%82%8B%E3%81%BE%E3%81%BE%E3%80%81%E3%81%A7%E3%82%82%E5%90%9B%E3%81%AF%E5%89%8D%E3%81%B8%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/010-08%20%E5%85%89%E3%82%92%E8%83%B8%E3%81%AB.txt#L32)；[OC03_MEIKO_X3 · 220-04 週末デートは穏やかに.txt L7–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-04%20%E9%80%B1%E6%9C%AB%E3%83%87%E3%83%BC%E3%83%88%E3%81%AF%E7%A9%8F%E3%82%84%E3%81%8B%E3%81%AB.txt#L7)；[OC03_MEIKO_E3 · 137-04 もっと強く (望月穂波).txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-04%20%E3%82%82%E3%81%A3%E3%81%A8%E5%BC%B7%E3%81%8F%20%28%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29.txt#L104)

**情感比较正文：** [OC03_MEIKO_X2 · 010-08 光を胸に.txt L32–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/010%20%E6%8F%BA%E3%82%8C%E3%82%8B%E3%81%BE%E3%81%BE%E3%80%81%E3%81%A7%E3%82%82%E5%90%9B%E3%81%AF%E5%89%8D%E3%81%B8%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/010-08%20%E5%85%89%E3%82%92%E8%83%B8%E3%81%AB.txt#L32)；[OC03_MEIKO_E5 · 158-06 手ごわい子供達.txt L40–44](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/158%20%E6%98%94%E6%97%A5%E3%81%AERead-aloud%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/158-06%20%E6%89%8B%E3%81%94%E3%82%8F%E3%81%84%E5%AD%90%E4%BE%9B%E9%81%94.txt#L40)；[OC03_MEIKO_E6 · 158-02 大好きな絵本.txt L52–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/158%20%E6%98%94%E6%97%A5%E3%81%AERead-aloud%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/158-02%20%E5%A4%A7%E5%A5%BD%E3%81%8D%E3%81%AA%E7%B5%B5%E6%9C%AC.txt#L52)；[OC03_MEIKO_G1 · 010-05 優しさと勇気と.txt L7–35、66–86、94–96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/010%20%E6%8F%BA%E3%82%8C%E3%82%8B%E3%81%BE%E3%81%BE%E3%80%81%E3%81%A7%E3%82%82%E5%90%9B%E3%81%AF%E5%89%8D%E3%81%B8%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/010-05%20%E5%84%AA%E3%81%97%E3%81%95%E3%81%A8%E5%8B%87%E6%B0%97%E3%81%A8.txt#L7)；[OC03_MEIKO_E3 · 137-04 もっと強く (望月穂波).txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/137%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%A4%9C%E7%A9%BA%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%B8%20%28Ln_WL%29/137-04%20%E3%82%82%E3%81%A3%E3%81%A8%E5%BC%B7%E3%81%8F%20%28%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29.txt#L104)；[OC03_MEIKO_X1 · 220-03 幼馴染みとして.txt L52–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-03%20%E5%B9%BC%E9%A6%B4%E6%9F%93%E3%81%BF%E3%81%A8%E3%81%97%E3%81%A6.txt#L52)；[OC03_MEIKO_E7 · 158-02 大好きな絵本.txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/158%20%E6%98%94%E6%97%A5%E3%81%AERead-aloud%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/158-02%20%E5%A4%A7%E5%A5%BD%E3%81%8D%E3%81%AA%E7%B5%B5%E6%9C%AC.txt#L10)

### OC03_Luka · 巡音流歌

**成长细分判断：** 0098自信与添麻烦困惑、121方法形成两条作用，核心自我帮助较稳定。

**情感细分判断：** 主动单独谈不安、请求把脆弱说出来，后来专带苹果派回报；信任与回访比一般咨询更明确。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,1,1,2|2,3,2,2|
|细档|3.5,7,1.25,1,2|2.5,3.5,2.5,2.75|

原粗档指数成长/情感 58.83 / 56.25；细分未归一原指数 66.33 / 70.31。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_Luka_X1 · 0098_巡音ルカ (Ln)_R2 教室のセカイ.txt L62–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0098_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R2%20%E6%95%99%E5%AE%A4%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L62)；[OC03_Luka_G1 · 121-03 力になりたい.txt L9–11、14–16、19–21、24、35–36、51–53、60–62、68–73、78–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-03%20%E5%8A%9B%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%9F%E3%81%84.txt#L9)；[OC03_Luka_G2 · 121-05 バラバラな音.txt L15–17、24–26、36–40、54–57、63–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-05%20%E3%83%90%E3%83%A9%E3%83%90%E3%83%A9%E3%81%AA%E9%9F%B3.txt#L15)；[OC03_Luka_E2 · 1405_望月穂波_R4 今度はわたしが (event_207).txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1405_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E4%BB%8A%E5%BA%A6%E3%81%AF%E3%82%8F%E3%81%9F%E3%81%97%E3%81%8C%20%28event_207%29.txt#L67)

**情感比较正文：** [OC03_Luka_E4 · 1405_望月穂波_R4 今度はわたしが (event_207).txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1405_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E4%BB%8A%E5%BA%A6%E3%81%AF%E3%82%8F%E3%81%9F%E3%81%97%E3%81%8C%20%28event_207%29.txt#L67)；[OC03_Luka_E6 · leo_01_19 needLe.txt L47–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/2%20Leo%EF%BC%8Fneed/leo_01_19%20needLe.txt#L47)；[OC03_Luka_X1 · 0098_巡音ルカ (Ln)_R2 教室のセカイ.txt L62–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0098_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28Ln%29_R2%20%E6%95%99%E5%AE%A4%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L62)；[OC03_Luka_E2 · 1405_望月穂波_R4 今度はわたしが (event_207).txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1405_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E4%BB%8A%E5%BA%A6%E3%81%AF%E3%82%8F%E3%81%9F%E3%81%97%E3%81%8C%20%28event_207%29.txt#L67)；[OC03_Luka_E7 · talk_event_218.txt L247–251](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_218.txt#L247)

### OC03_Len · 镜音连

**成长细分判断：** 40直接触及怕争吵与重要同伴关系，方法被接受；归因仍以共同感谢为主。

**情感细分判断：** 真说怕与志步争吵又不愿其受苦，拨片和画本是具体个别行为，关系围绕伙伴沟通。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,0,1|2,3,2,2|
|细档|3.25,4,1,0,1|2.25,3.5,2.25,2.5|

原粗档指数成长/情感 49.75 / 56.25；细分未归一原指数 52.88 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_Len_G1 · 040-06 必要なケンカ.txt L23–25、39–40、46、49、52–55、61–68、71–78、82–87、89–99、102–123](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/040%20%E6%8F%BA%E3%82%8B%E3%81%8C%E3%81%AC%E6%83%B3%E3%81%84%E3%80%81%E4%BB%8A%E8%A8%80%E8%91%89%E3%81%AB%E3%81%97%E3%81%A6%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/040-06%20%E5%BF%85%E8%A6%81%E3%81%AA%E3%82%B1%E3%83%B3%E3%82%AB.txt#L23)；[OC03_Len_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L76–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L76)

**情感比较正文：** [OC03_Len_E2 · 040-06 必要なケンカ.txt L107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/040%20%E6%8F%BA%E3%82%8B%E3%81%8C%E3%81%AC%E6%83%B3%E3%81%84%E3%80%81%E4%BB%8A%E8%A8%80%E8%91%89%E3%81%AB%E3%81%97%E3%81%A6%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/040-06%20%E5%BF%85%E8%A6%81%E3%81%AA%E3%82%B1%E3%83%B3%E3%82%AB.txt#L107)；[OC03_Len_E3 · talk_event_060.txt L177–181](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_060.txt#L177)；[OC03_Len_G1 · 040-06 必要なケンカ.txt L23–25、39–40、46、49、52–55、61–68、71–78、82–87、89–99、102–123](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/040%20%E6%8F%BA%E3%82%8B%E3%81%8C%E3%81%AC%E6%83%B3%E3%81%84%E3%80%81%E4%BB%8A%E8%A8%80%E8%91%89%E3%81%AB%E3%81%97%E3%81%A6%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/040-06%20%E5%BF%85%E8%A6%81%E3%81%AA%E3%82%B1%E3%83%B3%E3%82%AB.txt#L23)；[OC03_Len_E6 · talk_event_203.txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_203.txt#L59)；[OC03_Len_E7 · talk_event_070.txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_070.txt#L80)；[OC03_Len_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L76–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L76)

### OC03_Miku · 初音未来

**成长细分判断：** 合奏改变和自己思考的行动有本人回顾，保持具体成长而非根基启蒙。

**情感细分判断：** 合奏对伙伴关系的意义有本人确认，但具体陪练仍偏工作性投入。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,7,2,1,2|2,2,2,2|
|细档|2.25,7,2.25,1,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 51.33 / 50.00；细分未归一原指数 55.71 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_Miku_X1 · 0082_初音ミク (Ln)_R2 教室のセカイ.txt L71–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0082_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R2%20%E6%95%99%E5%AE%A4%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L71)；[OC03_Miku_X4 · 020-05 応えたい.txt L66–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/020%20Resonate%20with%20you%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/020-05%20%E5%BF%9C%E3%81%88%E3%81%9F%E3%81%84.txt#L66)；[OC03_Miku_X2 · 0536_望月穂波_R4 思いやりも添えて (event_76).txt L102–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/0536_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%E3%82%82%E6%B7%BB%E3%81%88%E3%81%A6%20%28event_76%29.txt#L102)；[OC03_Miku_E7 · talk_grade2.txt L268–272](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L268)

**情感比较正文：** [OC03_Miku_X1 · 0082_初音ミク (Ln)_R2 教室のセカイ.txt L71–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0082_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R2%20%E6%95%99%E5%AE%A4%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L71)；[OC03_Miku_X3 · 0527_望月穂波_RB Happy Birthday！！2022.txt L14–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/0527_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812022.txt#L14)；[OC03_Miku_X2 · 0536_望月穂波_R4 思いやりも添えて (event_76).txt L102–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/0536_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%E3%82%82%E6%B7%BB%E3%81%88%E3%81%A6%20%28event_76%29.txt#L102)；[OC03_Miku_E7 · talk_grade2.txt L268–272](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L268)；[OC03_Miku_X5 · talk_event_083.txt L54–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_083.txt#L54)

### OC03_Rin · 镜音铃

**成长细分判断：** 96邀请办法被回想并落实，本人明确说成功多亏铃，具体因果归因充分。

**情感细分判断：** 本人请其倾听邀请顾虑并感谢，头纱只是提出愿望回应，未确认交付。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,2,2|
|细档|2.25,4,2.5,1,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 46.83 / 50.00；细分未归一原指数 52.46 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_Rin_X1 · 096-02 ちょっとだけ強引に.txt L37–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/096%20%E9%9A%A3%E3%81%AB%E7%AB%8B%E3%81%A4%E3%80%81%E5%84%AA%E3%81%97%E3%81%84%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/096-02%20%E3%81%A1%E3%82%87%E3%81%A3%E3%81%A8%E3%81%A0%E3%81%91%E5%BC%B7%E5%BC%95%E3%81%AB.txt#L37)；[OC03_Rin_G1 · 069-05 全力の音.txt L29–45、50–59、65–67、72–80、82–87、89、94–102、106–109、111–115、118–123、126–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-05%20%E5%85%A8%E5%8A%9B%E3%81%AE%E9%9F%B3.txt#L29)；[OC03_Rin_E3 · 096-07 心を尽くして.txt L73–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/096%20%E9%9A%A3%E3%81%AB%E7%AB%8B%E3%81%A4%E3%80%81%E5%84%AA%E3%81%97%E3%81%84%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/096-07%20%E5%BF%83%E3%82%92%E5%B0%BD%E3%81%8F%E3%81%97%E3%81%A6.txt#L73)；[OC03_Rin_E2 · talk_grade2.txt L283–287](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L283)

**情感比较正文：** [OC03_Rin_E3 · 096-07 心を尽くして.txt L73–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/096%20%E9%9A%A3%E3%81%AB%E7%AB%8B%E3%81%A4%E3%80%81%E5%84%AA%E3%81%97%E3%81%84%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/096-07%20%E5%BF%83%E3%82%92%E5%B0%BD%E3%81%8F%E3%81%97%E3%81%A6.txt#L73)；[OC03_Rin_E4 · 1191_望月穂波_R4 未来へ想いを馳せて (event_171).txt L154–158](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1191_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E6%9C%AA%E6%9D%A5%E3%81%B8%E6%83%B3%E3%81%84%E3%82%92%E9%A6%B3%E3%81%9B%E3%81%A6%20%28event_171%29.txt#L154)；[OC03_Rin_X1 · 096-02 ちょっとだけ強引に.txt L37–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/096%20%E9%9A%A3%E3%81%AB%E7%AB%8B%E3%81%A4%E3%80%81%E5%84%AA%E3%81%97%E3%81%84%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/096-02%20%E3%81%A1%E3%82%87%E3%81%A3%E3%81%A8%E3%81%A0%E3%81%91%E5%BC%B7%E5%BC%95%E3%81%AB.txt#L37)；[OC03_Rin_E6 · 0657_鏡音リン (Ln)_R3 作戦成功・ハイタッチ！ (event_96).txt L23–27](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0657_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R3%20%E4%BD%9C%E6%88%A6%E6%88%90%E5%8A%9F%E3%83%BB%E3%83%8F%E3%82%A4%E3%82%BF%E3%83%83%E3%83%81%EF%BC%81%20%28event_96%29.txt#L23)；[OC03_Rin_E1 · 096-07 心を尽くして.txt L56–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/096%20%E9%9A%A3%E3%81%AB%E7%AB%8B%E3%81%A4%E3%80%81%E5%84%AA%E3%81%97%E3%81%84%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/096-07%20%E5%BF%83%E3%82%92%E5%B0%BD%E3%81%8F%E3%81%97%E3%81%A6.txt#L56)

### OC03_KAITO · KAITO

**成长细分判断：** 合奏诊断与帮助他人方法有本人确认，阶段范围目前较窄。

**情感细分判断：** 爱犬照片仅承诺、料理属本人群体投入，不能以未交付照片判持续高档。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,7,2,0,2|2,2,2,2|
|细档|2.25,7,2.25,0,2|2.25,2.25,2,2.25|

原粗档指数成长/情感 48.00 / 50.00；细分未归一原指数 52.38 / 54.69。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC03_KAITO_G1 · 121-05 バラバラな音.txt L25–30、36–40、42–52、61–63、66–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/121%20%E5%B0%8E%E3%81%8F%E5%8B%87%E6%B0%97%E3%80%81%E5%84%AA%E3%81%97%E3%81%95%E3%82%92%E8%83%B8%E3%81%AB%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/121-05%20%E3%83%90%E3%83%A9%E3%83%90%E3%83%A9%E3%81%AA%E9%9F%B3.txt#L25)；[OC03_KAITO_X1 · 126-05 恐怖をなくすには.txt L125–172](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/126%20Rise%20as%20ONE%EF%BC%81%20%28Mix_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/126-05%20%E6%81%90%E6%80%96%E3%82%92%E3%81%AA%E3%81%8F%E3%81%99%E3%81%AB%E3%81%AF.txt#L125)；[OC03_KAITO_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L76–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L76)；[OC03_KAITO_E2 · 0900_KAITO (Ln)_R4 やんちゃな発見者 (event_126).txt L117–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0900_KAITO%20%28Ln%29_R4%20%E3%82%84%E3%82%93%E3%81%A1%E3%82%83%E3%81%AA%E7%99%BA%E8%A6%8B%E8%80%85%20%28event_126%29.txt#L117)

**情感比较正文：** [OC03_KAITO_E1 · 0594_KAITO_RB Happy Anniversary！！2023.txt L103–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L103)；[OC03_KAITO_E2 · 0900_KAITO (Ln)_R4 やんちゃな発見者 (event_126).txt L117–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0900_KAITO%20%28Ln%29_R4%20%E3%82%84%E3%82%93%E3%81%A1%E3%82%83%E3%81%AA%E7%99%BA%E8%A6%8B%E8%80%85%20%28event_126%29.txt#L117)；[OC03_KAITO_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L76–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L76)；[OC03_KAITO_X1 · 126-05 恐怖をなくすには.txt L125–172](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/126%20Rise%20as%20ONE%EF%BC%81%20%28Mix_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/126-05%20%E6%81%90%E6%80%96%E3%82%92%E3%81%AA%E3%81%8F%E3%81%99%E3%81%AB%E3%81%AF.txt#L125)；[OC03_KAITO_Y2 · 1021_望月穂波_RB Happy Birthday！！2024.txt L15–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1021_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812024.txt#L15)；[OC03_KAITO_Y3 · 215-05 みんなが喜ぶメニューを.txt L100–172](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/215%20Mix%26Make%20Party%20Time%21%21%20%28Mix_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB-VS%29/215-05%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%8C%E5%96%9C%E3%81%B6%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%92.txt#L100)；[OC03_KAITO_Y5 · 215-05 みんなが喜ぶメニューを.txt L1–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/215%20Mix%26Make%20Party%20Time%21%21%20%28Mix_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB-VS%29/215-05%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%8C%E5%96%9C%E3%81%B6%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%92.txt#L1)

## 日野森志步

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|镜音铃|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|初音未来|2|3|2|80.11|80.77|80.44|80.44|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|3|2|3|75.52|84.62|80.07|80.07|研究估计；来源有依据，仍需独立复评|
|镜音连|5|4|4|67.87|76.92|72.40|72.40|暂定：综合差距不足2分，子档微调可能换位|
|KAITO|4|6|5|75.21|69.23|72.22|72.22|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|5|6|38.86|71.15|55.01|55.01|该组末位；仍为研究估计|

### OC04_Rin · 镜音铃

**成长细分判断：** 110帮助从Iolite回顾确认目标音乐，针对核心艺术方向且本人归因明确。

**情感细分判断：** 本人认真写鼓舞、展示童年相册与目标心意，投入有个人选择及跨情境回应。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|3,3,3,2|
|细档|3.5,4,2.5,1,2|3.5,3.5,3.5,2.5|

原粗档指数成长/情感 59.33 / 68.75；细分未归一原指数 68.08 / 81.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_Rin_G1 · 110-02 それぞれの目指すもの.txt L7–8、12、14–15、24–26、29–31、54–55、61、63、71–73、79、82–84、97–109、112–115、118–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/110%20Stick%20to%20your%20faith%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/110-02%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E7%9B%AE%E6%8C%87%E3%81%99%E3%82%82%E3%81%AE.txt#L7)；[OC04_Rin_G2 · 110-08 届くように.txt L7–22、30、36–43、47–54、56–59、73–75、77–83、94–96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/110%20Stick%20to%20your%20faith%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/110-08%20%E5%B1%8A%E3%81%8F%E3%82%88%E3%81%86%E3%81%AB.txt#L7)；[OC04_Rin_G3 · 069-05 全力の音.txt L29–45、50–59、65–67、72–80、82–87、89、94–109、111–115、118–123、126–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-05%20%E5%85%A8%E5%8A%9B%E3%81%AE%E9%9F%B3.txt#L29)；[OC04_Rin_G4 · 069-06 約束の日.txt L19–21、40–43、48、50、53、59–61、63–68、73–77、86–91、110–112、121–128、142–147、149–150、155、158、163–169](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-06%20%E7%B4%84%E6%9D%9F%E3%81%AE%E6%97%A5.txt#L19)；[OC04_Rin_X1 · 1129_鏡音リン (Ln)_R4 よしよしノーサンキュー！ (event_159).txt L117–150](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1129_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%82%88%E3%81%97%E3%82%88%E3%81%97%E3%83%8E%E3%83%BC%E3%82%B5%E3%83%B3%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%20%28event_159%29.txt#L117)；[OC04_Rin_X2 · 0775_鏡音リン (Ln)_R4 思い出を聞かせて (event_110).txt L73–119](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0775_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E6%80%9D%E3%81%84%E5%87%BA%E3%82%92%E8%81%9E%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_110%29.txt#L73)

**情感比较正文：** [OC04_Rin_X1 · 1129_鏡音リン (Ln)_R4 よしよしノーサンキュー！ (event_159).txt L117–150](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1129_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E3%82%88%E3%81%97%E3%82%88%E3%81%97%E3%83%8E%E3%83%BC%E3%82%B5%E3%83%B3%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%20%28event_159%29.txt#L117)；[OC04_Rin_G2 · 110-08 届くように.txt L7–22、30、36–43、47–54、56–59、73–75、77–83、94–96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/110%20Stick%20to%20your%20faith%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/110-08%20%E5%B1%8A%E3%81%8F%E3%82%88%E3%81%86%E3%81%AB.txt#L7)；[OC04_Rin_G1 · 110-02 それぞれの目指すもの.txt L7–8、12、14–15、24–26、29–31、54–55、61、63、71–73、79、82–84、97–109、112–115、118–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/110%20Stick%20to%20your%20faith%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/110-02%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E7%9B%AE%E6%8C%87%E3%81%99%E3%82%82%E3%81%AE.txt#L7)；[OC04_Rin_X2 · 0775_鏡音リン (Ln)_R4 思い出を聞かせて (event_110).txt L73–119](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0775_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28Ln%29_R4%20%E6%80%9D%E3%81%84%E5%87%BA%E3%82%92%E8%81%9E%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_110%29.txt#L73)

### OC04_Miku · 初音未来

**成长细分判断：** 与Luka共同推动赏月，另有针对练习盲点的个别菜单支持；该具体作用使K2内略前。

**情感细分判断：** 姐姐歉疚/咲希担忧真实交托，团子和初诣邀请有个别行动但定位表述较一般。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,2,2|2,3,2,2|
|细档|2.25,4,2.25,2,2|2.25,3.5,2.25,2.5|

原粗档指数成长/情感 50.17 / 56.25；细分未归一原指数 54.54 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_Miku_X1 · 0277_初音ミク (Ln)_R3 屋上での語らい (event_33).txt L18–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0277_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R3%20%E5%B1%8B%E4%B8%8A%E3%81%A7%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_33%29.txt#L18)；[OC04_Miku_X2 · 0111_日野森志歩_R4 気づきたかった熱さ (event_1).txt L19–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0111_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%B0%97%E3%81%A5%E3%81%8D%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E7%86%B1%E3%81%95%20%28event_1%29.txt#L19)；[OC04_Miku_F1 · talk_grade2.txt L335–349](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L335)

**情感比较正文：** [OC04_Miku_X1 · 0277_初音ミク (Ln)_R3 屋上での語らい (event_33).txt L18–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0277_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R3%20%E5%B1%8B%E4%B8%8A%E3%81%A7%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_33%29.txt#L18)；[OC04_Miku_E1 · 0111_日野森志歩_R4 気づきたかった熱さ (event_1).txt L49–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0111_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%B0%97%E3%81%A5%E3%81%8D%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E7%86%B1%E3%81%95%20%28event_1%29.txt#L49)；[OC04_Miku_X2 · 0111_日野森志歩_R4 気づきたかった熱さ (event_1).txt L19–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0111_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%B0%97%E3%81%A5%E3%81%8D%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E7%86%B1%E3%81%95%20%28event_1%29.txt#L19)；[OC04_Miku_E5 · 045-03 それぞれのお正月.txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/045%20%E7%A5%88%E3%82%8A%E3%81%AE%E5%85%88%20%E9%A1%98%E3%81%86%E6%98%8E%E6%97%A5%E3%81%AF%20%28Mix_%E6%A1%90%E8%B0%B7%E9%81%A5%29/045-03%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E3%81%8A%E6%AD%A3%E6%9C%88.txt#L10)；[OC04_Miku_F1 · talk_grade2.txt L335–349](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L335)

### OC04_Luka · 巡音流歌

**成长细分判断：** 赏月为共同推动，后期实际陪练成立；未再确认独立K2结果，核心作用与Miku很接近。

**情感细分判断：** 同样听姐姐/咲希脆弱，专程团子回报且本人说頼りにしてます，定位与求助连续性略强。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,2,2|2,3,2,2|
|细档|2,4,2.25,2,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 50.17 / 56.25；细分未归一原指数 51.42 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_Miku_X1 · 0277_初音ミク (Ln)_R3 屋上での語らい (event_33).txt L18–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0277_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R3%20%E5%B1%8B%E4%B8%8A%E3%81%A7%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_33%29.txt#L18)；[OC04_Miku_X2 · 0111_日野森志歩_R4 気づきたかった熱さ (event_1).txt L19–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0111_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%B0%97%E3%81%A5%E3%81%8D%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E7%86%B1%E3%81%95%20%28event_1%29.txt#L19)；[OC04_Luka_F1 · 1263_日野森志歩_R4 日々のルーティーン (event_182).txt L53–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1263_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%97%A5%E3%80%85%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%83%B3%20%28event_182%29.txt#L53)；[OC04_Luka_E1 · talk_event_069.txt L5–9](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_069.txt#L5)

**情感比较正文：** [OC04_Luka_E1 · talk_event_069.txt L5–9](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_069.txt#L5)；[OC04_Miku_X1 · 0277_初音ミク (Ln)_R3 屋上での語らい (event_33).txt L18–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0277_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28Ln%29_R3%20%E5%B1%8B%E4%B8%8A%E3%81%A7%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_33%29.txt#L18)；[OC04_Miku_X2 · 0111_日野森志歩_R4 気づきたかった熱さ (event_1).txt L19–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0111_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%B0%97%E3%81%A5%E3%81%8D%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E7%86%B1%E3%81%95%20%28event_1%29.txt#L19)；[OC04_Luka_F1 · 1263_日野森志歩_R4 日々のルーティーン (event_182).txt L53–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1263_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%97%A5%E3%80%85%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%83%B3%20%28event_182%29.txt#L53)

### OC04_Len · 镜音连

**成长细分判断：** 0493针对她伤害朋友的自责作具体肯定，本人接受；尚未具名归因长期人际改变。

**情感细分判断：** 0493深层自责口述清楚，但带谱及之后合作主要是具体训练关系，持续定位较弱。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,1,2|2,3,2,2|
|细档|2.25,4,1.25,1,2|2.25,3.25,2.25,2.25|

原粗档指数成长/情感 41.83 / 56.25；细分未归一原指数 46.21 / 62.50。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_Len_F1 · 1393_鏡音レン_R4 きらめきは重なって (event_205).txt L53–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1393_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3_R4%20%E3%81%8D%E3%82%89%E3%82%81%E3%81%8D%E3%81%AF%E9%87%8D%E3%81%AA%E3%81%A3%E3%81%A6%20%28event_205%29.txt#L53)；[OC04_Len_E1 · 0495_天馬咲希_R4 ムキムキになっちゃった！？ (event_69).txt L107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0495_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E3%83%A0%E3%82%AD%E3%83%A0%E3%82%AD%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F%EF%BC%81%EF%BC%9F%20%28event_69%29.txt#L107)；[OC04_Len_E2 · 0964_日野森志歩_R4 この電車に乗る時 (event_137).txt L112–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0964_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E3%81%93%E3%81%AE%E9%9B%BB%E8%BB%8A%E3%81%AB%E4%B9%97%E3%82%8B%E6%99%82%20%28event_137%29.txt#L112)；[OC04_Len_Y6 · 0493_日野森志歩_R4 全力のステージ (event_69).txt L10–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0493_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E5%85%A8%E5%8A%9B%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%20%28event_69%29.txt#L10)；[OC04_Len_Y4 · 0316_星乃一歌_R3 新曲の方向性 (event_40).txt L8–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0316_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E6%96%B0%E6%9B%B2%E3%81%AE%E6%96%B9%E5%90%91%E6%80%A7%20%28event_40%29.txt#L8)；[OC04_Len_Y8 · 1487_日野森志歩_R2 この夢を目指して (event_220).txt L21–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1487_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%93%E3%81%AE%E5%A4%A2%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6%20%28event_220%29.txt#L21)

**情感比较正文：** [OC04_Len_Y6 · 0493_日野森志歩_R4 全力のステージ (event_69).txt L10–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0493_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E5%85%A8%E5%8A%9B%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%20%28event_69%29.txt#L10)；[OC04_Len_E1 · 0495_天馬咲希_R4 ムキムキになっちゃった！？ (event_69).txt L107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0495_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E3%83%A0%E3%82%AD%E3%83%A0%E3%82%AD%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F%EF%BC%81%EF%BC%9F%20%28event_69%29.txt#L107)；[OC04_Len_E2 · 0964_日野森志歩_R4 この電車に乗る時 (event_137).txt L112–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0964_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E3%81%93%E3%81%AE%E9%9B%BB%E8%BB%8A%E3%81%AB%E4%B9%97%E3%82%8B%E6%99%82%20%28event_137%29.txt#L112)；[OC04_Len_Y1 · 110-08 届くように.txt L12–90](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/110%20Stick%20to%20your%20faith%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/110-08%20%E5%B1%8A%E3%81%8F%E3%82%88%E3%81%86%E3%81%AB.txt#L12)；[OC04_Len_Y8 · 1487_日野森志歩_R2 この夢を目指して (event_220).txt L21–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1487_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%93%E3%81%AE%E5%A4%A2%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6%20%28event_220%29.txt#L21)；[OC04_Len_E3 · talk_event_110.txt L158–162](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_110.txt#L158)；[OC04_Len_Y4 · 0316_星乃一歌_R3 新曲の方向性 (event_40).txt L8–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/0316_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R3%20%E6%96%B0%E6%9B%B2%E3%81%AE%E6%96%B9%E5%90%91%E6%80%A7%20%28event_40%29.txt#L8)；[OC04_Len_Y7 · 1394_日野森志歩_R4 想いと熱を込めて (event_205).txt L85–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1394_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%83%B3%E3%81%84%E3%81%A8%E7%86%B1%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28event_205%29.txt#L85)

### OC04_KAITO · KAITO

**成长细分判断：** 示范—模仿—弹成难点的过程和本人归因完整，K2实务结果明确。

**情感细分判断：** 具体陪练、设计咨询和群体赠票，以技术合作为主，暂无深层袒露。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,1|2,2,2,2|
|细档|2.25,4,2.5,1,1|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 45.58 / 50.00；细分未归一原指数 51.21 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_KAITO_G1 · 069-03 集中特訓、開始.txt L10–16、24–29、43–50、52–53、57–75、77–90、134–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-03%20%E9%9B%86%E4%B8%AD%E7%89%B9%E8%A8%93%E3%80%81%E9%96%8B%E5%A7%8B.txt#L10)；[OC04_KAITO_G2 · 069-05 全力の音.txt L33–35、101–106、119–121、127–134、137–139、141–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-05%20%E5%85%A8%E5%8A%9B%E3%81%AE%E9%9F%B3.txt#L33)；[OC04_KAITO_X1 · 0964_日野森志歩_R4 この電車に乗る時 (event_137).txt L113–153](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0964_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E3%81%93%E3%81%AE%E9%9B%BB%E8%BB%8A%E3%81%AB%E4%B9%97%E3%82%8B%E6%99%82%20%28event_137%29.txt#L113)

**情感比较正文：** [OC04_KAITO_G1 · 069-03 集中特訓、開始.txt L10–16、24–29、43–50、52–53、57–75、77–90、134–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/069%20Don%27t%20lose%20faith%21%20%28Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/069-03%20%E9%9B%86%E4%B8%AD%E7%89%B9%E8%A8%93%E3%80%81%E9%96%8B%E5%A7%8B.txt#L10)；[OC04_KAITO_E3 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L77–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L77)；[OC04_KAITO_X1 · 0964_日野森志歩_R4 この電車に乗る時 (event_137).txt L113–153](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0964_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E3%81%93%E3%81%AE%E9%9B%BB%E8%BB%8A%E3%81%AB%E4%B9%97%E3%82%8B%E6%99%82%20%28event_137%29.txt#L113)；[OC04_KAITO_E4 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L104)；[OC04_KAITO_E6 · 0594_KAITO_RB Happy Anniversary！！2023.txt L49–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0594_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L49)；[OC03_KAITO_X2 · 0685_KAITO (Ln)_R4 見守ってきた軌跡 (event_101).txt L92–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0685_KAITO%20%28Ln%29_R4%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E8%BB%8C%E8%B7%A1%20%28event_101%29.txt#L92)

### OC04_MEIKO · MEIKO

**成长细分判断：** 0159缓解说重话的紧绷，实际行动改变未核，保持K1的个人情绪帮助。

**情感细分判断：** 真实口述仅言辞重，较深自责是内心独白；书法/选玩具及可倾诉意义是具体双向关系。 明确向其承认对穗波说得过重属于个人自责分享，信任细分2.50；内心中学自责仍不口述计3。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,1|2,2,2,2|
|细档|1.25,0,1.25,1,1|2.25,2.5,2,2.5|

原粗档指数成长/情感 22.08 / 50.00；细分未归一原指数 26.46 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC04_MEIKO_F1 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L72–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L72)；[OC04_MEIKO_X1 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L8–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L8)；[OC04_MEIKO_X2 · 117-02 いざ、初売りへ！.txt L59–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/117%20%E5%A4%89%E3%82%8F%E3%82%89%E3%81%AC%E3%81%82%E3%81%9F%E3%81%9F%E3%81%8B%E3%81%95%E3%81%AE%E9%9A%A3%E3%81%A7%20%28Mix_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/117-02%20%E3%81%84%E3%81%96%E3%80%81%E5%88%9D%E5%A3%B2%E3%82%8A%E3%81%B8%EF%BC%81.txt#L59)；[OC04_MEIKO_E2 · 0209_天馬咲希_R4 窓辺の語らい (event_20).txt L83–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0209_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E7%AA%93%E8%BE%BA%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_20%29.txt#L83)

**情感比较正文：** [OC04_MEIKO_E3 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L93)；[OC04_MEIKO_E2 · 0209_天馬咲希_R4 窓辺の語らい (event_20).txt L83–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/0209_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E7%AA%93%E8%BE%BA%E3%81%AE%E8%AA%9E%E3%82%89%E3%81%84%20%28event_20%29.txt#L83)；[OC04_MEIKO_X1 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L8–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L8)；[OC04_MEIKO_Z1 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L47–106](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L47)；[OC04_MEIKO_X2 · 117-02 いざ、初売りへ！.txt L59–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/117%20%E5%A4%89%E3%82%8F%E3%82%89%E3%81%AC%E3%81%82%E3%81%9F%E3%81%9F%E3%81%8B%E3%81%95%E3%81%AE%E9%9A%A3%E3%81%A7%20%28Mix_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/117-02%20%E3%81%84%E3%81%96%E3%80%81%E5%88%9D%E5%A3%B2%E3%82%8A%E3%81%B8%EF%BC%81.txt#L59)；[OC04_MEIKO_F1 · 0159_日野森志歩_R2 いろんな優しさ (event_10).txt L72–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/0159_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%84%E3%82%8D%E3%82%93%E3%81%AA%E5%84%AA%E3%81%97%E3%81%95%20%28event_10%29.txt#L72)

## 花里实乃理

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|2|1|100.00|97.73|98.86|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|1|2|90.95|100.00|95.47|96.57|研究估计；来源有依据，仍需独立复评|
|镜音铃|4|3|3|64.78|95.45|80.12|81.04|研究估计；来源有依据，仍需独立复评|
|镜音连|5|4|4|58.35|93.18|75.77|76.64|暂定：综合差距不足2分，子档微调可能换位|
|MEIKO|3|6|5|73.54|75.00|74.27|75.12|研究估计；来源有依据，仍需独立复评|
|KAITO|6|5|6|34.17|81.82|57.99|58.66|该组末位；仍为研究估计|

### OC05_Miku · 初音未来

**成长细分判断：** 主线使憧憬转为行动、17帮助自我认识，重要自我问题的直接作用较强。

**情感细分判断：** 怕成为负担与帮不了遥是真实交托，愿共唱和按愿望庆生；主动行动仍偏共同活动。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,2,2|
|细档|3.5,7,2.25,1,2|2.25,3.5,2.25,2.75|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 71.33 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_Miku_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、85、91–92、94–101、104–106、108–112、117–121、129–135、138–140、142–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Miku_G3 · 017-07 わたしにしかできないこと.txt L7–12、15–17、22、30–32、36–39、41–42、48、75–77、82–84、92–94、99–100、106–109、112–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-07%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AB%E3%81%97%E3%81%8B%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8.txt#L7)；[OC05_Miku_G4 · mmj_01_16 青色の景色.txt L7–9、11、14–18、20、23–25、28–42、50–55、57、67–71、103–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_16%20%E9%9D%92%E8%89%B2%E3%81%AE%E6%99%AF%E8%89%B2.txt#L7)；[OC05_Miku_G5 · mmj_01_18 あの日見た希望.txt L8–10、21、23–25、27、33–35、74–76、79–81、87–98、111–113、122–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L8)；[OC05_Miku_X1 · 017-06 思いがけない出会い.txt L78–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-06%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%87%BA%E4%BC%9A%E3%81%84.txt#L78)

**情感比较正文：** [OC05_Miku_E1 · 0019_花里みのり_R3 ライブ前夜の決意.txt L43–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/05%20MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A/0019_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A_R3%20%E3%83%A9%E3%82%A4%E3%83%96%E5%89%8D%E5%A4%9C%E3%81%AE%E6%B1%BA%E6%84%8F.txt#L43)；[OC05_Miku_E2 · mmj_01_19 アイドル新鋭隊.txt L24–28](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_19%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E6%96%B0%E9%8B%AD%E9%9A%8A.txt#L24)；[OC05_Miku_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、85、91–92、94–101、104–106、108–112、117–121、129–135、138–140、142–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Miku_G4 · mmj_01_16 青色の景色.txt L7–9、11、14–18、20、23–25、28–42、50–55、57、67–71、103–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_16%20%E9%9D%92%E8%89%B2%E3%81%AE%E6%99%AF%E8%89%B2.txt#L7)；[OC05_Miku_E5 · 1234_初音ミク_RB Happy Anniversary！！2025.txt L25–29](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1234_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L25)；[OC05_Rin_E4 · mmj_01_19 アイドル新鋭隊.txt L54–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_19%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E6%96%B0%E9%8B%AD%E9%9A%8A.txt#L54)；[OC05_Miku_X1 · 017-06 思いがけない出会い.txt L78–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-06%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%87%BA%E4%BC%9A%E3%81%84.txt#L78)

### OC05_Luka · 巡音流歌

**成长细分判断：** 独有价值提问参与核心自我认识，实际发现亦有粉丝，作用保留共同背景。

**情感细分判断：** 追不上队友/成为负担直接托付，周年medley按愿望设计且实现、长期教学认可较清楚。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,0,2|2,3,2,2|
|细档|3.25,7,2.25,0,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 60.50 / 56.25；细分未归一原指数 64.88 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_Luka_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、91–92、94–95、100–102、105–106、108、112–114、116–125、127–129、133–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Luka_G2 · 017-06 思いがけない出会い.txt L1–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-06%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%87%BA%E4%BC%9A%E3%81%84.txt#L1)；[OC05_Luka_G3 · 017-07 わたしにしかできないこと.txt L7–17、22–27、30–32、35–42、48、75–77、82–84、92–94、99–100、106–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-07%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AB%E3%81%97%E3%81%8B%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8.txt#L7)；[OC05_Miku_X1 · 017-06 思いがけない出会い.txt L78–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-06%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%87%BA%E4%BC%9A%E3%81%84.txt#L78)；[OC05_Luka_X1 · 0860_巡音ルカ_RB Happy Anniversary！！2024.txt L17–45](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0860_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L17)

**情感比较正文：** [OC05_Luka_E1 · 0415_花里みのり_RB Happy Birthday！！.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/05%20MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A/0415_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A_RB%20Happy%20Birthday%EF%BC%81%EF%BC%81.txt#L38)；[OC05_Luka_E3 · 0193_巡音ルカ (MMJ)_R3 アイドルとしての心得 (event_17).txt L95–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0193_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28MMJ%29_R3%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E5%BF%83%E5%BE%97%20%28event_17%29.txt#L95)；[OC05_Luka_X1 · 0860_巡音ルカ_RB Happy Anniversary！！2024.txt L17–45](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0860_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L17)；[OC05_Luka_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、91–92、94–95、100–102、105–106、108、112–114、116–125、127–129、133–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Luka_G3 · 017-07 わたしにしかできないこと.txt L7–17、22–27、30–32、35–42、48、75–77、82–84、92–94、99–100、106–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-07%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AB%E3%81%97%E3%81%8B%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8.txt#L7)

### OC05_Rin · 镜音铃

**成长细分判断：** 实际舞台陪同与鼓励有具体作用，但主线决定性提议由Miku提出。

**情感细分判断：** 共同听主线自我怀疑，明确先辈定位及希望再live，亲近明确但尚缺更完整个别回访。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,1,2|2,3,2,2|
|细档|2.25,4,1.25,1,2|2.25,3.25,2.5,2.5|

原粗档指数成长/情感 41.83 / 56.25；细分未归一原指数 46.21 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_Rin_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、95–99、103–106、108、117–130、133–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Rin_G2 · 017-07 わたしにしかできないこと.txt L9–14、16–17、22、30–32、37–42、48、75–77、82–84、92–94、99–100、106–109、111–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-07%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AB%E3%81%97%E3%81%8B%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8.txt#L9)；[OC05_Rin_G3 · mmj_01_16 青色の景色.txt L7–9、11–18、20、23–25、28–32、35–39、42–43、45–48、50–51、53–55、57、60、62、65–68、101–106、108–111、114–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_16%20%E9%9D%92%E8%89%B2%E3%81%AE%E6%99%AF%E8%89%B2.txt#L7)；[OC05_Rin_G4 · mmj_01_18 あの日見た希望.txt L8–10、21、23–25、27、33–35、75–77、79–81、87–95、110–113、122–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L8)

**情感比较正文：** [OC05_Rin_E1 · 0088_初音ミク (MMJ)_R4 みんなにお披露目.txt L25–29](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0088_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28MMJ%29_R4%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AB%E3%81%8A%E6%8A%AB%E9%9C%B2%E7%9B%AE.txt#L25)；[OC05_Rin_E2 · 0415_花里みのり_RB Happy Birthday！！.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/05%20MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A/0415_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A_RB%20Happy%20Birthday%EF%BC%81%EF%BC%81.txt#L38)；[OC05_Rin_E3 · mmj_01_07 アイドル達の葛藤.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_07%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E9%81%94%E3%81%AE%E8%91%9B%E8%97%A4.txt#L38)；[OC05_Rin_G1 · 017-05 プロとして必要なこと.txt L47–49、79–83、95–99、103–106、108、117–130、133–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/017%20%E5%B1%8A%E3%81%91%EF%BC%81HOPEFUL%20STAGE%E2%99%AA%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/017-05%20%E3%83%97%E3%83%AD%E3%81%A8%E3%81%97%E3%81%A6%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%93%E3%81%A8.txt#L47)；[OC05_Rin_G3 · mmj_01_16 青色の景色.txt L7–9、11–18、20、23–25、28–32、35–39、42–43、45–48、50–51、53–55、57、60、62、65–68、101–106、108–111、114–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_16%20%E9%9D%92%E8%89%B2%E3%81%AE%E6%99%AF%E8%89%B2.txt#L7)；[OC05_Rin_E4 · mmj_01_19 アイドル新鋭隊.txt L54–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_19%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E6%96%B0%E9%8B%AD%E9%9A%8A.txt#L54)；[OC05_Rin_E5 · talk_grade2.txt L569–573](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L569)

### OC05_Len · 镜音连

**成长细分判断：** 98模拟帮助学校/工作矛盾的方法被采用，具体归因多为感谢而非重大确认。

**情感细分判断：** 学校与工作焦虑是真实袒露；205邀活动是另一SEKAI，不能扩成MMJ人格长期关系。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,0,1|2,3,2,2|
|细档|2.25,4,1.25,0,1|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 37.25 / 56.25；细分未归一原指数 41.63 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_Len_F1 · 098-01 単位制にいくために.txt L68–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/098%20STEP%20by%20STEP%EF%BC%81%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/098-01%20%E5%8D%98%E4%BD%8D%E5%88%B6%E3%81%AB%E3%81%84%E3%81%8F%E3%81%9F%E3%82%81%E3%81%AB.txt#L68)；[OC05_Len_E2 · 098-02 アイドルまっしぐらバージョンは.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/098%20STEP%20by%20STEP%EF%BC%81%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/098-02%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%BE%E3%81%A3%E3%81%97%E3%81%90%E3%82%89%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AF.txt#L38)

**情感比较正文：** [OC05_Len_E1 · 1453_鏡音レン (MMJ)_R4 花咲くレン談義 (event_215).txt L90–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1453_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R4%20%E8%8A%B1%E5%92%B2%E3%81%8F%E3%83%AC%E3%83%B3%E8%AB%87%E7%BE%A9%20%28event_215%29.txt#L90)；[OC05_Len_E4 · 0415_花里みのり_RB Happy Birthday！！.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/05%20MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A/0415_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A_RB%20Happy%20Birthday%EF%BC%81%EF%BC%81.txt#L38)；[OC05_Len_E6 · talk_grade2.txt L585–589](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L585)；[OC05_Len_F1 · 098-01 単位制にいくために.txt L68–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/098%20STEP%20by%20STEP%EF%BC%81%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/098-01%20%E5%8D%98%E4%BD%8D%E5%88%B6%E3%81%AB%E3%81%84%E3%81%8F%E3%81%9F%E3%82%81%E3%81%AB.txt#L68)；[OC05_Len_E2 · 098-02 アイドルまっしぐらバージョンは.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/098%20STEP%20by%20STEP%EF%BC%81%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/098-02%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%BE%E3%81%A3%E3%81%97%E3%81%90%E3%82%89%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AF.txt#L38)；[OC05_Len_X2 · 1394_日野森志歩_R4 想いと熱を込めて (event_205).txt L117–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1394_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%83%B3%E3%81%84%E3%81%A8%E7%86%B1%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28event_205%29.txt#L117)

### OC05_MEIKO · MEIKO

**成长细分判断：** 呼吸练习后确实改善访谈，方法及结果的具体归因充分。

**情感细分判断：** 具体求助和頼り称赞成立，参与庆祝不是个人专门赠礼，投入仍低档。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,1,2|
|细档|2.25,4,2.5,1,2|2.25,2.25,1.25,2.5|

原粗档指数成长/情感 46.83 / 43.75；细分未归一原指数 52.46 / 51.56。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_MEIKO_F1 · 0593_MEIKO (MMJ)_R2 もっともっと支えるために (event_85).txt L13–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0593_MEIKO%20%28MMJ%29_R2%20%E3%82%82%E3%81%A3%E3%81%A8%E3%82%82%E3%81%A3%E3%81%A8%E6%94%AF%E3%81%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%20%28event_85%29.txt#L13)；[OC05_MEIKO_E4 · talk_event_183.txt L70–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_183.txt#L70)

**情感比较正文：** [OC05_MEIKO_F1 · 0593_MEIKO (MMJ)_R2 もっともっと支えるために (event_85).txt L13–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0593_MEIKO%20%28MMJ%29_R2%20%E3%82%82%E3%81%A3%E3%81%A8%E3%82%82%E3%81%A3%E3%81%A8%E6%94%AF%E3%81%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%20%28event_85%29.txt#L13)；[OC05_MEIKO_E4 · talk_event_183.txt L70–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_183.txt#L70)；[OC05_MEIKO_X1 · 1277_MEIKO_RB Happy Anniversary！！2025.txt L95–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1277_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L95)

### OC05_KAITO · KAITO

**成长细分判断：** 行业知识、安全和演前鼓励是明确具体帮助，未核核心改变。

**情感细分判断：** 本人整装看纪念直播并评论是主动行动，但主要职业学习与具体欣赏。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,0,2|2,2,2,2|
|细档|1.25,0,1.25,0,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 20.00 / 50.00；细分未归一原指数 24.38 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC05_KAITO_F1 · 0519_桃井愛莉_R4 ワンマン作戦会議！ (event_73).txt L75–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0519_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%83%AF%E3%83%B3%E3%83%9E%E3%83%B3%E4%BD%9C%E6%88%A6%E4%BC%9A%E8%AD%B0%EF%BC%81%20%28event_73%29.txt#L75)；[OC05_KAITO_E2 · talk_event_043.txt L95–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_043.txt#L95)；[OC05_KAITO_E3 · 0333_KAITO (MMJ)_R3 アイドル兼マネージャー！？ (event_43).txt L96–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0333_KAITO%20%28MMJ%29_R3%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E5%85%BC%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%EF%BC%81%EF%BC%9F%20%28event_43%29.txt#L96)；[OC05_KAITO_X1 · talk_event_051.txt L105–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_051.txt#L105)

**情感比较正文：** [OC05_KAITO_E1 · 0519_桃井愛莉_R4 ワンマン作戦会議！ (event_73).txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0519_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%83%AF%E3%83%B3%E3%83%9E%E3%83%B3%E4%BD%9C%E6%88%A6%E4%BC%9A%E8%AD%B0%EF%BC%81%20%28event_73%29.txt#L88)；[OC05_KAITO_E3 · 0333_KAITO (MMJ)_R3 アイドル兼マネージャー！？ (event_43).txt L96–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0333_KAITO%20%28MMJ%29_R3%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E5%85%BC%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%EF%BC%81%EF%BC%9F%20%28event_43%29.txt#L96)；[OC05_KAITO_X1 · talk_event_051.txt L105–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_051.txt#L105)；[OC05_KAITO_X2 · 0379_KAITO_RB Happy Anniversary！！.txt L42–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0379_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L42)；[OC05_KAITO_F1 · 0519_桃井愛莉_R4 ワンマン作戦会議！ (event_73).txt L75–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0519_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%83%AF%E3%83%B3%E3%83%9E%E3%83%B3%E4%BD%9C%E6%88%A6%E4%BC%9A%E8%AD%B0%EF%BC%81%20%28event_73%29.txt#L75)

## 桐谷遥

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|MEIKO|1|2|1|100.00|97.73|98.86|100.00|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|2|1|2|96.03|100.00|98.02|99.14|研究估计；来源有依据，仍需独立复评|
|KAITO|3|6|3|90.24|86.36|88.30|89.32|研究估计；来源有依据，仍需独立复评|
|初音未来|4|4|4|77.67|93.18|85.43|86.41|研究估计；来源有依据，仍需独立复评|
|镜音连|5|3|5|64.99|95.45|80.22|81.15|研究估计；来源有依据，仍需独立复评|
|镜音铃|6|5|6|59.48|88.64|74.06|74.91|该组末位；仍为研究估计|

### OC06_MEIKO · MEIKO

**成长细分判断：** 78职业初心的反思和85新一步回顾有连续因果，多问题支持。

**情感细分判断：** 本人职业责任与伤害粉丝恐惧详细交托，训练和跳绳回应保留具体/未交付边界。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,2|2,3,2,2|
|细档|3.5,9,2.5,1,2|2.25,3.5,2.5,2.5|

原粗档指数成长/情感 66.83 / 56.25；细分未归一原指数 75.58 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_MEIKO_G1 · 023-07 やりたいこと、ひとつ.txt L13–17、19–20、22、33–35、41–44、49、55–56、62、69、71–73、75、84–86、92–94、117–122、125–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/023%20%E9%A0%91%E5%BC%B5%E3%82%8B%E3%81%82%E3%81%AA%E3%81%9F%E3%81%ABBreak%20Time%EF%BC%81%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/023-07%20%E3%82%84%E3%82%8A%E3%81%9F%E3%81%84%E3%81%93%E3%81%A8%E3%80%81%E3%81%B2%E3%81%A8%E3%81%A4.txt#L13)；[OC06_MEIKO_G2 · 078-04 想いの届けかた.txt L9–11、23–25、53、59–61、71–73、79–86、90–103、112、118–119、122–125、128–129、132–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/078%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%A4%A2%E3%81%AE%E3%80%81%E5%BD%BC%E6%96%B9%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/078-04%20%E6%83%B3%E3%81%84%E3%81%AE%E5%B1%8A%E3%81%91%E3%81%8B%E3%81%9F.txt#L9)；[OC06_MEIKO_G3 · 078-05 アイドルのルーツ.txt L12–13、19–21、34–36、39–41、44–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/078%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%A4%A2%E3%81%AE%E3%80%81%E5%BD%BC%E6%96%B9%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/078-05%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%84.txt#L12)；[OC06_MEIKO_E1 · 0996_MEIKO (MMJ)_R3 夢に近づくトレーニング♪ (event_142).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0996_MEIKO%20%28MMJ%29_R3%20%E5%A4%A2%E3%81%AB%E8%BF%91%E3%81%A5%E3%81%8F%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E2%99%AA%20%28event_142%29.txt#L12)；[OC06_MEIKO_E2 · 0592_桐谷遥_R3 帰ってきたこの場所 (event_85).txt L150–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/0592_%E6%A1%90%E8%B0%B7%E9%81%A5_R3%20%E5%B8%B0%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%20%28event_85%29.txt#L150)；[OC06_MEIKO_X1 · talk_event_078.txt L56–76](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_078.txt#L56)

**情感比较正文：** [OC06_MEIKO_E1 · 0996_MEIKO (MMJ)_R3 夢に近づくトレーニング♪ (event_142).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0996_MEIKO%20%28MMJ%29_R3%20%E5%A4%A2%E3%81%AB%E8%BF%91%E3%81%A5%E3%81%8F%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E2%99%AA%20%28event_142%29.txt#L12)；[OC06_MEIKO_E2 · 0592_桐谷遥_R3 帰ってきたこの場所 (event_85).txt L150–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/0592_%E6%A1%90%E8%B0%B7%E9%81%A5_R3%20%E5%B8%B0%E3%81%A3%E3%81%A6%E3%81%8D%E3%81%9F%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%20%28event_85%29.txt#L150)；[OC06_MEIKO_G2 · 078-04 想いの届けかた.txt L9–11、23–25、53、59–61、71–73、79–86、90–103、112、118–119、122–125、128–129、132–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/078%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%A4%A2%E3%81%AE%E3%80%81%E5%BD%BC%E6%96%B9%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/078-04%20%E6%83%B3%E3%81%84%E3%81%AE%E5%B1%8A%E3%81%91%E3%81%8B%E3%81%9F.txt#L9)；[OC06_MEIKO_X1 · talk_event_078.txt L56–76](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_078.txt#L56)

### OC06_Luka · 巡音流歌

**成长细分判断：** 157罪疚与1110解开迷惑明确前后相连，核心自我变化的个人渠道较清楚。

**情感细分判断：** 真实讲夺走希望的内疚，另专带联想到其脸颊的点心；个别求助和关心更集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,2,2|
|细档|3.5,7,2.5,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 72.58 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_Luka_F1 · talk_event_023.txt L159–168](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_023.txt#L159)；[OC06_Luka_X2 · 157-06 後悔も、未来も.txt L26–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/157%20Rise%20and%20Strive%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/157-06%20%E5%BE%8C%E6%82%94%E3%82%82%E3%80%81%E6%9C%AA%E6%9D%A5%E3%82%82.txt#L26)；[OC06_Luka_X1 · 1110_桐谷遥_R4 突きつけられた現実 (event_157).txt L40–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/1110_%E6%A1%90%E8%B0%B7%E9%81%A5_R4%20%E7%AA%81%E3%81%8D%E3%81%A4%E3%81%91%E3%82%89%E3%82%8C%E3%81%9F%E7%8F%BE%E5%AE%9F%20%28event_157%29.txt#L40)

**情感比较正文：** [OC06_Luka_E5 · 0266_桐谷遥_R4 小さなファンと一緒に (event_31).txt L71–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/0266_%E6%A1%90%E8%B0%B7%E9%81%A5_R4%20%E5%B0%8F%E3%81%95%E3%81%AA%E3%83%95%E3%82%A1%E3%83%B3%E3%81%A8%E4%B8%80%E7%B7%92%E3%81%AB%20%28event_31%29.txt#L71)；[OC06_Luka_E6 · 0483_MEIKO (MMJ)_R4 まずは腹筋の強化から！ (event_67).txt L101–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0483_MEIKO%20%28MMJ%29_R4%20%E3%81%BE%E3%81%9A%E3%81%AF%E8%85%B9%E7%AD%8B%E3%81%AE%E5%BC%B7%E5%8C%96%E3%81%8B%E3%82%89%EF%BC%81%20%28event_67%29.txt#L101)；[OC06_Luka_X2 · 157-06 後悔も、未来も.txt L26–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/157%20Rise%20and%20Strive%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/157-06%20%E5%BE%8C%E6%82%94%E3%82%82%E3%80%81%E6%9C%AA%E6%9D%A5%E3%82%82.txt#L26)；[OC06_Luka_E7 · talk_event_157.txt L36–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_157.txt#L36)；[OC06_Luka_X1 · 1110_桐谷遥_R4 突きつけられた現実 (event_157).txt L40–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/1110_%E6%A1%90%E8%B0%B7%E9%81%A5_R4%20%E7%AA%81%E3%81%8D%E3%81%A4%E3%81%91%E3%82%89%E3%82%8C%E3%81%9F%E7%8F%BE%E5%AE%9F%20%28event_157%29.txt#L40)

### OC06_KAITO · KAITO

**成长细分判断：** 粉丝合作与职业特色实际两线，归因包含共同思考、实乃理和团队作用。

**情感细分判断：** 核心粉丝担忧真实听见，但周年仅同看，不能借实乃理的个人行动提高投入。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,1,2|
|细档|3.25,7,2.25,1,2|2.25,3.5,1.25,2.5|

原粗档指数成长/情感 63.83 / 50.00；细分未归一原指数 68.21 / 59.38。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_KAITO_G1 · 043-04 アイドルでマネージャー？.txt L12–13、19、25–26、28–29、40–41、47、59–70、73–76、79–81、87、94–99、101–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/043%20MOREMOREMakingXmas%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/043-04%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%EF%BC%9F.txt#L12)；[OC06_KAITO_G2 · 043-05 踏み出す一歩.txt L29–34、46、52–53、59–60、73–75、93–95、100–102、123、129–132](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/043%20MOREMOREMakingXmas%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/043-05%20%E8%B8%8F%E3%81%BF%E5%87%BA%E3%81%99%E4%B8%80%E6%AD%A9.txt#L29)；[OC06_KAITO_G3 · 133-04 私達の個性は.txt L9、12–13、16–20、22–24、28–38、40–50、61、67、69、75–80、86、93–95、97–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/133%20Lead%20to%20shine%20more%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/133-04%20%E7%A7%81%E9%81%94%E3%81%AE%E5%80%8B%E6%80%A7%E3%81%AF.txt#L9)

**情感比较正文：** [OC06_KAITO_E1 · 1010_桐谷遥_RB Happy Birthday！！2024.txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/1010_%E6%A1%90%E8%B0%B7%E9%81%A5_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812024.txt#L39)；[OC06_KAITO_E2 · 1057_桐谷遥_R4 誇りに思えるようなアイドルに.txt L44–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/1057_%E6%A1%90%E8%B0%B7%E9%81%A5_R4%20%E8%AA%87%E3%82%8A%E3%81%AB%E6%80%9D%E3%81%88%E3%82%8B%E3%82%88%E3%81%86%E3%81%AA%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%AB.txt#L44)；[OC06_KAITO_E3 · 073-01 ワンマンライブ直前！.txt L87–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/073%20%E6%8B%9D%E5%95%93%E3%80%81%E3%81%82%E3%81%AE%E9%A0%83%E3%81%AE%E3%82%8F%E3%81%9F%E3%81%97%E3%81%B8%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/073-01%20%E3%83%AF%E3%83%B3%E3%83%9E%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%96%E7%9B%B4%E5%89%8D%EF%BC%81.txt#L87)；[OC06_KAITO_G1 · 043-04 アイドルでマネージャー？.txt L12–13、19、25–26、28–29、40–41、47、59–70、73–76、79–81、87、94–99、101–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/043%20MOREMOREMakingXmas%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/043-04%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%EF%BC%9F.txt#L12)；[OC06_KAITO_G3 · 133-04 私達の個性は.txt L9、12–13、16–20、22–24、28–38、40–50、61、67、69、75–80、86、93–95、97–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/133%20Lead%20to%20shine%20more%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/133-04%20%E7%A7%81%E9%81%94%E3%81%AE%E5%80%8B%E6%80%A7%E3%81%AF.txt#L9)；[OC05_KAITO_X2 · 0379_KAITO_RB Happy Anniversary！！.txt L42–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0379_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L42)

### OC06_Miku · 初音未来

**成长细分判断：** 主线追问意愿且帮她再上台，关键劝说仍有实乃理，个人成果归因较弱。

**情感细分判断：** 78核心职业困惑真实听见，但与其他多位共同；分享照片是个人行动，暂无更强特殊定位。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|2,3,2,2|
|细档|3.25,4,1.25,1,2|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 54.33 / 56.25；细分未归一原指数 58.71 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_Miku_G1 · mmj_01_18 あの日見た希望.txt L10–12、24–25、27、50、56–57、59–60、67–68、74–80、96–98、111–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L10)；[OC06_Miku_X1 · mmj_01_18 あの日見た希望.txt L96–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L96)；[OC06_MEIKO_G2 · 078-04 想いの届けかた.txt L9–11、23–25、53、59–61、71–73、79–86、90–103、112、118–119、122–125、128–129、132–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/078%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%A4%A2%E3%81%AE%E3%80%81%E5%BD%BC%E6%96%B9%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/078-04%20%E6%83%B3%E3%81%84%E3%81%AE%E5%B1%8A%E3%81%91%E3%81%8B%E3%81%9F.txt#L9)

**情感比较正文：** [OC06_Miku_E2 · talk_event_218.txt L7–11](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_218.txt#L7)；[OC06_Miku_E3 · mmj_01_07 アイドル達の葛藤.txt L11–15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_07%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E9%81%94%E3%81%AE%E8%91%9B%E8%97%A4.txt#L11)；[OC06_MEIKO_G2 · 078-04 想いの届けかた.txt L9–11、23–25、53、59–61、71–73、79–86、90–103、112、118–119、122–125、128–129、132–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/078%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%A4%A2%E3%81%AE%E3%80%81%E5%BD%BC%E6%96%B9%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/078-04%20%E6%83%B3%E3%81%84%E3%81%AE%E5%B1%8A%E3%81%91%E3%81%8B%E3%81%9F.txt#L9)；[OC06_Miku_E8 · 0644_初音ミク (MMJ)_R4 横浜ガイドはグルメの予感♪ (event_94).txt L101–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0644_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28MMJ%29_R4%20%E6%A8%AA%E6%B5%9C%E3%82%AC%E3%82%A4%E3%83%89%E3%81%AF%E3%82%B0%E3%83%AB%E3%83%A1%E3%81%AE%E4%BA%88%E6%84%9F%E2%99%AA%20%28event_94%29.txt#L101)；[OC06_Miku_E5 · 098-08 変わらない想い.txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/098%20STEP%20by%20STEP%EF%BC%81%20%28MMJ_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/098-08%20%E5%A4%89%E3%82%8F%E3%82%89%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L100)

### OC06_Len · 镜音连

**成长细分判断：** 舞步窍门本人具名归因明确，133职业解释主要KAITO而非連。

**情感细分判断：** 主动邀练、已赠哑铃、实际播放节目构成持续行动；本人袒露目前仍具体工作选择问题。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,0,2|2,2,3,2|
|细档|2.25,4,2.5,0,2|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 43.50 / 56.25；细分未归一原指数 49.13 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_Len_E2 · 1049_桃井愛莉_R2 ひとりのファンとして (event_151).txt L11–15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1049_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R2%20%E3%81%B2%E3%81%A8%E3%82%8A%E3%81%AE%E3%83%95%E3%82%A1%E3%83%B3%E3%81%A8%E3%81%97%E3%81%A6%20%28event_151%29.txt#L11)；[OC06_Len_E3 · talk_event_122.txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_122.txt#L93)；[OC06_Len_F1 · 0942_鏡音レン (MMJ)_R2 個性をもっと輝かせて (event_133).txt L88–106](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0942_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R2%20%E5%80%8B%E6%80%A7%E3%82%92%E3%82%82%E3%81%A3%E3%81%A8%E8%BC%9D%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_133%29.txt#L88)；[OC06_Len_X1 · 133-04 私達の個性は.txt L79–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/133%20Lead%20to%20shine%20more%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/133-04%20%E7%A7%81%E9%81%94%E3%81%AE%E5%80%8B%E6%80%A7%E3%81%AF.txt#L79)；[OC06_Len_X2 · 0942_鏡音レン (MMJ)_R2 個性をもっと輝かせて (event_133).txt L8–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0942_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R2%20%E5%80%8B%E6%80%A7%E3%82%92%E3%82%82%E3%81%A3%E3%81%A8%E8%BC%9D%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_133%29.txt#L8)；[OC06_Len_X3 · 133-04 私達の個性は.txt L50–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/133%20Lead%20to%20shine%20more%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/133-04%20%E7%A7%81%E9%81%94%E3%81%AE%E5%80%8B%E6%80%A7%E3%81%AF.txt#L50)

**情感比较正文：** [OC06_Len_E1 · 0942_鏡音レン (MMJ)_R2 個性をもっと輝かせて (event_133).txt L91–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0942_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R2%20%E5%80%8B%E6%80%A7%E3%82%92%E3%82%82%E3%81%A3%E3%81%A8%E8%BC%9D%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_133%29.txt#L91)；[OC06_Len_E2 · 1049_桃井愛莉_R2 ひとりのファンとして (event_151).txt L11–15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1049_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R2%20%E3%81%B2%E3%81%A8%E3%82%8A%E3%81%AE%E3%83%95%E3%82%A1%E3%83%B3%E3%81%A8%E3%81%97%E3%81%A6%20%28event_151%29.txt#L11)；[OC06_Len_E3 · talk_event_122.txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_122.txt#L93)；[OC06_Len_F1 · 0942_鏡音レン (MMJ)_R2 個性をもっと輝かせて (event_133).txt L88–106](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0942_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R2%20%E5%80%8B%E6%80%A7%E3%82%92%E3%82%82%E3%81%A3%E3%81%A8%E8%BC%9D%E3%81%8B%E3%81%9B%E3%81%A6%20%28event_133%29.txt#L88)；[OC06_Len_Z1 · talk_event_122.txt L89–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_122.txt#L89)

### OC06_Rin · 镜音铃

**成长细分判断：** 具体灯海提示与舞台陪同真实，核心心理转折不独占。

**情感细分判断：** 邀请购物、关心签名等活动是本人主动，具体双向交往比单次被祝福充分。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,1,1|2,2,2,2|
|细档|2.25,4,1.25,1,1|2.25,2.5,2.5,2.5|

原粗档指数成长/情感 40.58 / 50.00；细分未归一原指数 44.96 / 60.94。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC06_Rin_G1 · mmj_01_18 あの日見た希望.txt L10–12、24–25、27、50、56–57、59–60、67–68、74–80、110–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L10)；[OC06_Miku_X1 · mmj_01_18 あの日見た希望.txt L96–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L96)；[OC06_Rin_E2 · 011-02 セカイの新アイドル！？.txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-02%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%EF%BC%81%EF%BC%9F.txt#L104)

**情感比较正文：** [OC06_Rin_E6 · mmj_01_07 アイドル達の葛藤.txt L11–15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_07%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E9%81%94%E3%81%AE%E8%91%9B%E8%97%A4.txt#L11)；[OC06_Rin_E5 · 011-02 セカイの新アイドル！？.txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-02%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%EF%BC%81%EF%BC%9F.txt#L104)；[OC06_Rin_E2 · 011-02 セカイの新アイドル！？.txt L104–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-02%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%EF%BC%81%EF%BC%9F.txt#L104)；[OC06_Rin_X1 · 0424_鏡音リン (MMJ)_R4 もっと頼ってほしいんだ♪ (event_57).txt L29–66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0424_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R4%20%E3%82%82%E3%81%A3%E3%81%A8%E9%A0%BC%E3%81%A3%E3%81%A6%E3%81%BB%E3%81%97%E3%81%84%E3%82%93%E3%81%A0%E2%99%AA%20%28event_57%29.txt#L29)；[OC06_Rin_E3 · talk_event_168.txt L110–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_168.txt#L110)；[OC06_Rin_G1 · mmj_01_18 あの日見た希望.txt L10–12、24–25、27、50、56–57、59–60、67–68、74–80、110–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/3%20MORE%20MORE%20JUMP%EF%BC%81/mmj_01_18%20%E3%81%82%E3%81%AE%E6%97%A5%E8%A6%8B%E3%81%9F%E5%B8%8C%E6%9C%9B.txt#L10)

## 桃井爱莉

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|镜音铃|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|KAITO|2|2|2|91.25|92.45|91.85|91.85|研究估计；来源有依据，仍需独立复评|
|镜音连|3|4|3|82.60|83.02|82.81|82.81|研究估计；来源有依据，仍需独立复评|
|MEIKO|4|3|4|64.83|86.79|75.81|75.81|研究估计；来源有依据，仍需独立复评|
|巡音流歌|5|6|5|63.29|69.81|66.55|66.55|研究估计；来源有依据，仍需独立复评|
|初音未来|6|5|6|34.24|77.36|55.80|55.80|该组末位；仍为研究估计|

### OC07_Rin · 镜音铃

**成长细分判断：** 0091回到职业梦想的共同重大归因与经营探索有核心作用，非只实务陪伴。

**情感细分判断：** 过去综艺与旧友痛苦真实听见、本人制作糖偶并邀共同上台，长期个人回应较明确。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,3,2,2|3,3,3,2|
|细档|3.5,7,3.5,2,2|3.5,3.5,3.5,2.75|

原粗档指数成长/情感 72.17 / 68.75；细分未归一原指数 80.92 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_Rin_X1 · 005-06 どんな時も、笑顔で.txt L40–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/005%20%E3%81%93%E3%81%93%E3%81%8B%E3%82%89RE%EF%BC%9ASTART%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/005-06%20%E3%81%A9%E3%82%93%E3%81%AA%E6%99%82%E3%82%82%E3%80%81%E7%AC%91%E9%A1%94%E3%81%A7.txt#L40)；[OC07_Rin_X2 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L17–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L17)；[OC07_Rin_G1 · 031-06 アイドルとして.txt L9–16、20–31、43–45、48–50、58–64、80–82、94–96、124–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/031%20%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%83%BB%E3%83%A9%E3%83%96%E3%83%AA%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%96%E3%83%AA%E3%83%87%E3%82%A4%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/031-06%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6.txt#L9)；[OC07_Rin_E4 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L38)；[OC07_Rin_E5 · 1004_鏡音リン_R4 わたしの知らない『わたし』達.txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1004_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AE%E7%9F%A5%E3%82%89%E3%81%AA%E3%81%84%E3%80%8E%E3%82%8F%E3%81%9F%E3%81%97%E3%80%8F%E9%81%94.txt#L78)；[OC07_Miku_F1 · 138-05 理想を追うために.txt L34–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L34)；[OC07_Rin_X3 · 138-05 理想を追うために.txt L10–35](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L10)

**情感比较正文：** [OC07_Rin_E3 · 0611_桃井愛莉_RB Happy Birthday！！2023.txt L28–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0611_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812023.txt#L28)；[OC07_Rin_E4 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L38)；[OC07_Rin_E5 · 1004_鏡音リン_R4 わたしの知らない『わたし』達.txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1004_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_R4%20%E3%82%8F%E3%81%9F%E3%81%97%E3%81%AE%E7%9F%A5%E3%82%89%E3%81%AA%E3%81%84%E3%80%8E%E3%82%8F%E3%81%9F%E3%81%97%E3%80%8F%E9%81%94.txt#L78)；[OC07_Rin_X1 · 005-06 どんな時も、笑顔で.txt L40–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/005%20%E3%81%93%E3%81%93%E3%81%8B%E3%82%89RE%EF%BC%9ASTART%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/005-06%20%E3%81%A9%E3%82%93%E3%81%AA%E6%99%82%E3%82%82%E3%80%81%E7%AC%91%E9%A1%94%E3%81%A7.txt#L40)；[OC07_Rin_G1 · 031-06 アイドルとして.txt L9–16、20–31、43–45、48–50、58–64、80–82、94–96、124–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/031%20%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%83%BB%E3%83%A9%E3%83%96%E3%83%AA%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%96%E3%83%AA%E3%83%87%E3%82%A4%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/031-06%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6.txt#L9)；[OC07_Miku_X1 · 092-05 忘れられない記憶.txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L35)；[OC07_Rin_X2 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L17–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L17)

### OC07_KAITO · KAITO

**成长细分判断：** 旧友疏远和跨域顾虑均促本人行动，涉及持续职业/人际核心问题。

**情感细分判断：** 主动回访讲结果、珍惜所说的话并托付被贬低/旧友痛苦，个别咨询连续性比一般共同听众更强。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,3|3,3,2,2|
|细档|3.5,7,2.5,1,3|3.5,3.5,2.5,2.75|

原粗档指数成长/情感 65.08 / 62.50；细分未归一原指数 73.83 / 76.56。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_KAITO_F1 · 198-05 今の自分にできること.txt L34–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/198%20Open%20up%20new%20horizons%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/198-05%20%E4%BB%8A%E3%81%AE%E8%87%AA%E5%88%86%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L34)；[OC07_KAITO_X2 · 0633_KAITO (MMJ)_R3 消えない想いを信じて (event_92).txt L99–142](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0633_KAITO%20%28MMJ%29_R3%20%E6%B6%88%E3%81%88%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84%E3%82%92%E4%BF%A1%E3%81%98%E3%81%A6%20%28event_92%29.txt#L99)；[OC07_KAITO_E2 · talk_event_057.txt L128–132](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_057.txt#L128)；[OC07_KAITO_E5 · 1267_桃井愛莉_R4 ヒヤッとドッキリ！ (event_183).txt L99–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1267_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%83%92%E3%83%A4%E3%83%83%E3%81%A8%E3%83%89%E3%83%83%E3%82%AD%E3%83%AA%EF%BC%81%20%28event_183%29.txt#L99)

**情感比较正文：** [OC07_KAITO_X2 · 0633_KAITO (MMJ)_R3 消えない想いを信じて (event_92).txt L99–142](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0633_KAITO%20%28MMJ%29_R3%20%E6%B6%88%E3%81%88%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84%E3%82%92%E4%BF%A1%E3%81%98%E3%81%A6%20%28event_92%29.txt#L99)；[OC07_KAITO_E5 · 1267_桃井愛莉_R4 ヒヤッとドッキリ！ (event_183).txt L99–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1267_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%83%92%E3%83%A4%E3%83%83%E3%81%A8%E3%83%89%E3%83%83%E3%82%AD%E3%83%AA%EF%BC%81%20%28event_183%29.txt#L99)；[OC07_KAITO_F1 · 198-05 今の自分にできること.txt L34–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/198%20Open%20up%20new%20horizons%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/198-05%20%E4%BB%8A%E3%81%AE%E8%87%AA%E5%88%86%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L34)；[OC07_KAITO_X1 · talk_event_052.txt L90–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_052.txt#L90)

### OC07_Len · 镜音连

**成长细分判断：** 从她为人设计MC反推旧时希望，直接重识职业自我，具名说心情转轻。

**情感细分判断：** 对自己的综艺否定/理想能实际交托，并主动为连设计MC，个别理解渠道较Miku共同听众集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,2,2|
|细档|3.5,4,2.25,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 59.33 / 56.25；细分未归一原指数 66.83 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_Len_G1 · 031-06 アイドルとして.txt L7–10、15–17、21–30、44–65、73、80–82、94–96、124–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/031%20%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%83%BB%E3%83%A9%E3%83%96%E3%83%AA%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%96%E3%83%AA%E3%83%87%E3%82%A4%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/031-06%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6.txt#L7)；[OC07_Len_E3 · 1220_桃井愛莉_R4 スペシャルコラボ配信！ (event_176).txt L132–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1220_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%B3%E3%83%A9%E3%83%9C%E9%85%8D%E4%BF%A1%EF%BC%81%20%28event_176%29.txt#L132)；[OC07_Miku_F1 · 138-05 理想を追うために.txt L34–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L34)

**情感比较正文：** [OC07_Len_G1 · 031-06 アイドルとして.txt L7–10、15–17、21–30、44–65、73、80–82、94–96、124–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/031%20%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%83%BB%E3%83%A9%E3%83%96%E3%83%AA%E3%83%BC%E3%83%BB%E3%82%A8%E3%83%96%E3%83%AA%E3%83%87%E3%82%A4%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/031-06%20%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6.txt#L7)；[OC07_Len_E3 · 1220_桃井愛莉_R4 スペシャルコラボ配信！ (event_176).txt L132–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1220_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%B3%E3%83%A9%E3%83%9C%E9%85%8D%E4%BF%A1%EF%BC%81%20%28event_176%29.txt#L132)；[OC07_Len_E2 · talk_event_085.txt L126–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_085.txt#L126)

### OC07_MEIKO · MEIKO

**成长细分判断：** 168本人明确采用伸展后顺畅，实务方法归因完整，214仍具体取稿协助。

**情感细分判断：** 专属活动、搬箱、邀朋友/同练形成持续回报；深层旧事多共同交流，定位未特殊。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,3,3,2|
|细档|2.25,4,2.5,1,2|2.25,3.25,3.5,2.5|

原粗档指数成长/情感 46.83 / 62.50；细分未归一原指数 52.46 / 71.88。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_MEIKO_E6 · 1176_MEIKO (MMJ)_R4 レッツ・モアモアトレーニング！ (event_168).txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1176_MEIKO%20%28MMJ%29_R4%20%E3%83%AC%E3%83%83%E3%83%84%E3%83%BB%E3%83%A2%E3%82%A2%E3%83%A2%E3%82%A2%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_168%29.txt#L109)；[OC07_MEIKO_F1 · 214-04 抱きしめた声 (MEIKO).txt L7–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/214%20Again%20And%20Again%20Ambition%EF%BC%81%20%28Mix_WL%29/214-04%20%E6%8A%B1%E3%81%8D%E3%81%97%E3%82%81%E3%81%9F%E5%A3%B0%20%28MEIKO%29.txt#L7)；[OC07_MEIKO_E5 · talk_event_067.txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_067.txt#L82)

**情感比较正文：** [OC07_MEIKO_E1 · 214-01 思いがけない光.txt L55–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/214%20Again%20And%20Again%20Ambition%EF%BC%81%20%28Mix_WL%29/214-01%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%85%89.txt#L55)；[OC07_MEIKO_E2 · 1446_桃井愛莉_R4 夢の力になるものは (event_214).txt L16–20](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1446_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E5%A4%A2%E3%81%AE%E5%8A%9B%E3%81%AB%E3%81%AA%E3%82%8B%E3%82%82%E3%81%AE%E3%81%AF%20%28event_214%29.txt#L16)；[OC07_MEIKO_E3 · 067-08 ワンマン成功祈願！.txt L22–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/067%20%E9%9D%92%E7%A9%BA%E3%81%AE%E5%85%88%E3%80%81%E8%BC%9D%E3%81%8D%E3%82%92%E8%BF%BD%E3%81%84%E3%81%8B%E3%81%91%E3%81%A6%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/067-08%20%E3%83%AF%E3%83%B3%E3%83%9E%E3%83%B3%E6%88%90%E5%8A%9F%E7%A5%88%E9%A1%98%EF%BC%81.txt#L22)；[OC07_MEIKO_E5 · talk_event_067.txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_067.txt#L82)；[OC07_Miku_X1 · 092-05 忘れられない記憶.txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L35)；[OC07_MEIKO_E7 · 1277_MEIKO_RB Happy Anniversary！！2025.txt L28–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1277_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L28)；[OC07_MEIKO_E8 · talk_event_157.txt L72–76](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_157.txt#L72)；[OC07_MEIKO_E6 · 1176_MEIKO (MMJ)_R4 レッツ・モアモアトレーニング！ (event_168).txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1176_MEIKO%20%28MMJ%29_R4%20%E3%83%AC%E3%83%83%E3%83%84%E3%83%BB%E3%83%A2%E3%82%A2%E3%83%A2%E3%82%A2%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_168%29.txt#L109)

### OC07_Luka · 巡音流歌

**成长细分判断：** 0226使她准备去谈伙伴负荷，实际人际行动；结果完整落实仍有限。

**情感细分判断：** 深层旧事共同听见，但个人回报只确认参与周年，关系多是具体托付伙伴事务。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,3,1,2|
|细档|2.25,4,2.25,1,2|2.25,3.25,1.25,2.5|

原粗档指数成长/情感 46.83 / 50.00；细分未归一原指数 51.21 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_Luka_X1 · 0226_桃井愛莉_R2 パーフェクト・スイーツ (event_23).txt L47–88](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0226_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R2%20%E3%83%91%E3%83%BC%E3%83%95%E3%82%A7%E3%82%AF%E3%83%88%E3%83%BB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%84%20%28event_23%29.txt#L47)；[OC07_Luka_F1 · 0323_日野森雫_R2 フェニラン・ナイトデート (event_41).txt L20–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0323_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R2%20%E3%83%95%E3%82%A7%E3%83%8B%E3%83%A9%E3%83%B3%E3%83%BB%E3%83%8A%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%E3%83%88%20%28event_41%29.txt#L20)；[OC07_Miku_F1 · 138-05 理想を追うために.txt L34–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L34)

**情感比较正文：** [OC07_Luka_E1 · 0323_日野森雫_R2 フェニラン・ナイトデート (event_41).txt L28–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0323_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R2%20%E3%83%95%E3%82%A7%E3%83%8B%E3%83%A9%E3%83%B3%E3%83%BB%E3%83%8A%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%E3%83%88%20%28event_41%29.txt#L28)；[OC07_Luka_E2 · 1112_巡音ルカ (MMJ)_R4 後悔も包み込んで (event_157).txt L70–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1112_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28MMJ%29_R4%20%E5%BE%8C%E6%82%94%E3%82%82%E5%8C%85%E3%81%BF%E8%BE%BC%E3%82%93%E3%81%A7%20%28event_157%29.txt#L70)；[OC07_Luka_E3 · 0860_巡音ルカ_RB Happy Anniversary！！2024.txt L16–20](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0860_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L16)；[OC07_Luka_X1 · 0226_桃井愛莉_R2 パーフェクト・スイーツ (event_23).txt L47–88](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/0226_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R2%20%E3%83%91%E3%83%BC%E3%83%95%E3%82%A7%E3%82%AF%E3%83%88%E3%83%BB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%84%20%28event_23%29.txt#L47)；[OC07_Miku_X1 · 092-05 忘れられない記憶.txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L35)

### OC07_Miku · 初音未来

**成长细分判断：** 赞赏与愿助练习成立，核心理想转折早由爱莉/连提出。

**情感细分判断：** 痛苦旧事是共同听见，周年设计具体成立；暂无个别长期理解的更强定位。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,2|2,3,2,2|
|细档|1.25,0,1.25,1,2|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 23.33 / 56.25；细分未归一原指数 27.71 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC07_Miku_F1 · 138-05 理想を追うために.txt L34–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L34)；[OC07_Miku_E4 · 0083_初音ミク (MMJ)_R2 ステージのセカイ.txt L24–28](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0083_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28MMJ%29_R2%20%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L24)；[OC07_Miku_E6 · talk_grade1.txt L5725–5729](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L5725)；[OC07_Miku_X1 · 092-05 忘れられない記憶.txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L35)

**情感比较正文：** [OC07_Miku_E4 · 0083_初音ミク (MMJ)_R2 ステージのセカイ.txt L24–28](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0083_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28MMJ%29_R2%20%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L24)；[OC07_Miku_E6 · talk_grade1.txt L5725–5729](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L5725)；[OC07_Miku_X1 · 092-05 忘れられない記憶.txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L35)；[OC07_Miku_F1 · 138-05 理想を追うために.txt L34–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/138%20Chase%20my%20IDEAL%20IDOL%EF%BC%81%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/138-05%20%E7%90%86%E6%83%B3%E3%82%92%E8%BF%BD%E3%81%86%E3%81%9F%E3%82%81%E3%81%AB.txt#L34)；[OC07_Miku_E1 · 1234_初音ミク_RB Happy Anniversary！！2025.txt L16–20](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1234_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L16)

## 日野森雫

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|2|1|100.00|95.45|97.73|100.00|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|2|1|2|95.44|100.00|97.72|99.99|研究估计；来源有依据，仍需独立复评|
|KAITO|3|4|3|90.19|86.36|88.28|90.33|研究估计；来源有依据，仍需独立复评|
|MEIKO|5|3|4|58.35|93.18|75.77|77.53|暂定：综合差距不足2分，子档微调可能换位|
|镜音连|4|5|5|67.11|84.09|75.60|77.36|研究估计；来源有依据，仍需独立复评|
|镜音铃|6|6|6|37.09|68.18|52.64|53.86|该组末位；仍为研究估计|

### OC08_Miku · 初音未来

**成长细分判断：** 151核心初心与挑战有实际决定，52共同服装成果不独占。

**情感细分判断：** 本人直接讲失去带头心情与过去压力，但回报多共同礼物/应援，定位仍具体顾问。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,2,2|
|细档|3.5,7,2.25,1,2|2.25,3.5,2.25,2.5|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 71.33 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_Miku_F1 · 151-05 あの頃の私は.txt L81–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/151%20Grow%20glorious%20glow%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/151-05%20%E3%81%82%E3%81%AE%E9%A0%83%E3%81%AE%E7%A7%81%E3%81%AF.txt#L81)；[OC08_Miku_F2 · 151-05 あの頃の私は.txt L137–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/151%20Grow%20glorious%20glow%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/151-05%20%E3%81%82%E3%81%AE%E9%A0%83%E3%81%AE%E7%A7%81%E3%81%AF.txt#L137)；[OC08_Miku_X2 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_KAITO_X3 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L43–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L43)

**情感比较正文：** [OC08_Miku_F2 · 151-05 あの頃の私は.txt L137–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/151%20Grow%20glorious%20glow%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/151-05%20%E3%81%82%E3%81%AE%E9%A0%83%E3%81%AE%E7%A7%81%E3%81%AF.txt#L137)；[OC08_Miku_E2 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_Miku_F1 · 151-05 あの頃の私は.txt L81–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/151%20Grow%20glorious%20glow%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/151-05%20%E3%81%82%E3%81%AE%E9%A0%83%E3%81%AE%E7%A7%81%E3%81%AF.txt#L81)；[OC08_Miku_X2 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_Miku_X1 · 176-11 これからも、アイドルとして.txt L55–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/176%20All%20ways%20Jump%21%20with%20you%20%28MMJ_WL%29/176-11%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%82%82%E3%80%81%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A8%E3%81%97%E3%81%A6.txt#L55)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)

### OC08_Luka · 巡音流歌

**成长细分判断：** 11完美面具与真实自我的提示被回想采用，核心自我问题更直接。

**情感细分判断：** 恐惧真实自己不被欢迎直接袒露、本人邀远足并说一起更开心，个别自我信任较集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,2,2|
|细档|3.5,4,2.5,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 59.33 / 56.25；细分未归一原指数 68.08 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_Luka_G1 · 011-05 望まれない“私”.txt L37–38、44、86–112、114–118、121–123、125–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-05%20%E6%9C%9B%E3%81%BE%E3%82%8C%E3%81%AA%E3%81%84%E2%80%9C%E7%A7%81%E2%80%9D.txt#L37)；[OC08_Luka_G2 · 011-07 決断.txt L10–15、23–24、28–29、35–37、39–42、66、72、78–79、85、92–94、108–110、123–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-07%20%E6%B1%BA%E6%96%AD.txt#L10)；[OC08_Luka_E7 · 0830_巡音ルカ (MMJ)_R4 挨拶はアイドルの基本 (event_115).txt L98–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0830_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28MMJ%29_R4%20%E6%8C%A8%E6%8B%B6%E3%81%AF%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%AE%E5%9F%BA%E6%9C%AC%20%28event_115%29.txt#L98)；[OC08_Luka_X1 · 022-02 ピクニックに行こう！.txt L69–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/022%20%E3%81%8A%E6%82%A9%E3%81%BF%E8%81%9E%E3%81%8B%E3%81%9B%E3%81%A6%EF%BC%81%E3%82%8F%E3%81%8F%E3%82%8F%E3%81%8F%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/022-02%20%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%E3%81%AB%E8%A1%8C%E3%81%93%E3%81%86%EF%BC%81.txt#L69)

**情感比较正文：** [OC08_Luka_E3 · 022-02 ピクニックに行こう！.txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/022%20%E3%81%8A%E6%82%A9%E3%81%BF%E8%81%9E%E3%81%8B%E3%81%9B%E3%81%A6%EF%BC%81%E3%82%8F%E3%81%8F%E3%82%8F%E3%81%8F%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/022-02%20%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%E3%81%AB%E8%A1%8C%E3%81%93%E3%81%86%EF%BC%81.txt#L80)；[OC08_Luka_X1 · 022-02 ピクニックに行こう！.txt L69–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/022%20%E3%81%8A%E6%82%A9%E3%81%BF%E8%81%9E%E3%81%8B%E3%81%9B%E3%81%A6%EF%BC%81%E3%82%8F%E3%81%8F%E3%82%8F%E3%81%8F%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/022-02%20%E3%83%94%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%E3%81%AB%E8%A1%8C%E3%81%93%E3%81%86%EF%BC%81.txt#L69)；[OC08_Luka_G1 · 011-05 望まれない“私”.txt L37–38、44、86–112、114–118、121–123、125–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-05%20%E6%9C%9B%E3%81%BE%E3%82%8C%E3%81%AA%E3%81%84%E2%80%9C%E7%A7%81%E2%80%9D.txt#L37)；[OC08_Luka_E6 · 0161_巡音ルカ (MMJ)_R4 新メンバー登場♪ (event_11).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0161_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28MMJ%29_R4%20%E6%96%B0%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E7%99%BB%E5%A0%B4%E2%99%AA%20%28event_11%29.txt#L10)；[OC08_Luka_G2 · 011-07 決断.txt L10–15、23–24、28–29、35–37、39–42、66、72、78–79、85、92–94、108–110、123–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/011%20Color%20of%20Myself%EF%BC%81%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/011-07%20%E6%B1%BA%E6%96%AD.txt#L10)

### OC08_KAITO · KAITO

**成长细分判断：** 直说帮助真冬、服装设计及分任务三项实际变化，具体方法覆盖较广。

**情感细分判断：** 亲自教缝纫并愿继续供材料，实际双向互动；深层本人困惑目前未口述。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,9,2,1,3|2,2,2,2|
|细档|2.5,9,2.5,1,3|2.25,2.5,2.25,2.5|

原粗档指数成长/情感 55.58 / 50.00；细分未归一原指数 64.33 / 59.38。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_KAITO_F1 · 080-04 雪の弓道場で.txt L160–179](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/080%20%E5%BC%93%E5%BC%95%E3%81%91%E3%80%81%E7%99%BD%E3%81%AE%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/080-04%20%E9%9B%AA%E3%81%AE%E5%BC%93%E9%81%93%E5%A0%B4%E3%81%A7.txt#L160)；[OC08_KAITO_X1 · 0632_日野森雫_R4 元気いっぱい地方ロケ！ (event_92).txt L139–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0632_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20%E5%85%83%E6%B0%97%E3%81%84%E3%81%A3%E3%81%B1%E3%81%84%E5%9C%B0%E6%96%B9%E3%83%AD%E3%82%B1%EF%BC%81%20%28event_92%29.txt#L139)；[OC08_KAITO_X2 · talk_event_080.txt L53–68](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_080.txt#L53)；[OC08_KAITO_X3 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L43–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L43)；[OC08_KAITO_E3 · 092-05 忘れられない記憶.txt L43–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L43)；[OC08_KAITO_E5 · 092-05 忘れられない記憶.txt L33–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L33)

**情感比较正文：** [OC08_KAITO_E1 · 0632_日野森雫_R4 元気いっぱい地方ロケ！ (event_92).txt L137–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0632_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20%E5%85%83%E6%B0%97%E3%81%84%E3%81%A3%E3%81%B1%E3%81%84%E5%9C%B0%E6%96%B9%E3%83%AD%E3%82%B1%EF%BC%81%20%28event_92%29.txt#L137)；[OC08_KAITO_E3 · 092-05 忘れられない記憶.txt L43–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L43)；[OC08_KAITO_E5 · 092-05 忘れられない記憶.txt L33–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/092%20Re-tie%20Friendship%20%28MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/092-05%20%E5%BF%98%E3%82%8C%E3%82%89%E3%82%8C%E3%81%AA%E3%81%84%E8%A8%98%E6%86%B6.txt#L33)；[OC08_KAITO_X2 · talk_event_080.txt L53–68](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_080.txt#L53)；[OC08_KAITO_F1 · 080-04 雪の弓道場で.txt L160–179](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/080%20%E5%BC%93%E5%BC%95%E3%81%91%E3%80%81%E7%99%BD%E3%81%AE%E4%B8%96%E7%95%8C%E3%81%A7%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/080-04%20%E9%9B%AA%E3%81%AE%E5%BC%93%E9%81%93%E5%A0%B4%E3%81%A7.txt#L160)；[OC08_KAITO_X1 · 0632_日野森雫_R4 元気いっぱい地方ロケ！ (event_92).txt L139–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0632_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20%E5%85%83%E6%B0%97%E3%81%84%E3%81%A3%E3%81%B1%E3%81%84%E5%9C%B0%E6%96%B9%E3%83%AD%E3%82%B1%EF%BC%81%20%28event_92%29.txt#L139)；[OC08_Miku_X2 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)

### OC08_MEIKO · MEIKO

**成长细分判断：** 183想报恩/怕介入的沟通方法使准备行动，结果尚未完整确认。

**情感细分判断：** 复杂旧组合关系是真实个人难题，按其歌声专绣图案且收礼确认，个别回应充分但范围较窄。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,0,1|2,3,2,2|
|细档|2.25,4,1.25,0,1|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 37.25 / 56.25；细分未归一原指数 41.63 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_MEIKO_F1 · 183-06 拭えない想い.txt L34–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/183%20%E4%BA%A4%E3%82%8F%E3%82%8B%E8%89%B2%E3%81%AF%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E3%81%BE%E3%81%BE%E3%81%AB%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/183-06%20%E6%8B%AD%E3%81%88%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L34)；[OC08_MEIKO_X1 · 156-03 楽しい作業タイム.txt L102–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L102)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)；[OC08_MEIKO_X3 · 156-07 想いを込めたプレゼント.txt L73–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L73)；[OC08_Len_X1 · 156-05 おばあちゃんの宝物.txt L7–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-05%20%E3%81%8A%E3%81%B0%E3%81%82%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E5%AE%9D%E7%89%A9.txt#L7)

**情感比较正文：** [OC08_MEIKO_E1 · 023-02 セカイの新しいアイドル.txt L89–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/023%20%E9%A0%91%E5%BC%B5%E3%82%8B%E3%81%82%E3%81%AA%E3%81%9F%E3%81%ABBreak%20Time%EF%BC%81%20%28MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5%29/023-02%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E3%81%97%E3%81%84%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB.txt#L89)；[OC08_MEIKO_F1 · 183-06 拭えない想い.txt L34–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/183%20%E4%BA%A4%E3%82%8F%E3%82%8B%E8%89%B2%E3%81%AF%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E3%81%BE%E3%81%BE%E3%81%AB%20%28MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/183-06%20%E6%8B%AD%E3%81%88%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L34)；[OC08_Len_X1 · 156-05 おばあちゃんの宝物.txt L7–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-05%20%E3%81%8A%E3%81%B0%E3%81%82%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E5%AE%9D%E7%89%A9.txt#L7)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)；[OC08_MEIKO_X3 · 156-07 想いを込めたプレゼント.txt L73–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L73)

### OC08_Len · 镜音连

**成长细分判断：** 礼物设计被实际采纳且本人明确夸其顾及各人，具体结果归因充分。

**情感细分判断：** 实际教笑容/wink并为其进步开心，具体合作多于个人深层交托。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,0,1|2,2,2,2|
|细档|2.25,4,2.5,0,1|2.25,2.25,2.5,2.25|

原粗档指数成长/情感 42.25 / 50.00；细分未归一原指数 47.88 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_Len_F1 · 156-03 楽しい作業タイム.txt L116–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L116)；[OC08_Len_X1 · 156-05 おばあちゃんの宝物.txt L7–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-05%20%E3%81%8A%E3%81%B0%E3%81%82%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E5%AE%9D%E7%89%A9.txt#L7)；[OC08_MEIKO_X1 · 156-03 楽しい作業タイム.txt L102–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L102)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)

**情感比较正文：** [OC08_Len_E1 · 156-03 楽しい作業タイム.txt L116–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L116)；[OC08_Len_E3 · 1106_鏡音レン (MMJ)_R4 とびきりのハートをキミに (event_156).txt L150–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1106_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28MMJ%29_R4%20%E3%81%A8%E3%81%B3%E3%81%8D%E3%82%8A%E3%81%AE%E3%83%8F%E3%83%BC%E3%83%88%E3%82%92%E3%82%AD%E3%83%9F%E3%81%AB%20%28event_156%29.txt#L150)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)；[OC08_Len_E6 · 156-01 いつものお返しに.txt L90–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-01%20%E3%81%84%E3%81%A4%E3%82%82%E3%81%AE%E3%81%8A%E8%BF%94%E3%81%97%E3%81%AB.txt#L90)；[OC08_Len_F1 · 156-03 楽しい作業タイム.txt L116–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L116)；[OC08_MEIKO_X1 · 156-03 楽しい作業タイム.txt L102–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-03%20%E6%A5%BD%E3%81%97%E3%81%84%E4%BD%9C%E6%A5%AD%E3%82%BF%E3%82%A4%E3%83%A0.txt#L102)

### OC08_Rin · 镜音铃

**成长细分判断：** 场地与服装讨论是真实实务帮助，没有新核心因果。

**情感细分判断：** 本人绣铃肖像及购物照看有具体行动，直接定位证据仍一般伙伴。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,1|2,2,2,1|
|细档|1.25,0,1.25,1,1|2.25,2.25,2,1|

原粗档指数成长/情感 22.08 / 43.75；细分未归一原指数 26.46 / 46.88。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC08_Rin_F1 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L73–110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L73)；[OC08_Rin_E1 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_Rin_E2 · 0424_鏡音リン (MMJ)_R4 もっと頼ってほしいんだ♪ (event_57).txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0424_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R4%20%E3%82%82%E3%81%A3%E3%81%A8%E9%A0%BC%E3%81%A3%E3%81%A6%E3%81%BB%E3%81%97%E3%81%84%E3%82%93%E3%81%A0%E2%99%AA%20%28event_57%29.txt#L39)；[OC08_Rin_E4 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)

**情感比较正文：** [OC08_Rin_F1 · 0091_鏡音リン (MMJ)_R3 輝くステージ.txt L73–110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0091_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R3%20%E8%BC%9D%E3%81%8F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8.txt#L73)；[OC08_Rin_E1 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_Rin_E2 · 0424_鏡音リン (MMJ)_R4 もっと頼ってほしいんだ♪ (event_57).txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0424_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28MMJ%29_R4%20%E3%82%82%E3%81%A3%E3%81%A8%E9%A0%BC%E3%81%A3%E3%81%A6%E3%81%BB%E3%81%97%E3%81%84%E3%82%93%E3%81%A0%E2%99%AA%20%28event_57%29.txt#L39)；[OC08_Rin_E4 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_Miku_X2 · 0391_日野森雫_R4 Feel like Magic (event_52).txt L10–48](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/08%20MMJ_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB/0391_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB_R4%20Feel%20like%20Magic%20%28event_52%29.txt#L10)；[OC08_MEIKO_X2 · 156-07 想いを込めたプレゼント.txt L29–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-07%20%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%9F%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L29)

## 小豆泽心羽

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|3|2|1|87.97|97.78|92.88|100.00|暂定：综合差距不足2分，子档微调可能换位|
|镜音铃|1|5|2|100.00|84.44|92.22|99.30|暂定：综合差距不足2分，子档微调可能换位|
|镜音连|2|3|3|90.88|91.11|91.00|97.98|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|1|4|71.97|100.00|85.98|92.58|研究估计；来源有依据，仍需独立复评|
|KAITO|4|6|5|83.03|82.22|82.62|88.96|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|5|4|6|75.51|86.67|81.09|87.31|该组末位；仍为研究估计|

### OC09_Miku · 初音未来

**成长细分判断：** 主线确认愿望并回到杏、后续歌唱方法多线，重要自我愿望渠道直接。

**情感细分判断：** 本人袒露被否定及负于杏的执念；与她歌唱的特别心跳感有个人差异，信任较深。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,2|2,3,2,2|
|细档|3.5,9,2.5,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 66.83 / 56.25；细分未归一原指数 75.58 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_Miku_G1 · street_01_11 扉を開く勇気を.txt L14–18、41–46、52、60–63、65–81、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L14)；[OC09_Miku_G2 · 028-06 リベンジ・マッチを前に.txt L7–12、33–35](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/028%20Awakening%20Beat%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/028-06%20%E3%83%AA%E3%83%99%E3%83%B3%E3%82%B8%E3%83%BB%E3%83%9E%E3%83%83%E3%83%81%E3%82%92%E5%89%8D%E3%81%AB.txt#L7)；[OC09_Miku_X1 · 086-06 見守ってくれる人達.txt L109–161](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/086%20Kick%20it%20up%20a%20notch%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/086-06%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%BA%BA%E9%81%94.txt#L109)；[OC09_Miku_X2 · 0953_初音ミク (VBS)_R4 扉の向こうへ (event_135).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0953_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E6%89%89%E3%81%AE%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28event_135%29.txt#L10)

**情感比较正文：** [OC09_Miku_E1 · 0953_初音ミク (VBS)_R4 扉の向こうへ (event_135).txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0953_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E6%89%89%E3%81%AE%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28event_135%29.txt#L10)；[OC09_Miku_E2 · 086-06 見守ってくれる人達.txt L153–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/086%20Kick%20it%20up%20a%20notch%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/086-06%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%BA%BA%E9%81%94.txt#L153)；[OC09_Miku_E8 · talk_grade1.txt L3450–3454](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L3450)；[OC09_Miku_G1 · street_01_11 扉を開く勇気を.txt L14–18、41–46、52、60–63、65–81、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L14)；[OC09_Miku_X2 · 0953_初音ミク (VBS)_R4 扉の向こうへ (event_135).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0953_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E6%89%89%E3%81%AE%E5%90%91%E3%81%93%E3%81%86%E3%81%B8%20%28event_135%29.txt#L10)

### OC09_Rin · 镜音铃

**成长细分判断：** K4保留作品启蒙媒介事实，后续编曲方法有具体作用；不移植为SEKAI人格根基。

**情感细分判断：** 作品感激与编曲交流、帮清扫/相册均具体，心中意义区分作品与人格，不因启蒙加深情。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|4,7,3,2,2|2,2,2,2|
|细档|4,7,3.25,2,2|2.25,2.25,2.5,2.5|

原粗档指数成长/情感 84.67 / 50.00；细分未归一原指数 85.92 / 59.38。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_Rin_G1 · 071-04 一緒に作曲をしよう！.txt L67–69、82–94、96–98、108–114、116–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-04%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E6%9B%B2%E3%82%92%E3%81%97%E3%82%88%E3%81%86%EF%BC%81.txt#L67)；[OC09_Rin_G2 · 071-06 伝わるといいな.txt L27–32、36–44、50、64–69、76–78、80–82、87–89、118–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-06%20%E4%BC%9D%E3%82%8F%E3%82%8B%E3%81%A8%E3%81%84%E3%81%84%E3%81%AA.txt#L27)；[OC09_Rin_X1 · 0505_小豆沢こはね_R4 ミッドナイトメイキング (event_71).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0505_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E3%83%9F%E3%83%83%E3%83%89%E3%83%8A%E3%82%A4%E3%83%88%E3%83%A1%E3%82%A4%E3%82%AD%E3%83%B3%E3%82%B0%20%28event_71%29.txt#L10)；[OC09_Rin_X2 · 036-02 みんなで出よう！.txt L47–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/036%20%E3%82%B9%E3%82%AF%E3%83%A9%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E3%83%95%E3%82%A1%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF%EF%BC%81%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/036-02%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E5%87%BA%E3%82%88%E3%81%86%EF%BC%81.txt#L47)；[OC09_Rin_E1 · talk_event_191.txt L57–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_191.txt#L57)

**情感比较正文：** [OC09_Rin_E2 · 0442_MEIKO (VBS)_R4 頑張ったあなたへの (event_60).txt L135–139](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0442_MEIKO%20%28VBS%29_R4%20%E9%A0%91%E5%BC%B5%E3%81%A3%E3%81%9F%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%E3%81%AE%20%28event_60%29.txt#L135)；[OC09_Rin_X2 · 036-02 みんなで出よう！.txt L47–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/036%20%E3%82%B9%E3%82%AF%E3%83%A9%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E3%83%95%E3%82%A1%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF%EF%BC%81%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/036-02%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E5%87%BA%E3%82%88%E3%81%86%EF%BC%81.txt#L47)；[OC09_Rin_G1 · 071-04 一緒に作曲をしよう！.txt L67–69、82–94、96–98、108–114、116–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-04%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E6%9B%B2%E3%82%92%E3%81%97%E3%82%88%E3%81%86%EF%BC%81.txt#L67)；[OC09_Rin_X1 · 0505_小豆沢こはね_R4 ミッドナイトメイキング (event_71).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0505_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E3%83%9F%E3%83%83%E3%83%89%E3%83%8A%E3%82%A4%E3%83%88%E3%83%A1%E3%82%A4%E3%82%AD%E3%83%B3%E3%82%B0%20%28event_71%29.txt#L10)；[OC09_Rin_E1 · talk_event_191.txt L57–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_191.txt#L57)；[OC09_Rin_X3 · 0838_鏡音リン_RB Happy Anniversary！！2023.txt L31–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0838_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L31)；[OC09_Rin_G2 · 071-06 伝わるといいな.txt L27–32、36–44、50、64–69、76–78、80–82、87–89、118–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-06%20%E4%BC%9D%E3%82%8F%E3%82%8B%E3%81%A8%E3%81%84%E3%81%84%E3%81%AA.txt#L27)

### OC09_Len · 镜音连

**成长细分判断：** K4同为作品经杏演唱的音乐起点，之后主要实际支持和共同咨询。

**情感细分判断：** 主线否定痛苦真实倾诉、肯定其一直见证会开心，个人投入主要合唱与为铃礼物参与。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|4,4,3,1,2|2,3,2,2|
|细档|4,4,3.25,1,2|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 76.83 / 56.25；细分未归一原指数 78.08 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_Len_G1 · street_01_11 扉を開く勇気を.txt L14–18、21–25、45–46、52、60–62、69–72、74–80、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L14)；[OC09_Rin_X2 · 036-02 みんなで出よう！.txt L47–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/036%20%E3%82%B9%E3%82%AF%E3%83%A9%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E3%83%95%E3%82%A1%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF%EF%BC%81%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/036-02%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E5%87%BA%E3%82%88%E3%81%86%EF%BC%81.txt#L47)；[OC09_Len_E2 · talk_event_086.txt L139–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_086.txt#L139)；[OC09_Len_E1 · talk_grade1.txt L10058–10062](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L10058)

**情感比较正文：** [OC09_Len_E2 · talk_event_086.txt L139–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_086.txt#L139)；[OC09_Len_E4 · 059-08 一歩、前へ.txt L157–161](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-08%20%E4%B8%80%E6%AD%A9%E3%80%81%E5%89%8D%E3%81%B8.txt#L157)；[OC09_Len_G1 · street_01_11 扉を開く勇気を.txt L14–18、21–25、45–46、52、60–62、69–72、74–80、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L14)；[OC09_Len_E1 · talk_grade1.txt L10058–10062](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L10058)；[OC09_Rin_X3 · 0838_鏡音リン_RB Happy Anniversary！！2023.txt L31–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0838_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L31)；[OC09_Rin_X2 · 036-02 みんなで出よう！.txt L47–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/036%20%E3%82%B9%E3%82%AF%E3%83%A9%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E3%83%95%E3%82%A1%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF%EF%BC%81%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/036-02%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E5%87%BA%E3%82%88%E3%81%86%EF%BC%81.txt#L47)

### OC09_MEIKO · MEIKO

**成长细分判断：** 童年总做不到的固有认识得到具体回应，尚未彻底重构自信，归因主要相談感谢。

**情感细分判断：** 详细交托童年自我否定、咖啡安心经常被本人确认并主动实际帮店，关系有生活性回报。 帮店为本人自发提出并实际分工完成，相较请求陪练含更多为对方需求付出，投入细分2.75。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|2,3,2,2|
|细档|3.5,4,1.25,1,2|2.25,3.5,2.75,2.75|

原粗档指数成长/情感 54.33 / 56.25；细分未归一原指数 61.83 / 70.31。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_MEIKO_G1 · street_01_11 扉を開く勇気を.txt L12–18、25–27、45–46、52、60–62、69–72、75–79、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L12)；[OC09_MEIKO_G2 · 028-04 自信の持ちかた.txt L7–16、32–37、41–45、47–52、55–57、60–66、69–74、77–79、82、86–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/028%20Awakening%20Beat%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/028-04%20%E8%87%AA%E4%BF%A1%E3%81%AE%E6%8C%81%E3%81%A1%E3%81%8B%E3%81%9F.txt#L7)；[OC09_MEIKO_E1 · 0249_小豆沢こはね_R4 内なる力の目覚め (event_28).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0249_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E5%86%85%E3%81%AA%E3%82%8B%E5%8A%9B%E3%81%AE%E7%9B%AE%E8%A6%9A%E3%82%81%20%28event_28%29.txt#L12)；[OC09_MEIKO_E2 · 0251_MEIKO (VBS)_R4 トーキング・コーヒー・タイム (event_28).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0251_MEIKO%20%28VBS%29_R4%20%E3%83%88%E3%83%BC%E3%82%AD%E3%83%B3%E3%82%B0%E3%83%BB%E3%82%B3%E3%83%BC%E3%83%92%E3%83%BC%E3%83%BB%E3%82%BF%E3%82%A4%E3%83%A0%20%28event_28%29.txt#L12)；[OC09_MEIKO_E6 · 0766_小豆沢こはね_R3 新しい朝に向けて (event_108).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0766_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R3%20%E6%96%B0%E3%81%97%E3%81%84%E6%9C%9D%E3%81%AB%E5%90%91%E3%81%91%E3%81%A6%20%28event_108%29.txt#L131)；[OC09_MEIKO_X1 · 0138_MEIKO (VBS)_R2 温かい眼差し (event_6).txt L19–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0138_MEIKO%20%28VBS%29_R2%20%E6%B8%A9%E3%81%8B%E3%81%84%E7%9C%BC%E5%B7%AE%E3%81%97%20%28event_6%29.txt#L19)

**情感比较正文：** [OC09_MEIKO_E6 · 0766_小豆沢こはね_R3 新しい朝に向けて (event_108).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0766_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R3%20%E6%96%B0%E3%81%97%E3%81%84%E6%9C%9D%E3%81%AB%E5%90%91%E3%81%91%E3%81%A6%20%28event_108%29.txt#L131)；[OC09_MEIKO_E1 · 0249_小豆沢こはね_R4 内なる力の目覚め (event_28).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0249_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E5%86%85%E3%81%AA%E3%82%8B%E5%8A%9B%E3%81%AE%E7%9B%AE%E8%A6%9A%E3%82%81%20%28event_28%29.txt#L12)；[OC09_MEIKO_G2 · 028-04 自信の持ちかた.txt L7–16、32–37、41–45、47–52、55–57、60–66、69–74、77–79、82、86–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/028%20Awakening%20Beat%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/028-04%20%E8%87%AA%E4%BF%A1%E3%81%AE%E6%8C%81%E3%81%A1%E3%81%8B%E3%81%9F.txt#L7)；[OC09_MEIKO_G1 · street_01_11 扉を開く勇気を.txt L12–18、25–27、45–46、52、60–62、69–72、75–79、87–88、96](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_11%20%E6%89%89%E3%82%92%E9%96%8B%E3%81%8F%E5%8B%87%E6%B0%97%E3%82%92.txt#L12)；[OC09_MEIKO_X1 · 0138_MEIKO (VBS)_R2 温かい眼差し (event_6).txt L19–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0138_MEIKO%20%28VBS%29_R2%20%E6%B8%A9%E3%81%8B%E3%81%84%E7%9C%BC%E5%B7%AE%E3%81%97%20%28event_6%29.txt#L19)；[OC09_MEIKO_E5 · 0312_MEIKO_RB Happy Anniversary！！.txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0312_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L80)

### OC09_KAITO · KAITO

**成长细分判断：** 采样焦虑转为确认自己的意图，摄影成果也具名确认，个人艺术问题作用明确。

**情感细分判断：** 采样与海外紧张是真实具体求助，咖啡蛋糕为本人回报，暂缺如Luka摄影目标的个别自我分享广度。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,2,2,2|
|细档|3.5,7,2.25,1,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 63.83 / 50.00；细分未归一原指数 71.33 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_KAITO_G1 · 071-04 一緒に作曲をしよう！.txt L63–65、67–69、81–91、93–98、101–105、108、110–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-04%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E6%9B%B2%E3%82%92%E3%81%97%E3%82%88%E3%81%86%EF%BC%81.txt#L63)；[OC09_KAITO_G2 · 071-06 伝わるといいな.txt L23–25、28–30、36–44、50、64–69、76–78、80–82、87–91、93–97、116–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-06%20%E4%BC%9D%E3%82%8F%E3%82%8B%E3%81%A8%E3%81%84%E3%81%84%E3%81%AA.txt#L23)；[OC09_Rin_X1 · 0505_小豆沢こはね_R4 ミッドナイトメイキング (event_71).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0505_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E3%83%9F%E3%83%83%E3%83%89%E3%83%8A%E3%82%A4%E3%83%88%E3%83%A1%E3%82%A4%E3%82%AD%E3%83%B3%E3%82%B0%20%28event_71%29.txt#L10)；[OC09_Luka_X1 · 120-06 あの日の写真は.txt L45–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/120%20Take%20the%20Best%20Shot%EF%BC%81%20%28Mix_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/120-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%86%99%E7%9C%9F%E3%81%AF.txt#L45)；[OC09_KAITO_X1 · 0861_小豆沢こはね_R4 仲間に最高のチョコを (event_120).txt L80–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0861_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E4%BB%B2%E9%96%93%E3%81%AB%E6%9C%80%E9%AB%98%E3%81%AE%E3%83%81%E3%83%A7%E3%82%B3%E3%82%92%20%28event_120%29.txt#L80)；[OC09_KAITO_X2 · 204-06 視線.txt L147–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/204%20Stay%20solid%2C%20No%20fold%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/204-06%20%E8%A6%96%E7%B7%9A.txt#L147)

**情感比较正文：** [OC09_KAITO_E3 · talk_event_066.txt L91–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L91)；[OC09_KAITO_E4 · 204-06 視線.txt L161–165](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/204%20Stay%20solid%2C%20No%20fold%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/204-06%20%E8%A6%96%E7%B7%9A.txt#L161)；[OC09_KAITO_X1 · 0861_小豆沢こはね_R4 仲間に最高のチョコを (event_120).txt L80–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0861_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E4%BB%B2%E9%96%93%E3%81%AB%E6%9C%80%E9%AB%98%E3%81%AE%E3%83%81%E3%83%A7%E3%82%B3%E3%82%92%20%28event_120%29.txt#L80)；[OC09_KAITO_G1 · 071-04 一緒に作曲をしよう！.txt L63–65、67–69、81–91、93–98、101–105、108、110–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-04%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E6%9B%B2%E3%82%92%E3%81%97%E3%82%88%E3%81%86%EF%BC%81.txt#L63)；[OC09_Rin_X1 · 0505_小豆沢こはね_R4 ミッドナイトメイキング (event_71).txt L10–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0505_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E3%83%9F%E3%83%83%E3%83%89%E3%83%8A%E3%82%A4%E3%83%88%E3%83%A1%E3%82%A4%E3%82%AD%E3%83%B3%E3%82%B0%20%28event_71%29.txt#L10)；[OC09_KAITO_X2 · 204-06 視線.txt L147–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/204%20Stay%20solid%2C%20No%20fold%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/204-06%20%E8%A6%96%E7%B7%9A.txt#L147)；[OC09_KAITO_E1 · talk_event_066.txt L91–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L91)

### OC09_Luka · 巡音流歌

**成长细分判断：** 摄影初心与共同歌唱的帮助实际确认，核心创作侧重一次问题。

**情感细分判断：** 摄影目标是个人具体自我表达；邀跨世界活动及具名摄影谢礼是实际回应，但未有创伤袒露。 120本人说摄影的自我感动及想传达温暖，比编曲任务咨询更能看到自己的感受，信任细分2.50。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,0,2|2,2,2,2|
|细档|3.25,7,2.25,0,2|2.25,2.5,2.5,2.5|

原粗档指数成长/情感 60.50 / 50.00；细分未归一原指数 64.88 / 60.94。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC09_Miku_X1 · 086-06 見守ってくれる人達.txt L109–161](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/086%20Kick%20it%20up%20a%20notch%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/086-06%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%BA%BA%E9%81%94.txt#L109)；[OC09_Luka_X1 · 120-06 あの日の写真は.txt L45–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/120%20Take%20the%20Best%20Shot%EF%BC%81%20%28Mix_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/120-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%86%99%E7%9C%9F%E3%81%AF.txt#L45)；[OC09_KAITO_X1 · 0861_小豆沢こはね_R4 仲間に最高のチョコを (event_120).txt L80–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0861_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E4%BB%B2%E9%96%93%E3%81%AB%E6%9C%80%E9%AB%98%E3%81%AE%E3%83%81%E3%83%A7%E3%82%B3%E3%82%92%20%28event_120%29.txt#L80)；[OC09_Luka_F1 · 1407_小豆沢こはね_R4 心の奥へ届く歌 (event_207).txt L11–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/1407_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E5%BF%83%E3%81%AE%E5%A5%A5%E3%81%B8%E5%B1%8A%E3%81%8F%E6%AD%8C%20%28event_207%29.txt#L11)

**情感比较正文：** [OC09_Luka_E2 · 120-06 あの日の写真は.txt L79–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/120%20Take%20the%20Best%20Shot%EF%BC%81%20%28Mix_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/120-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%86%99%E7%9C%9F%E3%81%AF.txt#L79)；[OC09_Luka_E3 · 086-06 見守ってくれる人達.txt L153–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/086%20Kick%20it%20up%20a%20notch%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/086-06%20%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%BA%BA%E9%81%94.txt#L153)；[OC09_Luka_X1 · 120-06 あの日の写真は.txt L45–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/120%20Take%20the%20Best%20Shot%EF%BC%81%20%28Mix_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/120-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E5%86%99%E7%9C%9F%E3%81%AF.txt#L45)；[OC09_Luka_F1 · 1407_小豆沢こはね_R4 心の奥へ届く歌 (event_207).txt L11–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/1407_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E5%BF%83%E3%81%AE%E5%A5%A5%E3%81%B8%E5%B1%8A%E3%81%8F%E6%AD%8C%20%28event_207%29.txt#L11)；[OC09_KAITO_X1 · 0861_小豆沢こはね_R4 仲間に最高のチョコを (event_120).txt L80–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/0861_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E4%BB%B2%E9%96%93%E3%81%AB%E6%9C%80%E9%AB%98%E3%81%AE%E3%83%81%E3%83%A7%E3%82%B3%E3%82%92%20%28event_120%29.txt#L80)

## 白石杏

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|镜音铃|2|2|2|90.36|95.83|93.09|93.09|研究估计；来源有依据，仍需独立复评|
|巡音流歌|3|3|3|72.27|89.58|80.93|80.93|暂定：综合差距不足2分，子档微调可能换位|
|MEIKO|4|4|4|70.55|87.50|79.03|79.03|研究估计；来源有依据，仍需独立复评|
|KAITO|5|5|5|59.07|75.00|67.04|67.04|研究估计；来源有依据，仍需独立复评|
|镜音连|6|6|6|32.15|54.17|43.16|43.16|该组末位；仍为研究估计|

### OC10_Miku · 初音未来

**成长细分判断：** 辨相棒不安及面对记忆选择属于核心作用，1058取忆的直接支撑仍归铃。

**情感细分判断：** 多次真实讲相棒/丧失困惑并主动单独报决心、准备蛋糕，持续信任范围较广。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,3,3,2|
|细档|3.5,7,2.5,1,2|2.25,3.5,3.5,2.75|

原粗档指数成长/情感 63.83 / 62.50；细分未归一原指数 72.58 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_Miku_G1 · 037-05 路地裏の会話.txt L33–37、42–48、59–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-05%20%E8%B7%AF%E5%9C%B0%E8%A3%8F%E3%81%AE%E4%BC%9A%E8%A9%B1.txt#L33)；[OC10_Miku_G2 · 037-06 モヤモヤしていた理由.txt L8–10、12–21、36–42、45–48、66–72、114–117、123–125、137–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%97%E3%81%A6%E3%81%84%E3%81%9F%E7%90%86%E7%94%B1.txt#L8)；[OC10_Miku_X1 · 1058_白石杏_R4 かけがえのない人達.txt L154–220](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1058_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E3%81%8B%E3%81%91%E3%81%8C%E3%81%88%E3%81%AE%E3%81%AA%E3%81%84%E4%BA%BA%E9%81%94.txt#L154)；[OC10_Miku_X3 · 0298_初音ミク (VBS)_R4 聞きたくない言葉でも (event_37).txt L105–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0298_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E8%81%9E%E3%81%8D%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84%E8%A8%80%E8%91%89%E3%81%A7%E3%82%82%20%28event_37%29.txt#L105)；[OC10_Miku_E4 · 0463_白石杏_R4 優しい記憶 (event_64).txt L173–177](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/0463_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E5%84%AA%E3%81%97%E3%81%84%E8%A8%98%E6%86%B6%20%28event_64%29.txt#L173)

**情感比较正文：** [OC10_Miku_E2 · talk_event_037.txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_037.txt#L78)；[OC10_Miku_E3 · 0298_初音ミク (VBS)_R4 聞きたくない言葉でも (event_37).txt L108–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0298_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E8%81%9E%E3%81%8D%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84%E8%A8%80%E8%91%89%E3%81%A7%E3%82%82%20%28event_37%29.txt#L108)；[OC10_Miku_E4 · 0463_白石杏_R4 優しい記憶 (event_64).txt L173–177](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/0463_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E5%84%AA%E3%81%97%E3%81%84%E8%A8%98%E6%86%B6%20%28event_64%29.txt#L173)；[OC10_Miku_G1 · 037-05 路地裏の会話.txt L33–37、42–48、59–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-05%20%E8%B7%AF%E5%9C%B0%E8%A3%8F%E3%81%AE%E4%BC%9A%E8%A9%B1.txt#L33)；[OC10_Miku_G2 · 037-06 モヤモヤしていた理由.txt L8–10、12–21、36–42、45–48、66–72、114–117、123–125、137–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-06%20%E3%83%A2%E3%83%A4%E3%83%A2%E3%83%A4%E3%81%97%E3%81%A6%E3%81%84%E3%81%9F%E7%90%86%E7%94%B1.txt#L8)；[OC10_Miku_X1 · 1058_白石杏_R4 かけがえのない人達.txt L154–220](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1058_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E3%81%8B%E3%81%91%E3%81%8C%E3%81%88%E3%81%AE%E3%81%AA%E3%81%84%E4%BA%BA%E9%81%94.txt#L154)；[OC10_Miku_E5 · talk_event_181.txt L53–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_181.txt#L53)；[OC10_Miku_X2 · 0706_初音ミク_RB Happy Anniversary！！2023.txt L13–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0706_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L13)；[OC10_Miku_X3 · 0298_初音ミク (VBS)_R4 聞きたくない言葉でも (event_37).txt L105–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0298_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28VBS%29_R4%20%E8%81%9E%E3%81%8D%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84%E8%A8%80%E8%91%89%E3%81%A7%E3%82%82%20%28event_37%29.txt#L105)

### OC10_Rin · 镜音铃

**成长细分判断：** 1058直接承接面对丧失的决定并取回重要记忆，但已核核心线较单一。

**情感细分判断：** 真实陪看会哭的凪照片、取回记忆，加上按愿望买烟花；个别亲近清楚，持续范围略窄于Miku。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,1|2,3,3,2|
|细档|3.5,4,2.25,1,1|2.25,3.25,3.5,2.5|

原粗档指数成长/情感 58.08 / 62.50；细分未归一原指数 65.58 / 71.88。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_Rin_F1 · 1058_白石杏_R4 かけがえのない人達.txt L256–279](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1058_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E3%81%8B%E3%81%91%E3%81%8C%E3%81%88%E3%81%AE%E3%81%AA%E3%81%84%E4%BA%BA%E9%81%94.txt#L256)；[OC10_Miku_X1 · 1058_白石杏_R4 かけがえのない人達.txt L154–220](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1058_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E3%81%8B%E3%81%91%E3%81%8C%E3%81%88%E3%81%AE%E3%81%AA%E3%81%84%E4%BA%BA%E9%81%94.txt#L154)；[OC10_Rin_X1 · talk_event_097.txt L77–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_097.txt#L77)

**情感比较正文：** [OC10_Rin_E2 · talk_event_097.txt L87–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_097.txt#L87)；[OC10_Rin_F1 · 1058_白石杏_R4 かけがえのない人達.txt L256–279](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1058_%E7%99%BD%E7%9F%B3%E6%9D%8F_R4%20%E3%81%8B%E3%81%91%E3%81%8C%E3%81%88%E3%81%AE%E3%81%AA%E3%81%84%E4%BA%BA%E9%81%94.txt#L256)；[OC10_Rin_X1 · talk_event_097.txt L77–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_097.txt#L77)；[OC10_Rin_E4 · 0838_鏡音リン_RB Happy Anniversary！！2023.txt L16–20](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0838_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L16)；[OC10_Rin_E5 · 0532_鏡音リン (VBS)_R2 レッツ・エンジョイ文化祭♪ (event_75).txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0532_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28VBS%29_R2%20%E3%83%AC%E3%83%83%E3%83%84%E3%83%BB%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%E6%96%87%E5%8C%96%E7%A5%AD%E2%99%AA%20%28event_75%29.txt#L80)；[OC10_Rin_E6 · 1394_日野森志歩_R4 想いと熱を込めて (event_205).txt L137–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1394_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R4%20%E6%83%B3%E3%81%84%E3%81%A8%E7%86%B1%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28event_205%29.txt#L137)；[OC10_Len_X1 · talk_event_181.txt L53–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_181.txt#L53)

### OC10_Luka · 巡音流歌

**成长细分判断：** 201方法实际推动练习、后续英语自信本人回顾，直接落实较摄影间接传达充分。

**情感细分判断：** 相棒成长不安真实交托，并分享凪给的曲；个别相談比普通摄影信任更深。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,3,2,2|
|细档|2.25,4,2.5,1,2|2.25,3.5,2.5,2.5|

原粗档指数成长/情感 46.83 / 56.25；细分未归一原指数 52.46 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_Luka_F1 · 129-04 言葉にならないもの.txt L58–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/129%20Whip%20the%20wimp%20girl%21%21%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/129-04%20%E8%A8%80%E8%91%89%E3%81%AB%E3%81%AA%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE.txt#L58)；[OC10_Luka_X1 · 129-04 言葉にならないもの.txt L82–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/129%20Whip%20the%20wimp%20girl%21%21%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/129-04%20%E8%A8%80%E8%91%89%E3%81%AB%E3%81%AA%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE.txt#L82)；[OC10_Luka_X2 · 201-05 見えた光明.txt L62–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/201%20Show%20%27em%20what%27s%20up%EF%BC%81%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/201-05%20%E8%A6%8B%E3%81%88%E3%81%9F%E5%85%89%E6%98%8E.txt#L62)；[OC10_Luka_X3 · 201-05 見えた光明.txt L135–171](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/201%20Show%20%27em%20what%27s%20up%EF%BC%81%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/201-05%20%E8%A6%8B%E3%81%88%E3%81%9F%E5%85%89%E6%98%8E.txt#L135)；[OC10_Luka_F2 · 1468_白石杏_R3 交流は折り紙で！ (event_216).txt L16–30](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1468_%E7%99%BD%E7%9F%B3%E6%9D%8F_R3%20%E4%BA%A4%E6%B5%81%E3%81%AF%E6%8A%98%E3%82%8A%E7%B4%99%E3%81%A7%EF%BC%81%20%28event_216%29.txt#L16)；[OC10_Luka_E1 · 215-08 最後に、届けたい想い.txt L98–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/215%20Mix%26Make%20Party%20Time%21%21%20%28Mix_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB-VS%29/215-08%20%E6%9C%80%E5%BE%8C%E3%81%AB%E3%80%81%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E6%83%B3%E3%81%84.txt#L98)

**情感比较正文：** [OC10_Luka_E1 · 215-08 最後に、届けたい想い.txt L98–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/215%20Mix%26Make%20Party%20Time%21%21%20%28Mix_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB-VS%29/215-08%20%E6%9C%80%E5%BE%8C%E3%81%AB%E3%80%81%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E6%83%B3%E3%81%84.txt#L98)；[OC10_Luka_E3 · 129-03 この気持ちに決着を.txt L117–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/129%20Whip%20the%20wimp%20girl%21%21%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/129-03%20%E3%81%93%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%81%AB%E6%B1%BA%E7%9D%80%E3%82%92.txt#L117)；[OC10_Luka_F2 · 1468_白石杏_R3 交流は折り紙で！ (event_216).txt L16–30](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/10%20VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F/1468_%E7%99%BD%E7%9F%B3%E6%9D%8F_R3%20%E4%BA%A4%E6%B5%81%E3%81%AF%E6%8A%98%E3%82%8A%E7%B4%99%E3%81%A7%EF%BC%81%20%28event_216%29.txt#L16)；[OC10_Luka_F1 · 129-04 言葉にならないもの.txt L58–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/129%20Whip%20the%20wimp%20girl%21%21%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/129-04%20%E8%A8%80%E8%91%89%E3%81%AB%E3%81%AA%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE.txt#L58)；[OC10_Luka_X1 · 129-04 言葉にならないもの.txt L82–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/129%20Whip%20the%20wimp%20girl%21%21%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/129-04%20%E8%A8%80%E8%91%89%E3%81%AB%E3%81%AA%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE.txt#L82)；[OC10_Luka_E7 · 044-01 自由な歌声.txt L90–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/044%20Same%20Dreams%2CSame%20Colors%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/044-01%20%E8%87%AA%E7%94%B1%E3%81%AA%E6%AD%8C%E5%A3%B0.txt#L90)；[OC10_Luka_E8 · 0513_東雲彰人_R4 大歓声の熱狂を (event_72).txt L113–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0513_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E5%A4%A7%E6%AD%93%E5%A3%B0%E3%81%AE%E7%86%B1%E7%8B%82%E3%82%92%20%28event_72%29.txt#L113)；[OC10_Luka_X2 · 201-05 見えた光明.txt L62–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/201%20Show%20%27em%20what%27s%20up%EF%BC%81%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/201-05%20%E8%A6%8B%E3%81%88%E3%81%9F%E5%85%89%E6%98%8E.txt#L62)

### OC10_MEIKO · MEIKO

**成长细分判断：** 摄影思路经心羽传达且本人确认自己风格，实际作用成立但渠道间接。

**情感细分判断：** 憧憬可靠姐姐及实际帮店/秘密清洁很具体，但已核袒露是摄影不自信，低于深层搭档困惑。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,3,2|
|细档|2.25,4,2.25,1,2|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 46.83 / 56.25；细分未归一原指数 51.21 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_MEIKO_F1 · 060-08 これからも、私らしく！.txt L29–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/060%20%E9%9D%92%E7%A9%BA%E3%81%AB%E9%A1%98%E3%81%86%E3%83%A6%E3%82%A2%E3%83%BB%E3%83%8F%E3%83%94%E3%83%8D%E3%82%B9%EF%BC%81%20%28Mix_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/060-08%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%82%82%E3%80%81%E7%A7%81%E3%82%89%E3%81%97%E3%81%8F%EF%BC%81.txt#L29)；[OC10_MEIKO_E4 · 060-02 花嫁らしさを目指して.txt L64–68](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/060%20%E9%9D%92%E7%A9%BA%E3%81%AB%E9%A1%98%E3%81%86%E3%83%A6%E3%82%A2%E3%83%BB%E3%83%8F%E3%83%94%E3%83%8D%E3%82%B9%EF%BC%81%20%28Mix_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/060-02%20%E8%8A%B1%E5%AB%81%E3%82%89%E3%81%97%E3%81%95%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6.txt#L64)；[OC10_MEIKO_X1 · 060-08 これからも、私らしく！.txt L43–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/060%20%E9%9D%92%E7%A9%BA%E3%81%AB%E9%A1%98%E3%81%86%E3%83%A6%E3%82%A2%E3%83%BB%E3%83%8F%E3%83%94%E3%83%8D%E3%82%B9%EF%BC%81%20%28Mix_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/060-08%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%82%82%E3%80%81%E7%A7%81%E3%82%89%E3%81%97%E3%81%8F%EF%BC%81.txt#L43)；[OC10_KAITO_X2 · talk_event_066.txt L101–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L101)；[OC09_MEIKO_X1 · 0138_MEIKO (VBS)_R2 温かい眼差し (event_6).txt L19–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0138_MEIKO%20%28VBS%29_R2%20%E6%B8%A9%E3%81%8B%E3%81%84%E7%9C%BC%E5%B7%AE%E3%81%97%20%28event_6%29.txt#L19)；[OC10_MEIKO_E1 · 0312_MEIKO_RB Happy Anniversary！！.txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0312_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L35)；[OC10_MEIKO_E6 · 006-01 『STAY GOLD』.txt L33–37](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/006%20%E3%81%84%E3%81%A4%E3%81%8B%E3%80%81%E8%83%8C%E4%B8%AD%E3%81%82%E3%82%8F%E3%81%9B%E3%81%AE%E3%83%AA%E3%83%AA%E3%83%83%E3%82%AF%E3%82%92%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/006-01%20%E3%80%8ESTAY%20GOLD%E3%80%8F.txt#L33)

**情感比较正文：** [OC10_MEIKO_F1 · 060-08 これからも、私らしく！.txt L29–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/060%20%E9%9D%92%E7%A9%BA%E3%81%AB%E9%A1%98%E3%81%86%E3%83%A6%E3%82%A2%E3%83%BB%E3%83%8F%E3%83%94%E3%83%8D%E3%82%B9%EF%BC%81%20%28Mix_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/060-08%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%82%82%E3%80%81%E7%A7%81%E3%82%89%E3%81%97%E3%81%8F%EF%BC%81.txt#L29)；[OC10_MEIKO_X1 · 060-08 これからも、私らしく！.txt L43–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/060%20%E9%9D%92%E7%A9%BA%E3%81%AB%E9%A1%98%E3%81%86%E3%83%A6%E3%82%A2%E3%83%BB%E3%83%8F%E3%83%94%E3%83%8D%E3%82%B9%EF%BC%81%20%28Mix_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/060-08%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%82%82%E3%80%81%E7%A7%81%E3%82%89%E3%81%97%E3%81%8F%EF%BC%81.txt#L43)；[OC10_MEIKO_E1 · 0312_MEIKO_RB Happy Anniversary！！.txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0312_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L35)；[OC10_MEIKO_E3 · 0442_MEIKO (VBS)_R4 頑張ったあなたへの (event_60).txt L122–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0442_MEIKO%20%28VBS%29_R4%20%E9%A0%91%E5%BC%B5%E3%81%A3%E3%81%9F%E3%81%82%E3%81%AA%E3%81%9F%E3%81%B8%E3%81%AE%20%28event_60%29.txt#L122)；[OC09_MEIKO_X1 · 0138_MEIKO (VBS)_R2 温かい眼差し (event_6).txt L19–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0138_MEIKO%20%28VBS%29_R2%20%E6%B8%A9%E3%81%8B%E3%81%84%E7%9C%BC%E5%B7%AE%E3%81%97%20%28event_6%29.txt#L19)；[OC10_KAITO_X2 · talk_event_066.txt L101–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L101)

### OC10_KAITO · KAITO

**成长细分判断：** 材料比喻促理解团队磨合，后续共同商量，归因仍一般感谢。

**情感细分判断：** 具体团队相談、带清洁用品及愿分享构成合作关系，暂无更深本人交托。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,0,2|2,2,2,2|
|细档|2.25,4,1.25,0,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 38.50 / 50.00；细分未归一原指数 42.88 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_KAITO_F1 · 021-06 相棒としてできること.txt L103–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/021%20STRAY%20BAD%20DOG%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/021-06%20%E7%9B%B8%E6%A3%92%E3%81%A8%E3%81%97%E3%81%A6%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L103)；[OC10_KAITO_X1 · 059-06 ふわふわのパンケーキ.txt L18–88](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L18)；[OC10_KAITO_X3 · 059-06 ふわふわのパンケーキ.txt L87–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L87)；[OC10_KAITO_X2 · talk_event_066.txt L101–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L101)

**情感比较正文：** [OC10_KAITO_F1 · 021-06 相棒としてできること.txt L103–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/021%20STRAY%20BAD%20DOG%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/021-06%20%E7%9B%B8%E6%A3%92%E3%81%A8%E3%81%97%E3%81%A6%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L103)；[OC10_KAITO_X2 · talk_event_066.txt L101–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_066.txt#L101)；[OC10_KAITO_X1 · 059-06 ふわふわのパンケーキ.txt L18–88](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L18)

### OC10_Len · 镜音连

**成长细分判断：** 共同交流与协助真实，但关键不安诊断和解决发生连离场后。

**情感细分判断：** 烟花愿望被本人回应，核心相棒恐惧不是向他袒露，直接定位较一般。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,1|1,2,2,1|
|细档|1,0,1.25,1,1|1,2.25,2.25,1|

原粗档指数成长/情感 22.08 / 37.50；细分未归一原指数 23.33 / 40.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC10_Len_G1 · 037-05 路地裏の会話.txt L33–37、41–58、60–62、64–71、76–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-05%20%E8%B7%AF%E5%9C%B0%E8%A3%8F%E3%81%AE%E4%BC%9A%E8%A9%B1.txt#L33)；[OC10_Len_E1 · 1287_鏡音レン (VBS)_R3 笑顔のエールを (event_187).txt L60–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1287_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28VBS%29_R3%20%E7%AC%91%E9%A1%94%E3%81%AE%E3%82%A8%E3%83%BC%E3%83%AB%E3%82%92%20%28event_187%29.txt#L60)；[OC10_Len_E2 · street_01_06 不思議なカフェ.txt L81–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_06%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E3%82%AB%E3%83%95%E3%82%A7.txt#L81)；[OC10_Len_X1 · talk_event_181.txt L53–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_181.txt#L53)

**情感比较正文：** [OC10_Len_E1 · 1287_鏡音レン (VBS)_R3 笑顔のエールを (event_187).txt L60–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1287_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28VBS%29_R3%20%E7%AC%91%E9%A1%94%E3%81%AE%E3%82%A8%E3%83%BC%E3%83%AB%E3%82%92%20%28event_187%29.txt#L60)；[OC10_Len_E2 · street_01_06 不思議なカフェ.txt L81–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_06%20%E4%B8%8D%E6%80%9D%E8%AD%B0%E3%81%AA%E3%82%AB%E3%83%95%E3%82%A7.txt#L81)；[OC10_Len_G1 · 037-05 路地裏の会話.txt L33–37、41–58、60–62、64–71、76–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/037%20Bout%20for%20Beside%20You%20%28VBS_%E7%99%BD%E7%9F%B3%E6%9D%8F%29/037-05%20%E8%B7%AF%E5%9C%B0%E8%A3%8F%E3%81%AE%E4%BC%9A%E8%A9%B1.txt#L33)；[OC10_Len_E3 · 0838_鏡音リン_RB Happy Anniversary！！2023.txt L16–20](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0838_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L16)；[OC10_Len_X1 · talk_event_181.txt L53–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_181.txt#L53)

## 东云彰人

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|镜音连|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|2|2|97.26|83.02|90.14|90.14|研究估计；来源有依据，仍需独立复评|
|镜音铃|3|3|3|88.04|81.13|84.58|84.58|研究估计；来源有依据，仍需独立复评|
|MEIKO|4|4|4|79.80|69.81|74.81|74.81|研究估计；来源有依据，仍需独立复评|
|KAITO|5|5|5|56.48|60.38|58.43|58.43|研究估计；来源有依据，仍需独立复评|
|初音未来|6|6|6|36.50|58.49|47.49|47.49|该组末位；仍为研究估计|

### OC11_Len · 镜音连

**成长细分判断：** 核心自我和相棒支撑跨情境，主线核心方法保留MEIKO作用。

**情感细分判断：** 本人明确歌与话入心、多次相助，相棒痛苦真实向连说，个人信任与持续意义更集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,2|3,3,2,3|
|细档|3.5,7,2.5,2,2|3.5,3.5,2.5,3.75|

原粗档指数成长/情感 67.17 / 68.75；细分未归一原指数 75.92 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_Len_G1 · street_01_17 レンとMEIKOととっておき.txt L8–25、30–32、47–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L8)；[OC11_Rin_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L170–235](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L170)；[OC11_Len_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L235–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L235)；[OC11_Luka_X2 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L97–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L97)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)；[OC11_Len_X2 · street_01_17 レンとMEIKOととっておき.txt L41–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L41)

**情感比较正文：** [OC11_Luka_X2 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L97–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L97)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)；[OC11_Len_E1 · talk_event_163.txt L47–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_163.txt#L47)；[OC11_Len_G1 · street_01_17 レンとMEIKOととっておき.txt L8–25、30–32、47–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L8)；[OC11_Rin_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L170–235](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L170)；[OC11_Rin_X2 · talk_event_163.txt L36–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_163.txt#L36)

### OC11_Luka · 巡音流歌

**成长细分判断：** 109帮助释放压抑情感找到表演法，创作方向因果直接，79安全消息不当全部人生改变。

**情感细分判断：** 本人反复确认话与歌入心，是较强个人意义；深层创伤向谦而非Luka、投入主要受邀。 1153本人内心明确歌与话反复入心、实际多次得到帮助，表达细分3.50；未把凪/谦创伤转成她的听众经历。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,3|3,2,1,3|
|细档|3.5,7,2.5,1,3|3.5,2.5,1.25,3.75|

原粗档指数成长/情感 65.08 / 56.25；细分未归一原指数 73.83 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_Luka_G1 · 079-06 もし限界があるのなら.txt L21–23、32–34、39–41、55–57、64–68、77–79、104–108、117–118、120–121、127、131、134–138、141–142、145–147、155–157、169–170、176、188–191、199–201、208–211、227–229、232–235](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/079%20Find%20A%20Way%20Out%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/079-06%20%E3%82%82%E3%81%97%E9%99%90%E7%95%8C%E3%81%8C%E3%81%82%E3%82%8B%E3%81%AE%E3%81%AA%E3%82%89.txt#L21)；[OC11_Luka_G2 · 079-08 まだ遠くても、いつか.txt L5–7、9–17、27–30、34–36、105–106、112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/079%20Find%20A%20Way%20Out%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/079-08%20%E3%81%BE%E3%81%A0%E9%81%A0%E3%81%8F%E3%81%A6%E3%82%82%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B.txt#L5)；[OC11_Luka_F1 · 109-06 この胸にあるもの.txt L112–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/109%20BURN%20MY%20SOUL%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/109-06%20%E3%81%93%E3%81%AE%E8%83%B8%E3%81%AB%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE.txt#L112)；[OC11_Luka_X1 · 109-06 この胸にあるもの.txt L48–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/109%20BURN%20MY%20SOUL%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/109-06%20%E3%81%93%E3%81%AE%E8%83%B8%E3%81%AB%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE.txt#L48)；[OC11_Luka_X2 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L97–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L97)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)

**情感比较正文：** [OC11_Luka_X2 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L97–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L97)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)；[OC11_Luka_E3 · 0582_巡音ルカ_RB Happy Anniversary！！2023.txt L48–52](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0582_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L48)；[OC11_Luka_F1 · 109-06 この胸にあるもの.txt L112–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/109%20BURN%20MY%20SOUL%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/109-06%20%E3%81%93%E3%81%AE%E8%83%B8%E3%81%AB%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE.txt#L112)；[OC11_Luka_X1 · 109-06 この胸にあるもの.txt L48–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/109%20BURN%20MY%20SOUL%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/109-06%20%E3%81%93%E3%81%AE%E8%83%B8%E3%81%AB%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE.txt#L48)；[OC11_Luka_X3 · 0582_巡音ルカ_RB Happy Anniversary！！2023.txt L12–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0582_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L12)

### OC11_Rin · 镜音铃

**成长细分判断：** 0671真实支撑核心自我与同伴记忆，后续具名共同呼声帮助不独占。

**情感细分判断：** 真实听不能是自己的焦虑、本人回忆持续支持，惊喜练曲实际回应愿望。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,2,2|
|细档|3.5,4,2.25,1,2|2.25,3.5,2.5,2.5|

原粗档指数成长/情感 59.33 / 56.25；细分未归一原指数 66.83 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_Rin_F1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L155–169](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L155)；[OC11_Rin_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L170–235](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L170)；[OC11_Len_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L235–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L235)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)；[OC11_Rin_X3 · talk_event_216.txt L47–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_216.txt#L47)

**情感比较正文：** [OC11_Len_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L235–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L235)；[OC11_Len_X3 · 1153_東雲彰人_R4 予想外の言葉 (event_163).txt L150–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1153_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E4%BA%88%E6%83%B3%E5%A4%96%E3%81%AE%E8%A8%80%E8%91%89%20%28event_163%29.txt#L150)；[OC11_Rin_X1 · 0671_東雲彰人_R4 渇きのワンダラー.txt L170–235](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/0671_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E6%B8%87%E3%81%8D%E3%81%AE%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC.txt#L170)；[OC11_Rin_X3 · talk_event_216.txt L47–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_216.txt#L47)

### OC11_MEIKO · MEIKO

**成长细分判断：** 主线茶杯比喻直接促见冬弥，重要关系因果清楚但本人归因仍共谢。

**情感细分判断：** 真实听相棒否定痛苦，伸展/集会有本人动作，但直接情感表达及特殊定位仍较弱。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|1,3,2,2|
|细档|3.5,4,1,1,2|1,3.5,2.25,2.5|

原粗档指数成长/情感 54.33 / 50.00；细分未归一原指数 60.58 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_MEIKO_G1 · street_01_17 レンとMEIKOととっておき.txt L7–8、11–16、22–34、36–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L7)；[OC11_Len_G1 · street_01_17 レンとMEIKOととっておき.txt L8–25、30–32、47–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L8)；[OC11_Len_X2 · street_01_17 レンとMEIKOととっておき.txt L41–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L41)；[OC11_MEIKO_X1 · talk_event_125.txt L37–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_125.txt#L37)；[OC11_Miku_X1 · 1447_東雲彰人_R4 背を叩く言葉 (event_214).txt L10–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1447_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E8%83%8C%E3%82%92%E5%8F%A9%E3%81%8F%E8%A8%80%E8%91%89%20%28event_214%29.txt#L10)；[OC11_MEIKO_E3 · 1446_桃井愛莉_R4 夢の力になるものは (event_214).txt L118–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1446_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E5%A4%A2%E3%81%AE%E5%8A%9B%E3%81%AB%E3%81%AA%E3%82%8B%E3%82%82%E3%81%AE%E3%81%AF%20%28event_214%29.txt#L118)

**情感比较正文：** [OC11_MEIKO_E3 · 1446_桃井愛莉_R4 夢の力になるものは (event_214).txt L118–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1446_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E5%A4%A2%E3%81%AE%E5%8A%9B%E3%81%AB%E3%81%AA%E3%82%8B%E3%82%82%E3%81%AE%E3%81%AF%20%28event_214%29.txt#L118)；[OC11_Len_X2 · street_01_17 レンとMEIKOととっておき.txt L41–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L41)；[OC11_Len_G1 · street_01_17 レンとMEIKOととっておき.txt L8–25、30–32、47–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L8)；[OC11_MEIKO_G1 · street_01_17 レンとMEIKOととっておき.txt L7–8、11–16、22–34、36–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/4%20Vivid%20BAD%20SQUAD/street_01_17%20%E3%83%AC%E3%83%B3%E3%81%A8MEIKO%E3%81%A8%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D.txt#L7)；[OC11_MEIKO_X1 · talk_event_125.txt L37–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_125.txt#L37)；[OC11_Miku_X1 · 1447_東雲彰人_R4 背を叩く言葉 (event_214).txt L10–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1447_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E8%83%8C%E3%82%92%E5%8F%A9%E3%81%8F%E8%A8%80%E8%91%89%20%28event_214%29.txt#L10)

### OC11_KAITO · KAITO

**成长细分判断：** 59误会类比促重新理解远野，实际准备尝试，未核成效回顾。

**情感细分判断：** 具名歉谢关心与团队相談充分，个人主动投入目前仅受邀参与。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,0,2|2,2,1,2|
|细档|2.25,4,1.25,0,2|2.25,2.25,1.25,2.25|

原粗档指数成长/情感 38.50 / 43.75；细分未归一原指数 42.88 / 50.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_KAITO_F1 · 059-06 ふわふわのパンケーキ.txt L70–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L70)；[OC10_KAITO_X3 · 059-06 ふわふわのパンケーキ.txt L87–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L87)；[OC11_KAITO_X1 · 1278_東雲彰人_RB Happy Birthday！！2025.txt L12–38](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1278_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L12)

**情感比较正文：** [OC11_KAITO_F1 · 059-06 ふわふわのパンケーキ.txt L70–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/059%20THE%20POWER%20OF%20UNITY%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/059-06%20%E3%81%B5%E3%82%8F%E3%81%B5%E3%82%8F%E3%81%AE%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD.txt#L70)；[OC11_KAITO_X1 · 1278_東雲彰人_RB Happy Birthday！！2025.txt L12–38](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1278_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L12)

### OC11_Miku · 初音未来

**成长细分判断：** 歌唱反馈与预警有具体帮助，新技法已由彰人自行采用。

**情感细分判断：** 回应其兴趣邀看摊位是主动个人行动；情感表达仍共同祝福的一般谢谢。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,2|1,2,2,2|
|细档|1.25,0,1.25,1,2|1,2.25,2.25,2.25|

原粗档指数成长/情感 23.33 / 43.75；细分未归一原指数 27.71 / 48.44。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC11_Miku_F1 · talk_grade2.txt L1095–1101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1095)；[OC11_Miku_X1 · 1447_東雲彰人_R4 背を叩く言葉 (event_214).txt L10–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1447_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E8%83%8C%E3%82%92%E5%8F%A9%E3%81%8F%E8%A8%80%E8%91%89%20%28event_214%29.txt#L10)；[OC11_Miku_X2 · 169-03 ドタバタの再会.txt L21–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/169%20Aim%20higher%20and%20higher%EF%BC%81%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/169-03%20%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%81%AE%E5%86%8D%E4%BC%9A.txt#L21)；[OC11_KAITO_X1 · 1278_東雲彰人_RB Happy Birthday！！2025.txt L12–38](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1278_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L12)

**情感比较正文：** [OC11_KAITO_X1 · 1278_東雲彰人_RB Happy Birthday！！2025.txt L12–38](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1278_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L12)；[OC11_Miku_F1 · talk_grade2.txt L1095–1101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1095)；[OC11_Miku_X1 · 1447_東雲彰人_R4 背を叩く言葉 (event_214).txt L10–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/11%20VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA/1447_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA_R4%20%E8%83%8C%E3%82%92%E5%8F%A9%E3%81%8F%E8%A8%80%E8%91%89%20%28event_214%29.txt#L10)；[OC11_Miku_X2 · 169-03 ドタバタの再会.txt L21–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/169%20Aim%20higher%20and%20higher%EF%BC%81%20%28VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD%29/169-03%20%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%81%AE%E5%86%8D%E4%BC%9A.txt#L21)

## 青柳冬弥

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|KAITO|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|初音未来|2|4|2|98.37|79.25|88.81|88.81|暂定：综合差距不足2分，子档微调可能换位|
|MEIKO|4|2|3|86.98|88.68|87.83|87.83|暂定：综合差距不足2分，子档微调可能换位|
|巡音流歌|3|3|4|90.24|83.02|86.63|86.63|研究估计；来源有依据，仍需独立复评|
|镜音铃|5|5|5|66.65|77.36|72.00|72.00|研究估计；来源有依据，仍需独立复评|
|镜音连|6|6|6|62.58|69.81|66.20|66.20|该组末位；仍为研究估计|

### OC12_KAITO · KAITO

**成长细分判断：** 21相棒支持、71古典资产及编曲改善三项具体归因，情绪/伙伴作用较Miku实务支线集中。

**情感细分判断：** 本人明确充分依靠、愿继续依靠并解释长期心理作用，深层父亲/搭档相談及回报均有具名证据。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,3|3,3,2,3|
|细档|3.5,9,2.5,1,3|3.5,3.5,2.5,3.75|

原粗档指数成长/情感 68.08 / 68.75；细分未归一原指数 76.83 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_KAITO_G1 · 021-06 相棒としてできること.txt L11–13、18–23、71–81、87、90–93、104–106、110–120、133–135、184–186](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/021%20STRAY%20BAD%20DOG%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/021-06%20%E7%9B%B8%E6%A3%92%E3%81%A8%E3%81%97%E3%81%A6%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L11)；[OC12_KAITO_G2 · 071-06 伝わるといいな.txt L8–10、23–25、28–30、37–39、59–61、65–67、78–80、84–86、89–91、93–97、113–118、125–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-06%20%E4%BC%9D%E3%82%8F%E3%82%8B%E3%81%A8%E3%81%84%E3%81%84%E3%81%AA.txt#L8)；[OC12_KAITO_G3 · 071-07 込められた願い.txt L116、121、126–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-07%20%E8%BE%BC%E3%82%81%E3%82%89%E3%82%8C%E3%81%9F%E9%A1%98%E3%81%84.txt#L116)；[OC10_KAITO_F1 · 021-06 相棒としてできること.txt L103–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/021%20STRAY%20BAD%20DOG%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/021-06%20%E7%9B%B8%E6%A3%92%E3%81%A8%E3%81%97%E3%81%A6%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L103)；[OC12_KAITO_E1 · 118-05 いつかの楽譜 (青柳冬弥).txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L59)；[OC12_KAITO_E5 · 118-05 いつかの楽譜 (青柳冬弥).txt L62–66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L62)；[OC12_KAITO_X1 · 118-05 いつかの楽譜 (青柳冬弥).txt L47–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L47)；[OC12_KAITO_X3 · talk_grade2.txt L1203–1216](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1203)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)

**情感比较正文：** [OC12_KAITO_E1 · 118-05 いつかの楽譜 (青柳冬弥).txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L59)；[OC12_KAITO_E3 · 0893_KAITO (VBS)_R3 困難を支えて (event_125).txt L129–133](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0893_KAITO%20%28VBS%29_R3%20%E5%9B%B0%E9%9B%A3%E3%82%92%E6%94%AF%E3%81%88%E3%81%A6%20%28event_125%29.txt#L129)；[OC12_KAITO_X1 · 118-05 いつかの楽譜 (青柳冬弥).txt L47–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L47)；[OC12_KAITO_G1 · 021-06 相棒としてできること.txt L11–13、18–23、71–81、87、90–93、104–106、110–120、133–135、184–186](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/021%20STRAY%20BAD%20DOG%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/021-06%20%E7%9B%B8%E6%A3%92%E3%81%A8%E3%81%97%E3%81%A6%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L11)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)；[OC12_KAITO_X2 · 0214_KAITO (VBS)_R4 陽気なDJ現る？ (event_21).txt L98–110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0214_KAITO%20%28VBS%29_R4%20%E9%99%BD%E6%B0%97%E3%81%AADJ%E7%8F%BE%E3%82%8B%EF%BC%9F%20%28event_21%29.txt#L98)；[OC12_KAITO_E5 · 118-05 いつかの楽譜 (青柳冬弥).txt L62–66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/118%20BREAK%20DOWN%20THE%20WALL%20%28VBS_WL%29/118-05%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E6%A5%BD%E8%AD%9C%20%28%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29.txt#L62)

### OC12_Miku · 初音未来

**成长细分判断：** 0403压抑负担、71古典意义及87料理有不同结果，核心自我讨论较深但料理未完美成功。

**情感细分判断：** 童年期待与吞痛苦真实说出，蛋糕工具实际贡献，但定位主要具体料理/相談师友。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,3|2,3,2,2|
|细档|3.5,9,2.25,1,3|2.25,3.5,2.25,2.5|

原粗档指数成长/情感 68.08 / 56.25；细分未归一原指数 75.58 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_Miku_G1 · 071-06 伝わるといいな.txt L7–18、21–22、59–61、65–67、78–80、84–86、91–93、113–117、125–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-06%20%E4%BC%9D%E3%82%8F%E3%82%8B%E3%81%A8%E3%81%84%E3%81%84%E3%81%AA.txt#L7)；[OC12_Miku_G2 · 071-07 込められた願い.txt L97、103、105、116、121、126–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/071%20Walk%20on%20and%20on%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/071-07%20%E8%BE%BC%E3%82%81%E3%82%89%E3%82%8C%E3%81%9F%E9%A1%98%E3%81%84.txt#L97)；[OC12_Miku_X1 · 0403_青柳冬弥_R4 のみこんでしまっていた想い.txt L177–245](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0403_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E3%81%AE%E3%81%BF%E3%81%93%E3%82%93%E3%81%A7%E3%81%97%E3%81%BE%E3%81%A3%E3%81%A6%E3%81%84%E3%81%9F%E6%83%B3%E3%81%84.txt#L177)；[OC12_Miku_E1 · 087-05 レッツ、クッキング♪.txt L55–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-05%20%E3%83%AC%E3%83%83%E3%83%84%E3%80%81%E3%82%AF%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E2%99%AA.txt#L55)；[OC12_Miku_E3 · 087-03 頼りになる先生？.txt L128–132](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-03%20%E9%A0%BC%E3%82%8A%E3%81%AB%E3%81%AA%E3%82%8B%E5%85%88%E7%94%9F%EF%BC%9F.txt#L128)；[OC12_Miku_X2 · 087-05 レッツ、クッキング♪.txt L59–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-05%20%E3%83%AC%E3%83%83%E3%83%84%E3%80%81%E3%82%AF%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E2%99%AA.txt#L59)；[OC12_Miku_X3 · 087-06 いざ、試食！.txt L7–22](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-06%20%E3%81%84%E3%81%96%E3%80%81%E8%A9%A6%E9%A3%9F%EF%BC%81.txt#L7)；[OC12_Miku_E2 · 0890_青柳冬弥_R4 枷は、鍵に (event_125).txt L75–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0890_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E6%9E%B7%E3%81%AF%E3%80%81%E9%8D%B5%E3%81%AB%20%28event_125%29.txt#L75)

**情感比较正文：** [OC12_Miku_E5 · 0403_青柳冬弥_R4 のみこんでしまっていた想い.txt L243–247](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0403_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E3%81%AE%E3%81%BF%E3%81%93%E3%82%93%E3%81%A7%E3%81%97%E3%81%BE%E3%81%A3%E3%81%A6%E3%81%84%E3%81%9F%E6%83%B3%E3%81%84.txt#L243)；[OC12_Miku_E6 · 087-06 いざ、試食！.txt L20–24](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-06%20%E3%81%84%E3%81%96%E3%80%81%E8%A9%A6%E9%A3%9F%EF%BC%81.txt#L20)；[OC12_Miku_E2 · 0890_青柳冬弥_R4 枷は、鍵に (event_125).txt L75–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0890_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E6%9E%B7%E3%81%AF%E3%80%81%E9%8D%B5%E3%81%AB%20%28event_125%29.txt#L75)；[OC12_Miku_X1 · 0403_青柳冬弥_R4 のみこんでしまっていた想い.txt L177–245](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0403_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E3%81%AE%E3%81%BF%E3%81%93%E3%82%93%E3%81%A7%E3%81%97%E3%81%BE%E3%81%A3%E3%81%A6%E3%81%84%E3%81%9F%E6%83%B3%E3%81%84.txt#L177)；[OC10_Miku_X2 · 0706_初音ミク_RB Happy Anniversary！！2023.txt L13–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0706_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L13)；[OC12_Miku_E1 · 087-05 レッツ、クッキング♪.txt L55–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/087%20Never%20Give%20Up%20Cooking%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/087-05%20%E3%83%AC%E3%83%83%E3%83%84%E3%80%81%E3%82%AF%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E2%99%AA.txt#L55)

### OC12_MEIKO · MEIKO

**成长细分判断：** 125提示回看难说的自我情绪被实际采用，父亲最终和解仍由本人完成。

**情感细分判断：** 相棒痛苦和父亲负担多场实际向店内听众交托，咖啡店作为放下负荷的归属有本人明确说明。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,2,3|
|细档|3.5,4,2.25,1,2|2.25,3.5,2.5,3.5|

原粗档指数成长/情感 59.33 / 62.50；细分未归一原指数 66.83 / 73.44。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_MEIKO_F1 · 125-05 書かれていない想い.txt L124–139](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/125%20The%20first%20concerto%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/125-05%20%E6%9B%B8%E3%81%8B%E3%82%8C%E3%81%A6%E3%81%84%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L124)；[OC12_MEIKO_X1 · 125-06 消えない負い目.txt L14–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/125%20The%20first%20concerto%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/125-06%20%E6%B6%88%E3%81%88%E3%81%AA%E3%81%84%E8%B2%A0%E3%81%84%E7%9B%AE.txt#L14)；[OC12_MEIKO_E2 · 125-05 書かれていない想い.txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/125%20The%20first%20concerto%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/125-05%20%E6%9B%B8%E3%81%8B%E3%82%8C%E3%81%A6%E3%81%84%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L67)；[OC12_MEIKO_E4 · 0102_MEIKO (VBS)_R2 ストリートのセカイ.txt L58–62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0102_MEIKO%20%28VBS%29_R2%20%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%88%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L58)；[OC12_Rin_X1 · 139-02 接客特訓！.txt L35–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-02%20%E6%8E%A5%E5%AE%A2%E7%89%B9%E8%A8%93%EF%BC%81.txt#L35)；[OC12_MEIKO_X2 · talk_event_125.txt L56–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_125.txt#L56)；[OC12_Luka_X2 · 1181_青柳冬弥_R4 美味しい文化交流 (event_169).txt L113–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1181_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E7%BE%8E%E5%91%B3%E3%81%97%E3%81%84%E6%96%87%E5%8C%96%E4%BA%A4%E6%B5%81%20%28event_169%29.txt#L113)

**情感比较正文：** [OC12_MEIKO_E1 · talk_grade2.txt L1188–1192](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1188)；[OC12_MEIKO_E2 · 125-05 書かれていない想い.txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/125%20The%20first%20concerto%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/125-05%20%E6%9B%B8%E3%81%8B%E3%82%8C%E3%81%A6%E3%81%84%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L67)；[OC12_MEIKO_X2 · talk_event_125.txt L56–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_125.txt#L56)；[OC12_MEIKO_F1 · 125-05 書かれていない想い.txt L124–139](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/125%20The%20first%20concerto%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/125-05%20%E6%9B%B8%E3%81%8B%E3%82%8C%E3%81%A6%E3%81%84%E3%81%AA%E3%81%84%E6%83%B3%E3%81%84.txt#L124)；[OC12_MEIKO_E4 · 0102_MEIKO (VBS)_R2 ストリートのセカイ.txt L58–62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0102_MEIKO%20%28VBS%29_R2%20%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%88%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L58)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X2 · 1181_青柳冬弥_R4 美味しい文化交流 (event_169).txt L113–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1181_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E7%BE%8E%E5%91%B3%E3%81%97%E3%81%84%E6%96%87%E5%8C%96%E4%BA%A4%E6%B5%81%20%28event_169%29.txt#L113)

### OC12_Luka · 巡音流歌

**成长细分判断：** 44帮助超越仅能提供音乐知识的框架，本人回顾能为团队做事，核心自我作用直接。

**情感细分判断：** 完整父亲逃离故事与本人成果分享，按喜好准备器皿虽未确认交付，个别顾问意义较清楚。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,3|2,3,2,2|
|细档|3.5,4,2.5,1,3|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 60.58 / 56.25；细分未归一原指数 69.33 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_Luka_G1 · 044-02 見えない景色.txt L8–10、14–16、18–23、25、50–52、62–72、75、81、87–88、91–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/044%20Same%20Dreams%2CSame%20Colors%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/044-02%20%E8%A6%8B%E3%81%88%E3%81%AA%E3%81%84%E6%99%AF%E8%89%B2.txt#L8)；[OC12_Luka_G2 · 044-06 それぞれのできること.txt L28–30、34–35、37、43–45、75–78、81–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/044%20Same%20Dreams%2CSame%20Colors%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/044-06%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L28)；[OC12_Luka_G3 · 079-06 もし限界があるのなら.txt L118、120–121、127–131、134–138、141–149、153](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/079%20Find%20A%20Way%20Out%20%28VBS_%E6%9D%B1%E9%9B%B2%E5%BD%B0%E4%BA%BA%29/079-06%20%E3%82%82%E3%81%97%E9%99%90%E7%95%8C%E3%81%8C%E3%81%82%E3%82%8B%E3%81%AE%E3%81%AA%E3%82%89.txt#L118)；[OC11_Luka_X3 · 0582_巡音ルカ_RB Happy Anniversary！！2023.txt L12–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0582_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L12)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)；[OC12_Luka_X2 · 1181_青柳冬弥_R4 美味しい文化交流 (event_169).txt L113–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1181_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E7%BE%8E%E5%91%B3%E3%81%97%E3%81%84%E6%96%87%E5%8C%96%E4%BA%A4%E6%B5%81%20%28event_169%29.txt#L113)；[OC12_Len_X1 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L244–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L244)

**情感比较正文：** [OC12_Luka_G2 · 044-06 それぞれのできること.txt L28–30、34–35、37、43–45、75–78、81–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/044%20Same%20Dreams%2CSame%20Colors%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/044-06%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8.txt#L28)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)；[OC12_Luka_X2 · 1181_青柳冬弥_R4 美味しい文化交流 (event_169).txt L113–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1181_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E7%BE%8E%E5%91%B3%E3%81%97%E3%81%84%E6%96%87%E5%8C%96%E4%BA%A4%E6%B5%81%20%28event_169%29.txt#L113)；[OC12_Luka_G1 · 044-02 見えない景色.txt L8–10、14–16、18–23、25、50–52、62–72、75、81、87–88、91–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/044%20Same%20Dreams%2CSame%20Colors%20%28VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/044-02%20%E8%A6%8B%E3%81%88%E3%81%AA%E3%81%84%E6%99%AF%E8%89%B2.txt#L8)；[OC11_Luka_X3 · 0582_巡音ルカ_RB Happy Anniversary！！2023.txt L12–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0582_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L12)

### OC12_Rin · 镜音铃

**成长细分判断：** 139实际顾客模拟提高接客，191/204另属应援和照料，不增核心教学线。

**情感细分判断：** 103父亲训练真实共同听见，个人回报主要相册协作；持续自我相談的个别渠道较少。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,3,2,2|
|细档|2.25,4,2.25,1,2|2.25,3.25,2.25,2.5|

原粗档指数成长/情感 46.83 / 56.25；细分未归一原指数 51.21 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_Rin_X1 · 139-02 接客特訓！.txt L35–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-02%20%E6%8E%A5%E5%AE%A2%E7%89%B9%E8%A8%93%EF%BC%81.txt#L35)；[OC12_Rin_F1 · 139-08 憧れと喜び.txt L46–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-08%20%E6%86%A7%E3%82%8C%E3%81%A8%E5%96%9C%E3%81%B3.txt#L46)；[OC12_Rin_E2 · 191-06 祭りの夜.txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/191%20%E6%96%B0%E5%B9%B4%E8%A8%80%E7%A5%9D%E3%81%90%E3%80%81%E7%A5%88%E3%82%8A%E3%81%AE%E8%88%9E%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/191-06%20%E7%A5%AD%E3%82%8A%E3%81%AE%E5%A4%9C.txt#L12)；[OC12_Rin_E3 · talk_event_204.txt L69–73](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_204.txt#L69)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)

**情感比较正文：** [OC12_Rin_F1 · 139-08 憧れと喜び.txt L46–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-08%20%E6%86%A7%E3%82%8C%E3%81%A8%E5%96%9C%E3%81%B3.txt#L46)；[OC12_Rin_E2 · 191-06 祭りの夜.txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/191%20%E6%96%B0%E5%B9%B4%E8%A8%80%E7%A5%9D%E3%81%90%E3%80%81%E7%A5%88%E3%82%8A%E3%81%AE%E8%88%9E%20%28Mix_%E8%8A%B1%E9%87%8C%E3%81%BF%E3%81%AE%E3%82%8A%29/191-06%20%E7%A5%AD%E3%82%8A%E3%81%AE%E5%A4%9C.txt#L12)；[OC12_Rin_E3 · talk_event_204.txt L69–73](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_204.txt#L69)；[OC12_Rin_X1 · 139-02 接客特訓！.txt L35–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-02%20%E6%8E%A5%E5%AE%A2%E7%89%B9%E8%A8%93%EF%BC%81.txt#L35)；[OC12_Luka_X1 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L90–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L90)；[OC12_Luka_X3 · 0696_青柳冬弥_R4 久しぶりのお見舞い (event_103).txt L125–141](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/0696_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B9%85%E3%81%97%E3%81%B6%E3%82%8A%E3%81%AE%E3%81%8A%E8%A6%8B%E8%88%9E%E3%81%84%20%28event_103%29.txt#L125)；[OC09_Rin_X3 · 0838_鏡音リン_RB Happy Anniversary！！2023.txt L31–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0838_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L31)

### OC12_Len · 镜音连

**成长细分判断：** 139同样有实际接客帮助，1415反思核心答案来自冬弥与过去自己，新增作用以陪伴为主。

**情感细分判断：** 共同碎片/场所分享与黄色花束真实，旧自我前的对白不自动当向连深层交托。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,2,2|
|细档|2,4,2.25,1,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 46.83 / 50.00；细分未归一原指数 48.08 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC12_Rin_X1 · 139-02 接客特訓！.txt L35–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-02%20%E6%8E%A5%E5%AE%A2%E7%89%B9%E8%A8%93%EF%BC%81.txt#L35)；[OC12_Rin_F1 · 139-08 憧れと喜び.txt L46–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-08%20%E6%86%A7%E3%82%8C%E3%81%A8%E5%96%9C%E3%81%B3.txt#L46)；[OC12_Len_F1 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L303–317](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L303)；[OC12_Len_X1 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L244–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L244)；[OC12_Len_X2 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L99–138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L99)

**情感比较正文：** [OC12_Rin_F1 · 139-08 憧れと喜び.txt L46–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/139%20%E9%B3%B4%E3%82%89%E3%81%9B%E3%83%93%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%95%E3%83%AB%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/139-08%20%E6%86%A7%E3%82%8C%E3%81%A8%E5%96%9C%E3%81%B3.txt#L46)；[OC12_Len_F1 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L303–317](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L303)；[OC12_Len_X2 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L99–138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L99)；[OC12_Len_X1 · 1415_青柳冬弥_R4 一緒に帰ろう.txt L244–293](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/12%20VBS_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5/1415_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5_R4%20%E4%B8%80%E7%B7%92%E3%81%AB%E5%B8%B0%E3%82%8D%E3%81%86.txt#L244)；[OC11_Rin_X2 · talk_event_163.txt L36–59](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_163.txt#L36)

## 天马司

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|KAITO|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|3|3|2|88.88|89.80|89.34|89.34|研究估计；来源有依据，仍需独立复评|
|初音未来|2|5|3|91.43|75.51|83.47|83.47|研究估计；来源有依据，仍需独立复评|
|镜音连|5|2|4|61.17|95.92|78.55|78.55|研究估计；来源有依据，仍需独立复评|
|MEIKO|4|6|5|70.36|73.47|71.91|71.91|研究估计；来源有依据，仍需独立复评|
|镜音铃|6|4|6|32.40|85.71|59.06|59.06|该组末位；仍为研究估计|

### OC13_KAITO · KAITO

**成长细分判断：** 主线明星意义与多项实际脚本/表演支持，虽非童年起点，但本人具体合作归因多且清楚。

**情感细分判断：** 持续个人合作、被其依靠开心以及共同日记，将关系延伸到回忆记录，定位比临时表演伙伴更稳定。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,10,2,2,2|3,2,3,2|
|细档|3.5,10,2.75,2,2|3.5,2.5,3.5,2.75|

原粗档指数成长/情感 71.67 / 62.50；细分未归一原指数 81.67 / 76.56。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_KAITO_G1 · wonder_01_13 失った笑顔.txt L24–26、83、89、95、101–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_13%20%E5%A4%B1%E3%81%A3%E3%81%9F%E7%AC%91%E9%A1%94.txt#L24)；[OC13_KAITO_G2 · wonder_01_14 あの日の想い.txt L20–22、24–26、32、34–35、37–38、45–49、61–63、73–75、95–97、100–104、112–114、117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_14%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E3%81%84.txt#L20)；[OC13_KAITO_X3 · 0140_KAITO (WxS)_R4 ヒミツの演技指導 (event_7).txt L17–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0140_KAITO%20%28WxS%29_R4%20%E3%83%92%E3%83%9F%E3%83%84%E3%81%AE%E6%BC%94%E6%8A%80%E6%8C%87%E5%B0%8E%20%28event_7%29.txt#L17)；[OC13_KAITO_X5 · 0140_KAITO (WxS)_R4 ヒミツの演技指導 (event_7).txt L100–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0140_KAITO%20%28WxS%29_R4%20%E3%83%92%E3%83%9F%E3%83%84%E3%81%AE%E6%BC%94%E6%8A%80%E6%8C%87%E5%B0%8E%20%28event_7%29.txt#L100)；[OC13_KAITO_X2 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L62–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L62)；[OC13_KAITO_X6 · talk_event_113.txt L60–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_113.txt#L60)；[OC13_KAITO_X7 · 095-06 どんなことも力にして.txt L45–65](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/095%20%E3%82%AB%E3%83%8A%E3%83%AA%E3%82%A2%E3%81%AF%E7%AA%AE%E5%A2%83%E3%81%AB%E6%AD%8C%E3%81%86%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/095-06%20%E3%81%A9%E3%82%93%E3%81%AA%E3%81%93%E3%81%A8%E3%82%82%E5%8A%9B%E3%81%AB%E3%81%97%E3%81%A6.txt#L45)；[OC13_KAITO_X4 · 1454_KAITO (WxS)_R4 はやる想いをスプーンに乗せて (event_215).txt L103–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1454_KAITO%20%28WxS%29_R4%20%E3%81%AF%E3%82%84%E3%82%8B%E6%83%B3%E3%81%84%E3%82%92%E3%82%B9%E3%83%97%E3%83%BC%E3%83%B3%E3%81%AB%E4%B9%97%E3%81%9B%E3%81%A6%20%28event_215%29.txt#L103)；[OC13_KAITO_E6 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L98–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L98)；[OC13_Miku_E6 · 0410_天馬司_R4 星の旋律 (event_55).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0410_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E6%98%9F%E3%81%AE%E6%97%8B%E5%BE%8B%20%28event_55%29.txt#L100)

**情感比较正文：** [OC13_KAITO_E6 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L98–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L98)；[OC13_Miku_E6 · 0410_天馬司_R4 星の旋律 (event_55).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0410_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E6%98%9F%E3%81%AE%E6%97%8B%E5%BE%8B%20%28event_55%29.txt#L100)；[OC13_KAITO_X4 · 1454_KAITO (WxS)_R4 はやる想いをスプーンに乗せて (event_215).txt L103–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1454_KAITO%20%28WxS%29_R4%20%E3%81%AF%E3%82%84%E3%82%8B%E6%83%B3%E3%81%84%E3%82%92%E3%82%B9%E3%83%97%E3%83%BC%E3%83%B3%E3%81%AB%E4%B9%97%E3%81%9B%E3%81%A6%20%28event_215%29.txt#L103)；[OC13_KAITO_E1 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L40–44](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L40)；[OC13_KAITO_E3 · 0272_KAITO (WxS)_R3 座長の一日休暇 (event_32).txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0272_KAITO%20%28WxS%29_R3%20%E5%BA%A7%E9%95%B7%E3%81%AE%E4%B8%80%E6%97%A5%E4%BC%91%E6%9A%87%20%28event_32%29.txt#L19)；[OC13_KAITO_X1 · 055-05 共通点.txt L34–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/055%20%E3%81%BE%E3%81%B0%E3%82%86%E3%81%84%E5%85%89%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%A7%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/055-05%20%E5%85%B1%E9%80%9A%E7%82%B9.txt#L34)；[OC13_KAITO_X3 · 0140_KAITO (WxS)_R4 ヒミツの演技指導 (event_7).txt L17–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0140_KAITO%20%28WxS%29_R4%20%E3%83%92%E3%83%9F%E3%83%84%E3%81%AE%E6%BC%94%E6%8A%80%E6%8C%87%E5%B0%8E%20%28event_7%29.txt#L17)；[OC13_KAITO_G2 · wonder_01_14 あの日の想い.txt L20–22、24–26、32、34–35、37–38、45–49、61–63、73–75、95–97、100–104、112–114、117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_14%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E3%81%84.txt#L20)

### OC13_Luka · 巡音流歌

**成长细分判断：** 16改变兄妹理解并回家、100本人再确认，持续重要关系作用清楚。

**情感细分判断：** 本人说明咲希争执并回来谢，帮摆人偶/防受凉为生活性照顾，比单纯愿望实现更私人。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,2,3,2|
|细档|3.5,7,2.5,1,2|2.25,2.5,3.5,2.75|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 72.58 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_Luka_X4 · 016-06 行くべき場所.txt L38–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/016%20%E5%A4%A9%E9%A6%AC%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%81%B2%E3%81%AA%E7%A5%AD%E3%82%8A%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/016-06%20%E8%A1%8C%E3%81%8F%E3%81%B9%E3%81%8D%E5%A0%B4%E6%89%80.txt#L38)；[OC13_Luka_X5 · 016-06 行くべき場所.txt L100–119](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/016%20%E5%A4%A9%E9%A6%AC%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%81%B2%E3%81%AA%E7%A5%AD%E3%82%8A%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/016-06%20%E8%A1%8C%E3%81%8F%E3%81%B9%E3%81%8D%E5%A0%B4%E6%89%80.txt#L100)；[OC13_Luka_X3 · 0186_天馬司_R4 お兄ちゃんの苦悩 (event_16).txt L69–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0186_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E3%81%8A%E5%85%84%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E8%8B%A6%E6%82%A9%20%28event_16%29.txt#L69)；[OC13_Luka_F1 · 1343_天馬司_R2 眠れない夜には (event_196).txt L48–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/1343_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R2%20%E7%9C%A0%E3%82%8C%E3%81%AA%E3%81%84%E5%A4%9C%E3%81%AB%E3%81%AF%20%28event_196%29.txt#L48)；[OC13_Luka_E1 · 0186_天馬司_R4 お兄ちゃんの苦悩 (event_16).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0186_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E3%81%8A%E5%85%84%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E8%8B%A6%E6%82%A9%20%28event_16%29.txt#L131)；[OC13_Luka_X2 · talk_event_016.txt L91–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_016.txt#L91)

**情感比较正文：** [OC13_Luka_E1 · 0186_天馬司_R4 お兄ちゃんの苦悩 (event_16).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0186_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E3%81%8A%E5%85%84%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E8%8B%A6%E6%82%A9%20%28event_16%29.txt#L131)；[OC13_Luka_F1 · 1343_天馬司_R2 眠れない夜には (event_196).txt L48–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/1343_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R2%20%E7%9C%A0%E3%82%8C%E3%81%AA%E3%81%84%E5%A4%9C%E3%81%AB%E3%81%AF%20%28event_196%29.txt#L48)；[OC13_Luka_X4 · 016-06 行くべき場所.txt L38–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/016%20%E5%A4%A9%E9%A6%AC%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%81%B2%E3%81%AA%E7%A5%AD%E3%82%8A%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/016-06%20%E8%A1%8C%E3%81%8F%E3%81%B9%E3%81%8D%E5%A0%B4%E6%89%80.txt#L38)；[OC13_Luka_X2 · talk_event_016.txt L91–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_016.txt#L91)；[OC13_Luka_X3 · 0186_天馬司_R4 お兄ちゃんの苦悩 (event_16).txt L69–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0186_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E3%81%8A%E5%85%84%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E8%8B%A6%E6%82%A9%20%28event_16%29.txt#L69)

### OC13_Miku · 初音未来

**成长细分判断：** 主线协助重连表演初心且后续演出共归因，童年真正起点不是Miku创造。

**情感细分判断：** 脚本/角色困难具体相談和周年脚本本人参与，童年内心未口述，亲近主要协作。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,2|2,2,2,2|
|细档|3.5,7,2.25,2,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 67.17 / 50.00；细分未归一原指数 74.67 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_Miku_G1 · wonder_01_13 失った笑顔.txt L24–26、95、101–102](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_13%20%E5%A4%B1%E3%81%A3%E3%81%9F%E7%AC%91%E9%A1%94.txt#L24)；[OC13_Miku_G2 · wonder_01_14 あの日の想い.txt L20–22、24–26、32、34–35、37–38、44–47、49–51、61–63、73–75、97–100、103–104、112–114、117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_14%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E3%81%84.txt#L20)；[OC13_Miku_X1 · 055-05 共通点.txt L91–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/055%20%E3%81%BE%E3%81%B0%E3%82%86%E3%81%84%E5%85%89%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%A7%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/055-05%20%E5%85%B1%E9%80%9A%E7%82%B9.txt#L91)；[OC13_Miku_X2 · 055-07 星を見つけて.txt L90–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/055%20%E3%81%BE%E3%81%B0%E3%82%86%E3%81%84%E5%85%89%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%A7%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/055-07%20%E6%98%9F%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%81%A6.txt#L90)；[OC13_Miku_E6 · 0410_天馬司_R4 星の旋律 (event_55).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0410_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E6%98%9F%E3%81%AE%E6%97%8B%E5%BE%8B%20%28event_55%29.txt#L100)；[OC13_Miku_E5 · 160-01 ランニング中の出会い.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/160%20You%20are%20my%20HERO%21%21%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/160-01%20%E3%83%A9%E3%83%B3%E3%83%8B%E3%83%B3%E3%82%B0%E4%B8%AD%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L19)

**情感比较正文：** [OC13_Miku_E4 · 1133_天馬司_R4 ヒーローからヒーローへ (event_160).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/1133_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%81%8B%E3%82%89%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%81%B8%20%28event_160%29.txt#L12)；[OC13_Miku_E5 · 160-01 ランニング中の出会い.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/160%20You%20are%20my%20HERO%21%21%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/160-01%20%E3%83%A9%E3%83%B3%E3%83%8B%E3%83%B3%E3%82%B0%E4%B8%AD%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L19)；[OC13_Miku_E6 · 0410_天馬司_R4 星の旋律 (event_55).txt L100–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/13%20WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8/0410_%E5%A4%A9%E9%A6%AC%E5%8F%B8_R4%20%E6%98%9F%E3%81%AE%E6%97%8B%E5%BE%8B%20%28event_55%29.txt#L100)；[OC13_Miku_E2 · 0272_KAITO (WxS)_R3 座長の一日休暇 (event_32).txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0272_KAITO%20%28WxS%29_R3%20%E5%BA%A7%E9%95%B7%E3%81%AE%E4%B8%80%E6%97%A5%E4%BC%91%E6%9A%87%20%28event_32%29.txt#L19)；[OC13_Miku_E3 · 055-05 共通点.txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/055%20%E3%81%BE%E3%81%B0%E3%82%86%E3%81%84%E5%85%89%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%A7%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/055-05%20%E5%85%B1%E9%80%9A%E7%82%B9.txt#L93)；[OC13_KAITO_X1 · 055-05 共通点.txt L34–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/055%20%E3%81%BE%E3%81%B0%E3%82%86%E3%81%84%E5%85%89%E3%81%AE%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%81%A7%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/055-05%20%E5%85%B1%E9%80%9A%E7%82%B9.txt#L34)；[OC13_Miku_E8 · 1193_神代類_RB Happy Birthday！！2025.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1193_%E7%A5%9E%E4%BB%A3%E9%A1%9E_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L19)；[OC13_Luka_X4 · 016-06 行くべき場所.txt L38–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/016%20%E5%A4%A9%E9%A6%AC%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%81%B2%E3%81%AA%E7%A5%AD%E3%82%8A%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C%29/016-06%20%E8%A1%8C%E3%81%8F%E3%81%B9%E3%81%8D%E5%A0%B4%E6%89%80.txt#L38)；[OC13_Miku_G2 · wonder_01_14 あの日の想い.txt L20–22、24–26、32、34–35、37–38、44–47、49–51、61–63、73–75、97–100、103–104、112–114、117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/5%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%BA%C3%97%E3%82%B7%E3%83%A7%E3%82%A6%E3%82%BF%E3%82%A4%E3%83%A0/wonder_01_14%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E3%81%84.txt#L20)

### OC13_Len · 镜音连

**成长细分判断：** 回礼方式决定有实际促进，原本手做意愿已存在，非核心身份转折。

**情感细分判断：** 持续演出安心与主动回报、组织重逢很明确，但核心本人脆弱交托目前不足。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,1|3,2,3,2|
|细档|2.25,4,2.25,1,1|3.25,2.5,3.5,2.5|

原粗档指数成长/情感 45.58 / 62.50；细分未归一原指数 49.96 / 73.44。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_Len_F1 · 0389_鏡音レン (WxS)_R2 イノセント・スクワイア (event_51).txt L55–74](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0389_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%8E%E3%82%BB%E3%83%B3%E3%83%88%E3%83%BB%E3%82%B9%E3%82%AF%E3%83%AF%E3%82%A4%E3%82%A2%20%28event_51%29.txt#L55)；[OC13_Len_E2 · 051-01 サプライズを考えて.txt L56–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/051%20%E6%80%AA%E7%9B%97%E7%B4%B3%E5%A3%AB%E3%81%AE%E3%83%8F%E3%83%A9%E3%83%8F%E3%83%A9%EF%BC%81%EF%BC%9F%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/051-01%20%E3%82%B5%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E3%82%92%E8%80%83%E3%81%88%E3%81%A6.txt#L56)；[OC13_Len_E3 · 0389_鏡音レン (WxS)_R2 イノセント・スクワイア (event_51).txt L87–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0389_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%8E%E3%82%BB%E3%83%B3%E3%83%88%E3%83%BB%E3%82%B9%E3%82%AF%E3%83%AF%E3%82%A4%E3%82%A2%20%28event_51%29.txt#L87)；[OC13_Len_E5 · 051-03 それぞれのお返し作り.txt L43–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/051%20%E6%80%AA%E7%9B%97%E7%B4%B3%E5%A3%AB%E3%81%AE%E3%83%8F%E3%83%A9%E3%83%8F%E3%83%A9%EF%BC%81%EF%BC%9F%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/051-03%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E3%81%8A%E8%BF%94%E3%81%97%E4%BD%9C%E3%82%8A.txt#L43)；[OC13_Rin_E1 · 205-01 導かれた出会い.txt L202–206](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/205%20Great%20Yell%20for%20Dreamers%EF%BC%81%20%28Mix_WL%29/205-01%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%81%9F%E5%87%BA%E4%BC%9A%E3%81%84.txt#L202)

**情感比较正文：** [OC13_Len_E3 · 0389_鏡音レン (WxS)_R2 イノセント・スクワイア (event_51).txt L87–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0389_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%8E%E3%82%BB%E3%83%B3%E3%83%88%E3%83%BB%E3%82%B9%E3%82%AF%E3%83%AF%E3%82%A4%E3%82%A2%20%28event_51%29.txt#L87)；[OC13_Rin_E1 · 205-01 導かれた出会い.txt L202–206](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/205%20Great%20Yell%20for%20Dreamers%EF%BC%81%20%28Mix_WL%29/205-01%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%81%9F%E5%87%BA%E4%BC%9A%E3%81%84.txt#L202)；[OC13_Len_E2 · 051-01 サプライズを考えて.txt L56–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/051%20%E6%80%AA%E7%9B%97%E7%B4%B3%E5%A3%AB%E3%81%AE%E3%83%8F%E3%83%A9%E3%83%8F%E3%83%A9%EF%BC%81%EF%BC%9F%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/051-01%20%E3%82%B5%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E3%82%92%E8%80%83%E3%81%88%E3%81%A6.txt#L56)；[OC13_Len_E5 · 051-03 それぞれのお返し作り.txt L43–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/051%20%E6%80%AA%E7%9B%97%E7%B4%B3%E5%A3%AB%E3%81%AE%E3%83%8F%E3%83%A9%E3%83%8F%E3%83%A9%EF%BC%81%EF%BC%9F%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88%E3%83%87%E3%83%BC%20%28Mix_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/051-03%20%E3%81%9D%E3%82%8C%E3%81%9E%E3%82%8C%E3%81%AE%E3%81%8A%E8%BF%94%E3%81%97%E4%BD%9C%E3%82%8A.txt#L43)

### OC13_MEIKO · MEIKO

**成长细分判断：** 113通过环境和问故事触发演出方向，关键建议及最终推理不独占给MEIKO。

**情感细分判断：** 庆祝演出、礼物和具体表演困难真实，直接关系较共同创作/节日型。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|2,2,2,2|
|细档|3.25,4,1,1,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 54.33 / 50.00；细分未归一原指数 57.46 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_MEIKO_F1 · 113-06 あの日の想像力を.txt L109–153](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/113%20%E5%90%9B%E3%81%8C%E4%B8%BB%E5%BD%B9%E3%81%AE%E7%89%A9%E8%AA%9E%E3%82%92%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/113-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E5%83%8F%E5%8A%9B%E3%82%92.txt#L109)；[OC13_MEIKO_X3 · 113-06 あの日の想像力を.txt L151–154](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/113%20%E5%90%9B%E3%81%8C%E4%B8%BB%E5%BD%B9%E3%81%AE%E7%89%A9%E8%AA%9E%E3%82%92%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/113-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E5%83%8F%E5%8A%9B%E3%82%92.txt#L151)；[OC13_MEIKO_X1 · 062-02 無人島サバイバル！.txt L80–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/062%20%E7%B5%B6%E4%BD%93%E7%B5%B6%E5%91%BD%EF%BC%81%EF%BC%9F%E3%82%A2%E3%82%A4%E3%83%A9%E3%83%B3%E3%83%89%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/062-02%20%E7%84%A1%E4%BA%BA%E5%B3%B6%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%EF%BC%81.txt#L80)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)

**情感比较正文：** [OC13_MEIKO_F1 · 113-06 あの日の想像力を.txt L109–153](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/113%20%E5%90%9B%E3%81%8C%E4%B8%BB%E5%BD%B9%E3%81%AE%E7%89%A9%E8%AA%9E%E3%82%92%20%28WxS_%E5%A4%A9%E9%A6%AC%E5%8F%B8%29/113-06%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E6%83%B3%E5%83%8F%E5%8A%9B%E3%82%92.txt#L109)；[OC13_MEIKO_X1 · 062-02 無人島サバイバル！.txt L80–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/062%20%E7%B5%B6%E4%BD%93%E7%B5%B6%E5%91%BD%EF%BC%81%EF%BC%9F%E3%82%A2%E3%82%A4%E3%83%A9%E3%83%B3%E3%83%89%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/062-02%20%E7%84%A1%E4%BA%BA%E5%B3%B6%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%EF%BC%81.txt#L80)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)

### OC13_Rin · 镜音铃

**成长细分判断：** 游戏与活动共同参与真实，无新K2结果，不把被帮助次数当成长。

**情感细分判断：** 司主动实现重逢及游戏愿望，185实际问宁宁困难；相談尚具体任务，个人照顾以伙伴游戏为主。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,1|2,2,3,2|
|细档|1.25,0,1.25,1,1|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 22.08 / 56.25；细分未归一原指数 26.46 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC13_Rin_F1 · talk_event_124.txt L26–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_124.txt#L26)；[OC13_Rin_E1 · 205-01 導かれた出会い.txt L202–206](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/205%20Great%20Yell%20for%20Dreamers%EF%BC%81%20%28Mix_WL%29/205-01%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%81%9F%E5%87%BA%E4%BC%9A%E3%81%84.txt#L202)；[OC13_Rin_E3 · talk_event_081.txt L37–41](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_081.txt#L37)；[OC13_Rin_X1 · 0305_鏡音リン (WxS)_R2 インテリシティガール (event_38).txt L73–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0305_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%B3%E3%83%86%E3%83%AA%E3%82%B7%E3%83%86%E3%82%A3%E3%82%AC%E3%83%BC%E3%83%AB%20%28event_38%29.txt#L73)；[OC13_Rin_X2 · 205-01 導かれた出会い.txt L148–177](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/205%20Great%20Yell%20for%20Dreamers%EF%BC%81%20%28Mix_WL%29/205-01%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%81%9F%E5%87%BA%E4%BC%9A%E3%81%84.txt#L148)

**情感比较正文：** [OC13_Rin_E1 · 205-01 導かれた出会い.txt L202–206](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/205%20Great%20Yell%20for%20Dreamers%EF%BC%81%20%28Mix_WL%29/205-01%20%E5%B0%8E%E3%81%8B%E3%82%8C%E3%81%9F%E5%87%BA%E4%BC%9A%E3%81%84.txt#L202)；[OC13_Rin_Y1 · 185-06 主役と演出家.txt L1–44](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/185%20%E8%B6%85%E5%85%8B%E3%81%AE%E3%83%97%E3%83%AD%E3%82%BF%E3%82%B4%E3%83%8B%E3%82%B9%E3%82%BF%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/185-06%20%E4%B8%BB%E5%BD%B9%E3%81%A8%E6%BC%94%E5%87%BA%E5%AE%B6.txt#L1)；[OC13_Rin_E3 · talk_event_081.txt L37–41](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_081.txt#L37)；[OC13_Rin_F1 · talk_event_124.txt L26–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_124.txt#L26)

## 凤笑梦

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|MEIKO|2|1|1|98.42|100.00|99.21|100.00|研究估计；来源有依据，仍需独立复评|
|镜音连|1|2|2|100.00|90.57|95.28|96.04|研究估计；来源有依据，仍需独立复评|
|KAITO|3|3|3|86.27|83.02|84.65|85.32|研究估计；来源有依据，仍需独立复评|
|镜音铃|4|5|4|82.73|69.81|76.27|76.88|研究估计；来源有依据，仍需独立复评|
|初音未来|5|4|5|58.55|77.36|67.96|68.50|研究估计；来源有依据，仍需独立复评|
|巡音流歌|6|6|6|53.01|67.92|60.47|60.95|该组末位；仍为研究估计|

### OC14_MEIKO · MEIKO

**成长细分判断：** 104分离未来及0897祖父失落触及个人核心，部分未来顿悟为群体共同支持，归因较连更间接。

**情感细分判断：** 祖父相会后的泪与怕记忆流失真实托付，专门零食回报和失落承接使个人意义更集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,2,2|3,3,3,2|
|细档|3.5,9,2.25,2,2|3.5,3.5,3.5,2.75|

原粗档指数成长/情感 70.17 / 68.75；细分未归一原指数 77.67 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_MEIKO_G1 · 131-07 みんなの『視点』.txt L7–12、18–20、22–24、26–28、40–42、53–54、57、66–68、89、93–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L7)；[OC14_MEIKO_F1 · 131-07 みんなの『視点』.txt L61–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L61)；[OC14_MEIKO_X1 · 0897_鳳えむ_R4 うたかたの再会.txt L187–227](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/0897_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%81%86%E3%81%9F%E3%81%8B%E3%81%9F%E3%81%AE%E5%86%8D%E4%BC%9A.txt#L187)；[OC14_MEIKO_X2 · talk_event_104.txt L76–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_104.txt#L76)；[OC14_MEIKO_X3 · 104-06 あなた達のためのショー.txt L67–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L67)；[OC14_MEIKO_X4 · 104-06 あなた達のためのショー.txt L112–165](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L112)；[OC14_MEIKO_X5 · 1471_鳳えむ_R4 全力いんぐりっしゅ！ (event_217).txt L29–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1471_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E5%85%A8%E5%8A%9B%E3%81%84%E3%82%93%E3%81%90%E3%82%8A%E3%81%A3%E3%81%97%E3%82%85%EF%BC%81%20%28event_217%29.txt#L29)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)

**情感比较正文：** [OC14_MEIKO_X1 · 0897_鳳えむ_R4 うたかたの再会.txt L187–227](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/0897_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%81%86%E3%81%9F%E3%81%8B%E3%81%9F%E3%81%AE%E5%86%8D%E4%BC%9A.txt#L187)；[OC14_MEIKO_X2 · talk_event_104.txt L76–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_104.txt#L76)；[OC14_MEIKO_X4 · 104-06 あなた達のためのショー.txt L112–165](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L112)；[OC14_MEIKO_F1 · 131-07 みんなの『視点』.txt L61–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L61)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)；[OC14_Miku_E6 · 030-02 発表会で何しよう？.txt L9–13](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/030%20%E3%81%8D%E3%81%A3%E3%81%A8%E6%9C%80%E9%AB%98%E3%81%AEsummer%EF%BC%81%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/030-02%20%E7%99%BA%E8%A1%A8%E4%BC%9A%E3%81%A7%E4%BD%95%E3%81%97%E3%82%88%E3%81%86%EF%BC%9F.txt#L9)

### OC14_Len · 镜音连

**成长细分判断：** 15情绪求助和131/149视点、竞演实践直接落实，表演/企划的本人具体归因较充分。

**情感细分判断：** 反复合作、记得电影角色送钥匙扣是个别回应，演员困难相談尚未完整深层哭诉。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,2,2|3,2,3,2|
|细档|3.5,9,2.5,2,2|3.5,2.5,3.5,2.5|

原粗档指数成长/情感 70.17 / 62.50；细分未归一原指数 78.92 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_Len_G1 · 015-06 涙のような笑顔より.txt L15、18–19、24–28、30–32、34–40、43–44、47–50、91–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L15)；[OC14_Len_G2 · 131-07 みんなの『視点』.txt L7–12、14–24、26–38、40–44、47、53–54、57、89、93–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L7)；[OC14_Len_X3 · 015-06 涙のような笑顔より.txt L51–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L51)；[OC14_Len_X2 · 1036_鏡音レン (WxS)_R4 エール☆フォー☆ユー！ (event_149).txt L135–162](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1036_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%A8%E3%83%BC%E3%83%AB%E2%98%86%E3%83%95%E3%82%A9%E3%83%BC%E2%98%86%E3%83%A6%E3%83%BC%EF%BC%81%20%28event_149%29.txt#L135)；[OC14_Len_E2 · 1036_鏡音レン (WxS)_R4 エール☆フォー☆ユー！ (event_149).txt L159–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1036_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%A8%E3%83%BC%E3%83%AB%E2%98%86%E3%83%95%E3%82%A9%E3%83%BC%E2%98%86%E3%83%A6%E3%83%BC%EF%BC%81%20%28event_149%29.txt#L159)；[OC14_Len_X1 · 1472_巡音ルカ (WxS)_R4 静かな祈り (event_217).txt L95–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1472_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28WxS%29_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E7%A5%88%E3%82%8A%20%28event_217%29.txt#L95)

**情感比较正文：** [OC14_Len_E2 · 1036_鏡音レン (WxS)_R4 エール☆フォー☆ユー！ (event_149).txt L159–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1036_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%A8%E3%83%BC%E3%83%AB%E2%98%86%E3%83%95%E3%82%A9%E3%83%BC%E2%98%86%E3%83%A6%E3%83%BC%EF%BC%81%20%28event_149%29.txt#L159)；[OC14_Len_E3 · 1472_巡音ルカ (WxS)_R4 静かな祈り (event_217).txt L101–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1472_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28WxS%29_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E7%A5%88%E3%82%8A%20%28event_217%29.txt#L101)；[OC14_Len_X1 · 1472_巡音ルカ (WxS)_R4 静かな祈り (event_217).txt L95–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1472_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28WxS%29_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E7%A5%88%E3%82%8A%20%28event_217%29.txt#L95)；[OC14_Len_G2 · 131-07 みんなの『視点』.txt L7–12、14–24、26–38、40–44、47、53–54、57、89、93–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L7)；[OC14_Len_E4 · 1036_鏡音レン (WxS)_R4 エール☆フォー☆ユー！ (event_149).txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1036_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%A8%E3%83%BC%E3%83%AB%E2%98%86%E3%83%95%E3%82%A9%E3%83%BC%E2%98%86%E3%83%A6%E3%83%BC%EF%BC%81%20%28event_149%29.txt#L39)；[OC14_Len_E5 · talk_event_131.txt L63–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_131.txt#L63)；[OC14_Len_E6 · talk_event_003.txt L36–40](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_003.txt#L36)；[OC14_Len_X4 · talk_event_131.txt L57–67](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_131.txt#L57)；[OC14_Len_G1 · 015-06 涙のような笑顔より.txt L15、18–19、24–28、30–32、34–40、43–44、47–50、91–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L15)

### OC14_KAITO · KAITO

**成长细分判断：** 164把经营改革恐惧转为向哥哥求经验并落实，涉及本人重要道路，仍不独占兄长教育。

**情感细分判断：** 真实说怕伤旧客又要保剧团，核心矛盾的个人信任比Miku日常玩法求助更深。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,2,2|
|细档|3.5,4,2.5,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 59.33 / 56.25；细分未归一原指数 68.08 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_KAITO_F1 · 164-04 進む足を止めるもの.txt L31–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-04%20%E9%80%B2%E3%82%80%E8%B6%B3%E3%82%92%E6%AD%A2%E3%82%81%E3%82%8B%E3%82%82%E3%81%AE.txt#L31)；[OC14_KAITO_X1 · 164-05 選んだ道.txt L28–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-05%20%E9%81%B8%E3%82%93%E3%81%A0%E9%81%93.txt#L28)；[OC14_KAITO_X2 · talk_event_108.txt L137–152](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_108.txt#L137)；[OC14_MEIKO_X3 · 104-06 あなた達のためのショー.txt L67–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L67)；[OC14_MEIKO_X4 · 104-06 あなた達のためのショー.txt L112–165](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L112)

**情感比较正文：** [OC14_KAITO_E2 · 164-04 進む足を止めるもの.txt L23–27](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-04%20%E9%80%B2%E3%82%80%E8%B6%B3%E3%82%92%E6%AD%A2%E3%82%81%E3%82%8B%E3%82%82%E3%81%AE.txt#L23)；[OC14_KAITO_E3 · 164-05 選んだ道.txt L24–28](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-05%20%E9%81%B8%E3%82%93%E3%81%A0%E9%81%93.txt#L24)；[OC14_KAITO_F1 · 164-04 進む足を止めるもの.txt L31–51](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-04%20%E9%80%B2%E3%82%80%E8%B6%B3%E3%82%92%E6%AD%A2%E3%82%81%E3%82%8B%E3%82%82%E3%81%AE.txt#L31)；[OC14_KAITO_X1 · 164-05 選んだ道.txt L28–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/164%20Choices%20for%20the%20future%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/164-05%20%E9%81%B8%E3%82%93%E3%81%A0%E9%81%93.txt#L28)；[OC14_KAITO_X2 · talk_event_108.txt L137–152](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_108.txt#L137)

### OC14_Rin · 镜音铃

**成长细分判断：** 15参与拆强笑及支持说困境，核心关系作用实际，但具名结果归因不充分。

**情感细分判断：** 相机/分享活动与被认作经营者开心成立，悲伤详细袒露主要对OC伙伴而非铃。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,1,2,2|2,2,2,2|
|细档|3.25,7,1,2,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 62.17 / 50.00；细分未归一原指数 65.29 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_Rin_G1 · 015-06 涙のような笑顔より.txt L15、18–19、27–33、38–40、44–48、91–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L15)；[OC14_Rin_G2 · 131-07 みんなの『視点』.txt L7–12、18–20、22–24、26–28、40–42、53–54、57、62、65–67、89、93–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/131%20perspective%20for%20smile%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/131-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AE%E3%80%8E%E8%A6%96%E7%82%B9%E3%80%8F.txt#L7)；[OC14_Len_X3 · 015-06 涙のような笑顔より.txt L51–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L51)；[OC14_Rin_X1 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L107–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L107)；[OC14_Rin_X2 · 0235_鏡音リン (WxS)_R3 スマイルナイトタイム！ (event_25).txt L126–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0235_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R3%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%83%8A%E3%82%A4%E3%83%88%E3%82%BF%E3%82%A4%E3%83%A0%EF%BC%81%20%28event_25%29.txt#L126)；[OC14_Miku_X1 · 0479_初音ミク (WxS)_R2 ミクミク☆ガンナー！ (event_66).txt L87–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0479_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%9F%E3%82%AF%E3%83%9F%E3%82%AF%E2%98%86%E3%82%AC%E3%83%B3%E3%83%8A%E3%83%BC%EF%BC%81%20%28event_66%29.txt#L87)

**情感比较正文：** [OC14_Rin_E1 · 179-13 みんながひとつに (鏡音リン).txt L6–10](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/179%20Link%20the%20Beats%EF%BC%81%20%28VS_WL%29/179-13%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%8C%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AB%20%28%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%29.txt#L6)；[OC14_Rin_E2 · 196-05 父への想い.txt L114–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/196%20CHANGE%EF%BC%81%E3%81%88%E3%82%80%E3%81%AF%E7%8E%8B%E5%A5%B3%E3%81%95%E3%81%BE%EF%BC%81%EF%BC%9F%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/196-05%20%E7%88%B6%E3%81%B8%E3%81%AE%E6%83%B3%E3%81%84.txt#L114)；[OC14_Rin_X2 · 0235_鏡音リン (WxS)_R3 スマイルナイトタイム！ (event_25).txt L126–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0235_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R3%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%83%8A%E3%82%A4%E3%83%88%E3%82%BF%E3%82%A4%E3%83%A0%EF%BC%81%20%28event_25%29.txt#L126)；[OC14_Rin_G1 · 015-06 涙のような笑顔より.txt L15、18–19、27–33、38–40、44–48、91–93](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/015%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%83%89%E3%83%AA%E3%83%BC%E3%83%9E%E3%83%BC%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/015-06%20%E6%B6%99%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E7%AC%91%E9%A1%94%E3%82%88%E3%82%8A.txt#L15)；[OC14_Rin_X1 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L107–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L107)；[OC14_Miku_X1 · 0479_初音ミク (WxS)_R2 ミクミク☆ガンナー！ (event_66).txt L87–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0479_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%9F%E3%82%AF%E3%83%9F%E3%82%AF%E2%98%86%E3%82%AC%E3%83%B3%E3%83%8A%E3%83%BC%EF%BC%81%20%28event_66%29.txt#L87)

### OC14_Miku · 初音未来

**成长细分判断：** 相机办法促实际回家拿器材并组织活动，核心未来选择不平均归共同演出。

**情感细分判断：** 零食会、拾贝及相机回应属持续生活活动，真实自我脆弱相談仍具体方法。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,1,2|2,2,3,2|
|细档|2.25,4,1.25,1,2|2.25,2.25,3.25,2.5|

原粗档指数成长/情感 41.83 / 56.25；细分未归一原指数 46.21 / 64.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_Miku_F1 · 0479_初音ミク (WxS)_R2 ミクミク☆ガンナー！ (event_66).txt L67–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0479_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%9F%E3%82%AF%E3%83%9F%E3%82%AF%E2%98%86%E3%82%AC%E3%83%B3%E3%83%8A%E3%83%BC%EF%BC%81%20%28event_66%29.txt#L67)；[OC14_Miku_X1 · 0479_初音ミク (WxS)_R2 ミクミク☆ガンナー！ (event_66).txt L87–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0479_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%9F%E3%82%AF%E3%83%9F%E3%82%AF%E2%98%86%E3%82%AC%E3%83%B3%E3%83%8A%E3%83%BC%EF%BC%81%20%28event_66%29.txt#L87)；[OC14_Miku_E2 · 004-04 センパイといっしょ.txt L85–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/004%20%E8%B5%B0%E3%82%8C%EF%BC%81%E4%BD%93%E8%82%B2%E7%A5%AD%EF%BC%81%EF%BD%9E%E5%AE%9F%E8%A1%8C%E5%A7%94%E5%93%A1%E3%81%AF%E5%A4%A7%E5%BF%99%E3%81%97%EF%BD%9E%20%28Mix_%E9%B3%B3%E3%81%88%E3%82%80%29/004-04%20%E3%82%BB%E3%83%B3%E3%83%91%E3%82%A4%E3%81%A8%E3%81%84%E3%81%A3%E3%81%97%E3%82%87.txt#L85)；[OC14_Miku_E7 · talk_event_124.txt L42–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_124.txt#L42)；[OC14_MEIKO_X3 · 104-06 あなた達のためのショー.txt L67–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L67)；[OC14_MEIKO_X4 · 104-06 あなた達のためのショー.txt L112–165](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/104%20%E3%81%82%E3%81%9F%E3%81%97%E3%81%9F%E3%81%A1%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%20%28WxS_%E9%B3%B3%E3%81%88%E3%82%80%29/104-06%20%E3%81%82%E3%81%AA%E3%81%9F%E9%81%94%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC.txt#L112)

**情感比较正文：** [OC14_Miku_E1 · 030-03 ちぐはぐな音色.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/030%20%E3%81%8D%E3%81%A3%E3%81%A8%E6%9C%80%E9%AB%98%E3%81%AEsummer%EF%BC%81%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/030-03%20%E3%81%A1%E3%81%90%E3%81%AF%E3%81%90%E3%81%AA%E9%9F%B3%E8%89%B2.txt#L19)；[OC14_Miku_E2 · 004-04 センパイといっしょ.txt L85–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/004%20%E8%B5%B0%E3%82%8C%EF%BC%81%E4%BD%93%E8%82%B2%E7%A5%AD%EF%BC%81%EF%BD%9E%E5%AE%9F%E8%A1%8C%E5%A7%94%E5%93%A1%E3%81%AF%E5%A4%A7%E5%BF%99%E3%81%97%EF%BD%9E%20%28Mix_%E9%B3%B3%E3%81%88%E3%82%80%29/004-04%20%E3%82%BB%E3%83%B3%E3%83%91%E3%82%A4%E3%81%A8%E3%81%84%E3%81%A3%E3%81%97%E3%82%87.txt#L85)；[OC14_Miku_E3 · 0476_鳳えむ_R4 おめめキラキラだね☆ (event_66).txt L11–15](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/0476_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%81%8A%E3%82%81%E3%82%81%E3%82%AD%E3%83%A9%E3%82%AD%E3%83%A9%E3%81%A0%E3%81%AD%E2%98%86%20%28event_66%29.txt#L11)；[OC14_Miku_E7 · talk_event_124.txt L42–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_124.txt#L42)；[OC14_Miku_E4 · 0261_鳳えむ_R4 バーベキュー奉行！？ (event_30).txt L124–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/0261_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%90%E3%83%BC%E3%83%99%E3%82%AD%E3%83%A5%E3%83%BC%E5%A5%89%E8%A1%8C%EF%BC%81%EF%BC%9F%20%28event_30%29.txt#L124)；[OC14_Miku_E5 · 0085_初音ミク (WxS)_R2 ワンダーランドのセカイ.txt L77–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0085_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E3%81%AE%E3%82%BB%E3%82%AB%E3%82%A4.txt#L77)；[OC14_Miku_E6 · 030-02 発表会で何しよう？.txt L9–13](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/030%20%E3%81%8D%E3%81%A3%E3%81%A8%E6%9C%80%E9%AB%98%E3%81%AEsummer%EF%BC%81%20%28Mix_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/030-02%20%E7%99%BA%E8%A1%A8%E4%BC%9A%E3%81%A7%E4%BD%95%E3%81%97%E3%82%88%E3%81%86%EF%BC%9F.txt#L9)；[OC14_Miku_X1 · 0479_初音ミク (WxS)_R2 ミクミク☆ガンナー！ (event_66).txt L87–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0479_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R2%20%E3%83%9F%E3%82%AF%E3%83%9F%E3%82%AF%E2%98%86%E3%82%AC%E3%83%B3%E3%83%8A%E3%83%BC%EF%BC%81%20%28event_66%29.txt#L87)

### OC14_Luka · 巡音流歌

**成长细分判断：** 训练方法实际尝试但本人没感觉变强，217等待非现实救援因果。

**情感细分判断：** 可靠姐姐的称赞含周年演出语境，具体节目制作成立，尚未更私人袒露或连续回报。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,1,1,1|2,2,2,2|
|细档|2,4,1.25,1,1|2.25,2.25,2,2.5|

原粗档指数成长/情感 40.58 / 50.00；细分未归一原指数 41.83 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC14_Luka_F1 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L98–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L98)；[OC14_Rin_X1 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L107–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L107)；[OC14_Luka_X5 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L130–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L130)；[OC14_Luka_X1 · 217-07 進む覚悟.txt L69–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L69)；[OC14_Luka_X2 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L48–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L48)；[OC14_Luka_X3 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L22–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L22)；[OC14_Luka_X4 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L107–132](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L107)

**情感比较正文：** [OC14_Luka_X1 · 217-07 進む覚悟.txt L69–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L69)；[OC14_Luka_X2 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L48–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L48)；[OC14_Luka_F1 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L98–112](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L98)；[OC14_Luka_X5 · 1280_鳳えむ_R4 ハピハピハッピーなおもてなし (event_185).txt L130–160](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1280_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E3%83%8F%E3%83%94%E3%83%8F%E3%83%94%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%81%8A%E3%82%82%E3%81%A6%E3%81%AA%E3%81%97%20%28event_185%29.txt#L130)；[OC14_Luka_X3 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L22–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L22)；[OC14_Rin_X2 · 0235_鏡音リン (WxS)_R3 スマイルナイトタイム！ (event_25).txt L126–143](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0235_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R3%20%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB%E3%83%8A%E3%82%A4%E3%83%88%E3%82%BF%E3%82%A4%E3%83%A0%EF%BC%81%20%28event_25%29.txt#L126)

## 草薙宁宁

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|巡音流歌|3|1|1|96.20|100.00|98.10|100.00|研究估计；来源有依据，仍需独立复评|
|MEIKO|1|2|2|100.00|84.21|92.11|93.89|研究估计；来源有依据，仍需独立复评|
|镜音铃|2|3|3|97.68|77.19|87.43|89.13|研究估计；来源有依据，仍需独立复评|
|KAITO|4|5|4|88.12|64.91|76.52|78.00|暂定：综合差距不足2分，子档微调可能换位|
|镜音连|5|4|5|84.69|66.67|75.68|77.14|研究估计；来源有依据，仍需独立复评|
|初音未来|6|6|6|64.89|63.16|64.02|65.26|该组末位；仍为研究估计|

### OC15_Luka · 巡音流歌

**成长细分判断：** 32分离未来及208休整被本人理解/实行，关键心理认识直接，路线仍由本人决定。

**情感细分判断：** 本人详细说无法想象独自道路、后期仍回顾无需独自烦恼，海景/毯子/寄语真实延续依靠。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,2|3,3,3,3|
|细档|3.5,7,2.5,2,2|3.5,3.5,3.5,3.75|

原粗档指数成长/情感 67.17 / 75.00；细分未归一原指数 75.92 / 89.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_Luka_G1 · 032-07 まだ知らない世界.txt L8–10、17–20、23–26、38–40、46–51、87–89、92–94、105–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/032%20%E3%83%9E%E3%83%BC%E3%83%A1%E3%82%A4%E3%83%89%E3%81%AB%E3%81%82%E3%81%93%E3%81%8C%E3%82%8C%E3%81%A6%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/032-07%20%E3%81%BE%E3%81%A0%E7%9F%A5%E3%82%89%E3%81%AA%E3%81%84%E4%B8%96%E7%95%8C.txt#L8)；[OC15_Luka_G2 · 032-08 今は、できることを.txt L7–16、30–33、35–56、58–62、69–71、81–83、87–89、93–95、98–100、105–107、124–126、129–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/032%20%E3%83%9E%E3%83%BC%E3%83%A1%E3%82%A4%E3%83%89%E3%81%AB%E3%81%82%E3%81%93%E3%81%8C%E3%82%8C%E3%81%A6%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/032-08%20%E4%BB%8A%E3%81%AF%E3%80%81%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92.txt#L7)；[OC15_Luka_X2 · 1413_草薙寧々_R3 苦しみを見つめて (event_208).txt L18–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1413_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R3%20%E8%8B%A6%E3%81%97%E3%81%BF%E3%82%92%E8%A6%8B%E3%81%A4%E3%82%81%E3%81%A6%20%28event_208%29.txt#L18)；[OC14_Luka_X2 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L48–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L48)；[OC14_Luka_X3 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L22–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L22)；[OC14_Luka_X1 · 217-07 進む覚悟.txt L69–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L69)；[OC14_Len_X1 · 1472_巡音ルカ (WxS)_R4 静かな祈り (event_217).txt L95–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1472_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28WxS%29_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E7%A5%88%E3%82%8A%20%28event_217%29.txt#L95)；[OC15_Luka_X1 · 1452_巡音ルカ (VBS)_R4 仲良くイエーイ！ (event_215).txt L124–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1452_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28VBS%29_R4%20%E4%BB%B2%E8%89%AF%E3%81%8F%E3%82%A4%E3%82%A8%E3%83%BC%E3%82%A4%EF%BC%81%20%28event_215%29.txt#L124)

**情感比较正文：** [OC15_Luka_G2 · 032-08 今は、できることを.txt L7–16、30–33、35–56、58–62、69–71、81–83、87–89、93–95、98–100、105–107、124–126、129–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/032%20%E3%83%9E%E3%83%BC%E3%83%A1%E3%82%A4%E3%83%89%E3%81%AB%E3%81%82%E3%81%93%E3%81%8C%E3%82%8C%E3%81%A6%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/032-08%20%E4%BB%8A%E3%81%AF%E3%80%81%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92.txt#L7)；[OC14_Luka_X2 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L48–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L48)；[OC14_Luka_X1 · 217-07 進む覚悟.txt L69–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L69)；[OC15_Luka_G1 · 032-07 まだ知らない世界.txt L8–10、17–20、23–26、38–40、46–51、87–89、92–94、105–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/032%20%E3%83%9E%E3%83%BC%E3%83%A1%E3%82%A4%E3%83%89%E3%81%AB%E3%81%82%E3%81%93%E3%81%8C%E3%82%8C%E3%81%A6%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/032-07%20%E3%81%BE%E3%81%A0%E7%9F%A5%E3%82%89%E3%81%AA%E3%81%84%E4%B8%96%E7%95%8C.txt#L8)；[OC14_Len_X1 · 1472_巡音ルカ (WxS)_R4 静かな祈り (event_217).txt L95–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1472_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28WxS%29_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E7%A5%88%E3%82%8A%20%28event_217%29.txt#L95)；[OC15_Luka_X1 · 1452_巡音ルカ (VBS)_R4 仲良くイエーイ！ (event_215).txt L124–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1452_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28VBS%29_R4%20%E4%BB%B2%E8%89%AF%E3%81%8F%E3%82%A4%E3%82%A8%E3%83%BC%E3%82%A4%EF%BC%81%20%28event_215%29.txt#L124)

### OC15_MEIKO · MEIKO

**成长细分判断：** 勇气、同学关系与1416自我诊断多线作用清楚，核心变化仍共同完成。

**情感细分判断：** 深层自我压力与多场专属演出/玩偶筹备相结合，持续个别回应比一般致谢充分。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,2,2|2,3,3,2|
|细档|3.5,9,2.5,2,2|2.25,3.5,3.5,2.75|

原粗档指数成长/情感 70.17 / 62.50；细分未归一原指数 78.92 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_MEIKO_G1 · 008-06 魔法をかけて.txt L1–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-06%20%E9%AD%94%E6%B3%95%E3%82%92%E3%81%8B%E3%81%91%E3%81%A6.txt#L1)；[OC15_MEIKO_G2 · 008-07 セカイの新団員！？.txt L18–27、36–43、55–63、66–68、71–74、77、79–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-07%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E5%9B%A3%E5%93%A1%EF%BC%81%EF%BC%9F.txt#L18)；[OC15_MEIKO_F1 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L155–195](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L155)；[OC15_MEIKO_X1 · 0450_草薙寧々_R4 遊びのお礼に (event_62).txt L53–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/0450_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E9%81%8A%E3%81%B3%E3%81%AE%E3%81%8A%E7%A4%BC%E3%81%AB%20%28event_62%29.txt#L53)；[OC15_MEIKO_X2 · 062-02 無人島サバイバル！.txt L101–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/062%20%E7%B5%B6%E4%BD%93%E7%B5%B6%E5%91%BD%EF%BC%81%EF%BC%9F%E3%82%A2%E3%82%A4%E3%83%A9%E3%83%B3%E3%83%89%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/062-02%20%E7%84%A1%E4%BA%BA%E5%B3%B6%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%EF%BC%81.txt#L101)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC15_Rin_X2 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L196–224](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L196)；[OC15_MEIKO_E8 · talk_event_218.txt L399–403](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_218.txt#L399)

**情感比较正文：** [OC15_MEIKO_E2 · 062-07 みんなで一緒に.txt L27–31](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/062%20%E7%B5%B6%E4%BD%93%E7%B5%B6%E5%91%BD%EF%BC%81%EF%BC%9F%E3%82%A2%E3%82%A4%E3%83%A9%E3%83%B3%E3%83%89%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/062-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E4%B8%80%E7%B7%92%E3%81%AB.txt#L27)；[OC15_MEIKO_E8 · talk_event_218.txt L399–403](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_218.txt#L399)；[OC15_MEIKO_F1 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L155–195](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L155)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)；[OC15_Rin_E5 · talk_event_167.txt L42–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_167.txt#L42)；[OC15_MEIKO_X1 · 0450_草薙寧々_R4 遊びのお礼に (event_62).txt L53–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/0450_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E9%81%8A%E3%81%B3%E3%81%AE%E3%81%8A%E7%A4%BC%E3%81%AB%20%28event_62%29.txt#L53)

### OC15_Rin · 镜音铃

**成长细分判断：** 1416针对丢过去自我作直接提示，185训练效果本人确认，多独立问题已核。

**情感细分判断：** 真实说怕陌生人及不喜欢过去自己、想变的负担，演出回应具体，个人自我信任较深。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,10,2,1,2|2,3,2,2|
|细档|3.5,10,2.5,1,2|2.25,3.5,2.5,2.75|

原粗档指数成长/情感 68.33 / 56.25；细分未归一原指数 77.08 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_Rin_G1 · 013-02 交差する出会い.txt L8–17](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/013%20%E9%9F%BF%E3%81%8F%E3%83%88%E3%83%AF%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/013-02%20%E4%BA%A4%E5%B7%AE%E3%81%99%E3%82%8B%E5%87%BA%E4%BC%9A%E3%81%84.txt#L8)；[OC15_Rin_G2 · 013-03 はじめまして！？わんだほい！.txt L9–15、18–21、24、44–52、110–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/013%20%E9%9F%BF%E3%81%8F%E3%83%88%E3%83%AF%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/013-03%20%E3%81%AF%E3%81%98%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6%EF%BC%81%EF%BC%9F%E3%82%8F%E3%82%93%E3%81%A0%E3%81%BB%E3%81%84%EF%BC%81.txt#L9)；[OC15_Rin_G3 · 013-03 はじめまして！？わんだほい！.txt L9–15、18–21、24、44–52、110–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/013%20%E9%9F%BF%E3%81%8F%E3%83%88%E3%83%AF%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/013-03%20%E3%81%AF%E3%81%98%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6%EF%BC%81%EF%BC%9F%E3%82%8F%E3%82%93%E3%81%A0%E3%81%BB%E3%81%84%EF%BC%81.txt#L9)；[OC15_Rin_F1 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L155–195](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L155)；[OC15_Rin_X1 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L226–236](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L226)；[OC15_Rin_X2 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L196–224](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L196)；[OC15_Rin_E8 · talk_event_185.txt L27–31](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_185.txt#L27)

**情感比较正文：** [OC15_Rin_G1 · 013-02 交差する出会い.txt L8–17](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/013%20%E9%9F%BF%E3%81%8F%E3%83%88%E3%83%AF%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/013-02%20%E4%BA%A4%E5%B7%AE%E3%81%99%E3%82%8B%E5%87%BA%E4%BC%9A%E3%81%84.txt#L8)；[OC15_Rin_G2 · 013-03 はじめまして！？わんだほい！.txt L9–15、18–21、24、44–52、110–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/013%20%E9%9F%BF%E3%81%8F%E3%83%88%E3%83%AF%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9%29/013-03%20%E3%81%AF%E3%81%98%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6%EF%BC%81%EF%BC%9F%E3%82%8F%E3%82%93%E3%81%A0%E3%81%BB%E3%81%84%EF%BC%81.txt#L9)；[OC15_Rin_E2 · talk_event_081.txt L28–32](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_081.txt#L28)；[OC15_Rin_E3 · talk_event_025.txt L167–171](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_025.txt#L167)；[OC15_Rin_F1 · 1416_草薙寧々_R4 あなたのような“わたし”に.txt L155–195](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/1416_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E2%80%9C%E3%82%8F%E3%81%9F%E3%81%97%E2%80%9D%E3%81%AB.txt#L155)；[OC15_Rin_E5 · talk_event_167.txt L42–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_167.txt#L42)

### OC15_KAITO · KAITO

**成长细分判断：** 同学理解有核心追问，但95应援也加重过劳，成果具名归因主要连/风祭，保留边界。

**情感细分判断：** 具体机器/同学问题愿讲，但合作应援感谢与群体节目投入较工作性，定位为具体顾问。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,1,2,2|2,2,2,2|
|细档|3.25,9,1.25,2,2|2.25,2.25,2.25,2.5|

原粗档指数成长/情感 65.17 / 50.00；细分未归一原指数 69.54 / 57.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_KAITO_G1 · 008-07 セカイの新団員！？.txt L40–43、45、51–53、55、60–64、67–75、81–83](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-07%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E5%9B%A3%E5%93%A1%EF%BC%81%EF%BC%9F.txt#L40)；[OC15_KAITO_G2 · 095-04 思いがけない応援.txt L32–34、40–46、63–65、77–83、85、93–98、111–113、115–120、125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/095%20%E3%82%AB%E3%83%8A%E3%83%AA%E3%82%A2%E3%81%AF%E7%AA%AE%E5%A2%83%E3%81%AB%E6%AD%8C%E3%81%86%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/095-04%20%E6%80%9D%E3%81%84%E3%81%8C%E3%81%91%E3%81%AA%E3%81%84%E5%BF%9C%E6%8F%B4.txt#L32)；[OC15_KAITO_G3 · 095-06 どんなことも力にして.txt L14、17–18、60–63、70–73、76–83、86–87、98–100、113–116、121–123](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/095%20%E3%82%AB%E3%83%8A%E3%83%AA%E3%82%A2%E3%81%AF%E7%AA%AE%E5%A2%83%E3%81%AB%E6%AD%8C%E3%81%86%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/095-06%20%E3%81%A9%E3%82%93%E3%81%AA%E3%81%93%E3%81%A8%E3%82%82%E5%8A%9B%E3%81%AB%E3%81%97%E3%81%A6.txt#L14)；[OC15_KAITO_F1 · 114-03 想いを知ったら.txt L125–140](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L125)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC15_KAITO_X2 · 114-06 後悔しないように.txt L11–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-06%20%E5%BE%8C%E6%82%94%E3%81%97%E3%81%AA%E3%81%84%E3%82%88%E3%81%86%E3%81%AB.txt#L11)；[OC15_KAITO_X3 · talk_grade1.txt L10310–10320](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L10310)；[OC15_KAITO_E2 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L18–22](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L18)；[OC15_KAITO_E3 · talk_grade1.txt L7623–7627](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L7623)；[OC15_MEIKO_X2 · 062-02 無人島サバイバル！.txt L101–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/062%20%E7%B5%B6%E4%BD%93%E7%B5%B6%E5%91%BD%EF%BC%81%EF%BC%9F%E3%82%A2%E3%82%A4%E3%83%A9%E3%83%B3%E3%83%89%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/062-02%20%E7%84%A1%E4%BA%BA%E5%B3%B6%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%EF%BC%81.txt#L101)

**情感比较正文：** [OC15_KAITO_E1 · vswonder_01_04 空飛ぶショーステージ！？.txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/1%20%E3%83%90%E3%83%BC%E3%83%81%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%B7%E3%83%B3%E3%82%AC%E3%83%BC/vswonder_01_04%20%E7%A9%BA%E9%A3%9B%E3%81%B6%E3%82%B7%E3%83%A7%E3%83%BC%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%EF%BC%81%EF%BC%9F.txt#L10)；[OC15_KAITO_E2 · 0407_KAITO (WxS)_R4 大丈夫だよ、みんな (event_54).txt L18–22](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/0407_KAITO%20%28WxS%29_R4%20%E5%A4%A7%E4%B8%88%E5%A4%AB%E3%81%A0%E3%82%88%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%20%28event_54%29.txt#L18)；[OC15_KAITO_E3 · talk_grade1.txt L7623–7627](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L7623)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC15_KAITO_X3 · talk_grade1.txt L10310–10320](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L10310)；[OC15_Rin_E5 · talk_event_167.txt L42–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_167.txt#L42)

### OC15_Len · 镜音连

**成长细分判断：** 114直接指出性格不同不等于有墙并改善交谈，针对长期社交困惑而非完全治愈。

**情感细分判断：** 本人说明同学和导演困难并接受共玩，寄语实际递交；关系比普通协作更个别，但未深层创伤。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,2,2,2|
|细档|3.5,4,2.25,1,2|2.25,2.5,2.25,2.5|

原粗档指数成长/情感 59.33 / 50.00；细分未归一原指数 66.83 / 59.38。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_Len_F1 · 114-03 想いを知ったら.txt L125–140](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L125)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC15_KAITO_X2 · 114-06 後悔しないように.txt L11–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-06%20%E5%BE%8C%E6%82%94%E3%81%97%E3%81%AA%E3%81%84%E3%82%88%E3%81%86%E3%81%AB.txt#L11)；[OC15_Len_E1 · talk_event_003.txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_003.txt#L68)；[OC15_Len_E2 · 217-07 進む覚悟.txt L117–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L117)

**情感比较正文：** [OC15_Len_E1 · talk_event_003.txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_003.txt#L68)；[OC15_Len_E2 · 217-07 進む覚悟.txt L117–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/217%20Drive%20to%20Dream%EF%BC%81%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/217-07%20%E9%80%B2%E3%82%80%E8%A6%9A%E6%82%9F.txt#L117)；[OC15_Len_E3 · 114-06 後悔しないように.txt L22–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-06%20%E5%BE%8C%E6%82%94%E3%81%97%E3%81%AA%E3%81%84%E3%82%88%E3%81%86%E3%81%AB.txt#L22)；[OC15_KAITO_X1 · 114-03 想いを知ったら.txt L89–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-03%20%E6%83%B3%E3%81%84%E3%82%92%E7%9F%A5%E3%81%A3%E3%81%9F%E3%82%89.txt#L89)；[OC15_Luka_X1 · 1452_巡音ルカ (VBS)_R4 仲良くイエーイ！ (event_215).txt L124–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1452_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28VBS%29_R4%20%E4%BB%B2%E8%89%AF%E3%81%8F%E3%82%A4%E3%82%A8%E3%83%BC%E3%82%A4%EF%BC%81%20%28event_215%29.txt#L124)；[OC15_KAITO_X2 · 114-06 後悔しないように.txt L11–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/114%20%E6%9C%80%E9%AB%98%E3%81%AE%E3%82%AF%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%EF%BC%81%20%28Mix_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/114-06%20%E5%BE%8C%E6%82%94%E3%81%97%E3%81%AA%E3%81%84%E3%82%88%E3%81%86%E3%81%AB.txt#L11)

### OC15_Miku · 初音未来

**成长细分判断：** 0145理解共同笑容后决定再来，008恢复先由本人完成，不夸大成长。

**情感细分判断：** 愿再玩、具体依赖困惑与带书/选曲真实，定位仍共同娱乐支持伙伴。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|2,2,2,2|
|细档|2.25,4,2.25,1,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 46.83 / 50.00；细分未归一原指数 51.21 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC15_Miku_G1 · 008-07 セカイの新団員！？.txt L14–19、22–24、39–45、51、71–73、81–83、87–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-07%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E5%9B%A3%E5%93%A1%EF%BC%81%EF%BC%9F.txt#L14)；[OC15_Miku_F1 · 008-07 セカイの新団員！？.txt L8–54](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-07%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E5%9B%A3%E5%93%A1%EF%BC%81%EF%BC%9F.txt#L8)；[OC15_Miku_X3 · 0145_初音ミク (WxS)_R4 ワンダー☆クリスマス！ (event_8).txt L112–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0145_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R4%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E2%98%86%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9%EF%BC%81%20%28event_8%29.txt#L112)；[OC15_Miku_X4 · talk_grade2.txt L1514–1525](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1514)；[OC15_Miku_X2 · 0348_草薙寧々_R4 きらびやかな夢の舞台.txt L151–200](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/15%20WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85/0348_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85_R4%20%E3%81%8D%E3%82%89%E3%81%B3%E3%82%84%E3%81%8B%E3%81%AA%E5%A4%A2%E3%81%AE%E8%88%9E%E5%8F%B0.txt#L151)

**情感比较正文：** [OC15_Miku_E1 · talk_event_149.txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_149.txt#L82)；[OC15_Miku_E2 · vswonder_01_04 空飛ぶショーステージ！？.txt L10–14](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/1%20%E3%83%90%E3%83%BC%E3%83%81%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%B7%E3%83%B3%E3%82%AC%E3%83%BC/vswonder_01_04%20%E7%A9%BA%E9%A3%9B%E3%81%B6%E3%82%B7%E3%83%A7%E3%83%BC%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%EF%BC%81%EF%BC%9F.txt#L10)；[OC15_Miku_E3 · 008-07 セカイの新団員！？.txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/008%20%E8%81%96%E3%81%AA%E3%82%8B%E5%A4%9C%E3%81%AB%E3%80%81%E3%81%93%E3%81%AE%E6%AD%8C%E5%A3%B0%E3%82%92%20%28WxS_%E8%8D%89%E8%96%99%E5%AF%A7%E3%80%85%29/008-07%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%96%B0%E5%9B%A3%E5%93%A1%EF%BC%81%EF%BC%9F.txt#L39)；[OC15_Miku_X3 · 0145_初音ミク (WxS)_R4 ワンダー☆クリスマス！ (event_8).txt L112–137](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0145_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28WxS%29_R4%20%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E2%98%86%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9%EF%BC%81%20%28event_8%29.txt#L112)；[OC15_Miku_E4 · 003-05 一番いい演出を.txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/003%20%E5%85%A8%E5%8A%9B%EF%BC%81%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%8F%E3%83%AD%E3%82%A6%E3%82%A3%E3%83%B3%EF%BC%81%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/003-05%20%E4%B8%80%E7%95%AA%E3%81%84%E3%81%84%E6%BC%94%E5%87%BA%E3%82%92.txt#L80)；[OC15_Miku_X4 · talk_grade2.txt L1514–1525](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1514)；[OC13_Miku_E8 · 1193_神代類_RB Happy Birthday！！2025.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1193_%E7%A5%9E%E4%BB%A3%E9%A1%9E_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812025.txt#L19)

## 神代类

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|KAITO|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|3|2|99.57|92.98|96.28|96.28|研究估计；来源有依据，仍需独立复评|
|初音未来|3|4|3|92.44|89.47|90.96|90.96|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|2|4|72.03|98.25|85.14|85.14|研究估计；来源有依据，仍需独立复评|
|镜音铃|4|5|5|74.46|80.70|77.58|77.58|研究估计；来源有依据，仍需独立复评|
|镜音连|5|6|6|73.81|73.68|73.75|73.75|该组末位；仍为研究估计|

### OC16_KAITO · KAITO

**成长细分判断：** 3辨认归属恐惧且本人行动恢复，211机制帮助新办法，核心自我与归属的个人渠道持续。

**情感细分判断：** 童年远拒、孤独及失归属真实交托，日记记录与后续直接求观点，将关系连接核心过去与当前归属。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,3|3,3,3,3|
|细档|3.5,7,2.5,2,3|3.5,3.5,3.5,3.75|

原粗档指数成长/情感 68.42 / 75.00；细分未归一原指数 77.17 / 89.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_KAITO_G1 · 003-05 一番いい演出を.txt L12–14、20–22、25–27、50–52、82–85、89–90、96–98、101–103、106–108、113–117](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/003%20%E5%85%A8%E5%8A%9B%EF%BC%81%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%8F%E3%83%AD%E3%82%A6%E3%82%A3%E3%83%B3%EF%BC%81%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/003-05%20%E4%B8%80%E7%95%AA%E3%81%84%E3%81%84%E6%BC%94%E5%87%BA%E3%82%92.txt#L12)；[OC16_KAITO_G2 · 003-06 役者と演出家.txt L8、10–15、21–25、27、33–37、47–49、51–53、62–70、90–95、97–100、103–107、110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/003%20%E5%85%A8%E5%8A%9B%EF%BC%81%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%8F%E3%83%AD%E3%82%A6%E3%82%A3%E3%83%B3%EF%BC%81%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/003-06%20%E5%BD%B9%E8%80%85%E3%81%A8%E6%BC%94%E5%87%BA%E5%AE%B6.txt#L8)；[OC16_KAITO_G3 · 003-07 僕達の全力で.txt L1–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/003%20%E5%85%A8%E5%8A%9B%EF%BC%81%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%8F%E3%83%AD%E3%82%A6%E3%82%A3%E3%83%B3%EF%BC%81%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/003-07%20%E5%83%95%E9%81%94%E3%81%AE%E5%85%A8%E5%8A%9B%E3%81%A7.txt#L1)；[OC16_KAITO_E1 · 007-05 お揃いのシャツ.txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/007%20KAMIKOU%20FESTIVAL%EF%BC%81%20%28Mix_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/007-05%20%E3%81%8A%E6%8F%83%E3%81%84%E3%81%AE%E3%82%B7%E3%83%A3%E3%83%84.txt#L68)；[OC16_KAITO_X1 · 1431_神代類_R4 心の濁り (event_211).txt L26–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1431_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%BF%83%E3%81%AE%E6%BF%81%E3%82%8A%20%28event_211%29.txt#L26)；[OC16_KAITO_X2 · 211-04 虚飾から本心を (神代類).txt L119–172](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/211%20%E5%90%9B%E3%81%AE%E9%9A%A3%E3%80%81%E5%90%9B%E3%81%A8%E8%A6%8B%E3%82%8B%E6%98%8E%E6%97%A5%20%28Mix_WL%29/211-04%20%E8%99%9A%E9%A3%BE%E3%81%8B%E3%82%89%E6%9C%AC%E5%BF%83%E3%82%92%20%28%E7%A5%9E%E4%BB%A3%E9%A1%9E%29.txt#L119)；[OC16_KAITO_X3 · 211-04 虚飾から本心を (神代類).txt L190–225](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/211%20%E5%90%9B%E3%81%AE%E9%9A%A3%E3%80%81%E5%90%9B%E3%81%A8%E8%A6%8B%E3%82%8B%E6%98%8E%E6%97%A5%20%28Mix_WL%29/211-04%20%E8%99%9A%E9%A3%BE%E3%81%8B%E3%82%89%E6%9C%AC%E5%BF%83%E3%82%92%20%28%E7%A5%9E%E4%BB%A3%E9%A1%9E%29.txt#L190)；[OC16_KAITO_E2 · 0428_神代類_R4 黄昏の輝き (event_58).txt L50–54](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0428_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E8%BC%9D%E3%81%8D%20%28event_58%29.txt#L50)；[OC13_KAITO_X4 · 1454_KAITO (WxS)_R4 はやる想いをスプーンに乗せて (event_215).txt L103–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1454_KAITO%20%28WxS%29_R4%20%E3%81%AF%E3%82%84%E3%82%8B%E6%83%B3%E3%81%84%E3%82%92%E3%82%B9%E3%83%97%E3%83%BC%E3%83%B3%E3%81%AB%E4%B9%97%E3%81%9B%E3%81%A6%20%28event_215%29.txt#L103)

**情感比较正文：** [OC16_KAITO_E1 · 007-05 お揃いのシャツ.txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/007%20KAMIKOU%20FESTIVAL%EF%BC%81%20%28Mix_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/007-05%20%E3%81%8A%E6%8F%83%E3%81%84%E3%81%AE%E3%82%B7%E3%83%A3%E3%83%84.txt#L68)；[OC16_KAITO_E2 · 0428_神代類_R4 黄昏の輝き (event_58).txt L50–54](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0428_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E9%BB%84%E6%98%8F%E3%81%AE%E8%BC%9D%E3%81%8D%20%28event_58%29.txt#L50)；[OC16_KAITO_E3 · 1431_神代類_R4 心の濁り (event_211).txt L51–55](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1431_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%BF%83%E3%81%AE%E6%BF%81%E3%82%8A%20%28event_211%29.txt#L51)；[OC16_KAITO_G2 · 003-06 役者と演出家.txt L8、10–15、21–25、27、33–37、47–49、51–53、62–70、90–95、97–100、103–107、110](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/003%20%E5%85%A8%E5%8A%9B%EF%BC%81%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%8F%E3%83%AD%E3%82%A6%E3%82%A3%E3%83%B3%EF%BC%81%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/003-06%20%E5%BD%B9%E8%80%85%E3%81%A8%E6%BC%94%E5%87%BA%E5%AE%B6.txt#L8)；[OC16_KAITO_X2 · 211-04 虚飾から本心を (神代類).txt L119–172](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/211%20%E5%90%9B%E3%81%AE%E9%9A%A3%E3%80%81%E5%90%9B%E3%81%A8%E8%A6%8B%E3%82%8B%E6%98%8E%E6%97%A5%20%28Mix_WL%29/211-04%20%E8%99%9A%E9%A3%BE%E3%81%8B%E3%82%89%E6%9C%AC%E5%BF%83%E3%82%92%20%28%E7%A5%9E%E4%BB%A3%E9%A1%9E%29.txt#L119)；[OC16_KAITO_X3 · 211-04 虚飾から本心を (神代類).txt L190–225](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/211%20%E5%90%9B%E3%81%AE%E9%9A%A3%E3%80%81%E5%90%9B%E3%81%A8%E8%A6%8B%E3%82%8B%E6%98%8E%E6%97%A5%20%28Mix_WL%29/211-04%20%E8%99%9A%E9%A3%BE%E3%81%8B%E3%82%89%E6%9C%AC%E5%BF%83%E3%82%92%20%28%E7%A5%9E%E4%BB%A3%E9%A1%9E%29.txt#L190)；[OC16_KAITO_E4 · 1121_KAITO_RB Happy Anniversary！！2025.txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1121_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L35)；[OC13_KAITO_X4 · 1454_KAITO (WxS)_R4 はやる想いをスプーンに乗せて (event_215).txt L103–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1454_KAITO%20%28WxS%29_R4%20%E3%81%AF%E3%82%84%E3%82%8B%E6%83%B3%E3%81%84%E3%82%92%E3%82%B9%E3%83%97%E3%83%BC%E3%83%B3%E3%81%AB%E4%B9%97%E3%81%9B%E3%81%A6%20%28event_215%29.txt#L103)

### OC16_Luka · 巡音流歌

**成长细分判断：** 58信任、82情绪承接、172实际请教形成多问题核心支持，本人求助习惯变化明确。

**情感细分判断：** 本人说难控制情绪与怕被拒，回访确认可以自然求助，显式持续依靠使情感意义较Miku更强。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,2|3,3,2,3|
|细档|3.5,9,2.75,1,2|3.5,3.5,2.5,3.75|

原粗档指数成长/情感 66.83 / 68.75；细分未归一原指数 76.83 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_Luka_X1 · 058-04 引っかかり.txt L111–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/058%20%E7%99%BD%E7%86%B1%EF%BC%81%E7%A5%9E%E9%AB%98%E5%BF%9C%E6%8F%B4%E5%9B%A3%EF%BC%81%20%28Mix_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/058-04%20%E5%BC%95%E3%81%A3%E3%81%8B%E3%81%8B%E3%82%8A.txt#L111)；[OC16_Luka_F1 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L55–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L55)；[OC16_Luka_X3 · 172-05 悪夢.txt L97–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/172%20Deeper%20and%20deeper%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/172-05%20%E6%82%AA%E5%A4%A2.txt#L97)；[OC16_Luka_X2 · 172-06 自分自身.txt L97–122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/172%20Deeper%20and%20deeper%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/172-06%20%E8%87%AA%E5%88%86%E8%87%AA%E8%BA%AB.txt#L97)；[OC16_Luka_E3 · 1196_神代類_R4 憧れまでの距離 (event_172).txt L97–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1196_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%86%A7%E3%82%8C%E3%81%BE%E3%81%A7%E3%81%AE%E8%B7%9D%E9%9B%A2%20%28event_172%29.txt#L97)；[OC14_Luka_X2 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L48–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L48)；[OC14_Luka_X3 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L22–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L22)

**情感比较正文：** [OC16_Luka_F1 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L55–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L55)；[OC16_Luka_E3 · 1196_神代類_R4 憧れまでの距離 (event_172).txt L97–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1196_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%86%A7%E3%82%8C%E3%81%BE%E3%81%A7%E3%81%AE%E8%B7%9D%E9%9B%A2%20%28event_172%29.txt#L97)；[OC16_Luka_X1 · 058-04 引っかかり.txt L111–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/058%20%E7%99%BD%E7%86%B1%EF%BC%81%E7%A5%9E%E9%AB%98%E5%BF%9C%E6%8F%B4%E5%9B%A3%EF%BC%81%20%28Mix_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/058-04%20%E5%BC%95%E3%81%A3%E3%81%8B%E3%81%8B%E3%82%8A.txt#L111)；[OC16_Luka_X3 · 172-05 悪夢.txt L97–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/172%20Deeper%20and%20deeper%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/172-05%20%E6%82%AA%E5%A4%A2.txt#L97)；[OC14_Luka_X3 · 1326_巡音ルカ_RB Happy Anniversary！！2026.txt L22–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1326_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L22)

### OC16_Miku · 初音未来

**成长细分判断：** 74触及追梦与伙伴的核心选择，1003照片诊断具体，但不独占完整自我解释。

**情感细分判断：** 珍惜其认真面对自己并真实托付选择，装置/教角色持续回应；显式长期依靠定位暂不如Luka。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|3,3,3,2|
|细档|3.5,7,2.25,1,2|3.5,3.5,3.25,2.5|

原粗档指数成长/情感 63.83 / 68.75；细分未归一原指数 71.33 / 79.69。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_Miku_G1 · 074-06 どちらも大事な.txt L43–45、65–68、113–115、127–131、133–144、148–155、166–167、169–183、185–189、191–202、208–210、221–223](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/074%20%E3%82%AB%E3%83%BC%E3%83%86%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%AB%E3%81%AB%E6%83%9C%E5%88%A5%E3%82%92%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/074-06%20%E3%81%A9%E3%81%A1%E3%82%89%E3%82%82%E5%A4%A7%E4%BA%8B%E3%81%AA.txt#L43)；[OC16_Miku_X2 · 1003_神代類_R4 宝物を見つめて.txt L136–199](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1003_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%9D%E7%89%A9%E3%82%92%E8%A6%8B%E3%81%A4%E3%82%81%E3%81%A6.txt#L136)；[OC16_Rin_F1 · 0514_神代類_R4 投げかける言葉は (event_72).txt L109–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0514_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%8A%95%E3%81%92%E3%81%8B%E3%81%91%E3%82%8B%E8%A8%80%E8%91%89%E3%81%AF%20%28event_72%29.txt#L109)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)

**情感比较正文：** [OC16_Miku_G1 · 074-06 どちらも大事な.txt L43–45、65–68、113–115、127–131、133–144、148–155、166–167、169–183、185–189、191–202、208–210、221–223](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/074%20%E3%82%AB%E3%83%BC%E3%83%86%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%AB%E3%81%AB%E6%83%9C%E5%88%A5%E3%82%92%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/074-06%20%E3%81%A9%E3%81%A1%E3%82%89%E3%82%82%E5%A4%A7%E4%BA%8B%E3%81%AA.txt#L43)；[OC16_Miku_E1 · 0455_神代類_RB Happy Birthday！！.txt L19–23](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0455_%E7%A5%9E%E4%BB%A3%E9%A1%9E_RB%20Happy%20Birthday%EF%BC%81%EF%BC%81.txt#L19)；[OC16_Miku_X1 · 0986_初音ミク_RB Happy Anniversary！！2024.txt L51–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0986_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L51)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)；[OC16_Miku_E2 · 0412_神代類_R4 その心意気を買って (event_55).txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0412_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E3%81%9D%E3%81%AE%E5%BF%83%E6%84%8F%E6%B0%97%E3%82%92%E8%B2%B7%E3%81%A3%E3%81%A6%20%28event_55%29.txt#L39)

### OC16_MEIKO · MEIKO

**成长细分判断：** 82共同承诺使实际求助/获得妙案，K2结果直接；不能把58主导诊断移给她K3。

**情感细分判断：** 真实听私情负担并获回访，装置/周年持续双向回应；个人依靠很明确但童年核心归属更多向KAITO说。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,2|3,3,3,3|
|细档|2.5,4,2.5,1,2|3.5,3.5,3.5,3.5|

原粗档指数成长/情感 46.83 / 75.00；细分未归一原指数 55.58 / 87.50。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_MEIKO_F1 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L55–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L55)；[OC16_MEIKO_E2 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L148–152](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L148)；[OC16_Len_E2 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L147–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L147)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)；[OC16_MEIKO_X2 · 1363_神代類_R4 思い描いたその画が (event_200).txt L83–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1363_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%80%9D%E3%81%84%E6%8F%8F%E3%81%84%E3%81%9F%E3%81%9D%E3%81%AE%E7%94%BB%E3%81%8C%20%28event_200%29.txt#L83)；[OC16_MEIKO_X3 · 0927_鳳えむ_R4 天下を笑う者 (event_131).txt L82–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/0927_%E9%B3%B3%E3%81%88%E3%82%80_R4%20%E5%A4%A9%E4%B8%8B%E3%82%92%E7%AC%91%E3%81%86%E8%80%85%20%28event_131%29.txt#L82)；[OC16_MEIKO_E6 · talk_event_200.txt L39–43](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_200.txt#L39)

**情感比较正文：** [OC16_MEIKO_F1 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L55–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L55)；[OC16_MEIKO_E3 · 200-02 ドラマに出るなら.txt L31–35](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/200%20%E6%AE%8B%E7%85%A7%E3%81%AEInside%20Direction%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/200-02%20%E3%83%89%E3%83%A9%E3%83%9E%E3%81%AB%E5%87%BA%E3%82%8B%E3%81%AA%E3%82%89.txt#L31)；[OC16_MEIKO_E5 · 1363_神代類_R4 思い描いたその画が (event_200).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1363_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%80%9D%E3%81%84%E6%8F%8F%E3%81%84%E3%81%9F%E3%81%9D%E3%81%AE%E7%94%BB%E3%81%8C%20%28event_200%29.txt#L93)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)；[OC13_MEIKO_X2 · 1027_MEIKO_RB Happy Anniversary！！2024.txt L50–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1027_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812024.txt#L50)；[OC16_MEIKO_X2 · 1363_神代類_R4 思い描いたその画が (event_200).txt L83–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1363_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%80%9D%E3%81%84%E6%8F%8F%E3%81%84%E3%81%9F%E3%81%9D%E3%81%AE%E7%94%BB%E3%81%8C%20%28event_200%29.txt#L83)；[OC16_Len_E2 · 0572_神代類_R4 負けるわけにはいかないね (event_82).txt L147–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0572_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E8%B2%A0%E3%81%91%E3%82%8B%E3%82%8F%E3%81%91%E3%81%AB%E3%81%AF%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E3%81%AD%20%28event_82%29.txt#L147)

### OC16_Rin · 镜音铃

**成长细分判断：** 58真实推动重看不敢说原因，后续关键信任比喻来自Luka，个人归因仍共谢。

**情感细分判断：** 童年被拒/同伴沟通真实听见，装置与周年回应持续，但关系定位目前是具体合作伙伴。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|2,3,3,2|
|细档|3.25,4,1,1,2|2.25,3.25,3.5,2.5|

原粗档指数成长/情感 54.33 / 62.50；细分未归一原指数 57.46 / 71.88。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_Rin_F1 · 0514_神代類_R4 投げかける言葉は (event_72).txt L109–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0514_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E6%8A%95%E3%81%92%E3%81%8B%E3%81%91%E3%82%8B%E8%A8%80%E8%91%89%E3%81%AF%20%28event_72%29.txt#L109)；[OC16_Rin_X1 · 038-05 越えられなかった垣根.txt L110–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/038%20Revival%20my%20dream%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/038-05%20%E8%B6%8A%E3%81%88%E3%82%89%E3%82%8C%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E5%9E%A3%E6%A0%B9.txt#L110)；[OC16_Rin_X2 · 058-04 引っかかり.txt L100–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/058%20%E7%99%BD%E7%86%B1%EF%BC%81%E7%A5%9E%E9%AB%98%E5%BF%9C%E6%8F%B4%E5%9B%A3%EF%BC%81%20%28Mix_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/058-04%20%E5%BC%95%E3%81%A3%E3%81%8B%E3%81%8B%E3%82%8A.txt#L100)；[OC16_Luka_X1 · 058-04 引っかかり.txt L111–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/058%20%E7%99%BD%E7%86%B1%EF%BC%81%E7%A5%9E%E9%AB%98%E5%BF%9C%E6%8F%B4%E5%9B%A3%EF%BC%81%20%28Mix_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/058-04%20%E5%BC%95%E3%81%A3%E3%81%8B%E3%81%8B%E3%82%8A.txt#L111)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)；[OC16_Rin_E3 · 038-05 越えられなかった垣根.txt L155–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/038%20Revival%20my%20dream%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/038-05%20%E8%B6%8A%E3%81%88%E3%82%89%E3%82%8C%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E5%9E%A3%E6%A0%B9.txt#L155)

**情感比较正文：** [OC16_Rin_E1 · 0305_鏡音リン (WxS)_R2 インテリシティガール (event_38).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0305_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%B3%E3%83%86%E3%83%AA%E3%82%B7%E3%83%86%E3%82%A3%E3%82%AC%E3%83%BC%E3%83%AB%20%28event_38%29.txt#L93)；[OC16_Rin_E2 · 0601_神代類_R4 唐突な試練 (event_87).txt L121–125](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/0601_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%94%90%E7%AA%81%E3%81%AA%E8%A9%A6%E7%B7%B4%20%28event_87%29.txt#L121)；[OC16_Rin_E3 · 038-05 越えられなかった垣根.txt L155–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/038%20Revival%20my%20dream%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/038-05%20%E8%B6%8A%E3%81%88%E3%82%89%E3%82%8C%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E5%9E%A3%E6%A0%B9.txt#L155)；[OC16_Rin_X1 · 038-05 越えられなかった垣根.txt L110–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/038%20Revival%20my%20dream%20%28WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/038-05%20%E8%B6%8A%E3%81%88%E3%82%89%E3%82%8C%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E5%9E%A3%E6%A0%B9.txt#L110)；[OC16_Rin_X2 · 058-04 引っかかり.txt L100–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/058%20%E7%99%BD%E7%86%B1%EF%BC%81%E7%A5%9E%E9%AB%98%E5%BF%9C%E6%8F%B4%E5%9B%A3%EF%BC%81%20%28Mix_%E7%A5%9E%E4%BB%A3%E9%A1%9E%29/058-04%20%E5%BC%95%E3%81%A3%E3%81%8B%E3%81%8B%E3%82%8A.txt#L100)；[OC16_Rin_E4 · 0346_鏡音リン_RB Happy Anniversary！！.txt L52–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0346_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L52)；[OC16_Rin_E5 · talk_event_119.txt L78–82](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_119.txt#L78)；[OC16_MEIKO_X1 · 1340_神代類_R4 宇宙でドタバタシューティング！ (event_196).txt L90–105](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1340_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%87%E5%AE%99%E3%81%A7%E3%83%89%E3%82%BF%E3%83%90%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%81%20%28event_196%29.txt#L90)

### OC16_Len · 镜音连

**成长细分判断：** 24结尾点子被采用并本人具名确认，219合作执行不新增独立核心教学线。

**情感细分判断：** 婚礼邀约、机器人/表演教学、周年回应跨情境，本人脆弱目前没向连同样深讲。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,7,2,1,2|2,2,3,2|
|细档|2.25,7,2.5,1,2|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 51.33 / 56.25；细分未归一原指数 56.96 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC16_Len_X1 · 024-06 信頼と理解.txt L103–114](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/024%20%E7%B4%94%E7%99%BD%E3%81%AE%E8%B2%B4%E6%96%B9%E3%81%B8%E3%80%81%E8%AA%93%E3%81%84%E3%81%AE%E6%AD%8C%E3%82%92%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/024-06%20%E4%BF%A1%E9%A0%BC%E3%81%A8%E7%90%86%E8%A7%A3.txt#L103)；[OC16_Len_F1 · 1479_神代類_R4 笑顔を生み出す仕掛け (event_219).txt L124–155](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1479_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E7%AC%91%E9%A1%94%E3%82%92%E7%94%9F%E3%81%BF%E5%87%BA%E3%81%99%E4%BB%95%E6%8E%9B%E3%81%91%20%28event_219%29.txt#L124)；[OC16_Len_E1 · 1054_鳳えむ_R2 わくわく♪お菓子の町づくり！ (event_152).txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1054_%E9%B3%B3%E3%81%88%E3%82%80_R2%20%E3%82%8F%E3%81%8F%E3%82%8F%E3%81%8F%E2%99%AA%E3%81%8A%E8%8F%93%E5%AD%90%E3%81%AE%E7%94%BA%E3%81%A5%E3%81%8F%E3%82%8A%EF%BC%81%20%28event_152%29.txt#L109)；[OC16_Len_E4 · 0229_鏡音レン (WxS)_R4 キラキラ好奇心☆ (event_24).txt L124–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0229_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%AD%E3%83%A9%E3%82%AD%E3%83%A9%E5%A5%BD%E5%A5%87%E5%BF%83%E2%98%86%20%28event_24%29.txt#L124)；[OC16_Len_E5 · 0305_鏡音リン (WxS)_R2 インテリシティガール (event_38).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0305_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%B3%E3%83%86%E3%83%AA%E3%82%B7%E3%83%86%E3%82%A3%E3%82%AC%E3%83%BC%E3%83%AB%20%28event_38%29.txt#L93)；[OC16_Miku_X2 · 1003_神代類_R4 宝物を見つめて.txt L136–199](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1003_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E5%AE%9D%E7%89%A9%E3%82%92%E8%A6%8B%E3%81%A4%E3%82%81%E3%81%A6.txt#L136)

**情感比较正文：** [OC16_Len_E5 · 0305_鏡音リン (WxS)_R2 インテリシティガール (event_38).txt L93–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0305_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28WxS%29_R2%20%E3%82%A4%E3%83%B3%E3%83%86%E3%83%AA%E3%82%B7%E3%83%86%E3%82%A3%E3%82%AC%E3%83%BC%E3%83%AB%20%28event_38%29.txt#L93)；[OC16_Len_E6 · 024-06 信頼と理解.txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/024%20%E7%B4%94%E7%99%BD%E3%81%AE%E8%B2%B4%E6%96%B9%E3%81%B8%E3%80%81%E8%AA%93%E3%81%84%E3%81%AE%E6%AD%8C%E3%82%92%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/024-06%20%E4%BF%A1%E9%A0%BC%E3%81%A8%E7%90%86%E8%A7%A3.txt#L109)；[OC16_Len_F1 · 1479_神代類_R4 笑顔を生み出す仕掛け (event_219).txt L124–155](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1479_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E7%AC%91%E9%A1%94%E3%82%92%E7%94%9F%E3%81%BF%E5%87%BA%E3%81%99%E4%BB%95%E6%8E%9B%E3%81%91%20%28event_219%29.txt#L124)；[OC16_Len_E1 · 1054_鳳えむ_R2 わくわく♪お菓子の町づくり！ (event_152).txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/14%20WxS_%E9%B3%B3%E3%81%88%E3%82%80/1054_%E9%B3%B3%E3%81%88%E3%82%80_R2%20%E3%82%8F%E3%81%8F%E3%82%8F%E3%81%8F%E2%99%AA%E3%81%8A%E8%8F%93%E5%AD%90%E3%81%AE%E7%94%BA%E3%81%A5%E3%81%8F%E3%82%8A%EF%BC%81%20%28event_152%29.txt#L109)；[OC16_Len_E10 · talk_event_099.txt L103–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_099.txt#L103)；[OC16_Len_E9 · 024-01 突然の代役.txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/024%20%E7%B4%94%E7%99%BD%E3%81%AE%E8%B2%B4%E6%96%B9%E3%81%B8%E3%80%81%E8%AA%93%E3%81%84%E3%81%AE%E6%AD%8C%E3%82%92%EF%BC%81%20%28Mix_%E9%9D%92%E6%9F%B3%E5%86%AC%E5%BC%A5%29/024-01%20%E7%AA%81%E7%84%B6%E3%81%AE%E4%BB%A3%E5%BD%B9.txt#L131)；[OC16_Len_E7 · 0346_鏡音リン_RB Happy Anniversary！！.txt L52–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0346_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%81.txt#L52)；[OC16_Len_E3 · talk_event_082.txt L67–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_082.txt#L67)；[OC16_Len_E4 · 0229_鏡音レン (WxS)_R4 キラキラ好奇心☆ (event_24).txt L124–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0229_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28WxS%29_R4%20%E3%82%AD%E3%83%A9%E3%82%AD%E3%83%A9%E5%A5%BD%E5%A5%87%E5%BF%83%E2%98%86%20%28event_24%29.txt#L124)

## 宵崎奏

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|镜音铃|2|2|2|95.61|91.23|93.42|93.42|研究估计；来源有依据，仍需独立复评|
|巡音流歌|3|3|3|93.96|84.21|89.09|89.09|研究估计；来源有依据，仍需独立复评|
|KAITO|4|4|4|85.73|75.44|80.58|80.58|研究估计；来源有依据，仍需独立复评|
|镜音连|5|5|5|67.45|73.68|70.57|70.57|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|6|6|36.50|63.16|49.83|49.83|该组末位；仍为研究估计|

### OC17_Miku · 初音未来

**成长细分判断：** 主线给继续创作/救助的实际方向，本人明确相信其判断，入门根基仍属父亲。

**情感细分判断：** 创作无意义痛苦真实交托、持续安心，并主动给正月体验/CD/手作，信任围绕核心救助选择。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,2|3,3,3,3|
|细档|3.5,7,2.5,2,2|3.5,3.5,3.5,3.75|

原粗档指数成长/情感 67.17 / 75.00；细分未归一原指数 75.92 / 89.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_Miku_G1 · nightcode_01_12 ただひとつの歌.txt L39–42、45–59、71–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_12%20%E3%81%9F%E3%81%A0%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AE%E6%AD%8C.txt#L39)；[OC17_Miku_G2 · nightcode_01_15 消えてしまう前に.txt L27–29、43–44、46、59–60、66、72–75、77–78、87–88、90、97–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_15%20%E6%B6%88%E3%81%88%E3%81%A6%E3%81%97%E3%81%BE%E3%81%86%E5%89%8D%E3%81%AB.txt#L27)；[OC17_Miku_G3 · 116-08 あの日の音色を.txt L9–18、23–26、31–34、36–41、64–67、69–73](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-08%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E9%9F%B3%E8%89%B2%E3%82%92.txt#L9)；[OC17_Miku_X2 · nightcode_01_12 ただひとつの歌.txt L59–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_12%20%E3%81%9F%E3%81%A0%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AE%E6%AD%8C.txt#L59)；[OC17_Miku_X1 · 1378_宵崎奏_R4 気合いは十分？ (event_202).txt L75–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/1378_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R4%20%E6%B0%97%E5%90%88%E3%81%84%E3%81%AF%E5%8D%81%E5%88%86%EF%BC%9F%20%28event_202%29.txt#L75)；[OC17_Miku_E2 · 0947_宵崎奏_R2 平穏な夜を願って (event_134).txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/0947_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R2%20%E5%B9%B3%E7%A9%8F%E3%81%AA%E5%A4%9C%E3%82%92%E9%A1%98%E3%81%A3%E3%81%A6%20%28event_134%29.txt#L38)

**情感比较正文：** [OC17_Miku_E2 · 0947_宵崎奏_R2 平穏な夜を願って (event_134).txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/0947_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R2%20%E5%B9%B3%E7%A9%8F%E3%81%AA%E5%A4%9C%E3%82%92%E9%A1%98%E3%81%A3%E3%81%A6%20%28event_134%29.txt#L38)；[OC17_Miku_G2 · nightcode_01_15 消えてしまう前に.txt L27–29、43–44、46、59–60、66、72–75、77–78、87–88、90、97–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_15%20%E6%B6%88%E3%81%88%E3%81%A6%E3%81%97%E3%81%BE%E3%81%86%E5%89%8D%E3%81%AB.txt#L27)；[OC17_Miku_G1 · nightcode_01_12 ただひとつの歌.txt L39–42、45–59、71–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_12%20%E3%81%9F%E3%81%A0%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AE%E6%AD%8C.txt#L39)；[OC17_Miku_X2 · nightcode_01_12 ただひとつの歌.txt L59–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_12%20%E3%81%9F%E3%81%A0%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AE%E6%AD%8C.txt#L59)；[OC17_Miku_E9 · 0152_東雲絵名_R4 東雲家の年末 (event_9).txt L176–180](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0152_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E6%9D%B1%E9%9B%B2%E5%AE%B6%E3%81%AE%E5%B9%B4%E6%9C%AB%20%28event_9%29.txt#L176)；[OC17_KAITO_X1 · talk_event_116.txt L63–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L63)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)

### OC17_Rin · 镜音铃

**成长细分判断：** 116自我音乐意义和155反向交流任务均有本人具体归因，父亲启蒙不归铃。

**情感细分判断：** 救助义务与幸福家庭矛盾实际说出，主动报结果和分享成片/选礼物使关系持续。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|3,3,3,2|
|细档|3.5,7,2.5,1,2|3.5,3.5,3.5,2.5|

原粗档指数成长/情感 63.83 / 68.75；细分未归一原指数 72.58 / 81.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_Rin_G1 · 116-04 辿る、記憶の先は.txt L17–29、31–38、40–42、72–73、79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-04%20%E8%BE%BF%E3%82%8B%E3%80%81%E8%A8%98%E6%86%B6%E3%81%AE%E5%85%88%E3%81%AF.txt#L17)；[OC17_Rin_G2 · 116-06 優しい思い出と現実.txt L12–17、20–24、40–44、46–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-06%20%E5%84%AA%E3%81%97%E3%81%84%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E7%8F%BE%E5%AE%9F.txt#L12)；[OC17_Rin_G3 · 116-08 あの日の音色を.txt L9–24、32–41、64–67、69–73](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-08%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E9%9F%B3%E8%89%B2%E3%82%92.txt#L9)；[OC17_Rin_X1 · 155-06 視点を変えれば.txt L69–121](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/155%20Show%20your%20shine%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/155-06%20%E8%A6%96%E7%82%B9%E3%82%92%E5%A4%89%E3%81%88%E3%82%8C%E3%81%B0.txt#L69)；[OC17_Rin_X2 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L99–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L99)；[OC17_Rin_E1 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L99–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L99)；[OC17_KAITO_G3 · 116-07 願い.txt L18–20、27–29、39–41、43、45、48–49、51–53、55、70–71、73、75、77–78、113、115–126、155、157–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-07%20%E9%A1%98%E3%81%84.txt#L18)

**情感比较正文：** [OC17_Rin_E1 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L99–103](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L99)；[OC17_Rin_X2 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L99–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L99)；[OC17_Rin_G2 · 116-06 優しい思い出と現実.txt L12–17、20–24、40–44、46–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-06%20%E5%84%AA%E3%81%97%E3%81%84%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E7%8F%BE%E5%AE%9F.txt#L12)；[OC17_Rin_G1 · 116-04 辿る、記憶の先は.txt L17–29、31–38、40–42、72–73、79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-04%20%E8%BE%BF%E3%82%8B%E3%80%81%E8%A8%98%E6%86%B6%E3%81%AE%E5%85%88%E3%81%AF.txt#L17)；[OC17_Rin_E4 · 0839_鏡音レン_RB Happy Anniversary！！2023.txt L21–25](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0839_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L21)

### OC17_Luka · 巡音流歌

**成长细分判断：** 26创作目的及63自身快乐产生实际认识，关键发现仍与瑞希生活体验共同完成。

**情感细分判断：** 本人反复认可引路与自身快乐建议，是较明确稳定顾问意义；所讲困惑尚不等于父亲负罪深层口述。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|3,2,2,3|
|细档|3.5,7,2.25,1,2|3.5,2.5,2.25,3.75|

原粗档指数成长/情感 63.83 / 62.50；细分未归一原指数 71.33 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_Luka_G1 · 026-02 ルカの言葉.txt L20、22、24、50–52、54–56、58–65、71–73、75–77、80–87、90–101、103–109](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/026%20%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%BB%E3%83%AA%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/026-02%20%E3%83%AB%E3%82%AB%E3%81%AE%E8%A8%80%E8%91%89.txt#L20)；[OC17_Luka_G2 · 026-07 迷路の先にあるもの.txt L7–10、33–35、49–55、57、63、69、86、89–90](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/026%20%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%BB%E3%83%AA%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/026-07%20%E8%BF%B7%E8%B7%AF%E3%81%AE%E5%85%88%E3%81%AB%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE.txt#L7)；[OC17_Luka_G3 · 026-08 ほほ笑み.txt L7–9、16–18、49–53、66、68–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/026%20%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%BB%E3%83%AA%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/026-08%20%E3%81%BB%E3%81%BB%E7%AC%91%E3%81%BF.txt#L7)；[OC17_Luka_X3 · 063-08 つながる笑顔.txt L50–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/063%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%EF%BC%81%E3%82%B9%E3%83%9D%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%91%E3%83%BC%E3%82%AF%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/063-08%20%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E7%AC%91%E9%A1%94.txt#L50)；[OC17_Luka_X4 · 063-02 いざ、体力づくり！.txt L79–124](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/063%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%EF%BC%81%E3%82%B9%E3%83%9D%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%91%E3%83%BC%E3%82%AF%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/063-02%20%E3%81%84%E3%81%96%E3%80%81%E4%BD%93%E5%8A%9B%E3%81%A5%E3%81%8F%E3%82%8A%EF%BC%81.txt#L79)；[OC17_Luka_X5 · 063-06 自分の気持ちを.txt L31–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/063%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%EF%BC%81%E3%82%B9%E3%83%9D%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%91%E3%83%BC%E3%82%AF%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/063-06%20%E8%87%AA%E5%88%86%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%82%92.txt#L31)；[OC17_Luka_G4 · 112-08 もどかしい想い (宵崎奏).txt L12–14、20–22、30–32、39–41、56–58、62–67、69–81、90–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-08%20%E3%82%82%E3%81%A9%E3%81%8B%E3%81%97%E3%81%84%E6%83%B3%E3%81%84%20%28%E5%AE%B5%E5%B4%8E%E5%A5%8F%29.txt#L12)；[OC17_Luka_X1 · 112-09 一緒に探そう (宵崎奏).txt L65–100](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-09%20%E4%B8%80%E7%B7%92%E3%81%AB%E6%8E%A2%E3%81%9D%E3%81%86%20%28%E5%AE%B5%E5%B4%8E%E5%A5%8F%29.txt#L65)；[OC17_Luka_X2 · 112-09 一緒に探そう (宵崎奏).txt L100–123](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-09%20%E4%B8%80%E7%B7%92%E3%81%AB%E6%8E%A2%E3%81%9D%E3%81%86%20%28%E5%AE%B5%E5%B4%8E%E5%A5%8F%29.txt#L100)；[OC17_Luka_E2 · 035-08 ほんの少しの灯.txt L53–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-08%20%E3%81%BB%E3%82%93%E3%81%AE%E5%B0%91%E3%81%97%E3%81%AE%E7%81%AF.txt#L53)

**情感比较正文：** [OC17_Luka_E1 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L82)；[OC17_Luka_E2 · 035-08 ほんの少しの灯.txt L53–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-08%20%E3%81%BB%E3%82%93%E3%81%AE%E5%B0%91%E3%81%97%E3%81%AE%E7%81%AF.txt#L53)；[OC17_Luka_X3 · 063-08 つながる笑顔.txt L50–71](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/063%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%EF%BC%81%E3%82%B9%E3%83%9D%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%91%E3%83%BC%E3%82%AF%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/063-08%20%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E7%AC%91%E9%A1%94.txt#L50)；[OC17_Luka_G1 · 026-02 ルカの言葉.txt L20、22、24、50–52、54–56、58–65、71–73、75–77、80–87、90–101、103–109](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/026%20%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%BB%E3%83%AA%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/026-02%20%E3%83%AB%E3%82%AB%E3%81%AE%E8%A8%80%E8%91%89.txt#L20)；[OC17_Luka_G4 · 112-08 もどかしい想い (宵崎奏).txt L12–14、20–22、30–32、39–41、56–58、62–67、69–81、90–108](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-08%20%E3%82%82%E3%81%A9%E3%81%8B%E3%81%97%E3%81%84%E6%83%B3%E3%81%84%20%28%E5%AE%B5%E5%B4%8E%E5%A5%8F%29.txt#L12)；[OC17_Luka_X5 · 063-06 自分の気持ちを.txt L31–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/063%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%A7%E3%82%A4%EF%BC%81%E3%82%B9%E3%83%9D%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%91%E3%83%BC%E3%82%AF%20%28Mix_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/063-06%20%E8%87%AA%E5%88%86%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%82%92.txt#L31)；[OC17_Luka_E6 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L38–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L38)

### OC17_KAITO · KAITO

**成长细分判断：** 116对压抑愿望的反驳与绘名共促幸福曲，主要具名归因保留铃/绘名，不移占。

**情感细分判断：** 父亲负罪与无资格幸福的痛苦实际通话听见，个人蛋糕回报明确但范围较具体。 116介入实际通话并听到父亲负罪/无资格幸福的自我否定，这是该档很强的核心脆弱交托，信任细分3.75；不宣称私人独谈。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,1,1,2|2,3,2,2|
|细档|3.5,7,1,1,2|2.25,3.75,2.25,2.5|

原粗档指数成长/情感 58.83 / 56.25；细分未归一原指数 65.08 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_KAITO_G1 · 089-06 認めたくない.txt L17、22–23、39–41、43–61、63–72、75–78、87–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/089%20%E3%82%A4%E3%83%9F%E3%82%B7%E3%83%96%E3%83%AB%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/089-06%20%E8%AA%8D%E3%82%81%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84.txt#L17)；[OC17_KAITO_G2 · 100-08 手を伸ばす、そのさきは.txt L68–69、75、142–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-08%20%E6%89%8B%E3%82%92%E4%BC%B8%E3%81%B0%E3%81%99%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF.txt#L68)；[OC17_KAITO_G3 · 116-07 願い.txt L18–20、27–29、39–41、43、45、48–49、51–53、55、70–71、73、75、77–78、113、115–126、155、157–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-07%20%E9%A1%98%E3%81%84.txt#L18)；[OC17_KAITO_G4 · 116-08 あの日の音色を.txt L14–16、21–23、29–34、39–41、64–67、69–73](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-08%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E9%9F%B3%E8%89%B2%E3%82%92.txt#L14)；[OC17_KAITO_X1 · talk_event_116.txt L63–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L63)；[OC17_KAITO_X2 · 1274_KAITO (N25)_R4 迷いなき“らしさ”を (event_184).txt L23–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1274_KAITO%20%28N25%29_R4%20%E8%BF%B7%E3%81%84%E3%81%AA%E3%81%8D%E2%80%9C%E3%82%89%E3%81%97%E3%81%95%E2%80%9D%E3%82%92%20%28event_184%29.txt#L23)；[OC17_KAITO_X3 · 1338_KAITO_RB Happy Anniversary！！2026.txt L81–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L81)；[OC17_Rin_X3 · 116-07 願い.txt L163–180](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-07%20%E9%A1%98%E3%81%84.txt#L163)

**情感比较正文：** [OC17_KAITO_E2 · talk_event_116.txt L73–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L73)；[OC17_KAITO_X3 · 1338_KAITO_RB Happy Anniversary！！2026.txt L81–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L81)；[OC17_KAITO_G3 · 116-07 願い.txt L18–20、27–29、39–41、43、45、48–49、51–53、55、70–71、73、75、77–78、113、115–126、155、157–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/116%20%E3%81%82%E3%81%AE%E6%97%A5%E3%80%81%E5%A5%8F%E3%81%A7%E3%81%9F%E9%9F%B3%E8%89%B2%E3%82%92%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/116-07%20%E9%A1%98%E3%81%84.txt#L18)；[OC17_KAITO_X1 · talk_event_116.txt L63–75](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L63)

### OC17_Len · 镜音连

**成长细分判断：** 共同手作快乐有本人直接归因，165传信只是实務帮助，核心创作未全归连。

**情感细分判断：** 主动寻找低落连、缓解不安与教烛礼实际，奏本人的深层痛苦目前没同等向连说。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,1,1|2,2,3,2|
|细档|2.25,4,2.5,1,1|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 45.58 / 56.25；细分未归一原指数 51.21 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_Len_F1 · 084-06 一緒に作ろう.txt L59–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-06%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E3%82%8D%E3%81%86.txt#L59)；[OC17_Len_X1 · 084-06 一緒に作ろう.txt L24–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-06%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E3%82%8D%E3%81%86.txt#L24)；[OC17_Len_X2 · 1163_宵崎奏_R4 からっぽになる部屋 (event_165).txt L101–133](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/1163_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R4%20%E3%81%8B%E3%82%89%E3%81%A3%E3%81%BD%E3%81%AB%E3%81%AA%E3%82%8B%E9%83%A8%E5%B1%8B%20%28event_165%29.txt#L101)；[OC17_Len_E2 · 1163_宵崎奏_R4 からっぽになる部屋 (event_165).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/1163_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R4%20%E3%81%8B%E3%82%89%E3%81%A3%E3%81%BD%E3%81%AB%E3%81%AA%E3%82%8B%E9%83%A8%E5%B1%8B%20%28event_165%29.txt#L131)；[OC17_Len_E3 · talk_event_116.txt L162–166](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L162)；[OC17_Len_X3 · 084-07 みんなへのプレゼント.txt L126–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L126)

**情感比较正文：** [OC17_Len_E2 · 1163_宵崎奏_R4 からっぽになる部屋 (event_165).txt L131–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/1163_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R4%20%E3%81%8B%E3%82%89%E3%81%A3%E3%81%BD%E3%81%AB%E3%81%AA%E3%82%8B%E9%83%A8%E5%B1%8B%20%28event_165%29.txt#L131)；[OC17_Len_E3 · talk_event_116.txt L162–166](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L162)；[OC17_Len_X3 · 084-07 みんなへのプレゼント.txt L126–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L126)；[OC17_Len_F1 · 084-06 一緒に作ろう.txt L59–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-06%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E3%82%8D%E3%81%86.txt#L59)；[OC17_Len_X1 · 084-06 一緒に作ろう.txt L24–58](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-06%20%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%9C%E3%82%8D%E3%81%86.txt#L24)

### OC17_MEIKO · MEIKO

**成长细分判断：** 作品类型提醒与湖风险关心明确，尚未核具体改变后果。

**情感细分判断：** 主动请听作品及周年点心确实，但主要具体关心/咨询，暂无深层交托或稳定特殊依靠。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,2|2,2,2,2|
|细档|1.25,0,1.25,1,2|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 23.33 / 50.00；细分未归一原指数 27.71 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC17_MEIKO_F1 · 0294_宵崎奏_R3 音楽が見せてくれる世界 (event_36).txt L118–138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/0294_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R3%20%E9%9F%B3%E6%A5%BD%E3%81%8C%E8%A6%8B%E3%81%9B%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%B8%96%E7%95%8C%20%28event_36%29.txt#L118)；[OC17_MEIKO_X1 · talk_event_134.txt L130–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_134.txt#L130)；[OC17_MEIKO_X2 · 0533_MEIKO_RB Happy Anniversary！！2022.txt L23–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0533_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812022.txt#L23)；[OC17_MEIKO_E2 · talk_event_134.txt L145–149](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_134.txt#L145)

**情感比较正文：** [OC17_MEIKO_E2 · talk_event_134.txt L145–149](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_134.txt#L145)；[OC17_MEIKO_F1 · 0294_宵崎奏_R3 音楽が見せてくれる世界 (event_36).txt L118–138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/17%20N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F/0294_%E5%AE%B5%E5%B4%8E%E5%A5%8F_R3%20%E9%9F%B3%E6%A5%BD%E3%81%8C%E8%A6%8B%E3%81%9B%E3%81%A6%E3%81%8F%E3%82%8C%E3%82%8B%E4%B8%96%E7%95%8C%20%28event_36%29.txt#L118)；[OC17_MEIKO_X2 · 0533_MEIKO_RB Happy Anniversary！！2022.txt L23–47](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0533_MEIKO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812022.txt#L23)；[OC17_MEIKO_X1 · talk_event_134.txt L130–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_134.txt#L130)

## 朝比奈真冬

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|初音未来|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|镜音铃|2|2|2|78.12|91.38|84.75|84.75|研究估计；来源有依据，仍需独立复评|
|镜音连|3|4|3|76.77|74.14|75.45|75.45|研究估计；来源有依据，仍需独立复评|
|KAITO|4|3|4|65.20|75.86|70.53|70.53|研究估计；来源有依据，仍需独立复评|
|巡音流歌|5|6|5|60.49|65.52|63.01|63.01|研究估计；来源有依据，仍需独立复评|
|MEIKO|6|5|6|24.89|67.24|46.06|46.06|该组末位；仍为研究估计|

### OC18_Miku · 初音未来

**成长细分判断：** 本人与奏共同赋予自我能存在/保留心意的根基意义，K4保留；重大共同归因S3内较充分。

**情感细分判断：** 本人持续确认相遇很好、真实说消失/回忆恐惧并亲手回报，显式根基关系4保留，不移用Miku自己的誓言。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|4,10,3,2,3|3,3,3,4|
|细档|4,10,3.5,2,3|3.5,3.5,3.5,4|

原粗档指数成长/情感 90.42 / 81.25；细分未归一原指数 92.92 / 90.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_Miku_G2 · nightcode_01_19 悔やむと書いてミライ.txt L17–22、24–36、39–41、46–47、53、73、75–76](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/6%2025%E6%99%82%E3%80%81%E3%83%8A%E3%82%A4%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E3%80%82/nightcode_01_19%20%E6%82%94%E3%82%84%E3%82%80%E3%81%A8%E6%9B%B8%E3%81%84%E3%81%A6%E3%83%9F%E3%83%A9%E3%82%A4.txt#L17)；[OC18_Miku_G3 · 100-06 心を守るために.txt L36–39、44–49、52–54、66–72、90、96–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-06%20%E5%BF%83%E3%82%92%E5%AE%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB.txt#L36)；[OC18_Miku_G4 · 100-07 仮面を捨てて.txt L19–21、35–37、52–54、56–60、76–78、138、140–142、144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-07%20%E4%BB%AE%E9%9D%A2%E3%82%92%E6%8D%A8%E3%81%A6%E3%81%A6.txt#L19)；[OC18_Miku_G5 · 100-08 手を伸ばす、そのさきは.txt L6–8、13–20、29–31、47–49、55、75、81–82、88、91–93、96、98、100、102、104、106、165–167](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-08%20%E6%89%8B%E3%82%92%E4%BC%B8%E3%81%B0%E3%81%99%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF.txt#L6)；[OC18_Miku_G6 · 112-03 水底に沈むもの (朝比奈まふゆ).txt L27–29、44–54、63–70、72–74、86–88、92–94、96–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-03%20%E6%B0%B4%E5%BA%95%E3%81%AB%E6%B2%88%E3%82%80%E3%82%82%E3%81%AE%20%28%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29.txt#L27)；[OC18_Miku_G7 · 112-10 いつか、進むために.txt L16、18–19、59–61、65–67、73–75、77–83、86–88、91–93、118–120、177、180–181、187、197–199、208–210、231–236、238–239](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-10%20%E3%81%84%E3%81%A4%E3%81%8B%E3%80%81%E9%80%B2%E3%82%80%E3%81%9F%E3%82%81%E3%81%AB.txt#L16)；[OC18_Miku_X1 · 0365_初音ミク (N25)_R2 始まりの想いを見守って (event_47).txt L130–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0365_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R2%20%E5%A7%8B%E3%81%BE%E3%82%8A%E3%81%AE%E6%83%B3%E3%81%84%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_47%29.txt#L130)；[OC18_Miku_X3 · 0365_初音ミク (N25)_R2 始まりの想いを見守って (event_47).txt L152–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0365_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R2%20%E5%A7%8B%E3%81%BE%E3%82%8A%E3%81%AE%E6%83%B3%E3%81%84%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_47%29.txt#L152)；[OC18_Len_X4 · 0834_朝比奈まふゆ_R4 こぼれた本音 (event_116).txt L111–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/0834_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E3%81%93%E3%81%BC%E3%82%8C%E3%81%9F%E6%9C%AC%E9%9F%B3%20%28event_116%29.txt#L111)；[OC18_Miku_E4 · vsnightcode_01_02 痛そうな音符.txt L22–26](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/1%20%E3%83%90%E3%83%BC%E3%83%81%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%B7%E3%83%B3%E3%82%AC%E3%83%BC/vsnightcode_01_02%20%E7%97%9B%E3%81%9D%E3%81%86%E3%81%AA%E9%9F%B3%E7%AC%A6.txt#L22)

**情感比较正文：** [OC18_Miku_E1 · 0086_初音ミク (N25)_R2 誰もいないセカイ.txt L56–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0086_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R2%20%E8%AA%B0%E3%82%82%E3%81%84%E3%81%AA%E3%81%84%E3%82%BB%E3%82%AB%E3%82%A4.txt#L56)；[OC18_Miku_X1 · 0365_初音ミク (N25)_R2 始まりの想いを見守って (event_47).txt L130–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0365_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R2%20%E5%A7%8B%E3%81%BE%E3%82%8A%E3%81%AE%E6%83%B3%E3%81%84%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_47%29.txt#L130)；[OC18_Len_X4 · 0834_朝比奈まふゆ_R4 こぼれた本音 (event_116).txt L111–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/0834_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E3%81%93%E3%81%BC%E3%82%8C%E3%81%9F%E6%9C%AC%E9%9F%B3%20%28event_116%29.txt#L111)；[OC18_Miku_G3 · 100-06 心を守るために.txt L36–39、44–49、52–54、66–72、90、96–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-06%20%E5%BF%83%E3%82%92%E5%AE%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB.txt#L36)；[OC18_Miku_G6 · 112-03 水底に沈むもの (朝比奈まふゆ).txt L27–29、44–54、63–70、72–74、86–88、92–94、96–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-03%20%E6%B0%B4%E5%BA%95%E3%81%AB%E6%B2%88%E3%82%80%E3%82%82%E3%81%AE%20%28%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29.txt#L27)；[OC18_Miku_E7 · vsnightcode_01_04 あなたの音楽.txt L25–29](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/main/1%20%E3%83%90%E3%83%BC%E3%83%81%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%B7%E3%83%B3%E3%82%AC%E3%83%BC/vsnightcode_01_04%20%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AE%E9%9F%B3%E6%A5%BD.txt#L25)；[OC18_Miku_E8 · talk_event_170.txt L53–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_170.txt#L53)；[OC18_Miku_E9 · 0904_朝比奈まふゆ_R4 穏やかな身支度 (event_127).txt L109–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/0904_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E7%A9%8F%E3%82%84%E3%81%8B%E3%81%AA%E8%BA%AB%E6%94%AF%E5%BA%A6%20%28event_127%29.txt#L109)；[OC18_Miku_X2 · talk_event_170.txt L53–64](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_170.txt#L53)；[OC18_Rin_X5 · 156-08 伝わったもの.txt L26–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-08%20%E4%BC%9D%E3%82%8F%E3%81%A3%E3%81%9F%E3%82%82%E3%81%AE.txt#L26)；[OC18_Miku_X3 · 0365_初音ミク (N25)_R2 始まりの想いを見守って (event_47).txt L152–159](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/0365_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R2%20%E5%A7%8B%E3%81%BE%E3%82%8A%E3%81%AE%E6%83%B3%E3%81%84%E3%82%92%E8%A6%8B%E5%AE%88%E3%81%A3%E3%81%A6%20%28event_47%29.txt#L152)

### OC18_Rin · 镜音铃

**成长细分判断：** 134父亲温柔提示使开口、35歌词提醒两任务有实际作用，仍保留瑞希/父亲共同贡献。

**情感细分判断：** 父亲意义和无法否定的困惑真实口述，照顾惊雷及手作回应持续，个人顾问意义较清楚。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|3,3,3,2|
|细档|3.5,7,2.5,1,2|3.5,3.5,3.5,2.75|

原粗档指数成长/情感 63.83 / 68.75；细分未归一原指数 72.58 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_Rin_F1 · 134-07 雷鳴の夜.txt L59–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-07%20%E9%9B%B7%E9%B3%B4%E3%81%AE%E5%A4%9C.txt#L59)；[OC18_Rin_X1 · 035-07 辿り着きたい場所.txt L66–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-07%20%E8%BE%BF%E3%82%8A%E7%9D%80%E3%81%8D%E3%81%9F%E3%81%84%E5%A0%B4%E6%89%80.txt#L66)；[OC18_Rin_X3 · 134-08 灯を握りしめて.txt L35–91](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-08%20%E7%81%AF%E3%82%92%E6%8F%A1%E3%82%8A%E3%81%97%E3%82%81%E3%81%A6.txt#L35)；[OC18_Rin_X4 · 134-07 雷鳴の夜.txt L43–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-07%20%E9%9B%B7%E9%B3%B4%E3%81%AE%E5%A4%9C.txt#L43)；[OC18_Rin_X6 · 134-08 灯を握りしめて.txt L17–36](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-08%20%E7%81%AF%E3%82%92%E6%8F%A1%E3%82%8A%E3%81%97%E3%82%81%E3%81%A6.txt#L17)；[OC18_Rin_E1 · 1142_鏡音リン (N25)_R3 届かない声 (event_161).txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1142_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R3%20%E5%B1%8A%E3%81%8B%E3%81%AA%E3%81%84%E5%A3%B0%20%28event_161%29.txt#L82)；[OC18_Rin_E3 · 0945_鏡音リン (N25)_R4 初めての轟音 (event_134).txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0945_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E8%BD%9F%E9%9F%B3%20%28event_134%29.txt#L68)

**情感比较正文：** [OC18_Rin_E1 · 1142_鏡音リン (N25)_R3 届かない声 (event_161).txt L82–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1142_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R3%20%E5%B1%8A%E3%81%8B%E3%81%AA%E3%81%84%E5%A3%B0%20%28event_161%29.txt#L82)；[OC18_Rin_E2 · 035-07 辿り着きたい場所.txt L73–77](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-07%20%E8%BE%BF%E3%82%8A%E7%9D%80%E3%81%8D%E3%81%9F%E3%81%84%E5%A0%B4%E6%89%80.txt#L73)；[OC18_Rin_E3 · 0945_鏡音リン (N25)_R4 初めての轟音 (event_134).txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0945_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E8%BD%9F%E9%9F%B3%20%28event_134%29.txt#L68)；[OC18_Rin_X1 · 035-07 辿り着きたい場所.txt L66–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-07%20%E8%BE%BF%E3%82%8A%E7%9D%80%E3%81%8D%E3%81%9F%E3%81%84%E5%A0%B4%E6%89%80.txt#L66)；[OC18_Rin_F1 · 134-07 雷鳴の夜.txt L59–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-07%20%E9%9B%B7%E9%B3%B4%E3%81%AE%E5%A4%9C.txt#L59)；[OC18_Rin_X4 · 134-07 雷鳴の夜.txt L43–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/134%20%E7%81%AF%E3%82%92%E6%89%8B%E7%B9%B0%E3%82%8A%E3%82%88%E3%81%9B%E3%81%A6%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/134-07%20%E9%9B%B7%E9%B3%B4%E3%81%AE%E5%A4%9C.txt#L43)；[OC18_Rin_X5 · 156-08 伝わったもの.txt L26–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-08%20%E4%BC%9D%E3%82%8F%E3%81%A3%E3%81%9F%E3%82%82%E3%81%AE.txt#L26)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)

### OC18_Len · 镜音连

**成长细分判断：** 61辨温暖和0834身体自照实际改变，核心自我感知直接；父亲开口并非该线结果。

**情感细分判断：** 纪念品/手作/游戏回应持续，但61童年迷路主要内心，信任细分不按口述创伤加分。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|2,2,3,2|
|细档|3.5,7,2.25,1,2|2.25,2.5,3.5,2.5|

原粗档指数成长/情感 63.83 / 56.25；细分未归一原指数 71.33 / 67.19。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_Len_G1 · 061-08 私にとって、この場所は.txt L50–61、69、74、79–81、86–91、108–110、112、117、122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/061%20%E8%BF%B7%E3%81%84%E5%AD%90%E3%81%AE%E6%89%8B%E3%82%92%E5%BC%95%E3%81%8F%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/061-08%20%E7%A7%81%E3%81%AB%E3%81%A8%E3%81%A3%E3%81%A6%E3%80%81%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%E3%81%AF.txt#L50)；[OC18_Len_G2 · 112-03 水底に沈むもの (朝比奈まふゆ).txt L5–12、14–16、23–38、44、49–51、54–56、58–63、67–69、73–75、87–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-03%20%E6%B0%B4%E5%BA%95%E3%81%AB%E6%B2%88%E3%82%80%E3%82%82%E3%81%AE%20%28%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29.txt#L5)；[OC18_Len_X2 · 061-08 私にとって、この場所は.txt L36–61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/061%20%E8%BF%B7%E3%81%84%E5%AD%90%E3%81%AE%E6%89%8B%E3%82%92%E5%BC%95%E3%81%8F%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/061-08%20%E7%A7%81%E3%81%AB%E3%81%A8%E3%81%A3%E3%81%A6%E3%80%81%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%E3%81%AF.txt#L36)；[OC18_Len_X3 · talk_event_084.txt L103–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_084.txt#L103)；[OC18_Len_X4 · 0834_朝比奈まふゆ_R4 こぼれた本音 (event_116).txt L111–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/0834_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E3%81%93%E3%81%BC%E3%82%8C%E3%81%9F%E6%9C%AC%E9%9F%B3%20%28event_116%29.txt#L111)；[OC18_Len_E1 · 077-08 私が表現したいもの.txt L51–55](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/077%20%E9%A1%98%E3%81%84%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E6%9C%9D%E3%82%92%E3%81%93%E3%81%88%E3%81%A6%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/077-08%20%E7%A7%81%E3%81%8C%E8%A1%A8%E7%8F%BE%E3%81%97%E3%81%9F%E3%81%84%E3%82%82%E3%81%AE.txt#L51)

**情感比较正文：** [OC18_Len_E1 · 077-08 私が表現したいもの.txt L51–55](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/077%20%E9%A1%98%E3%81%84%E3%81%AF%E3%80%81%E3%81%84%E3%81%A4%E3%81%8B%E6%9C%9D%E3%82%92%E3%81%93%E3%81%88%E3%81%A6%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/077-08%20%E7%A7%81%E3%81%8C%E8%A1%A8%E7%8F%BE%E3%81%97%E3%81%9F%E3%81%84%E3%82%82%E3%81%AE.txt#L51)；[OC18_Len_E2 · 215-06 何が何でどれがどれ？.txt L80–84](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/215%20Mix%26Make%20Party%20Time%21%21%20%28Mix_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB-VS%29/215-06%20%E4%BD%95%E3%81%8C%E4%BD%95%E3%81%A7%E3%81%A9%E3%82%8C%E3%81%8C%E3%81%A9%E3%82%8C%EF%BC%9F.txt#L80)；[OC18_Len_X4 · 0834_朝比奈まふゆ_R4 こぼれた本音 (event_116).txt L111–144](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/0834_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E3%81%93%E3%81%BC%E3%82%8C%E3%81%9F%E6%9C%AC%E9%9F%B3%20%28event_116%29.txt#L111)；[OC18_Len_G2 · 112-03 水底に沈むもの (朝比奈まふゆ).txt L5–12、14–16、23–38、44、49–51、54–56、58–63、67–69、73–75、87–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-03%20%E6%B0%B4%E5%BA%95%E3%81%AB%E6%B2%88%E3%82%80%E3%82%82%E3%81%AE%20%28%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29.txt#L5)；[OC18_Len_X2 · 061-08 私にとって、この場所は.txt L36–61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/061%20%E8%BF%B7%E3%81%84%E5%AD%90%E3%81%AE%E6%89%8B%E3%82%92%E5%BC%95%E3%81%8F%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/061-08%20%E7%A7%81%E3%81%AB%E3%81%A8%E3%81%A3%E3%81%A6%E3%80%81%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%E3%81%AF.txt#L36)；[OC18_Len_X3 · talk_event_084.txt L103–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_084.txt#L103)；[OC18_Rin_X5 · 156-08 伝わったもの.txt L26–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-08%20%E4%BC%9D%E3%82%8F%E3%81%A3%E3%81%9F%E3%82%82%E3%81%AE.txt#L26)；[OC18_Luka_E3 · talk_event_189.txt L35–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_189.txt#L35)；[OC18_Len_G1 · 061-08 私にとって、この場所は.txt L50–61、69、74、79–81、86–91、108–110、112、117、122](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/061%20%E8%BF%B7%E3%81%84%E5%AD%90%E3%81%AE%E6%89%8B%E3%82%92%E5%BC%95%E3%81%8F%E3%80%81%E3%81%9D%E3%81%AE%E3%81%95%E3%81%8D%E3%81%AF%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/061-08%20%E7%A7%81%E3%81%AB%E3%81%A8%E3%81%A3%E3%81%A6%E3%80%81%E3%81%93%E3%81%AE%E5%A0%B4%E6%89%80%E3%81%AF.txt#L50)

### OC18_KAITO · KAITO

**成长细分判断：** 母亲关系与保护自我尖锐提醒被回应/实际表达，核心作用较直接，结果归因尚不独占给他。

**情感细分判断：** 本人直接问没人听拒绝该怎么办和恐惧，桔梗手帕亲送；深层自身问题交托比对连的具体感受更完整。 089及100本人直接回应没人听拒绝、再问怎么做，并让他看见保护自我时的恐惧，信任细分3.75；冲突非赞成其全部方法。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,2|2,3,2,2|
|细档|3.5,4,1,1,2|2.25,3.75,2.5,2.5|

原粗档指数成长/情感 54.33 / 56.25；细分未归一原指数 60.58 / 68.75。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_KAITO_G1 · 089-05 意思表示の果てに.txt L25–27、42–44、58–60、66、75–79、85、88–90、109–114、135–137、147–151](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/089%20%E3%82%A4%E3%83%9F%E3%82%B7%E3%83%96%E3%83%AB%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/089-05%20%E6%84%8F%E6%80%9D%E8%A1%A8%E7%A4%BA%E3%81%AE%E6%9E%9C%E3%81%A6%E3%81%AB.txt#L25)；[OC18_KAITO_G2 · 089-06 認めたくない.txt L43–61、63–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/089%20%E3%82%A4%E3%83%9F%E3%82%B7%E3%83%96%E3%83%AB%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/089-06%20%E8%AA%8D%E3%82%81%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84.txt#L43)；[OC18_KAITO_G3 · 100-05 見えない心、確かな想い.txt L15、26–27、33–35、42–43、49、69–71、77、83、124–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-05%20%E8%A6%8B%E3%81%88%E3%81%AA%E3%81%84%E5%BF%83%E3%80%81%E7%A2%BA%E3%81%8B%E3%81%AA%E6%83%B3%E3%81%84.txt#L15)；[OC18_KAITO_G4 · 100-06 心を守るために.txt L36–50、53–64、90、96–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-06%20%E5%BF%83%E3%82%92%E5%AE%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB.txt#L36)；[OC18_KAITO_G5 · 100-07 仮面を捨てて.txt L19–21、35–37、52–54、56–60、76–78、132、134–136、138](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-07%20%E4%BB%AE%E9%9D%A2%E3%82%92%E6%8D%A8%E3%81%A6%E3%81%A6.txt#L19)；[OC18_KAITO_G6 · 112-03 水底に沈むもの (朝比奈まふゆ).txt L11–13、15–22、27–29、31–35、92–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-03%20%E6%B0%B4%E5%BA%95%E3%81%AB%E6%B2%88%E3%82%80%E3%82%82%E3%81%AE%20%28%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29.txt#L11)；[OC18_KAITO_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L140–162](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L140)；[OC18_KAITO_E2 · talk_event_192.txt L86–90](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_192.txt#L86)；[OC18_KAITO_E3 · talk_event_192.txt L90–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_192.txt#L90)

**情感比较正文：** [OC18_KAITO_E3 · talk_event_192.txt L90–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_192.txt#L90)；[OC18_KAITO_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L140–162](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L140)；[OC18_KAITO_G2 · 089-06 認めたくない.txt L43–61、63–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/089%20%E3%82%A4%E3%83%9F%E3%82%B7%E3%83%96%E3%83%AB%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89%20%28N25_%E5%AE%B5%E5%B4%8E%E5%A5%8F%29/089-06%20%E8%AA%8D%E3%82%81%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84.txt#L43)；[OC18_KAITO_G4 · 100-06 心を守るために.txt L36–50、53–64、90、96–97](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/100%20%E4%BB%AE%E9%9D%A2%E3%81%AE%E7%A7%81%E3%81%AB%E3%81%95%E3%82%88%E3%81%AA%E3%82%89%E3%82%92%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/100-06%20%E5%BF%83%E3%82%92%E5%AE%88%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB.txt#L36)

### OC18_Luka · 巡音流歌

**成长细分判断：** 112给回忆形成自我的方向，实际敢试关键也有奏承诺，个人成果归因仍感谢。

**情感细分判断：** 本人说不敢再探湖但未详细口述记忆，较一般礼物相談有个人脆弱；庆生及群体刺绣有本人行动。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,1,1|2,2,2,2|
|细档|3.25,4,1,1,1|2.25,2.5,2.25,2.5|

原粗档指数成长/情感 53.08 / 50.00；细分未归一原指数 56.21 / 59.38。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_Luka_G1 · 112-10 いつか、進むために.txt L16、18–19、61–63、86–88、92–100、118–120、134–136、177、180–181、187、197–199、218–221、232–234、236–238](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-10%20%E3%81%84%E3%81%A4%E3%81%8B%E3%80%81%E9%80%B2%E3%82%80%E3%81%9F%E3%82%81%E3%81%AB.txt#L16)；[OC18_Luka_X3 · 112-10 いつか、進むために.txt L87–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-10%20%E3%81%84%E3%81%A4%E3%81%8B%E3%80%81%E9%80%B2%E3%82%80%E3%81%9F%E3%82%81%E3%81%AB.txt#L87)；[OC18_Luka_E2 · talk_event_042.txt L131–133](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_042.txt#L131)；[OC18_Luka_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L116–139](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L116)；[OC18_Luka_X2 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L19–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L19)；[OC18_Rin_X5 · 156-08 伝わったもの.txt L26–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-08%20%E4%BC%9D%E3%82%8F%E3%81%A3%E3%81%9F%E3%82%82%E3%81%AE.txt#L26)

**情感比较正文：** [OC18_Luka_E2 · talk_event_042.txt L131–133](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_042.txt#L131)；[OC18_Luka_X2 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L19–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L19)；[OC18_Luka_X3 · 112-10 いつか、進むために.txt L87–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-10%20%E3%81%84%E3%81%A4%E3%81%8B%E3%80%81%E9%80%B2%E3%82%80%E3%81%9F%E3%82%81%E3%81%AB.txt#L87)；[OC18_Luka_E1 · talk_event_192.txt L41–45](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_192.txt#L41)；[OC18_Luka_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L116–139](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L116)；[OC18_Rin_X5 · 156-08 伝わったもの.txt L26–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/156%20%E3%81%93%E3%81%AE%E3%81%B2%E3%81%A8%E9%87%9D%E3%81%AB%E6%83%B3%E3%81%84%E3%82%92%E8%BE%BC%E3%82%81%E3%81%A6%20%28Mix_%E6%97%A5%E9%87%8E%E6%A3%AE%E9%9B%AB%29/156-08%20%E4%BC%9D%E3%82%8F%E3%81%A3%E3%81%9F%E3%82%82%E3%81%AE.txt#L26)

### OC18_MEIKO · MEIKO

**成长细分判断：** 疲倦倚睡的个别照料实际，没核个别新的K2+改变。

**情感细分判断：** 允许近身倚睡、认一直见守并亲手专送蝴蝶手帕，是生活性信赖；没有深层创伤口述。 疲倦时实际接受倚睡，是把身体休息交给她的具体生活信赖，信任细分2.50；不扩成口述核心创伤。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,0,1|2,2,2,2|
|细档|1.25,0,1.25,0,1|2.25,2.5,2.5,2.5|

原粗档指数成长/情感 18.75 / 50.00；细分未归一原指数 23.13 / 60.94。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC18_MEIKO_F1 · talk_grade2.txt L1884–1889](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1884)；[OC18_MEIKO_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L92–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L92)；[OC18_Len_X3 · talk_event_084.txt L103–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_084.txt#L103)

**情感比较正文：** [OC18_MEIKO_F1 · talk_grade2.txt L1884–1889](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1884)；[OC18_MEIKO_X1 · 1105_朝比奈まふゆ_R4 静かな図書室で (event_156).txt L92–113](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/18%20N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86/1105_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86_R4%20%E9%9D%99%E3%81%8B%E3%81%AA%E5%9B%B3%E6%9B%B8%E5%AE%A4%E3%81%A7%20%28event_156%29.txt#L92)

## 东云绘名

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|镜音铃|1|2|1|100.00|92.98|96.49|100.00|研究估计；来源有依据，仍需独立复评|
|MEIKO|4|1|2|84.93|100.00|92.46|95.83|研究估计；来源有依据，仍需独立复评|
|镜音连|2|3|3|94.28|84.21|89.25|92.49|研究估计；来源有依据，仍需独立复评|
|KAITO|3|5|4|88.98|80.70|84.84|87.93|研究估计；来源有依据，仍需独立复评|
|初音未来|5|4|5|79.47|82.46|80.96|83.91|研究估计；来源有依据，仍需独立复评|
|巡音流歌|6|6|6|71.05|78.95|75.00|77.73|该组末位；仍为研究估计|

### OC19_Rin · 镜音铃

**成长细分判断：** 自我认可、画中未来和父画三问题持续有实际提示，本人具体愿继续走的归因较充分。

**情感细分判断：** 无人认可、追梦与父亲痛苦实际连续交托，教构图/带材料按兴趣回应，个人艺术理解较集中。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,2,2|3,3,3,2|
|细档|3.5,9,2.75,2,2|3.5,3.5,3.5,2.75|

原粗档指数成长/情感 70.17 / 68.75；细分未归一原指数 80.17 / 82.81。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_Rin_G1 · 014-06 一番大切なことは.txt L79、82–85、88–95、101–103、109、120–123、125–127、130–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/014%20%E6%BA%80%E3%81%9F%E3%81%95%E3%82%8C%E3%81%AA%E3%81%84%E3%83%9A%E3%82%A4%E3%83%AB%E3%82%AB%E3%83%A9%E3%83%BC%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/014-06%20%E4%B8%80%E7%95%AA%E5%A4%A7%E5%88%87%E3%81%AA%E3%81%93%E3%81%A8%E3%81%AF.txt#L79)；[OC19_Rin_G2 · 112-06 目指したい場所 (東雲絵名).txt L11–16、21–23、25–26、28–32、35、38、40、42、50–51、57–63、106–124、127–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-06%20%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%9F%E3%81%84%E5%A0%B4%E6%89%80%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L11)；[OC19_Rin_G3 · 112-07 届いていたもの (東雲絵名).txt L5–10、22–28、37–45、48–56、66–70、73–76、78–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-07%20%E5%B1%8A%E3%81%84%E3%81%A6%E3%81%84%E3%81%9F%E3%82%82%E3%81%AE%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L5)；[OC19_Rin_G4 · 127-04 憂鬱な朝.txt L7–8、21–29、70–72、81–84、89–91、96–98](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-04%20%E6%86%82%E9%AC%B1%E3%81%AA%E6%9C%9D.txt#L7)；[OC19_Rin_G5 · 127-05 向き合わなきゃ.txt L6–8、37–39、43、45–46、55–64、66–74、77–83、85–90、96–98、100–102、120–122、131–134、141、146–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-05%20%E5%90%91%E3%81%8D%E5%90%88%E3%82%8F%E3%81%AA%E3%81%8D%E3%82%83.txt#L6)；[OC19_Rin_G6 · 127-06 夜更けの景色.txt L11–16、19–21、32–35、68–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-06%20%E5%A4%9C%E6%9B%B4%E3%81%91%E3%81%AE%E6%99%AF%E8%89%B2.txt#L11)；[OC19_Rin_X1 · 112-07 届いていたもの (東雲絵名).txt L86–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-07%20%E5%B1%8A%E3%81%84%E3%81%A6%E3%81%84%E3%81%9F%E3%82%82%E3%81%AE%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L86)；[OC19_Rin_E5 · 0175_東雲絵名_R4 諦めたくないから (event_14).txt L74–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0175_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E8%AB%A6%E3%82%81%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84%E3%81%8B%E3%82%89%20%28event_14%29.txt#L74)

**情感比较正文：** [OC19_Rin_E3 · 0914_東雲絵名_RB Happy Birthday！！2024.txt L154–158](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0914_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812024.txt#L154)；[OC19_Rin_E4 · 0399_鏡音リン (N25)_R4 届けたい歌声 (event_53).txt L49–53](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0399_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E5%B1%8A%E3%81%91%E3%81%9F%E3%81%84%E6%AD%8C%E5%A3%B0%20%28event_53%29.txt#L49)；[OC19_Rin_E5 · 0175_東雲絵名_R4 諦めたくないから (event_14).txt L74–78](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0175_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E8%AB%A6%E3%82%81%E3%81%9F%E3%81%8F%E3%81%AA%E3%81%84%E3%81%8B%E3%82%89%20%28event_14%29.txt#L74)；[OC19_Rin_G2 · 112-06 目指したい場所 (東雲絵名).txt L11–16、21–23、25–26、28–32、35、38、40、42、50–51、57–63、106–124、127–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-06%20%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%9F%E3%81%84%E5%A0%B4%E6%89%80%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L11)；[OC19_Rin_G1 · 014-06 一番大切なことは.txt L79、82–85、88–95、101–103、109、120–123、125–127、130–136](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/014%20%E6%BA%80%E3%81%9F%E3%81%95%E3%82%8C%E3%81%AA%E3%81%84%E3%83%9A%E3%82%A4%E3%83%AB%E3%82%AB%E3%83%A9%E3%83%BC%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/014-06%20%E4%B8%80%E7%95%AA%E5%A4%A7%E5%88%87%E3%81%AA%E3%81%93%E3%81%A8%E3%81%AF.txt#L79)；[OC19_Rin_G5 · 127-05 向き合わなきゃ.txt L6–8、37–39、43、45–46、55–64、66–74、77–83、85–90、96–98、100–102、120–122、131–134、141、146–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-05%20%E5%90%91%E3%81%8D%E5%90%88%E3%82%8F%E3%81%AA%E3%81%8D%E3%82%83.txt#L6)；[OC19_Rin_E1 · 0837_鏡音リン (N25)_R2 セカイを描いて、彩って (event_116).txt L12–16](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0837_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R2%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%82%92%E6%8F%8F%E3%81%84%E3%81%A6%E3%80%81%E5%BD%A9%E3%81%A3%E3%81%A6%20%28event_116%29.txt#L12)；[OC19_Rin_E2 · 054-01 お花見をしよう.txt L45–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/054%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%A1%9C%E3%80%81%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E6%83%B3%E3%81%84%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-N25%29/054-01%20%E3%81%8A%E8%8A%B1%E8%A6%8B%E3%82%92%E3%81%97%E3%82%88%E3%81%86.txt#L45)；[OC19_Rin_X2 · 0837_鏡音リン (N25)_R2 セカイを描いて、彩って (event_116).txt L14–46](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0837_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R2%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%82%92%E6%8F%8F%E3%81%84%E3%81%A6%E3%80%81%E5%BD%A9%E3%81%A3%E3%81%A6%20%28event_116%29.txt#L14)；[OC19_Rin_G3 · 112-07 届いていたもの (東雲絵名).txt L5–10、22–28、37–45、48–56、66–70、73–76、78–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-07%20%E5%B1%8A%E3%81%84%E3%81%A6%E3%81%84%E3%81%9F%E3%82%82%E3%81%AE%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L5)

### OC19_MEIKO · MEIKO

**成长细分判断：** 39改变守望方法并被0310本人明确回顾，150实际联络支持持续但非独占关系修复。

**情感细分判断：** 本人明确MEIKOにだから相談できること，持续朋友安全/守望痛苦交托与回报，定位有可区别的稳定信任。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|3,3,3,3|
|细档|3.5,4,2.5,1,2|3.5,3.5,3.5,3.75|

原粗档指数成长/情感 59.33 / 75.00；细分未归一原指数 68.08 / 89.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_MEIKO_G1 · 039-06 どうかその目で.txt L7–21、26–28、33–39、42、45–52、55–72、78–79、85、91、93–95、101、107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/039%20%E3%83%9C%E3%82%AF%E3%81%AE%E3%81%82%E3%81%97%E3%81%82%E3%81%A8%20%E3%82%AD%E3%83%9F%E3%81%AE%E3%82%86%E3%81%8F%E3%81%95%E3%81%8D%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/039-06%20%E3%81%A9%E3%81%86%E3%81%8B%E3%81%9D%E3%81%AE%E7%9B%AE%E3%81%A7.txt#L7)；[OC19_MEIKO_G2 · 150-06 怖い.txt L25–31、44–45、51、59–72、87–92、98–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-06%20%E6%80%96%E3%81%84.txt#L25)；[OC19_MEIKO_X1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L90–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L90)；[OC19_MEIKO_X2 · 1449_東雲絵名_R4 あの頃言えなかったこと (event_214).txt L19–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1449_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E3%81%82%E3%81%AE%E9%A0%83%E8%A8%80%E3%81%88%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E3%81%93%E3%81%A8%20%28event_214%29.txt#L19)；[OC19_MEIKO_E6 · talk_event_116.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L88)；[OC19_MEIKO_E2 · 210-07 茜色のひととき.txt L46–50](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/210%20%E8%A4%AA%E3%81%9B%E3%81%AA%E3%81%84%E4%BB%8A%E3%82%92%E3%80%81%E5%BD%A9%E3%81%A3%E3%81%A6%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/210-07%20%E8%8C%9C%E8%89%B2%E3%81%AE%E3%81%B2%E3%81%A8%E3%81%A8%E3%81%8D.txt#L46)

**情感比较正文：** [OC19_MEIKO_X1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L90–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L90)；[OC19_MEIKO_E2 · 210-07 茜色のひととき.txt L46–50](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/210%20%E8%A4%AA%E3%81%9B%E3%81%AA%E3%81%84%E4%BB%8A%E3%82%92%E3%80%81%E5%BD%A9%E3%81%A3%E3%81%A6%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/210-07%20%E8%8C%9C%E8%89%B2%E3%81%AE%E3%81%B2%E3%81%A8%E3%81%A8%E3%81%8D.txt#L46)；[OC19_MEIKO_G2 · 150-06 怖い.txt L25–31、44–45、51、59–72、87–92、98–99](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-06%20%E6%80%96%E3%81%84.txt#L25)；[OC19_MEIKO_G1 · 039-06 どうかその目で.txt L7–21、26–28、33–39、42、45–52、55–72、78–79、85、91、93–95、101、107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/039%20%E3%83%9C%E3%82%AF%E3%81%AE%E3%81%82%E3%81%97%E3%81%82%E3%81%A8%20%E3%82%AD%E3%83%9F%E3%81%AE%E3%82%86%E3%81%8F%E3%81%95%E3%81%8D%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/039-06%20%E3%81%A9%E3%81%86%E3%81%8B%E3%81%9D%E3%81%AE%E7%9B%AE%E3%81%A7.txt#L7)；[OC19_MEIKO_E6 · talk_event_116.txt L88–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_116.txt#L88)；[OC19_MEIKO_X2 · 1449_東雲絵名_R4 あの頃言えなかったこと (event_214).txt L19–39](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1449_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E3%81%82%E3%81%AE%E9%A0%83%E8%A8%80%E3%81%88%E3%81%AA%E3%81%8B%E3%81%A3%E3%81%9F%E3%81%93%E3%81%A8%20%28event_214%29.txt#L19)；[OC19_MEIKO_E4 · talk_event_218.txt L386–390](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_218.txt#L386)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)

### OC19_Len · 镜音连

**成长细分判断：** 父亲也痛苦的追问与197用擅长的画辨世界都有实际被回想采用，核心创作/家人认识直接。

**情感细分判断：** 具体讲父作差距与表达他人世界压力并亲自教画，彼此回应围绕持续艺术自我而非一般点子求助。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,9,2,1,2|2,3,3,2|
|细档|3.5,9,2.5,1,2|2.25,3.5,3.5,2.75|

原粗档指数成长/情感 66.83 / 62.50；细分未归一原指数 75.58 / 75.00。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_Len_G1 · 112-07 届いていたもの (東雲絵名).txt L12–22、24–28、36–38、42–46、48–54、58–62、65–68、73–78、85–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-07%20%E5%B1%8A%E3%81%84%E3%81%A6%E3%81%84%E3%81%9F%E3%82%82%E3%81%AE%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L12)；[OC19_Len_G2 · 127-04 憂鬱な朝.txt L7–8、25–28、70–72、81–84、86–88、91–94、96–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-04%20%E6%86%82%E9%AC%B1%E3%81%AA%E6%9C%9D.txt#L7)；[OC19_Len_G3 · 127-05 向き合わなきゃ.txt L6–8、30–32、37–42、45–47、49–54、56–74、76–79、82–85、92–94、99–101、120–125、141、146–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-05%20%E5%90%91%E3%81%8D%E5%90%88%E3%82%8F%E3%81%AA%E3%81%8D%E3%82%83.txt#L6)；[OC19_Len_G4 · 127-06 夜更けの景色.txt L12–21、32–35、68–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-06%20%E5%A4%9C%E6%9B%B4%E3%81%91%E3%81%AE%E6%99%AF%E8%89%B2.txt#L12)；[OC19_Len_G5 · 127-07 感じ取る想いは.txt L29、34–35、37、43–45、64–68、74–76、93–95](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-07%20%E6%84%9F%E3%81%98%E5%8F%96%E3%82%8B%E6%83%B3%E3%81%84%E3%81%AF.txt#L29)；[OC19_Len_X1 · 197-04 私だから感じ取れること.txt L44–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/197%20%E6%82%AA%E5%A4%A2%E3%81%AE%E5%BA%AD%E3%82%92%E6%AD%8C%E3%81%84%E6%98%8E%E3%81%8B%E3%81%97%E3%81%A6%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/197-04%20%E7%A7%81%E3%81%A0%E3%81%8B%E3%82%89%E6%84%9F%E3%81%98%E5%8F%96%E3%82%8C%E3%82%8B%E3%81%93%E3%81%A8.txt#L44)；[OC19_Len_X2 · 197-05 二次審査へ.txt L33–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/197%20%E6%82%AA%E5%A4%A2%E3%81%AE%E5%BA%AD%E3%82%92%E6%AD%8C%E3%81%84%E6%98%8E%E3%81%8B%E3%81%97%E3%81%A6%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/197-05%20%E4%BA%8C%E6%AC%A1%E5%AF%A9%E6%9F%BB%E3%81%B8.txt#L33)；[OC19_Len_X3 · 1187_東雲絵名_R4 いつも、あなたが (event_170).txt L98–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1187_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E3%81%84%E3%81%A4%E3%82%82%E3%80%81%E3%81%82%E3%81%AA%E3%81%9F%E3%81%8C%20%28event_170%29.txt#L98)；[OC19_Len_E2 · 1347_鏡音レン (N25)_R4 指さす先にある道 (event_197).txt L58–62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1347_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R4%20%E6%8C%87%E3%81%95%E3%81%99%E5%85%88%E3%81%AB%E3%81%82%E3%82%8B%E9%81%93%20%28event_197%29.txt#L58)

**情感比较正文：** [OC19_Len_E1 · 0839_鏡音レン_RB Happy Anniversary！！2023.txt L18–22](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0839_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L18)；[OC19_Len_E2 · 1347_鏡音レン (N25)_R4 指さす先にある道 (event_197).txt L58–62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1347_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R4%20%E6%8C%87%E3%81%95%E3%81%99%E5%85%88%E3%81%AB%E3%81%82%E3%82%8B%E9%81%93%20%28event_197%29.txt#L58)；[OC19_Len_G2 · 127-04 憂鬱な朝.txt L7–8、25–28、70–72、81–84、86–88、91–94、96–101](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-04%20%E6%86%82%E9%AC%B1%E3%81%AA%E6%9C%9D.txt#L7)；[OC19_Len_G3 · 127-05 向き合わなきゃ.txt L6–8、30–32、37–42、45–47、49–54、56–74、76–79、82–85、92–94、99–101、120–125、141、146–147](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/127%20Knowing%20the%20Unseen%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/127-05%20%E5%90%91%E3%81%8D%E5%90%88%E3%82%8F%E3%81%AA%E3%81%8D%E3%82%83.txt#L6)；[OC19_Len_X1 · 197-04 私だから感じ取れること.txt L44–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/197%20%E6%82%AA%E5%A4%A2%E3%81%AE%E5%BA%AD%E3%82%92%E6%AD%8C%E3%81%84%E6%98%8E%E3%81%8B%E3%81%97%E3%81%A6%20%28Mix_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/197-04%20%E7%A7%81%E3%81%A0%E3%81%8B%E3%82%89%E6%84%9F%E3%81%98%E5%8F%96%E3%82%8C%E3%82%8B%E3%81%93%E3%81%A8.txt#L44)；[OC19_Len_E4 · 0839_鏡音レン_RB Happy Anniversary！！2023.txt L68–72](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0839_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812023.txt#L68)；[OC19_Len_E5 · 1347_鏡音レン (N25)_R4 指さす先にある道 (event_197).txt L58–62](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/1347_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R4%20%E6%8C%87%E3%81%95%E3%81%99%E5%85%88%E3%81%AB%E3%81%82%E3%82%8B%E9%81%93%20%28event_197%29.txt#L58)；[OC19_Len_X3 · 1187_東雲絵名_R4 いつも、あなたが (event_170).txt L98–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1187_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E3%81%84%E3%81%A4%E3%82%82%E3%80%81%E3%81%82%E3%81%AA%E3%81%9F%E3%81%8C%20%28event_170%29.txt#L98)；[OC19_Len_G1 · 112-07 届いていたもの (東雲絵名).txt L12–22、24–28、36–38、42–46、48–54、58–62、65–68、73–78、85–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-07%20%E5%B1%8A%E3%81%84%E3%81%A6%E3%81%84%E3%81%9F%E3%82%82%E3%81%AE%20%28%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29.txt#L12)

### OC19_KAITO · KAITO

**成长细分判断：** 184从最讨厌之事重看作品意图，实际课题思路有具名确认，系统技法教育仍雪平。

**情感细分判断：** 持续感谢并按喜好赠咖啡/冰淇淋，本人深层父亲痛苦没向他同样说出，合作侧重具体课题。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,1,2|3,2,3,2|
|细档|3.5,7,2.25,1,2|3.25,2.5,3.25,2.5|

原粗档指数成长/情感 63.83 / 62.50；细分未归一原指数 71.33 / 71.88。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_KAITO_F1 · 0836_東雲絵名_R3 憂いの午後 (event_116).txt L100–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0836_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R3%20%E6%86%82%E3%81%84%E3%81%AE%E5%8D%88%E5%BE%8C%20%28event_116%29.txt#L100)；[OC19_KAITO_F2 · 1272_東雲絵名_R4 己の境界を超えて (event_184).txt L112–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1272_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E5%B7%B1%E3%81%AE%E5%A2%83%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%A6%20%28event_184%29.txt#L112)；[OC19_KAITO_X3 · 184-04 何気ないヒント.txt L52–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/184%20Colors%20of%20Pure%20Sense%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/184-04%20%E4%BD%95%E6%B0%97%E3%81%AA%E3%81%84%E3%83%92%E3%83%B3%E3%83%88.txt#L52)；[OC19_KAITO_X1 · 184-05 私が嫌なこと.txt L64–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/184%20Colors%20of%20Pure%20Sense%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/184-05%20%E7%A7%81%E3%81%8C%E5%AB%8C%E3%81%AA%E3%81%93%E3%81%A8.txt#L64)；[OC19_KAITO_X2 · 184-06 自分の武器.txt L14–76](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/184%20Colors%20of%20Pure%20Sense%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/184-06%20%E8%87%AA%E5%88%86%E3%81%AE%E6%AD%A6%E5%99%A8.txt#L14)；[OC19_KAITO_X5 · 1272_東雲絵名_R4 己の境界を超えて (event_184).txt L133–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1272_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E5%B7%B1%E3%81%AE%E5%A2%83%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%A6%20%28event_184%29.txt#L133)；[OC19_Miku_X1 · 1275_初音ミク (N25)_R3 お礼のアイス (event_184).txt L111–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1275_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R3%20%E3%81%8A%E7%A4%BC%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B9%20%28event_184%29.txt#L111)；[OC19_Luka_X1 · 1338_KAITO_RB Happy Anniversary！！2026.txt L19–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L19)

**情感比较正文：** [OC19_KAITO_F2 · 1272_東雲絵名_R4 己の境界を超えて (event_184).txt L112–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1272_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E5%B7%B1%E3%81%AE%E5%A2%83%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%A6%20%28event_184%29.txt#L112)；[OC19_KAITO_X5 · 1272_東雲絵名_R4 己の境界を超えて (event_184).txt L133–163](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1272_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E5%B7%B1%E3%81%AE%E5%A2%83%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%A6%20%28event_184%29.txt#L133)；[OC19_Miku_X1 · 1275_初音ミク (N25)_R3 お礼のアイス (event_184).txt L111–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1275_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R3%20%E3%81%8A%E7%A4%BC%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B9%20%28event_184%29.txt#L111)；[OC19_KAITO_F1 · 0836_東雲絵名_R3 憂いの午後 (event_116).txt L100–120](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/0836_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R3%20%E6%86%82%E3%81%84%E3%81%AE%E5%8D%88%E5%BE%8C%20%28event_116%29.txt#L100)；[OC19_KAITO_X3 · 184-04 何気ないヒント.txt L52–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/184%20Colors%20of%20Pure%20Sense%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/184-04%20%E4%BD%95%E6%B0%97%E3%81%AA%E3%81%84%E3%83%92%E3%83%B3%E3%83%88.txt#L52)；[OC19_Luka_X1 · 1338_KAITO_RB Happy Anniversary！！2026.txt L19–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L19)

### OC19_Miku · 初音未来

**成长细分判断：** 14推动面对伙伴歌曲与相见是关键支持，恢复绘画仍有奏/瑞希；184主导建议不归她。

**情感细分判断：** 真实讲虚无/否定与父亲打击，连续买涂色本怕其寂寞、具体关心主动，但显式定位仍师友。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,2|2,3,3,2|
|细档|3.25,4,2.25,1,2|2.25,3.5,3.5,2.5|

原粗档指数成长/情感 59.33 / 62.50；细分未归一原指数 63.71 / 73.44。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_Miku_G1 · 014-06 一番大切なことは.txt L46–48、83–85、90–92、97–103、126–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/014%20%E6%BA%80%E3%81%9F%E3%81%95%E3%82%8C%E3%81%AA%E3%81%84%E3%83%9A%E3%82%A4%E3%83%AB%E3%82%AB%E3%83%A9%E3%83%BC%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/014-06%20%E4%B8%80%E7%95%AA%E5%A4%A7%E5%88%87%E3%81%AA%E3%81%93%E3%81%A8%E3%81%AF.txt#L46)；[OC19_Miku_G2 · 068-04 ボク達をつないだ絵.txt L49–55、58–63、73–75、78–85、146、152–153、155–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L49)；[OC19_Miku_G3 · 068-08 ボクが進みたい道は.txt L15、17、196–198、201、207–210、213–215、221–226、233–237](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-08%20%E3%83%9C%E3%82%AF%E3%81%8C%E9%80%B2%E3%81%BF%E3%81%9F%E3%81%84%E9%81%93%E3%81%AF.txt#L15)；[OC19_Miku_X4 · 014-07 認められたいなら.txt L29–61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/014%20%E6%BA%80%E3%81%9F%E3%81%95%E3%82%8C%E3%81%AA%E3%81%84%E3%83%9A%E3%82%A4%E3%83%AB%E3%82%AB%E3%83%A9%E3%83%BC%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/014-07%20%E8%AA%8D%E3%82%81%E3%82%89%E3%82%8C%E3%81%9F%E3%81%84%E3%81%AA%E3%82%89.txt#L29)；[OC19_KAITO_F2 · 1272_東雲絵名_R4 己の境界を超えて (event_184).txt L112–129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1272_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E5%B7%B1%E3%81%AE%E5%A2%83%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%A6%20%28event_184%29.txt#L112)；[OC19_KAITO_X3 · 184-04 何気ないヒント.txt L52–69](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/184%20Colors%20of%20Pure%20Sense%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/184-04%20%E4%BD%95%E6%B0%97%E3%81%AA%E3%81%84%E3%83%92%E3%83%B3%E3%83%88.txt#L52)；[OC19_Miku_X1 · 1275_初音ミク (N25)_R3 お礼のアイス (event_184).txt L111–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1275_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R3%20%E3%81%8A%E7%A4%BC%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B9%20%28event_184%29.txt#L111)

**情感比较正文：** [OC19_Miku_X1 · 1275_初音ミク (N25)_R3 お礼のアイス (event_184).txt L111–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1275_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF%20%28N25%29_R3%20%E3%81%8A%E7%A4%BC%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B9%20%28event_184%29.txt#L111)；[OC19_Miku_X3 · talk_grade2.txt L1913–1925](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1913)；[OC19_Miku_G1 · 014-06 一番大切なことは.txt L46–48、83–85、90–92、97–103、126–135](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/014%20%E6%BA%80%E3%81%9F%E3%81%95%E3%82%8C%E3%81%AA%E3%81%84%E3%83%9A%E3%82%A4%E3%83%AB%E3%82%AB%E3%83%A9%E3%83%BC%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/014-06%20%E4%B8%80%E7%95%AA%E5%A4%A7%E5%88%87%E3%81%AA%E3%81%93%E3%81%A8%E3%81%AF.txt#L46)；[OC19_Miku_G2 · 068-04 ボク達をつないだ絵.txt L49–55、58–63、73–75、78–85、146、152–153、155–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L49)；[OC19_Miku_E1 · talk_grade2.txt L1913–1917](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L1913)；[OC19_Miku_E3 · 009-03 カウントダウンパーティー！.txt L52–56](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/009%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%A4%E3%83%BC%EF%BC%81%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-VBS%29/009-03%20%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%83%80%E3%82%A6%E3%83%B3%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%EF%BC%81.txt#L52)

### OC19_Luka · 巡音流歌

**成长细分判断：** 39陪伴使能说观点、生日方法实际奏效，仍具体改变而非对奏的核心教学移植。

**情感细分判断：** 父亲/无法被接纳真实听见，蛋糕和教学有回报；部分甜食分享有处理剩食实务动机。 068本人答应讲入团前经历并说当时精神濒临极限，39另有实际陪伴，信任细分3.50；回忆中内心逐句不当口述。 再比较主动回应和本人关系定位：部分蛋糕分享兼有处理剩食的实务动机、教画有尚未兑现部分，持续投入取3.25；未见像连的艺术认可或Miku的孤独牵挂那样更明确个人角色意义，定位取2.25。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,7,2,1,2|2,3,3,2|
|细档|2.25,7,2.5,1,2|2.25,3.5,3.25,2.25|

原粗档指数成长/情感 51.33 / 62.50；细分未归一原指数 56.96 / 70.31。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC19_Luka_G1 · 068-04 ボク達をつないだ絵.txt L50–52、54–56、60–64、69–71、75–77、85–87、146、152–153、155–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L50)；[OC19_Luka_G2 · 068-06 【K】との出会い.txt L7–8、12–14、126–127、129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-06%20%E3%80%90K%E3%80%91%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L7)；[OC19_Luka_E1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L127–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L127)；[OC19_MEIKO_X1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L90–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L90)；[OC19_Luka_X1 · 1338_KAITO_RB Happy Anniversary！！2026.txt L19–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L19)；[OC19_Luka_X2 · talk_event_150.txt L204–214](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_150.txt#L204)；[OC18_Luka_X2 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L19–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L19)

**情感比较正文：** [OC19_Luka_E1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L127–131](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L127)；[OC19_Luka_X2 · talk_event_150.txt L204–214](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_150.txt#L204)；[OC19_Luka_G1 · 068-04 ボク達をつないだ絵.txt L50–52、54–56、60–64、69–71、75–77、85–87、146、152–153、155–157](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L50)；[OC19_Luka_G2 · 068-06 【K】との出会い.txt L7–8、12–14、126–127、129](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-06%20%E3%80%90K%E3%80%91%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84.txt#L7)；[OC19_MEIKO_X1 · 0310_MEIKO (N25)_R3 正しさの天秤 (event_39).txt L90–130](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/0310_MEIKO%20%28N25%29_R3%20%E6%AD%A3%E3%81%97%E3%81%95%E3%81%AE%E5%A4%A9%E7%A7%A4%20%28event_39%29.txt#L90)；[OC18_Luka_X2 · 1103_巡音ルカ_RB Happy Anniversary！！2025.txt L19–42](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/1103_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812025.txt#L19)；[OC19_Len_X3 · 1187_東雲絵名_R4 いつも、あなたが (event_170).txt L98–145](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1187_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E3%81%84%E3%81%A4%E3%82%82%E3%80%81%E3%81%82%E3%81%AA%E3%81%9F%E3%81%8C%20%28event_170%29.txt#L98)

## 晓山瑞希

|VS|成长顺位|情感顺位|综合顺位|相对成长|相对情感|综合原平均（1:1）|综合相对分（最高100）|对下一位的判断限制|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|MEIKO|1|1|1|100.00|100.00|100.00|100.00|研究估计；来源有依据，仍需独立复评|
|巡音流歌|2|3|2|86.61|96.55|91.58|91.58|研究估计；来源有依据，仍需独立复评|
|镜音连|4|2|3|62.04|98.28|80.16|80.16|研究估计；来源有依据，仍需独立复评|
|KAITO|3|6|4|68.52|62.07|65.29|65.29|研究估计；来源有依据，仍需独立复评|
|初音未来|6|4|5|34.29|87.93|61.11|61.11|研究估计；来源有依据，仍需独立复评|
|镜音铃|5|5|6|35.91|72.41|54.16|54.16|该组末位；仍为研究估计|

### OC20_MEIKO · MEIKO

**成长细分判断：** 112面对逃避、145/150提醒在危机被回想并参与重连，核心自我作用跨阶段且本人愿面对有明确归因。

**情感细分判断：** 未来支持承诺与话被带入真实面对自己及危机回想，连续回报按其兴趣选择，长期核心困境的关系意义最强。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,7,2,2,2|3,3,3,3|
|细档|3.5,7,2.75,2,2|3.5,3.5,3.75,3.75|

原粗档指数成长/情感 67.17 / 75.00；细分未归一原指数 77.17 / 90.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_MEIKO_G1 · 150-06 怖い.txt L10–12、22–31、44–45、51、61–67、69–72、90–92](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-06%20%E6%80%96%E3%81%84.txt#L10)；[OC20_MEIKO_G2 · 150-07 逃走.txt L28–30、58、61–66](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-07%20%E9%80%83%E8%B5%B0.txt#L28)；[OC20_MEIKO_G3 · 150-08 友達.txt L24–27、40–46、55–57、96、101–102、107、110–114、119–123、131–134](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-08%20%E5%8F%8B%E9%81%94.txt#L24)；[OC20_MEIKO_G4 · 019-05 最後の心霊スポット.txt L8–20、26–27、32–34、37–39、45、63–65、69–71、92–94](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/019%20%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%B9%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/019-05%20%E6%9C%80%E5%BE%8C%E3%81%AE%E5%BF%83%E9%9C%8A%E3%82%B9%E3%83%9D%E3%83%83%E3%83%88.txt#L8)；[OC20_MEIKO_G5 · 112-04 逃げた、その先は (暁山瑞希).txt L16–18、45–47、56–98、110–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-04%20%E9%80%83%E3%81%92%E3%81%9F%E3%80%81%E3%81%9D%E3%81%AE%E5%85%88%E3%81%AF%20%28%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29.txt#L16)；[OC20_MEIKO_G6 · 112-05 やさしい言葉 (暁山瑞希).txt L7–13、16–18、21–31、37–44、47–49、51–54、57–59、62–64、73–76、81–83、92–99、107–110、112–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-05%20%E3%82%84%E3%81%95%E3%81%97%E3%81%84%E8%A8%80%E8%91%89%20%28%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29.txt#L7)；[OC20_MEIKO_G7 · 145-02 見守る者達.txt L7、16、22–23、29–43、45–52、55–61、64–66、72、74–76、84–88、100–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-02%20%E8%A6%8B%E5%AE%88%E3%82%8B%E8%80%85%E9%81%94.txt#L7)；[OC20_MEIKO_G8 · 145-03 友の願い.txt L17–19、55–57、60–62、84–86、90–98、110–114、116–118、137–138、144、151、153–154、157、160、166–167、179–182、189、194、199](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-03%20%E5%8F%8B%E3%81%AE%E9%A1%98%E3%81%84.txt#L17)；[OC20_MEIKO_G9 · 019-06 同じ桜なのに.txt L12–32、38、43–44、46、73–75、81–83、90–91、97、108–110、113–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/019%20%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88%E3%83%BB%E3%83%87%E3%82%A3%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%B9%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/019-06%20%E5%90%8C%E3%81%98%E6%A1%9C%E3%81%AA%E3%81%AE%E3%81%AB.txt#L12)；[OC20_MEIKO_X1 · talk_event_210.txt L43–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_210.txt#L43)

**情感比较正文：** [OC20_MEIKO_G5 · 112-04 逃げた、その先は (暁山瑞希).txt L16–18、45–47、56–98、110–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-04%20%E9%80%83%E3%81%92%E3%81%9F%E3%80%81%E3%81%9D%E3%81%AE%E5%85%88%E3%81%AF%20%28%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29.txt#L16)；[OC20_MEIKO_G6 · 112-05 やさしい言葉 (暁山瑞希).txt L7–13、16–18、21–31、37–44、47–49、51–54、57–59、62–64、73–76、81–83、92–99、107–110、112–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/112%20%E6%B0%B4%E5%BA%95%E3%81%AB%E5%BD%B1%E3%82%92%E6%8E%A2%E3%81%97%E3%81%A6%20%28N25_WL%29/112-05%20%E3%82%84%E3%81%95%E3%81%97%E3%81%84%E8%A8%80%E8%91%89%20%28%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29.txt#L7)；[OC20_MEIKO_X1 · talk_event_210.txt L43–57](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_210.txt#L43)；[OC19_Rin_E2 · 054-01 お花見をしよう.txt L45–49](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/054%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%81%AE%E6%A1%9C%E3%80%81%E3%81%A4%E3%81%AA%E3%81%8C%E3%82%8B%E6%83%B3%E3%81%84%20%28Mix_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF-N25%29/054-01%20%E3%81%8A%E8%8A%B1%E8%A6%8B%E3%82%92%E3%81%97%E3%82%88%E3%81%86.txt#L45)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)；[OC20_MEIKO_G8 · 145-03 友の願い.txt L17–19、55–57、60–62、84–86、90–98、110–114、116–118、137–138、144、151、153–154、157、160、166–167、179–182、189、194、199](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-03%20%E5%8F%8B%E3%81%AE%E9%A1%98%E3%81%84.txt#L17)；[OC20_MEIKO_G3 · 150-08 友達.txt L24–27、40–46、55–57、96、101–102、107、110–114、119–123、131–134](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/150%20%E5%82%B7%E3%81%A0%E3%82%89%E3%81%91%E3%81%AE%E6%89%8B%E3%81%A7%E3%80%81%E7%A7%81%E9%81%94%E3%81%AF%20%28N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D%29/150-08%20%E5%8F%8B%E9%81%94.txt#L24)

### OC20_Luka · 巡音流歌

**成长细分判断：** 093将退路经验化为支持伙伴的行动方法，重要自我/关系因果直接。

**情感细分判断：** 本人把少有人理解真实真冬的她当同边、赠吊坠后特意修复，持续依靠与主动关心充分。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,2,1,1|3,3,3,3|
|细档|3.5,4,2.5,1,1|3.5,3.5,3.5,3.5|

原粗档指数成长/情感 58.08 / 75.00；细分未归一原指数 66.83 / 87.50。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_Luka_G1 · 093-02 自分らしくいられるように.txt L14–16、18–20、31–56、58–60、73–75、87–89、101–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-02%20%E8%87%AA%E5%88%86%E3%82%89%E3%81%97%E3%81%8F%E3%81%84%E3%82%89%E3%82%8C%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB.txt#L14)；[OC20_Luka_G2 · 093-06 ボクの方法.txt L7–9、14–17、19–31、33–50、52–53、56–68、71、86–88、98–100、107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-06%20%E3%83%9C%E3%82%AF%E3%81%AE%E6%96%B9%E6%B3%95.txt#L7)；[OC20_Luka_G3 · 093-08 怖いけど、それでも.txt L24–26、39–41、45–50、58–73、75–77、79–81](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-08%20%E6%80%96%E3%81%84%E3%81%91%E3%81%A9%E3%80%81%E3%81%9D%E3%82%8C%E3%81%A7%E3%82%82.txt#L24)；[OC20_Luka_G4 · 068-02 姉からの贈り物.txt L19–21、30–64、124–126、156–158、162–164](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-02%20%E5%A7%89%E3%81%8B%E3%82%89%E3%81%AE%E8%B4%88%E3%82%8A%E7%89%A9.txt#L19)；[OC20_Luka_G5 · 068-04 ボク達をつないだ絵.txt L17–19、27、33–34、37–40、50–52、54–56、62–64、69–71、75–78、85–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L17)；[OC20_Luka_G6 · 068-08 ボクが進みたい道は.txt L74–76、91–93、100–112、136–138、167、180–182、187–189、220–225、227–229、237、240–241、243–247](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-08%20%E3%83%9C%E3%82%AF%E3%81%8C%E9%80%B2%E3%81%BF%E3%81%9F%E3%81%84%E9%81%93%E3%81%AF.txt#L74)；[OC20_Luka_E5 · 0638_巡音ルカ (N25)_R4 考えかたを変えて (event_93).txt L124–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0638_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28N25%29_R4%20%E8%80%83%E3%81%88%E3%81%8B%E3%81%9F%E3%82%92%E5%A4%89%E3%81%88%E3%81%A6%20%28event_93%29.txt#L124)

**情感比较正文：** [OC20_Luka_E5 · 0638_巡音ルカ (N25)_R4 考えかたを変えて (event_93).txt L124–128](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0638_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28N25%29_R4%20%E8%80%83%E3%81%88%E3%81%8B%E3%81%9F%E3%82%92%E5%A4%89%E3%81%88%E3%81%A6%20%28event_93%29.txt#L124)；[OC20_Luka_X1 · talk_event_068.txt L80–89](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_068.txt#L80)；[OC20_Luka_E2 · 0638_巡音ルカ (N25)_R4 考えかたを変えて (event_93).txt L114–118](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/24%20VS_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB/0638_%E5%B7%A1%E9%9F%B3%E3%83%AB%E3%82%AB%20%28N25%29_R4%20%E8%80%83%E3%81%88%E3%81%8B%E3%81%9F%E3%82%92%E5%A4%89%E3%81%88%E3%81%A6%20%28event_93%29.txt#L114)；[OC20_Luka_G1 · 093-02 自分らしくいられるように.txt L14–16、18–20、31–56、58–60、73–75、87–89、101–107](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-02%20%E8%87%AA%E5%88%86%E3%82%89%E3%81%97%E3%81%8F%E3%81%84%E3%82%89%E3%82%8C%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB.txt#L14)；[OC20_Luka_G2 · 093-06 ボクの方法.txt L7–9、14–17、19–31、33–50、52–53、56–68、71、86–88、98–100、107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-06%20%E3%83%9C%E3%82%AF%E3%81%AE%E6%96%B9%E6%B3%95.txt#L7)；[OC20_Luka_G4 · 068-02 姉からの贈り物.txt L19–21、30–64、124–126、156–158、162–164](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-02%20%E5%A7%89%E3%81%8B%E3%82%89%E3%81%AE%E8%B4%88%E3%82%8A%E7%89%A9.txt#L19)；[OC20_Luka_G5 · 068-04 ボク達をつないだ絵.txt L17–19、27、33–34、37–40、50–52、54–56、62–64、69–71、75–78、85–87](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L17)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)；[OC20_Luka_E4 · talk_event_100.txt L59–63](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_100.txt#L59)

### OC20_Len · 镜音连

**成长细分判断：** 缎带祝愿后本人明确有干劲去行动，核心退路解释主要Luka，K2因果保持。

**情感细分判断：** 本人明确少有人认真共忧伤、定位连的温柔，蛋糕/玩偶实际个人回应；理解深但行动引路主要Luka。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|2,4,2,0,1|3,3,3,3|
|细档|2.25,4,2.5,0,1|3.5,3.5,3.5,3.75|

原粗档指数成长/情感 42.25 / 75.00；细分未归一原指数 47.88 / 89.06。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_Len_G1 · 093-06 ボクの方法.txt L7–13、16–22、28–30、32–42、45–47、49–51、86–88、98–100、107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-06%20%E3%83%9C%E3%82%AF%E3%81%AE%E6%96%B9%E6%B3%95.txt#L7)；[OC20_Len_X1 · 0639_鏡音レン (N25)_R3 リボンに込めた思いやり (event_93).txt L131–174](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0639_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R3%20%E3%83%AA%E3%83%9C%E3%83%B3%E3%81%AB%E8%BE%BC%E3%82%81%E3%81%9F%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%20%28event_93%29.txt#L131)；[OC20_Len_X3 · 0639_鏡音レン (N25)_R3 リボンに込めた思いやり (event_93).txt L174–193](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0639_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R3%20%E3%83%AA%E3%83%9C%E3%83%B3%E3%81%AB%E8%BE%BC%E3%82%81%E3%81%9F%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%20%28event_93%29.txt#L174)

**情感比较正文：** [OC20_Len_X1 · 0639_鏡音レン (N25)_R3 リボンに込めた思いやり (event_93).txt L131–174](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0639_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R3%20%E3%83%AA%E3%83%9C%E3%83%B3%E3%81%AB%E8%BE%BC%E3%82%81%E3%81%9F%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%20%28event_93%29.txt#L131)；[OC20_Len_X3 · 0639_鏡音レン (N25)_R3 リボンに込めた思いやり (event_93).txt L174–193](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0639_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R3%20%E3%83%AA%E3%83%9C%E3%83%B3%E3%81%AB%E8%BE%BC%E3%82%81%E3%81%9F%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%20%28event_93%29.txt#L174)；[OC20_Len_G1 · 093-06 ボクの方法.txt L7–13、16–22、28–30、32–42、45–47、49–51、86–88、98–100、107–111](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/093%20%E3%83%9C%E3%82%AF%E9%81%94%E3%81%AE%E7%94%9F%E5%AD%98%E9%80%83%E8%B5%B0%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/093-06%20%E3%83%9C%E3%82%AF%E3%81%AE%E6%96%B9%E6%B3%95.txt#L7)；[OC20_Len_X2 · talk_grade2.txt L2001–2014](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade2.txt#L2001)；[OC20_Len_E7 · 0837_鏡音リン (N25)_R2 セカイを描いて、彩って (event_116).txt L105–109](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0837_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R2%20%E3%82%BB%E3%82%AB%E3%82%A4%E3%82%92%E6%8F%8F%E3%81%84%E3%81%A6%E3%80%81%E5%BD%A9%E3%81%A3%E3%81%A6%20%28event_116%29.txt#L105)

### OC20_KAITO · KAITO

**成长细分判断：** 145选路提醒被本人回想并参与准备行动，结果遭暴露，仍无个别重大结果归因。

**情感细分判断：** 本人想邀其同赴会、定饮料和庆生多为具体意向，深层自身秘密尚未真正向其交托。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|3,4,1,0,1|2,2,2,2|
|细档|3.25,4,1,0,1|2.25,2.25,2.25,2.25|

原粗档指数成长/情感 49.75 / 50.00；细分未归一原指数 52.88 / 56.25。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_KAITO_G1 · 145-02 見守る者達.txt L22–23、29、32–38、42–52、56–61、64、74–83、87–101、114–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-02%20%E8%A6%8B%E5%AE%88%E3%82%8B%E8%80%85%E9%81%94.txt#L22)；[OC20_KAITO_G2 · 145-03 友の願い.txt L17–19、55–57、60–62、84–86、90–98、110–114、116–118、137–138、144、149–151、153、160、166–167、179–182、189、194、199](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-03%20%E5%8F%8B%E3%81%AE%E9%A1%98%E3%81%84.txt#L17)；[OC20_KAITO_X1 · 1432_暁山瑞希_R4 重なる想いと過去 (event_211).txt L33–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/1432_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R4%20%E9%87%8D%E3%81%AA%E3%82%8B%E6%83%B3%E3%81%84%E3%81%A8%E9%81%8E%E5%8E%BB%20%28event_211%29.txt#L33)；[OC20_KAITO_X2 · 1429_天馬咲希_R4 あの日の諦め (event_211).txt L104–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1429_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E8%AB%A6%E3%82%81%20%28event_211%29.txt#L104)

**情感比较正文：** [OC20_KAITO_E2 · 211-07 待ち遠しい未来.txt L111–115](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/211%20%E5%90%9B%E3%81%AE%E9%9A%A3%E3%80%81%E5%90%9B%E3%81%A8%E8%A6%8B%E3%82%8B%E6%98%8E%E6%97%A5%20%28Mix_WL%29/211-07%20%E5%BE%85%E3%81%A1%E9%81%A0%E3%81%97%E3%81%84%E6%9C%AA%E6%9D%A5.txt#L111)；[OC20_KAITO_G1 · 145-02 見守る者達.txt L22–23、29、32–38、42–52、56–61、64、74–83、87–101、114–116](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/145%20%E8%8D%8A%E6%A3%98%E3%81%AE%E9%81%93%E3%81%AF%E4%BD%95%E5%87%A6%E3%81%B8%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/145-02%20%E8%A6%8B%E5%AE%88%E3%82%8B%E8%80%85%E9%81%94.txt#L22)；[OC20_KAITO_X1 · 1432_暁山瑞希_R4 重なる想いと過去 (event_211).txt L33–80](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/1432_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R4%20%E9%87%8D%E3%81%AA%E3%82%8B%E6%83%B3%E3%81%84%E3%81%A8%E9%81%8E%E5%8E%BB%20%28event_211%29.txt#L33)；[OC20_KAITO_X2 · 1429_天馬咲希_R4 あの日の諦め (event_211).txt L104–126](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1429_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E3%81%82%E3%81%AE%E6%97%A5%E3%81%AE%E8%AB%A6%E3%82%81%20%28event_211%29.txt#L104)；[OC19_Luka_X1 · 1338_KAITO_RB Happy Anniversary！！2026.txt L19–60](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/26%20VS_KAITO/1338_KAITO_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L19)

### OC20_Miku · 初音未来

**成长细分判断：** 0285察觉并保密痛苦是具体支持，没确认独立核心行动改变。

**情感细分判断：** 本人要求不要告诉别人、专为她开心备聚会，脆弱保密与持续实际回报结合。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,1|3,3,3,2|
|细档|1.25,0,1.25,1,1|3.25,3.5,3.5,2.5|

原粗档指数成长/情感 22.08 / 68.75；细分未归一原指数 26.46 / 79.69。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_Miku_G1 · 068-02 姉からの贈り物.txt L19–24、30–54、57–65、124–126、156–158、162–164](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-02%20%E5%A7%89%E3%81%8B%E3%82%89%E3%81%AE%E8%B4%88%E3%82%8A%E7%89%A9.txt#L19)；[OC20_Miku_G2 · 068-04 ボク達をつないだ絵.txt L17–19、27、33–34、37–40、49–55、58–60、73–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L17)；[OC20_Miku_G3 · 068-08 ボクが進みたい道は.txt L74–76、91–93、100–112、136–138、167、180–182、187–189、201、207–208、220–229、235–237、240–241、243–247](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-08%20%E3%83%9C%E3%82%AF%E3%81%8C%E9%80%B2%E3%81%BF%E3%81%9F%E3%81%84%E9%81%93%E3%81%AF.txt#L74)；[OC20_Miku_X1 · 0285_暁山瑞希_R4 ひとときの安息 (event_35).txt L154–196](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/0285_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R4%20%E3%81%B2%E3%81%A8%E3%81%A8%E3%81%8D%E3%81%AE%E5%AE%89%E6%81%AF%20%28event_35%29.txt#L154)；[OC20_Miku_X2 · 1451_初音ミク_RB Happy Anniversary！！2026.txt L14–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1451_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L14)；[OC20_Miku_E6 · talk_grade1.txt L8281–8285](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L8281)

**情感比较正文：** [OC20_Miku_X1 · 0285_暁山瑞希_R4 ひとときの安息 (event_35).txt L154–196](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/0285_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R4%20%E3%81%B2%E3%81%A8%E3%81%A8%E3%81%8D%E3%81%AE%E5%AE%89%E6%81%AF%20%28event_35%29.txt#L154)；[OC20_Miku_X2 · 1451_初音ミク_RB Happy Anniversary！！2026.txt L14–70](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1451_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_RB%20Happy%20Anniversary%EF%BC%81%EF%BC%812026.txt#L14)；[OC20_Miku_G3 · 068-08 ボクが進みたい道は.txt L74–76、91–93、100–112、136–138、167、180–182、187–189、201、207–208、220–229、235–237、240–241、243–247](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-08%20%E3%83%9C%E3%82%AF%E3%81%8C%E9%80%B2%E3%81%BF%E3%81%9F%E3%81%84%E9%81%93%E3%81%AF.txt#L74)；[OC20_Miku_G1 · 068-02 姉からの贈り物.txt L19–24、30–54、57–65、124–126、156–158、162–164](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-02%20%E5%A7%89%E3%81%8B%E3%82%89%E3%81%AE%E8%B4%88%E3%82%8A%E7%89%A9.txt#L19)；[OC20_Miku_G2 · 068-04 ボク達をつないだ絵.txt L17–19、27、33–34、37–40、49–55、58–60、73–85](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/068%20%E3%81%9D%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%80%81%E3%83%AA%E3%83%9C%E3%83%B3%E3%82%92%E7%B5%90%E3%82%93%E3%81%A7%20%28N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C%29/068-04%20%E3%83%9C%E3%82%AF%E9%81%94%E3%82%92%E3%81%A4%E3%81%AA%E3%81%84%E3%81%A0%E7%B5%B5.txt#L17)；[OC20_Miku_E6 · talk_grade1.txt L8281–8285](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_grade1.txt#L8281)；[OC17_Miku_X6 · 084-07 みんなへのプレゼント.txt L66–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/084%20%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E9%A6%99%E3%82%8A%E3%81%AF%E6%80%9D%E3%81%84%E5%87%BA%E3%81%A8%E5%85%B1%E3%81%AB%20%28Mix_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C%29/084-07%20%E3%81%BF%E3%82%93%E3%81%AA%E3%81%B8%E3%81%AE%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88.txt#L66)

### OC20_Rin · 镜音铃

**成长细分判断：** 本人要求留下聊天、谢照看奏是实際支持，未把铃内心设想缓解当已实现K2。

**情感细分判断：** 本人具体讲人际弄僵后又回避，胸针/发饰/奖章回应持续，未完整托付核心秘密。

|量尺|成长K,C,S,T,B|情感表达/袒露/投入/定位|
|---|---|---|
|原整数档|1,0,1,1,2|2,2,3,2|
|细档|1.25,0,1.25,1,2|2.25,2.25,3.5,2.5|

原粗档指数成长/情感 23.33 / 56.25；细分未归一原指数 27.71 / 65.63。各维原理由与具体方向限制见粗档附录；下列是本组用于比较的已核窗口集合，不表示每个链接单独证明全部细档。

**成长比较正文：** [OC20_Rin_X1 · 1143_暁山瑞希_R2 “みんな”で打ち上げ (event_161).txt L154–187](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/1143_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R2%20%E2%80%9C%E3%81%BF%E3%82%93%E3%81%AA%E2%80%9D%E3%81%A7%E6%89%93%E3%81%A1%E4%B8%8A%E3%81%92%20%28event_161%29.txt#L154)；[OC20_Rin_F1 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L48–61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L48)；[OC20_Rin_Y7 · 0286_鏡音リン (N25)_R4 アルバムのあの子 (event_35).txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0286_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%82%A2%E3%83%AB%E3%83%90%E3%83%A0%E3%81%AE%E3%81%82%E3%81%AE%E5%AD%90%20%28event_35%29.txt#L35)；[OC20_Rin_Y8 · 035-03 いつかの記憶.txt L80–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-03%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E8%A8%98%E6%86%B6.txt#L80)

**情感比较正文：** [OC20_Rin_X1 · 1143_暁山瑞希_R2 “みんな”で打ち上げ (event_161).txt L154–187](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/20%20N25_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C/1143_%E6%9A%81%E5%B1%B1%E7%91%9E%E5%B8%8C_R2%20%E2%80%9C%E3%81%BF%E3%82%93%E3%81%AA%E2%80%9D%E3%81%A7%E6%89%93%E3%81%A1%E4%B8%8A%E3%81%92%20%28event_161%29.txt#L154)；[OC20_Rin_F1 · 1099_鏡音リン (N25)_R4 おめかしは難しい (event_155).txt L48–61](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/1099_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%81%8A%E3%82%81%E3%81%8B%E3%81%97%E3%81%AF%E9%9B%A3%E3%81%97%E3%81%84%20%28event_155%29.txt#L48)；[OC20_Rin_Y8 · 035-03 いつかの記憶.txt L80–104](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/035%20%E7%81%AF%E3%81%AE%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%20%28N25_%E6%9C%9D%E6%AF%94%E5%A5%88%E3%81%BE%E3%81%B5%E3%82%86%29/035-03%20%E3%81%84%E3%81%A4%E3%81%8B%E3%81%AE%E8%A8%98%E6%86%B6.txt#L80)；[OC20_Rin_Y7 · 0286_鏡音リン (N25)_R4 アルバムのあの子 (event_35).txt L35–79](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/22%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3/0286_%E9%8F%A1%E9%9F%B3%E3%83%AA%E3%83%B3%20%28N25%29_R4%20%E3%82%A2%E3%83%AB%E3%83%90%E3%83%A0%E3%81%AE%E3%81%82%E3%81%AE%E5%AD%90%20%28event_35%29.txt#L35)；[OC20_Rin_Y2 · talk_event_014.txt L72–86](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/area/talk_event_014.txt#L72)；[OC20_Rin_E1 · 0639_鏡音レン (N25)_R3 リボンに込めた思いやり (event_93).txt L175–179](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/23%20VS_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3/0639_%E9%8F%A1%E9%9F%B3%E3%83%AC%E3%83%B3%20%28N25%29_R3%20%E3%83%AA%E3%83%9C%E3%83%B3%E3%81%AB%E8%BE%BC%E3%82%81%E3%81%9F%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A%20%28event_93%29.txt#L175)

## 原47个同分组合如何拉开

以下逐组给出细档排序，并逐对列出使原同分发生差异的编码。细档理由与正文在上方关系ID，原并列比较理由仍见tie-review.md。跨维优势用明确编码和等权公式体现，不另增加综合排序权重。

### F01 · 星乃一歌 · 成长 · 原指数 68.42

深评顺序：镜音连 ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ 镜音铃|K 3.25 对 3。分别见 OC01_Len、OC01_Rin 的具体判读及来源。|

### F02 · 星乃一歌 · 成长 · 原指数 77.67

深评顺序：KAITO ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 巡音流歌|K 3.5 对 3.25；S 3.5 对 3.25。分别见 OC01_KAITO、OC01_Luka 的具体判读及来源。|

### F03 · 星乃一歌 · 情感 · 原指数 68.75

深评顺序：巡音流歌 ＞ KAITO ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ KAITO|表达 3.25 对 3.5；投入 3.5 对 3.25；定位 2.5 对 2.25。分别见 OC01_Luka、OC01_KAITO 的具体判读及来源。|
|巡音流歌 ＞ 镜音铃|袒露 3.5 对 3.25；定位 2.5 对 2.25。分别见 OC01_Luka、OC01_Rin 的具体判读及来源。|
|KAITO ＞ 镜音铃|表达 3.5 对 3.25；袒露 3.5 对 3.25；投入 3.25 对 3.5。分别见 OC01_KAITO、OC01_Rin 的具体判读及来源。|

### F04 · 星乃一歌 · 情感 · 原指数 56.25

深评顺序：MEIKO ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 镜音连|袒露 3.5 对 3.25；投入 2.25 对 2；定位 2.5 对 2.25。分别见 OC01_MEIKO、OC01_Len 的具体判读及来源。|

### F05 · 天马咲希 · 情感 · 原指数 50.00

深评顺序：MEIKO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 初音未来|袒露 2.5 对 2.25；投入 2 对 2.25；定位 2.5 对 2.25。分别见 OC02_MEIKO、OC02_Miku 的具体判读及来源。|

### F06 · 天马咲希 · 情感 · 原指数 56.25

深评顺序：镜音连 ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ KAITO|袒露 3.5 对 3.25；投入 2.5 对 2.25。分别见 OC02_Len、OC02_KAITO 的具体判读及来源。|

### F07 · 望月穗波 · 情感 · 原指数 50.00

深评顺序：初音未来 ＞ 镜音铃 ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|初音未来 ＞ 镜音铃|定位 2.5 对 2.25。分别见 OC03_Miku、OC03_Rin 的具体判读及来源。|
|初音未来 ＞ KAITO|投入 2.25 对 2；定位 2.5 对 2.25。分别见 OC03_Miku、OC03_KAITO 的具体判读及来源。|
|镜音铃 ＞ KAITO|投入 2.25 对 2。分别见 OC03_Rin、OC03_KAITO 的具体判读及来源。|

### F08 · 望月穗波 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 镜音连|表达 2.5 对 2.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC03_Luka、OC03_Len 的具体判读及来源。|

### F09 · 日野森志步 · 成长 · 原指数 50.17

深评顺序：初音未来 ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|初音未来 ＞ 巡音流歌|K 2.25 对 2。分别见 OC04_Miku、OC04_Luka 的具体判读及来源。|

### F10 · 日野森志步 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 初音未来 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 初音未来|投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC04_Luka、OC04_Miku 的具体判读及来源。|
|巡音流歌 ＞ 镜音连|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.25。分别见 OC04_Luka、OC04_Len 的具体判读及来源。|
|初音未来 ＞ 镜音连|袒露 3.5 对 3.25；定位 2.5 对 2.25。分别见 OC04_Miku、OC04_Len 的具体判读及来源。|

### F11 · 日野森志步 · 情感 · 原指数 50.00

深评顺序：MEIKO ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ KAITO|袒露 2.5 对 2.25；投入 2 对 2.25；定位 2.5 对 2.25。分别见 OC04_MEIKO、OC04_KAITO 的具体判读及来源。|

### F12 · 花里实乃理 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 初音未来 ＞ 镜音铃 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 初音未来|投入 2.5 对 2.25。分别见 OC05_Luka、OC05_Miku 的具体判读及来源。|
|巡音流歌 ＞ 镜音铃|袒露 3.5 对 3.25；定位 2.75 对 2.5。分别见 OC05_Luka、OC05_Rin 的具体判读及来源。|
|巡音流歌 ＞ 镜音连|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC05_Luka、OC05_Len 的具体判读及来源。|
|初音未来 ＞ 镜音铃|袒露 3.5 对 3.25；投入 2.25 对 2.5；定位 2.75 对 2.5。分别见 OC05_Miku、OC05_Rin 的具体判读及来源。|
|初音未来 ＞ 镜音连|袒露 3.5 对 3.25；定位 2.75 对 2.5。分别见 OC05_Miku、OC05_Len 的具体判读及来源。|
|镜音铃 ＞ 镜音连|投入 2.5 对 2.25。分别见 OC05_Rin、OC05_Len 的具体判读及来源。|

### F13 · 桐谷遥 · 成长 · 原指数 63.83

深评顺序：巡音流歌 ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ KAITO|K 3.5 对 3.25；S 2.5 对 2.25。分别见 OC06_Luka、OC06_KAITO 的具体判读及来源。|

### F14 · 桐谷遥 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ MEIKO ＞ 镜音连 ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ MEIKO|定位 2.75 对 2.5。分别见 OC06_Luka、OC06_MEIKO 的具体判读及来源。|
|巡音流歌 ＞ 镜音连|袒露 3.5 对 2.25；投入 2.5 对 3.5；定位 2.75 对 2.5。分别见 OC06_Luka、OC06_Len 的具体判读及来源。|
|巡音流歌 ＞ 初音未来|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC06_Luka、OC06_Miku 的具体判读及来源。|
|MEIKO ＞ 镜音连|袒露 3.5 对 2.25；投入 2.5 对 3.5。分别见 OC06_MEIKO、OC06_Len 的具体判读及来源。|
|MEIKO ＞ 初音未来|袒露 3.5 对 3.25；投入 2.5 对 2.25。分别见 OC06_MEIKO、OC06_Miku 的具体判读及来源。|
|镜音连 ＞ 初音未来|袒露 2.25 对 3.25；投入 3.5 对 2.25。分别见 OC06_Len、OC06_Miku 的具体判读及来源。|

### F15 · 桐谷遥 · 情感 · 原指数 50.00

深评顺序：镜音铃 ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|镜音铃 ＞ KAITO|袒露 2.5 对 3.5；投入 2.5 对 1.25。分别见 OC06_Rin、OC06_KAITO 的具体判读及来源。|

### F16 · 桃井爱莉 · 成长 · 原指数 46.83

深评顺序：MEIKO ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 巡音流歌|S 2.5 对 2.25。分别见 OC07_MEIKO、OC07_Luka 的具体判读及来源。|

### F17 · 桃井爱莉 · 情感 · 原指数 56.25

深评顺序：镜音连 ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ 初音未来|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC07_Len、OC07_Miku 的具体判读及来源。|

### F18 · 桃井爱莉 · 情感 · 原指数 62.50

深评顺序：KAITO ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ MEIKO|表达 3.5 对 2.25；袒露 3.5 对 3.25；投入 2.5 对 3.5；定位 2.75 对 2.5。分别见 OC07_KAITO、OC07_MEIKO 的具体判读及来源。|

### F19 · 日野森雫 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 初音未来 ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 初音未来|投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC08_Luka、OC08_Miku 的具体判读及来源。|
|巡音流歌 ＞ MEIKO|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC08_Luka、OC08_MEIKO 的具体判读及来源。|
|初音未来 ＞ MEIKO|袒露 3.5 对 3.25。分别见 OC08_Miku、OC08_MEIKO 的具体判读及来源。|

### F20 · 日野森雫 · 情感 · 原指数 50.00

深评顺序：KAITO ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 镜音连|袒露 2.5 对 2.25；投入 2.25 对 2.5；定位 2.5 对 2.25。分别见 OC08_KAITO、OC08_Len 的具体判读及来源。|

### F21 · 小豆泽心羽 · 情感 · 原指数 56.25

深评顺序：MEIKO ＞ 初音未来 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 初音未来|投入 2.75 对 2.5。分别见 OC09_MEIKO、OC09_Miku 的具体判读及来源。|
|MEIKO ＞ 镜音连|袒露 3.5 对 3.25；投入 2.75 对 2.25；定位 2.75 对 2.5。分别见 OC09_MEIKO、OC09_Len 的具体判读及来源。|
|初音未来 ＞ 镜音连|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC09_Miku、OC09_Len 的具体判读及来源。|

### F22 · 小豆泽心羽 · 情感 · 原指数 50.00

深评顺序：巡音流歌 ＞ 镜音铃 ＞ KAITO

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 镜音铃|袒露 2.5 对 2.25。分别见 OC09_Luka、OC09_Rin 的具体判读及来源。|
|巡音流歌 ＞ KAITO|袒露 2.5 对 2.25；投入 2.5 对 2.25。分别见 OC09_Luka、OC09_KAITO 的具体判读及来源。|
|镜音铃 ＞ KAITO|投入 2.5 对 2.25。分别见 OC09_Rin、OC09_KAITO 的具体判读及来源。|

### F23 · 白石杏 · 成长 · 原指数 46.83

深评顺序：巡音流歌 ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ MEIKO|S 2.5 对 2.25。分别见 OC10_Luka、OC10_MEIKO 的具体判读及来源。|

### F24 · 白石杏 · 情感 · 原指数 62.50

深评顺序：初音未来 ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|初音未来 ＞ 镜音铃|袒露 3.5 对 3.25；定位 2.75 对 2.5。分别见 OC10_Miku、OC10_Rin 的具体判读及来源。|

### F25 · 白石杏 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ MEIKO|袒露 3.5 对 2.25；投入 2.5 对 3.5。分别见 OC10_Luka、OC10_MEIKO 的具体判读及来源。|

### F26 · 东云彰人 · 情感 · 原指数 43.75

深评顺序：KAITO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 初音未来|表达 2.25 对 1；投入 1.25 对 2.25。分别见 OC11_KAITO、OC11_Miku 的具体判读及来源。|

### F27 · 东云彰人 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 镜音铃|表达 3.5 对 2.25；袒露 2.5 对 3.5；投入 1.25 对 2.5；定位 3.75 对 2.5。分别见 OC11_Luka、OC11_Rin 的具体判读及来源。|

### F28 · 青柳冬弥 · 成长 · 原指数 68.08

深评顺序：KAITO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 初音未来|S 2.5 对 2.25。分别见 OC12_KAITO、OC12_Miku 的具体判读及来源。|

### F29 · 青柳冬弥 · 成长 · 原指数 46.83

深评顺序：镜音铃 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|镜音铃 ＞ 镜音连|K 2.25 对 2。分别见 OC12_Rin、OC12_Len 的具体判读及来源。|

### F30 · 青柳冬弥 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 初音未来 ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 初音未来|投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC12_Luka、OC12_Miku 的具体判读及来源。|
|巡音流歌 ＞ 镜音铃|袒露 3.5 对 3.25；投入 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC12_Luka、OC12_Rin 的具体判读及来源。|
|初音未来 ＞ 镜音铃|袒露 3.5 对 3.25。分别见 OC12_Miku、OC12_Rin 的具体判读及来源。|

### F31 · 天马司 · 情感 · 原指数 50.00

深评顺序：初音未来 ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|初音未来 ＞ MEIKO|定位 2.5 对 2.25。分别见 OC13_Miku、OC13_MEIKO 的具体判读及来源。|

### F32 · 天马司 · 情感 · 原指数 56.25

深评顺序：巡音流歌 ＞ 镜音铃

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 镜音铃|袒露 2.5 对 2.25；定位 2.75 对 2.5。分别见 OC13_Luka、OC13_Rin 的具体判读及来源。|

### F33 · 天马司 · 情感 · 原指数 62.50

深评顺序：KAITO ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 镜音连|表达 3.5 对 3.25；定位 2.75 对 2.5。分别见 OC13_KAITO、OC13_Len 的具体判读及来源。|

### F34 · 凤笑梦 · 成长 · 原指数 70.17

深评顺序：镜音连 ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ MEIKO|S 2.5 对 2.25。分别见 OC14_Len、OC14_MEIKO 的具体判读及来源。|

### F35 · 凤笑梦 · 情感 · 原指数 56.25

深评顺序：KAITO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 初音未来|袒露 3.5 对 2.25；投入 2.5 对 3.25；定位 2.75 对 2.5。分别见 OC14_KAITO、OC14_Miku 的具体判读及来源。|

### F36 · 凤笑梦 · 情感 · 原指数 50.00

深评顺序：镜音铃 ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|镜音铃 ＞ 巡音流歌|投入 2.25 对 2。分别见 OC14_Rin、OC14_Luka 的具体判读及来源。|

### F37 · 草薙宁宁 · 情感 · 原指数 50.00

深评顺序：镜音连 ＞ KAITO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ KAITO|袒露 2.5 对 2.25。分别见 OC15_Len、OC15_KAITO 的具体判读及来源。|
|镜音连 ＞ 初音未来|袒露 2.5 对 2.25；定位 2.5 对 2.25。分别见 OC15_Len、OC15_Miku 的具体判读及来源。|
|KAITO ＞ 初音未来|定位 2.5 对 2.25。分别见 OC15_KAITO、OC15_Miku 的具体判读及来源。|

### F38 · 神代类 · 情感 · 原指数 68.75

深评顺序：巡音流歌 ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|巡音流歌 ＞ 初音未来|投入 2.5 对 3.25；定位 3.75 对 2.5。分别见 OC16_Luka、OC16_Miku 的具体判读及来源。|

### F39 · 神代类 · 情感 · 原指数 75.00

深评顺序：KAITO ＞ MEIKO

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ MEIKO|定位 3.75 对 3.5。分别见 OC16_KAITO、OC16_MEIKO 的具体判读及来源。|

### F40 · 宵崎奏 · 成长 · 原指数 63.83

深评顺序：镜音铃 ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|镜音铃 ＞ 巡音流歌|S 2.5 对 2.25。分别见 OC17_Rin、OC17_Luka 的具体判读及来源。|

### F41 · 宵崎奏 · 情感 · 原指数 56.25

深评顺序：KAITO ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 镜音连|袒露 3.75 对 2.25；投入 2.25 对 3.5。分别见 OC17_KAITO、OC17_Len 的具体判读及来源。|

### F42 · 朝比奈真冬 · 成长 · 原指数 63.83

深评顺序：镜音铃 ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|镜音铃 ＞ 镜音连|S 2.5 对 2.25。分别见 OC18_Rin、OC18_Len 的具体判读及来源。|

### F43 · 朝比奈真冬 · 情感 · 原指数 56.25

深评顺序：KAITO ＞ 镜音连

|比较|细档差异及排序依据|
|---|---|
|KAITO ＞ 镜音连|袒露 3.75 对 2.5；投入 2.5 对 3.5。分别见 OC18_KAITO、OC18_Len 的具体判读及来源。|

### F44 · 朝比奈真冬 · 情感 · 原指数 50.00

深评顺序：MEIKO ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 巡音流歌|投入 2.5 对 2.25。分别见 OC18_MEIKO、OC18_Luka 的具体判读及来源。|

### F45 · 东云绘名 · 成长 · 原指数 59.33

深评顺序：MEIKO ＞ 初音未来

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 初音未来|K 3.5 对 3.25；S 2.5 对 2.25。分别见 OC19_MEIKO、OC19_Miku 的具体判读及来源。|

### F46 · 东云绘名 · 情感 · 原指数 62.50

深评顺序：镜音连 ＞ 初音未来 ＞ KAITO ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|镜音连 ＞ 初音未来|定位 2.75 对 2.5。分别见 OC19_Len、OC19_Miku 的具体判读及来源。|
|镜音连 ＞ KAITO|表达 2.25 对 3.25；袒露 3.5 对 2.5；投入 3.5 对 3.25；定位 2.75 对 2.5。分别见 OC19_Len、OC19_KAITO 的具体判读及来源。|
|镜音连 ＞ 巡音流歌|投入 3.5 对 3.25；定位 2.75 对 2.25。分别见 OC19_Len、OC19_Luka 的具体判读及来源。|
|初音未来 ＞ KAITO|表达 2.25 对 3.25；袒露 3.5 对 2.5；投入 3.5 对 3.25。分别见 OC19_Miku、OC19_KAITO 的具体判读及来源。|
|初音未来 ＞ 巡音流歌|投入 3.5 对 3.25；定位 2.5 对 2.25。分别见 OC19_Miku、OC19_Luka 的具体判读及来源。|
|KAITO ＞ 巡音流歌|表达 3.25 对 2.25；袒露 2.5 对 3.5；定位 2.5 对 2.25。分别见 OC19_KAITO、OC19_Luka 的具体判读及来源。|

### F47 · 晓山瑞希 · 情感 · 原指数 75.00

深评顺序：MEIKO ＞ 镜音连 ＞ 巡音流歌

|比较|细档差异及排序依据|
|---|---|
|MEIKO ＞ 镜音连|投入 3.75 对 3.5。分别见 OC20_MEIKO、OC20_Len 的具体判读及来源。|
|MEIKO ＞ 巡音流歌|投入 3.75 对 3.5；定位 3.75 对 3.5。分别见 OC20_MEIKO、OC20_Luka 的具体判读及来源。|
|镜音连 ＞ 巡音流歌|定位 3.75 对 3.5。分别见 OC20_Len、OC20_Luka 的具体判读及来源。|
