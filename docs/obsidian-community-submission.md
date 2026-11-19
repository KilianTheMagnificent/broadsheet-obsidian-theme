# Obsidian Community Theme Submission Packet

This document tracks everything required to publish **Broadsheet** to the official Obsidian Community Themes directory once `KilianTheMagnificent/broadsheet-obsidian-theme` is made public.

## Pre-submission checks (verified locally)

| Requirement | Status | Details |
| --- | --- | --- |
| Root `manifest.json` | Ready | Valid JSON with `name`, `version` (`1.0.0`), `minAppVersion` (`1.4.0`), `author`, and `authorUrl` (`https://github.com/KilianTheMagnificent`). |
| Unique theme name | Ready | `"Broadsheet"` uses Basic Latin characters only, avoids `"Obsidian"` and `"Theme"`, and has zero collisions in `obsidianmd/obsidian-releases/community-css-themes.json`. |
| Root `theme.css` | Ready | Supports both `.theme-light` (**Day**) and `.theme-dark` (**Night Print**) with offline local/system font stacks only (zero external `@import` requests). |
| Root `README.md` | Ready | Describes the theme, install steps, Style Settings controls, offline fonts, and links screenshots via relative `./docs/screenshots/...` paths. |
| Root `LICENSE` + notices | Ready | MIT License (`Copyright (c) 2026 Andre Romero`) plus `THIRD_PARTY_NOTICES.md` and CSS header attribution for CyanVoxel's MIT-licensed companion snippets (`Copyright (c) 2024 Travis Abendshien`). |
| Store screenshot (`512 × 288`, 16:9) | Ready | [`docs/screenshots/broadsheet-store-preview.png`](./screenshots/broadsheet-store-preview.png) (`512 × 288` PNG showing Day and Night Print side by side), alongside full-page light/dark previews. |

## `community-css-themes.json` entry

Validated JSON entry matching the schema of `obsidianmd/obsidian-releases/community-css-themes.json`:

```json
{
  "name": "Broadsheet",
  "author": "Andre Romero",
  "repo": "KilianTheMagnificent/broadsheet-obsidian-theme",
  "screenshot": "docs/screenshots/broadsheet-store-preview.png",
  "modes": ["dark", "light"]
}
```

## Post-publish checklist (run after Andre confirms going public)

1. **Create and push the public repository** at `https://github.com/KilianTheMagnificent/broadsheet-obsidian-theme` (`main` branch).
2. **Configure GitHub repository settings:**
   - Enable **Private Vulnerability Reporting** under **Settings → Code security** (matching `SECURITY.md`).
   - Restrict pull requests / interactions to collaborators where applicable (matching `CONTRIBUTING.md`).
   - Confirm the `.github/workflows/validate.yml` workflow passes on `main`.
3. **Create the initial GitHub Release (`1.0.0`):**
   - **Important tag rule:** Obsidian requires the GitHub release tag to match `manifest.json`'s `"version"` literally — use **`1.0.0`** (SemVer `x.y.z`, **no leading `v`**).
   - Attach **`manifest.json`** and **`theme.css`** as release assets.
4. **Submit to the Obsidian Community Directory:**
   - Go to <https://community.obsidian.md> and sign in with your Obsidian account.
   - Link your GitHub account (`KilianTheMagnificent`) to verify repository ownership.
   - Open **Themes → New theme** and enter:
     - Repository: `KilianTheMagnificent/broadsheet-obsidian-theme`
     - Screenshot path: `docs/screenshots/broadsheet-store-preview.png`
     - Supported modes: **Dark** and **Light**
   - Review and resolve any automated check messages from the directory review.
   - *(Note: Obsidian now handles new theme registrations via [community.obsidian.md](https://community.obsidian.md), which updates `obsidianmd/obsidian-releases/community-css-themes.json`; the validated JSON block above is kept here as an exact schema reference.)*
