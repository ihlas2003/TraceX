
import requests

def check_username (username):
	print ("\n-----------------------------------------")
	print (f" '{username}' - searching")

	sites = {
		"Github" : f"https://github.com/{username}/",
		"Instagram" : f"https://www.instagram.com/{username}/",
		"Facebook" : f"https://www.facebook.com/{username}/",
		"LinkedIn" : f"https://www.linkedin.com/in/{username}/",
		"TikTok" : f"https://www.tiktok.com/@{username}/",
		"Pinterest" : f"https://www.pinterest.com/{username}/",
		"Tryhackme" : f"https://tryhackme.com/api/user/exist/{username}/",
		}

	headers = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
		}


	for site_name , url in sites.items():
		try :
			responce = requests.get (url, headers=headers, timeout = 55)

			if responce.status_code == 200:
				print (f"{site_name} user is there {url} ")
		
			elif responce.status_code == 404:
				print (f"{site_name} User is not there ")

			else:

				print (f"{site_name} something went wrong! or Security Blocked the Request (code: {responce.status_code})")
	
		except Exception as e:
			print (f"{site_name} Searching Error.....! Reason {e}")


	print ('----------------------------------------\n')

if __name__ == "__main__":
	target_user = input ("Enter your User name (e.g. ihlas) : ")

	check_username(target_user)
