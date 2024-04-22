import requests

BASE_URL = "https://trex-runner.com"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

session = requests.Session()
session.headers["User-Agent"] = USER_AGENT
session.headers["Origin"] = BASE_URL
session.headers["Referer"] = BASE_URL + "/"

username = input("Username: ")
score = int(input("Score: "))

page_response = session.get(BASE_URL + "/")
token = page_response.text.split("id=\"token\" value=\"")[1].split("\"")[0]

targetScore = round(score)
distanceRan = targetScore / 0.025
timeSpent = round(targetScore * 57)

data={
    "name": username,
    "points": score,
    "dist": distanceRan,
    "t": timeSpent,
    "token": token
}
print(data)

score_response = session.post(
    BASE_URL + "/ajax/qufw/",
    data=data
)

print(str(score_response))
print(score_response.text)
