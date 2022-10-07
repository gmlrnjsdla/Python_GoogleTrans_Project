import googletrans  # 파이썬 구글번역 api 모듈

trans = googletrans.Translator()

trans_result = trans.translate('나는 한국사람입니다.', dest='en')

print(trans_result.text)
