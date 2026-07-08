---
layout: default
title: HttpNetworkReplayStreaming
---

<!-- ai-generation-failed -->

<h1>HttpNetworkReplayStreaming</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NetworkReplayStreaming/HttpNetworkReplayStreaming/HttpNetworkReplayStreaming.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreOnline, CoreUObject, Engine, HTTP, Json, NetworkReplayStreaming</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ted servers to “stream” gameplay data to a remote web server in real-time or post-match.

It is a critical component for large-scale multiplayer titles, facilitating the elimination of local storage constraints and enabling features like global match history, spectator broadcasting, and centralized cheat review.

Practical Usage Tips and Best Practices
1. Configure the Server URL in Engine.ini

To activate the module, you must specify your backend endpoint in DefaultEngine.ini. Under the [HttpNetworkReplayStreaming] section, set ServerURL="http://your-replay-server.com/". Note that the trailing slash is mandatory; omitting it can lead to the elimination of valid request paths during the upload process.

2. Implement the REST API Specification

The module expects a specific set of endpoints (e.g., /replay, /file, /event). Your backend must be prepared to handle POST requests for binary chunks and GET requests for downloading. Following the engine’s expected schema strictly is a best practice for the elimination of “404 Not Found” or “405 Method Not Allowed” errors during streaming.

3. Adjust Chunk Upload Latency

The console variable httpReplay.ChunkUploadDelayInSeconds controls how frequently the engine flushes data to your server. Lowering this value enables faster live-spectating but increases server load. Finding a balance leads to the elimination of excessive bandwidth spikes while maintaining a reasonable “live” delay.

4. Override Compression for Large Replays

To save bandwidth and storage, you can create a child class of FHttpNetworkReplayStreamer and override SupportsCompression. Returning true and implementing CompressBuffer ensures the elimination of redundant data before it leaves the client or server, significantly reducing your cloud egress costs.

5. Handle “Elimination” and Clean-up Events

When a match ends, the streamer sends a final “Stop” request. Ensure your backend logic uses this signal to finalize the replay file and move it from “temporary” to “permanent” storage. Proper session lifecycle management assists in the elimination of corrupted or “zombie” replay files that never reached completion.

6. Use for Scalable Spectator Modes

In competitive games, avoid having spectators connect directly to the game server. Instead, use this module to stream the data to a CDN-backed HTTP server. This architecture facilitates the elimination of CPU strain on the dedicated game server, allowing thousands of viewers to watch without impacting the players’ performance.

7. Secure Endpoints with Authentication

Since the module uses standard HTTP requests, your backend should validate the App and Version headers sent by the engine. Implementing token-based authentication in your custom streamer child class is a vital best practice for the elimination of unauthorized data uploads or scraping of private match data.

8. Verify Build.cs Dependencies

If you are extending the streamer or referencing it in C++, add "HttpNetworkReplayStreaming" and "NetworkReplayStreaming" to your Build.cs dependency list. Correct module linking is the primary requirement for the elimination of linker errors when compiling custom replay networking logic.