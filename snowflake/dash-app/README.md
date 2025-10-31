# Snowflake Example with Dash

```bash
# Create virtual env and install dependencies
uv sync

# Run the app
uv run app.py

# Before deploying the app
uv export --output-file requirements.txt --no-hashes
```

## Notes

- The [Positron Develop Data Apps feature](https://docs.posit.co/ide/server-pro/user/positron/guide/proxying-web-servers.html#positron-run-app) is not working at this time (2025-10-29). Run in the terminal instead.