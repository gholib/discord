import discum
import parsingUsersID

f_token = open("files/token.txt")

token = f_token.readline()
bot = discum.Client(token=token)
print("👀 scanning channels")

f_channels = open("files/channels.txt", "r")
channels = [line.rstrip() for line in f_channels]
for channel_id in channels:
    parsingUsersID.parsingMembers(bot, channel_id)
print(f'🌐 scanning end.')