from CCPRestSDK import REST
import ConfigParser

accountSid = '您的主账号';
# 说明：主账号，登陆云通讯网站后，可在控制台首页中看到开发者主账号ACCOUNT SID。

accountToken = '您的主账号Token';
# 说明：主账号Token，登陆云通讯网站后，可在控制台首页中看到开发者主账号AUTH TOKEN。

appId = '您的应用ID';
# 请使用管理控制台中已创建应用的APPID。

serverIP = 'app.cloopen.com';
# 说明：请求地址，生产环境配置成app.cloopen.com。

serverPort = '8883';
# 说明：请求端口 ，生产环境为8883.

softVersion = '2013-12-26';  # 说明：REST API版本号保持不变。


def sendTemplateSMS(to, datas, tempId):
    # 初始化REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    for k, v in result.iteritems():
        if k == 'templateSMS':
            for k, s in v.iteritems():
                print
                '%s:%s' % (k, s)
        else:
            print
            '%s:%s' % (k, v)