class Result:
    def __init__(self, code, msg, data=None):
        self.code = code
        self.msg = msg
        self.data = data

    def to_dict(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}

    @classmethod
    def success(cls, data=None):
        return Result(200, 'success', data)

    @classmethod
    def fail(cls, data=None):
        return Result(400, 'fail', data)
