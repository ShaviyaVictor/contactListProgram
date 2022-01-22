#!/usr/bin/env python3.8
import email
from contact import Contact


# creating the functions that implement our app behaviours

def createContact(firstName, lastName, phone, email) :
  """
  Function to create a new contact
  """

  newContact = Contact(firstName, lastName, phone, email) 
  return newContact




def save_contact(contact) :
  """
  Function to save contact
  """

  contact.save_contact()




def deleteContact(contact) :
  """
  Function to delete contact
  """

  contact.deleteContact()





def searchContact(number) :
  """
  Function that finds a contact by number and returns the contact
  """

  return Contact.searchByNum(number)





def checkContactExist(number) :
  """
  Function that checks ifa contact exists with that number and returns a Boolean
  """

  return Contact.contactExists(number)





def displayContact() :
  """"
  Function that returns all the saved contacts
  """

  return Contact.displayContacts()





#---------->>>> Copy Function, it has an Attributerror in class
# def coppyMail() :
#   """
#   Function that copies to clipboard
#   """

#   return Contact.copyMail()






def main() :
  print("Hello Welcome to your contact list. What is your name?")
  userName = input()

  print(f"Hello {userName}. What would you like to do?")

  print('\n')

  while True :
    print("Use these short codes: cc - to create a new contact; dc - to display the contacts; fc - to find a contact; ex - to exit the contact list")

    shortCode = input().lower()

    if shortCode == 'cc' :

      print('New Contact')
      print('-' * 10)

      print('First Name:')
      fName = input()

      print('Last Name:')
      lName = input()

      print('Phone:')
      phone = input()

      print('Email Address:')
      emailAdd = input()


      # Create and save the new contact
      save_contact(createContact(fName, lName, phone, emailAdd))

      print('\n')

      print(f"New Contact: {fName} {lName} has been created.")

      print('\n')



    elif shortCode == 'dc' :

      if displayContact() :

        print('Here is a list of all your contacts...')
        
        print('\n')

        for contact in displayContact() :
          print(f"{contact.firstName} {contact.lastName} {contact.phone} {contact.email}")
        
        print("\n")

      else :

        print("\n")
        print("You dont seem to have any contacts saved yet")
        print("\n")



    elif shortCode == 'fc' :

      print("Enter the number you want to search for:")

      findNumber = input()

      if checkContactExist(findNumber) :

        search4Contact = searchContact(findNumber)
        
        print(f'{search4Contact.firstName} {search4Contact.lastName}')

        print('-' * 20)

        print(f'Phone Number: {search4Contact.phone}')

        print(f'Email address: {search4Contact.email}')

        print('-' * 30)
        
      else :

        print('\n')

        print('Oops!!! That contact does not exist.\nSave a contact with us and save yourself the memory trouble.')

        print('\n')



    elif shortCode == 'ex' :

      print('\n.')

      print('Bye...')

      print('\n.')
          
      break

    else :
      
      print('\n.')
      
      print('I for sure didn\'t get that. Please use the short codes provided...\nThank You!')

      print('\n.')



if __name__ == '__main__':
  
  main()
  """
  to make the main function to run only if it was run from this module.
  """
    

      







    