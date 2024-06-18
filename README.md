# Public Archive

As you can see, this project has been stale for a while, I'm finally archiving it.<br />
I'm deleting this account. Feel free to restart/fork the project if you want to.<br />
Thanks to everyone!<br />
Farewell<br />
~_hxr404_


# Discord-ExpireBot

This Bot allows you to let roles expire. If you set e.g. the @voted role to 12h, the role will get removed automatically 12h after obtaining. This is individual to all users on the guild. It also saves the obtaining time into a JSON File, so if the Bot gets temporary offline, it can handle this.<br>
Join my [Discord Server](https://discord.com/invite/ptpyaEPapy) if you have any question/feedback or just want to talk.<br>

## Commands
| Command                 | Function                          |Permissions Required|
|-------------------------|-----------------------------------|--------------------|
|`%help`                  |Disply Help Embed                  |                    |
|`%expire <role> <time>`  |Set  Role to Expire                |Bot Manager         |
|`%unexpire <role> <time>`|Set Role to not Expire             |Bot Manager         |
|`%viewroles`             |View Expiring Roles                |                    |
|`%addperm <role>`        |Grant Role Bot Manager perm        |Manage Roles        |
|`%delperm <role>`        |Revoke Bot Manager perm for Role   |Manage Roles        |
|`%viewperms`             |View wich Role has Bot Manager perm|                    |
|`%ping%`                 |Display the Bot's latency          |                    |
|`%stop`                  |Stop/Shutdown the Bot              |Be the Bot's Owner  |

## Credit
This Bot is based on code not made by me. The Creator of that piece of code wants to stay private, so I can't link them. Go to legacy branch for more information.
Everything I coded afer this was either made by me or is mentioned below.
I'll probably host the bot and make it public so anyone can use it, but I currently can't afford it.<br>

Thanks to [DerSeb90](https://github.com/DerSeb90) for fixing a Critical Bug!!!

<details>
 <summary>I also want to say thank you to:</summary>
 <li> the ppl from Discord's official Python Community <a href="https://discord.gg/python">https://discord.gg/python</a></li>
 <li> the ppl from Scicraft's <a href="https://discord.com/channels/211786369951989762/423506375780466688">#coding-stuff</a> channel
 <li> the ppl from <a href="https://discord.com/channels/724417775795306530">"The Garage"</a> (F34R, Yumns. Armster15 and more)
 <li> My friends, allthough they can't code :D</li>
 <li> Everyone who uses this Bot and reports issues
</details>

## Invite
(currently only works on one server so its disabled)
https://discord.com/api/oauth2/authorize?client_id=786697105838309426&permissions=268438656&scope=bot

## Permissions
List of all Permissions the Bot needs to function properly.<br>
I recommend giving the Bot admin perms, so you can't do something wrong with the perms
| Permission                  | Why its needed                                                                                                   |
|-----------------------------|------------------------------------------------------------------------------------------------------------------|
| View Channels/Read Messages | To listen to your commands                                                                                       |
| Send Messages               | To reply to your commands so you know whats happening                                                            |
| Add Reactions               | Sometimes the Bot just reacts to your commands instead of replying                                               |
| Manage Roles                | To unassign the Role that should expire                                                                          |
| View Audit Log              | To know when somebody obtained a specific Role (to know when to remove it again)                                 |
|                             |                                                                                                                  |
| Administrator <strike>(Optional)</strike>| People reported that the Bot sometimes doesn't work properly and that giving it admin perms fixes those problems |

## Contributing
Consider giving this Repo a star if you like it and vote for the Bot at top.gg!!!<br>
Write issues and pulls! Test and Report! This helps the project.<br>
Also I don't mind donations ;)<br>
If you have any question or feedback, feel free to Contact me<br>
I'm looking for someone who can create the logo for ExpireBot. Join my Discord and go to #logo-submission

## Hosting the Bot
The Bot currently only supports 1 Guild per Bot so you need to host your own copy.<br>
You can Selfhost it ony your PC (I'd recommend to use a Raspberry Pi because its cheap and bc its easier to setup), on a VPS, or any other hosting Service.<br>
<b>Quick summary for experienced people:</b> You can either use the [.env](.env) file or environment variables to store the secrets (Using dotenv). All dependencies are listed with their PyPI/pip name in [requirements.txt](requirements.txt))<br>
<br>
<b>If you need a tutorial expand the Dropdown tag below</b>
<details>
 <summary><b>Step-by-Step Tutorial</b></summary>
 
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)]
  
 ### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.<br>![Botscreen](https://user-images.githubusercontent.com/55095883/109214314-fba8ea00-77b1-11eb-8400-b34bf79c55ce.png)<br>![add bot](https://user-images.githubusercontent.com/55095883/109363538-1bf9a700-788d-11eb-891f-4f0872378999.png)<br>![confirmation popup](https://user-images.githubusercontent.com/55095883/109363570-329ffe00-788d-11eb-8384-fc4c30a82173.png)
 * Enable Both Intents ![intents_screen](https://user-images.githubusercontent.com/55095883/109213772-4bd37c80-77b1-11eb-9d63-9c8700cfd07c.png)
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!<br>![copytoken](https://user-images.githubusercontent.com/55095883/109214153-c3a1a700-77b1-11eb-909c-c9d5cf72701b.png)

### Downloading Repo and configuring it
* Download / Clone the Repo as zip file and unpack it<br>![download](https://user-images.githubusercontent.com/55095883/111070049-2b553300-84d0-11eb-9fe9-057914517921.png)
* Change the values in .env with a text editor of your choice
 * discord_token=`(Enter the bot token that you copied from the developer portal)`
 * guild_id=`(Enter the ID of your Server. Rightclick on your Server on Discord and then click on 'Copy ID')`

### Setting Up Dependencies and Running the Bot
 
<details>
 <summary><b>For Linux (Raspberry Pi)</b></summary>
 
 * Open a Terminal in the Repo's location
 * Run `python3 -m pip install -r requirements.txt` in to install dependencies
 * You're ready to start the Bot! (`python3 ./bot/main.py` or double click main.py in the `bot` folder)
 </details>
 <details>
 <summary><b>For Windows 10</b></summary>
 
 * Install [Python](https://www.python.org/downloads/) if you don't have it
   * Recommended options:<br>
     Install for all users (as admin)<br>
     Add to path
 * open cmd (as admin) and cd to the repo
   * open the unpacked zip file in explorer
   * click the bar at the top of explorer<br>![example path](https://user-images.githubusercontent.com/55095883/111071058-b1737880-84d4-11eb-9105-7c62d1387f04.png)
   * Copy it (Press `CTRL` + `C`)
   * Press `Windows` + R and type cmd into the Window that opens<br>![run box](https://user-images.githubusercontent.com/55095883/111071394-37dc8a00-84d6-11eb-8ebf-5e4f5bb8f186.png)
   * Press `CTRL` + `SHIFT` + `ENTER` and confirm the popup with yes<br>![uac](https://user-images.githubusercontent.com/55095883/111071521-d36dfa80-84d6-11eb-8e12-15c00a699b67.png)
   * enter `cd /D ` into the command prompt and press `CTRL + V` or Rightclick -> Paste<br>![cd command](https://user-images.githubusercontent.com/55095883/111083998-bce49500-8510-11eb-8872-3af5bf39b72e.png)
   * Press `ENTER`
 * Run `pip install -r requirements.txt` to install dependencies
 * You're ready to start the Bot! (type `py bot\main.py` in the console prompt or simply double-click main.py in the `bot` folder)
 </details>
 
 <details>
 <summary><b>None of the above</b></summary>
 
 ### Downloading Repo and installing dependencies
  * install python if its not already installed
  * install the missing requirements by running `pip install -r requirements.txt` in the repo's folder
  
 </details>
 <details>
 <summary><b>Host using repl.it</b></summary>
 Note that you won't have 100% uptime<br>
 https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008
</details>
 <details>
 <summary><b>Host using Heroku (not recommended)</b></summary>
 Check out the original tutorial from https://github.com/audieni/discord-py-heroku/
 Note that Heroku doesn't have a persistent storage so you'd have to use some other storage addons. (You can't use the Bot without persistent storage)
 
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link (https://signup.heroku.com/)].

 ### How to fork the repository and set it up to work with Heroku?
 * Fork a copy of this repository by clicking the 'Fork' on the upper right-hand.
 * Create an application for Heroku by clicking [here](https://dashboard.heroku.com/new-app).
 * Under 'Settings', click on 'Reveal Config Vars' and enter the following:
   * KEY => discord_token
   * VALUE => (Enter the bot token that you copied from the developer portal)
   * Click the 'Add' button after entering all of this information.
 same for the GuildID:
   * KEY => guild_id
   * VALUE => (Enter the ID of your Server. Rightclick on your Server on Discord and then click on `Copy ID`)
   * Again, click the 'Add' button after entering all of this information.
 ![config vars](https://user-images.githubusercontent.com/55095883/103836278-e99bac80-5088-11eb-8283-b3744b3f587d.png)
 * Under 'Deploy', do the following:
   * Deployment Method => Connect your GitHub
   * App connected to GitHub => Search for the forked repository
   * Automatic Deploy => Enable Automatic Deploy (to redeploy after every commit)
   * It should look like something like this:
    ![deploy](https://user-images.githubusercontent.com/55095883/104065542-35bd2d00-5200-11eb-98e3-978ceb2af120.png)
 * Under 'Resources', do the following:
 ![worker](https://user-images.githubusercontent.com/13210233/103232638-fb52b680-4908-11eb-861d-767e59522b93.png)
   * Click on the 'Pencil' icon.
   * Switch the worker from off to on.
   * Click 'Confirm' to finalize the decision.
   * NOTE: You are allocated 550 free Dyno hours, which will not last the entire month. However, if you provide a credit card to verify your identity, you are given an additional 450 hours, which will allow your bot to run indefinitely.
</details>

<br>

### Getting an Invite Link
1. Go to your Bot's page at [Discord Developers](https://discordapp.com/developers/applications/)
2. Click on "OAuth2" and scroll down to "OAuth2 URL Generator"
3. Select the `bot` scope
![scopes](https://user-images.githubusercontent.com/55095883/114564426-98471e80-9c70-11eb-9e40-087381f9f43b.png)
4. Select all Required [Permissions](https://github.com/hxr404/Discord-ExpireBot#permissions)
5. Click on the Copy button next to the Link
6. The Invite Link is now in your Clipboard. Now just go to your Browser and paste it in the URL Bar.
</details>

## First Steps
After inviting the Bot you can start configuring it.
1. Go to the Role Settings of your Server and pull the Role of ExpireBot as high as possible. (At least higher than the Role you want to expire)
2. Choose wich Role(s) can manage the Bot using the addperm command (e.g. `%addperm @Owner`)
3. Select the Role(s) you want to expire

# FAQ
Read this before writing issues

**Q:** Where is the invite Link?<br>
**A:** The Bot currently only works for 1 Server at the time. This will be changed in a future Release. So there is no Invite Link. See [Hosting the Bot](https://github.com/hxr404/Discord-ExpireBot#hosting-the-bot) to get your own invite Link. <br>

**Q:** The Bot doesn't remove the Roles, but everything else seems to work<br>
**A:** The Bot is probably lacking Permissions. Check if the Bot's Role has all required [Permissions](https://github.com/hxr404/Discord-ExpireBot#permissions). Also make sure that the Bot's Role is higher than the Role you want to expire.<br>

**Q:** I cant use the expire command (No Permission)<br>
**A:** You neeed to configure wich Role(s) can change the Bot's settings using the `addperm` command<br>

**Q:** The Bot crashes and in the Error Message is something like "Privileged Intentes"<br>
**A:** You forgot to enable two switches on Discord Developers (see [Tutorial](https://github.com/hxr404/Discord-ExpireBot#hosting-the-bot))<br>

**Q:** The Bot crashes immediatly after startup<br>
**A:** Make sure to install all [dependencies](https://github.com/hxr404/Discord-ExpireBot#setting-up-dependencies-and-running-the-bot) and to use the lastest Version of Python. Also an invalid Token can crash the Bot. Check the .env File or the Environment Variables. If this doesn't help, check your Internet Connection<br>

**Q:** The Bot works on my Server, but not on the second one<br>
**A:** You need to host a seperate Bot for each of your Servers. MultiGuild Support is being worked on.<br>

**Q:** I like this Project! How can I help?<br>
**A:** Check [Contributing](https://github.com/hxr404/Discord-ExpireBot#setting-up-dependencies-and-running-the-bot) and [CONTRIBUTING.md](CONTRIBUTING.md)<br>

**Q:** I need help!<br>
**A:** Ask in my Discord Server, write an issue or a discussion on GitHub, or contact me directly. Same thin for giving feedback etc.

# Copyright
    Discord ExpipreBot
    Copyright (C) 2021 hxr404

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
