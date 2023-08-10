from Python_Playwright_ReportalPortal.api.api import ApiBooking, ApiAuth


class TestsBooking:
    def test_get_booking_ids(self, api_request_context):
        list_ids = ApiBooking().get_booking_ids(api_request_context)
        assert "bookingid" in list_ids[0]

    def test_create_new_book(self, api_auth):
        new_book = ApiBooking().create_booking(api_auth)
        assert "bookingid" in new_book
