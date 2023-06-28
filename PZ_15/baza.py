import sqlite3 as sq

# ВАРИАНТ 2

with sq.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute('''create table if not exists goods (
        id_go integer primary key,
        name varchar,
        description varchar, 
        si varchar)
    ''')
    cur.execute('''create table if not exists shops (
        id_sh integer primary key,
        name varchar,
        address varchar, 
        number varchar)
    ''')
    cur.execute('''create table if not exists requests (
        id_req integer primary key,
        id_sh integer,
        data date,
        foreign key (id_sh) references shops(id_sh))
    ''')
    cur.execute('''create table if not exists invent_list (
        id_il integer primary key,
        id_go integer,
        count_go int,
        foreign key (id_go) references goods(id_go))
    ''')
    cur.execute('''create table if not exists compound (
        id_co integer primary key,
        id_req integer,
        id_go integer,
        count int,
        foreign key (id_go) references goods(id_go),
        foreign key (id_req) references requests(id_req))
    ''')

lst_gooods = [(1, 'Огурец', 'Гладкий', 'кг'), (2, 'Помидор', 'Красный', 'кг'), (3, 'Творог', 'Обезжиренный', 'шт'),
              (4, 'Молоко', '1%', 'л'), (5, 'Булочка', 'Шоколадная', 'шт'), (6, 'Соус', 'Сырный', 'шт'),
              (7, 'Сок', 'Томатный', 'л'), (8, 'Картофель', 'Мелкий', 'кг'), (9, 'Печенье', 'Шоколадное', 'гр'),
              (10, 'Рис', 'Крупный', 'гр')]
lst_shops = [(1, 'Жасмин', 'пер. Братский 45', '89345670067'), (2, 'Магнит', 'пер. Халтуринский 33', '89006721234'),
             (3, 'У дома', 'ул. Большая Садовая 105', '89248420485'),
             (4, 'Пятерочка', 'ул. Московская 56', '89331284500'),
             (5, 'Пятница', 'ул. Сергеева 57', '89247682948'),
             (6, 'Ключик', 'пер. Гоголевский 103', '89005670067'), (7, 'Дом', 'ул. Петровская 11', '89231114422'),
             (8, 'Оксана', 'пер. Славы 112', '8910340756'),
             (9, 'Красота', 'ул. Максима Горького 7', '89890467007'),
             (10, 'Вкуснятина', 'пер. Дорожный 35', '892346076553')]
lst_req = [(1, 1, '2023-03-31'), (2, 1, '2023-03-31'), (3, 2, '2023-04-01'), (4, 4, '2023-03-31'),
           (5, 10, '2023-04-01'), (6, 10, '2023-03-28'), (7, 7, '2023-03-30'), (8, 4, '2023-04-01'),
           (9, 3, '2023-02-13'), (10, 2, '2023-01-02')]
lst_il = [(1, 1, 34), (2, 2, 12), (3, 3, 89), (4, 4, 3), (5, 5, 100), (6, 6, 23), (7, 7, 56), (8, 8, 12), (9, 9, 34),
          (10, 10, 78)]
lst_com = [(1, 1, 4, 1), (2, 2, 4, 2), (3, 3, 5, 34), (4, 5, 10, 30), (5, 4, 4, 12), (6, 6, 3, 89), (7, 8, 10, 10),
           (8, 7, 9, 34), (9, 9, 4, 5)]

with sq.connect('base.db') as conn:
    cur = conn.cursor()
    cur.executemany('insert into goods values(?, ?, ?, ?)', lst_gooods)
    cur.executemany('insert into shops values(?, ?, ?, ?)', lst_shops)
    cur.executemany('insert into requests values(?, ?, ?)', lst_req)
    cur.executemany('insert into invent_list values(?, ?, ?)', lst_il)
    cur.executemany('insert into compound values(?, ?, ?, ?)', lst_com)

# SELECT

with sq.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute('select name, description from goods')  # 1
    res_1 = cur.fetchall()
    print(res_1)
    cur.execute('select name, address from shops')  # 2
    res_2 = cur.fetchall()
    print(res_2)
    cur.execute('select id_sh, data from requests')  # 3
    res_3 = cur.fetchall()
    print(res_3)
    cur.execute('select goods.name, invent_list.count_go from goods inner join invent_list on goods.id_go = '
                'invent_list.id_go')  # 4
    res_4 = cur.fetchall()
    print(res_4)
    cur.execute(
        'select goods.name, invent_list.count_go from goods inner join invent_list on goods.id_go = invent_list.id_go '
        'order by invent_list.count_go desc')  # 5
    res_5 = cur.fetchall()
    print(res_5)
    cur.execute(
        'select requests.id_req, goods.name from requests inner join compound on requests.id_req = compound.id_req '
        'inner join goods on compound.id_go = goods.id_go')  # 6
    res_6 = cur.fetchall()
    print(res_6)
    cur.execute(
        'select goods.name, invent_list.count_go from goods inner join invent_list on goods.id_go = invent_list.id_go '
        'where invent_list.count_go < 10')  # 7
    res_7 = cur.fetchall()
    print(res_7)
    cur.execute('select * from requests where data between "2023-03-01" and "2023-03-31"')  # 8
    res_8 = cur.fetchall()
    print(res_8)
    cur.execute('''select * from shops where id_sh in (select id_sh from requests join compound on requests.id_req = 
    compound.id_req join invent_list on compound.id_go = invent_list.id_go where invent_list.count_go < 20 group by 
    id_sh )''')  # 9
    res_9 = cur.fetchall()
    print(res_9)

# UPDATE 

with sq.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute('update invent_list set count_go = 50 where id_il=1')  # 1
    cur.execute('update compound set id_go = 1, count = 12 where id_co=2')  # 2, 3
    cur.execute('update shops set address = "ул. Одуанчиков, 15" where id_sh=10')  # 4
    cur.execute('update requests set data = "2023-04-07" where id_sh=9')  # 5
    cur.execute('update invent_list set count_go = 100 where id_go > 5')  # 6
    cur.execute('update goods set description = "Какoй-то" where id_go = 9')  # 7
    cur.execute(
        'update invent_list set count_go = (select count_go from invent_list) - (select count from compound)')  # 8
    cur.execute(
        'update invent_list set count_go = (select count_go from invent_list where id_go = 1) - (select count from '
        'compound where id_go = 1) where id_go = 1')  # 9
    cur.execute(
        'update shops set name = "Кукурузники", address = "ул. Колокольчиков, 34" where id_sh = (select id_sh from '
        'requests where id_sh = 3)')  # 10
    cur.execute(
        'update requests set id_sh = (select id_sh from shops where name = "Куку") where id_sh = (select id_sh from '
        'shops where name = "Ключик" ) ')  # 11
    cur.execute('update compound set count = 30, id_req = 8 where id_go = 4')  # 12
    cur.execute(
        'update goods set description = "Испорчен", id_go = (select id_il from invent_list where count_go = 34) where '
        'id_go =  (select id_go from invent_list where count_go = 34 or count_go = 100) ')  # 13

# DELETE

with sq.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute('delete from compound where id_req = 1')  # 1
    cur.execute('delete from requests where id_req = 1 ')
    cur.execute('delete from invent_list where id_go not in (select distinct id_go from compound)')  # 2
    cur.execute('delete from shops where address like "ул. Ленина%"')  # 3
    cur.execute('delete from compound where id_go in (select id_go from invent_list where count_go = 0 )')  # 4
    cur.execute(
        'delete from shops where id_sh not in (select id_sh from requests where data > date("now", "-1 month") )')  # 5
    cur.execute('delete from goods where id_go not in (select distinct id_go from compound )')  # 6
    cur.execute('delete from invent_list where id_go not in (select distinct id_go from compound )')  # 7
    cur.execute(
        'delete from compound where id_req in (select id_req from requests where data <= date("now", "-1 month"))')  # 8
