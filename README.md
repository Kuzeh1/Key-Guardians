
<img width="910" height="814" alt="Logo Key" src="https://github.com/user-attachments/assets/05bfc80b-92b1-436a-ba38-efed263b3a66" />



KeyGuardians – Secure Messaging Prototype 

Team Members: Kevin Pasato, Jonathan Tyner, Matthew Chu, Kevin Wong, Alae Laaziri, Naser Shabbir

Project Name: SecureDove
Project Type: Internal security-focused prototype

Project Overview

I contributed to the development of SecureDove, an internal secure messaging prototype. The project was designed to test and validate authentication, encryption, and abuse-prevention strategies in a controlled environment before applying them to production systems. My role focused on implementing and hardening security controls, performing security testing, and documenting risks and mitigations.

Functional Features

1. User Account Management: Registration, login, password management, and session handling.

2. Messaging: Secure sending and receiving of messages with encryption and integrity verification.

3. File Sharing: Secure file storage with AES-256 encryption.

4. Message History and Backup: Encrypted storage and retrieval of message history.


Security-Focused Implementation

1. User Authentication and Key Management: Secure login, password hashing with bcrypt, and key handling for message encryption.

2. Message Integrity: HMAC-SHA256 ensures messages cannot be tampered with in transit.

3. Denial of Service (DoS) Prevention: Rate limiting and account lockout mechanisms to mitigate brute-force attacks.

4. Secure Deployment: Closed exposed MongoDB ports, enforced HTTPS-only secure cookies.



<img width="508" height="338" alt="Registration" src="https://github.com/user-attachments/assets/6ab25afd-22e6-4a46-aa00-d28e3f492b2a" />

● To use the website, you will need an account

● If you have an account, enter the email/username and password

● If you do not have an account, you can create one using the “click here” link.

<img width="514" height="372" alt="Message Page" src="https://github.com/user-attachments/assets/b716c5c9-c36d-4ba5-9f59-3b831e4263a0" />

Sidebar Includes:

● Account Management Page

● Message Page

● Logout Button
Account Management Page:
The user can view their username, email, and User ID. They can also change their email and passwords.
Message Page:-The user can add a friend by inputting a username and clicking send

<img width="412" height="319" alt="Message" src="https://github.com/user-attachments/assets/7dd31cf2-db0c-4f4a-8255-2ab37c7cdb2d" />

Select a friend from the friends list and type your message to send it.-Encrypted and decrypted messages which ensures that the each message received is sent from the server.

<img width="269" height="109" alt="Exposed Port" src="https://github.com/user-attachments/assets/7c93c91d-42b6-4e93-8a43-1ae7a42daa97" />


<img width="701" height="119" alt="CodeQI " src="https://github.com/user-attachments/assets/821b5167-0744-405a-b1ea-c2c9459edaf9" />

● The authentication cookies did not “Secure” attributes to “true”. Setting them to “true” would ensure that they were only passed through https connections.

● The database port “27017:27107” was left exposed. This allows unauthenticated remote access to sensitive data unless properly restricted.


<img width="270" height="249" alt="Port Removal" src="https://github.com/user-attachments/assets/d104a991-8eac-47fb-bf42-8b32fad459e8" />



<img width="771" height="117" alt="Included Secure Flag" src="https://github.com/user-attachments/assets/93d4498b-0926-495d-a8e1-d4a529771f4d" />


Technical Highlights

Built with Python, Flask, MongoDB, and Docker.

Implemented encrypted messaging, secure authentication, and abuse prevention mechanisms.

Conducted security testing and hardening, fixing misconfigurations like exposed database ports and insecure cookie flags.

Collaborated with team members to review code, test vulnerabilities, and refine security patterns.


Security Outcomes

1. Closed exposed database ports to block unauthenticated access.

2. Enabled secure cookie flags to prevent token leakage over insecure connections.

3. Implemented rate-limiting to prevent brute-force login attempts.

4. Verified message encryption and integrity across sessions.

## Impact-
This project gave the team actionable insights into secure authentication, message integrity, and deployment best practices. The prototype provided a safe environment to test security strategies before applying them to production applications, ensuring that lessons learned could be incorporated into future company systems.



