import logging

from faker import Faker

logger = logging.getLogger(__name__)


class Users:
    fake = Faker("en_US")

    static_user = "TestUser_Auto"

    api_auth_user = {
        "username": "admin",
        "password": "password123"
    }

    def user_id(self) -> str:
        user_id = "TestUser_" + str(self.fake.random_number(digits=5))
        logger.info("Generated USER_ID: %s", user_id)
        return user_id

    def account_info(self) -> dict:
        ac_info = {
            # "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
            "address1": self.fake.street_address(),
            "address2": self.fake.street_address(),
            "city": self.fake.city(),
            "state": self.fake.state(),
            "zip_code": self.fake.zipcode(),
            "country": self.fake.country()
        }
        logger.info("Account Info: %s", ac_info)
        return ac_info
