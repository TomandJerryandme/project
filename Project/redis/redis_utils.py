import redis

from redis.sentinel import Sentinel

from rediscluster import StrictRedisCluster

# 直联模式
# 获取单独的redis连接
r = redis.Redis(host='127.0.0.1', port=6379)
# 获取一个redis连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r_pool = redis.Redis(connection_pool=pool)


# 哨兵模式   主要用于多个redis服务器，当主服务器宕机时，通过哨兵监察投票机制，将另外的从服务器设置为主服务器，当原主服务重新运行之后会变为从服务器
# sentinel = Sentinel([('192.168.1.110',16380), ('192.168.1.110', 16381), ('192.168.1.110', 16382) ], socket_timeout=0.5, sentinel_kwargs={'password': '123456'}, db=0)     # 连接哨兵服务器
# master = sentinel.master_for('mymaster', password='123456')   # 获取主服务器进行读写
# slave = sentinel.slave_for('mymaster', password='123456')     # 获取从服务器进行读取
# print(master.llen('test'))
# 集群模式
# redis_nodes = [{'host':'192.168.1.110','port':13790},{'host':'192.168.1.110','port':13791},{'host':'192.168.1.110','port':13793},{'host':'192.168.1.120','port':13794}]
# redisconn = StrictRedisCluster(startup_nodes=redis_nodes,decode_responses=True,password='123456')