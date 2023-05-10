# import pytest
# from database import user_database
# import core.schemes
#
#
# def create_important_contacts_data():
#     contact = core.schemes.important_contacts_schemes.ImportantContactsPost
#     contact.contact_name = "Nome teste"
#     contact.contact_phone = "999999999"
#     contact.contact_email = "teste@email"
#     contact.contact_type = "Test"
#     return contact
#
#
# def test_important_contact_database():
#     data = create_important_contacts_data()
#     response = user_database.add_user(data)
#     assert response is True
