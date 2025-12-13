
<img width="910" height="814" alt="Logo Key" src="https://github.com/user-attachments/assets/05bfc80b-92b1-436a-ba38-efed263b3a66" />



Team Name: KeyGuardians

Team Members: Kevin Pasato, Jonathan Tyner, Matthew Chu, Kevin Wong, Alae Laaziri, Naser Shabbir

Project Topic: SecureDove

- Develop an instant messenger that provides secure messaging
with explicit confidentiality and integrity defenses


Functional Requirements:
1. User Account Management
2. Message Sending and Receiving
4. File Sharing
6. Message History and Backup
8. Session Management


Security Focused Development:
1. User Authentication and Key Management
3. Integrity via Message Authentication
10. Denial of Service (DoS) Attack Prevention



<img width="508" height="338" alt="Registration" src="https://github.com/user-attachments/assets/6ab25afd-22e6-4a46-aa00-d28e3f492b2a" />

● To use the website, you will need an account
● If you have an account, enter the email/username and password
● If you do not have an account, you can create one using the “click here” link.

<img width="514" height="372" alt="Message Page" src="https://github.com/user-attachments/assets/b716c5c9-c36d-4ba5-9f59-3b831e4263a0" />

Sidebar Includes:
● Account Management Page

● Message Page

● Logout Button
Account Management Page:-The user can view their username, email, and User ID. They can also change their email and passwords.
Message Page:-The user can add a friend by inputting a username and clicking send

<img width="412" height="319" alt="Message" src="https://github.com/user-attachments/assets/7dd31cf2-db0c-4f4a-8255-2ab37c7cdb2d" />

Select a friend from the friends list and type your message to send it.-Encrypted and decrypted messages which ensures that the each message received is sent from the server.

<img width="269" height="109" alt="Exposed Port" src="https://github.com/user-attachments/assets/7c93c91d-42b6-4e93-8a43-1ae7a42daa97" />


<img width="701" height="119" alt="CodeQI " src="https://github.com/user-attachments/assets/821b5167-0744-405a-b1ea-c2c9459edaf9" />

● The authentication cookies did not “Secure” attributes to “true”. Setting them to “true” would ensure that they were only passed through https connections.

● The database port “27017:27107” was left exposed. This allows unauthenticated remote access to sensitive data unless properly restricted.


<img width="270" height="249" alt="Port Removal" src="https://github.com/user-attachments/assets/d104a991-8eac-47fb-bf42-8b32fad459e8" />



<img width="771" height="117" alt="Included Secure Flag" src="https://github.com/user-attachments/assets/93d4498b-0926-495d-a8e1-d4a529771f4d" />

SECURITY RISKS - Fix It
After reviewing the security risk findings, we made two 
changes:
● We closed the open MongoDB port - We removed the port line in docker-compose.yml, so the database no longer exposes 27017 to potential attackers. This blocks unauthenticated connections.

● Secured cookie authentication - We updated the set_cookie call in app.py to include a secure flag. This ensures that cookies are transmitted only over https and reduces the risk of token leakage.


## Lessons Learned-
This project taught us several crucial lessons about security. First, security must be considered at every layer of the application stack. Our focus on secure message transmission didn't prevent us from making configuration errors at the deployment level.-We learned the value of independent security testing. Having another team review our application uncovered vulnerabilities we had overlooked, highlighting the importance of fresh perspectives in security auditing.




