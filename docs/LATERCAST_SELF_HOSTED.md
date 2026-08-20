# LaterCast self-hosted downloader

LaterCast now uses a hybrid workflow:

- **Download + FFmpeg**: runs on a repository self-hosted runner labeled `latercast`.
- **GitHub Release + RSS update**: runs on GitHub-hosted Ubuntu after the prepared audio is uploaded as a temporary Actions artifact.
- **Local audio is temporary**: the workflow deletes `work/` on the self-hosted machine after the artifact upload (and also on failures).

## One-time runner setup

1. Open this repository on GitHub.
2. Go to **Settings → Actions → Runners → New self-hosted runner**.
3. Choose the operating system/architecture of the machine that will do the Bilibili download.
4. Run the exact download/configuration commands GitHub shows on that page.
5. Add the custom runner label:

   `latercast`

   You can add it during configuration or later from the runner's Labels section.
6. Start the runner and leave it online while adding an episode.

The registration token shown by GitHub is a one-time runner registration token. It is not stored in this repository and does not need to be added as a repository Secret.

## Required software on the self-hosted machine

The workflow installs Python 3.12 and the Python packages itself, but the machine must have these commands available in `PATH`:

- `ffmpeg`
- `ffprobe`

The workflow checks both before downloading an episode and fails early if either is missing.

## VPN / proxy routing

The runner must be able to reach GitHub over HTTPS. If GitHub needs a local HTTP(S) proxy, configure the self-hosted runner to use that proxy.

The LaterCast job sets:

```text
NO_PROXY=bilibili.com,.bilibili.com,b23.tv
```

so Bilibili traffic bypasses an ordinary HTTP(S) proxy while GitHub traffic can continue through the proxy.

If the VPN client is a **full-tunnel/TUN VPN** that routes all system traffic, `NO_PROXY` cannot override the operating-system route. In that case enable split tunneling in the VPN client so GitHub uses the VPN while Bilibili goes direct.

## Normal use

Once the runner shows **Idle** in GitHub:

1. Open **Actions → Add LaterCast Episode**.
2. Click **Run workflow**.
3. Paste a Bilibili/YouTube URL.
4. The self-hosted runner downloads/transcodes the audio and uploads a temporary artifact.
5. A GitHub-hosted runner publishes the M4A to GitHub Releases and commits RSS metadata to the `latercast` branch.

No podcast audio is intended to remain on the self-hosted machine after the job.