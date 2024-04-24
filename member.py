class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def get_member_id(self):
        return self.member_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

