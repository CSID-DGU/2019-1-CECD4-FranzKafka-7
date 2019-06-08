class TwittersController < ApplicationController
    def months
        @months = Twitter.group_by_month(:p_date, format: "%s%3N").count.to_a
        render json: @months
    end
    def cache_months
        @months = [["1257001200000",56],["1259593200000",195],["1262271600000",2255],["1264950000000",8544],["1267369200000",4094],["1270047600000",2923],["1272639600000",1428],["1275318000000",1339],["1277910000000",1583],["1280588400000",1082],["1283266800000",1996],["1285858800000",2531],["1288537200000",2568],["1291129200000",1567],["1293807600000",2034],["1296486000000",4130],["1298905200000",125096],["1301583600000",26422],["1304175600000",10634],["1306854000000",6271],["1309446000000",8920],["1312124400000",8609],["1314802800000",5513],["1317394800000",5954],["1320073200000",5821],["1322665200000",3467],["1325343600000",7318],["1328022000000",6910],["1330527600000",10760],["1333206000000",8246],["1335798000000",6364],["1338476400000",5345],["1341068400000",5590],["1343746800000",11434],["1346425200000",8487],["1349017200000",6944],["1351695600000",5613],["1354287600000",8882],["1356966000000",3292],["1359644400000",10059],["1362063600000",3418],["1364742000000",12039],["1367334000000",6025],["1370012400000",3304],["1372604400000",3115],["1375282800000",3893],["1377961200000",3879],["1380553200000",5135],["1383231600000",4564],["1385823600000",2639],["1388502000000",2411],["1391180400000",2350],["1393599600000",5186],["1396278000000",9066],["1398870000000",4466],["1401548400000",2976],["1404140400000",4956],["1406818800000",6980],["1409497200000",5444],["1412089200000",5521],["1414767600000",11431],["1417359600000",21682],["1420038000000",39987],["1422716400000",45586],["1425135600000",34851],["1427814000000",39941],["1430406000000",50018],["1433084400000",35108],["1435676400000",37750],["1438354800000",39559],["1441033200000",29919],["1443625200000",28848],["1446303600000",30269],["1448895600000",38991],["1451574000000",40680],["1454252400000",42335],["1456758000000",29898],["1459436400000",57746],["1462028400000",34700],["1464706800000",30158],["1467298800000",59897],["1469977200000",34882],["1472655600000",223018],["1475247600000",49140],["1477926000000",41103],["1480518000000",41653],["1483196400000",40910],["1485874800000",38900],["1488294000000",31276],["1490972400000",28380],["1493564400000",30293],["1496242800000",24790],["1498834800000",29863],["1501513200000",29722],["1504191600000",26437],["1506783600000",24588],["1509462000000",132168],["1512054000000",27906],["1514732400000",28612],["1517410800000",48343],["1519830000000",17851],["1522508400000",18583],["1525100400000",19152],["1527778800000",14024],["1530370800000",20758],["1533049200000",19696],["1535727600000",22834],["1538319600000",19531],["1540998000000",17817],["1543590000000",18455],["1546268400000",19681],["1548946800000",24912],["1551366000000",20203],["1554044400000",20562],["1556636400000",20479],["1559314800000",334]]
        render json: @months
    end
end
