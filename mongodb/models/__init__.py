from beanie import Document

class User(Document):
    member_id: str
    name: str
    context: str

    class Settings:
        use_state_management = True