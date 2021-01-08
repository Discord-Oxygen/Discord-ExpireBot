# Discord-ExpireBot

This Bot allows you to let roles expire. If you set e.g. the @voted role to 12h, the role will get removed automatically 12h after obtaining. This is individual to all users on the guild. It also saves the obtaining time into a JSON File, so if the Bot gets temporary offline, it can handle this.

## Credit
I didn't code it all on myself, I only helped and send feedback/did testing etc. The original Creator wants to stay private, so we decided to make the bot my own.
I'll probably host the bot and make it public for top.gg so anyone can use it, and I'll add multi-guild functuallity. The more complicated features will be coded by my friend (my Python knowledge is very limited)

## Invite
(currently only works on one server so its disabled)
https://discord.com/api/oauth2/authorize?client_id=786697105838309426&permissions=268438656&scope=bot

## Contributing
Consider giving this Repo a star if you like it and vote for the Bot at top.gg!!!
Write issues and pulls! Test and Report! This helps the project.
Also I don't mind donations ;)
I need a (fake) Credit Card to confirm my Identity to reduce the hosting fees. It doesn't need to have money on it. If you have one or know where I can find one pls Contact me!!

## Selfhost
(I'd recommend to use a Raspberry Pi)
Set the environment Variables `discord_token` and `guild_id` or
change the token string at the end of the code and the guildId to yours.
Than install dependencies: `python3 -m pip install discord.py` and `python3 -m pip install durations`
and than finally run `python3 bot/main.py`

## Host using Heroku
Check out the original tutorial from https://github.com/audieni/discord-py-heroku/
<details>
  <summary><b>Step-by-Step Tutorial</b></summary>
  
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link (https://signup.heroku.com/)].

 ### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!<br>
 ![token example](https://user-images.githubusercontent.com/55095883/104066667-14f5d700-5202-11eb-82e0-6e44e4e1759a.png)

 ### How to clone the repository
 * Clone this repository to your own (do **not** fork!!)
 * Make your Repo private
 * Replace 681478549240283171 in the source code with your guild id
 * Replace the 'token' string at the end with the bot token you copied before e.g. `NzgxODc4MzQ1NzQ1ODI1ODlz.X8EC9A.-FI1PEnksgFsrid-m1O8c-eUTdc`
 * Create an application for Heroku by clicking [here](https://dashboard.heroku.com/new-app).
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
