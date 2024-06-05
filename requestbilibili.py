import requests

headers = {
    "Cookie": "DedeUserID=443919340; DedeUserID__ckMd5=9ca22e395ff89733; is-2022-channel=1; buvid_fp_plain=undefined; hit-new-style-dyn=1; hit-dyn-v2=1; enable_web_push=DISABLE; blackside_state=0; CURRENT_BLACKGAP=0; FEED_LIVE_VERSION=V_HEADER_LIVE_NEW_POP; PVID=1; CURRENT_QUALITY=80; fingerprint=3eac52398c81e7a67b99dc6926b8a057; buvid_fp=3eac52398c81e7a67b99dc6926b8a057; _uuid=108B3BA69-C7B8-934B-A1027-10810CAD2D716772789infoc; buvid4=3F344FBA-538E-C98C-CC0B-0757190179DC73511-024052006-0OQFkKd5ER57lJyybua4EA%3D%3D; home_feed_column=5; browser_resolution=1528-750; buvid3=4495A5B7-94EC-457C-858B-2D12F8E9CEEC11802infoc; b_nut=1717491311; bsource=search_bing; SESSDATA=907cfae4%2C1733043323%2Cd55f6%2A61CjD30qCBLd3yFFnnMIpDFcamVbjVAiipqceaod6sAIzapUGGVh7n3umcsKCi9rgctH8SVlRDbVpCS2k0UU93eWtYRFlxakc2a0pXTXhGbmVVMjdLbm1SRFlxRTVrOXBPMWQtd1FDU0dfU2dfNEc3V0JBMUItejExbHZkbmRNdGxtSUF1SGtFQkZBIIEC; bili_jct=855b5ffe5e467b91cc0f585745280100; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc3NTA1MzcsImlhdCI6MTcxNzQ5MTI3NywicGx0IjotMX0.90JeHR31KNoZaT3XSxQtbLJKNukpewF03RCYEZdd-Co; bili_ticket_expires=1717750477; rpdid=|(uR|kJmRmRk0J'u~u~RmuJ)|; bp_t_offset_443919340=939106475121311830; sid=8ubxyuoo; b_lsid=D10E102EFA_18FE73A90AC; CURRENT_FNVAL=16; header_theme_version=CLOSE",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
}#cookie, UA
#cookie：nav中有
param = {
    "search_type": "video",
    "_extra": "",
    "context": "",
    "page": "1",
    "page_size": "5",#决定爬多少链接
    "order": "click",
    "from_source": "",
    "keyword": "小黑子",#此处为搜索内容
}
#&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page=1&page_size=42&order=click&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=
resp = requests.get("https://api.bilibili.com/x/web-interface/wbi/search/type", headers=headers, params=param)#type?category_id那个包
data = resp.json()
if data['code'] == 0:
    data = data['data']['result']
    for video in data:
        print(video['arcurl'])#得到前五个链接