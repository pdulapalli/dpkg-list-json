# dpkg-json-parser
Produces a JSON output form of the installed Debian packages list

## Requirements:

* Python 2.7+ or Python 3.6+
* An Ubuntu or Debian distribution of Linux

## Usage

`python dpkg_list_json.py > /path/to/output.json`

## Example

`python dpkg_list_json.py > $(pwd)/example.json`


See examples directory for sample output from a Raspberry Pi 3+

* [Raw JSON](examples/example_raw.json)
* [Formatted JSON](examples/example_formatted.json)
