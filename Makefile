.PHONY: run clean test

.DEFAULT_GOAL := run

run:
	python main.py

create-allure-dirs:
	mkdir -p allure allure/allure-results allure/allure-report

run-tests:
	pytest --clean-alluredir --alluredir=allure/allure-results

generate-report:
	allure --verbose generate allure/allure-results --clean \
	--report-dir allure/allure-report --report-name "Testing report"

open-report:
	allure --verbose open allure/allure-report

test: create-allure-dirs run-tests generate-report open-report

clean:
	rm -rf build .pytest_cache allure
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} + 