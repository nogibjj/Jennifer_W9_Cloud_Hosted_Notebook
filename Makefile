install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py test_*.py *.ipynb

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

# refactor: format lint

# deploy:
# 	#deploy goes here
		
# generate_and_push:
# 	python main.py
# 	git config --local user.email "action@github.com"; \
# 	git config --local user.name "GitHub Action"; \
# 	git add .; \
# 	git commit -m "test"; \
# 	git push


all: install format lint test
