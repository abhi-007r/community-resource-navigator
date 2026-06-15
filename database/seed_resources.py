from database.db import SessionLocal
from models.resource import Resource

db = SessionLocal()

resources = [
    Resource(
        name="St. Patrick Center",
        category="Housing",
        description="Provides housing assistance and homelessness prevention services.",
        city="St. Louis",
        state="MO",
        phone="314-802-0700",
        website="https://stpatrickcenter.org",
        eligibility="Individuals and families experiencing housing instability.",
        services="Housing placement, case management, employment support."
    ),
    Resource(
        name="Operation Food Search",
        category="Food",
        description="Provides food assistance through community partners.",
        city="St. Louis",
        state="MO",
        phone="314-726-5355",
        website="https://operationfoodsearch.org",
        eligibility="Residents experiencing food insecurity.",
        services="Food pantry support and meal programs."
    ),
    Resource(
        name="Legal Services of Eastern Missouri",
        category="Legal Aid",
        description="Provides free civil legal assistance.",
        city="St. Louis",
        state="MO",
        phone="314-534-4200",
        website="https://lsem.org",
        eligibility="Income-qualified individuals.",
        services="Housing, family law, public benefits, consumer protection."
    ),
    Resource(
        name="BJC Behavioral Health",
        category="Mental Health",
        description="Mental health and behavioral health services.",
        city="St. Louis",
        state="MO",
        phone="314-747-7490",
        website="https://bjcbehavioralhealth.org",
        eligibility="Varies by program.",
        services="Counseling, psychiatric care, crisis support."
    ),
    Resource(
        name="Urban League of Metropolitan St. Louis",
        category="Workforce Development",
        description="Employment and workforce development programs.",
        city="St. Louis",
        state="MO",
        phone="314-615-3600",
        website="https://ulstl.com",
        eligibility="Open to community members.",
        services="Job training, career coaching, placement assistance."
    )
]

for resource in resources:
    db.add(resource)

db.commit()

print("Resources seeded successfully.")