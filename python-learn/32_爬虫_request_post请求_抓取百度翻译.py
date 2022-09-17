import requests

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    "Cookie": "BIDUPSID=EB22B91AC066C48DCBFFB91E5688CE15; PSTM=1650465892; BD_UPN=12314753; newlogin=1; BDUSS=JDZXNpeVdlM1poRThrS3dCdi1ueWcwd0NtNjZoeVYwWkpkTlEyZE53fjR0fmhpRVFBQUFBJCQAAAAAAAAAAAEAAAATCWcY2K3O9MjV2K3s4cnx1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgq0WL4KtFiQX; BDUSS_BFESS=JDZXNpeVdlM1poRThrS3dCdi1ueWcwd0NtNjZoeVYwWkpkTlEyZE53fjR0fmhpRVFBQUFBJCQAAAAAAAAAAAEAAAATCWcY2K3O9MjV2K3s4cnx1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgq0WL4KtFiQX; BA_HECTOR=a024840gak052hah04amv1621hgo5pt17; BAIDUID_BFESS=C1B7E585E91BE6E4CA4EE7229DAE234C:FG=1; ZFY=J1:BFxLgmbvUvp4zNlX:AZKEo:ADgzHbLu7suGHowpC:B:BM:C; ab_sr=1.0.1_MDY2MmU4YjI4YWFkODU2MjA5MTA0ZDBmZDkxYzY3NzYzZTBiYzQ0NGVkYzczNzhiNjBkMGYzMjE5NTM5YTc1ZWRiNzFiOGM3Mzg4OWZhYjlhZWRlMGZhODkwMjE1MDI0YmE3YjZmOTQxMWY2ZGJiY2MwZjAzNDE2ZWEyNDRlMjRlN2Q3ZDZmMzZkYzQwYzk3MjJjYjRjYjVhZWIxNWExMQ==; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=7; channel=baidusearch; B64_BOT=1; COOKIE_SESSION=349_0_5_3_21_4_1_0_3_4_950_1_651_0_62_0_1661736827_0_1661736765%7C9%230_0_1661736765%7C1; H_PS_PSSID=36548_36885_37144_37136_26350_22158; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; sugstore=0; H_PS_645EC=54b6auHfClVljQPtQmjXEuD2KYkRt5Wi6skJhJMbUBzmdDiV07TLFyu8BbcdXcnayrQI; baikeVisitId=440abe29-c9e2-4cab-b607-3e42d1c0e001; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=C1B7E585E91BE6E4CA4EE7229DAE234C:FG=1"
}

data = {
    'kw': 'eye'
}

#   这个要加上, 不然会报错
requests = requests.Session()
requests.trust_env = False

#   第一个参数 url 请求路径
#   第二个参数 data 请求参数
#   第三个参数 json (暂时用不上)
#   第四个参数 kwargs 字典
response = requests.post(url=url, data=data, headers=headers)
import json
content = response.text
#   注意,load是文件, loads是内容
#   obj = json.loads(content, encoding = "utf-8"), 3.9版本弃用了
#   可以用 obj = json.loads(content.encode("utf-8"))
obj = json.loads(content.encode("utf-8"))
print(obj)
