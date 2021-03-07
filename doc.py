from oauth2client.service_account import ServiceAccountCredentials
import gspread

class Doc:
	def __init__(self, main_sheet_url, worksheet):
		self.main_sheet_url = main_sheet_url
		self.worksheet = worksheet
		self.credentials = []

		self.connect_to_API()

	def connect_to_API(self):
		