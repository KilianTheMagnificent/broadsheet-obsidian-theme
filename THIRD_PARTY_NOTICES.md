# Third-Party Notices

The Broadsheet core theme (`theme.css`, `manifest.json`) is original work by Andre Romero released under the MIT License (see [LICENSE](LICENSE)).

The two optional companion CSS snippets under `snippets/` (and their corresponding offline previews in `preview/daily.html` and `preview/sidebar.html`) adapt open-source Obsidian CSS snippets created by **Travis Abendshien (CyanVoxel)** under the MIT License:

1. **Obsidian Daily Themes** (v1.0.5)
   - Upstream repository: <https://github.com/CyanVoxel/Obsidian-Daily-Themes>
   - Adapted in: `snippets/Daily Note Themes (Broadsheet).css`
   - Summary of modifications: Retargeted weekday accent hues onto Broadsheet CSS tokens (`--bs-accent`, `--bs-accent-text`, `--bs-paper`, `--bs-ink`) using `color-mix()` for both Day (light) and Night Print (dark) modes, added `:has()` leaf styling for the inline title masthead, and adjusted H4 kicker pills for Reading view and Live Preview.

2. **Obsidian Colored Sidebar** (v2.0.0)
   - Upstream repository: <https://github.com/CyanVoxel/Obsidian-Colored-Sidebar>
   - Adapted in: `snippets/Colored Sidebar Items (Broadsheet).css`
   - Summary of modifications: Preserved the numbered folder prefix color map (`00`–`07`, `99`) and re-based the contrast anchors (`--shadow`, `--highlight`, `--default-text-color`) onto Broadsheet's warm ink and newsprint palette so sidebar items stay readable in both light and dark modes, with active-file flags matching each folder's hue.

Both upstream works are distributed under the MIT License reproduced verbatim below:

```text
MIT License

Copyright (c) 2024 Travis Abendshien

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
