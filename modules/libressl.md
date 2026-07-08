---
layout: default
title: LibreSSL
---

<!-- ai-generation-failed -->

<h1>LibreSSL</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/LibreSSL/LibreSSL.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

vides a secure, lightweight implementation of the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols. Originally a fork of OpenSSL by the OpenBSD project, it is used by the engine as a robust security backend for encrypted network communication.

This module is primarily utilized by the SSL and WebSockets modules on platforms where a modern, audited, and “cleaned-up” version of the SSL library is preferred over the system default. It facilitates the elimination of security vulnerabilities associated with legacy codebases while ensuring that game clients can communicate safely with HTTPS web services and dedicated game servers.

Practical Usage Tips and Best Practices
1. Rely on the SSL Module Wrapper

For most gameplay tasks, do not interface with the LibreSSL module directly. Instead, use the engine’s high-level SSL module. This abstraction facilitates the elimination of platform-specific security logic, allowing the engine to automatically swap between LibreSSL and other backends (like OpenSSL or Apple’s Security framework) as needed.

2. Wrap Headers with Third-Party Macros

If you require direct access to LibreSSL functions (e.g., specific cryptographic primitives), always wrap your #include statements with the engine’s third-party macros. This practice leads to the elimination of naming conflicts and compiler warnings that often arise between C-style libraries and the Unreal reflection system:

C++
	THIRD_PARTY_INCLUDES_START

	#include "openssl/ssl.h"

	THIRD_PARTY_INCLUDES_END
Copy code
3. Update Root Certificates Regularly

LibreSSL requires a certificate bundle (usually cacert.pem) to verify server identities. If your game fails to connect to a backend after a server migration, verifying that your project’s certificates are up to date is a best practice for the elimination of “SSL Handshake Failed” errors during development.

4. Audit for Cross-Platform Differences

While LibreSSL is used on several platforms, some operating systems (like iOS or Windows) may default to different libraries. Testing your secure connections on all target platforms leads to the elimination of “mystery” bugs where a connection works in the editor but fails on a physical mobile device due to differing cipher suite support.

5. Monitor for Thread Safety

Cryptographic operations are computationally intensive. When using LibreSSL for custom encryption, always perform these tasks on a background thread. This assists in the elimination of hitches on the Game Thread, ensuring that the encryption of large data packets does not interfere with the game’s frame rate.

6. Utilize “Elimination” of Memory Leaks via UPROPERTY

If you are managing custom LibreSSL objects (like SSL_CTX or X509 certificates) in a C++ wrapper, ensure you handle their lifecycle carefully. While they aren’t UObjects, managing the pointers within a class that tracks their lifetime facilitates the elimination of memory leaks in the networking layer.

7. Debug with “LogSSL” Verbosity

To troubleshoot secure connection issues, enable verbose logging for the engine’s SSL category using the console command log LogSSL Verbose. This allows you to see the specific error codes returned by LibreSSL, aiding in the elimination of confusion when a certificate is rejected or a connection is dropped by the remote host.

8. Verify Build.cs Dependencies

If your module requires the LibreSSL headers or libraries, you must add "LibreSSL" to your Build.cs file under the appropriate platform checks. Correctly managing these dependencies is essential for the elimination of linker errors when building for platforms where the engine expects a specific security backend.