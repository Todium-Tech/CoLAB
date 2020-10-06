import requests

My_API_Key = "d573edc801ed6ff70bba198db7f5ff2527bb2" # API Key 
shorten_url = input("Enter the URL You Want To Shorten --> ")
custom_alias = input("Enter the Custom Alias --> ")

main_link = "https://cutt.ly/api/api.php?key={}&short={}&name={}".format(My_API_Key,shorten_url,custom_alias)
result = requests.get(main_link)
data = result.json()

shortned_link = data["url"]["shortLink"]
print(shortned_link)