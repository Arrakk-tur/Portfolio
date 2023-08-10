import logging

from Python_Playwright_ReportalPortal.data.users import Users

logger = logging.getLogger(__name__)

api_auth_user = Users.api_auth_user


class ApiAuth:

    def create_auth_token(self, api_request_context):
        data = {
            "username": api_auth_user["username"],
            "password": api_auth_user["password"]
        }
        headers = {
            "Content-Type": "application/json"
        }
        endpoint = "auth"

        auth_token_request = api_request_context.post(
            endpoint,
            headers=headers,
            data=data
        )
        auth_token_response = auth_token_request.json()
        logging.info("AUTH TOKEN: %s", auth_token_response)
        return auth_token_response["token"]


class ApiBooking:

    def get_booking_ids(self, api_request_context):
        endpoint = "booking"
        headers = {
            "Content-Type": "application/json"
        }
        list_ids_request = api_request_context.get(endpoint, headers=headers)
        list_ids_response = list_ids_request.json()
        logging.info("BOOKS_IDS: %s", list_ids_response)
        return list_ids_response

    def create_booking(self, api_auth):
        endpoint = "booking"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        create_book = api_auth.post(
            endpoint,
            headers=headers,
            data=data
        )
        create_book_response = create_book.json()
        logging.info("NEW BOOK DATA: %s", create_book_response)
        return create_book_response
