# PASSWORD LOCKER
#### An application using which you can keep track of your usernames and passwords for various accounts, 25/01/2019.
#### By **ANUM ASIF**
## Description
This application is developed to allow a user to save it's credentials for various accounts. Using it you can add as many credentials as you like. You can search for a credential of a particular site, you can delete a credential or you can see all the credentials. It gives you an option to autogenerate password for a site or you can enter the password yourself.

## Specifications
### Application:
1. display an option to create an account
   - INPUT:"ca"
   - OUTPUT:An account created with inputted username and password 
2. User is logged into the application by entering username and password
   - INPUT:"li"
   - OUTPUT:"logins to the user account providing more options for navigation"
3. add a credential with user name, site name, account name and password
   - INPUT:"cc" 
   - OUTPUT:"User credential is created with the inputted required values" 
4. delete a credential of a user for a particular site
   - INPUT:"dl" 
   - OUTPUT:"User credential of the site name entered is deleted"
5. displays all credentials of a user
   - INPUT:"selected dc from the displayed codes of navigation"
   - OUTPUT:"All saved credentials of a user"
6. displays an error message if the username and password entered doesn't exist
   - INPUT:"li" 
   - OUTPUT:"This username doesnot exist"
7. displays a goodbye message and exit
   - INPUT:"ex
   - OUTPUT:"Don't forget to add a credential for a new site" 

## Setup/Installation Requirements
* python3.6
* pip
## Running the Application
   * To run the application, in your terminal:

	```
	$ chmod +x password_locker.py
  	$ ./password_locker.py
	```
## Testing the Application
   * To run the tests for the class file:

	```
	$ python3.6 user_credentials_test.py
	```	
### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 
## Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/AnumAsif/Password-Locker/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/AnumAsif/Password-Locker/issues/new). Please include sample queries and their corresponding results.
## Technologies Used
- This project was generated with [Python3.6](https://devdocs.io/python~3.6/) 
## Support and contact details
Please feel free to contact me if you have any suggestion for me to improve this website.
- Email: anum@cockar.com
### License
*MIT*
Copyright (c) 2018 **ANUM ASIF**

