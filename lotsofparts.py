"""Generate example data."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Part, User

engine = create_engine('postgresql://catalog:catalog@localhost:5432/items')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="CPUs/Processors")

session.add(category1)
session.commit()

category2 = Category(user_id=1, name="Memory")

session.add(category2)
session.commit()

category3 = Category(user_id=1, name="Motherboards")

session.add(category3)
session.commit()

category4 = Category(user_id=1, name="Video Cards")

session.add(category4)
session.commit()

part1 = Part(user_id=1, name="AMD FX Processor",
             description="Processors built on AMD Bulldozer and Piledriver microarchitectures", category=category1)

session.add(part1)
session.commit()

part2 = Part(user_id=1, name="Intel Core Processor",
             description="Processors built on Intel Skylake and Kaby Lake microarchitectures", category=category1)

session.add(part2)
session.commit()

part3 = Part(user_id=1, name="ARM processor",
             description="Processors built on ARM microarchitectures")

session.add(part3)
session.commit()

part4 = Part(user_id=1, name="4GB RAM",
             description="4 gigabytes of DDR3 memory", category=category2)

session.add(part4)
session.commit()

part5 = Part(user_id=1, name="8GB RAM",
             description="8 gigabytes of DDR3 memory", category=category2)

session.add(part5)
session.commit()

part6 = Part(user_id=1, name="16GB RAM",
             description="16 gigabytes of DDR3 memory", category=category2)

session.add(part6)
session.commit()

part7 = Part(user_id=1, name="Intel Motherboard",
             description="Intel Core iX Motherboard", category=category3)

session.add(part7)
session.commit()

part8 = Part(user_id=1, name="AMD Motherboard",
             description="AMD Ryzen Motherboard", category=category3)

session.add(part8)
session.commit()

part9 = Part(user_id=1, name="Nvidia Geforece Video Card",
             description="High performance Geforce GPU", category=category4)

session.add(part9)
session.commit()

part10 = Part(user_id=1, name="AMD Radeon Video Card",
              description="High performance Radeon GPU", category=category4)

session.add(part10)
session.commit()

print "added computer parts!"
