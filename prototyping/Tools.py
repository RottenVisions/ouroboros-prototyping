import datetime


def getTime():
	timeObj = datetime.datetime.now()
	return "%s:%s:%s" % (timeObj.hour, timeObj.minute, timeObj.second)

def getTimeDots():
	timeObj = datetime.datetime.now()
	return "%s.%s.%s" % (timeObj.hour, timeObj.minute, timeObj.second)

def getDate():
	timeObj = datetime.datetime.now()
	return "%s/%s/%s" % (timeObj.month, timeObj.day, timeObj.year)

def getDateDots():
	timeObj = datetime.datetime.now()
	return "%s.%s.%s" % (timeObj.month, timeObj.day, timeObj.year)