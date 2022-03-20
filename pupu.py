import requests
import datetime
import time


# 获取数据
def getData():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/831b632e-12bd-4c23-a6fd-a18749d8d508/ed60af11-25b0-48b8-bc5b-f9136d9f89ad'
    # 浏览器标识
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    # 发送请求给url
    productData = requests.get(url, headers=headers).json()
    return productData


def getProduct():
    # 获取值
    response = getData()
    name = response['data']['name']
    spec = response['data']['spec']
    price = str(response['data']['price'] / 100)
    guide = str(response['data']['market_price'] / 100)
    title = response['data']['sub_title']
    text = response['data']['custom_tag_text']
    # 输出商品信息
    print('---------------' + '商品: ' + name + '---------------')
    print('规格:' + spec)
    print('价格: ' + price)
    print('原价/折扣价: ' + guide + '/' + price)
    print('详细内容: ' + spec + '; ' + title + text)
    print('---------------' + '商品: ' + name + '的价格波动---------------')


def monitor():
    # 监控价格
    while 1:
        # 获取值
        response = getData()
        price = str(response['data']['price'] / 100)
        # 获取当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('当前时间为' + now + ', ' + '价格为' + price)
        time.sleep(1)


# 调用函数
def run():
    getProduct()
    monitor()


# 运行
run()