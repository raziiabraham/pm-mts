# Standalone book diagrams

The packaged companion includes all 25 final book diagrams as individual files:

- `png/` contains the reading- and presentation-ready raster versions.
- `svg/` contains scalable vector versions for print, slides, and editing.
- `pdf/` contains A4-normalized, individually printable versions with figure titles and captions.
- `manifest.json` maps each figure number to its title, chapter, caption, alt text,
  format, and source notes.
- `contact_sheet.png` provides a quick visual index of the complete set.

The repository root also contains `PM-MTS-Printable-Figures.pdf`, a combined
25-page print pack. Portrait diagrams use portrait A4 pages; landscape diagrams,
including the three spread figures, use landscape A4 pages. Print with “Fit to
printable area” if your PDF viewer does not scale mixed-orientation pages
automatically.

The spread figures (`F0.1`, `F12.2`, and `F20.1`) are supplied as complete
two-page compositions. Their cross-page connectors align when the image is
split at its vertical midpoint, matching the final book.

These are the same generated assets used by the current publication build; they
are added to the companion archive during release packaging so the book and
standalone copies cannot drift apart.
