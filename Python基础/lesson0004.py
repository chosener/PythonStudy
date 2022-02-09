def find_Element(self, type, value):
    '''
    method explain:查找某个元素
    parameter explain: 【type】 取值的类型包括：id\name\class_name...   【value】根据type的类型给值
    Usage:
        device.find_Element('name',"我的認證")
    '''
    logging.info("执行--------find_Element-------方法")
    try:
        if type == 'id':
            try:
                return self.driver.find_element(By.ID, value)  # 查找ID元素，存在则直接返回
            except Exception, e:
                　　　　　　　　　　　　　　　　　　　　　　　　  # appium存在元素则直接返回，不存在则跑出异常，因此必须用异常来处理不存在元素的情况
            logging.info("未找到%type--%value" % (type, value))
            return False　　　　　　　　　　　　　　　　　　　　　　　　  # 查找ID元素，不存在则返回False
            elif type == 'name':
            try:
                return self.driver.find_element(By.NAME, value)
            except Exception, e:
                logging.info("未找到%type--%value" % (type, value))
                return False
    except:
        logging.warn("此处已抛异常---------------find_Element")
        self.take_screenShot(
            "find_Element")　　　　　　　　　　　　　'''　　　　　　　　take_screenShot()自己封装的截图方法，如果你没封装就可以删除掉此句话，或者看链接将此方法添加到你封装py文　　　　　　　　件中：http://www.cnblogs.com/syw20170419/p/8280017.html　　　　　　　　　'''
        assert 'find_Element'


def click(self):
    '''
    method explain:查找某个元素
    parameter explain: 【type】 取值的类型   【value】根据type的类型给值
    Undertake method:device.find_Element(type,value)
    Usage:
        name_value == device.find_Element(type = 'name',value="我的認證")
        name_value.click()
    '''
    self.find_Element(type, self.value).click()



# 具体的封装方法在测试中调用如下：
def creat_Message(self):
        logging.info("start creat message")
        '''创建短信'''
        sleep(5)
        new = self.device.find_Element(type = 'name',value="新建")     #调用封装的find_Element方法　　　　 if new:　　　　　　　　　　　　　　　　　　　　#判断新建存在，则执行点击　　　　　　　new.click()
        elif new == False:　　　　　　　　　#判断新建不存在，则打印log
            logging.error( '新建不存在')