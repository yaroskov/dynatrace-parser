import likes


# User's configuration of program:

# Options:
options = {
	"printData": True,
	"writeData": True,
	"writeBeauty": True,
	"runFull": True
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
		"source": "tasks_22-12-2021_17.23.07.json"
	},
	"tasksSource": {
		"path": "source_tasks/",
		"source": "jira.egovdev 2021-12-22T17_12_40+0300.html"
	},
	"reportsFilled": {"path": "reports_filled/"},
	"beauties": {"path": "beauties/"}
}

# Likes list for grouping similar problems by the Message:
likes = likes.likes
