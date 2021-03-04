import discord
from discord.ext import tasks
import json
from durations import Duration
import time
from discord.ext.commands import *
import os
import sys
from dotenv import load_dotenv
load_dotenv()

command_prefix = "%"
bot = Bot(command_prefix=command_prefix, intents=discord.Intents.all(), help_command=None)

state = os.environ.get('state')
if (state=="stable"):
    bot_name = "ExpireBot"
    filename = "roles.json"
    status = ""
elif (state=="BETA"):
    bot_name = "ExpireBot BETA"
    filename = "beta_roles.json"
    status = "(BETA)"
elif (state=="ALPHA"):
    bot_name = "ExpireBot ALPHA (private)"
    filename = "alpha_roles.json"
    status = "(private ALPHA)"
else:
    print(f"ERROR: Invalid State (\"{state}\") parameter.")
    bot_name="ExpireBot?"
    filename = "unknown_roles.json"
    status = state


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

def timeformat(secs):
    dyears = 31622400
    dmonth = 2635200
    dweeks = 604800
    ddays = 86400
    dhours = 3600
    dmins = 60
    years = int(secs//dyears)
    month = int((secs - years*dyears)//dmonth)
    weeks = int((secs - years*dyears - month*dmonth)//dweeks)
    days = int((secs - years*dyears - month*dmonth - weeks*dweeks)//ddays)
    hours = int((secs - years*dyears - month*dmonth - weeks*dweeks - days*ddays)//dhours)
    minutes = int((secs - years*dyears - month*dmonth - weeks*dweeks - days*ddays - hours*dhours)//dmins)
    seconds = int((secs - years*dyears - month*dmonth - weeks*dweeks - days*ddays - hours*dhours - minutes*dmins)//1)
    milliseconds = float(round(((secs - years*dyears - month*dmonth - weeks*dweeks - days*ddays - hours*dhours - minutes*dmins - seconds)*1000), 3))
    if milliseconds.is_integer():
        int(milliseconds)
    result = []
    if years != 0:
        if years == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{years} year{s}")
    if month != 0:
        result.append(f"{month} month")
    if weeks != 0:
        if weeks == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{weeks} week{s}")
    if days != 0:
        if days == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{days} day{s}")
    if hours != 0:
        if hours == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{hours} hour{s}")
    if minutes != 0:
        if minutes == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{minutes} minute{s}")
    if seconds != 0:
        if seconds == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{seconds} second{s}")
    if milliseconds != 0:
        if years == 1:
            s = ""
        else:
            s = "s"
        result.append(f"{milliseconds} millisecond{s}")
    result = ", ".join(result)
    return result


# EVENTS
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.content)

@bot.event
async def on_ready():
    global RJD, RolesJson
    await bot.change_presence(activity=discord.Game(name=f"{command_prefix}help"))
    TestingZone = bot.get_guild(int(os.environ.get('guild_id')))
    try:
        RolesJson = open(filename, "r+")
    except:
        RolesJson = open(filename, "w+")
        json.dump({"perms": [], "roles": []}, RolesJson)
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
    print(f"ExpireBot v1.1 {status}")
    print(f"Discord API Version: {discord.__version__}")

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
        value=f"_Sets a role to expire after a certain amount of time_\n\n`{command_prefix}expire <role> <time>`\n(eg, {command_prefix}expire @examplerole 1m 12s)",
        inline=False
    )
    help_embed.add_field(
        name="Unexpire",
        value=f"_Removes a role from the list of expiring roles_\n\n`{command_prefix}unexpire <role>`\n(eg, {command_prefix}unexpire @examplerole2)",
        inline=False
    )
    help_embed.add_field(
        name="AddPerm",
        value=f"_Gives a role permissions to use this bot. You need to have `Manage Roles` Permissions to use this command._\n\n`{command_prefix}addperm <role>`",
        inline=False
    )
    help_embed.add_field(
        name="DelPerm",
        value=f"_Removes a role's permission to use this bot. You need to have `Manage Roles` Permissions to use this command._\n\n`{command_prefix}delperm <role>`",
        inline=False
    )
    help_embed.add_field(
        name="ViewRoles",
        value=f"_Displays the current settings_\n\n`{command_prefix}viewroles`",
        inline=False
    )
    help_embed.add_field(
        name="ViewPerms",
        value=f"_Displays wich Roles have permissions to configure the Bot_\n\n`{command_prefix}viewperms`",
        inline=False
    )
    help_embed.add_field(
        name="Ping",
        value=f"_Displays the bots latency. Check it before reporting Errors_\n\n`{command_prefix}ping`",
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

@bot.command()
async def viewroles(ctx: Context):
    Roles = []
    for role in RJD["roles"]:
        Roles.append(f"<@&{role[0]}>")
    expires = []
    for role in RJD["roles"]:
        expires.append(timeformat(role[1]))
    roles_embed = discord.Embed(
        title=f"{bot_name} >> Roles",
        description=f"Displays all Roles you added using {command_prefix}expire",
        colour=discord.Colour.blue()
    )
    roles_embed.add_field(
        name="Role",
        value="\n".join(Roles),
        inline=True
    )
    roles_embed.add_field(
        name="Expires After",
        value="\n".join(expires),
        inline=True
    )
    await ctx.send(embed=roles_embed)

@bot.command()
async def viewperms(ctx: Context):
    perms = []
    for role in RJD["perms"]:
        perms.append(f"<@&{role}>")
    perms_embed = discord.Embed(
        title=f"{bot_name} >> Permissions",
        description=f"Displays all Roles (you added using {command_prefix}addperm) that have permissions.",
        colour=discord.Colour.blue()
    )
    perms_embed.add_field(
        name="Role(s) with Permissions",
        value="\n".join(perms),
        inline=False
    )
    await ctx.send(embed=perms_embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round((bot.latency * 1000), 3)} ms!')

@bot.command()
@is_owner()
async def stop(ctx: Context):
    await ctx.send("Bot is shutting down...")
    sys.exit()


@bot.event
async def on_command_error(ctx: Context, err):
    await ctx.send(err)

bot.run(os.environ.get('discord_token'))
