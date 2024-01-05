
class MissingMandatoryAttribute(AttributeError):
    """
    An exception that occurs when an SCS mandatory attributes are missing.
    """

    def __init__(self, *args, **kwargs):
        super(MissingMandatoryAttribute, self).__init__(
            args, "Are you sure this is a SCS compliant cluster."
        )
