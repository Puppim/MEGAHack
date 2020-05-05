from flask_restful import Resource, Api


class Scraper(Resource):

    def get(self):
        return {
            'api': {
                'status': 'OK',
                'version': '1.0'
            }
        }

    def post(self): 
        pass
