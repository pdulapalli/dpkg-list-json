#!/usr/bin/env python

# MIT License

# Copyright (c) 2019 Anurag Dulapalli

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import sys
import argparse

parser = argparse.ArgumentParser(description='Write installed package list from dpkg to the JSON format')
parser.add_argument('--output-path', help='what filepath to store the created JSON in')

args = vars(parser.parse_args())

lines = os.popen('dpkg -l | grep "^ii"').read().split('\n')
i = 0
while len([l for l in lines[i].split('  ') if l]) != 5:
   i += 1
offsets = [lines[i].index(l) for l in lines[i].split('  ') if len(l)]
pkgs = {}
for line in lines:
    parsed = []
    for i in range(len(offsets)):
        if len(offsets) == i + 1:
            parsed.append(line[offsets[i]:].strip())
        else:
            parsed.append(line[offsets[i]:offsets[i + 1]].strip())

    if len(parsed[1]) > 0:
        pkgs.update({parsed[1]:{'State':parsed[0], 'Version':parsed[2], 'Architecture':parsed[3],'Description':parsed[4]}})

json_output = json.dumps(pkgs)

# Print results to stdout
print json_output

# Checks for output_path before writing JSON to it
if (args["output_path"] is not None) and (type(args["output_path"]) is str) and (len(args["output_path"]) > 0):
    text_file = open(args["output_path"], "w")
    text_file.write("%s" % json_output)
    text_file.close()
else:
    sys.stderr.write('Output path was not supplied, was not a string, or was not empty. Skipping file write.\n')

sys.exit(0)
