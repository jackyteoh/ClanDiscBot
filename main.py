import discord
import json
import re
import asyncio
import gspread
from datetime import datetime
from doc import Doc

class RadBot(discord.Client):
	def __init__(self, sheet, configs):
		self.token = configs['Bot Token']
		self.admin_name = configs['Admin Rank']
		self.sheet = sheet
		self.start_bot()

	def start_bot(self):
		event_loop = asyncio.get_event_loop()
		event_loop.create_task(self.start(self.token))
		try:
			event_loop.run_forever()
		finally:
			event_loop.stop()

	async def message(self, input_message):
		splitted = input_message.split(" ")

		input_command = splitted[0].strip('.')
		command_targets = splitted[1:]
		author = input_message.author
		channel = input_message.channel
		isAdmin = 1 if author in self.admin_name else -1
		await self.verify(input_command, command_targets, author, channel, isAdmin)

	async def verify(self, command, input_message, author, channel, isAdmin):
		if lower(command) == "check":
			# prints out all splits for said user

	def start():
		all_configs = open("config.json", "r")
		configs = json.loads(all_configs.read())
		sheet = Doc(configs["Spreadsheet URL"], configs["Worksheet Name"])
		rad_bot_instance = RadBot(doc, configs)

if __name__ == "__main__":
	start()