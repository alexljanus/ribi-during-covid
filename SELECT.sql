USE RIBI;

SELECT Country, Gender, 2020 - BirthYear AS Age
FROM IndvLvl;

SELECT ClubID, IndvID, RelTypeR, ContactInPerson, ContactPhone, ContactEmail, ContactText, ContactVideo, ContactSocMedia, ChangeContact, ChangeInPerson
FROM RelLvl_2;

SELECT Latitude, Longitude
FROM IndvLvl;