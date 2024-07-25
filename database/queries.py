class Queries:
    CREATE_REVIEW_DIALOG_TABLE = '''
    CREATE TABLE IF NOT EXISTS review_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        visit_date DATE,
        food_rating INTEGER,
        cleanliness_rating INTEGER,
        extra_comments TEXT
    )
    '''

    DROP_DISHES_CATEGORY_TABLE = 'DROP TABLE IF EXISTS dishes_category'

    CREATE_DISHES_CATEGORY_TABLE = '''
    CREATE TABLE IF NOT EXISTS dishes_category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
    '''

    POPULATE_DISHES_CATEGORY_TABLE = '''
    INSERT INTO dishes_category(name) VALUES 
    ('Завтраки'),
    ('Восточные блюда'),
    ('Первые блюда')
    '''

    DROP_DISHES_TABLE = 'DROP TABLE IF EXISTS dishes'

    CREATE_DISHES_TABLE = '''
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        cover TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES dishes_category(id)
        )
    '''

    POPULATE_DISHES_TABLE = '''
    INSERT INTO dishes(name, price, cover, category_id) VALUES 
    ('Босо лагман', 140, 'media/for_menu/boso_lagman.jpg', 2),
    ('Гуйру лагман', 130, 'media/for_menu/guyru_lagman.jpg', 2),
    ('Пельмени', 100, 'media/for_menu/pelmeni.jpg', 3),
    ('Блины со сметаной', 60, 'media/for_menu/bliny.jpg', 1)
    '''
