from com_stock_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, FLOAT

class Member(Base):

    __tablename__ = "members"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    password = Column(VARCHAR(50), nullable=False)
    name = Column(VARCHAR(50))
    geography = Column(VARCHAR(30))
    age = Column(Integer)
    tenure = Column(Integer)
    balance = Column(FLOAT, default=0.0)
    has_credit = Column(Integer)
    is_active_member = Column(Integer, default=1)
    estimated_salary = Column(FLOAT)
    role = Column(VARCHAR(30), default='ROLE_USER')
    exited = Column(Integer, default=0)

    def __repr__(self):
        return 'Member(member_id={}, email={}, password={},'\
        'name={}, geography={}, age={}, tenure={}, balance={},'\
        'hasCrCard={}, isActiveMember={}, estimatedSalary={}, role={}, exited={}'\
        .format(self.id, self.email, self.password, self.name, self.geography, self.age, self.tenure, self.balance, self.has_credit, self.is_active_member, self.estimated_salary, self.role, self.exited)


engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stockdb?charset=utf8', encoding='utf8', echo=True)
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# session.add(Member(email='test@test.com', password='1234', name='test', geography='', age=30, tenure=0, has_credit=0, estimated_salary=0))
query = session.query(Member).filter((Member.name == 'test'))
print(f'query: {query}')
for m in query:
    print(m)

session.commit()