# STRUGAL corporate film 2026

Source supplied by the user: https://www.youtube.com/watch?v=Uotj6h6rSXc

Downloaded originals are retained in the workspace media directory, outside the deployment source tree:
- ../media/strugal-2026-4k.mkv
- ../media/strugal-2026-4k-stream.mkv

Verified source: 3840 × 2160, 25 fps, 93.188 seconds, VP9 with original Opus audio. The website background is intentionally silent and excludes subtitle tracks.

The 4K video is repackaged without re-encoding into fragmented MP4 HLS segments under dist/assets/film-4k/. A 1080p H.264 stream and 720p MP4 provide compatibility. dist/assets/strugal-film.m3u8 declares the available streaming variants. The site serves all video segments and its HLS helper itself; no YouTube iframe or YouTube scripts remain. The original audio remains in the downloaded master files.

HLS helper: hls.js 1.7.4, BSD-2-Clause, license retained in dist/vendor/hls-LICENSE.txt.
