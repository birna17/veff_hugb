"""Dummy data for testing."""
from typing import Dict
from uuid import UUID
from ..models.user import User
from ..models.dog import Dog
from ..models.walker import Walker
from ..models.walk_request import WalkRequest
from ..models.dog_owner import DogOwner
from ..models.walker_review import WalkerReview
from ..models.login import Login
from datetime import datetime

data: Dict[str, dict] = {
    # Dummy data for dogs to make testing possible
    "Dogs": {
        "9123588c-1797-49b8-80a4-b47bd301dbe8": Dog(
            name="snati",
            override_id="9123588c-1797-49b8-80a4-b47bd301dbe8",
            breed="poodle",
            photo_url="example.com/mypic.png",
        ),
        "972f5d9a-88d4-4550-a5b4-d8e4d2509c06": Dog(
            name="Skuggi",
            override_id="972f5d9a-88d4-4550-a5b4-d8e4d2509c06",
            breed="French bulldog",
            photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:" \
            "ANd9GcSb3luSjvvTjKJY67E_rXyldiYM9oLmfGXv19chmU1jdOAqMU2a",
        ),
        "b5bfae80-305f-4807-a6aa-42be1ec946ab": Dog(
            name="Benni",
            override_id="b5bfae80-305f-4807-a6aa-42be1ec946ab",
            breed="Labrador",
            photo_url="https://cosmos-images2.imgix.net/file/spina/photo/" \
            "16924/181022-puppy-full.jpg?ixlib=rails-2.1.4&auto=" \
            "format&ch=Width%2CDPR&fit=max&w=835",
        ),
        "7c9d0269-5604-4d9c-bf34-595926083f83": Dog(
            name="Enzo",
            override_id="7c9d0269-5604-4d9c-bf34-595926083f83",
            breed="Pitbull",
            photo_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/" \
            "American_Pitbull_Terrier_-_Colby_Line.jpg",
        ),
        "24da0589-4e6b-4d7b-af53-9d328f0aecbf": Dog(
            name="Eros",
            override_id="24da0589-4e6b-4d7b-af53-9d328f0aecbf",
            breed="German shepherd",
            photo_url="https://www.zooplus.co.uk/magazine/CACHE_IMAGES/768/" \
            "content/uploads/2019/04/german-shepherd-dog.jpg",
        ),
        "b17317f6-c7bd-4223-b2cb-9f6f46ca428c": Dog(
            name="Stormur",
            override_id="b17317f6-c7bd-4223-b2cb-9f6f46ca428c",
            breed="Rottweiler",
            photo_url="https://vetstreet-brightspot.s3.amazonaws.com/a5/" \
            "16f550a7fb11e0a0d50050568d634f/file/Rottweiler-2-645mk062811.jpg",
        ),
        "b9745759-7310-4b81-81bd-c48a4f496ec7": Dog(
            name="Bangsi",
            override_id="b9745759-7310-4b81-81bd-c48a4f496ec7",
            breed="Pomeranian",
            photo_url="https://www.purina.com.au/-/media/Project/Purina/Main" \
            "/Breeds/Dog/Mobile/Dog_Pomeranian_Mobile.jpg?h=300&la=en&w=375&" \
            "hash=C057DC10E58E3C43347D2727117C66A0",
        ),
        "34e8156b-a8ae-4f95-8a50-bc3ffeecee2f": Dog(
            name="Erró",
            override_id="34e8156b-a8ae-4f95-8a50-bc3ffeecee2f",
            breed="Chihuahua",
            photo_url="https://www.pets4homes.co.uk/images/breeds/41/large/" \
            "4269acdc72f57976adef0bc65efb0cdc.jpeg",
        ),
        "55192895-3a07-4996-a5c9-4b05809f9cb0": Dog(
            name="Klaki",
            override_id="55192895-3a07-4996-a5c9-4b05809f9cb0",
            breed="Border collie",
            photo_url="https://mk0cesarswaykigy4yk3.kinstacdn.com/wp-" \
            "content/uploads/2017/08/Ten-things-you-didn%E2%80%99t-know-" \
            "about-Border-collies-1-1.jpg",
        ),
        "706112f1-a262-4613-9692-635f6254afa3": Dog(
            name="Lalli",
            override_id="706112f1-a262-4613-9692-635f6254afa3",
            breed="Doberman",
            photo_url="https://www.insidedogsworld.com/wp-content/uploads" \
            "/2017/08/doberman_hero_image-1.jpg",
        )
    },
    "Users": {
        # Dummy data for Users to make testing possible
        "4b0e4c08-f9c1-4870-9471-5905111db3db": User(
            username="kalli96",
            password="kallibesti",
            override_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            first_name="Karl",
            last_name="Jónsson",
            address="Kirkjugata 12",
            phone_number="7775105",
            email_address="kallierbestur@gmail.com",
        ),
        "3590bc0f-0cdb-47a9-8659-4a45ba4f9726": User(
            username="johnjohnson",
            password="woopwoop",
            override_id="3590bc0f-0cdb-47a9-8659-4a45ba4f9726",
            first_name="John",
            last_name="Johnson",
            address="Haukdælabraut 34",
            phone_number="8249996",
            email_address="johnson@gmail.com",
        ),
        "e1426e41-caa7-4ae6-a471-073617643ed0": User(
            username="siggi",
            password="siggsterinn",
            override_id="e1426e41-caa7-4ae6-a471-073617643ed0",
            first_name="Sigurður",
            last_name="Hafsteinsson",
            address="Garðsstaðir 56",
            phone_number="8875969",
            email_address="siggi22@gmail.com",
        ),
        "80ed37c4-16ae-4689-9287-19c257461c51": User(
            username="dagur",
            password="golf22",
            override_id="80ed37c4-16ae-4689-9287-19c257461c51",
            first_name="Dagur",
            last_name="Bjarnason",
            address="Akurgata 12",
            phone_number="5572215",
            email_address="dagur93@gmail.com",
        ),
        "a33e121e-5bfc-44ad-b84d-b6afaf7e42f0": User(
            username="thor",
            password="bangsi22",
            override_id="a33e121e-5bfc-44ad-b84d-b6afaf7e42f0",
            first_name="Þór",
            last_name="Þorláksson",
            address="Bakkastaðir 56",
            phone_number="6952341",
            email_address="thorthehammer@gmail.com",
        ),
        "8bcb0a84-ddfd-4a25-b660-4bcc83bc5d47": User(
            username="keli",
            password="kotturinn",
            override_id="8bcb0a84-ddfd-4a25-b660-4bcc83bc5d47",
            first_name="Hrafnkell",
            last_name="Sigurðsson",
            address="Döllugata 12",
            phone_number="9935105",
            email_address="kelikottur@gmail.com",
        ),
        "f200f395-9086-44c7-9bbc-0bcdf8820889": User(
            username="ronni",
            password="ggez69",
            override_id="f200f395-9086-44c7-9bbc-0bcdf8820889",
            first_name="Aron",
            last_name="Diego",
            address="Hafnargata 8",
            phone_number="7744440",
            email_address="aron98@gmail.com",
        ),
        "2819e6f0-810c-4677-b5d8-d6dc5c8879eb": User(
            username="biggi",
            password="bbking",
            override_id="2819e6f0-810c-4677-b5d8-d6dc5c8879eb",
            first_name="Birgir",
            last_name="Kristinsson",
            address="Ægissíða 96",
            phone_number="7724480",
            email_address="biggi44@gmail.com",
        ),
        "a41d5285-2494-4cbf-8167-3059c9dce1f0": User(
            username="jonstori",
            password="store99",
            override_id="a41d5285-2494-4cbf-8167-3059c9dce1f0",
            first_name="Jón",
            last_name="Stóri",
            address="vesturgata 58",
            phone_number="8221496",
            email_address="jonstori@gmail.com",
        ),
        "45b5c59a-35c4-4276-9168-7ad4e0f72018": User(
            username="binni",
            password="binni123",
            override_id="45b5c59a-35c4-4276-9168-7ad4e0f72018",
            first_name="BRynjar",
            last_name="Jóhannsson",
            address="Rauðalækur 36",
            phone_number="8825995",
            email_address="binni123@gmail.com",
        ),
    },
    "Walkers": {
        # Dummy data for Walkers to make testing possible
        "04852ade-5a71-4162-a837-c1d7166a05be": Walker(
            override_id="04852ade-5a71-4162-a837-c1d7166a05be",
            user_id="45b5c59a-35c4-4276-9168-7ad4e0f72018",
            is_available=True,
        ),
        "8a4ed207-59bd-401c-a32c-b3480c424ce2": Walker(
            override_id="8a4ed207-59bd-401c-a32c-b3480c424ce2",
            user_id="a41d5285-2494-4cbf-8167-3059c9dce1f0",
            is_available=True,
        ),
        "a65dfcb8-0e03-4d99-a209-ecdfb9295277": Walker(
            override_id="a65dfcb8-0e03-4d99-a209-ecdfb9295277",
            user_id="2819e6f0-810c-4677-b5d8-d6dc5c8879eb",
            is_available=False,
        ),
        "b76debee-16b3-4f9e-ba3c-68b1402901b2": Walker(
            override_id="b76debee-16b3-4f9e-ba3c-68b1402901b2",
            user_id="f200f395-9086-44c7-9bbc-0bcdf8820889",
            is_available=True,
        ),
        "afa19ea6-d848-4a3e-84ba-a9683978f9a2": Walker(
            override_id="afa19ea6-d848-4a3e-84ba-a9683978f9a2",
            user_id="8bcb0a84-ddfd-4a25-b660-4bcc83bc5d47",
            is_available=False,
        ),
        "0202d8cc-e4c9-4ddd-9e11-a15b2cce70f1": Walker(
            override_id="0202d8cc-e4c9-4ddd-9e11-a15b2cce70f1",
            user_id="a33e121e-5bfc-44ad-b84d-b6afaf7e42f0",
            is_available=False,
        ),
        "81b3ee4c-4450-461a-b506-ceaac06d2067": Walker(
            override_id="81b3ee4c-4450-461a-b506-ceaac06d2067",
            user_id="80ed37c4-16ae-4689-9287-19c257461c51",
            is_available=True,
        ),
        "97fc5df4-2fc3-4890-adc0-2c4589c51c66": Walker(
            override_id="97fc5df4-2fc3-4890-adc0-2c4589c51c66",
            user_id="e1426e41-caa7-4ae6-a471-073617643ed0",
            is_available=False,
        ),
        "f9399670-030d-425e-b68a-873e427567ea": Walker(
            override_id="f9399670-030d-425e-b68a-873e427567ea",
            user_id="3590bc0f-0cdb-47a9-8659-4a45ba4f9726",
            is_available=True,
        ),
        "f3352587-692f-4d2f-97d3-7169db581932": Walker(
            override_id="f3352587-692f-4d2f-97d3-7169db581932",
            user_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            is_available=False,
        ),
    },
    "DogOwners": {
        # Dummy data for DogOwners to make testing possible
        "706112f1-a262-4613-9692-635f6254afa3": DogOwner(
            owner_id="5ec1b89a-dfbc-4967-a562-86796406ecb0",
            dog_id="9123588c-1797-49b8-80a4-b47bd301dbe8"
        ),
        "7f84a206-3886-4644-8487-5291144863f7": DogOwner(
            owner_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            dog_id="7c9d0269-5604-4d9c-bf34-595926083f83"
        ),
        "b3a2242b-379f-4d3b-aa62-684cf7c98a57": DogOwner(
            owner_id="33626229-34f4-43d0-8668-26c4193d0d54",
            dog_id="24da0589-4e6b-4d7b-af53-9d328f0aecbf"
        ),
        "fa2faef8-4327-4a06-a967-d1e60c464132": DogOwner(
            owner_id="3ccce369-95eb-416b-be18-767de5d2d361",
            dog_id="b9745759-7310-4b81-81bd-c48a4f496ec7"
        ),
        "202d4d97-9820-4158-a899-f46986ea96ab": DogOwner(
            owner_id="e616f11c-8545-407e-9388-b86147664cdd",
            dog_id="34e8156b-a8ae-4f95-8a50-bc3ffeecee2f"
        ),
    },
    "WalkerReviews": {
        # Dummy data for WalkerReviews to make testing possible
        "4fe18eab-65df-4864-bd3f-3a1c940514fc": WalkerReview(
            override_id="4fe18eab-65df-4864-bd3f-3a1c940514fc",
            walker_id=1,
            rating=5,
        ),
        "22546a1d-1e86-4106-8923-c47780958203": WalkerReview(
            override_id="22546a1d-1e86-4106-8923-c47780958203",
            walker_id=1,
            rating=2,
        ),
        "1ed0b785-0f33-4804-b4dc-a49135fd7709": WalkerReview(
            override_id="1ed0b785-0f33-4804-b4dc-a49135fd7709",
            walker_id=2,
            rating=4,
        ),
        "cc6ab004-707a-4e3a-bea4-d9604bfda0b6": WalkerReview(
            override_id="cc6ab004-707a-4e3a-bea4-d9604bfda0b6",
            walker_id=3,
            rating=1,
        ),
        "75a16020-d662-4b49-8adc-c5e1163f159e": WalkerReview(
            override_id="75a16020-d662-4b49-8adc-c5e1163f159e",
            walker_id=4,
            rating=2,
        ),
        "83a6d6d5-a9ea-4d18-80df-da7c7f650571": WalkerReview(
            override_id="83a6d6d5-a9ea-4d18-80df-da7c7f650571",
            walker_id=5,
            rating=5,
        ),
        "987850f5-6f34-4f77-8e75-8a08432c6fba": WalkerReview(
            override_id="987850f5-6f34-4f77-8e75-8a08432c6fba",
            walker_id=5,
            rating=4,
        ),
        "d0a78fdc-4024-49e7-b8e0-7b6cb2681181": WalkerReview(
            override_id="d0a78fdc-4024-49e7-b8e0-7b6cb2681181",
            walker_id=6,
            rating=1,
        ),
        "3b5d6406-3673-403d-b1cf-e202e711219f": WalkerReview(
            override_id="3b5d6406-3673-403d-b1cf-e202e711219f",
            walker_id=6,
            rating=3,
        ),
        "f88dadd9-2f48-4882-9f8b-89f921b78ed5": WalkerReview(
            override_id="f88dadd9-2f48-4882-9f8b-89f921b78ed5",
            walker_id=7,
            rating=4,
        ),
        "db566249-502f-4e82-89b0-8ff6c0a47600": WalkerReview(
            override_id="db566249-502f-4e82-89b0-8ff6c0a47600",
            walker_id=8,
            rating=5,
        ),
    },
    "WalkRequests": {
        # Dummy data for WalkRequests to make testing possible
        "f5ec862e-a0e1-4b3d-b17f-26c4aea04fef": WalkRequest(
            owner_id="e616f11c-8545-407e-9388-b86147664cdd",
            walker_id="f3352587-692f-4d2f-97d3-7169db581932",
            dog_id="34e8156b-a8ae-4f95-8a50-bc3ffeecee2f",
            status="PENDING",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="f5ec862e-a0e1-4b3d-b17f-26c4aea04fef"
        ),
        "e4c7ee1c-7354-496d-af77-3f755dfa727c": WalkRequest(
            owner_id="3ccce369-95eb-416b-be18-767de5d2d361",
            walker_id="f9399670-030d-425e-b68a-873e427567ea",
            dog_id="b9745759-7310-4b81-81bd-c48a4f496ec7",
            status="ONGOING",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="e4c7ee1c-7354-496d-af77-3f755dfa727c"
        ),
        "158e17b8-283b-4f28-a997-feca441b879c": WalkRequest(
            owner_id="33626229-34f4-43d0-8668-26c4193d0d54",
            walker_id="97fc5df4-2fc3-4890-adc0-2c4589c51c66",
            dog_id="b17317f6-c7bd-4223-b2cb-9f6f46ca428c",
            status="DONE",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="158e17b8-283b-4f28-a997-feca441b879c"
        ),
        "b718a73e-2b26-4cb3-b02d-682973026f67": WalkRequest(
            owner_id="3590bc0f-0cdb-47a9-8659-4a45ba4f9726",
            walker_id="81b3ee4c-4450-461a-b506-ceaac06d2067",
            dog_id="7c9d0269-5604-4d9c-bf34-595926083f83",
            status="ONGOING",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="b718a73e-2b26-4cb3-b02d-682973026f67"
        ),
        "2180857c-d217-4de4-b9f8-4009bb905536": WalkRequest(
            owner_id="33626229-34f4-43d0-8668-26c4193d0d54",
            walker_id="04852ade-5a71-4162-a837-c1d7166a05be",
            dog_id="24da0589-4e6b-4d7b-af53-9d328f0aecbf",
            status="DONE",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="2180857c-d217-4de4-b9f8-4009bb905536"
        ),
        "b7a433e6-1d02-4d4e-8f8e-136102c6e917": WalkRequest(
            owner_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            walker_id="a65dfcb8-0e03-4d99-a209-ecdfb9295277",
            dog_id="7c9d0269-5604-4d9c-bf34-595926083f83",
            status="PENDING",
            time_start=datetime.now(),
            time_end=datetime.now(),
            override_id="b7a433e6-1d02-4d4e-8f8e-136102c6e917"
        ),
    },
    "Notifications": {},
    "Logins": {
        "6a206e39-561f-44fc-a233-b8f5edf3d356": Login(
            user_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            log_token="6a206e39-561f-44fc-a233-b8f5edf3d356",
            log_date=datetime(2019, 1, 1),
            log_expiry_date=datetime(2020, 1, 1),
            override_id="6a206e39-561f-44fc-a233-b8f5edf3d356"
        ),
        "3bcd8888-2a4e-4521-bba1-21285976e83c": Login(
            user_id="4b0e4c08-f9c1-4870-9471-5905111db3db",
            log_token="3bcd8888-2a4e-4521-bba1-21285976e83c",
            log_date=datetime(2019, 1, 1),
            log_expiry_date=datetime(2019, 9, 1),
            override_id="3bcd8888-2a4e-4521-bba1-21285976e83c"
        )
    },
}

# Covert key strings to UUID
for repo_key in dict(data).keys():
    for key, value in dict(data[repo_key]).items():
        data[repo_key][UUID(str(key))] = value

for repo_key in dict(data).keys():
    for key, value in dict(data[repo_key]).items():
        if not isinstance(key, UUID):
            del data[repo_key][key]
