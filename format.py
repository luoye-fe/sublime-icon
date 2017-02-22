# 格式化 icon json

import os;
import json;

result = {};

for root, dirs, files in os.walk('./svg'):
	for file in files:
		result[file] = '';

fo = open('./icons.json', 'r+');

fo.write(json.dumps(result, indent = 4));

fo.close();
