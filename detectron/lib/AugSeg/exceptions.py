class TrimapError(Exception):
    """
    Error when creating matting trimap.
    """
    def __init__(self, err):
        super(TrimapError, self).__init__(err)


class AnnError(Exception):
    """
    Error with Input annotation.
    """
    def __init__(self, err):
        super(AnnError, self).__init__(err)
