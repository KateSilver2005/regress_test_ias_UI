from selenium.webdriver.common.by import By

from .const_and_test_data import ConstMainPage


class HeaderLocators:
    LOGO_IN_HEADER = (By.CSS_SELECTOR, '.header-logo .img-fluid')
    TITLE_TEXT_IN_HEADER = (By.CSS_SELECTOR, '.header-title.text-uppercase')
    INSCRIPTION_IN_HEADER = (By.CSS_SELECTOR, '.col-8.d-flex.align-items-center span.opacity-50')
    BUTTON_FOR_VERSION_UNSEEING = (By.CSS_SELECTOR, 'div.text-center.border-left')
    BUTTON_IN_LK = (By.CSS_SELECTOR, '.px-4.btn.btn-primary.dropdown-toggle.transition-ease')
    OPEN_BUTTON_IN_LK = (By.CSS_SELECTOR, '.px-4.btn.btn-primary.dropdown-toggle.transition-ease.show')
    NORMAL_VERSION = (By.CSS_SELECTOR, '.bvi-blocks.bvi-block-center div:nth-child(5) a[data-bvi="close"]')
    PROFILE = (By.CSS_SELECTOR, '[href="/cabinet/profile"]')
    MYCOMPANY = (By.CSS_SELECTOR, '[href="/cabinet/mycompany"]')
    MY_DOSC = (By.CSS_SELECTOR, '[href="/cabinet/my-docs"]')
    SCIENTIST = (By.CSS_SELECTOR, '[href="/cabinet/scientist"]')
    EXIT = (By.CSS_SELECTOR, '.dropdown-menu-end.show a[href="#logout"]')
    WINDOW_LOG_OUT = (By.CSS_SELECTOR, '.swal2-popup')
    BUTTON_LOG_OUT = (By.CSS_SELECTOR, '.swal2-actions button.swal2-confirm')


class HotNewsLocators:
    MODULE_WITH_HOT_NEWS = (By.CSS_SELECTOR, '.container.py-2')
    LINK_ON_PAGE_WITH_ALL_NEWS = (By.CSS_SELECTOR, '.container.py-2 [href="/cabinet/news"]')
    COUNTER_NEWS = (By.CSS_SELECTOR, 'div.justify-content-between > div span')
    NEXT_HOT_NEWS = (By.CSS_SELECTOR, 'button.next-hotnews')
    PREVIOUS_HOT_NEWS = (By.CSS_SELECTOR, 'button.prev-hotnews')
    LIST_NEWS = (By.CSS_SELECTOR, 'ul.hotnews li')
    WRAPPER_LIST_NEWS = (By.CSS_SELECTOR, 'ul.hotnews')
    EACH_NEWS = (By.CSS_SELECTOR, '.hotnews li:nth-child({})')
    DATE_OF_NEWS = (By.CSS_SELECTOR, '.hotnews li:nth-child({}) .me-2.text-grey')
    ICON = (By.CSS_SELECTOR, '.hotnews > li:nth-child({}) > .fal')
    ICON_SCI_PUBS_NEWS = (By.CSS_SELECTOR, '.hotnews > li:nth-child({}) > .fa-microscope')
    ICON_SMI_NEWS = (By.CSS_SELECTOR, '.hotnews > li:nth-child({}) > .fa-newspaper')
    TITLE_OF_NEWS = (By.CSS_SELECTOR, '.hotnews li:nth-child({}) a')


class NewsPageLocators:
    TITLE_MAIN_PAGE = (By.CSS_SELECTOR, '#h1')
    TITLE = (By.CSS_SELECTOR, '#h1 span')
    DATE = (By.CSS_SELECTOR, '.card .badge')
    ICON = (By.CSS_SELECTOR, '.news-item__kind .fal')
    DESCRIPTION_ICON = (By.CSS_SELECTOR, '.news-item__kind .ms-1')


class FooterLocators:
    LOGO_CSP_IN_FOOTER = (By.CSS_SELECTOR, '.footer-logo.mb-3 .img-fluid')
    TEXT_CSP_IN_FOOTER = (By.CSS_SELECTOR, 'div.footer-logo.mb-3 > div:nth-child(2)')
    LOGO_FMBA_IN_FOOTER = (By.CSS_SELECTOR, '.col-4 .footer-logo:nth-child(2) .img-fluid')
    TEXT_FMBA_IN_FOOTER = (By.CSS_SELECTOR, '.col-4 .footer-logo:nth-child(2) >div:nth-child(2)')
    TITLE_AND_INSCRIPTION_IN_FOOTER = (By.CSS_SELECTOR, 'footer .col-5 > div')
    LINK_PAGE_REALESE = (By.PARTIAL_LINK_TEXT, 'Версия приложения ')
    LINK_MAIL_SUPPORT = (By.CSS_SELECTOR, '.d-flex.flex-column.h-100 a:nth-child(1)')
    LINK_FAQ = (By.CSS_SELECTOR, '.d-flex.flex-column.h-100 a:nth-child(2)')
    LINK_HELP = (By.CSS_SELECTOR, '.d-flex.flex-column.h-100 a:nth-child(3)')


class MainPageLocators:
    BUTTON_ANALITIC = (By.CSS_SELECTOR, 'a[href="/cabinet/analytic"]')
    BUTTON_IN_SERVICES = (By.CSS_SELECTOR, 'a[href="/cabinet/services"]')
    BUTTON_INFO_ABOUT_INFOPROVIDER = (By.CSS_SELECTOR, '.card-banner a[href="/cabinet/mycompany"]')
    TITLE_LK = (By.CSS_SELECTOR, '.container #h1:nth-child(1)')

    TABS_SEARCH = (By.ID, 'nav-tab')
    TAB_COMPETENCY = (By.CSS_SELECTOR, '#nav-tab a:nth-child(1)')
    TAB_DOC = (By.CSS_SELECTOR, '#nav-tab a:nth-child(2)')
    TAB_ORG = (By.CSS_SELECTOR, '#nav-tab a:nth-child(3)')
    TAB_PERSON = (By.CSS_SELECTOR, '#nav-tab a:nth-child(4)')
    SEARCH_AREA = (By.CSS_SELECTOR, '.p-4 input')
    CLEAR_BUTTON = (By.CSS_SELECTOR, '.cursor-pointer.grey')
    TABS = [
        TAB_COMPETENCY,
        TAB_DOC,
        TAB_ORG,
        TAB_PERSON
    ]
    PLACEHOLDERS_IN_SEARCH_AREA_TABS = [
        (TAB_COMPETENCY, ConstMainPage.placeholder_competency),
        (TAB_DOC, ConstMainPage.placeholder_doc),
        (TAB_ORG, ConstMainPage.placeholder_org),
        (TAB_PERSON, ConstMainPage.placeholder_person)
    ]

    GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body')
    TITLE_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body h4')
    LIST_SLIDES_IN_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body li')
    SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body li:nth-child({})')
    NEXT_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, ".col-8 .card-body .carousel__next")
    PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body .carousel__prev')
    PICTURE_IN_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY = (By.CSS_SELECTOR, '.col-8 .card-body li:nth-child({}) img')

    SECTION_NEWS = (By.CSS_SELECTOR, '.card-doc.p-0.m-0 >div')
    TITLE_SECTION_NEWS = (By.CSS_SELECTOR, '.col-4 .card-body h4')
    CONTENT_SECTION_NEWS = (By.CSS_SELECTOR, '.content.py-2')
    LINK_ON_PAGE_WITH_ALL_NEWS = (By.CSS_SELECTOR, '.col-4 .card-body:nth-child(1) a')

    GLOBAL_CHARTS = (By.CSS_SELECTOR, '.container > div > .card .card-body')
    TITLE_GLOBAL_CHARTS = (By.CSS_SELECTOR, '.container > div > .card .card-body h4')
    LIST_SLIDES_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, '.container > div > .card .card-body .carousel__track > li')
    NEXT_SLIDE_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, ".container > div > .card .card-body .carousel__next")
    PREVIOUS_SLIDE_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, '.container > div > .card .card-body .carousel__prev')
    SLIDE_IN_GLOBAL_CHARTS = (By.ID, 'chart-graph{}')
    TITLE_OF_SLIDE_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, '.card-body .carousel__viewport li:nth-child({}) h5')
    COLOR_OF_ELEMENT_IN_LEGEND_CHART_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, '#legend-graph{} li:nth-child({}) span')
    TITLE_OF_ELEMENT_IN_LEGEND_CHART_IN_GLOBAL_CHARTS = (By.CSS_SELECTOR, '#legend-graph{} li:nth-child({}) p')

    INFO_FOR_USERS = (By.CSS_SELECTOR, 'main .container >div >div.row:last-child')
    TITLE_INFO_FOR_USERS = (By.CSS_SELECTOR, 'h1:nth-of-type(2)')
    ELEMENT_IN_INFO_FOR_USERS = (By.CSS_SELECTOR, 'main .container >div >div.row:last-child >div:nth-child({})')
    ICON_OF_ELEMENT_IN_INFO_FOR_USERS = (By.CSS_SELECTOR, 'main .container > div > div:last-child > .col-4.mb-4:nth-child({}) img')
    TITLE_OF_ELEMENT_IN_INFO_FOR_USERS = (By.CSS_SELECTOR, 'main .container > div > div:last-child > .col-4.mb-4:nth-child({}) .title')
    URL_OF_ELEMENT_IN_INFO_FOR_USERS = (By.CSS_SELECTOR, 'main .container >div >div.row:last-child >div:nth-child({}) a')



class AdvancedSearch:
    ADVANCED_SEARCH_BUTTON = (By.ID, 'btn-advancedSearch')
    ADVANCED_SEARCH_AREA = (By.ID, 'advancedSearch')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn-search')
    SYNONYMS_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR, '#advancedSearch .col:nth-child(1) .d-block:nth-child(1) .cspfmba')

    LABEL_SYNONYMS_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR,
                                         '#advancedSearch .col:nth-child(1) .d-block:nth-child(1) .lbl')
    FULL_TEXT_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR, '#advancedSearch .col:nth-child(1) .d-block:nth-child(2) .cspfmba')

    LABEL_FULL_TEXT_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR,
                                          '#advancedSearch .col:nth-child(1) .d-block:nth-child(2) .lbl')

    DISTANCE_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR, '#advancedSearch .col:nth-child(2) .d-block:nth-child(1) .cspfmba')

    LABEL_DISTANCE_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR,
                                         '#advancedSearch .col:nth-child(2) .d-block:nth-child(1) .lbl')

    VALUE_DISTANCE_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR,
                                         '#advancedSearch .col:nth-child(2) .d-block:nth-child(2) .cspfmba')

    LABEL_VALUE_DISTANCE_IN_ADVANCED_SEARCH = (By.CSS_SELECTOR,
                                               '#advancedSearch .col:nth-child(2) .d-block:nth-child(2) .lbl')
    LABEL_TEXT_SYNONYMS_IN_ADVANCED_SEARCH = 'Использовать словарь синонимов'
    LABEL_TEXT_FULL_TEXT_IN_ADVANCED_SEARCH = 'Искать в полном тексте публикации/патента'
    LABEL_TEXT_DISTANCE_IN_ADVANCED_SEARCH = 'Учитывать расстояние между словами'
    LABEL_TEXT_VALUE_DISTANCE_IN_ADVANCED_SEARCH = 'Расстояние между словами - не более чем:'

    FILTERS_IN_ADVANCED_SEARCH = [
        (MainPageLocators.TAB_COMPETENCY, SYNONYMS_IN_ADVANCED_SEARCH,
         LABEL_SYNONYMS_IN_ADVANCED_SEARCH, LABEL_TEXT_SYNONYMS_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_COMPETENCY, FULL_TEXT_IN_ADVANCED_SEARCH,
         LABEL_FULL_TEXT_IN_ADVANCED_SEARCH, LABEL_TEXT_FULL_TEXT_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         LABEL_DISTANCE_IN_ADVANCED_SEARCH, LABEL_TEXT_DISTANCE_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, SYNONYMS_IN_ADVANCED_SEARCH,
         LABEL_SYNONYMS_IN_ADVANCED_SEARCH, LABEL_TEXT_SYNONYMS_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, FULL_TEXT_IN_ADVANCED_SEARCH,
         LABEL_FULL_TEXT_IN_ADVANCED_SEARCH, LABEL_TEXT_FULL_TEXT_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         LABEL_DISTANCE_IN_ADVANCED_SEARCH, LABEL_TEXT_DISTANCE_IN_ADVANCED_SEARCH),
        ]
    CHECKBOX_SYNONYM = [
        (MainPageLocators.TAB_COMPETENCY, SYNONYMS_IN_ADVANCED_SEARCH, DISTANCE_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, SYNONYMS_IN_ADVANCED_SEARCH, DISTANCE_IN_ADVANCED_SEARCH)
    ]
    CHECKBOX_FULLTEXT = [
        (MainPageLocators.TAB_COMPETENCY, FULL_TEXT_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, FULL_TEXT_IN_ADVANCED_SEARCH)
    ]
    CHECKBOX_DISTANCE = [
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -55, ' 0'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -40, ' 1'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -30, ' 2'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -20, ' 3'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -10, ' 4'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 5, ''),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 10, ' 6'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 20, ' 7'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 30, ' 8'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 40, ' 9'),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 55, ' 10'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -55, ' 0'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -40, ' 1'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -30, ' 2'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -20, ' 3'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, -10, ' 4'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 5, ''),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 10, ' 6'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 20, ' 7'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 30, ' 8'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 40, ' 9'),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         SYNONYMS_IN_ADVANCED_SEARCH, VALUE_DISTANCE_IN_ADVANCED_SEARCH, 55, ' 10'),
    ]

    CHECKBOX_SYNONYM_AND_FULLTEXT = [
        (MainPageLocators.TAB_COMPETENCY, SYNONYMS_IN_ADVANCED_SEARCH,
         FULL_TEXT_IN_ADVANCED_SEARCH, DISTANCE_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, SYNONYMS_IN_ADVANCED_SEARCH,
         FULL_TEXT_IN_ADVANCED_SEARCH, DISTANCE_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_COMPETENCY, DISTANCE_IN_ADVANCED_SEARCH,
         FULL_TEXT_IN_ADVANCED_SEARCH, SYNONYMS_IN_ADVANCED_SEARCH),
        (MainPageLocators.TAB_DOC, DISTANCE_IN_ADVANCED_SEARCH,
         FULL_TEXT_IN_ADVANCED_SEARCH, SYNONYMS_IN_ADVANCED_SEARCH)
    ]


class LoginPageLocators:
    AUTH_FORM = (By.CSS_SELECTOR, '.card-body.form-auth form')
    ENTER_EMAIL = (By.CSS_SELECTOR, 'input[id="loginForm"]')
    ENTER_PASSWORD = (By.CSS_SELECTOR, 'input[id="passwordForm"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, '.w-100.btn-primary')
    BUTTON_PERSONAL_ACC = (By.ID, 'topMenuUser')
    CHOOSE_DOMAIN = (By.CSS_SELECTOR, '.input-group.login button.btn.dropdown-toggle')
    NO_DOMAIN = (By.CSS_SELECTOR, '.dropdown-menu.show .dropdown-item:nth-child(6)')


class SearchCompetencyPageLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[placeholder="Поиск компетенций"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, 'button.btn-search[type="button"]')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '.btn-search[type="button"]')
    BUTTON_CLEAR = (By.CSS_SELECTOR, '.fas.fa-times-circle')
    MODULE_MAP = (By.CSS_SELECTOR, '.container >div >div:nth-child(6) .card-body')
    CONTENT_MAP = (By.ID, 'map')
    MODULE_STATISTICS = (By.CSS_SELECTOR, '[href="#collapse-stats"]')
    CONTENT_STATISTICS = (By.CSS_SELECTOR, '.container >div >div:nth-child(7)')
    MODULE_GRAPH_AK = (By.CSS_SELECTOR, '[href="#collapse-social-graph-author-teams"]')
    CONTENT_GRAPH_AK = (By.CSS_SELECTOR, '.container >div >div:nth-child(8)')
    MODULE_GRAPH_KO = (By.CSS_SELECTOR, '[href="#collapse-social-graph-organization-teams"]')
    CONTENT_GRAPH_KO = (By.CSS_SELECTOR, '.container >div >div:nth-child(9)')
    MODULE_RATING = (By.CSS_SELECTOR, '.container >div >div:nth-child(10)')

class MapLocators:
    TITLE = (By.CSS_SELECTOR, '.container >div >div:nth-child(6) h3')
    BUTTON_FULL_SCREEN = (By.CSS_SELECTOR, '.container >div >div:nth-child(6)  > div > div > div > a:nth-child(1)')
    BUTTON_REFRESH = (By.CSS_SELECTOR, '.container >div >div:nth-child(6)  > div > div > div > a:nth-child(2)')
    ZOOMCONTROL_BODY = (By.CSS_SELECTOR, '.zoomcontrol-slider-body')
    BUTTON_ZOOMCONTROL_OUT = (By.CSS_SELECTOR, '.zoomcontrol-zoom-out')
    BUTTON_ZOOMCONTROL_IN = (By.CSS_SELECTOR, '.zoomcontrol-zoom-in')
    ZOOMCONTROL_SLIDER = (By.CSS_SELECTOR, '.zoomcontrol-slider')
    ZOOMCONTROL_LEVEL_REGIONS = (By.CSS_SELECTOR, '.zoomcontrol-hints-container div:nth-child(1) span')
    ZOOMCONTROL_LEVEL_AGLOMIRATIONS = (By.CSS_SELECTOR, '.zoomcontrol-hints-container div:nth-child(2) span')
    ZOOMCONTROL_LEVEL_TOWNS = (By.CSS_SELECTOR, '.zoomcontrol-hints-container div:nth-child(3) span')
    HINTS_ZOOMCONTROL_LEVELS = (By.CSS_SELECTOR, '.zoomcontrol-hints-container div:nth-child({}) span')
    ZOOMCONTROL_LEVELS = (By.CSS_SELECTOR, '.zoomcontrol-hints-container div:nth-child({})')
    SCALE_VALUE = (By.CSS_SELECTOR, '.zoom-text')


class StatisticLocators:
    TITLE = (By.CSS_SELECTOR, '.container >div >div:nth-child(7) h3')
    QUANTITY_CHARTS = (By.CSS_SELECTOR, '#chart > div')
    LEGEND_CHART = (By.CSS_SELECTOR, '#chart >div:nth-child({}) div')




class ReleasePageLocators:
    TITLE = (By.ID, 'h1')

class FaqPageLocators:
    TITLE = (By.ID, 'h1')

class HelpPageLocators:
    TITLE = (By.ID, 'h1')

class AnaliticPageLocators:
    TITLE = (By.ID, 'h1')

class ServicesPageLocators:
    TITLE = (By.ID, 'h1')

class InfoAboutProviderPageLocators:
    TITLE = (By.ID, 'h1')

