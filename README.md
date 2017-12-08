# Icon 8 API tests

### Minimum Requirements
    Python 2.7
    Pytest-3.1.2
    

### Команда для запуска
    python init.py -request_url demoapi -auth_id f5901f402ac93fb372b19542f73cd3103a794b83
    
    
### Структура
    init.py - файл запуска
    param.json - параметры запуска
    api_logic.py - логика тестов.
    tests папка - Содержит в себе тесты, 1 файл - 1 api.
    context папка - Содержит фикстуры и доп. контекст каждого тестового класса
    
    1 файл - 1 api
    1 тестовый класс - проверяет 1 ответ с определёнными настройками
    1 метод - проверяет 1 тег  с определёнными настройками.
    В 1 методе может содержаться проверок более одного атрибута одного тега.

### Существующие тесты api:
    - Search
    - Suggest
    - Latest
    - Total
    - Icon
    - Icons
    - Similiar
    - List
    - Category
    - Ctegories
    - v2 Icon
    - v2 Vategory
    - v2 Categories
    - v3 Latest
    - v3 Search
    - v3 Categoreis
    - v3 Category
    - v3 Total

### Api:
    Описание всего апи (плюс - покрыт тестами\ минус - покрыт тестамиы)
    v1 (возвращают результат в xml, медленно устаревают)

        - search (-) -				/api/iconsets/search?term=car&platform=ios7&amount=25
        - download (-) -			/api/iconsets/download?id=1&format=png&size=100&color=ffff00&filename=test.png
        - download-collection (-) -	/api/iconsets/download-collection?ids=1,2,3&format=png&size=100&color=ffff00
        - suggest (+) -				/api/iconsets/suggest?term=car&platform=ios7&amount=25
        - latest (+) -				/api/iconsets/latest?amount=10&platform=ios7
        - total (+) -				/api/iconsets/total?since=2015-01-01
        - icon (+) -				/api/iconsets/icon?id=17
        - icons (+) -				/api/iconsets/icons?amount=10&offset=0&platform=ios7
        - responsive icons - 	    /api/iconsets/responsive-icons?amount=10&offset=0&platform=responsive
        - svg set -				    /api/iconsets/svg-symbol?icons=flat_color-address_book,flat_color-about,ios-about
        - similar (+) -				/api/iconsets/similar?id=17&amount=10
        - list (+) -				/api/iconsets/list?platform=ios7
        - category (+) -			/api/iconsets/category?category=Animals&attributes=filled&amount=10&platform=ios7
        - categories (+) -			/api/iconsets/categories?platform=ios7

    v2 (возвращают результат в xml и в json - задается параметром format)

        - icon (+) -				/api/iconsets/v2/icon?id=1833&format=json&files=eps,svg&variants=enabled&info=enabled
        - category (+) -			/api/iconsets/v2/category?category=Animals&attributes=filled&amount=10&platform=ios7
        - categories (+) -			/api/iconsets/v2/categories?platform=ios7

    v3 (возвращают json, работают быстрее, инфы возвращают по минимуму - только то, что нужно веб-аппу)

        - latest (+) -				/api/iconsets/v3/latest?amount=10&platform=ios7&offset=10&impresser_preview=true&language=en-US
        - search (+) -				/api/iconsets/v3/search?term=facebook&amount=10&platform=ios7&offset=10
        - categories (+) -			/api/iconsets/v3/categories?platform=ios7
        - category (+) -			/api/iconsets/v3/category?category=Animals&amount=10&platform=ios7
        - resolutions (-) -			/api/iconsets/v3/resolutions?icon_id=10   --- 4 свг для офисной иконки
        - total (+) -				/api/iconsets/v3/total?since=2015-01-01
    










