# dpkg-list-json
Produces a JSON output form of the installed Debian packages list

## Requirements:

* Python 3.4.3+
* An Ubuntu or Debian distribution of Linux (for `dpkg`)

## Install
    pip install dpkg_list_json

## Usage
    dpkg_list_json > /path/to/output.json

## Example
    dpkg_list_json > $(pwd)/example.json

See examples directory for sample output from a Raspberry Pi 3+

* [Raw JSON](examples/example_raw.json)
* [Formatted JSON](examples/example_formatted.json)
