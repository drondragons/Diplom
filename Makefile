.PHONY: run clean test

.DEFAULT_GOAL := run

run:
	python main.py

create-allure-dirs:
	mkdir -p allure allure/allure-results allure/allure-report allure/allure-single-report

run-tests:
	pytest --random-order --verbose --clean-alluredir --alluredir=allure/allure-results

generate-report:
	allure --verbose generate allure/allure-results --clean \
	--report-dir allure/allure-report --report-name "Testing report"

generate-single-report:
	allure --verbose generate allure/allure-results --clean \
	--report-dir allure/allure-single-report --report-name "Testing report" --single-file

open-report:
	allure --verbose open allure/allure-report

test: create-allure-dirs run-tests generate-report generate-single-report open-report

clean:
	rm -rf build .pytest_cache
	rm -rf allure/allure-report allure/allure-results
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} + 