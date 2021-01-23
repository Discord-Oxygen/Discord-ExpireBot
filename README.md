# Discord-ExpireBot

This Bot allows you to let roles expire. If you set e.g. the @voted role to 12h, the role will get removed automatically 12h after obtaining. This is individual to all users on the guild. It also saves the obtaining time into a JSON File, so if the Bot gets temporary offline, it can handle this.
[Support Server](https://discord.com/invite/ptpyaEPapy)

## Commands
`%help`<br>
`%expire <role> <time>` and `%unexpire <role> <time>`<br>
`%addperm <role>` and `%delperm <role>`<br>

## Credit
I didn't code it all on myself, I only helped and send feedback/did testing etc. The original Creator wants to stay private, so we decided to make the bot my own.
I'll probably host the bot and make it public for top.gg so anyone can use it, and I'll add multi-guild functuallity.<br>

Thanks to (I'll add the LInk in the next commit) for fixing a Critical Bug!!!

<details><summary>I also want to say thank you to:
<small>the guys from Scicraft
the guys from "The Garage" (Armster15, F34R and Yumns) for the good advices.</small>
</detail>

## Invite
(currently only works on one server so its disabled)
https://discord.com/api/oauth2/authorize?client_id=786697105838309426&permissions=268438656&scope=bot

## Contributing
Consider giving this Repo a star if you like it and vote for the Bot at top.gg!!!
Write issues and pulls! Test and Report! This helps the project.
Also I don't mind donations ;)
I need a (fake) Credit Card to confirm my Identity to reduce the hosting fees. It doesn't need to have money on it. If you have one or know where I can find one pls Contact me!!

## Selfhost
(I'd recommend to use a Raspberry Pi because it have to run 24/7 and bc its easier to setup)
<details>
 <summary><b>Step-by-Step Tutorial</b></summary>
 
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)]
  
 ### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!

 ### Downloading Repo and installing dependencies
 * Download the Repo as zip file and unpack it
 * Install Python if you don't have it (preinstalled on raspi)
 * Run `python3 -m pip install discord.py` and `python3 -m pip install durations` in a Terminal to install dependencies
 
 ### Runnung the bot
 * Change the values in start.sh
  * discord_token=`(Enter the bot token that you copied from the developer portal)`
  * guild_id=`(Enter the ID of your Server. Rightclick on your Server on Discord and then click on 'Copy ID')`
 * Then doubleclick start.sh and click on "Open in Terminal" or run ./start.sh in a Terminal
 
</details>

## Host using Heroku
Check out the original tutorial from https://github.com/audieni/discord-py-heroku/
Note that Heroku doesn't have a persistent storage so you'd have to use some other storage addons.
<details>
  <summary><b>Step-by-Step Tutorial</b></summary>
  
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link (https://signup.heroku.com/)].

 ### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!

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
