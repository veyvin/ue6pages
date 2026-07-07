---
layout: default
title: S3Client
---

<!-- ai-generation-failed -->

<h1>S3Client</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/S3Client/S3Client.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Json, SSL, Sockets, XmlParser, libcurl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ween Unreal Engine and Amazon S3 (Simple Storage Service), primarily acting as an Unreal-idiomatic wrapper for the AWS C++ SDK.

Description and Purpose

This module handles low-level communication with S3 buckets, managing authentication, request signing, and asynchronous data transfer. Its most critical role in the Unreal ecosystem is supporting the Cloud Derived Data Cache (DDC), which allows distributed teams to share compiled shaders and assets via the cloud. Beyond DDC, it provides the C++ infrastructure needed for any custom cloud-based storage task, such as uploading crash reports or downloading game patches. Its primary purpose is to eliminate the complexity of manual SDK integration by providing a thread-safe, non-blocking way to interface with S3 within the engine’s framework.

Practical Usage Tips and Best Practices
Implement via IS3Client for Custom Tools
If you are building a custom patcher or cloud-save system, add "S3Client" to your PrivateDependencyModuleNames in your .Build.cs. Using the provided IS3Client interface is a best practice to eliminate direct dependencies on the raw AWS SDK, keeping your project’s module architecture clean.
Centralize Credentials in DefaultEngine.ini
Rather than hardcoding keys, use the [StorageServers] configuration section. This allows you to eliminate the risk of leaking sensitive AccessKey and SecretKey data in your source code, as these values can be safely overridden by local environment variables on build machines.
Always Use Asynchronous Requests
S3 operations are subject to network latency. The module is designed for non-blocking execution. Always bind a delegate to the completion event of your S3 requests to eliminate Game Thread stalls that would cause the editor or game client to freeze during a transfer.
Leverage for Geo-Distributed DDC
For teams working across different continents, configure the S3 client to point to a bucket in the nearest AWS region. This helps you eliminate high-latency bottlenecks, ensuring that developers pull DDC data from a localized cloud instance rather than a distant central server.
Implement a Local Proxy Cache
Because cloud storage is slower than a local disk, a best practice is to use the S3 client in tandem with a local NVMe-based cache. This “layered” approach allows the engine to check the fast local drive first and only use the S3 client for missing data, helping you eliminate redundant bandwidth costs.
Use for Automated Crash Report Uploads
Utilize the S3 client to automatically push minidumps and logs to a private bucket when an error occurs. This is the most efficient way to eliminate the need for manual reporting from testers, as the engine can push diagnostic data to the cloud as soon as an elimination of the process (a crash) is detected.
Monitor for Redacted Credential Errors
When a request fails, S3 client logs often redact sensitive details to prevent security leaks. To eliminate ambiguity during debugging, check the LogS3Client output; if the error is “Access Denied,” ensure the UE-CloudDataCacheAccessToken is correctly set in your environment.
Optimize Bucket Permissions (Deny LIST)
For security, configure your S3 bucket to deny LIST requests. The S3 client works best when it knows the exact path or hash of the object it needs. This “Need-to-Know” configuration helps you eliminate security vulnerabilities where a compromised key could be used to scan the entire bucket contents.