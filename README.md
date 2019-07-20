# dpkg-list-json
Produces a JSON output form of the installed Debian packages list

## Requirements:

* Python 3.4.3+
* An Ubuntu or Debian distribution of Linux (for `dpkg`)

## Usage

`python3 dpkg_list_json.py > /path/to/output.json`

## Example

`python3 dpkg_list_json.py > $(pwd)/example.json`


See examples directory for sample output from a Raspberry Pi 3+

* [Raw JSON](examples/example_raw.json)
* [Formatted JSON](examples/example_formatted.json)
