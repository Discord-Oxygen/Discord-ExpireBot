import discord
from discord.ext import tasks
import json
from durations import Duration
import time
from discord.ext.commands import *
command_prefix = "%"
bot = Bot(command_prefix=command_prefix, intents=discord.Intents.all(), help_command=None)
bot_name = "Expire Bot"


def jsondump(v: dict):
    RolesJson.seek(0)
    json.dump(v, RolesJson)
    RolesJson.truncate()
    RolesJson.seek(0)


async def has_perms(ctx):
    for b in ctx.author.roles:
        if b.id in RJD["perms"]:
            return True
    await ctx.send("You don't have the permissions to do that!")
    return False


# EVENTS
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.content)

@bot.event
async def on_ready():
    global RJD, RolesJson
    await bot.change_presence(activity=discord.Game(name=f"{command_prefix}help"))
    TestingZone = bot.get_guild(Your GuildID Goes here!!!!!!)
    try:
        RolesJson = open("roles.json", "r+")
    except:
        RolesJson = open("roles.json", "w+")
        json.dump({{"perms": [], "roles": []}, RolesJson)
        RolesJson.seek(0)
    # Setup
    RJD = json.load(RolesJson)
    RolesJson.seek(0)
    for role in RJD["roles"]:
        for member in RJD[role[0]]:
            if member[1] <= time.time():
                try:
                    await TestingZone.get_member(member[0]).remove_roles(TestingZone.get_role(int(role[0])), reason="expired")
                except:
                    pass
                RJD[role[0]].remove(member)
            else:
                break
    jsondump(RJD)
    current_time = time.time()
    for role in RJD["roles"]:
        for member in RJD[role[0]]:
            member[1] -= current_time
    # Lets you know that the bot is ready and what version you're running
    print("Bot is ready")
    print(f"Version: {discord.__version__}")

    async def pushList(n: str):
        try:
            RJD[n][0][1] = RJD[n][0][1]
        except IndexError:
            return False
        if RJD[n][0][1] <= 0:
            try:
                await TestingZone.get_member(RJD[n][0][0]).remove_roles(TestingZone.get_role(int(n)), reason="expired")
            except:
                pass
            del RJD[n][0]
            RolesJson.seek(0)
            r = json.load(RolesJson)
            del r[n][0]
            jsondump(r)
            for memberlist in RJD[n]:
                memberlist[1] -= 0.5
            await pushList(n)
        else:
            return True

    @tasks.loop(seconds=0.5)
    async def dec():
        for role in RJD["roles"]:
            n = role[0]
            if not await pushList(n):
                continue
            for memberlist in RJD[n]:
                memberlist[1] -= 0.5
    dec.start()


@bot.event
async def on_member_update(before:discord.Member, after:discord.Member):
    RolesJson.seek(0)
    a = json.load(RolesJson)
    RolesJson.seek(0)
    for role in after.roles:
        if role in before.roles:
            continue
        h = str(role.id)
        for roleTup in a["roles"]:
            if h == roleTup[0]:
                RJD[h].append([after.id, roleTup[1]])
                a[h].append([after.id, roleTup[1] + round(time.time())])
    jsondump(a)


# Command to set a role to expire
@bot.command()
@check(has_perms)
async def expire(ctx: Context, role: discord.Role, *, time: str):
    print(role.permissions)
    ExpireDuration = Duration(time)
    ExpireDuration = ExpireDuration.to_seconds()
    if int(ExpireDuration) == 0:
        await ctx.send(f"Check your syntax, see {command_prefix}help")
        return
    RolesJsonData = json.load(RolesJson)
    RolesJson.seek(0)
    found = False
    t = str(role.id)
    for ExpiringRole in RolesJsonData["roles"]:
        if ExpiringRole[0] == t:
            for memberlist in RJD[t]:
                memberlist[1] -= (ExpiringRole[1] - ExpireDuration)
            for memberlist2 in RolesJsonData[t]:
                memberlist2[1] -= (ExpiringRole[1] - ExpireDuration)
            ExpiringRole[1] = ExpireDuration
            RJD["roles"][RolesJsonData["roles"].index(ExpiringRole)][1] = ExpireDuration
            print(RolesJsonData)
            found = True
            break
    if not found:
        RJD["roles"].append([t, ExpireDuration])
        RJD[t] = []
        RolesJsonData["roles"].append([t, ExpireDuration])
        RolesJsonData[t] = []
    jsondump(RolesJsonData)
    await ctx.message.add_reaction("✅")


@bot.command()
@check(has_perms)
async def unexpire(ctx, role: discord.Role):
    RolesJson.seek(0)
    RolesJsonData = json.load(RolesJson)
    RolesJson.seek(0)
    for ExpiringRole in RolesJsonData["roles"]:
        if ExpiringRole[0] == str(role.id):
            RolesJsonData["roles"].remove(ExpiringRole)
            RJD["roles"].remove(ExpiringRole)
            del RolesJsonData[str(role.id)]
            del RJD[str(role.id)]
    jsondump(RolesJsonData)
    await ctx.message.add_reaction("✅")


@bot.command(name="help")
async def _help(ctx: discord.ext.commands.Context):
    help_embed = discord.Embed(
        title=f"{bot_name} >> Help",
        description="Commands",
        colour=discord.Colour.blue()
    )
    help_embed.add_field(
        name="Expire",
        value=f"_Sets a role to expire after a certain amount of time_\n\n{command_prefix}expire <role> <time>\n(eg, {command_prefix}expire @examplerole 1m 12s)",
        inline=False
    )
    help_embed.add_field(
        name="Unexpire",
        value=f"_Removes a role from the list of expiring roles_\n\n{command_prefix}unexpire <role>\n(eg, {command_prefix}unexpire @examplerole2)",
        inline=False
    )
    help_embed.add_field(
        name="AddPerm",
        value=f"_Gives a role permissions to use this bot_\n\n{command_prefix}addperm <role>",
        inline=False
    )
    help_embed.add_field(
        name="DelPerm",
        value=f"_Removes a role's permission to use this bot_\n\n{command_prefix}delperm <role>",
        inline=False
    )
    await ctx.send(embed=help_embed)


@bot.command()
@has_permissions(manage_roles=True)
async def addperm(ctx: Context, role: discord.Role):
    r = role.id
    if r not in RJD["perms"]:
        RJD["perms"].append(r)
        y = json.load(RolesJson)
        RolesJson.seek(0)
        y["perms"].append(r)
        jsondump(y)
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("That role already has permissions!")


@bot.command()
@has_permissions(manage_roles=True)
async def delperm(ctx: Context, role: discord.Role):
    r = role.id
    if r in RJD["perms"]:
        RJD["perms"].remove(r)
        y = json.load(RolesJson)
        RolesJson.seek(0)
        y["perms"].remove(r)
        jsondump(y)
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("I don't think that role had permissions :confused:")

@bot.event
async def on_command_error(ctx: Context, err):
    await ctx.send(err)

bot.run('token')
