# 🤖 MUGA THON First-Time Chatter Bot

Welcome to the **MUGA THON Twitch Bot** — a fun, terminal-based bot that welcomes first-time chatters with a customizable message and lets you chat directly from the console, like a mini Twitch client! Built by **yoboiyeeter_ / LGMBrydan** 🎉

---

## ✨ Features

- 👋 Automatically welcomes first-time chatters
- 💬 Lets you send messages from the terminal like a Twitch chat client
- 🎛️ Customizable welcome messages using `{user}` placeholder
- 🔁 Fun loading animation with random funny lines
- 📺 Channel picker and main menu system
- 🧠 Beginner-friendly and easy to run

---

## 🛠️ Setup Instructions

### 1. Install Python 3

Make sure Python 3.7 or higher is installed. To check:

```bash
python3 --version```

If it's not installed, download it from:
``` 👉 https://www.python.org/downloads/ ```

2. Download the Bot
If you're using GitHub:

``git clone https://github.com/LGMBrydann/TwitchFirstTimeChatterBot.git
cd mugathon-bot``
Or simply download twitch-replier.py and place it in a folder.

3. Generate Your Twitch OAuth Token
Visit: https://twitchtokengenerator.com

Click "Login with Twitch"

Log in with your bot Twitch account (create one if needed)

Under Scopes, check:

✅ chat:read

✅ chat:edit

Click Generate Token

Copy the generated token — it will start with oauth:

4. Configure the Bot
Open bot.py and look for this section at the top:

```NICK = "your_bot_username"
PASS = "oauth:your_generated_token"```
Replace:

your_bot_username → with your bot Twitch username (exactly as it appears)

your_generated_token → with the token you copied in Step 6

✅ Note: Never use your main Twitch account for the bot.

5. Run the Bot
In your terminal, run:

```python3 twitch-replier.py```
or
```python twitch-replier.py```

You'll see a menu like:
=== MUGA THON BOT MENU ===
1. Start Bot
2. Set Welcome Message
3. Exit
Choose option 1, enter the channel name (without the #), and the bot will connect and start watching the chat!

🧾 Customizing the Welcome Message
Choose menu option 2 to set your custom welcome message.
Use {user} where you want the first-time chatter's name to appear.

Example:
📢 WELCOME {user} TO THE THUNDER ZONE 💥 Enjoy your stay, legend!
🔐 Important Notes
⚠️ Never publish your real token — treat it like a password.

Always use a separate Twitch account for bots — don’t risk your main account.

# 🧠 Made by
LGMBrydan / yoboiyeeter_
👑 Twitch: twitch.tv/yoboiyeeter_

Enjoy the MUGA THON o7 <3
