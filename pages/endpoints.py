from .const_and_test_data import TestData, Env

class Endpoints:
    params = {
        'username': TestData.TEST_LOGIN,
        'password': TestData.TEST_PASSWORD
    }
    Charts_MainPage = Env.MAIN_LINK+'api/v2/service/charts/main-page/'
    Login = Env.MAIN_LINK+'api/v2/login/'
    Map_CompetencyPage = Env.MAIN_LINK+'api/v2/map/legal-person/'
    RaitingInMap_CompetencyPage = Env.MAIN_LINK+ 'api/v2/map/legal-person/detail_info/'
    Statistic_CompetencyPage = Env.MAIN_LINK +'api/v2/service/charts/'