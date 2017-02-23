# 格式化 icon json

import os;
import json;

result = {};

with open('./icons.json', 'r') as f:
	data = json.load(f);

for root, dirs, files in os.walk('./svg'):
	for file in files:
		if not data[file]:
			data[file] = '';

fo = open('./icons.json', 'r+');

fo.write(json.dumps(data, indent = 4, sort_keys=True));

fo.close();
