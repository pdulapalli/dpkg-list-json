#!/usr/bin/env python3

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

import json
import sys
import subprocess
import re

def safe_str(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    return ""

def main():
    ps = subprocess.Popen(('dpkg', '-l'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', '^ii'), stdin=ps.stdout)
    ps.wait()
    
    lines = safe_str(output).split('\\n')

    i = 0
    while len([l for l in re.split(r" {2,}", lines[i]) if l]) != 5:
        i += 1
    
    pkgs = {}
    for line in lines:
        parsed_line = re.split(r" {2,}", line)
        if (len(parsed_line) == 5) and (len(parsed_line[1]) > 0):
            pkgs.update({parsed_line[1]:{'State':parsed_line[0], 'Version':parsed_line[2], 'Architecture':parsed_line[3],'Description':parsed_line[4]}})

    json_output = json.dumps(pkgs)

    # Print results to stdout
    print(json_output)
    sys.exit(0)

if __name__ == "__main__":
    main()
