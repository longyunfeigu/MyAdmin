# admin 的流程
1. 启动
    发现所有app下写的admin.py文件
    import admin
    def autodiscover():
         autodiscover_modules('admin', register_to=site)    
2. 注册
      单例模式    -- 文件导入方式
3. 设计urls
      根据模型自动得到对应的url
      
      
# zadmin 流程
1. 启动
    启动会调用 settings.py 的 'Zadmin.apps.ZadminConfig',
    会自动调用  ZadminConfig 这个类的ready 方法，可以在这个里面autodiscover
2. 注册
3. 设计urls
    二级url放到了ZModelAdmin，因为在这个类的对象里可以获取model
    从而可以获取数据通过render渲染到html文件