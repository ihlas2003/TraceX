
# 🕵️‍♂️  TraceX - OSINT Location & Data Harvester

TraceX is a Python-based Open Source Intelligence (OSINT) tool designed to demonstrate data exposure risks. It gathers public information including social media presence, IP address geolocation, and hidden EXIF metadata (GPS coordinates & device fingerprinting) from images.

---

## 🚀 Features

- **🌐 IP Address Tracker**: Fetches city, country, and ISP details(sometimes) using public IP APIs.
- **👤 Username Tracker**: Enumerates usernames across multiple platforms (GitHub, TryHackMe, Instagram, Instagram, Pinterest, TkiTok) using HTTP status detection.
- **📸 Photo EXIF & Device Fingerprint Extractor**: Reads image metadata to extract:
  - Device Make & Model
  - Software / Operating System
  - Date & Time taken
  - Exact GPS Coordinates (Latitude & Longitude)
- **🗺️ Interactive Map Generator**: Draws exact GPS locations on an HTML interactive map using `Folium`.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**: `requests`, `exifread`, `folium`, `pillow`
- **Platform**: Kali Linux

---

## 📦 Installation & Usage

**Clone the Repository**:
---------------------------
   git clone [https://github.com/ihlas2003/TraceX.git](https://github.com/ihlas2003/TraceX.git)
   cd TraceX
   chmod +x traceX.sh && ./traceX.sh
