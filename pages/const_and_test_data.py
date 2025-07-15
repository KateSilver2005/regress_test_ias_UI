class TestData:
    TEST_LOGIN = 'EAlekseeva@cspfmba.ru'
    TEST_PASSWORD = 'KateSilver1'
    SEARCH_COMPETENCY = 'ГЕНЕТИЧЕСКИЕ ФАКТОРЫ В ВОЗНИКНОВЕНИИ УРОЛОГИЧЕСКИХ ОНКОЛОГИЧЕСКИХ ЗАБОЛЕВАНИЙ'
    #SEARCH_COMPETENCY = 'Центр коллективного пользования научным оборудованием «Центр исследований минерального сырья и состояния окружающей среды»'
    # SEARCH_COMPETENCY = 'crispr'
    SEARCH_PARAM = {'search': SEARCH_COMPETENCY}


class Env:
    # MAIN_LINK = 'https://nir.pak-cspmz.ru/'
    # MAIN_LINK = 'https://nirtest-portal.cspfmba.ru/'
    MAIN_LINK = 'https://nir-stage.pak-cspmz.ru/'


class ConstMyCompanyPage:
    my_company_path = 'cabinet/mycompany'
    title_in_info_about_provider_page = "моя организация"


class ConstAnaliticPage:
    analitic_path = 'cabinet/analytic'
    title_in_analitic_page = "аналитика"


class ConstServicesPage:
    services_path = 'cabinet/services'
    title_in_services_page = "сервисы"

class ConstFaqPage:
    faq_path = "faq"
    title_in_faq_page = "часто задаваемые вопросы"

class ConstRealesePage:
    release_path = "release"
    title_in_release_page = "релиз приложения"

class ConstHelpPage:
    help_path = "help"
    title_in_help_page = "краткий курс по нир"

class ConstNewsPage:
    title_in_news_page = 'новости'
    news_path = 'cabinet/news?search=&types=ias_news_docnews&types=hot_news&ordering=-publication_date&page=1'
    title_icon_scipub_in_hot_news = "Новости из публикаций"
    description_icon_scipub_in_hot_news = "Публикации"
    title_icon_smi_in_hot_news = "Новости СМИ"
    description_icon_smi_in_hot_news = "Новости СМИ"


class ConstMainPage:
    MAIL_SUPPORT = "mailto:is@cspfmba.ru"
    title_text_in_header_part1 = "национальный"
    title_text_in_header_part2 = "информационный ресурс"
    inscription_in_header = ("содержащий сведения о популяционных иммунологических и генетических исследованиях, "
                             "проводимых в Российской Федерации")
    text_csp_in_footer = "ФГБУ «ЦСП» ФМБА России"
    text_fmba_in_footer_part1 = "Федеральное медико-"
    text_fmba_in_footer_part2 = "биологическое агентство"
    title_and_inscription_in_footer_part1 = "Национальный информационный ресурс,"
    title_lk = 'Личный кабинет'
    placeholder_competency = 'Поиск компетенций'
    placeholder_doc = 'Исходные документы'
    placeholder_org = 'Поиск по организациям'
    placeholder_person = 'Поиск ученых'
    PLACEHOLDERS = [
        placeholder_competency,
        placeholder_doc,
        placeholder_org,
        placeholder_person
    ]
    title_grafic_vneseniya_svedeniy = 'график внесения сведений'
    title_section_news = 'новости'
    text_to_link_in_section_news = 'все новости'
    title_global_charts = 'статистика'
    title_info_users = 'информация для пользователей'
    title_of_slide_in_global_charts = [
        'используемые источники данных за последние 10 лет',
        'распределение диссертаций по годам',
        'распределение ниокр по годам',
        'распределение рид по годам',
        'распределение икрбс по годам',
        'распределение грантов рнф по годам',
        'распределение публикаций по годам',
        'распределение патентов по годам',
        'динамика количества инициированных нир по генетике и иммунологии за последние 5 лет',
        'рейтинг публикационной активности за 2022 год',
        'основные заказчики генетических и иммунологических нир за последние 5 лет',
        'основные исполнители исследований в области генетики и иммунологии за 2022 год',
        'количество выданных патентов в российской федерации с 2017 по 2022 годы в области генетики и иммунологии',
        'топ-5 разработчиков генетических баз данных, разработанных в 2022 году',
        'финансирование закупки оборудования, расходных материалов и технического обслуживания в 2022 году',
        'распределение генно-инженерных методов по частоте применения в 2022 году',
        'зарегистрированные в 2021-2022 годах иммунологические лекарственные препараты'
    ]

    dict_global_chart_may_2025 = {
        "Диссертации": [0, 1, 0, 0, 0, 0, 0, 340, 2550, 2549, 1967, 2548, 2614, 2467, 2244, 10],
        "НИОКР": [0, 0, 0, 0, 0, 0, 0, 0, 5850, 4068, 3164, 3543, 5127, 3925, 2502, 113],
        "РИД": [0, 0, 0, 0, 0, 0, 0, 0, 1674, 3322, 2641, 2278, 3992, 4638, 4327, 555],
        "ИКРБС": [0, 0, 0, 0, 0, 0, 0, 0, 3761, 4701, 4210, 3633, 5098, 5356, 5387, 468],
        "Гранты РНФ": [0, 0, 0, 0, 344, 89, 228, 376, 289, 458, 289, 407, 523, 0, 0, 0],
        "Публикации": [0, 0, 0, 0, 0, 0, 0, 0, 87072, 90273, 88179, 83361, 85453, 81970, 47798, 132],
        "Патенты": [2015, 6866, 12197, 13022, 13957, 14672, 12847, 15457, 15913, 16858, 14009, 12256, 6743, 0, 0, 0],
        "Год": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    }
    images_in_info_for_users = ["elibrary", "pubmed_medline", "pmc", "nioktr", "yandexpatent", "ntirf", "grants",
                                "scopus", "rffi", "zakupki", "goslekarstva", "zdravnadzor", "goslekarstva",
                                "googleacademy", "googlepatent", "webofscience"]
    titles_in_info_for_users = ['Научная электронная библиотека E-library', 'Pubmed Medline', 'Pubmed Central',
                                'ЕГИСУ НИОКР', 'Яндекс.Патенты', 'Научно-технологическая инфраструктура (НТИ РФ)',
                                'Российский научный фонд', 'База данных Scopus',
                                'Российский фонд фундаментальных исследований',
                                'ЕИС ЗАКУПКИ', 'Государственный реестр лекарственных средств',
                                'Единый реестр лицензий Росздравнадзора',
                                'Клинические исследования', 'Google Академия', 'Google Патенты',
                                'База данных Web of Science']
    urls_in_info_for_users = ['elibrary.ru', 'pubmed.ncbi.nlm.nih.gov',
                              'pmc.ncbi.nlm.nih.gov', 'rosrid.ru/', 'yandex.ru/patents',
                              'ckp-rf.ru', 'rscf.ru', 'scopus.com', 'rfbr.ru',
                              'sbis-zakupki.ru', 'grls.rosminzdrav.ru', 'roszdravnadzor.gov.ru',
                              'grls.rosminzdrav.ru', 'scholar.google.ru', 'patents.google.com',
                              'access.clarivate.com']
    total_scipubs_in_info_for_users = [[513832, 410912], [72330, 30394], [25079, 24590], [0, 0], 'Публикаций', 'Полных текстов']
    description_rosrid = ['НИОКР', 28292, 'РИД', 23427, 'ИКРБС', 32614, 'Диссертаций', 17291]
    description_ya_patents = ['Патентов', 156812, 'Полных текстов', 156812]
    description_ckp_usu = ['ЦКП', 598, 'Оборудование ЦКП', 13799, 'Услуги ЦКП', 7072, 'УНУ', 391,
                           'Оборудование УНУ', 4958, 'Услуги УНУ', 1375]
    description_rnf = ['Грантов', 3003]


class ConstHotNewsModule:
    EACH_NEWS_PAGE = 'cabinet/news/'
    icon_scipub = "Публикации"
    icon_smi = "Новости СМИ"


class ConstCompetencyPage:
    title_in_module_map_in_competency_page = 'карта'
    full_screen_in_map = 'на весь экран'
    hints_zoomcontrol_level_in_map = [(1, 'Регионы'), (2, 'Агломерации'), (3, 'Города')]
    zoomcontrol_level_in_map = [('x 1.00', 1), ('x 4.00', 2), ('x 12.00', 3)]
    title_in_module_statistic_in_competency_page = 'статистика'
    titles_chart_in_statistic_in_competency_page = [(0, "Публикационная и другие виды активности"),
                                                     (1, "Суммы, выделяемые на НИОКР, млн. руб."),
                                                     (2, "Топ-5 журналов по количеству публикаций"),
                                                     (3, "Топ-5 авторов по количеству работ"),
                                                     (4, "Топ-5 организаций по количеству работ")]
    name_aixis_of_charts_in_statistic_in_competency_page = [(0, ['results', 0, 'options', 'scales', 'x', 'title', 'text'], "Годы"),
                                                            (0, ['results', 0, 'options', 'scales', 'y', 'title', 'text'], "Количество"),
                                                            (1, ['results', 1, 'options', 'scales', 'x', 'title', 'text'], "Годы"),
                                                            (1, ['results', 1, 'options', 'scales', 'y', 'title', 'text'], "Сумма"),
                                                            (2, ['results', 2, 'data', 'labels', 0], "За весь период"),
                                                            (3, ['results', 3, 'data', 'labels', 0], "Публикации"),
                                                            (4, ['results', 4, 'data', 'labels', 0], "Публикации")]
    color_entity_in_chart_activites_in_statistic_in_competency_page = {
        'Диссертации': '#ff9f1c',
        'НИОКР': '#f1d600',
        'РИД': '#c8ff00',
        'ИКРБС': '#4c5dc9',
        'Гранты РНФ': '#eb5a47',
        'Публикации': '#61bd50',
        'Патенты': '#c378e1'
    }
    color_entity_in_chart_niokr_budjet_in_statistic_in_competency_page = {'Бюджет': '#f1d600'}
    correct_color_entity_in_charts = [(0, color_entity_in_chart_activites_in_statistic_in_competency_page),
                                     (1, color_entity_in_chart_niokr_budjet_in_statistic_in_competency_page)]
    title_of_element_in_legent_chart_activity_in_global_charts = ['Диссертации', 'НИОКР', 'РИД', 'ИКРБС', 'Гранты РНФ',
                                                         'Публикации', 'Патенты']
    title_in_legent_chart_niokr_budget_in_global_charts = ['Бюджет']
    correct_name_entity_in_charts = [(0, title_of_element_in_legent_chart_activity_in_global_charts),
                                     (1, title_in_legent_chart_niokr_budget_in_global_charts)]
    color_entity_in_top_5_charts_in_statistic_in_competency_page = ['#108dff', '#60bc4e', '#0154ad', '#ea5a46', '#f1d600']

