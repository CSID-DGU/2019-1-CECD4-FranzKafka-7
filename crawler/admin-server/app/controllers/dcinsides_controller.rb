class DcinsidesController < ApplicationController
    def months
        @months = Dcinside.group_by_month(:written_at, format: "%s%3N").count.to_a
        render json: @months
    end
    def cache_months
        @months = [["1220194800000",173],["1222786800000",192],["1225465200000",105],["1228057200000",110],["1230735600000",31],["1233414000000",19],["1235833200000",12],["1238511600000",18],["1241103600000",53],["1243782000000",23],["1246374000000",15],["1249052400000",16],["1251730800000",2],["1254322800000",2],["1257001200000",5],["1259593200000",2],["1262271600000",3],["1264950000000",116],["1267369200000",3],["1270047600000",0],["1272639600000",0],["1275318000000",0],["1277910000000",0],["1280588400000",600],["1283266800000",485],["1285858800000",801],["1288537200000",266],["1291129200000",262],["1293807600000",231],["1296486000000",55],["1298905200000",0],["1301583600000",0],["1304175600000",0],["1306854000000",0],["1309446000000",0],["1312124400000",0],["1314802800000",0],["1317394800000",0],["1320073200000",0],["1322665200000",0],["1325343600000",109],["1328022000000",1391],["1330527600000",246],["1333206000000",41],["1335798000000",5],["1338476400000",8],["1341068400000",1],["1343746800000",3],["1346425200000",9],["1349017200000",8],["1351695600000",0],["1354287600000",4],["1356966000000",32],["1359644400000",7],["1362063600000",34],["1364742000000",0],["1367334000000",2],["1370012400000",6],["1372604400000",4],["1375282800000",2],["1377961200000",1],["1380553200000",5],["1383231600000",3],["1385823600000",2],["1388502000000",2],["1391180400000",0],["1393599600000",0],["1396278000000",0],["1398870000000",0],["1401548400000",0],["1404140400000",0],["1406818800000",0],["1409497200000",1],["1412089200000",3],["1414767600000",1],["1417359600000",0],["1420038000000",0],["1422716400000",2],["1425135600000",2],["1427814000000",7],["1430406000000",0],["1433084400000",0],["1435676400000",1],["1438354800000",2],["1441033200000",10],["1443625200000",33],["1446303600000",41],["1448895600000",72],["1451574000000",80],["1454252400000",430],["1456758000000",390],["1459436400000",379],["1462028400000",41],["1464706800000",13],["1467298800000",415],["1469977200000",86],["1472655600000",1766],["1475247600000",6],["1477926000000",63],["1480518000000",60],["1483196400000",35],["1485874800000",104],["1488294000000",44],["1490972400000",18],["1493564400000",14],["1496242800000",6],["1498834800000",10],["1501513200000",10],["1504191600000",42],["1506783600000",17],["1509462000000",1764],["1512054000000",75],["1514732400000",0],["1517410800000",110],["1519830000000",103],["1522508400000",50],["1525100400000",37],["1527778800000",0],["1530370800000",46],["1533049200000",96],["1535727600000",34],["1538319600000",54],["1540998000000",66],["1543590000000",33],["1546268400000",47],["1548946800000",0],["1551366000000",25],["1554044400000",239],["1556636400000",30],["1559314800000",5]]
        render json: @months
    end
end
