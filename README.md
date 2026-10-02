<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:10b981&height=220&section=header&text=Shivam%20Nath%20Goswami&fontSize=46&fontColor=ffffff&fontAlignY=38&desc=Backend%20Engineer%20%C2%B7%20Java%20%C2%B7%20Spring%20Boot%20%C2%B7%20Distributed%20Systems&descAlignY=60&descSize=18" width="100%"/>
</div>

<h3 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=10B981&center=true&vCenter=true&width=700&lines=I+build+backends+that+don't+fall+over+under+load;Spring+Boot+%7C+PostgreSQL+%7C+JWT+%7C+Webhooks+%7C+RAG;Smart+India+Hackathon+%E2%80%94+Top+8+Finalist+%F0%9F%8F%86;Open+to+SDE+%2F+Backend+internships" alt="Typing SVG" />
</h3>

<p align="center">
  <a href="https://shvmmonk.vercel.app"><img src="https://img.shields.io/badge/Portfolio-shvmmonk.vercel.app-06B6D4?style=for-the-badge&logo=vercel&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/shivam-goswami-88633124a/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:shvmnath.monk@gmail.com"><img src="https://img.shields.io/badge/Email-Hire_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

---

## ⚡ Recruiter TL;DR

| | |
|---|---|
| **Role** | Backend Developer Intern @ [Flowshipz](https://flowshipz.com) — Spring Boot REST APIs, PostgreSQL/MySQL schemas, JWT auth, webhooks |
| **Education** | B.Tech CSE, SRM Institute of Science & Technology (2024–2028) · **CGPA 8.9** |
| **Strengths** | Java · Spring Boot · REST API design · SQL · Concurrency · Socket networking · RAG pipelines |
| **Proof** | 🏆 **SIH Top 8 Finalist** (180+ teams) · 🥈 Technova 2026 National Finalist · 🧩 200+ LeetCode / NeetCode problems |
| **Looking for** | Backend / SDE internships & full-time roles |

> 💡 *"APIs & clean architecture > AI hype. Get the fundamentals right."*

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
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=shvmmonk&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=shvmmonk&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" />
</p>

---

## 🌱 Currently

- 🔨 Building **supportlyAi** — RAG + WhatsApp automation
- 📚 Learning **distributed systems design** & advanced DSA
- 🔭 Exploring **microservices**, caching and message queues

---

<div align="center">

### 🤝 Let's build something solid.

**Open to backend / SDE roles** · [Email](mailto:shvmnath.monk@gmail.com) · [LinkedIn](https://www.linkedin.com/in/shivam-goswami-88633124a/) · [Portfolio](https://shvmmonk.vercel.app)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:10b981,100:0f172a&height=100&section=footer" width="100%"/>

</div>
