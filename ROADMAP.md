# CS Fundamentals Learning Project
## URL Shortener + Analytics Dashboard

A full-stack project built to learn computer science fundamentals from the ground up.
Built with: Python · FastAPI · PostgreSQL · Redis · React · Docker · GitHub Actions

---

## What We're Building

A system where users:
1. Paste a long URL → get a short one (e.g. `myapp.com/abc123`)
2. Share the short URL → it redirects to the original
3. View an analytics dashboard → see click counts, geography, timestamps

This single project teaches every major CS discipline.

---

## Tech Stack & Why

| Layer | Tool | Why |
|-------|------|-----|
| Backend | Python + FastAPI | Easy to learn, fast, industry-standard |
| Database | PostgreSQL | Relational SQL — most common in industry |
| Cache | Redis | Key-value store — teaches caching & performance |
| Frontend | React | Most in-demand frontend framework |
| Containers | Docker | Run anywhere, used at every company |
| CI/CD | GitHub Actions | Industry-standard automation |
| Deployment | Railway or Render | Free tier, simple, production-like |

---

## 11-Week Roadmap

### Phase 1 — Foundations (Weeks 1-2)
**Topics:** How the internet works · Git & GitHub · Project structure

- [ ] Understand HTTP, DNS, client-server model
- [ ] Install Git, create GitHub account
- [ ] Learn: commit, branch, push, pull
- [ ] Initialize this project repo on GitHub
- [ ] Set up Python environment (venv)

**Deliverable:** Project repo on GitHub with a README

---

### Phase 2 — Backend API (Weeks 3-5)
**Topics:** REST APIs · FastAPI · PostgreSQL · SQL · JWT Authentication

- [ ] Understand what an API is and REST principles
- [ ] Build FastAPI app with first endpoints
- [ ] Connect to PostgreSQL database
- [ ] Design the database schema (users, urls, clicks tables)
- [ ] Write SQL queries (SELECT, INSERT, JOIN)
- [ ] Add user registration and login with JWT tokens

**Deliverable:** Working API — shorten a URL, redirect, see clicks

---

### Phase 3 — Frontend (Weeks 6-7)
**Topics:** HTML · CSS · JavaScript · React · API integration

- [ ] HTML structure and semantic elements
- [ ] CSS styling basics
- [ ] JavaScript fundamentals (functions, events, fetch)
- [ ] React components, state, and props
- [ ] Build a dashboard: input form, URL list, click stats
- [ ] Connect React frontend to FastAPI backend

**Deliverable:** Usable web UI connected to the API

---

### Phase 4 — System Design in Practice (Week 8)
**Topics:** Caching · Hashing · Rate limiting · Performance

- [ ] Add Redis to cache URL lookups (fast redirects)
- [ ] Understand the hashing algorithm that generates short codes
- [ ] Add rate limiting (prevent abuse)
- [ ] Understand when caching helps vs. hurts

**Deliverable:** App handles load better, short codes generated correctly

---

### Phase 5 — DevOps (Weeks 9-10)
**Topics:** Docker · docker-compose · GitHub Actions · Deployment

- [ ] Write a Dockerfile for the backend
- [ ] Write docker-compose to run backend + PostgreSQL + Redis together
- [ ] Set up GitHub Actions: run tests on every push
- [ ] Deploy to Railway or Render (live public URL)

**Deliverable:** Live deployed app + CI/CD pipeline

---

### Phase 6 — Polish (Week 11)
**Topics:** Testing · Documentation · Resume presentation

- [ ] Write unit tests for URL shortening logic
- [ ] Write integration tests for API endpoints
- [ ] Write a solid README (what it is, how to run it, screenshots)
- [ ] Add the project to your resume

**Deliverable:** Resume-ready project with live link

---

## Concepts Covered (for Resume)

- REST API design
- Relational databases (PostgreSQL, SQL)
- Caching (Redis)
- Authentication (JWT, password hashing)
- React frontend development
- System design thinking
- Docker containerization
- CI/CD automation (GitHub Actions)
- Cloud deployment
- Software testing

---

## Learning Pattern (Every Phase)

1. **Explain** — understand the concept before touching code
2. **Read** — look at code together and understand each line
3. **Build** — write it yourself with guidance
4. **Verify** — confirm it works before moving on

---

## Current Phase

**Phase 1 — Foundations** (started 2026-05-20)
