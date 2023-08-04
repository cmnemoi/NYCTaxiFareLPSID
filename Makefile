run:
	streamlit run src/app/main.py

setup-env-variables:
	cp .streamlit/secrets.toml.example .streamlit/secrets.toml