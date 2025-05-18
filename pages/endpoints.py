from .const_and_test_data import Const, TestData

class Endpoints:
    params = {
        'username': TestData.TEST_LOGIN,
        'password': TestData.TEST_PASSWORD
    }
    Charts_MainPage = Const.MAIN_LINK+'api/v2/service/charts/main-page/'
    Login = Const.MAIN_LINK+'api/v2/login/'