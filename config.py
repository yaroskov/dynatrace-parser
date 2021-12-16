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
	"sourcesNumber": 7,
	"source_bags": {"path": "source_bags/"},
	"source_bags_kibana": {"path": "source_bags_kibana/"},
	"reports": {"path": "reports/"},
	"tasks": {
		"path": "tasks/",
		"source": "tasks_11-11-2021_14.54.01.json"
	},
	"tasksSource": {
		"path": "source_tasks/",
		"source": "gosuslugi-jira 2021-11-11T14_47_51+0300.html"
	},
	"reportsFilled":{"path": "reports_filled/"},
	"beauties": {"path": "beauties/"}
}

# Likes list for grouping similar problems by the Message:
likes = likes.likes
