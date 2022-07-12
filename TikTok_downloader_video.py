import requests
from os import system
import random
	
url=str(input(f"Enter the video link from Tik Tok :"))
if "https://" not in url:
	input(" please Add https:// in your URL")

system("clear")

number_chose = input(f"""

[1] Download video no watermark
[2] Download video watermark
[3] Download picture
[4] Download music video



Choose Your Number: """)

req_login=requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={url}&key=godownloader.com").json()	

if number_chose == "1":			
	choose_it = req_login["video_no_watermark"]
	pass
elif number_chose == "2":
	choose_it=req_login["video_watermark"]
	pass
elif number_chose == "3":
	choose_it=req_login["author_cover"]	
	pass
elif number_chose == "4":
	choose_it=req_login["music_url"]
	pass
else:
	input("please choose th number between 1 to 4")

req_choose = requests.get(choose_it).content

# random_choose = str("".join(random.choice("1234567890abcdefghijklmnopqstuvwxyz")for i in range(5)))
wqmd = "wqmd"
random_choose = str("".join(random.choice("1234567890")))
for number in random_choose:
	wqmd_choose = wqmd+number
	
if number_chose == "1":	
	with open(f"{wqmd_choose}.mp4", 'wb') as file:
		file.write(req_choose)
		input(f"⌯ It has been downloaded successfully as {wqmd_choose}")
	pass
elif number_chose == "2":
	with open(f"{wqmd_choose}.mp4", 'wb') as file:
		file.write(req_choose)
		input(f"⌯ It has been downloaded successfully as {wqmd_choose}")			
	pass
elif number_chose == "3":
	with open(f"{wqmd_choose}.jpg", 'wb') as file:
		file.write(req_choose)
		input(f"⌯ It has been downloaded successfully as {wqmd_choose}")			
	pass
elif number_chose == "4":
	with open(f"{wqmd_choose}.mp3", 'wb') as file:
		file.write(req_choose)
		input(f"⌯ It has been downloaded successfully as {wqmd_choose}")			
	pass
	
		