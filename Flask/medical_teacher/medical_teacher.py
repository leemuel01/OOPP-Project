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
class MedicalTeacher():
    def __init__(self):
        pass

    def display_review(self):
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




#=============================================post=========================================





#======================================delete=================================
"""delete_review_display = sqlite_connection.execute("delete from post_review where ")
review_display.commit()"""