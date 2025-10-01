# Secure Messaging App — Project Planning

## 1. Project Overview
This repository contains the source code and documentation for a **Windows-only encrypted messaging app**.  

The app is designed to be lightweight, private, and simple:
- One-to-one encrypted messaging only  
- No accounts, no login, no registration  
- No databases or servers storing messages  
- No backups or recovery mechanisms  
- Single device per user (no sync across devices)  
- Download, install, exchange keys, and start messaging  

---

## 2. Goals
- Provide **end-to-end encrypted messaging** between two Windows devices.  
- Ensure all cryptographic keys are **generated and stored locally**.  
- Minimize user friction: **no setup, no accounts, no cloud**.  
- Ensure that even the app developers cannot access user messages.  

---

## 3. Scope
**In Scope**
- Local key generation (X25519 for encryption, Ed25519 for signatures)  
- Encrypted messaging (AES-GCM or ChaCha20-Poly1305)  
- Peer-to-peer messaging over TCP/UDP sockets  
- Optional relay server for NAT traversal (forwards ciphertext only)  
- Windows desktop client (C#/WPF, WinUI, or Electron)  

**Out of Scope**
- Group messaging  
- Multi-device sync  
- Accounts or authentication services  
- Backups, recovery, or key escrow  
- Analytics or telemetry  

---

## 4. Deliverables
- **Windows executable (.exe installer)** for end users  
- **Crypto module**: local key generation, encryption, decryption  
- **Networking module**: peer-to-peer communication  
- **UI module**: chat window, key exchange screen  
- **Optional local encrypted storage** for chat history  

---

## 5. Security Model
- Each client generates a **key pair** on first launch.  
- Users exchange public keys (via QR code, copy-paste, or file).  
- Session keys derived with **ECDH (X25519)**.  
- All messages encrypted with **AES-GCM** or **ChaCha20-Poly1305**.  
- Decryption only occurs on the recipient’s device.  

---

## 6. Architecture Overview
**Client (Windows app)**
- Crypto module: keygen, session management, encryption/decryption  
- Networking module: direct socket communication, relay fallback  
- UI module: chat interface, key exchange, status indicators  
- Local storage (optional): encrypted file or SQLite DB  

**Relay Server (optional)**
- Forwards encrypted payloads if direct peer-to-peer fails  
- Does not log or store plaintext messages  

---

## 7. Risks & Mitigation
- **NAT traversal problems** → Provide optional relay server fallback  
- **Device loss = data loss** → Accepted (no backups by design)  
- **Compromised device** → Cannot be prevented by app; user is responsible for device security  
- **User key exchange errors** → Mitigated with QR code or checksum verification  

---

## 8. Timeline (High-Level)
- **Week 1–2:** Implement crypto module (keygen, encryption, decryption)  
- **Week 3–4:** Implement networking (peer-to-peer + relay fallback)  
- **Week 5:** Develop Windows UI (chat + key exchange)  
- **Week 6:** Add optional encrypted local storage  
- **Week 7:** Security testing and bug fixes  
- **Week 8:** Build installer and release MVP  

---

## 9. Success Criteria
- Messages remain encrypted end-to-end.  
- No plaintext leaves the device.  
- App runs without requiring accounts, logins, or external services.  
- Minimal setup: install → exchange keys → chat.  

---

## 10. Repository Structure (planned) 
