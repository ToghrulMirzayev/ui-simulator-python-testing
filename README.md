# ui-simulator-python-testing

Automated tests for ui-simulator: `https://toghrulmirzayev.github.io/ui-simulator/`


# Overview
Testing developed using Page Object Model pattern, 
by following OOP principles and clean code rules. 
You can run tests both locally and via CI.
Secrets encrypted in CI environment variables.
Check below guide to set up secrets locally. 


# Getting started

* Clone repository to your local machine
  * `git clone https://github.com/ToghrulMirzayev/ui-simulator-python-testing.git`

* Create virtual environment
  * `python -m venv venv`

* Activate virtual environment
  * Windows
    * `venv/Scripts/activate`
  * MacOS/Linux
    * `source venv/bin/activate`

* Create `.env` file and fill it as shown below
  * ```text
     TEST_USERNAME = "correct_username"
     TEST_PASSWORD = "correct_password"
     ```
* Install dependencies
  * `pip install -r requirements.txt`

* Run tests
  * To run all tests
    * `pytest`
  * To run only specific scope
    * `pytest -m smoke`
  * To run tests filtering by name
    * `pytest -k "test_something"`
  * To send test result to the telegram channel
    * `pytest --telegram-pyreport <chat id> <bot token> --server <URL>`
