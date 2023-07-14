from pydantic import ValidationError


class calculations():
    def __init__(self, schema, data):
        self.schema = schema
        self.data = data

    def calculate_balance(self):
        try:
            bills_calc = self.schema(**self.data)
            response = []
            for i in range(len(bills_calc.months)):
                month = bills_calc.months[i]
                balance = bills_calc.sales[i] - bills_calc.bills[i]
                item = {
                    "month": month,
                    "sales": bills_calc.sales[i],
                    "bills": bills_calc.bills[i],
                    "balance": balance,
                }
                response.append(item)
            return response, 201
        except IndexError as e:
            return {"message": str(e)}, 500
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400
