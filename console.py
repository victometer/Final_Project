import pdb
from models.gym_class import Gym_class
from models.member import Member
from models.session import Session

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

session_repository.delete_all()
member_repository.delete_all()
gym_class_repository.delete_all()

member1 = Member ('Joe')
member_repository.save(member1)

member2 = Member ('Kate')
member_repository.save(member2)

member3 = Member ('Sam')
member_repository.save(member3)


gym_class1 = Gym_class ('Pilates', '12:45', 60)
gym_class_repository.save(gym_class1)

gym_class2 = Gym_class ('Zumba', '10:45', 60)
gym_class_repository.save(gym_class2)

gym_class3 = Gym_class ('Yoga', '19:45', 60)
gym_class_repository.save(gym_class3)

session1 = Session (member1, gym_class1)
session_repository.save(session1)

session2 = Session (member2, gym_class1)
session_repository.save(session2)

session3 = Session (member3, gym_class1)
session_repository.save(session3)

session4 = Session (member1, gym_class2)
session_repository.save(session4)

session5 = Session (member1, gym_class3)
session_repository.save(session5)

session6 = Session (member3, gym_class3)
session_repository.save(session6)



# pdb.set_trace()