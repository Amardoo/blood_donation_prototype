How to Set Up and Run
Create Project Folder:
Make a folder (e.g., blood_donation_prototype).
Save app.py in the root.
Create a templates subfolder and save the HTML files (index.html, register.html, view_donors.html, fmea.html, view_risks.html) inside it.
Install Dependencies:
Open a terminal in the project folder.
Run: pip install flask.
Run the Application:
In the terminal, run: python app.py.
Open a browser and go to http://localhost:5000.
Using the App:
Home Page: Links to register donors, view donors, calculate FMEA risks, or view risk logs.
Register Donor: Enter donor details (name, ID, age, hemoglobin, blood group, medical history). Data saves to blood_donation.db.
View Donors: Displays all registered donors in a table.
FMEA Calculator: Select a donation process step (e.g., "Donor Registration"), enter a failure mode (e.g., "Donor register without ID"), and input scores (1-10) for severity, occurrence, and detection. The app calculates RPN and stores it.
View Risks: Shows all logged FMEA risks with their RPNs.
For Your Thesis:
Include the code in an appendix (copy the app.py and HTML files).
Add screenshots of the app (e.g., registration form, risk log table).
Describe how it supports the paper’s findings: The system addresses high-RPN failure modes (e.g., donor ID issues, RPN=126; wrong medical history, RPN=150) by enforcing ID entry and storing medical history for validation.
Note: The database (blood_donation.db) is created automatically in the project folder when you run the app.
Why This Is Suitable
Simplicity: Minimal code (one Python file, five HTML templates). No complex frameworks or external servers.
Relevance: Directly supports the paper’s focus on donor registration, medical history, and FMEA risk management (e.g., tracks high-RPN issues like impersonation or phlebotomy errors).
Extensibility: Easy to add features (e.g., validation for hemoglobin <12.5 g/dL for females, per the paper) for your thesis.
Dependencies: Only Flask and SQLite, both lightweight and widely supported.
Time: Setup and testing take ~30 minutes. Coding from scratch takes ~1-2 hours if you’re familiar with Python.
Notes
Security: This is a prototype, not production-ready. For a real system, add user authentication and input sanitization (e.g., to prevent SQL injection).
Customization: To align further with the paper, add validation rules (e.g., reject donors with hemoglobin <13.0 g/dL for males) or alerts for RPN >60 (threshold from the paper).
GitHub Alternative: If you prefer not to code, you can still use a GitHub repo like sumitkumar1503/bloodbankmanagement, but it’s more complex and requires Django setup. The provided code is simpler for thesis purposes.


<img width="898" height="534" alt="1" src="https://github.com/user-attachments/assets/d954f254-9cca-42a5-bdf3-db8c9f572c95" />
<img width="1434" height="686" alt="6" src="https://github.com/user-attachments/assets/7988d289-df9b-4746-851a-53de95cd91b6" />
<img width="1458" height="622" alt="7" src="https://github.com/user-attachments/assets/2981aafb-1a4e-4905-ba26-afdc3ac0cc76" />
<img width="1460" height="663" alt="8" src="https://github.com/user-attachments/assets/7fb2b0ff-5bb3-4bfe-84f5-e86c4eee8282" />
<img width="1419" height="491" alt="9" src="https://github.com/user-attachments/assets/fe31042b-0230-4670-8459-07dd52435345" />








Documentation: In your thesis, explain that this is a prototype to demonstrate a digital solution for managing donor data and risks, supporting the paper’s call for a Risk Management Information System (RMIS).
If you need specific modifications (e.g., Arabic UI, additional FMEA fields, or a different stack like PHP), let me know, and I can adjust the code!


