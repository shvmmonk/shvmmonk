<!-- =========================================================
     GITHUB PROFILE README — SHIVAM NATH GOSWAMI
     ========================================================= -->

<div align="left">
  <h1>Shivam Nath Goswami</h1>
  <h3>Backend engineering is what happens behind the screen.</h3>
  <p>
    Backend Developer Intern at <a href="https://flowshipz.com">Flowshipz</a> &nbsp;·&nbsp;
    B.Tech CSE at SRMIST (2024–2028)
  </p>
</div>

I build backend services with **Java, Spring Boot, SQL, and REST APIs**. I enjoy turning complex workflows into secure, maintainable systems—from authentication and order processing to integrations and real-time communication.

Outside my internship work, I'm building **supportlyAi**, exploring **distributed systems**, and sharpening my **DSA and problem-solving** skills.

<p align="left">
  <a href="https://shvmmonk.vercel.app"><img src="https://img.shields.io/badge/Portfolio-181717?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/shivam-goswami-88633124a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:shvmnath.monk@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

> **Currently:** Backend Developer Intern · Open to **Backend / SDE internship opportunities**

---

## 👨‍💻 Engineering at a Glance

| | |
|---|---|
| **Building** | [supportlyAi](https://github.com/shvmmonk/supportlyAi) — WhatsApp customer support automation |
| **Working on** | [Flowshipz](https://flowshipz.com) — orders, shipments, tracking, API testing |
| **Core stack** | Java · Spring Boot · PostgreSQL · MySQL · JWT · REST APIs |
| **Learning** | Distributed Systems · System Design · DSA |

---

## 🛠️ Tech Stack

**Backend** &nbsp;
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

**Databases** &nbsp;
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**Frontend** &nbsp;
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Tools** &nbsp;
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![IntelliJ](https://img.shields.io/badge/IntelliJ-000000?style=flat-square&logo=intellijidea&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

---

## 🚀 Flagship Project

### 🤖 supportlyAi — RAG Customer Support & WhatsApp Automation Platform

**Problem:** Small businesses answer the same customer questions on WhatsApp all day.

**Solution:** Upload a PDF knowledge base → the platform answers customer queries automatically on WhatsApp using retrieval-augmented generation.

```mermaid
flowchart LR
    A[Customer on WhatsApp] -->|message| B[WhatsApp API Webhook]
    B --> C[Spring Boot REST API]
    C --> D{JWT Auth}
    D --> E[RAG Engine]
    E --> F[(PDF Vector Knowledge Base)]
    E --> G[LLM]
    G --> C
    C --> H[(MySQL)]
    C -->|reply| A
```

**Highlights:** Spring Boot REST APIs · JWT auth · PDF vector knowledge base · WhatsApp API integration · MySQL persistence

**Stack:** `Java` `Spring Boot` `RAG` `JWT` `MySQL`

[![Repo](https://img.shields.io/badge/View_Code-181717?style=for-the-badge&logo=github)](https://github.com/shvmmonk/supportlyAi)

---

## 🧱 More Projects

### 🏢 Flowshipz — Production Backend Services

**Problem:** The product needs secure, reliable APIs that talk to the frontend and to third-party services in real time.

**Solution:** Built and maintained Spring Boot REST APIs with JWT-secured endpoints, relational schemas and webhook handlers.

```mermaid
flowchart LR
    A[Client App] -->|HTTPS request| B[Spring Boot REST API]
    B --> C{JWT Auth Filter}
    C -->|valid token| D[Service Layer]
    C -->|invalid| X[401 Unauthorized]
    D --> E[(PostgreSQL / MySQL)]
    F[Third-party Service] -->|webhook event| G[Webhook Endpoint]
    G --> D
    D -->|JSON response| A
```

**Highlights:** REST API design · PostgreSQL/MySQL schema design · JWT authentication · Webhook integrations

**Stack:** `Java` `Spring Boot` `PostgreSQL` `MySQL` `JWT`

[![Company](https://img.shields.io/badge/Visit-Flowshipz-10B981?style=for-the-badge)](https://flowshipz.com)

---

### 📡 An Intelligent Eye — Drone GCS

**Problem:** Live drone video drops frames and lags when the network is unreliable.

**Solution:** A custom Ground Control Station with low-level socket networking: UDP for the live video stream and TCP for reliable control commands, tuned to reduce packet loss.

```mermaid
flowchart LR
    A[Drone Camera] --> B[Video Encoder]
    B -->|UDP video stream| C[GCS Receiver]
    C --> D[Packet Buffer and Reassembly]
    D --> E[Live Video Display]
    F[Operator Controls] --> G[GCS Command Module]
    G -->|TCP reliable commands| H[Drone Controller]
    H -->|TCP telemetry| G
```

**Highlights:** UDP/TCP socket protocols · Packet-loss mitigation for video · Custom Ground Control Station

**Stack:** `Java` `UDP/TCP Sockets` `Networking`

[![Repo](https://img.shields.io/badge/View_Profile-181717?style=for-the-badge&logo=github)](https://github.com/shvmmonk)

---

## 🏆 Achievements

- 🥇 **Smart India Hackathon — Top 8 Finalist** out of 180+ teams
- 🥈 **Technova 2026 — National Finalist**
- 🧩 **200+ problems** solved on LeetCode / NeetCode
- 🎓 **CGPA 8.9** at SRMIST

---

## 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=shvmmonk&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=shvmmonk&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" alt="Top languages" />
</p>

---

## 🌱 Currently

- 🔨 Building **supportlyAi** — RAG + WhatsApp automation
- 📚 Learning **distributed systems design** & advanced DSA
- 🔭 Exploring **microservices**, caching and message queues

---

<div align="center">
  <h3>Let's build something solid.</h3>
  <p>
    <a href="mailto:shvmnath.monk@gmail.com">Email</a> ·
    <a href="https://www.linkedin.com/in/shivam-goswami-88633124a/">LinkedIn</a> ·
    <a href="https://shvmmonk.vercel.app">Portfolio</a>
  </p>
</div>
