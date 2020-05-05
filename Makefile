run:
	python3 server.py

test:
	pytest -s

push:
	git add .
	git commit -m '...'
	git push origin master

pull:
	git pull origin master