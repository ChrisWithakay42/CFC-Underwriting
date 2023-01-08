test:
	pytest -vvv
lint:
	pylint --load-plugins "pylint_flask_sqlalchemy,pylint_pydantic" --fail-under=9 core