from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 40  ind /🌎 0.4792$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 60  ind /🌎 0.7188$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 129  ind /🌎  1.5454$  per Month
	
	
	Pay Using Upi I'd `9675208706@fam`
	
	After Payment Send Screenshots Of 
        Payment To Admin @itz_tusarr"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/itz_tusarr")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/about_tosuu"),
        			InlineKeyboardButton("UPI ",url = "https://t.me/about_tosuu")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 40  ind /🌎 0.59$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 60  ind /🌎 0.7188$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 179  ind /🌎 1.5454$  per Month
	
	
	Pay Using Upi I'd `9675208706@fam`
	
	After Payment Send Screenshots Of 
        Payment To Admin @itz_tusarr"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/itz_tusarr")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/about_tosuu"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/about_tosuu")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

	 








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
