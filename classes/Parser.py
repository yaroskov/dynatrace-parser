import json
import os
from datetime import datetime

class Parser:

	@staticmethod
	def jsonView(results):
		
		return json.dumps(results, sort_keys=False, indent=4, ensure_ascii=False)

	@staticmethod
	def jsonLoad(source, path=""):

		jsonData = None
		with open(path + source, "r", encoding='utf-8') as txtData:
			jsonData = json.load(txtData)

		return jsonData

	@staticmethod
	def writeDataToFile(data, path="", prefix="", extension="json"):

		if not os.path.exists(path):
			os.mkdir(path)

		encoded_unicode = data.encode("utf8")

		currDateTime = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
		a_file = open(path + prefix + "_" + currDateTime + "." + extension, "wb")
		a_file.write(encoded_unicode)

		pass