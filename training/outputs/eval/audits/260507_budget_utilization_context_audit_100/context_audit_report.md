# Planner 预算利用型 Context 审计

- 样本数：100
- 失败数：0
- 耗时：201.283 秒
- contexts：`training/outputs/eval/v3_budget_utilization_context_audit_100/contexts.jsonl`
- errors：`training/outputs/eval/v3_budget_utilization_context_audit_100/errors.jsonl`

## 分布

- budget_level：`{"comfortable": 36, "premium": 48, "luxury": 16}`
- travel_days：`{"4": 40, "5": 40, "3": 20}`

## 核心可达性

| 分组 | 数量 | 可达target_min | 可达target_mid | 高价餐饮覆盖 | 高价体验覆盖 | 高价景点覆盖 | high ratio p50 | food max均值 | exp max均值 | scenic max均值 | hotel max均值 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | 100 | 26.0% | 21.0% | 71.0% | 95.0% | 99.0% | 0.70 | 425.0 | 322.1 | 299.3 | 985.5 |
| comfortable | 36 | 61.1% | 52.8% | 61.1% | 94.4% | 100.0% | 1.06 | 306.1 | 321.9 | 313.2 | 1086.1 |
| luxury | 16 | 0.0% | 0.0% | 87.5% | 93.8% | 93.8% | 0.34 | 799.2 | 249.2 | 275.8 | 996.9 |
| premium | 48 | 8.3% | 4.2% | 72.9% | 95.8% | 100.0% | 0.62 | 389.4 | 346.6 | 296.8 | 906.2 |

说明：`high_budget_ratio` 是用当前候选池做粗上限估算，不是模型输出预算；用于判断候选是否足以支撑 95%-105% 的预算利用型样本。

## 最弱样本 Top20

| 城市 | 档位 | 预算 | 天数 | 人数 | 高配估算/预算 | 可达target_min | food max | exp max | scenic max | hotel max |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 成都 | luxury | 90600 | 5 | 4 | 0.09 | 否 | 0 | 0 | 0 | 800 |
| 重庆 | luxury | 134100 | 5 | 4 | 0.21 | 否 | 684 | 219 | 280 | 750 |
| 呼和浩特 | luxury | 32500 | 3 | 2 | 0.26 | 否 | 320 | 280 | 280 | 750 |
| 大连 | luxury | 128600 | 4 | 5 | 0.28 | 否 | 1362 | 280 | 280 | 500 |
| 广州 | luxury | 122300 | 5 | 4 | 0.30 | 否 | 735 | 288 | 300 | 1250 |
| 郑州 | luxury | 124400 | 5 | 5 | 0.30 | 否 | 467 | 280 | 280 | 1200 |
| 桂林 | premium | 71900 | 5 | 4 | 0.32 | 否 | 113 | 280 | 280 | 1200 |
| 张家界 | premium | 46700 | 4 | 4 | 0.32 | 否 | 80 | 266 | 180 | 750 |
| 青岛 | luxury | 84100 | 3 | 5 | 0.32 | 否 | 807 | 280 | 280 | 1250 |
| 南京 | luxury | 91200 | 5 | 3 | 0.34 | 否 | 1872 | 217 | 280 | 1250 |
| 厦门 | luxury | 70400 | 3 | 4 | 0.34 | 否 | 585 | 180 | 450 | 800 |
| 重庆 | luxury | 78600 | 5 | 4 | 0.36 | 否 | 684 | 219 | 280 | 750 |
| 大理 | luxury | 17800 | 5 | 1 | 0.38 | 否 | 110 | 180 | 280 | 750 |
| 大理 | premium | 47400 | 4 | 4 | 0.41 | 否 | 120 | 280 | 280 | 1200 |
| 贵阳 | luxury | 48400 | 5 | 3 | 0.42 | 否 | 1031 | 280 | 280 | 500 |
| 呼和浩特 | premium | 56100 | 5 | 4 | 0.42 | 否 | 219 | 280 | 280 | 750 |
| 张家界 | premium | 35500 | 5 | 3 | 0.43 | 否 | 108 | 266 | 180 | 750 |
| 泉州 | premium | 41100 | 4 | 3 | 0.45 | 否 | 195 | 184 | 280 | 1200 |
| 成都 | premium | 85400 | 5 | 6 | 0.45 | 否 | 480 | 465 | 280 | 800 |
| 厦门 | premium | 76300 | 5 | 5 | 0.46 | 否 | 341 | 280 | 450 | 1250 |

## 高价候选示例

### v3_request_003002 杭州 comfortable 31600元 ratio_high=0.75

- 餐饮：龙井御庄·精致江南菜(西湖景区店)(368元,food_budget/精致餐厅) / 乔村二十八道(天目山路店)(190元,food_budget_upgrade/创意菜) / 乔村二十八道(未来科技城店)(152元,food_budget/创意菜) / 杨记肴·精致浙菜(东站店)(150元,food_budget/精致餐厅) / 杨记肴•精致浙菜(闸弄口黑金店)(150元,food_budget_upgrade/精致餐厅)
- 体验：未来城市乐园(303元,experience_budget_upgrade/夜游) / 运河大剧院(301元,experience_budget_upgrade/演出) / 杭州大剧院(282元,experience_budget_upgrade/演出) / 杭州金沙湖大剧院(255元,experience_budget_upgrade/演出) / 杭州剧院(223元,experience_budget_upgrade/演出)
- 景点：未来城市乐园(303元,attraction_budget_upgrade/夜游) / 云栖竹径(180元,attraction_budget_upgrade/夜游) / 千岛湖风景区(130元,classic/必游景点) / 东新足球主题公园(91元,attraction_budget_upgrade/主题公园) / 西溪国家湿地公园(80元,attraction_budget_upgrade/夜游)
- 酒店：杭州西溪宾馆(1400元,hotel_budget_upgrade/精品酒店) / UrCove逸扉酒店(杭州钱塘店)(500元,hotel_budget_upgrade/中高端酒店) / 罗马酒店(杭州富春江店)(500元,hotel_budget_upgrade/高端酒店)

### v3_request_003001 杭州 comfortable 19800元 ratio_high=1.20

- 餐饮：龙井御庄·精致江南菜(西湖景区店)(368元,food_budget/精致餐厅) / 乔村二十八道(天目山路店)(190元,food_budget_upgrade/创意菜) / 乔村二十八道(未来科技城店)(152元,food_budget/创意菜) / 杨记肴·精致浙菜(东站店)(150元,food_budget/精致餐厅) / 杨记肴•精致浙菜(闸弄口黑金店)(150元,food_budget_upgrade/精致餐厅)
- 体验：未来城市乐园(303元,experience_budget_upgrade/夜游) / 运河大剧院(301元,experience_budget_upgrade/演出) / 杭州大剧院(282元,experience_budget_upgrade/演出) / 杭州金沙湖大剧院(255元,experience_budget_upgrade/演出) / 杭州剧院(223元,experience_budget_upgrade/演出)
- 景点：未来城市乐园(303元,attraction_budget_upgrade/夜游) / 云栖竹径(180元,attraction_budget_upgrade/夜游) / 千岛湖风景区(130元,classic/必游景点) / 东新足球主题公园(91元,attraction_budget_upgrade/主题公园) / 西溪国家湿地公园(80元,attraction_budget_upgrade/夜游)
- 酒店：良渚君澜度假酒店(1400元,hotel_base/亲子酒店) / UrCove逸扉酒店(杭州钱塘店)(600元,hotel_budget_upgrade/中高端酒店) / 九思居·环谷秘境·日出云海·珍馐度假美宿(天目山店)(600元,hotel_budget_upgrade/高端亲子酒店)

### v3_request_003006 昆明 comfortable 13400元 ratio_high=0.93

- 餐饮：上菌山·云南野生牛肝菌火锅(昆明老街店)(130元,food_companion/家常菜) / 熙楼(125元,food_budget/精致餐厅) / 祥云荟馆庭院餐厅(祥云街店)(99元,food_budget_upgrade/品质餐厅) / 从水居餐厅.特色云南菜(滇池海鸥岛店)(92元,food_base/特色餐厅) / 福照楼汽锅鸡饭店·云南特色菜·西南联大主题(老街胜利堂店)(91元,food_base/特色餐厅)
- 体验：云南映象剧院(283元,experience_budget_upgrade/演出) / 云南艺术剧院(东风西路)(273元,experience_budget_upgrade/演出) / 七彩云南古滇温泉山庄(180元,experience_budget_upgrade/温泉) / 石屏会馆(165元,experience/美食体验) / 昆明剧院(青年路)(164元,experience_budget_upgrade/演出)
- 景点：小人国主题公园(280元,attraction_budget_upgrade/主题公园) / 蓝花楹主题公园(280元,attraction_budget_upgrade/主题公园) / 公园1903梦幻联邦乐园(280元,attraction_budget_upgrade/主题公园) / 昆明大渔公园(280元,attraction_budget_upgrade/主题公园) / 冰雪海洋世界(280元,attraction_budget_upgrade/海洋馆)
- 酒店：昆明华邑酒店(1200元,hotel_budget_upgrade/精品酒店) / 昆明香格里拉(400元,hotel_budget_upgrade/精品酒店) / 话题酒店(昆明嵩明杨林大学城店)(400元,hotel_budget_upgrade/中高端酒店)

### v3_request_003005 武汉 comfortable 21200元 ratio_high=0.97

- 餐饮：水樂棠铭隐主厨江景餐厅(352元,food_budget/创意菜) / 百分之五洋房餐厅(247元,food_budget/创意菜) / 金马门国际美食百汇(珞喻路店)(160元,food_preference/老字号) / Hygge薄荷花园餐厅(吉庆街店)(127元,food_budget/创意菜) / 巴厘龙虾(旗舰店·万松园店)(121元,food_budget_upgrade/品质餐厅)
- 体验：武汉剧院(167元,experience_budget_upgrade/演出) / 洛嘉自然探索中心(105元,experience/亲子体验) / 黄鹤楼(70元,experience_budget_upgrade/夜游) / 武汉琴台大剧院(68元,experience_budget_upgrade/演出) / 彩虹岛亲子乐园(68元,experience/亲子体验)
- 景点：鹦鹉洲汉阳桥梁主题公园(280元,attraction_budget_upgrade/主题公园) / 东西湖极地海洋公园(280元,attraction_budget_upgrade/海洋馆) / 黄鹤楼(70元,attraction_budget_upgrade/夜游) / 万松园雪松路美食街(68元,preference/美食街) / 东湖磨山景区(60元,classic/必游景点)
- 酒店：武汉汉口喜来登大酒店(1200元,hotel_budget_upgrade/精品酒店) / 东湖宾馆(1200元,hotel_budget_upgrade/精品酒店) / 武汉雄楚大道枫渡酒店(500元,hotel_budget_upgrade/高端亲子酒店)

### v3_request_003000 广州 comfortable 17600元 ratio_high=1.32

- 餐饮：闻风相悦素食餐厅(286元,food_budget/创意菜) / 新海私厨(新海Park店)(200元,food_budget/创意菜) / 大良毋米粥·粥水火锅(珠江新城冼村店)(140元,food_breakfast/粥) / 松苑·浓汤广府菜(总店)(121元,food_base/本地菜) / 滋粥楼·顺德菜(南村万博长隆商圈店)(112元,food_breakfast/粥)
- 体验：广州大剧院歌剧厅(485元,experience_budget_upgrade/演出) / 广州大剧院(475元,experience_budget_upgrade/演出) / 从化温泉度假区(180元,experience_budget_upgrade/温泉) / 友谊剧院(180元,experience_budget_upgrade/演出) / 广州蓓蕾剧院(172元,experience_budget_upgrade/演出)
- 景点：长隆野生动物世界(300元,classic/必游景点) / 广州长隆旅游度假区(200元,classic/必游景点) / 广东科学中心(180元,attraction_budget_upgrade/游船) / 珠江夜游(天字码头)(180元,attraction_budget_upgrade/夜游) / 珠江夜游(大沙头码头)(180元,attraction_budget_upgrade/夜游)
- 酒店：爱立斯水善坊酒店(北京路省人民医院店)(1250元,hotel_budget_upgrade/五星级酒店) / 谊尚(广州花都融创工商学院店)(800元,hotel_budget_upgrade/高端酒店) / 丽呈铂锐酒店(广州奥体中心鱼珠地铁站店)(800元,hotel_budget_upgrade/高端酒店)

### v3_request_003007 杭州 premium 60100元 ratio_high=0.47

- 餐饮：暗香·Wild Yeast(914元,food_budget/黑珍珠餐厅) / 青岚(杨公堤店)(641元,food_budget/黑珍珠餐厅) / 桂语山房(满觉陇店)(607元,food_budget/黑珍珠餐厅) / 龙井御庄·精致江南菜(西湖景区店)(368元,food_budget/精致餐厅) / 乔村二十八道(天目山路店)(190元,food_budget_upgrade/创意菜)
- 体验：未来城市乐园(303元,experience_budget_upgrade/夜游) / 运河大剧院(301元,experience_budget_upgrade/演出) / 杭州大剧院(282元,experience_budget_upgrade/演出) / 杭州金沙湖大剧院(255元,experience_budget_upgrade/演出) / 杭州剧院(223元,experience_budget_upgrade/演出)
- 景点：未来城市乐园(303元,attraction_budget_upgrade/夜游) / 湘湖国家旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 云栖竹径(180元,attraction_budget_upgrade/夜游) / 千岛湖风景区(130元,attraction_budget_upgrade/旅游度假区) / 西溪国家湿地公园(80元,attraction_budget_upgrade/旅游度假区)
- 酒店：伴客女生青旅(杭州火车东站店)(350元,hotel_budget_upgrade/度假民宿) / 珑璟心情民宿(西湖太子湾店)(350元,hotel_budget_upgrade/精品民宿) / 听涧·西湖|越上云舍民宿(杭州太子湾公园店)(350元,hotel_budget_upgrade/精品民宿)

### v3_request_003003 厦门 premium 76300元 ratio_high=0.46

- 餐饮：宴遇·福建荟馆(新景中心店)(341元,food_budget_upgrade/商务宴请) / 鹭鼎会·私房菜(330元,food_budget/精致餐厅) / 闽南渔港·町潮(观音山店)(278元,food_budget_upgrade/商务宴请) / 兴旺海鲜城(五缘湾店)(263元,food_budget_upgrade/商务宴请) / 小埕戏·饮茶肆|流水席(169元,food_budget_upgrade/商务宴请)
- 体验：厦门方特梦幻王国(280元,experience_budget_upgrade/主题公园) / 菽庄花园(180元,experience_budget_upgrade/夜游) / 海峡大剧院(180元,experience_budget_upgrade/演出) / 厦门歌舞剧院(143元,experience_budget_upgrade/演出) / 萌发地·海野乐园(64元,experience/亲子体验)
- 景点：盛之乡温泉度假村(450元,attraction_budget_upgrade/旅游度假区) / 厦门方特梦幻王国(280元,attraction_budget_upgrade/主题公园) / 一国两制沙滩(180元,attraction_budget_upgrade/索道) / 菽庄花园(180元,attraction_budget_upgrade/夜游) / 钟鼓索道(70元,attraction_budget_upgrade/索道)
- 酒店：厦门集美温德姆至尊豪廷大酒店(1250元,hotel_base/亲子酒店) / 厦门穹顶观海度假酒店(550元,hotel_budget_upgrade/亲子度假酒店) / 鼓浪屿鼓疗度假酒店(菽庄花园观海园沙滩店)(550元,hotel_budget_upgrade/亲子度假酒店)

### v3_request_003009 北京 premium 28300元 ratio_high=1.37

- 餐饮：然寿司(钱粮胡同店)(1440元,food_budget/黑珍珠餐厅) / 然锅料理(831元,food_budget/黑珍珠餐厅) / 北京凯瑞御仙都皇家菜博物馆(586元,food_preference/本地菜) / 宫宴(北京店)(543元,food_preference/特色餐厅) / 芙蓉无双荣派湘菜(450元,food_budget/黑珍珠餐厅)
- 体验：保利剧院(保利大厦店)(525元,experience_budget_upgrade/演出) / 不白吃有文化中心(304元,experience/文化体验) / 北京环球度假区(280元,experience_budget_upgrade/主题公园) / 国家体育场(280元,experience_budget_upgrade/滑雪场) / 北京人民艺术剧院(200元,experience_budget_upgrade/演出)
- 景点：北京欢乐谷(280元,attraction_budget_upgrade/主题公园) / 哈利·波特的魔法世界(280元,attraction_budget_upgrade/主题公园) / 瀛海足球主题公园(280元,attraction_budget_upgrade/主题公园) / 温都水城(280元,attraction_budget_upgrade/旅游度假区) / 景山公园(180元,attraction_budget_upgrade/夜游)
- 酒店：华北宾馆(1400元,hotel_budget_upgrade/高端酒店) / 北京宝格丽酒店(1400元,hotel_budget_upgrade/五星级酒店) / 北京大兴中心假日酒店(850元,hotel_budget_upgrade/高端酒店)

### v3_request_003012 杭州 luxury 71200元 ratio_high=0.47

- 餐饮：暗香·Wild Yeast(914元,food_budget/黑珍珠餐厅) / 杭州康莱德酒店·里安(新业路店)(703元,food_budget/黑珍珠餐厅) / 青岚(杨公堤店)(641元,food_budget/黑珍珠餐厅) / 杭州柏悦酒店悦轩中餐厅(631元,food_budget/黑珍珠餐厅) / 桂语山房(满觉陇店)(607元,food_budget/黑珍珠餐厅)
- 体验：太阳剧场(420元,experience_budget_upgrade/沉浸式剧场) / 未来城市乐园(303元,experience_budget_upgrade/夜游) / 城市蓝厅·香樟园(227元,experience/特色餐厅体验) / 剧隐奇观沉浸式剧本杀演绎馆(207元,experience_budget_upgrade/沉浸式剧场) / 云栖竹径(180元,experience_budget_upgrade/夜游)
- 景点：未来城市乐园(303元,attraction_budget_upgrade/夜游) / 湘湖国家旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 云栖竹径(180元,attraction_budget_upgrade/夜游) / 千岛湖风景区(130元,attraction_budget_upgrade/旅游度假区) / 胜利河美食街(94元,preference/美食街)
- 酒店：浙江西子宾馆(南山路店)(1400元,hotel_budget_upgrade/高端酒店) / 杭州九里云松度假酒店(1400元,hotel_budget_upgrade/五星级酒店) / 罗马酒店(杭州富春江店)(850元,hotel_budget_upgrade/高端酒店)

### v3_request_003004 泉州 premium 41100元 ratio_high=0.45

- 餐饮：蚂蚁私厨(195元,food_budget_upgrade/私房菜) / 绿岛海鲜酒楼(瑞昌街石狮市步行街店)(144元,food_budget_upgrade/商务宴请) / 欣悦喜宴楼(晋江店)(142元,food_budget_upgrade/商务宴请) / 闽南厝闽南菜(桥南店)(138元,food_budget_upgrade/商务宴请) / 闽荣记·闽南菜(126元,food_budget/精致餐厅)
- 体验：泉州市公共文化中心泉州大剧院(184元,experience_budget_upgrade/演出) / 泉州木偶剧院(180元,experience_budget_upgrade/演出) / 泉州大开元寺(180元,experience_budget_upgrade/夜游) / 通淮关岳庙(180元,experience_budget_upgrade/夜游) / 晋江大剧院(180元,experience_budget_upgrade/演出)
- 景点：紫帽山旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 五店市传统街区(280元,attraction_budget_upgrade/旅游度假区) / 泉州海丝野生动物世界(280元,attraction_budget_upgrade/海洋馆) / 十里黄金海岸红塔湾旅游区(280元,attraction_budget_upgrade/旅游度假区) / 清源山国家重点风景名胜区(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：泉州悦华酒店(1200元,hotel_budget_upgrade/五星级酒店) / 绿岛国际酒店(1200元,hotel_budget_upgrade/五星级酒店) / 泉州泉商希尔顿酒店(1200元,hotel_budget_upgrade/五星级酒店)

### v3_request_003011 泉州 premium 13100元 ratio_high=0.83

- 餐饮：蚂蚁私厨(195元,food_budget_upgrade/私房菜) / 海桐里(海峡体育中心店)(168元,food_base/本地菜) / 绿岛海鲜酒楼(瑞昌街石狮市步行街店)(144元,food_budget_upgrade/商务宴请) / 欣悦喜宴楼(晋江店)(142元,food_budget_upgrade/商务宴请) / 闽南厝闽南菜(桥南店)(138元,food_budget_upgrade/商务宴请)
- 体验：泉州市公共文化中心泉州大剧院(184元,experience_budget_upgrade/演出) / 泉州木偶剧院(180元,experience_budget_upgrade/演出) / 泉州大开元寺(180元,experience_budget_upgrade/夜游) / 通淮关岳庙(180元,experience_budget_upgrade/夜游) / 晋江大剧院(180元,experience_budget_upgrade/演出)
- 景点：紫帽山旅游度假区(280元,attraction_budget_upgrade/旅游度假区) / 五店市传统街区(280元,attraction_budget_upgrade/旅游度假区) / 泉州海丝野生动物世界(280元,attraction_budget_upgrade/海洋馆) / 十里黄金海岸红塔湾旅游区(280元,attraction_budget_upgrade/旅游度假区) / 清源山国家重点风景名胜区(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：泉州悦华酒店(1200元,hotel_budget_upgrade/五星级酒店) / 绿岛国际酒店(1200元,hotel_budget_upgrade/五星级酒店) / 泉州泉商希尔顿酒店(1200元,hotel_budget_upgrade/五星级酒店)

### v3_request_003008 沈阳 premium 5100元 ratio_high=0.87

- 餐饮：小苍兰蛋糕甜品店(161元,food_breakfast/糕点) / 洛缦音乐餐厅(140元,food_base/特色餐厅) / 百富源·海鲜辽菜(惠工店)(96元,food_budget/精致餐厅) / 百富源·海鲜辽菜(浑河堡店)(96元,food_budget/精致餐厅) / 百富源·海鲜辽菜(和平北大街店)(96元,food_base/本地菜)
- 体验：沈阳方特欢乐世界(280元,experience_budget_upgrade/主题公园) / 沈阳东北亚国际滑雪场(暂停营业)(280元,experience_budget_upgrade/滑雪场) / 棋盘山冰雪大世界(暂停营业)(280元,experience_budget_upgrade/滑雪场) / 沈阳棋盘山国际风景旅游开发区(180元,experience_budget_upgrade/夜游) / 老北市剧场(151元,experience_budget_upgrade/演出)
- 景点：沈阳故宫博物院(280元,attraction_budget_upgrade/旅游度假区) / 北陵公园(280元,attraction_budget_upgrade/旅游度假区) / 辽宁省博物馆(280元,attraction_budget_upgrade/旅游度假区) / 海蓝星梦幻城(280元,attraction_budget_upgrade/海洋馆) / 沈阳棋盘山国际风景旅游开发区(280元,attraction_budget_upgrade/旅游度假区)
- 酒店：新民文隆美国郡家庭温泉宾馆(750元,hotel_budget_upgrade/度假酒店) / 沈阳缤纷假日酒店(医大一院沈阳站太原街店)(750元,hotel_budget_upgrade/度假酒店) / 沈阳五爱市场大南街亚朵X酒店(750元,hotel_budget_upgrade/高端酒店)
