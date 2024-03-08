Description 

The Library Management System is a Python project aimed at optimizing library operations.
It facilitates tasks like adding, removing, and updating books and patrons, alongside functionalities for book check-in/out and report generation. Employing object-oriented programming,
it employs classes such as Book, Patron, and Transaction for structured data handling. Through file-based storage using JSON, data persistence is ensured, enhancing system reliability. 
The project offers a user-friendly command-line interface, empowering librarians with intuitive tools for efficient resource management and seamless patron interactions.
Overall, the system streamlines library processes, promoting organized and accessible library services.

Structure for the Program

### Code Structure:

•	1. Item (Base Class):
   - Attributes:
     - title
   - Methods:
     - display_details()

•	2. Book (Derived from Item):
   - Attributes:
     - author
     - ISBN
     - quantity
   - Methods:
     - display_details()

•	3. Patron (Derived from Item):
   - Attributes:
     - patron_id
     - contact_info
   - Methods:
     - display_details()

•	4. Action (Base Class):
   - Attributes:
     - item
     - patron
     - date

•	5. Transaction (Derived from Action):
   - Attributes:
     - checkout
     - due_date (if checkout is True)‘
     - return_date (upon check-in)’
   - Methods:
     - check_in()


•	6. Library:
   - Attributes:
     - books (list)
     - patrons (list)
     - transactions (list)
   - Methods:
     - add_item()
     - remove_item()
     - checkout_item()
     - checkin_item()
     - search_items()
     - generate_report()



•	7. Main Functionality:
   - load_data()
   - save_data()
   - main()
	    CLI for a user to control the library management system 

Guidance on how to use this program
1. Run the Program:
   - Ensure you have Python installed on your system.
   - Save the provided code in a Python file (e.g., `library_management.py`).
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python file.
   - Run the program by executing the command: `python library_management.py`.

2. Interacting with the Program:
   - Once the program is running, you'll see a menu displaying various options.
   - Use the numbers to select an option corresponding to the action you want to perform.
   - Follow the prompts to input necessary information such as book details, patron information, etc.

3. Available Functionalities:
   - Adding and removing books.
   - Adding and removing patrons.
   - Checking out books to patrons.
   - Checking in books that have been returned by patrons.
   - Searching for books or patrons by title or name.
   - Generating reports of books and patrons in the library.

4. Exiting the Program:
   - To exit the program, select the option to exit (usually option 9) from the menu.
   - Upon exiting, the program will save any changes made to the library's data to a file.

5. Additional Considerations:
   - Ensure to follow the prompts and provide valid input as requested by the program.
   - Pay attention to any error messages or feedback provided by the program.
   - You can modify the code or extend its functionalities according to your specific requirements.
 
