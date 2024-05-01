import pymongo

# 連接 MongoDB
mc = pymongo.MongoClient('mongodb://localhost:27017/')
db = mc['SportsCenterTraffic']
sc_col = db["SportsCenter"]
sc_col.create_index("CenterId", unique=True)

# 插入資料
# 台北市
qry = {"CenterId": 1, "CenterName": "北投運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://www.btsport.org.tw/", "GymCapacity": 60, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 2, "CenterName": "士林運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://www.slsc-taipei.org/", "GymCapacity": 100, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 3, "CenterName": "內湖運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://nhsc.cyc.org.tw/", "GymCapacity": 130, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 4, "CenterName": "南港運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://ngsc.cyc.org.tw/", "GymCapacity": 110, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 5, "CenterName": "信義運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://xysc.teamxports.com/", "GymCapacity": 65, "PoolCapacity":100}}, upsert=True)
qry = {"CenterId": 6, "CenterName": "大同運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://www.dtsc-wdyg.com.tw/", "GymCapacity": 90, "PoolCapacity":250}}, upsert=True)
qry = {"CenterId": 7, "CenterName": "中山運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://cssc.cyc.org.tw/", "GymCapacity": 50, "PoolCapacity":150}}, upsert=True)
qry = {"CenterId": 8, "CenterName": "中正運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://www.tpejjsports.com.tw/", "GymCapacity": 100, "PoolCapacity":250}}, upsert=True)
qry = {"CenterId": 9, "CenterName": "大安運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://www.daansports.com.tw/", "GymCapacity": 80, "PoolCapacity":250}}, upsert=True)
qry = {"CenterId": 10, "CenterName": "文山運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "台北市", "Website": "https://wssc.cyc.org.tw/", "GymCapacity": 85, "PoolCapacity":200}}, upsert=True)

# 新北市
qry = {"CenterId": 11, "CenterName": "新莊國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://www.xzsports.com.tw/", "GymCapacity": 150, "PoolCapacity":350}}, upsert=True)
qry = {"CenterId": 12, "CenterName": "蘆洲國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://lzcsc.cyc.org.tw/", "GymCapacity": 75, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 13, "CenterName": "淡水國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "http://www.tssc.tw/", "GymCapacity": 70, "PoolCapacity":400}}, upsert=True)
qry = {"CenterId": 14, "CenterName": "三重國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "http://www.scsports.com.tw/", "GymCapacity": 60, "PoolCapacity":400}}, upsert=True)
qry = {"CenterId": 15, "CenterName": "土城國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://tccsc.cyc.org.tw/", "GymCapacity": 60, "PoolCapacity":230}}, upsert=True)
qry = {"CenterId": 16, "CenterName": "板橋國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://www.bqsports.com.tw/", "GymCapacity": 80, "PoolCapacity":400}}, upsert=True)
qry = {"CenterId": 17, "CenterName": "永和國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://yhcsc.cyc.org.tw/", "GymCapacity": 65, "PoolCapacity":300}}, upsert=True)
qry = {"CenterId": 18, "CenterName": "汐止國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://xzcsc.cyc.org.tw/", "GymCapacity": 80, "PoolCapacity":200}}, upsert=True)
qry = {"CenterId": 19, "CenterName": "樹林國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://www.ntcslsports.com.tw/", "GymCapacity": 90, "PoolCapacity":250}}, upsert=True)
qry = {"CenterId": 20, "CenterName": "三鶯國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://scysports.com.tw/", "GymCapacity": 150, "PoolCapacity":350}}, upsert=True)
qry = {"CenterId": 21, "CenterName": "林口國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://lkcsc.cyc.org.tw/", "GymCapacity": 80, "PoolCapacity":230}}, upsert=True)
qry = {"CenterId": 22, "CenterName": "五股國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://wgsc.chanchao.com.tw/", "GymCapacity": 60, "PoolCapacity":100}}, upsert=True)
qry = {"CenterId": 23, "CenterName": "新店國民運動中心"}
sc_col.find_one_and_update(qry, {"$set": {"City": "新北市", "Website": "https://www.xdsports.com.tw/", "GymCapacity": 100, "PoolCapacity":180}}, upsert=True)
