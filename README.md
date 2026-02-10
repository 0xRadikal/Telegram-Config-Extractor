<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=220&text=V2Ray%20Config%20Extractor&fontAlign=50&fontAlignY=40&color=0:7c3aed,50:ec4899,100:f97316&animation=twinkling&fontColor=ffffff&desc=Advanced%20Telegram%20Bot%20for%20Subscription%20Parsing&descAlignY=70&descAlign=50" width="100%" alt="V2Ray Config Extractor header" />
</p>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=20&duration=2600&pause=1100&color=F97316&center=true&vCenter=true&width=720&lines=Auto+Base64+Padding+Fix+Algorithm;Extracts+Configs+from+Subscription+Links;Generates+Ready-to-Import+.txt+Files;Built-in+HTTP+Proxy+Tunneling;High+Performance+Python+Bot" alt="Config Extractor typing intro" />
</p>

<p align="center">
<a href="https://github.com/0xradikal/Telegram-Config-Extractor"><img src="https://img.shields.io/badge/Repo-Config_Extractor-6366f1?style=for-the-badge&logo=github" alt="Repo" /></a>
<a href="https://github.com/0xradikal"><img src="https://img.shields.io/badge/Made_by-Radikal.eth-ec4899?style=for-the-badge&logo=ethereum" alt="Author" /></a>
<img src="https://img.shields.io/badge/Stack-Python%20%7C%20PTB%20%7C%20Requests-0ea5e9?style=for-the-badge" alt="Stack" />
<img src="https://img.shields.io/badge/Protocol-V2Ray_/_Xray-14b8a6?style=for-the-badge" alt="Protocol" />
</p>

# Telegram Config Extractor

A robust, open-source Python Telegram bot that fetches V2Ray/Xray subscription links, fixes common Base64 padding errors, and outputs clean, ready-to-import .txt configuration files. Built for speed, reliability, and ease of use.

Short summary:
- Smart Base64 auto-fix for malformed subscriptions.
- Exports configs (vmess, vless, trojan, ...) as a downloadable .txt.
- Optional local HTTP proxy tunneling via environment variables.
- Async, non-blocking handling using python-telegram-bot (v20+).

## Features

| Feature | Description | Status |
|---|---:|:--:|
| Subscription Fetching | Download HTTP/HTTPS subscription content with custom User-Agent | ✅ |
| Base64 Auto-Fix | Detects & repairs missing Base64 padding before decoding | ✅ |
| File Generation | Creates in-memory .txt files (io.BytesIO) with extracted nodes | ✅ |
| Proxy Support | Route outgoing requests through local HTTP proxy (os.environ) | ✅ |
| Async Handling | Async python-telegram-bot for concurrent users | ✅ |
| Error Handling | Robust try/except for timeouts and invalid links | ✅ |
| Interactive UI | Custom ReplyKeyboard for improved UX | ✅ |

## Tech Stack
- Python 3.9+
- python-telegram-bot (v20+, async)
- requests
- base64, io, os, asyncio

## Quick Start

1. Clone
```bash
git clone https://github.com/0xradikal/Telegram-Config-Extractor.git
cd Telegram-Config-Extractor
```

2. Install
```bash
pip install -r requirements.txt
# or
pip install python-telegram-bot requests
```

3. Configure
- Edit main.py (or your entry script) and set:
```py
TOKEN = "YOUR_BOT_TOKEN_HERE"      # from @BotFather
PROXY_URL = "http://127.0.0.1:3067"  # optional local proxy
```
- Recommended: use environment variables or a .env file for TOKEN and PROXY_URL.

4. Run
```bash
python main.py
```

## Usage
1. /start — Initialize the bot and show keyboard.
2. Send any subscription link (http:// or https://).
3. Bot fetches the content (via proxy if configured), repairs Base64 padding, decodes, extracts nodes, and replies with configs.txt.

Example link:
https://sub.example.com/api/v1/client/subscribe?token=...

## How it works (Base64 padding fix)
Many subscription providers return Base64 strings missing '=' padding. The bot repairs them before decoding:

```py
# Repair missing padding
missing = len(encoded_data) % 4
if missing:
    encoded_data += "=" * (4 - missing)
decoded = base64.b64decode(encoded_data)
```

This simple step dramatically increases successful decodes for malformed subscriptions.

## Security & Proxy
- Proxy: The bot can route requests through a local HTTP proxy by setting os.environ['http_proxy'] / os.environ['https_proxy'] to PROXY_URL.
- Do not hardcode tokens in public repos. Use env vars for production.

## Persian — راهنمای فارسی
ربات برای استخراج و اصلاح کانفیگ‌های V2Ray/Xray طراحی شده است. لینک سابسکرایب را دریافت می‌کند، خطاهای Base64 را برطرف می‌کند و یک فایل txt آماده‌ی ایمپورت تحویل می‌دهد. مراحل استفاده مانند بخش انگلیسی است: استارت، ارسال لینک، دریافت فایل.

## Author
Mohammad (Radikal) — Python Developer & Network Security Enthusiast  
<p align="center">
<a href="https://github.com/0xradikal"><img src="https://img.shields.io/badge/GitHub-0xradikal-000000?style=for-the-badge&logo=github" alt="GitHub" /></a>
<a href="https://t.me/Raydikalx"><img src="https://img.shields.io/badge/Telegram-%40Raydikalx-26A5E4?style=for-the-badge&logo=telegram" alt="Telegram" /></a>
</p>

## License
MIT — free to fork, modify, and distribute.

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=140&section=footer&color=0:f97316,50:ec4899,100:6366f1&animation=twinkling" width="100%" alt="footer" />
</p>
