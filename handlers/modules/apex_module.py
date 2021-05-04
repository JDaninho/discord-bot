import discord
from utils.apex_api import ApexAPI


class ApexModule:
    @staticmethod
    async def on_message(message):
        if message.content.startswith("/apex"):
            channel = message.channel
            tag, player_name = message.content.split(" ")
            apex_player = ApexAPI.get_stats(player_name)
            if apex_player is None:
                await channel.send("Invalid Origin username, ex: /apex xBaronful")

            # Gathering data for the bot to display
            display_name = apex_player['data']['platformInfo']['platformUserHandle']
            icon = apex_player['data']['platformInfo']['avatarUrl']
            rank = apex_player['data']['segments'][0]['stats']['rankScore']['metadata']['rankName']
            rank_icon = apex_player['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']
            level = apex_player['data']['segments'][0]['stats']['level']['value']
            total_kills = apex_player['data']['segments'][0]['stats']['kills']['value']
            total_damage = apex_player['data']['segments'][0]['stats']['damage']['value']
            latest_season_kills = apex_player['data']['segments'][0]['stats']['season8Kills']
            latest_season_wins = apex_player['data']['segments'][0]['stats']['season8Wins']
            active_legend_name = apex_player['data']['segments'][1]['metadata']['name']
            active_legend_icon = apex_player['data']['segments'][1]['metadata']['imageUrl']

            # Create the Embed message that the bot will show when retrieving stats
            embed = discord.Embed(colour=0xFF0000, )
            embed.set_author(name="Stats for {}".format(display_name), icon_url=icon,
                             url="https://apex.tracker.gg/apex/profile/origin/{}/overview".format(player_name))
            embed.set_thumbnail(url=rank_icon)
            embed.add_field(name="Rank", value=rank, inline=False)
            embed.add_field(name="Level", value=str(int(level)))
            embed.add_field(name="Total Kills", value=str(int(total_kills)), inline=True)
            embed.add_field(name="Total Damage", value=str(int(total_damage)), inline=True)
            embed.add_field(name=latest_season_kills['displayName'], value=str(int(latest_season_kills['value'])))
            embed.add_field(name=latest_season_wins['displayName'], value=str(int(latest_season_wins['value'])))
            embed.add_field(name="Current active legend:", value=active_legend_name, inline=False)
            embed.set_image(url=active_legend_icon)

            await channel.send(embed=embed)
