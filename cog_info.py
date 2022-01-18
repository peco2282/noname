import discord
from discord.ext import commands
from permissionvalue import permissions


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx: commands.Context):
        user_name = ctx.author.name
        date = ctx.author.created_at.strftime('%Y年 %m月 %d日 %H:%M:%S:%f')
        avatar = ctx.author.avatar
        status = ctx.author.desktop_status
        avatarimg = ctx.author.banner
        joindata = ctx.author.joined_at.strftime('%Y年 %m月 %d日 %H:%M:%S:%f')
        role_info = ctx.author.roles
        role_info.reverse()
        perm = permissions(ctx)

        pm = perm[0]
        val = perm[1]
        s = ''
        for i in role_info:
            if i.name == '@everyone':
                s += '@everyone'
            else:
                s += f'{i.mention},  '

        embed = discord.Embed(color=discord.Colour.green(), title=f'{ctx.author.name} のユーザー情報')
        embed.add_field(name='-----名前-----', value=f'**{user_name}**')
        embed.add_field(name='-ユーザー作成日時-', value=date, inline=False)
        embed.add_field(name='--ユーザー参加日--', value=joindata, inline=False)
        embed.add_field(name='---ロール一覧---', value=s)
        embed.add_field(name='--状態--', value=f'**{status}**', inline=False)
        embed.add_field(name=f'----{val}----', value=pm, inline=False)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
