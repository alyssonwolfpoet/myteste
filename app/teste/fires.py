from models import engine,Base 

Base.metadata.drop_all(bind=engine)