from sqlalchemy import create_engine, text
import os

db_connection_string= os.environ['DB_CONNECTION_STRING']



engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                        
                        
                      }
                      )

def load_jobs_from_db():
  with engine.connect() as conn:
    results_columns = conn.execute(text("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = 'jobs'")).fetchall()
    
    columns = [item[0] for item in results_columns]
    
    results = conn.execute(text("select * from jobs")).fetchall()
  
    jobs = []
    for i in results:
      temp_dict = dict(zip(columns, i))
      jobs.append(temp_dict)
    
  return jobs