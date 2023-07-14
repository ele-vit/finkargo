from pydantic import ValidationError
class TheMatrixHasYou():

    def __init__(self, schema, data):
        self.schema = schema
        self.data = data

    def sort_array(self):
        try:
            array = self.schema(**self.data)
            sorted_array = sorted(array.unclassified)
            duplicates = [x for x in sorted_array if sorted_array.count(x) > 1]
            unique_elements = list(set(sorted_array))
            return {"unclassified": array.unclassified, "classified": unique_elements + duplicates}, 201
        except IndexError as e:
            return {"message": str(e)}, 500
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400
