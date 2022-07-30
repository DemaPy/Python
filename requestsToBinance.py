import json
import requests
from fake_useragent import UserAgent


ua = UserAgent()

def download_stepn():
    cookies = {
        'cid': 'Knwv7uR8',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        '_gcl_au': '1.1.2115481214.1650128700',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY_EXPIRE': '1650215100948',
        'BNC_FV_KEY': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'OptanonAlertBoxClosed': '2022-04-16T17:05:03.109Z',
        'nft-init-compliance': 'true',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'lang': 'ru',
        '_uetsid': 'a3e12740bd8311ecab6375a57dbd9a24',
        '_uetvid': '3c7720e0adca11ecaec0414900024bd4',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Apr+17+2022+09%3A23%3A47+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        'clienttype': 'web',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cid=Knwv7uR8; bnc-uuid=6b5296e4-454d-43ad-8072-18000808cd66; _gcl_au=1.1.2115481214.1650128700; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D; userPreferredCurrency=RUB_USD; BNC_FV_KEY_EXPIRE=1650215100948; BNC_FV_KEY=333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5; OptanonAlertBoxClosed=2022-04-16T17:05:03.109Z; nft-init-compliance=true; source=referral; campaign=www.binance.com; lang=ru; _uetsid=a3e12740bd8311ecab6375a57dbd9a24; _uetvid=3c7720e0adca11ecaec0414900024bd4; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+17+2022+09%3A23%3A47+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCsyIiwidGltZXpvbmVPZmZzZXQiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTAwLjAuNDg5Ni4xMjcgU2FmYXJpLzUzNy4zNiIsImxpc3RfcGx1Z2luIjoiUERGIFZpZXdlcixDaHJvbWUgUERGIFZpZXdlcixDaHJvbWl1bSBQREYgVmlld2VyLE1pY3Jvc29mdCBFZGdlIFBERiBWaWV3ZXIsV2ViS2l0IGJ1aWx0LWluIFBERiIsImNhbnZhc19jb2RlIjoiYzhkNjcwZDIiLCJ3ZWJnbF92ZW5kb3IiOiJHb29nbGUgSW5jLiAoSW50ZWwpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwsIEludGVsKFIpIFVIRCBHcmFwaGljcyA2MzAgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJFdXJvcGUvV2Fyc2F3IiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwMC4wLjQ4OTYuMTI3IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiOGRmNTg5N2NlNmJlY2U4ZGYxMzM2Zjk2OGU1ZmNjOTQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==',
        'dnt': '1',
        'fvideo-id': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'lang': 'ru',
        'origin': 'https://www.binance.com',
        'referer': 'https://www.binance.com/ru/nft/collection/stepn-x-asics-nft-sneakers-563307193154007041?keyword=STEPN+Shoebox+&orderBy=list_time&orderType=-1&isBack=1&id=565720121522372609&order=list_time%40-1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'x-trace-id': '4ef5b729-6471-41e5-b26f-2aeb740c320e',
        'x-ui-request-trace': '4ef5b729-6471-41e5-b26f-2aeb740c320e',
    }

    json_data = {
        'tradeType': '',
        'currency': '',
        'amountFrom': '',
        'amountTo': '',
        'properties': [],
        'statusList': [],
        'reSale': '',
        'keyword': 'STEPN Shoebox ',
        'orderBy': 'list_time',
        'orderType': -1,
        'page': 1,
        'rows': 16,
        'collectionId': '565720121522372609',
    }

    response = requests.post('https://www.binance.com/bapi/nft/v1/friendly/nft/layer-product-list', headers=headers, cookies=cookies, json=json_data)

    with open ('stepn.json', 'w', encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
        
    # nfts = response.json()
    # for items in nfts['data']['rows']:
    #     if items['amount']:
    #         print(items['productId'])

def download_fantasy():
    cookies = {
        'cid': 'Knwv7uR8',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        '_gcl_au': '1.1.2115481214.1650128700',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY_EXPIRE': '1650215100948',
        'BNC_FV_KEY': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'OptanonAlertBoxClosed': '2022-04-16T17:05:03.109Z',
        'nft-init-compliance': 'true',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'lang': 'ru',
        '_uetsid': 'a3e12740bd8311ecab6375a57dbd9a24',
        '_uetvid': '3c7720e0adca11ecaec0414900024bd4',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Apr+17+2022+10%3A15%3A57+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        'clienttype': 'web',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cid=Knwv7uR8; bnc-uuid=6b5296e4-454d-43ad-8072-18000808cd66; _gcl_au=1.1.2115481214.1650128700; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D; userPreferredCurrency=RUB_USD; BNC_FV_KEY_EXPIRE=1650215100948; BNC_FV_KEY=333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5; OptanonAlertBoxClosed=2022-04-16T17:05:03.109Z; nft-init-compliance=true; source=referral; campaign=www.binance.com; lang=ru; _uetsid=a3e12740bd8311ecab6375a57dbd9a24; _uetvid=3c7720e0adca11ecaec0414900024bd4; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+17+2022+10%3A15%3A57+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCsyIiwidGltZXpvbmVPZmZzZXQiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTAwLjAuNDg5Ni4xMjcgU2FmYXJpLzUzNy4zNiIsImxpc3RfcGx1Z2luIjoiUERGIFZpZXdlcixDaHJvbWUgUERGIFZpZXdlcixDaHJvbWl1bSBQREYgVmlld2VyLE1pY3Jvc29mdCBFZGdlIFBERiBWaWV3ZXIsV2ViS2l0IGJ1aWx0LWluIFBERiIsImNhbnZhc19jb2RlIjoiYzhkNjcwZDIiLCJ3ZWJnbF92ZW5kb3IiOiJHb29nbGUgSW5jLiAoSW50ZWwpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwsIEludGVsKFIpIFVIRCBHcmFwaGljcyA2MzAgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJFdXJvcGUvV2Fyc2F3IiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwMC4wLjQ4OTYuMTI3IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiOGRmNTg5N2NlNmJlY2U4ZGYxMzM2Zjk2OGU1ZmNjOTQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==',
        'dnt': '1',
        'fvideo-id': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'lang': 'ru',
        'origin': 'https://www.binance.com',
        'referer': 'https://www.binance.com/ru/nft/collection/tap-fantasy-metaverse-526724142891474945?orderBy=list_time&orderType=-1&isBack=1&id=526724142891474945&order=list_time%40-1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'x-trace-id': 'a3adfd2b-a92f-4e69-9784-62e1ebc66db5',
        'x-ui-request-trace': 'a3adfd2b-a92f-4e69-9784-62e1ebc66db5',
    }

    json_data = {
        'tradeType': '',
        'currency': '',
        'amountFrom': '',
        'amountTo': '',
        'properties': [],
        'statusList': [],
        'reSale': '',
        'keyword': '',
        'orderBy': 'list_time',
        'orderType': -1,
        'page': 1,
        'rows': 16,
        'collectionId': '526724142891474945',
    }

    response = requests.post('https://www.binance.com/bapi/nft/v1/friendly/nft/layer-product-list', headers=headers, cookies=cookies, json=json_data)

    with open ('fantasy.json', 'w', encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

def download_zombie():
    cookies = {
        'cid': 'Knwv7uR8',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        '_gcl_au': '1.1.2115481214.1650128700',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY_EXPIRE': '1650215100948',
        'BNC_FV_KEY': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'OptanonAlertBoxClosed': '2022-04-16T17:05:03.109Z',
        'nft-init-compliance': 'true',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'lang': 'ru',
        '_uetsid': 'a3e12740bd8311ecab6375a57dbd9a24',
        '_uetvid': '3c7720e0adca11ecaec0414900024bd4',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Apr+17+2022+10%3A24%3A01+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'bnc-uuid': '6b5296e4-454d-43ad-8072-18000808cd66',
        'clienttype': 'web',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cid=Knwv7uR8; bnc-uuid=6b5296e4-454d-43ad-8072-18000808cd66; _gcl_au=1.1.2115481214.1650128700; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803355c3075cf-02382321e5f938-6b3e555b-2073600-1803355c3087e4%22%7D; userPreferredCurrency=RUB_USD; BNC_FV_KEY_EXPIRE=1650215100948; BNC_FV_KEY=333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5; OptanonAlertBoxClosed=2022-04-16T17:05:03.109Z; nft-init-compliance=true; source=referral; campaign=www.binance.com; lang=ru; _uetsid=a3e12740bd8311ecab6375a57dbd9a24; _uetvid=3c7720e0adca11ecaec0414900024bd4; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+17+2022+10%3A24%3A01+GMT%2B0200+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=e0b78951-75b2-4a26-8fa2-d970b7b202fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PL%3B22&AwaitingReconsent=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCsyIiwidGltZXpvbmVPZmZzZXQiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTAwLjAuNDg5Ni4xMjcgU2FmYXJpLzUzNy4zNiIsImxpc3RfcGx1Z2luIjoiUERGIFZpZXdlcixDaHJvbWUgUERGIFZpZXdlcixDaHJvbWl1bSBQREYgVmlld2VyLE1pY3Jvc29mdCBFZGdlIFBERiBWaWV3ZXIsV2ViS2l0IGJ1aWx0LWluIFBERiIsImNhbnZhc19jb2RlIjoiYzhkNjcwZDIiLCJ3ZWJnbF92ZW5kb3IiOiJHb29nbGUgSW5jLiAoSW50ZWwpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwsIEludGVsKFIpIFVIRCBHcmFwaGljcyA2MzAgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJFdXJvcGUvV2Fyc2F3IiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwMC4wLjQ4OTYuMTI3IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiOGRmNTg5N2NlNmJlY2U4ZGYxMzM2Zjk2OGU1ZmNjOTQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==',
        'dnt': '1',
        'fvideo-id': '333bbad74fe0a6189b8a5fe6cfe4d16e8b5dd3b5',
        'lang': 'ru',
        'origin': 'https://www.binance.com',
        'referer': 'https://www.binance.com/ru/nft/collection/zombie-nfts-by-braindom-games-563307193154007041?orderBy=list_time&orderType=-1&isBack=1&id=563307193154007041&order=list_time%40-1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'x-trace-id': '74cca6cb-4ffe-432f-b9ae-677a89d82af1',
        'x-ui-request-trace': '74cca6cb-4ffe-432f-b9ae-677a89d82af1',
    }

    json_data = {
        'tradeType': '',
        'currency': '',
        'amountFrom': '',
        'amountTo': '',
        'properties': [],
        'statusList': [],
        'reSale': '',
        'keyword': '',
        'orderBy': 'list_time',
        'orderType': -1,
        'page': 1,
        'rows': 16,
        'collectionId': '563307193154007041',
    }

    response = requests.post('https://www.binance.com/bapi/nft/v1/friendly/nft/layer-product-list', headers=headers, cookies=cookies, json=json_data)

    with open ('zombie.json', 'w', encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    

def main():
    download_zombie()
    download_stepn()
    download_fantasy()


if __name__ == '__main__':
    main()
