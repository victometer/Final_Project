from db.run_sql import run_sql

from models.gym_class import Gym_class
from models.member import Member


def save(gym_class):
    sql = 'INSERT INTO gym_classes(name, time, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING id'
    values = [gym_class.name, gym_class.time, gym_class.duration, gym_class.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    gym_classes = []

    sql = 'SELECT * FROM gym_classes'
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['time'], row['duration'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes
    
def select(id):
    sql = 'SELECT * FROM gym_classes WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['time'], result['duration'], result['capacity'], result['id'])
    return gym_class

def gym_classes_for_member(member):
    gym_classes = []

    sql = 'SELECT gym_classes.* FROM gym_classes INNER JOIN sessions ON sessions.gym_class_id = gym_class.id WHERE member_id = %s'
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Gym_class(row['name'], row['time'], row['duration'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes



def delete_all():
    sql = 'DELETE FROM gym_classes'
    run_sql(sql)

def update(gym_class):
    sql = "UPDATE gym_classes SET (name, time, duration) = (%s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.time, gym_class.duration, gym_class.capacity, gym_class.id]
    run_sql(sql, values)



