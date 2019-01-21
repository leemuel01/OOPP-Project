import sqlite3
import requests
import datetime
"""
sqlite_connection = sqlite3.connect("Flask/site.db")
sqlite_connection.cursor()
num_rows = sqlite_connection.execute("select count(id) from post_review")


review_display = sqlite_connection.execute("select * from post_review where id=2")

print(review_display)
for i in review_display:
    print("id= ", i[0], i[1], i[2])
"""

def display_review():
    sqlite_connection = sqlite3.connect("Flask/site.db")
    row_count = sqlite_connection.execute("select count(*) from post_review").fetchone()[0]
    print(row_count)
    all_review = []
    for i in range(row_count):
        review_row = sqlite_connection.execute("select * from post_review where id = ?", (i+1,))

        for j in review_row:
            row_review = [j[0], j[1], j[2]]
            all_review.append(row_review)
    return all_review


display_review()


#=============================================post=========================================
def submit():
    variable1 = requests.form.get("project")
    form_date_now = datetime.datetime.now()
    post_comment = review_display.execute("insert into review_table_name(content,date_posted) values (?,?)"
                                            , (variable1, form_date_now))




#======================================delete=================================
"""delete_review_display = sqlite_connection.execute("delete from post_review where ")
review_display.commit()"""