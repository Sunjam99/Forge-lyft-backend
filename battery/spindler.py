from battery.battery import Battery
from utilities import add_years_to_date

class Spindler(Battery):
    def _init(self, current_date, last_servicing_date):
        self.current_date = current_date
        self.last_servicing_date = last_servicing_date
        
    def needs_servicing(self):
        date_for_battery_service = add_years_to_date(self.last_servicing_date, 2)
        if date_for_battery_service < self.current_date:
            return True
        else:
            return False