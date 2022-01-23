import discum
import json
import time
import random


def save(data):
    f_file = open("files/blacklist.txt", "w")
    for s in data:
        f_file.write(s + "\n")
    f_file.close()


f_blacklist = open("files/blacklist.txt", "r")
blacklist_ids = [line.rstrip() for line in f_blacklist]
blacklist = []
for blacklist_id in blacklist_ids:
    blacklist.append(blacklist_id)
f_blacklist.close()

f_token = open("files/token.txt")
token = f_token.readline()
f_token.close()

bot = discum.Client(token=token)

f_message = open("files/message.txt", "r")
message = ''.join(f_message.readlines())
f_message.close()

f_users = open("files/users.txt", "r")
users = [line.rstrip() for line in f_users]

for user_id in users:
    if user_id in blacklist:
        continue

    response = bot.createDM(user_id)
    json_data = json.loads(response.content)
    channel_id = json_data["id"]

    time.sleep(random.randint(30, 120))
    bot.sendMessage(channel_id, message)
    save(blacklist)
