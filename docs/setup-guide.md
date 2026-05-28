**Setup Guide**

Prerequisites 
Python 3.x 
pip 
Flask

Install Python Download and install Python from: https://python.org (For a wndoes system you can directly nstall python from Microsoft Store)
<img width="1201" height="948" alt="image" src="https://github.com/user-attachments/assets/342806ae-b602-4c90-b41a-4691cd077836" />
<img width="600" height="473" alt="00" src="https://github.com/user-attachments/assets/5058c01f-fcb2-4a2a-9f08-94360cd846af" />
<img width="601" height="473" alt="000" src="https://github.com/user-attachments/assets/8f695acf-d285-4b7c-a6eb-5c0785aa4a3a" />

Once Python is installed verify the installation by executng below command in cmd.

python

<img width="675" height="218" alt="01" src="https://github.com/user-attachments/assets/01c39718-06f5-428c-be5d-1ce119b7fcae" />
<img width="675" height="219" alt="02" src="https://github.com/user-attachments/assets/4b4eb478-e9af-4f70-8da5-686f4fa5e25a" />


Now pen cmd/ terminal and run the below command to install Flask 
pip install flask
<img width="675" height="199" alt="03" src="https://github.com/user-attachments/assets/1e368b5a-dad3-41c2-8eb6-bb1b73bf0e6a" />
<img width="676" height="360" alt="04" src="https://github.com/user-attachments/assets/c5aa3b00-1664-4e1a-aef1-6d3afd2295dc" />

Download the upload_server.py script. 
<img width="960" height="376" alt="001" src="https://github.com/user-attachments/assets/b6fdaf74-9bb1-4284-a54d-f9dc7f7ff060" />

After downloading, create a new directory on your system and move the script into the same folder.
<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/459bfbcc-60fe-4221-b646-6ca85bd9a935" />
<img width="815" height="511" alt="004" src="https://github.com/user-attachments/assets/0bace1ba-a3c6-409b-bdfb-61a45dddccee" />

Within the same directory, create a folder named uploads.
<img width="772" height="510" alt="010" src="https://github.com/user-attachments/assets/c6a0e4a7-04db-49f4-9854-8b28968644aa" />

**Note:** Ensure the folder is exactly named as uploads, as the script is configured to store and reflect all uploaded content in this directory.

Navigate to the folder in the system where the file named "upload_server.py" is downloaded and run the below command: 
python upload_server.py

<img width="854" height="372" alt="100" src="https://github.com/user-attachments/assets/f4694613-515f-4763-b8fd-d345a8a71ca1" />

Once the command is executed, it will provide a local IP-based URL. 
<img width="675" height="289" alt="07" src="https://github.com/user-attachments/assets/94010b6b-6da4-4170-a25c-566f09818e0c" />

Connect the system on which DLP and proxy restrictions are being tested (target system) to the same network or Wi-Fi as the system running the script.
Next, open the URL displayed as output when the script was executed in any browser on the target system.
Once accessed, the webpage with the file upload functionality should be visible.
<img width="960" height="303" alt="08" src="https://github.com/user-attachments/assets/7dc6d024-3d5e-4d4e-8026-0ba4417b20c5" />
<img width="960" height="365" alt="09" src="https://github.com/user-attachments/assets/6d11eab0-107f-4efe-a82c-502dd2b5ad26" />

Now you can click on choose file opton in web page and select the file that needs to be uploaded and click on open.
<img width="960" height="474" alt="120" src="https://github.com/user-attachments/assets/3e6aa04a-26f2-4889-a718-b8c8e6b417d0" />

Once the file is selected, click on Upload button n web page.
<img width="960" height="238" alt="121" src="https://github.com/user-attachments/assets/d43df1fb-1d82-4fa2-b2f2-4cff05e6493a" />

You can see that the web application responds with a message, File uploaded successfully.
<img width="960" height="333" alt="122" src="https://github.com/user-attachments/assets/1bb266f3-5366-40e4-a421-abdcaa355a5b" />

Now, on the system running the upload_server.py script, navigate to the directory where the script is stored. Then, open the folder named uploads that was created prior to executing the script.
<img width="592" height="340" alt="125" src="https://github.com/user-attachments/assets/cafedeea-0e7c-418c-acba-ff8761e9dd02" />

You can observe that the file uploaded from the target system is reflected within the uploads folder on the testing system, making it evident that the data has been sucessfully exfiltrated from the restricted system.
<img width="591" height="327" alt="126" src="https://github.com/user-attachments/assets/4e0fb01e-c490-480b-91f4-555f9c0b5fbf" />

Additionally, the HTTP interactions, including the GET and POST requests initiated by the target system, are logged as part of the testing process, providing visibility into the communication flow during the controlled validation activity.
<img width="855" height="388" alt="124" src="https://github.com/user-attachments/assets/4ac1929a-6f36-4c36-bb98-8049d061c0cf" />



