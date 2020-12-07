build:
	docker build -t content-summary -f Dockerfile ./

run:
	docker build -t content-summary -f Dockerfile ./
	docker run --rm -it -p 5000:5000 content-summary:latest

test:
	docker build -t content-summary -f Dockerfile ./
	docker run --rm -it content-summary:latest python ./test/tests.py
	
client-run:
	cd client; echo "In client dir"; \
        HOST=localhost yarn start