---
layout: default
title: RSA
---

<!-- ai-generation-failed -->

<h1>RSA</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/RSA/RSA.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, OpenSSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ivest–Shamir–Adleman) public-key cryptosystem. It is a low-level runtime module used for asymmetric encryption, decryption, digital signatures, and signature verification.

While historically used for network packet encryption, in modern UE5, RSA is deprecated for networking in favor of more efficient authenticated encryption (like AES-GCM). However, it remains the standard for Asset Integrity and Security, specifically for signing and verifying .pak files and validating secure handshakes between services.

Practical Usage Tips and Best Practices
Include the Module and Header
To use the RSA API in C++, you must add "RSA" to your PublicDependencyModuleNames in your .Build.cs file. The primary interface is the FRSA static class, accessed via #include "RSA.h".
Use for Digital Signatures, Not Data Encryption
RSA is computationally expensive and has strict limits on data size. Do not use it to encrypt large game data. Instead, use it to Sign data (creating a hash and encrypting it with a private key) to ensure it hasn’t been tampered with. This is how Unreal verifies that a .pak file was created by your build machine.
Implement Hybrid Encryption
If you need to send a secure message to a server, do not encrypt the whole message with RSA. Instead, generate a random AES key, encrypt that key with the server’s RSA Public Key, and then encrypt the message body with the AES Key. This combines RSA’s security with AES’s speed.
Protect Your Private Keys
In an RSA workflow, the Public Key can be included in your shipping client, but the Private Key must never be distributed. If an attacker gains the private key, they can forge digital signatures for your game assets or decrypt secure communications.
Configure Pak File Signing
Use the Project Settings > Crypto panel to generate or assign RSA keys for your project. This module handles the runtime verification of these keys. Enabling “Sign Pak Files” helps you eliminate the risk of users injecting modified assets or cheat-modded blueprints into your packaged game.
Observe Data Size Constraints
The maximum amount of data you can encrypt with RSA is determined by the key size minus padding (e.g., a 2048-bit key allows roughly 245 bytes of data). Use FRSA::GetMaxDataSize(KeyHandle) to check your limits and eliminate errors caused by trying to encrypt too much data at once.
Transition Networking to AES-GCM
If your project still uses legacy RSA-based encryption handlers for networking, you should migrate to the AESGCM handler. The engine’s networking team recommends this as the most tested and secure option for modern multiplayer, helping you eliminate potential vulnerabilities or performance bottlenecks.
Manage Key Lifetimes with Handle Types
When creating keys via FRSA::CreateKey, you receive an FRSAKeyHandle. Always ensure you call FRSA::DestroyKey(Handle) when you are finished (the “elimination” of the security session) to avoid memory leaks in the underlying cryptographic provider.