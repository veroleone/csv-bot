# 📊 CSV-Bot

CSV-Bot is a simple Discord bot that exports only **eligible members** from a server into a CSV file. Only members with the **"⭐ | Member"** role are considered (bots are excluded). Additionally, if a member is a Server Booster and has the OG role **"🏆 | OG‘s"**, they are listed twice, increasing their chances in giveaways.

---

## 🚀 Features
- ✅ Exports eligible server members to a CSV file
- ✅ Excludes bots
- ✅ Only includes members with the **"⭐ | Member"** role
- ✅ Doubles the entry for members who are Server Boosters and have the OG role (**"🏆 | OG‘s"**)
- ✅ Saves the Discord name and join date for each member

---

## 🛠 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/veroleone/csv-bot.git
cd csv-bot
```

### **2️⃣ Install Dependencies**
Make sure you have Python installed, then run:
```bash
pip install discord.py python-dotenv
```

### **3️⃣ Set Up the Environment Variables**
Create a `.env` file in the project directory and add:
```ini
TOKEN=your_discord_bot_token_here
GUILD_ID=your_server_id_here
```
- **TOKEN** → Your bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
- **GUILD_ID** → Your server's ID (Right-click the server name → Copy ID)

### **4️⃣ Enable Privileged Intents**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your bot and navigate to the **Bot** tab
3. Enable **SERVER MEMBERS INTENT**
4. Click **Save Changes**

### **5️⃣ Run the Bot**
```bash
python main.py
```
When started, the bot will generate a `discord_members.csv` file with the eligible members.

---

## 📂 CSV Output Format
The CSV file will contain the following columns:
```csv
Discord Name,Join Date
"@User1","2024-01-10"
"@User2","2023-12-05"
```
*Note:* Members who are Server Boosters and have the OG role (**"🏆 | OG‘s"**) appear twice in the CSV, which increases their chance in giveaways.

---

## ❓ Troubleshooting

### **Bot Does Not Detect Members**
- Ensure the bot has the **"Read Member Information"** permission in your Discord server.
- Verify that **SERVER MEMBERS INTENT** is enabled in the Developer Portal.

### **Error: `NoneType object has no attribute 'members'`**
- Check that the `GUILD_ID` in the `.env` file is correct.
- Ensure the bot is invited to the server with the correct permissions.

### **Bot Does Not Start?**
- Make sure Python and all dependencies are installed (`pip install -r requirements.txt`).
- Restart the bot and check the error messages.

---

## ⚡ Contributing
Pull requests and issue reports are welcome!
