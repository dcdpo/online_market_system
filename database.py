from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 資料庫連接字符串，格式為：資料庫類型+資料庫區定://用戶名:密碼@主機地址:端口號/資料庫名
SQLALCHEMY_DATABASE_URL = "mysql://root:springboot@localhost:3306/myjdbc"

# create SQL engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# create SQL communication session and bind
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create SQL mapping table
Base = declarative_base()