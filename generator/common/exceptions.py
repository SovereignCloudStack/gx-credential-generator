
class MissingMandatoryAttribute(AttributeError):
    def __init__(self, *args, **kwargs):
        super(MissingMandatoryAttribute, self).__init__(args, "Are you sure this is a SCS compliant cluster.")

