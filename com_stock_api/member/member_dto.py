from com_stock_api.ext.db import db
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from com_stock_api.member.member_pro import MemberPro

# config = {
#     'user': 'root',
#     'password': 'root',
#     'host': '127.0.0.1',
#     'port': '3306',
#     'database': 'stockdb'
# }

# charset = {'utf8': 'utf8'}
# url = f'mysql+mysqlconnector://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}?charset=utf8'
# engine = create_engine(url)

class MemberDto(db.Model):

    __tablename__ = "members"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    email: str = db.Column(db.String(100), primary_key=True, index=True)
    password: str = db.Column(db.String(50), nullable=False)
    name: str = db.Column(db.String(50), nullable=False)
    profile: str = db.Column(db.String(200), default='noimage.png')
    geography: str = db.Column(db.String(50))
    gender: str = db.Column(db.String(10))
    age: int = db.Column(db.Integer)
    tenure: int = db.Column(db.Integer, default=0)
    stock_qty: int = db.Column(db.Integer, default=0)
    balance: float = db.Column(db.FLOAT, default=0.0)
    has_credit: int = db.Column(db.Integer)
    credit_score: int = db.Column(db.Integer)
    is_active_member: int = db.Column(db.Integer, nullable=False, default=1)
    estimated_salary: float = db.Column(db.FLOAT)
    role: str = db.Column(db.String(30), nullable=False, default='ROLE_USER')
    # exited: int = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, email, password, name, profile, geography, gender, age, tenure, stock_qty, balance, has_credit, credit_score, is_active_member, estimated_salary, role):
        self.email = email
        self.password = password
        self.name = name
        self.profile = profile
        self.geography = geography
        self.gender = gender
        self.age = age
        self.tenure = tenure
        self.stock_qty = stock_qty
        self.balance = balance
        self.has_credit = has_credit
        self.credit_score = credit_score
        self.is_active_member = is_active_member
        self.estimated_salary = estimated_salary
        self.role = role
        # self.exited = exited

    def __repr__(self):
        return 'Member(member_id={}, email={}, password={},'\
        'name={}, profile={}, geography={}, gender={}, age={}, tenure={}, stock_qty={}, balance={},'\
        'hasCrCard={}, credit_score={}, isActiveMember={}, estimatedSalary={}, role={}'\
        .format(self.id, self.email, self.password, self.name, self.profile, self.geography, self.gender, self.age, self.tenure, self.stock_qty, self.balance, self.has_credit, self.credit_score, self.is_active_member, self.estimated_salary, self.role)

    @property
    def json(self):
        return {
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'profile': self.profile,
            'geography': self.geography,
            'gender': self.gender,
            'age': self.age,
            'tenure': self.tenure,
            'stock_qty': self.stock_qty,
            'balance': self.balance,
            'has_credit': self.has_credit,
            'credit_score': self.credit_score,
            'is_active_member': self.is_active_member,
            'estimated_salary': self.estimated_salary,
            'role': self.role,
            # 'exited': self.exited
        }

class MemberVo:
    email: str = ''
    password: str = ''
    name: str = ''
    profile: str = ''
    geography: str = ''
    gender: str = ''
    age: int = 0
    tenure: int = 0
    stock_qty: int = 0
    balance: float = 0.0
    has_credit: int = 0
    credit_score: int = 0
    is_active_member: int = 1
    estimated_salary: float = 0.0
    role: str = 'ROLE_USER'

# service = MemberPro()
# Session = sessionmaker(bind=engine)
# s = Session()
# df = service.hook()
# print(df.head())
# s.bulk_insert_mappings(MemberDto, df.to_dict(orient="records"))
# s.commit()
# s.close()
