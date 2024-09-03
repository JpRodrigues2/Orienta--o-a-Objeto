from bottle import template , redirect
from app.controllers.db.datarecord import DataRecord

class Application():

    def __init__(self):

        self.pages = {
        'pagina': self.pagina
        }

        self.models= DataRecord()


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)
        

    def helper(self):
        return template('app/views/html/helper')
 
    def pagina(self,parameter=None):
        if not parameter:
            return template('app/views/html/pagina',transfered= False)
        else:
            info = self.models.work_with_parameter(parameter)
            if not info:
               redirect('/pagina')
            else:
               return template('app/views/html/pagina',transfered= True, data=info)