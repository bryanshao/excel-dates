import parsekit
import datetime
import time

class DatesToStrings(parsekit.Step):
    """Converts datetime objects and partial dates (e.g. year only) to date strings"""

    fields = parsekit.Argument(
        "Names of fields to convert",
        type=list,
        required=True)

    def configure(self, options):
        pass

    def run(self, record, metadata):
        schema = metadata.get_closest('schema')
        for field in self.options.fields:
            field_idx = schema.field_index(field)
            field_val = record[field_idx]
            if type(field_val) is datetime.datetime:
                field_string = field_val.strftime('%m/%d/%Y')
                if field_string:
                    record[field_idx] = field_string
            else:
                field_string = str(field_val)
                if field_string:
                    record[field_idx] = field_string
        return record, metadata

    def teardown(self, *args, **kwargs):
        pass
