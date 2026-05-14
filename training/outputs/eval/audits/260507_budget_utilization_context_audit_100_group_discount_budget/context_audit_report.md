# Planner 预算利用型 Context 审计

- 样本数：100
- 失败数：0
- 耗时：34.664 秒
- contexts：`training/outputs/eval/v3_budget_utilization_context_audit_100_group_discount_budget/contexts.jsonl`
- errors：`training/outputs/eval/v3_budget_utilization_context_audit_100_group_discount_budget/errors.jsonl`

## 分布

- budget_level：`{"comfortable": 50, "premium": 50}`
- travel_days：`{"4": 40, "5": 40, "3": 20}`

## 核心可达性

| 分组 | 数量 | 可达target_min | 可达target_mid | 高价餐饮覆盖 | 高价体验覆盖 | 高价景点覆盖 | high ratio p50 | food max均值 | exp max均值 | scenic max均值 | hotel max均值 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | 100 | 78.0% | 72.0% | 73.0% | 94.0% | 100.0% | 1.17 | 347.7 | 331.8 | 287.3 | 958.0 |
| comfortable | 50 | 82.0% | 82.0% | 70.0% | 98.0% | 100.0% | 1.25 | 288.7 | 326.7 | 290.1 | 964.0 |
| premium | 50 | 74.0% | 62.0% | 76.0% | 90.0% | 100.0% | 1.11 | 406.7 | 336.9 | 284.5 | 952.0 |

说明：`high_budget_ratio` 是用当前候选池做粗上限估算，不是模型输出预算；用于判断候选是否足以支撑 95%-105% 的预算利用型样本。

## 最弱样本 Top20

| 城市 | 档位 | 预算 | 天数 | 人数 | 高配估算/预算 | 可达target_min | food max | exp max | scenic max | hotel max |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 昆明 | comfortable | 12900 | 5 | 2 | 0.73 | 否 | 125 | 283 | 280 | 300 |
| 大理 | premium | 18400 | 5 | 3 | 0.74 | 否 | 120 | 280 | 280 | 300 |
| 厦门 | comfortable | 11200 | 5 | 2 | 0.77 | 否 | 330 | 367 | 280 | 300 |
| 天津 | premium | 13600 | 3 | 3 | 0.80 | 否 | 501 | 226 | 180 | 500 |
| 桂林 | premium | 18700 | 5 | 4 | 0.80 | 否 | 113 | 280 | 280 | 300 |
| 大理 | comfortable | 10300 | 4 | 2 | 0.81 | 否 | 120 | 204 | 280 | 750 |
| 重庆 | comfortable | 22700 | 4 | 4 | 0.82 | 否 | 306 | 224 | 280 | 750 |
| 桂林 | premium | 23400 | 5 | 3 | 0.82 | 否 | 113 | 280 | 280 | 1200 |
| 桂林 | premium | 11000 | 5 | 2 | 0.82 | 否 | 113 | 280 | 280 | 500 |
| 大理 | comfortable | 20000 | 5 | 3 | 0.84 | 否 | 120 | 204 | 280 | 750 |
| 桂林 | premium | 11000 | 5 | 2 | 0.84 | 否 | 130 | 280 | 280 | 500 |
| 苏州 | premium | 17300 | 5 | 2 | 0.84 | 否 | 236 | 530 | 280 | 1250 |
| 张家界 | comfortable | 12700 | 5 | 2 | 0.85 | 否 | 80 | 292 | 280 | 750 |
| 西安 | premium | 10900 | 5 | 1 | 0.85 | 否 | 568 | 550 | 280 | 800 |
| 张家界 | comfortable | 12200 | 3 | 3 | 0.86 | 否 | 108 | 292 | 280 | 750 |
| 昆明 | premium | 28600 | 4 | 5 | 0.88 | 否 | 381 | 283 | 280 | 750 |
| 天津 | premium | 11500 | 4 | 2 | 0.89 | 否 | 501 | 226 | 180 | 1200 |
| 青岛 | premium | 7400 | 3 | 2 | 0.91 | 否 | 316 | 361 | 280 | 550 |
| 丽江 | comfortable | 17700 | 4 | 3 | 0.92 | 否 | 111 | 207 | 280 | 1200 |
| 丽江 | premium | 35800 | 5 | 5 | 0.94 | 否 | 107 | 280 | 280 | 1200 |

## 高价候选示例

### v3_request_005200 青岛 comfortable 10600元 ratio_high=1.74

- 餐饮：味语膳房(石老人)(316元,food_budget/精致餐厅) / 海派·悦庭(209元,food_budget_upgrade/品质餐厅) / 升海·本源海鲜海胆水饺(西海岸店)(120元,food_budget/精致餐厅) / 开海·红岛海鲜虾水饺店(八大关店)(115元,food_base/特色餐厅) / 双合园·海鲜水饺青岛菜(上清路店)(97元,food_base/简餐)
- 体验：青岛城阳开心麻花大剧院(361元,experience_budget_upgrade/演出) / 青岛大剧院(210元,experience_budget_upgrade/演出) / 青岛凤凰之声大剧院(192元,experience_budget_upgrade/演出) / 青岛红树林度假世界(180元,experience_budget_upgrade/温泉) / 小麦岛公园(180元,experience_budget_upgrade/夜游)
- 景点：青岛方特梦幻王国(280元,attraction_budget_upgrade/主题公园) / 青岛海底世界(280元,attraction_budget_upgrade/海洋馆) / 海合安·青岛极地海洋公园(280元,attraction_budget_upgrade/主题公园) / 青岛嘉年华主题乐园(280元,attraction_budget_upgrade/主题公园) / 小麦岛公园(180元,attraction_budget_upgrade/夜游)
- 酒店：青岛香格里拉大酒店(1250元,hotel_budget_upgrade/精品酒店) / 青岛海景花园大酒店(1250元,hotel_budget_upgrade/精品酒店) / 青岛鑫江温德姆酒店(1250元,hotel_budget_upgrade/精品酒店)

### v3_request_005201 成都 comfortable 10600元 ratio_high=1.12

- 餐饮：蜀宴赋(536元,food_budget/品质餐厅) / 柴门荟(中海环宇荟店)(480元,food_budget/创意菜) / 不二翠浪(233元,food_budget/创意菜) / 悦百味·品质川菜(悠方店)(160元,food_budget/品质餐厅) / 悦百味·品质川菜(优品道店)(140元,food_budget_upgrade/品质餐厅)
- 体验：成都金融城演艺中心(465元,experience_budget_upgrade/演出) / 成都高新中演大剧院(229元,experience_budget_upgrade/演出) / CH8绿树演艺中心(208元,experience_budget_upgrade/演出) / 百家班川剧团·非遗传承·戏曲变脸(春熙路·西部文化中心店)(200元,experience_budget_upgrade/演出) / 梨园会馆-非遗川剧变脸演出(文殊院店)(101元,experience_budget_upgrade/演出)
- 景点：灌县古城(180元,attraction_budget_upgrade/夜游) / 望江楼公园(180元,attraction_budget_upgrade/夜游) / 青城山景区(180元,attraction_budget_upgrade/夜游) / 安仁古镇(180元,attraction_budget_upgrade/温泉景区) / 都江堰熊猫谷(80元,attraction_budget_upgrade/夜游)
- 酒店：凡漫美宿酒店(成都青白江东站万达广场店)(550元,hotel_budget_upgrade/高端酒店) / 尚锦品酒店(建设路东郊记忆店)(550元,hotel_budget_upgrade/高端亲子酒店) / 如家睿柏·云酒店(成都青白江大弯中学店)(550元,hotel_budget_upgrade/高端酒店)

### v3_request_005205 张家界 comfortable 12700元 ratio_high=0.85

- 餐饮：醉湘亲私房菜(武陵源店)(80元,food_preference/本地菜) / 湘健土菜馆(78元,food_preference/特色餐厅) / 索溪山寨·湘西民间土菜(溪布街店)(76元,food_preference/本地菜) / 渔膳湾私房菜(71元,food_budget_upgrade/精致餐厅) / 索溪山寨·湘西民间土菜(标志门店)(70元,food_preference/本地菜)
- 体验：张家界千古情大剧院(292元,experience_budget_upgrade/剧场) / 张家界天门狐仙实景演出(266元,experience_budget_upgrade/演出) / 张家界《魅力湘西》演出(238元,experience_budget_upgrade/演出) / 魅力湘西大剧院(225元,experience_budget_upgrade/演出) / 万福温泉(180元,experience_budget_upgrade/温泉)
- 景点：天门郡莓茶主题公园(280元,attraction_budget_upgrade/主题公园) / 张家界元宇宙馆(280元,attraction_budget_upgrade/主题公园) / 张家界市消防主题公园(280元,attraction_budget_upgrade/主题公园) / 万福温泉(180元,attraction_budget_upgrade/温泉景区) / 茅岩河漂流(180元,attraction_budget_upgrade/温泉景区)
- 酒店：张家界水木潇湘度假民宿(森林公园店)(750元,hotel_budget_upgrade/高端酒店) / 张家界栖石里洞穴民宿(张家界国家森林公园武陵源标志门店)(750元,hotel_budget_upgrade/五星级酒店) / 张家界如可酒店(天门山索道店)(750元,hotel_budget_upgrade/五星级酒店)

### v3_request_005204 厦门 premium 16800元 ratio_high=1.08

- 餐饮：宴遇·福建荟馆(新景中心店)(341元,food_budget_upgrade/商务宴请) / 鹭鼎会·私房菜(330元,food_budget/精致餐厅) / 闽南渔港·町潮(观音山店)(278元,food_budget_upgrade/商务宴请) / 兴旺海鲜城(五缘湾店)(263元,food_budget_upgrade/商务宴请) / 小埕戏·饮茶肆|流水席(169元,food_budget_upgrade/商务宴请)
- 体验：厦门方特梦幻王国(280元,experience_budget_upgrade/主题公园) / 菽庄花园(180元,experience_budget_upgrade/夜游) / 海峡大剧院(180元,experience_budget_upgrade/演出) / 厦门歌舞剧院(143元,experience_budget_upgrade/演出) / 艾尔拉格啤酒体验馆(阿罗海城市广场店)(65元,experience/美食体验)
- 景点：盛之乡温泉度假村(450元,attraction_budget_upgrade/旅游度假区) / 厦门方特梦幻王国(280元,attraction_budget_upgrade/主题公园) / 一国两制沙滩(180元,attraction_budget_upgrade/索道) / 菽庄花园(180元,attraction_budget_upgrade/夜游) / 钟鼓索道(70元,attraction_budget_upgrade/索道)
- 酒店：厦门集美温德姆至尊豪廷大酒店(1250元,hotel_base/亲子酒店) / 厦门穹顶观海度假酒店(550元,hotel_budget_upgrade/亲子度假酒店) / 鼓浪屿鼓疗度假酒店(菽庄花园观海园沙滩店)(550元,hotel_budget_upgrade/亲子度假酒店)

### v3_request_005207 苏州 premium 21300元 ratio_high=1.10

- 餐饮：江南雅厨·非遗苏州菜(李公堤店)(236元,food_preference/本地菜) / 玉桂樓·苏式美学园林餐厅(斜塘老街店)(228元,food_budget_upgrade/商务宴请) / 宴昆山·精致苏帮菜(西城后街店)(226元,food_budget/精致餐厅) / 馋遇江南·精致湖景雅宴(东方之门店)(216元,food_budget/精致餐厅) / 荣庄(狮子山店)(210元,food_budget_upgrade/商务宴请)
- 体验：苏州湾大剧院(530元,experience_budget_upgrade/演出) / Pass Door Player沉浸式交互剧场(224元,experience_budget_upgrade/沉浸式剧场) / 苏州狮山大剧院(194元,experience_budget_upgrade/演出) / 开明大戏院(观前街店)(182元,experience_budget_upgrade/演出) / MELAND CLUB(昆山万象汇店)(147元,experience/亲子体验)
- 景点：尚湖风景区(280元,attraction_budget_upgrade/旅游度假区) / 阳澄湖半岛旅游度假(280元,attraction_budget_upgrade/旅游度假区) / 山塘街白居易码头游船(180元,attraction_budget_upgrade/游船) / 拙政园(70元,attraction_budget_upgrade/夜游) / 虎丘山风景区(60元,attraction_budget_upgrade/旅游度假区)
- 酒店：永联小镇度假酒店(1250元,hotel_budget_upgrade/亲子度假酒店) / 苏州凯悦酒店(1250元,hotel_base/亲子酒店) / 苏州园区香格里拉大酒店(1250元,hotel_base/亲子酒店)

### v3_request_005208 天津 premium 3900元 ratio_high=1.30

- 餐饮：天津四季酒店·津韵中餐厅(501元,food_budget/黑珍珠餐厅) / 117花园别墅(320元,food_budget/精致餐厅) / 津禧荟.古法鲍鱼(中海店)(232元,food_budget_upgrade/创意菜) / 春和·礼 臻宴融合菜(五大道店)(181元,food_budget/精致餐厅) / 海岛海鲜·海胆水饺(津南旗舰)(139元,food_companion/商务餐厅)
- 体验：天津大剧院(226元,experience_budget_upgrade/演出) / 德云社(东天仙特色商业街店)(104元,experience_budget_upgrade/演出) / 海河剧院(90元,experience_budget_upgrade/演出) / 津湾大剧院(83元,experience_budget_upgrade/演出) / 五大道地标钟(80元,experience/城市地标体验)
- 景点：海河游船(天津站码头)(180元,attraction_budget_upgrade/游船) / 津门故里(180元,attraction_budget_upgrade/夜游) / 天津之眼(80元,attraction_budget_upgrade/旅游度假区) / 瓷房子(50元,attraction_budget_upgrade/旅游度假区) / 张园(30元,classic/历史文化)
- 酒店：天津丽思卡尔顿酒店(1200元,hotel_budget_upgrade/五星级酒店) / 幽幽南山民宿(天津蓟州盘山店)(750元,hotel_budget_upgrade/度假酒店) / 美豪丽致酒店(天津五大道滨江道步行街店)(750元,hotel_budget_upgrade/高端酒店)

### v3_request_005209 天津 premium 4600元 ratio_high=0.94

- 餐饮：天津四季酒店·津韵中餐厅(501元,food_budget/黑珍珠餐厅) / 117花园别墅(320元,food_budget/精致餐厅) / 春和·礼 臻宴融合菜(五大道店)(181元,food_budget/精致餐厅) / 青年餐厅(津湾店)(107元,food_base/特色餐厅) / 大铁勺新津菜(梅江天街店)(103元,food_base/本地菜)
- 体验：天津大剧院(226元,experience_budget_upgrade/演出) / 德云社(东天仙特色商业街店)(104元,experience_budget_upgrade/演出) / 海河剧院(90元,experience_budget_upgrade/演出) / 津湾大剧院(83元,experience_budget_upgrade/演出) / 中国大戏院(金街店)(70元,experience_budget_upgrade/演出)
- 景点：海河游船(天津站码头)(180元,attraction_budget_upgrade/游船) / 津门故里(180元,attraction_budget_upgrade/夜游) / 天津之眼(80元,attraction_budget_upgrade/旅游度假区) / 瓷房子(50元,attraction_budget_upgrade/旅游度假区) / 张园(30元,classic/历史文化)
- 酒店：海河边天津景区萌宠民宿(津浦北路分店)(300元,hotel_budget_upgrade/精品民宿) / 映像磐山·云端奢居·汤泉民宿(天津蓟州盘山店)(300元,hotel_budget_upgrade/精品民宿) / 密斯万象酒店式公寓(天津红郡店)(300元,hotel_budget_upgrade/精品民宿)

### v3_request_005210 桂林 premium 23400元 ratio_high=0.82

- 餐饮：春庄·桂语茶叙(113元,food_budget_upgrade/商务宴请) / 阿甘酒家(解西店)(85元,food_breakfast/早茶) / 凤凰山斑鱼馆(82元,food_budget/精致餐厅) / 水云轩(知味餐饮旗下品牌店)(82元,food_base/特色餐厅) / 桂隐厨·私房家常菜(万象城店)(80元,food_companion/家常菜)
- 体验：桂林千古情景区(280元,experience_budget_upgrade/夜游) / 桂林市两江四湖景区(210元,experience_budget_upgrade/夜游) / 叠彩山(180元,experience_budget_upgrade/夜游) / 千古情大剧院(180元,experience_budget_upgrade/演出) / 银子岩景区(180元,experience_budget_upgrade/实景演出)
- 景点：桂林千古情景区(280元,attraction_budget_upgrade/夜游) / 龙脊梯田风景名胜区(280元,attraction_budget_upgrade/旅游度假区) / 银子岩景区(280元,attraction_budget_upgrade/旅游度假区) / 桂林市两江四湖景区(210元,attraction_budget_upgrade/夜游) / 叠彩山(180元,attraction_budget_upgrade/夜游)
- 酒店：桂林戴斯酒店(1200元,hotel_budget_upgrade/高端酒店) / 桂林阳朔九壤度假酒店(750元,hotel_budget_upgrade/五星级酒店) / 菘蓝之镜SL•Realm度假酒店(遇龙河阳朔湾店)(750元,hotel_budget_upgrade/五星级酒店)

### v3_request_005211 济南 premium 24000元 ratio_high=1.52

- 餐饮：泉客厅Spring Pavilion中餐厅(济南绿地中心店)(891元,food_budget/黑珍珠餐厅) / 长安道高端火锅(697元,food_budget/高端餐厅) / 鼎煮高端和牛放题(国华广场店)(487元,food_budget/高端餐厅) / 舜和海鲜(天发店)(158元,food_budget/精致餐厅) / 7号院·精品湘菜羊汤(奥体中路CBD店)(141元,food_budget/精致餐厅)
- 体验：梦幻童话亲子乐园(长清店)(393元,experience/亲子体验) / 山东省会大剧院(392元,experience_budget_upgrade/演出) / 济南高新区开心麻花剧场(282元,experience_budget_upgrade/演出) / 济南融创乐园(280元,experience_budget_upgrade/主题公园) / 山东剧院(206元,experience_budget_upgrade/演出)
- 景点：山东博物馆(280元,attraction_budget_upgrade/海洋馆) / 清照泉城·明水古城国际泉水旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 千佛山风景名胜区(280元,attraction_budget_upgrade/旅游度假区) / 济南融创乐园(280元,attraction_budget_upgrade/主题公园) / 华山风景区(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：九如山阅木山居民宿(750元,hotel_budget_upgrade/高端酒店) / 清照精品酒店(明水古城店)(750元,hotel_budget_upgrade/五星级酒店) / 九如山不二木居民宿(750元,hotel_budget_upgrade/高端酒店)

### v3_request_005202 丽江 comfortable 17700元 ratio_high=0.92

- 餐饮：金生丽水·龙潭别院(111元,food_companion/商务餐厅) / Lan岚•云南菜•bistro(107元,food_preference/本地菜) / 大宅门野生菌主题餐厅(100元,food_base/特色餐厅) / 滇西王子·山风云南菜·丽江地标品牌(古城南门店)(98元,food_preference/本地菜) / 木王宴语·滇藏野菌火锅(花马店)(92元,food_budget/品质餐厅)
- 体验：丽水金沙表演(207元,experience_budget_upgrade/演出) / 印象丽江剧场(197元,experience_budget_upgrade/剧场) / 丽江古城(180元,experience_budget_upgrade/夜游) / 丽江古城博物院-木府(180元,experience_budget_upgrade/夜游) / 三江民族演艺中心(180元,experience_budget_upgrade/演出)
- 景点：玉龙雪山国家级风景名胜区(280元,attraction_budget_upgrade/主题公园) / 玉龙冰川主题乐园(280元,attraction_budget_upgrade/主题公园) / 丽江古城(180元,attraction_budget_upgrade/夜游) / 丽江古城博物院-木府(180元,attraction_budget_upgrade/夜游) / 拉市海湿地公园-游船(180元,attraction_budget_upgrade/游船)
- 酒店：丽江金茂璞修·雪山酒店(1200元,hotel_budget_upgrade/五星级酒店) / 红花会馆客栈(丽江纳西风情店)(750元,hotel_budget_upgrade/高端酒店) / 望湖轩湖景花园客栈(古城店)(750元,hotel_budget_upgrade/高端酒店)

### v3_request_005213 大理 premium 18400元 ratio_high=0.74

- 餐饮：绿也花园餐厅(120元,food_budget_upgrade/创意菜) / 桃红小馆·特色大理菜·小菜小酒小馆(91元,food_budget/精致餐厅) / 沐府私厨·老大理菜头牌·野生菌汤锅(人民路店)(83元,food_preference/老字号) / 梅子井酒家(81元,food_base/特色餐厅) / 尹珍珠·韩式无限烤肉(80元,food_budget/黑珍珠餐厅)
- 体验：大理路极主题公园(280元,experience_budget_upgrade/主题公园) / 大理杨丽萍大剧院(204元,experience_budget_upgrade/演出) / 索兰央卓(180元,experience_budget_upgrade/演出) / 里白云南家常菜(167元,experience/美食体验) / 康巴唐古拉演艺中心(165元,experience_budget_upgrade/演出)
- 景点：洗马潭索道(280元,attraction_budget_upgrade/旅游度假区) / 大理海洋世界(280元,attraction_budget_upgrade/海洋馆) / 大理苍山石门关旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 大理苍山中和索道(180元,attraction_budget_upgrade/索道) / 苍山景区苍山感通索道(180元,attraction_budget_upgrade/索道)
- 酒店：听花堂海景花园美宿(大理洱海天境店)(300元,hotel_budget_upgrade/精品民宿) / 大理洱海·無云设计师海景酒店(300元,hotel_budget_upgrade/精品民宿) / 大理沐云花舍民宿(300元,hotel_budget_upgrade/精品民宿)

### v3_request_005214 武汉 premium 18400元 ratio_high=1.13

- 餐饮：粗茶淡饭·壹号餐房(洞庭街店)(311元,food_budget/黑珍珠餐厅) / 喜舍黑珍珠餐厅(307元,food_budget/黑珍珠餐厅) / 湖滨客舍(272元,food_budget/黑珍珠餐厅) / 武汉宴·禧樽(271元,food_budget_upgrade/商务宴请) / 玖玺宴(195元,food_budget_upgrade/私房菜)
- 体验：武汉剧院(167元,experience_budget_upgrade/演出) / 洛嘉自然探索中心(105元,experience/亲子体验) / 黄鹤楼(70元,experience_budget_upgrade/夜游) / 武汉琴台大剧院(68元,experience_budget_upgrade/演出) / 彩虹岛亲子乐园(68元,experience/亲子体验)
- 景点：鹦鹉洲汉阳桥梁主题公园(280元,attraction_budget_upgrade/主题公园) / 黄鹤楼(70元,attraction_budget_upgrade/夜游) / 万松园雪松路美食街(68元,preference/美食街) / 东湖磨山景区(60元,attraction_budget_upgrade/索道) / 江夏夜市(38元,preference/美食街)
- 酒店：武汉汉口喜来登大酒店(1200元,hotel_budget_upgrade/精品酒店) / 东湖宾馆(1200元,hotel_budget_upgrade/精品酒店) / 武汉神怡山庄(400元,hotel_budget_upgrade/度假酒店)
