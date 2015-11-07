# Salad Software

Features:

 + Populates the database with system usage data.
 + Stores in the database information captured from a web form.
 + Produces reports and web dashboards using data from the database.

## Prerequisites

Clone this repository:

```` sh
git clone git@github.com:gwu-business/salad-data.git
cd salad-data/
````

Install python and pip (using [homebrew](https://github.com/gwu-business/istm-4121/blob/master/notes/database-management/database-management-software/homebrew-package-manager.md)) if necessary.

```` sh
brew install python
brew linkapps python
````

Install package dependencies:

```` sh
pip install -r requirements.txt
````

Start a local web server:

```` sh
python -m SimpleHTTPServer 8888 &
````

## Usage

Populate the database with system usage data.

```` sh
python populate_menu_data.py
python populate_usage_data.py
````

Produce management reports.

```` sh
python produce_reports.py
````

Input information into a web form at localhost:8888/employees/new.
