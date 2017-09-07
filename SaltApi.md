SaltApi
====
自定义SaltApi工具类

配置应用程序
----
```python3
初始化方式如下：
  salt = Salt(app)
or
  salt = Salt()
  salt.init_app(app)
```

已实现方法
----
* minions
* run

方法使用方式：
----

#### minions(args:mid=None)
说明：获取master端的客户端信息，有mid参数时获取指定minion节点的信息，没有mid则获取的是当前master的所有minion的grains信息

参数：
* mid (可选) 客户端的ID

使用场景：资产收集
```python3
# 获取所有minion信息
all_minions = salt.mid()
print(all_minions)

# 获取单个minion信息
single_minion = salt.mid('master')
```
************

#### run(args:method, module, tgt, args):
说明：执行Modules,相当于在命令行执行一个模块

参数:
* method: 执行方法（同步或异步）如果为异步则会返回执行的jid
* tgt：目标，也就是minion
* module: 模块
* args：该模块的参数，例如 `salt '*' cmd.run 'ls'` 其中`ls` 即为参数

使用场景：命令执行、执行模块
```python3
method = 'local'
module = 'cmd.run'
tgt = ['master','minion']
args = 'ls cwd=/tmp'
ret = salt.run(method=method,module=module,tgt=tgt,args=args)
print(ret)
```
