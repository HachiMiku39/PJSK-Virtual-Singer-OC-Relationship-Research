# 日服最新剧情增量研究：2026-10-12

本轮接续2026-09-21的一歌试评，读取之后已发布的活动与卡牌剧情，最新至 **Stars Off Orbit（活动220）**。核心变化是：MEIKO对穗波的帮助出现清晰行动链；一歌与咲希的个人愿望和乐队共同方向仍有冲突，不能把既有职业选择写成已解决的成长终点。成长与情感两套评分暂保持原值，新增证据和限定分别记录。

[返回项目首页](../../README.md) · [来源与覆盖清单](manifest.json) · [24条证据及对照记录](evidence.json) · [抓取与复核工具](sync_stories.py)

## 范围与来源

|活动|日服开始时间（JST）|本轮正文|
|---|---|---|
|[218 Connect to SEKAI！](https://pjsk.moe/ja-jp/story/event/218/)|2026-09-25 20:00|2话|
|[219 Side by Side, Our Ways！](https://pjsk.moe/ja-jp/story/event/219/)|2026-09-30 15:00|8话|
|[220 Stars Off Orbit](https://pjsk.moe/ja-jp/story/event/220/)|2026-10-12 15:00|8话|

另读卡牌1475—1487共13张的前后篇，包括9月30日两张Bloom Festival卡、10月1日发布的遥生日卡，以及219、220相关卡。合计 **31份文本文件，18话活动＋26篇卡牌侧故事**。生日卡发行日、剧情中的生日日期与活动日期分别保存，不能混用。Stars Off Orbit已在日服上线，举办时间亦见[SEGA发布文转载](https://www.4gamer.net/games/476/G047609/20261009050/)。

日文来源固定为 ci-ke/ProjectSekai-story 的 `aa934ac00875eae6e89066292fe96c8bd9abb283`（2026-10-12更新）；日期与章节标识依据 Sekai-World/sekai-master-db-diff 的 `dd8126175c308435e73dd4c1c39066a6c64c37e5`。来源均为第三方托管，不是游戏官方正文发布站。未逐句对照游戏画面。

本轮实际访问pjsk.moe的公开资源镜像：218、219全部10话可取回，共712条TalkData，与固定文本的对白顺序和内容在忽略空白后全部一致。这说明两份文本相符，**不代表两个独立目击来源**。220目录可访问，但8话资源均返回HTTP 404；因此220正文与卡牌判读目前依据固定版本文本。manifest保存每份文本、主数据及可用镜像的SHA-256，不在仓库重发全文。

清单的`acquisition_status`与`review_status`是抓取器状态，下载不自动等于审读；本轮人工阅读范围以evidence.json中的`reviewed_source_ids`为准。已开始但资料缺失的章节必须留缺口，不能跳过后写成全覆盖。本轮所选区间没有缺失活动话数或卡牌文件；区域对话、特殊故事、MYSEKAI互动及历史空白仍未纳入。

## 1. 穗波与MEIKO：具体建议改变了谈话方式，结果仍开放

[220第3话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-03%20%E5%B9%BC%E9%A6%B4%E6%9F%93%E3%81%BF%E3%81%A8%E3%81%97%E3%81%A6.txt#L68)中，穗波已经注意到咲希可能隐瞒顾虑，并担心作为队长无法问到本心。MEIKO提出转换身份：作为从小认识的朋友表达关心，并把谈话放在一起游玩的延长线上。穗波感谢并决定去谈；[第4话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-04%20%E9%80%B1%E6%9C%AB%E3%83%87%E3%83%BC%E3%83%88%E3%81%AF%E7%A9%8F%E3%82%84%E3%81%8B%E3%81%AB.txt#L10)立即回想这条建议，承认此前把问题当成队长必须处理的事。

[第5话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-05%20%E6%98%9F%E9%99%8D%E3%82%8B%E5%A4%9C%E7%A9%BA%E3%81%AE%E4%B8%8B%E3%81%A7.txt#L48)中，穗波用自己的过去后悔和接纳承诺继续问。[第7话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-07%20%E6%9C%AC%E9%9F%B3.txt#L17)终于由咲希说出真正矛盾：她想在能看见观众脸、伸手可及的距离演奏，担心与伙伴追求更大场馆的方向相反。

N01支持本次行动改变的K2，核心关系理解的K3可作为进一步复核问题；是否独立于穗波既有温柔与勇气线，须回到历史材料比较后才调整C。N02另记录穗波主动请MEIKO听自己说的信任证据，不再算另一条成长线。

[第8话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-08%20%E6%98%9F%E3%80%85%E3%81%AF%E7%A9%BA%E3%81%AE%E6%9E%9C%E3%81%A6%E3%81%B8.txt#L65)仍是暂缓移籍、继续寻找共同道路；[穗波卡1483后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/03%20Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2/1483_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2_R4%20%E6%AE%8B%E3%81%95%E3%82%8C%E3%81%9F%E6%83%B3%E3%81%84%E3%82%92%20%28event_220%29.txt#L75)也继续忧虑。故不能把MEIKO的建议写成修好了乐队、带来移籍成功。[MEIKO卡1485后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/25%20VS_MEIKO/1485_MEIKO%20%28Ln%29_R4%20%E5%85%88%E8%BC%A9%E3%81%8B%E3%82%89%E3%81%AE%E3%82%A2%E3%83%89%E3%83%90%E3%82%A4%E3%82%B9%20%28event_220%29.txt#L79)中的KAITO愿意帮忙，但此处尚无对OC实施的行动，不能共享MEIKO的因果。

## 2. 一歌、咲希：优先乐队不是最终消除个人愿望

一歌的旧报告已经提示《Echo of a Prayer》结尾存在余波。新材料将这一限制具体化：[220第8话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/220%20Stars%20Off%20Orbit%20%28Ln_%E6%9C%9B%E6%9C%88%E7%A9%82%E6%B3%A2%29/220-08%20%E6%98%9F%E3%80%85%E3%81%AF%E7%A9%BA%E3%81%AE%E6%9E%9C%E3%81%A6%E3%81%B8.txt#L23)里志步追问她是否其实更想个人活动，一歌未当场回答。[一歌卡1484后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/1484_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E4%BB%8A%E3%81%AF%E3%81%9F%E3%81%A0%E3%80%81%E9%9A%A3%E3%81%AB%20%28event_220%29.txt#L118)里，她承认自己认真选择了优先乐队，却仍无言、自责并继续寻找以后该怎么办。

因此，保留212话中铃、连帮助梳理和一歌当时明确感谢的历史事实；K3、S2、C7等旧试评本轮不自动升降。但新增“决定仍受后续检验”的限定，不能把自主决定进一步夸大成稳定的人生结局，也不能反过来认定一歌已经反悔、铃连建议失败。[同卡前篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/01%20Ln_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C/1484_%E6%98%9F%E4%B9%83%E4%B8%80%E6%AD%8C_R4%20%E4%BB%8A%E3%81%AF%E3%81%9F%E3%81%A0%E3%80%81%E9%9A%A3%E3%81%AB%20%28event_220%29.txt#L33)Miku和铃陪热身、连提醒适度，属于已作决定之后的日常支持，不能倒写为Miku促成她拒绝个人事务所。

尤其不能漏掉9月30日[咲希Bloom Festival卡1475](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1475_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R4%20%E6%8A%BC%E3%81%97%E8%BE%BC%E3%82%81%E3%81%9F%E6%83%B3%E3%81%84.txt#L50)：连说明想念碎片的机制，两人陪她面对另一自我；咲希自己选择不抹消近距离演奏的愿望，同时仍想与伙伴一起。末尾明确未全部解决，之后220话延续这条矛盾。铃、连的机制说明、陪伴和安眠支持分别成立，但核心保留愿望的选择由咲希作出，不能只凭同行就归为两人独占的人生转折。

[咲希卡1486后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/02%20Ln_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C/1486_%E5%A4%A9%E9%A6%AC%E5%92%B2%E5%B8%8C_R3%20%E3%81%8D%E3%81%A3%E3%81%A8%E4%BB%8A%E5%BA%A6%E3%81%AF%E3%80%81%E3%81%BF%E3%82%93%E3%81%AA%E3%81%A7%20%28event_220%29.txt#L78)对Miku、Luka分享出游准备时没有说明移籍矛盾；读者看见的内心独白不能算成向她们袒露。[志步卡1487前篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/04%20Ln_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9/1487_%E6%97%A5%E9%87%8E%E6%A3%AE%E5%BF%97%E6%AD%A9_R2%20%E3%81%93%E3%81%AE%E5%A4%A2%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6%20%28event_220%29.txt#L9)中的竞技场是梦境，醒后的应援不证明她已达成职业成果。

## 3. 一歌与Miku：新重逢证据和形象边界

[218第2话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/218%20Connect%20to%20SEKAI%EF%BC%81%20%28Mix_WL%29/218-02%20%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%81%AF%E2%80%A6%E2%80%A6%EF%BC%81.txt#L20)新增一歌向大树SEKAI中无组合标注Miku表达想见、守约和今后交往的直接证据。同伴调侃她等待再会时像恋爱少女、说她很喜欢Miku，只作他人观察，不是恋爱确认，不能写成一歌自己宣告恋爱。此处Miku也不能未经说明替换成教室Miku。

[219第7话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/219%20Side%20by%20Side%2C%20Our%20Ways%EF%BC%81%20%28Mix_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/219-07%20%E6%9C%AA%E6%9D%A5%E3%81%AE%E8%87%AA%E5%88%86%E3%81%B8.txt#L56)对MMJ Miku的应援，一歌明确表示很受鼓舞，心羽也说想回应她的心意。两者是有对象的回应；但各人先表明自己的梦想，Miku随后祝福，所以不能额外算一条由她引发的梦想确立线。

218的新稳定SEKAI与[Miku Bloom Festival卡1476后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1476_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_R4%20%E5%85%B1%E3%81%AB%E6%AD%A9%E3%82%81%E3%82%8B%E6%9C%AA%E6%9D%A5.txt#L186)扩大了无组合标注VS与OC直接交流的条件。未来应单记VS形象再汇总基础身份。卡1476回看各组合过去节点，不能因为新卡发行而给旧回忆再次增加C或新的T时期。

## 4. 情感方向与其他角色的新候选

|对象|新材料|当前可支持的判断|
|---|---|---|
|心羽→VBS Miku、MEIKO|[卡1478后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/09%20VBS_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD/1478_%E5%B0%8F%E8%B1%86%E6%B2%A2%E3%81%93%E3%81%AF%E3%81%AD_R4%20%E9%A3%9B%E3%81%B3%E8%BE%BC%E3%82%93%E3%81%A0%E5%85%88%E3%81%AE%E5%A4%A7%E6%89%8B%E6%9F%84%20%28event_219%29.txt#L71)|主动带群体礼物、分享照片并咨询选片；有具体投入，非个人专属赠礼|
|类→WxS KAITO、连|[卡1479前篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/16%20WxS_%E7%A5%9E%E4%BB%A3%E9%A1%9E/1479_%E7%A5%9E%E4%BB%A3%E9%A1%9E_R4%20%E7%AC%91%E9%A1%94%E3%82%92%E7%94%9F%E3%81%BF%E5%87%BA%E3%81%99%E4%BB%95%E6%8E%9B%E3%81%91%20%28event_219%29.txt#L19)|主动邀请、介绍兴趣、感谢陪伴；不能把类的教学倒记成VS的创作指导|
|VS→绘名|[卡1480前篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/19%20N25_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D/1480_%E6%9D%B1%E9%9B%B2%E7%B5%B5%E5%90%8D_R4%20%E6%9C%AA%E6%9D%A5%E3%81%AB%E6%AE%8B%E3%81%99%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%20%28event_219%29.txt#L12)|Miku与连劝休息后，绘名决定购物约好友；是行动改变的K2候选，需合并旧自我照顾证据|
|绘名、瑞希→N25 Miku|[卡1476后篇回忆](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/21%20VS_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF/1476_%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF_R4%20%E5%85%B1%E3%81%AB%E6%AD%A9%E3%82%81%E3%82%8B%E6%9C%AA%E6%9D%A5.txt#L118)|照顾Miku的忧虑、一起整理头发；需追溯原场景去重，不以新发行当新发生|
|爱莉→MMJ铃、Luka|[卡1477后篇](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/07%20MMJ_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89/1477_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89_R4%20%E5%85%B1%E3%81%AB%E7%B6%B4%E3%82%8B%E6%80%9D%E3%81%84%E5%87%BA%E3%81%AF%20%28event_219%29.txt#L77)|分享休假、理想和猫周边，并求助布置；日常亲近不能自动形成K2+线|

[219第6话](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/event/219%20Side%20by%20Side%2C%20Our%20Ways%EF%BC%81%20%28Mix_%E6%A1%83%E4%BA%95%E6%84%9B%E8%8E%89%29/219-06%20%E3%81%9A%E3%81%A3%E3%81%A8%E3%80%81%E4%B8%80%E7%95%AA%E8%BF%91%E3%81%8F%E3%81%A7.txt#L32)中亲友、一番近处支持的强定位发生在爱莉与绘名之间，不能记到后来听故事的Miku。[遥生日卡1482末段](https://github.com/ci-ke/ProjectSekai-story/blob/aa934ac00875eae6e89066292fe96c8bd9abb283/story_jp/card/06%20MMJ_%E6%A1%90%E8%B0%B7%E9%81%A5/1482_%E6%A1%90%E8%B0%B7%E9%81%A5_RB%20Happy%20Birthday%EF%BC%81%EF%BC%812026.txt#L187)中的“你”和承诺指观众语境，不能猜成KAITO。以上对照与正向证据一起保存，避免只检索强烈词汇就错配对象。

这些记录还没有将其余19人补成V3完整评分，也没有因新证据中某位VS出场就把其他五位记0。一歌成长及情感表暂沿用9月21日试评；新证据不足以推翻Miku现有根基性定位，中间五位仍需同口径比较。

## 复核与继续研究

Python 3标准库即可运行；从仓库根目录执行，全文缓存放到仓库外的scratch目录。抓取器只按日服已发布时间获取资料；即使主数据提前载入未来内容，也不将未开始活动或未发布卡牌算入范围。

```sh
python3 research/latest/sync_stories.py --since 2026-09-21 --through 2026-10-12 \
  --master-ref dd8126175c308435e73dd4c1c39066a6c64c37e5 \
  --story-ref aa934ac00875eae6e89066292fe96c8bd9abb283 \
  --probe-mirror --cache-dir ../story-cache --output research/latest/manifest.json

python3 research/latest/sync_stories.py --verify --cache-dir ../story-cache \
  --output research/latest/manifest.json --evidence research/latest/evidence.json
```

复核检查31份文本的哈希、行数、10话镜像对白比对及每条引用的来源ID和行号范围；它不验证研究解释必然正确。再次抓取时会刷新抓取时间和源状态；固定版本文本可复核，活动镜像可能继续更新或暂缺。调查新时期用main解析成新的固定SHA并保留旧清单，不能覆盖后丢掉版本差异。

接续工作按以下顺序：

1. 重访220的8话资源，补游戏画面核对；跟进之后的Leo/need方向分歧，保留尚未解决的结果。
2. 回溯1475、1476的回忆原场景，合并重复证据；穗波—MEIKO先与主线、早期勇气线及其他五位贡献做完整V3比较。
3. 补213—217及其相关卡等本轮开始日期之前的空白；之后再按组合迁移其他19人的114组关系。旧v2.3至150的覆盖与一歌至212等的重点精读是不同范围。
4. 区域、特殊故事、MYSEKAI互动另建清单，再作长期情感与T判定；获取完成、正文读完、对象判断及同口径排名必须分别记录。

这份报告是已完成的增量研究及交接，不代表已完成全部历史剧情或已安排未来自动巡查。
