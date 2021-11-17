import requests
import re
import os
import time


def save_to_txt(results, name, i):
    pass


def get_parse_page(pn,name):
    for i in range(int(pn)):
        print('正在获取第{}页'.format(i+1))

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' % (name, i * 20)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'
        }

        response = requests.get(url, headers=headers)
        html = response.content.decode()

        results = re.findall('"objURL":"(.*?)",', html)
        save_to_txt(results, name, i)



# 保存图片到本地
def save_to_txt(results, name, i):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    proxies = {
        "http": "",
        "https": "",
    }

    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # 下载图片
    for result in results:
        print('正在保存第{}个'.format(j))
        pic = requests.get(result, headers=headers, proxies=proxies)
        try:

            print(result)
            pic = requests.get(result, headers=headers, proxies=proxies)
            print(pic)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 把图片保存到文件夹
        file_full_name = './' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)

        j += 1


if __name__ == "__main__":
    name = input('成龙：')
    pn = input('3:')
    get_parse_page(pn, name)
    pass


print

print(325+5142)

name = 'zhangjinhui'
name1 = name.upper()
print(name1)


name = input('what is your name ? ')
print('hello'+name)


