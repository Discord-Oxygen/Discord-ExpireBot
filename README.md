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
 <li> the guys from Discord's official Python Community <a href="https://discord.gg/python">https://discord.gg/python</a></li>
 <li> the guys from Scicraft's <a href="https://discord.com/channels/211786369951989762/423506375780466688">#coding-stuff</a> channel
 <li> the guys from <a href="https://discord.com/channels/724417775795306530">"The Garage"</a> (Armster15, F34R and Yumns)
 <li> My friends, allthough they can't code :D</li>
</details>

## Invite
(currently only works on one server so its disabled)
https://discord.com/api/oauth2/authorize?client_id=786697105838309426&permissions=268438656&scope=bot

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
</details>
