# Apollo Music Library – DevOps Starter Skeleton

This repository provides a **minimal DevOps starter skeleton** for the Apollo Music Library assignment. It includes a basic Flask app, a sample SQLAlchemy model, a placeholder Apache config, and empty Dockerfile and docker-compose.yml for you to complete as part of your assignment.

## What You Get

- Minimal Flask app with a health check endpoint (`/health`)
- Example SQLAlchemy model (not music-specific)
- Sample Apache HTTPD config (reverse proxy)
- Empty `Dockerfile` and `docker-compose.yml` (add your own implementation)
- Minimal test for `/health` endpoint
- Example CI workflow (GitHub Actions)
- `CONTRIBUTORS.md` for tracking team contributions

## How to Start

1. **Clone this repository.**
2. **Set up your Python environment** (e.g., `python -m venv venv && source venv/bin/activate`).
3. **Install dependencies:**
   ```sh
   pip install -r app/requirements.txt
   ```
4. **Run the Flask app locally:**
   ```sh
   python -m app.app
   ```
5. **Run tests:**
   ```sh
   pytest
   ```
6. **Complete the Dockerfile and docker-compose.yml** to containerize the app and orchestrate the stack.
7. **Implement the music library features** as described in your assignment brief.

## Contributors

- Use `CONTRIBUTORS.md` to record your work. Each team member should add their name, GitHub username, and a brief summary of their contributions. This helps instructors review individual work.

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Apache HTTPD Docs](https://httpd.apache.org/docs/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

**Note:** The provided Dockerfile and docker-compose.yml are intentionally left empty with comments. You are expected to complete them as part of your assignment.
