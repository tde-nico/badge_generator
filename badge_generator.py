import requests


# basic badge generator for github

# search for logos:	 https://simpleicons.org/
# site for badges:	  https://shields.io/

def download(url, fname):
	get_response = requests.get(url)
	name = url.split('/')[-1]
	with open(fname, "wb") as out_file:
		out_file.write(get_response.content)


def main():
	name = input("Name: ")
	color = input("Color: ") # can be word, hex, RGB($r,$g,$d) (in case of wrong spelling it will be green)
	logo_name =  input("logo: ")
	if logo_name != '':
		logo = logo_name.replace(" ", "") # it's possible that doesn't exist
	else:
		logo = name.replace(" ", "")
	name = name.replace(" ", "%20")
	url = "https://img.shields.io/badge/" + name + "-" + color + "?logo=" + logo + "&logoColor=white"
	print(url)
	try:
		download(url, name + ".svg")
	except Exception as e:
		print("[-] Error: " + str(e))

if __name__ == "__main__":
	main()
