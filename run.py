import os
import json

json_file = json.load(open("./source_file_2.json"))

WATCHERS = []
MANAGERS = [[]]
ORGS = []

NEW_ARR = {}
FULL_ARR = []
PRIORITY = []

data_managers = {}
data_watchers = {}

for i in json_file:
    PRIORITY.append(i["priority"])

for i in json_file:
    for j in reversed(PRIORITY):
        if i["priority"] == j:
            NEW_ARR = i
            FULL_ARR.append(NEW_ARR)

for i in FULL_ARR:
    if i["name"] not in ORGS:
        ORGS.append(i["name"])
    for manager in i["managers"]:
        if manager not in MANAGERS:
            MANAGERS.append(manager)
            data_managers[manager] = []
    for manager in MANAGERS:
        if manager in i["managers"]:
            data_managers[manager].append(i["name"])
    for watcher in i["watchers"]:
        if watcher not in WATCHERS:
            WATCHERS.append(watcher)
            data_watchers[watcher] = []
    for watcher in WATCHERS:
        if watcher in i["watchers"]:
            data_watchers[watcher].append(i["name"])


f = open("managers.json", "a")
f.write(json.dumps(data_managers))
f.close()

f = open("watchers.json", "a")
f.write(json.dumps(data_watchers))
f.close()