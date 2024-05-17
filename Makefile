.PHONY: run

run:
	python main.py

.DEFAULT_GOAL := run

.PHONY: clean

clean:
	rm -rf build 
	rm -rf src/*.egg-info
	rm -rf __pycache__ src/__pycache__ 
	rm -rf src/validators/__pycache__
	rm -rf src/real/__pycache__
	rm -rf src/measurement/__pycache__