#!/usr/bin/env python3
import psycopg2


def connect(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Error in connecting to database")


# The questions that these queries answer
question_1 = ("What are the most popular three articles of all time?")
question_2 = ("Who are the most popular article authors of all time?")
question_3 = ("On which days did more than 1% of requests lead to errors?")

# This query answers first question
query_1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# This query answers second question
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# This query answers third question
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def get_result(query):
    # Return the results of the first and the second queries
    db, c = connect()
    c.execute(query)
    return c.fetchall()
    db.close()


def print_result(query_results):
    # Return the results of the first and the second queries
    print (query_results[1])
    for i, items in enumerate(query_results[0]):
        print (
            "\t", i+1, "-", items[0],
            "\t -", str(items[1]), "views")


def print_error_results(query_results):
    # return the result of the last query
    print (query_results[1])
    for items in query_results[0]:
        print ("\t", items[0], "-", str(items[1]) + "% errors")


if __name__ == '__main__':
    # Store the results
    popular_articles = get_result(query_1), question_1
    popular_authors = get_result(query_2), question_2
    get_errors = get_result(query_3), question_3

    # Print out the results
    print_result(popular_articles)
    print_result(popular_authors)
    print_error_results(get_errors)
