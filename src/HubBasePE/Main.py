from . import all_programs
from .Programs.Manager import Program
__version__ = "0.0.3.0.00b1"


class User:
    def __init__(self, login: str = "", password: str = "1041"):
        self.VipAccess = False
        self.username = login
        self.password = password

    def __str__(self) -> str:
        return f"{self.username} (pass: {self.password}, VIP: {self.VipAccess})"

    def login(self, *, resetpau: bool = False):
        if resetpau:
            self.username, self.password = input("Username -- "), input("Password -- ")
        self.VipAccess = input("VIP password -- ") == "5280"
        if not self.VipAccess:
            print("Incorrect.")
        else:
            print("Correct.")


def main():
    user = User()
    user.login(resetpau=True)
    for pr_id in all_programs:
        try:
            Program(pr_id).run()
        except ImportError as e:
            print(e)
        except Exception as e:
            print(f"Failed to run program {pr_id}: {e}")


if __name__ == '__main__':
    main()
