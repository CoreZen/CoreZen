<div align="center">

<img src="assets/header.svg" alt="Daniel Grigoriev, Threat Hunter and Software Engineer" width="854" height="260" />

[![Portfolio](https://img.shields.io/badge/engin.re-portfolio-0d1117?style=flat-square&logo=cloudflare&logoColor=f38020)](https://engin.re)
[![LinkedIn](https://img.shields.io/badge/linkedin-daniel--grigoriev-0d1117?style=flat-square&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iIzBhNjZjMiIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU2di01LjU3YzAtMS4zMy0uMDItMy4wNC0xLjg1LTMuMDQtMS44NSAwLTIuMTMgMS40NS0yLjEzIDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjh6TTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTN6TTcuMTIgMjAuNDVIMy41NVY5aDMuNTd2MTEuNDV6TTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1Yy45OCAwIDEuNzgtLjc3IDEuNzgtMS43M1YxLjczQzI0IC43NyAyMy4yIDAgMjIuMjIgMHoiLz48L3N2Zz4=)](https://linkedin.com/in/daniel-grigoriev)

</div>

```console
$ cat about.txt
```

Threat hunter and software engineer. I look for adversaries in telemetry, take malware apart, and build the tooling that makes both faster.

- **Hunt.** Hypothesis-driven threat hunting and detection engineering.
- **Reverse.** Malware analysis and reverse engineering.
- **Build.** Detection tooling and adversary-facing infrastructure. Backends, mobile apps, and open-source contributions on the side.

> *"A jack of all trades is a master of none, but oftentimes better than a master of one."*

```console
$ ls arsenal/
```

| Project | What it does | Stack |
|---|---|---|
| [**SecureSign**](https://github.com/raz34900/SecureSign) | Offline handwritten-signature verification and forgery detection as a shared registry. A bank enrols once, every subscriber verifies against the same references. Took it [from prototype to production](https://github.com/raz34900/SecureSign/pull/1): Docker Compose, Nginx TLS, AES-256-GCM PII, pgBackRest PITR. | Python · FastAPI · PyTorch · OpenCV · Vue 3 · PostgreSQL |
| **Nkazi** | Hebrew-first iOS GPA calculator. Kotlin Multiplatform shared logic, SwiftUI, SwiftData + CloudKit sync, [App Store](https://apps.apple.com/us/app/id6759505137). | Kotlin · Swift |
| **CheckBin** | Card BIN lookup REST API. Redis-cached, load-tested on a tiny EC2 box. Source private. | Kotlin · Ktor · PostgreSQL · Redis |

```console
$ git log --author=CoreZen --upstream
```

<!--START_SECTION:pinned-->
| Repo | Contribution | Status |
|---|---|---|
| [cowrie/cowrie](https://github.com/cowrie/cowrie) | [Shell fd redirection and stderr routing](https://github.com/cowrie/cowrie/pull/2849): fixed `2>/dev/null` edge cases, refactored parsing, added tests. Original PR [#2805](https://github.com/cowrie/cowrie/pull/2805). | Merged · shipped in [v2.9.3](https://github.com/cowrie/cowrie/releases/tag/v2.9.3) |
| [cowrie/cowrie](https://github.com/cowrie/cowrie) | [Discord webhook output plugin](https://github.com/cowrie/cowrie/pull/2798): queue-based retry and rate-limit handling. | Merged |
| [cowrie/cowrie](https://github.com/cowrie/cowrie) | [FTP URL support in emulated `wget`](https://github.com/cowrie/cowrie/pull/2787). | Merged |
| [0ct0sec/M5PORKCHOP](https://github.com/0ct0sec/M5PORKCHOP) | [WiGLE/WPA-SEC uploads failing on low heap](https://github.com/0ct0sec/M5PORKCHOP/pull/49): static-canvas TLS arena. | Merged |
| [0ct0sec/M5PORKCHOP](https://github.com/0ct0sec/M5PORKCHOP) | [pwncrack.org hash-cracking sync](https://github.com/0ct0sec/M5PORKCHOP/pull/50). | Open |
| [raz34900/SecureSign](https://github.com/raz34900/SecureSign) | [From prototype to production](https://github.com/raz34900/SecureSign/pull/1): full platform build-out. | Merged |
<!--END_SECTION:pinned-->

<sub>More, refreshed weekly:</sub>

<!--START_SECTION:prs-->
| Repo | Contribution | Status |
|---|---|---|
| [maorm36/PiraTv](https://github.com/maorm36/PiraTv) | [Fix ellipsis formatting in README](https://github.com/maorm36/PiraTv/pull/1) | Merged |
<!--END_SECTION:prs-->

```console
$ cat skills.txt
```

**Security**

<img src="https://img.shields.io/badge/Threat%20Hunting-161b22?style=for-the-badge&color=161b22" alt="Threat Hunting" />
<img src="https://img.shields.io/badge/Detection%20Engineering-161b22?style=for-the-badge&color=161b22" alt="Detection Engineering" />
<img src="https://img.shields.io/badge/Malware%20Analysis-161b22?style=for-the-badge&color=161b22" alt="Malware Analysis" />
<img src="https://img.shields.io/badge/Reverse%20Engineering-161b22?style=for-the-badge&color=161b22" alt="Reverse Engineering" />
<img src="https://img.shields.io/badge/DFIR-161b22?style=for-the-badge&color=161b22" alt="DFIR" />
<img src="https://img.shields.io/badge/Network%20Forensics-161b22?style=for-the-badge&color=161b22" alt="Network Forensics" />
<img src="https://img.shields.io/badge/MITRE%20ATT%26CK-161b22?style=for-the-badge&color=161b22" alt="MITRE ATT&CK" />
<img src="https://img.shields.io/badge/SIEM%20%2F%20EDR-161b22?style=for-the-badge&color=161b22" alt="SIEM / EDR" />

**Tooling**

<a href="https://ghidra-sre.org/"><img src="https://img.shields.io/badge/Ghidra-b30000?style=for-the-badge&logoColor=white" alt="Ghidra" /></a>
<a href="https://hex-rays.com/ida-pro"><img src="https://img.shields.io/badge/IDA%20Pro-1a1a1a?style=for-the-badge&logoColor=white" alt="IDA Pro" /></a>
<a href="https://www.wireshark.org/"><img src="https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" alt="Wireshark" /></a>
<a href="https://www.splunk.com/"><img src="https://img.shields.io/badge/Splunk%20%2F%20SPL-000000?style=for-the-badge&logo=splunk&logoColor=white" alt="Splunk / SPL" /></a>
<a href="https://suricata.io/"><img src="https://img.shields.io/badge/Suricata-e45a1c?style=for-the-badge&logoColor=white" alt="Suricata" /></a>
<a href="https://virustotal.github.io/yara/"><img src="https://img.shields.io/badge/YARA-4b6cb7?style=for-the-badge&logoColor=white" alt="YARA" /></a>

**Languages**
<img src="https://skillicons.dev/icons?i=python,kotlin,java,swift,c,ts,js,dart,bash&theme=dark" alt="Python, Kotlin, Java, Swift, C, TypeScript, JavaScript, Dart, Bash" height="36" />

**Infra & tools**
<img src="https://skillicons.dev/icons?i=linux,docker,kubernetes,aws,gcp,cloudflare,terraform,postgres,mongodb,redis,githubactions,react,ktor,spring,flutter&theme=dark" alt="Linux, Docker, Kubernetes, AWS, GCP, Cloudflare, Terraform, PostgreSQL, MongoDB, Redis, GitHub Actions, React, Ktor, Spring, Flutter" height="36" />

---

<div align="center">

Open to interesting problems. Reach me through <a href="https://engin.re">engin.re</a> or <a href="https://linkedin.com/in/daniel-grigoriev">LinkedIn</a>.

</div>
