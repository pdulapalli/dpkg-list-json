#!/usr/bin/env python3

# MIT License

# Copyright (c) 2019-2020 Anurag Dulapalli

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

import json
import sys
import subprocess
import re

def safe_str(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    return ""

def generate_dpkg_json():
    ps = subprocess.Popen(('dpkg', '-l'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', '^ii'), stdin=ps.stdout)
    ps.wait()

    lines = safe_str(output).split('\\n')

    i = 0
    while len([l for l in re.split(r" {1,}", lines[i]) if l]) != 5:
        i += 1

    pkgs = {}
    for line in lines:
        parsed_line_core = re.split(r" {1,}", line)
        if (len(parsed_line_core) >= 5) and (len(parsed_line_core[1]) > 0):
            parsed_line_supplement = re.split(r" {2,}", line)
            description = ''
            if (len(parsed_line_supplement) > 0):
                description = parsed_line_supplement[-1]
            pkgs.update({parsed_line_core[1]:{'State':parsed_line_core[0], 'Version':parsed_line_core[2], 'Architecture':parsed_line_core[3],'Description':description}})

    json_output = json.dumps(pkgs)

    # Print results to stdout
    print(json_output)
    sys.exit(0)

if __name__ == "__main__":
    generate_dpkg_json()
