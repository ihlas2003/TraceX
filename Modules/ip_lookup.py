
import requests

def get_ip_location (ip_address):
	print ("-------------------------------")
	print (f"{ip_address} - Searching.....")

	url = f"http://ip-api.com/json/{ip_address}"

	try:
		response = requests.get(url).json()

		if response['status'] == 'success':
			print ("Location found!")
			print (f"City : {response ['city']}")
			print (f"Country : {response['country']}")
			print (f"ISP : {response['ISP']}")

		else:
			print ("Oops! Not Found.....")

	except Exception as e:
		print ("Something went wrong!" , e)
		
	print ("---------------------------------------------")

if __name__ == "__main__":
	target_ip = input ("Enter Target's IP address (192.168.1.10) : ")
	get_ip_location (target_ip)
