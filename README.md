# Discord-ExpireBot

This Bot allows you to let roles expire. If you set e.g. the @voted role to 12h, the role will get removed automatically 12h after obtaining. This is individual to all users on the guild. It also saves the obtaining time into a JSON File, so if the Bot gets temporary offline, it can handle this.
This branch is the original code, its tested and works. But I won't add new features and won't fix minor bugs. See this bracnhe as "Archieved". I recomend using the main branch.

## Credit
This branch is the original code, not made by me.
I only helped and send feedback/did testing etc. The original Creator wants to stay private, so we decided to make the bot my own.
I won't update this branch, except for critical bugs.

## Invite
This is the legacy Version, you have to selfhost it.

## Contributing
see main branch

## Selfhost or VPS
(I'd recommend to use a Raspberry Pi if you Selfhost)
<details>
  <summary><b>Step-by-Step Tutorial</b></summary>
  
 ### Prerequisites
 You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)]

 ### Creating a bot to get a bot token
 * Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
 * Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
 * After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later. Keep the token secret!!!!<br>
 ![token example](https://user-images.githubusercontent.com/55095883/104066667-14f5d700-5202-11eb-82e0-6e44e4e1759a.png)

 ### How to clone the repository
 * Download this repo (or Clone it to your own private repo)
 * Replace 681478549240283171 in the source code (main.py) with your guild id
 * Replace the 'token' string at the end with the bot token you copied before e.g. `NzgxODc4MzQ1NzQ1ODI1ODlz.X8EC9A.-FI1PEnksgFsrid-m1O8c-eUTdc`

 ### Installing dependencies and running the Bot
 * run `pip install discord.py` and `pip install durations` in an elevated command prompt
 * now just run main.py!

</details> 
