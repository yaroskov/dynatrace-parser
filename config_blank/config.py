from config.dict import errors_dict, services

# User's configuration of program:

# Services:
services = services.data

# Errors dictionary:
errors = errors_dict.errors

# Options:
options = {
	"printData": False,
	"writeData": True,
	"writeBeauty": True,
	"runFull": True,
	"customData": {
		"date": "13.01.2022",
		"isOn": False
	}
}

# Paths to program files and folders:
paths = {
	"dynotraceURI": {"path": "https://juu410.dynatrace-managed.com/e/3051004e-37e8-4d8f-98ff-9e175c2f39eb/#servicecall;sci=SERVICE-BE720D12C8680318;callURI="},
	"dataPath": {"path": "data/"},
	"sourcesNumber": 12,
	"source_bags": {"path": "source_bags/"},
	"source_bags_kibana": {"path": "source_bags_kibana/"},
	"reports": {"path": "reports/"},
	"tasks": {
		"path": "tasks/",
		"source": "tasks_13-01-2022_16.02.40.json"
	},
	"tasksSource": {
		"path": "source_tasks/",
		"source": "jira.egovdev 2022-01-13T16_00_50+0300.html"
	},
	"reportsFilled": {"path": "reports_filled/"},
	"beauties": {"path": "beauties/"}
}
