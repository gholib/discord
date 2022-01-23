import json


def parsingMembers(bot, channelID):
    channel_info = bot.getChannel(channelID)
    json_data = json.loads(channel_info.content)

    auto_guild_id = json_data["guild_id"]

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
            print(str(lenmembersfetched) + ' members fetched')
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(channel_id):
        bot.gateway.session.guild(auto_guild_id).large = True
        bot.gateway.fetchMembers(auto_guild_id, channel_id, keep=['username', 'presence'], wait=5)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': auto_guild_id}})
        bot.gateway.run(auto_reconnect=True)
        bot.gateway.resetSession()
        return bot.gateway.session.guild(auto_guild_id).members

    members = get_members(channelID)
    memberslist = []

    for memberID in members:
        if members[memberID]["presence"]["status"] == "offline":
            continue
        memberslist.append(memberID)
        print(memberID)

    f = open('files/users.txt', "a")
    for element in memberslist:
        f.write(element + '\n')
    f.close()