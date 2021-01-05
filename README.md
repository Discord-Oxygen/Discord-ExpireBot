# Discord-ExpireBot

This Bot allows you to let roles expire. If you set e.g. the @voted role to 12h, the role will get removed automatically 12h after obtaining. This is individual to all users on the guild. It also saves the obtaining time into a JSON File, so if the Bot gets temporary offline, it can handle this.

###Credit
I didn't code it all on myself, I only helped and send feedback/did testing etc. The original Creator wants to stay private, so we decided to make the bot my own.
I'll probably host the bot and make it public for top.gg so anyone can use it, and I'll add multi-guild functuallity. The more complicated features will be coded by my friend (my Python knowledge is very limited)

###Invite
(currently only works on one server so its disabled)
https://discord.com/api/oauth2/authorize?client_id=786697105838309426&permissions=268438656&scope=bot

###Selfhost
change the 'token' string at the end of the code to yours
and the guildId to yours.
Than install dependencies: `python3 -m pip install discord.py` and `python3 -m pip install durations`
and than finally run `python3 bot/main.py`

<details>
  <summary>###Host using Heroku</summary>
 Check out the original tutorial from https://github.com/audieni/discord-py-heroku/
 ##### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link (https://signup.heroku.com/)].

 ##### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!

 ##### How to fork the repository and set it up to work with Heroku?
 * Fork a copy of this repository by clicking the 'Fork' on the upper right-hand.
 * Create an application for Heroku by clicking [here](https://dashboard.heroku.com/new-app).
 * Under 'Deploy', do the following:
   * Deployment Method => Connect your GitHub
   * App connected to GitHub => Search for the forked repository
   * Automatic Deploy => Enable Automatic Deploy (to redeploy after every commit)
 * Under 'Resources', do the following:
   * Click on the 'Pencil' icon.
   * Switch the worker from off to on.
   * Click 'Confirm' to finalize the decision.
   * NOTE: You are allocated 550 free Dyno hours, which will not last the entire month. However, if you provide a credit card to verify your identity, you are given an additional 450 hours, which will allow your bot to run indefinitely.
  </details>
