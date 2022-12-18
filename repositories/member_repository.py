from db.run_sql import run_sql

from models.gym_class import Gym_class
from models.member import Member


def save(member):
    sql = 'INSERT INTO members(name) VALUES (%s) RETURNING id'
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = 'SELECT * FROM members'
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['id'])
    return member

def members_for_gym_class(gym_class):
    members = []

    sql = 'SELECT members.* FROM members INNER JOIN sessions ON sessions.member_id = members.id WHERE gym_class_id = %s'
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members


def delete_all():
    sql = 'DELETE FROM members'
    run_sql(sql)


def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)
