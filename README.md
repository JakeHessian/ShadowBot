# ShadowBot
Multi function Discord bot for a video game clan

# Usage and Functionality:
## Application Cog
When a user first joins the Discord server, the user is prompted with a greeting in a DM to run the **.apply** command in a specific text-channel:

![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/channelprompt.PNG "Channel Prompt")

Then the application starts in the requested user's DMs:

![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/DMconversation.PNG "Channel Prompt")

After the user is completed the application, the bot automatically sends the exported application to a private channel where admins can accept the user for a specific role. The admin must click (react to) the emojis at the bottom of the application for the bot to know to give the user a "Farmer 👩‍🌾" or "PvP 🔫" role. Also, if an admin wishes to deny an applicant, the Admins clicks the ⛔ emoji.

![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/exportedapp.PNG "Channel Prompt")

Underneath the exported application, the bot confirms with the admins that their action was registered:

![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/response1.PNG "Channel Prompt")

And the applicant receives a DM from the bot that they were accepted with a certain role or denied:

![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/response2.PNG "Channel Prompt")

## Reddit Image Grabber
A user may run the command **.get <subreddit>** to pull a random image from the subreddit. Sample usage: **.get wholesomememes** sends back:
  
![Alt text](https://github.com/JakeHessian/ShadowBot/blob/main/screenshots/redditgrabber.png "Channel Prompt")
