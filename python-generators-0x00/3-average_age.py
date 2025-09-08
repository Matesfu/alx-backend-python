#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    """Generator that streams user ages one by one from the DB"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:   
        yield row["age"]
    connection.close()


def compute_average_age():
    """Compute average age using generator without loading all rows"""
    total_age = 0
    count = 0
    for age in stream_user_ages():   
        total_age += age
        count += 1
    
    average_age = total_age / count if count > 0 else 0
    print(f"Average age of users: {average_age:.2f}")
