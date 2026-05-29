# SvelteKit on Connect

**Requires Connect 2026.05 or higher**

Deploying a SvelteKit app to Posit Connect.

## Connect config

`/etc/rstudio-connect/rstudio-connect.gcfg`

```ini
[EarlyAccess]
NodeJs = true

[NodeJs]
Enabled = true
Executable = /usr/bin/node
```

Install NodeJS on Connect:

```bash
apt-get update && apt-get install -y curl ca-certificates \
  && curl -fsSL https://deb.nodesource.com/setup_24.x | bash - \
  && apt-get install -y nodejs \
  && rm -rf /var/lib/apt/lists/*
```

## Developing

Once you've created a project and installed dependencies with `npm install`, start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

## Deploying to Connect

<https://docs.posit.co/connect/user/nodejs/>

```sh
# Build the app
npm run check
npm run build

# Deploy to Connect
uvx --with rsconnect-python rsconnect deploy nodejs --entrypoint build/index.js .

# Or...
npm run connect-deploy
```
