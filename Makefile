run:
	python app.py

test:
	python app_test.py

integration:
	TAG=$(TAG) APP_NAME=foobar INTEGRATION_TEST=true ./integration_test

build:
	docker build -t app .
