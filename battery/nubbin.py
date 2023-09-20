from battery.battery import Battery
from utilities import add_years_to_date

class Nubbin(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def need_service(self):
        servicing_date = add_years_to_date(self.last_service_date, 4)
        if servicing_date < self.current_date:
            return True
        else:
            return False