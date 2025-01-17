from flask_restful import Resource, reqparse

from com_stock_api.kospi_pred.dao import KospiDao
from com_stock_api.kospi_pred.dto import KospiDto

class Kospi(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('date', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('covid_date', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('stock_date', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('news_date', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('stock', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('price', type=int, required=False, help='This field cannot be left blank')


    def post(self):
        data = self.parset.parse_args()
        kospi = KospiDto(data['date'],data['covid_date'],data['stock_date'],data['news_date'],data['stock'],data['price'])
        try:
            kospi.save()
        except:
            return {'message':'An error occured inserting the kospi'}, 500
        return kospi.json(), 201

    def get(self,id):
        kospi = KospiDao.find_by_id(id)
        if kospi:
            return kospi.json()
        return {'message': 'Kospi not found'}, 404

    def put (self, id):
        data = Kospi.parser.parse_args()
        kospi = KospiDto.find_by_id(id)

        kospi.date = data['date']
        kospi.date = data['covid_date']
        kospi.date = data['stock_date']
        kospi.date = data['news_date']
        kospi.stock = data['stock']
        kospi.price= data['price']
        kospi.save()
        return kospi.json()

class Kospis(Resource):
    def get(self):
        return {'kospis': list(map(lambda kospi: kospi.json(), KospiDao.find_all()))}
        #return {'kospis':[kospi.json() for kospi in KospiDao.find_all()]}

