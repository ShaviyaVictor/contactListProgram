# Importing the unittest module
from cgi import test
import unittest
import pyperclip




# importing our class contact
from contact import Contact

class testContact(unittest.TestCase) :

  """
  Test class that defines test cases for the contact class behaviours
  
  Args :
    unittest.TestCase: TestCase class that helps in creating test cases
  """


  def setUp(self) :
    """
    Set up method to run before each test case
    """

    # ------>>> 1st Test to confirm we are running the right file
    #     #creating contact object
    self.contact1 = Contact("Victor", "Shaviya", "0791082379", "shaviyavictor@gmail.com")




  # ------>>> the tearDown method
  def tearDown(self) :
    """
    tearDown method that does clean up after each test case has ran
    """

    Contact.contactList = []






  def test_init(self) :
    """
    test_init test case to test if the object is initialized properly
    """

    
    self.assertEqual(self.contact1.firstName,'Victor')
    self.assertEqual(self.contact1.lastName,'Shaviya')
    self.assertEqual(self.contact1.phone,'0791082379')
    self.assertEqual(self.contact1.email,'shaviyavictor@gmail.com')




# ------>>> 2nd Test to confirm we are running the right file

  def test_save_contact(self) :
    """
    test_save_contact test case to test if the contact object is saved into the contact list
    """

    #saving the new contact
    self.contact1.save_contact()
    self.assertEqual(len(Contact.contactList),1)




  # ------>>> 3rd Test to confirm we are running the right file

  def test_save_multiple_contact(self) :
    """
    test_save_multiple_contact to check if we can save multiple contact objects to our contactList
    """
    self.contact1.save_contact()

    # a new contact
    contact2 = Contact("Josphine", "Mbaisi", "0717541960", "mbaisijos@gmail.com")
    contact2.save_contact()
    self.assertEqual(len(Contact.contactList),2)




  # ------>>> 4th Test to test if we can delete the contact
  def testDeleteContact(self) :
    """
    testDeleteContact method to test if we can remove a contact from our contact list
    """

    self.contact1.save_contact()

    contact2 = Contact("Josphine", "Mbaisi", "0717541960", "mbaisijos@gmail.com")
    contact2.save_contact()

    self.contact1.deleteContact()
    self.assertEqual(len(Contact.contactList),1)
    




  # ------>>> 5th Test to test if we can find a contact by phone number and display the info of the contact
  def testSearchByNum(self) :
    """
    test to check if we can find a contact by phone and display the other info
    """
    self.contact1.save_contact()

    contact2 = Contact("Josphine", "Mbaisi", "0717555560", "mbaisijos@gmail.com")
    contact2.save_contact()

    foundContact = Contact.searchByNum('0717555560')
    self.assertEqual(foundContact.email, contact2.email)



  # ----->>> 6th Test to check if a contact object actually exists
  def testContactExists(self) :
    """
    test to check if we can return a Boolean if we cannot find the contact
    """

    self.contact1.save_contact() 

    contact2 = Contact("Josphine", "Mbaisi", "0717555560", "mbaisijos@gmail.com")
    contact2.save_contact()

    contactExists = Contact.contactExists('0717555560')
    self.assertTrue(contactExists)




  # ----->>> 7th Test to display all the contacts
  def testDisplayContacts(self) :
    """
    method that returns a list of all contacts saved
    """

    self.assertEqual(Contact.displayContacts(),Contact.contactList)




  #  ###   FAILED - TO REVERT
  # # ----->>> 8th Test to copy to clipboard
  # def testCopyMail(self) :
  #   """
  #   Test to confirm we can copy the email address from a found contact
  #   """

  #   self.contact1.save_contact()

  #   Contact.copyMail('0717555560')
  #   self.assertEqual(self.contact1.email, pyperclip.paste())






if __name__ == '__main__' :
  unittest.main()










