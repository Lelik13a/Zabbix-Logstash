#!/bin/python3
"""

Get pipeline stats from logstash

"""

import urllib.request
import json
import sys

#plugin = sys.argv[1]

with urllib.request.urlopen("http://localhost:9600/_node/stats/pipelines") as url:
   data = json.loads(url.read().decode())

res = []
pipelines = data["pipelines"]
for pipeline in pipelines:
        plugins = pipelines[pipeline]["plugins"]
        for plugin in plugins:
                items = plugins[plugin]
                for item in items:
                        res.append({"{#PIPELINE}": pipeline, "{#PLUGIN}": plugin, "{#ID}": item["id"], "{#NAME}": item["name"]})

print("", json.dumps(res))
