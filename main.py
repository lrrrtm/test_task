import sys

from psycopg2 import extras
import psycopg2 as pg

from data import articles, orders

connection = pg.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="postgressuper",
    database="shop",
)
cur = connection.cursor(cursor_factory=extras.RealDictCursor)


def manual_insert_articles():
    sql = """
            INSERT INTO articles (id, name, main_shelf, opt_shelfs) 
            VALUES (%(id)s, %(name)s, %(main_shelf)s, %(opt_shelfs)s)
            """
    cur.executemany(sql, articles)
    connection.commit()


def manual_insert_orders():
    sql = """
            INSERT INTO orders (id, articles)
            VALUES (%(id)s, %(articles)s)
            """
    cur.executemany(sql, orders)
    connection.commit()


articles_cache = {}


def sort_by_shelfs(orders_list):
    result = {}
    cur.execute(f"SELECT * FROM orders WHERE id IN %s", (orders_list,))
    orders = cur.fetchall()
    for order in orders:
        for article in order['articles']:
            if article['id'] not in articles_cache:
                cur.execute(f"SELECT * FROM articles WHERE id = {article['id']}")
                articles_cache[article['id']] = cur.fetchone()
            article_info = articles_cache[article['id']]

            opt_shelfs = ""
            if article_info['opt_shelfs']:
                opt_shelfs = ",".join(article_info['opt_shelfs'])

            if article_info['main_shelf'] not in result:
                result[article_info['main_shelf']] = []

            result[article_info['main_shelf']].append(
                {
                    "name": article_info['name'],
                    "article_id": article_info['id'],
                    "order_id": order['id'],
                    "amount": article['amount'],
                    "opt_shelfs": opt_shelfs
                }
            )
    return result


def print_shelfs(dictionary):
    for shelf in dictionary:
        print(f"===Стеллаж {shelf}")
        for article in dictionary[shelf]:
            print(f"{article['name']} (id={article['article_id']})")
            print(f"заказ {article['order_id']}, {article['amount']} шт")
            if article['opt_shelfs']:
                print(f"доп стелаж: {article['opt_shelfs']}")
            print("\n")


if __name__ == "__main__":
    manual_insert_articles()
    manual_insert_orders()
    sorted_by_shelf = sort_by_shelfs(tuple(sys.argv[1:]))
    print(f"Страница сборки заказов {', '.join(sys.argv[1:])}")
    print_shelfs(sorted_by_shelf)
