# Planner 预算利用型 Context 审计

- 样本数：100
- 失败数：0
- 耗时：70.457 秒
- contexts：`training/outputs/eval/v3_budget_utilization_context_audit_100_no_luxury_premium_rebased/contexts.jsonl`
- errors：`training/outputs/eval/v3_budget_utilization_context_audit_100_no_luxury_premium_rebased/errors.jsonl`

## 分布

- budget_level：`{"comfortable": 50, "premium": 50}`
- travel_days：`{"4": 40, "5": 40, "3": 20}`

## 核心可达性

| 分组 | 数量 | 可达target_min | 可达target_mid | 高价餐饮覆盖 | 高价体验覆盖 | 高价景点覆盖 | high ratio p50 | food max均值 | exp max均值 | scenic max均值 | hotel max均值 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | 100 | 54.0% | 48.0% | 65.0% | 96.0% | 100.0% | 0.98 | 349.2 | 335.1 | 300.6 | 958.5 |
| comfortable | 50 | 62.0% | 56.0% | 60.0% | 100.0% | 100.0% | 1.05 | 301.8 | 337.2 | 315.6 | 969.0 |
| premium | 50 | 46.0% | 40.0% | 70.0% | 92.0% | 100.0% | 0.93 | 396.6 | 333.1 | 285.5 | 948.0 |

说明：`high_budget_ratio` 是用当前候选池做粗上限估算，不是模型输出预算；用于判断候选是否足以支撑 95%-105% 的预算利用型样本。

## 最弱样本 Top20

| 城市 | 档位 | 预算 | 天数 | 人数 | 高配估算/预算 | 可达target_min | food max | exp max | scenic max | hotel max |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 桂林 | premium | 35600 | 4 | 4 | 0.41 | 否 | 130 | 280 | 280 | 500 |
| 大理 | comfortable | 27600 | 5 | 3 | 0.50 | 否 | 120 | 204 | 280 | 300 |
| 洛阳 | comfortable | 34700 | 4 | 5 | 0.51 | 否 | 104 | 201 | 280 | 400 |
| 张家界 | premium | 26600 | 4 | 4 | 0.56 | 否 | 80 | 266 | 180 | 750 |
| 扬州 | premium | 26200 | 5 | 3 | 0.57 | 否 | 353 | 180 | 280 | 300 |
| 杭州 | comfortable | 28100 | 4 | 4 | 0.59 | 否 | 368 | 303 | 303 | 350 |
| 呼和浩特 | premium | 30600 | 4 | 4 | 0.60 | 否 | 219 | 280 | 280 | 750 |
| 成都 | premium | 36500 | 5 | 4 | 0.60 | 否 | 480 | 465 | 280 | 300 |
| 天津 | premium | 28500 | 5 | 4 | 0.60 | 否 | 501 | 226 | 180 | 300 |
| 哈尔滨 | comfortable | 32600 | 5 | 4 | 0.61 | 否 | 156 | 230 | 330 | 300 |
| 张家界 | premium | 14300 | 5 | 2 | 0.64 | 否 | 80 | 266 | 180 | 750 |
| 沈阳 | comfortable | 15000 | 5 | 2 | 0.66 | 否 | 161 | 226 | 280 | 300 |
| 武汉 | premium | 30900 | 5 | 3 | 0.68 | 否 | 311 | 167 | 280 | 1200 |
| 黄山 | premium | 15900 | 3 | 3 | 0.68 | 否 | 97 | 180 | 280 | 1200 |
| 杭州 | comfortable | 33300 | 4 | 4 | 0.70 | 否 | 368 | 303 | 303 | 1400 |
| 西安 | comfortable | 32800 | 5 | 4 | 0.70 | 否 | 215 | 550 | 280 | 550 |
| 桂林 | premium | 26400 | 4 | 4 | 0.71 | 否 | 113 | 280 | 280 | 1200 |
| 福州 | premium | 21700 | 4 | 3 | 0.71 | 否 | 468 | 280 | 280 | 500 |
| 西安 | comfortable | 36500 | 4 | 5 | 0.73 | 否 | 215 | 550 | 280 | 800 |
| 三亚 | comfortable | 40100 | 5 | 4 | 0.73 | 否 | 160 | 280 | 280 | 1400 |

## 高价候选示例

### v3_request_004100 三亚 comfortable 19400元 ratio_high=1.22

- 餐饮：东海龙宫(大东海店)(160元,food_base/老字号) / 林姐香味海鲜(亚龙湾店)(144元,food_base/老字号) / 不仔客海鲜270度海景餐厅(134元,food_base/特色餐厅) / 阿浪海鲜连锁加工(第一市场店)(132元,food_base/老字号) / 外滩18号海鲜(海棠湾分店)(123元,food_budget/精致餐厅)
- 体验：亚龙湾国家旅游度假区(280元,experience_budget_upgrade/夜游) / 亚特兰蒂斯C秀剧场(273元,experience_budget_upgrade/剧场) / 鹿回头风景区(180元,experience_budget_upgrade/夜游) / 三亚·中交凤凰岛(180元,experience_budget_upgrade/夜游) / 三亚湾(180元,experience_budget_upgrade/夜游)
- 景点：亚龙湾国家旅游度假区(280元,attraction_budget_upgrade/夜游) / 临春岭森林公园(280元,attraction_budget_upgrade/主题公园) / 亚特兰蒂斯失落的空间水族馆(280元,attraction_budget_upgrade/海洋馆) / 亚龙湾海底世界(280元,attraction_budget_upgrade/海洋馆) / 三亚东岸湿地公园(280元,attraction_budget_upgrade/主题公园)
- 酒店：三亚海棠湾九号度假酒店(1400元,hotel_budget_upgrade/精品酒店) / 三亚海棠湾君悦酒店(1400元,hotel_budget_upgrade/精品酒店) / 三亚湾假日度假酒店(1400元,hotel_budget_upgrade/精品酒店)

### v3_request_004101 上海 comfortable 25600元 ratio_high=1.49

- 餐饮：宫宴(上海店)(473元,food_budget/精致餐厅) / 浦江淮宴(263元,food_budget/创意菜) / 浦江家宴(256元,food_budget_upgrade/精致餐厅) / 海福多共富海鲜面馆(224元,food_breakfast/早餐) / Efes Restaurant艾菲斯餐厅(陆家嘴店)(217元,food_budget/品质餐厅)
- 体验：西岸大剧院(475元,experience_budget_upgrade/演出) / 上海迪士尼度假区(475元,experience_budget_upgrade/夜游) / 上海大剧院(314元,experience_budget_upgrade/演出) / 交通银行前滩31演艺中心(309元,experience_budget_upgrade/剧场) / 艺海剧院(FanclArtCenter)(306元,experience_budget_upgrade/剧场)
- 景点：上海迪士尼度假区(475元,attraction_budget_upgrade/主题公园) / 上海欢乐谷(280元,attraction_budget_upgrade/主题公园) / 上海海昌海洋公园(280元,attraction_budget_upgrade/海洋馆) / 上海海洋水族馆(280元,attraction_budget_upgrade/海洋馆) / 东方明珠广播电视塔(199元,attraction_budget_upgrade/夜游)
- 酒店：上海瑞金洲际酒店(1400元,hotel_budget_upgrade/精品酒店) / 上海半岛酒店(1400元,hotel_budget_upgrade/精品酒店) / 东郊宾馆(1400元,hotel_budget_upgrade/精品酒店)

### v3_request_004103 大理 comfortable 13100元 ratio_high=0.74

- 餐饮：绿也花园餐厅(120元,food_budget/创意菜) / 桃红小馆·特色大理菜·小菜小酒小馆(91元,food_budget/精致餐厅) / 沐府私厨·老大理菜头牌·野生菌汤锅(人民路店)(83元,food_preference/老字号) / 梅子井酒家(81元,food_base/特色餐厅) / 幸会小仙女精品石板烧野生菌火锅(大理总店)(74元,food_budget/品质餐厅)
- 体验：大理杨丽萍大剧院(204元,experience_budget_upgrade/演出) / 索兰央卓(180元,experience_budget_upgrade/演出) / 火花剧本·剧场(180元,experience_budget_upgrade/剧场) / 古梨园空中稻田剧场(180元,experience_budget_upgrade/剧场) / 里白云南家常菜(167元,experience/美食体验)
- 景点：大理海洋世界(280元,attraction_budget_upgrade/海洋馆) / 苍山自然影像博物馆(280元,attraction_budget_upgrade/海洋馆) / 青海湖主题乐园(280元,attraction_budget_upgrade/主题公园) / 白族园(280元,attraction_budget_upgrade/主题公园) / 文华公园(280元,attraction_budget_upgrade/主题公园)
- 酒店：大理青朴酒店(400元,hotel_budget_upgrade/高端酒店) / 麓引全LUYANGTREE·莱安海景度假美宿(大理洱海店)(400元,hotel_budget_upgrade/高端酒店) / 大理栖海听风客栈(张家花园店)(400元,hotel_budget_upgrade/高端酒店)

### v3_request_004104 福州 premium 21700元 ratio_high=0.71

- 餐饮：御宴(福州店)(468元,food_budget_upgrade/创意菜) / 悦港琴湾·福宴(华林路店)(242元,food_budget/精致餐厅) / 难得怪味·客家山宴(福州奥体店)(139元,food_budget/精致餐厅) / 紫阳海鲜楼·传承闽味(华林路店)(121元,food_budget/精致餐厅) / 闽知岚·鲜作福建菜(119元,food_budget/精致餐厅)
- 体验：龙王头海洋公园(280元,experience_budget_upgrade/夜游) / 中国船政文化景区(280元,experience_budget_upgrade/主题公园) / 平潭岛海滩(180元,experience_budget_upgrade/夜游) / 闽江夜游(180元,experience_budget_upgrade/夜游) / 福建大剧院(147元,experience_budget_upgrade/演出)
- 景点：龙王头海洋公园(280元,attraction_budget_upgrade/海洋馆) / 平潭国际旅游岛-长江澳风力田景观区(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·68海里景区(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·仙人井(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·坛南湾(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：伴岛·度假酒店(龙王头沙滩店)(500元,hotel_budget_upgrade/亲子度假酒店) / 福州三坊七巷三宝宾邸(500元,hotel_budget_upgrade/五星级酒店) / 择宁而居民宿(龙王头沙滩店)(500元,hotel_budget_upgrade/度假酒店)

### v3_request_004107 武汉 premium 30900元 ratio_high=0.68

- 餐饮：粗茶淡饭·壹号餐房(洞庭街店)(311元,food_budget/黑珍珠餐厅) / 喜舍黑珍珠餐厅(307元,food_budget/黑珍珠餐厅) / 湖滨客舍(272元,food_budget/黑珍珠餐厅) / 武汉宴·禧樽(271元,food_budget_upgrade/商务宴请) / 玖玺宴(195元,food_budget_upgrade/私房菜)
- 体验：武汉剧院(167元,experience_budget_upgrade/演出) / 黄鹤楼(70元,experience_budget_upgrade/夜游) / 武汉琴台大剧院(68元,experience_budget_upgrade/演出) / 湖北剧院(67元,experience_budget_upgrade/演出) / 名熙堂·扁鹊爷爷会员体验中心(39元,experience/美食体验)
- 景点：鹦鹉洲汉阳桥梁主题公园(280元,attraction_budget_upgrade/主题公园) / 黄鹤楼(70元,attraction_budget_upgrade/夜游) / 万松园雪松路美食街(68元,preference/美食街) / 东湖磨山景区(60元,attraction_budget_upgrade/索道) / 江夏夜市(38元,preference/美食街)
- 酒店：武汉汉口喜来登大酒店(1200元,hotel_budget_upgrade/五星级酒店) / 东湖宾馆(1200元,hotel_budget_upgrade/五星级酒店) / 武汉神怡山庄(750元,hotel_budget_upgrade/度假酒店)

### v3_request_004105 三亚 comfortable 40100元 ratio_high=0.73

- 餐饮：东海龙宫(大东海店)(160元,food_base/老字号) / 林姐香味海鲜(亚龙湾店)(144元,food_base/老字号) / 不仔客海鲜270度海景餐厅(134元,food_base/特色餐厅) / 阿浪海鲜连锁加工(第一市场店)(132元,food_base/老字号) / 外滩18号海鲜(海棠湾分店)(123元,food_budget/精致餐厅)
- 体验：亚龙湾国家旅游度假区(280元,experience_budget_upgrade/夜游) / 亚特兰蒂斯C秀剧场(273元,experience_budget_upgrade/剧场) / 鹿回头风景区(180元,experience_budget_upgrade/夜游) / 三亚·中交凤凰岛(180元,experience_budget_upgrade/夜游) / 三亚湾(180元,experience_budget_upgrade/夜游)
- 景点：亚龙湾国家旅游度假区(280元,attraction_budget_upgrade/夜游) / 临春岭森林公园(280元,attraction_budget_upgrade/主题公园) / 亚特兰蒂斯失落的空间水族馆(280元,attraction_budget_upgrade/海洋馆) / 亚龙湾海底世界(280元,attraction_budget_upgrade/海洋馆) / 三亚东岸湿地公园(280元,attraction_budget_upgrade/主题公园)
- 酒店：三亚海棠湾九号度假酒店(1400元,hotel_budget_upgrade/亲子度假酒店) / 三亚湾假日度假酒店(1400元,hotel_budget_upgrade/亲子度假酒店) / 三亚湾海居铂尔曼度假酒店(1400元,hotel_budget_upgrade/亲子度假酒店)

### v3_request_004109 杭州 premium 6200元 ratio_high=1.61

- 餐饮：暗香·Wild Yeast(914元,food_budget/黑珍珠餐厅) / 青岚(杨公堤店)(641元,food_budget/黑珍珠餐厅) / 桂语山房(满觉陇店)(607元,food_budget/黑珍珠餐厅) / 龙井御庄·精致江南菜(西湖景区店)(368元,food_budget/精致餐厅) / 乔村二十八道(天目山路店)(190元,food_budget_upgrade/创意菜)
- 体验：未来城市乐园(303元,experience_budget_upgrade/夜游) / 运河大剧院(301元,experience_budget_upgrade/演出) / 杭州大剧院(282元,experience_budget_upgrade/演出) / 杭州金沙湖大剧院(255元,experience_budget_upgrade/演出) / 城市蓝厅·香樟园(227元,experience/特色餐厅体验)
- 景点：未来城市乐园(303元,attraction_budget_upgrade/夜游) / 湘湖国家旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 云栖竹径(180元,attraction_budget_upgrade/夜游) / 千岛湖风景区(130元,attraction_budget_upgrade/旅游度假区) / 西溪国家湿地公园(80元,attraction_budget_upgrade/旅游度假区)
- 酒店：浙江西子宾馆(南山路店)(1400元,hotel_budget_upgrade/高端酒店) / 杭州九里云松度假酒店(1400元,hotel_budget_upgrade/五星级酒店) / 罗马酒店(杭州富春江店)(850元,hotel_budget_upgrade/高端酒店)

### v3_request_004106 昆明 comfortable 10000元 ratio_high=1.22

- 餐饮：熙楼(125元,food_budget/精致餐厅) / 祥云荟馆庭院餐厅(祥云街店)(99元,food_budget_upgrade/品质餐厅) / 从水居餐厅.特色云南菜(滇池海鸥岛店)(92元,food_base/特色餐厅) / 福照楼汽锅鸡饭店·云南特色菜·西南联大主题(老街胜利堂店)(91元,food_base/特色餐厅) / 山以南·云贵菜(同德店)(83元,food_budget/创意菜)
- 体验：云南映象剧院(283元,experience_budget_upgrade/演出) / 云南艺术剧院(东风西路)(273元,experience_budget_upgrade/演出) / 七彩云南古滇温泉山庄(180元,experience_budget_upgrade/温泉) / 石屏会馆(165元,experience/美食体验) / 昆明剧院(青年路)(164元,experience_budget_upgrade/演出)
- 景点：小人国主题公园(280元,attraction_budget_upgrade/主题公园) / 蓝花楹主题公园(280元,attraction_budget_upgrade/主题公园) / 公园1903梦幻联邦乐园(280元,attraction_budget_upgrade/主题公园) / 昆明大渔公园(280元,attraction_budget_upgrade/主题公园) / 冰雪海洋世界(280元,attraction_budget_upgrade/海洋馆)
- 酒店：昆明鑫盛达宏晟国际酒店(1200元,hotel_budget_upgrade/五星级酒店) / 昆明千寻墨问温泉SPA民宿(750元,hotel_budget_upgrade/五星级酒店) / 昆明兰度酒店(750元,hotel_budget_upgrade/高端酒店)

### v3_request_004110 青岛 premium 14300元 ratio_high=0.98

- 餐饮：味语膳房(石老人)(316元,food_budget/精致餐厅) / 升海·本源海鲜海胆水饺(西海岸店)(120元,food_budget/精致餐厅) / 开海·红岛海鲜虾水饺店(八大关店)(115元,food_base/特色餐厅) / 蓝港海鲜厨房(云霄路店)(114元,food_budget_upgrade/商务宴请) / 味莊·臻选店(101元,food_budget_upgrade/商务宴请)
- 体验：青岛城阳开心麻花大剧院(361元,experience_budget_upgrade/演出) / 青岛大剧院(210元,experience_budget_upgrade/演出) / 青岛凤凰之声大剧院(192元,experience_budget_upgrade/演出) / 青岛红树林度假世界(180元,experience_budget_upgrade/温泉) / 小麦岛公园(180元,experience_budget_upgrade/夜游)
- 景点：青岛方特梦幻王国(280元,attraction_budget_upgrade/主题公园) / 青岛海底世界(280元,attraction_budget_upgrade/海洋馆) / 青岛奥帆海洋文化旅游区(280元,attraction_budget_upgrade/旅游度假区) / 崂山风景区(180元,attraction_budget_upgrade/旅游度假区) / 小麦岛公园(180元,attraction_budget_upgrade/夜游)
- 酒店：青岛世界博览城润生大酒店(1250元,hotel_budget_upgrade/高端酒店) / 青岛香格里拉大酒店(1250元,hotel_base/亲子酒店) / 青岛海景花园大酒店(1250元,hotel_base/亲子酒店)

### v3_request_004111 深圳 premium 4400元 ratio_high=1.64

- 餐饮：鹤松(聚会·高空景观店)(563元,food_budget_upgrade/创意菜) / 至正潮菜(华侨城店)(483元,food_budget/黑珍珠餐厅) / 嘉苑饭店(477元,food_budget/黑珍珠餐厅) / 水岸十里(440元,food_budget/黑珍珠餐厅) / 阅悦·私房菜(南山店)(228元,food_budget_upgrade/创意菜)
- 体验：南山文体中心聚橙剧院(464元,experience_budget_upgrade/演出) / 深圳开心麻花红山剧场(375元,experience_budget_upgrade/演出) / 保利剧院(291元,experience_budget_upgrade/演出) / 深圳滨海艺术中心(276元,experience_budget_upgrade/演出) / 深圳大剧院(128元,experience_budget_upgrade/演出)
- 景点：华侨城欢乐海岸(280元,attraction_budget_upgrade/旅游度假区) / 锦绣中华民俗村(280元,attraction_budget_upgrade/主题公园) / 白石龙音乐主题公园(280元,attraction_budget_upgrade/主题公园) / 深圳世界之窗(220元,attraction_budget_upgrade/旅游度假区) / 罗瑞合美食步行街(43元,preference/美食街)
- 酒店：中濠悦际酒店(深圳龙华大浪商业中心店)(450元,hotel_budget_upgrade/中高端酒店) / 深圳科技园高新中亚朵S酒店(450元,hotel_budget_upgrade/中高端酒店) / 全季酒店(深圳CBD福田地铁站店)(450元,hotel_budget_upgrade/高端酒店)

### v3_request_004112 桂林 premium 26400元 ratio_high=0.71

- 餐饮：春庄·桂语茶叙(113元,food_budget_upgrade/商务宴请) / 阿甘酒家(解西店)(85元,food_breakfast/早茶) / 凤凰山斑鱼馆(82元,food_budget/精致餐厅) / 水云轩(知味餐饮旗下品牌店)(82元,food_base/特色餐厅) / 桂隐厨·空中合院餐厅(80元,food_budget/精致餐厅)
- 体验：桂林千古情景区(280元,experience_budget_upgrade/夜游) / 桂林市两江四湖景区(210元,experience_budget_upgrade/夜游) / 叠彩山(180元,experience_budget_upgrade/夜游) / 千古情大剧院(180元,experience_budget_upgrade/演出) / 银子岩景区(180元,experience_budget_upgrade/实景演出)
- 景点：桂林千古情景区(280元,attraction_budget_upgrade/夜游) / 龙脊梯田风景名胜区(280元,attraction_budget_upgrade/旅游度假区) / 银子岩景区(280元,attraction_budget_upgrade/旅游度假区) / 桂林市两江四湖景区(210元,attraction_budget_upgrade/夜游) / 叠彩山(180元,attraction_budget_upgrade/夜游)
- 酒店：桂林戴斯酒店(1200元,hotel_budget_upgrade/高端酒店) / 桂林阳朔九壤度假酒店(750元,hotel_budget_upgrade/五星级酒店) / 菘蓝之镜SL•Realm度假酒店(遇龙河阳朔湾店)(750元,hotel_budget_upgrade/五星级酒店)

### v3_request_004114 福州 premium 14600元 ratio_high=0.87

- 餐饮：御宴(福州店)(468元,food_budget_upgrade/创意菜) / 悦港琴湾·福宴(华林路店)(242元,food_budget/精致餐厅) / 福州中庚聚龙酒店香汇自助餐厅(南江滨西大道店)(166元,food_companion/亲子餐厅) / 难得怪味·客家山宴(福州奥体店)(139元,food_budget/精致餐厅) / 紫阳海鲜楼·传承闽味(华林路店)(121元,food_budget/精致餐厅)
- 体验：龙王头海洋公园(280元,experience_budget_upgrade/夜游) / 中国船政文化景区(280元,experience_budget_upgrade/主题公园) / 平潭岛海滩(180元,experience_budget_upgrade/夜游) / 闽江夜游(180元,experience_budget_upgrade/夜游) / 福建大剧院(147元,experience_budget_upgrade/演出)
- 景点：龙王头海洋公园(280元,attraction_budget_upgrade/海洋馆) / 平潭国际旅游岛-长江澳风力田景观区(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·68海里景区(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·仙人井(280元,attraction_budget_upgrade/旅游度假区) / 平潭国际旅游岛·坛南湾(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：福州三坊七巷三宝宾邸(750元,hotel_budget_upgrade/五星级酒店) / 伴岛·度假酒店(龙王头沙滩店)(750元,hotel_budget_upgrade/度假酒店) / 择宁而居民宿(龙王头沙滩店)(750元,hotel_budget_upgrade/度假酒店)
