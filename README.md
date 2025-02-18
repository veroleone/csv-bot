# 📊 CSV-Bot

CSV-Bot is a simple Discord bot that exports all members from a server into a CSV file, including information about whether they are a Server Booster and if they have a specific role (e.g., `🏆 | OG's`).

---

## 🚀 Features
- ✅ Export all server members to a CSV file
- ✅ Detect Server Boosters
- ✅ Detect members with a specific role (e.g., `🏆 | OG's`)
- ✅ Saves join date and all roles of each member

---

## 🛠 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/csv-bot.git
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
- **GUILD_ID** → Your server's ID (Right-click server name → Copy ID)

### **4️⃣ Enable Privileged Intents**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your bot → Go to the **Bot** tab
3. Enable **SERVER MEMBERS INTENT**
4. Click **Save Changes**

### **5️⃣ Run the Bot**
```bash
python main.py
```
Once started, the bot will generate a `discord_members.csv` file with all members.

---

## 📂 CSV Output Format
The CSV file will contain:
```csv
Discord Name, Join Date, Server Booster, OG Member, Roles
"@User1", "2024-01-10", "Yes", "No", "Member, Moderator"
"@User2", "2023-12-05", "No", "Yes", "🏆 | OG's, Admin"
```

---

## ❓ Troubleshooting
### **Bot does not detect members**
- Ensure the bot has **"Read Member Information"** permission in your Discord server.
- Make sure **Server Members Intent** is enabled in the Developer Portal.

### **Error: `NoneType` object has no attribute 'members'`**
- Check if `GUILD_ID` is correctly set in `.env`
- Re-invite the bot using the correct permissions

### **Bot does not start?**
- Ensure Python and dependencies are installed: `pip install -r requirements.txt`
- Restart the bot and check for errors

---

## ⚡ Contributing
Feel free to submit pull requests or report issues!

---

## 📜 License
This project is open-source and licensed under the MIT License.

