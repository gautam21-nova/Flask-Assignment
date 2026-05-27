import urllib.parse
from sqlalchemy import create_engine



raw_password = "gautam_123@2026"
encoded_password = urllib.parse.quote_plus(raw_password)

engine = create_engine(f"mysql+pymysql://root:{encoded_password}@localhost:3306/users")