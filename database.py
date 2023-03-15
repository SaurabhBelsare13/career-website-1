from sqlalchemy import create_engine, text
import os

db_connection_engine =os.environ['DB_CONNECTION_ENGINE']


engine=create_engine(
  db_connection_engine,
  connect_args={
    "ssl": {
      "ssl_ca":"etc/ssl/cert.pem"
    }
  }
)

def load_data_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs= []
    for row in result.all():
     jobs.append(dict(row))

    return jobs


