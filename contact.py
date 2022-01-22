import pyperclip



from xmlrpc.client import Boolean


class Contact :

  """
  Class that generates new instances of contacts
  """

  

  # empty contact list
  contactList = []

  def __init__(self, firstName, lastName, phone, email):

    """
    __init__ method that helps us define properties for our objects. self is a variable that represents the instance of the object itself
    
    Args :
      firstName : New contact first name.
      lastName : New contact last name.
      phone : New contact phone number.
      email : New contact email address.
    """

    self.firstName = firstName
    self.lastName = lastName
    self.phone = phone
    self.email = email

  # method to append the new objects and save them || comes at the top
  def save_contact(self) :
    """
    save_contact method saves contact objects into contactList[]
    """

    Contact.contactList.append(self)



  def deleteContact(self) :
    """
    deleteContact method that deletes a saved contact from the contactList
    """

    Contact.contactList.remove(self)



  # search functionality
  @classmethod
  def searchByNum(cls, number) :
    """
    method that takes in a number and returns a contact that matches that number
    
    Args :
      number : Phone number to search for 
    Returns :
      Contact of person that matches the number
    """

    for contact in cls.contactList :
      if contact.phone == number :
        
        return contact




  # exist-check functionality
  @classmethod
  def contactExists(cls, number) :
    """
    Method that checks if a contact exists from the contact list.
    Args :
      number : phone number to search if it exists
    Returns :
      Boolean : True or false depending on whether the contact exists
    """

    for contact in cls.contactList :
      if contact.phone == number :
        return True

    return False

    

  # display functionality
  @classmethod
  def displayContacts(cls) :
    """
    method that returns the contactList
    """

    return cls.contactList



# ###   FAILED - REVERT AND SOLVE THIS! --- getting AttributeError
#   # ----->>> copy to clipboard functionality
#   @classmethod
#   def copyMail(cls, number) :
#     contactExists = Contact.searchByNum(number)
#     pyperclip.copy(contactExists.email)





  # method to give us the full name of our instances
  def fullName(self):
    return '{} {}'.format(self.firstName,self.lastName)


contact1 = Contact("Victor", "Shaviya", "0791082379", "shaviyavictor@gmail.com")
contact2 = Contact("Josphine", "Mbaisi", "0717541960", "mbaisijos@gmail.com")

# print(contact1.firstName)

# print('{} {}'.format(contact1.firstName, contact1.lastName))

# print(contact1.fullName())
# # or
# print(Contact.fullName(contact2))
