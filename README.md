# STRUGAL Maroc website

French-language STRUGAL website with a native video hero, product catalogue, system comparisons, professional services, Moroccan project references, and a local contact directory.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 5173 --directory dist
```

Open http://localhost:5173/ in your browser. Serve through HTTP rather than opening HTML files directly: the location directory and video streaming use local HTTP requests.

## Project structure

- `dist/`: deployable static website, including HTML, styles, JavaScript, images, and streaming video assets.
- `scripts/home-template.html`: homepage content template.
- `scripts/build-content.py`: generates the static pages and shared navigation.
- `scripts/check-site.py`: validates internal links, assets, IDs, headings, and form labels.
- `.openai/hosting.json`: existing Sites deployment identity and static directory configuration.
- `VIDEO-SOURCE.md`: original film provenance, formats, and playback details.
- `VALIDATION.md`: design, accessibility, and functional verification notes.

## Generate and validate

```sh
python3 scripts/build-content.py
python3 scripts/check-site.py
node --check dist/script.js
node --check dist/video.js
```

No npm install or framework build is required. Python 3 generates and checks the pages; Node.js is only used for optional JavaScript syntax checks.

## Video

The native background uses a self-hosted HLS playlist with 4K VP9 and 1080p H.264 variants, plus a 720p MP4 fallback. Browser and connection support determine playback quality. There are no YouTube embeds, player controls, or subtitle tracks. Reduced-motion preferences use a still image.

The downloaded original masters are retained outside this repository in the workspace's `media/` folder. They are not required to run the site; the deployable video assets are included in `dist/assets/`.

## Deployment

Deploy `dist/` with a static host that supports the included video files. Preserve the `.m3u8`, `.m4s`, `.mp4`, and `.ts` assets. The current Sites configuration is retained. GitHub Pages publishes the `gh-pages` branch, whose root contains the contents of `dist/`.

After committing changes to `main`, publish an update with:

```sh
bash scripts/deploy-github-pages.sh
```

GitHub CLI authentication is required. This pushes only the deployable website to `gh-pages`, keeping the source branch separate. The live address is https://prompolu.github.io/strugal-website/.

## Contact brief

The project brief is prepared locally in the browser and can be copied. It does not submit email or CRM requests. Telephone and directions links use the published STRUGAL contact details.

## Assets and licensing

STRUGAL branding, photography, product data, and film retain their respective owners' rights. The vendored hls.js library includes its BSD-2-Clause license under `dist/vendor/`.
