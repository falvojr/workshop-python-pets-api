run:
	export SQLALCHEMY_DATABASE_URL=postgresql://dssseuhz:XkETRS4ZdJDT6cc1sZOI8VwaxkrqgdSr@tuffi.db.elephantsql.com:5432/dssseuhz
	uvicorn app.main:app --reload