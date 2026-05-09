# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

Proposal workspace for **neurogenetics.my** — a website project for client Prabu Sithamparam (Malaysia), managed by Karumbu.in (Chennai). Current status: Proposal Review phase. Quote v1.2 delivered; awaiting client approval before Milestone 1 kickoff.

Pricing: ₹48,000 INR (30-50-20 milestone payment). Blog Pack: ₹7,500/12-blog. Hosting: ₹10k upfront.

## PDF Generation

The primary deliverable is `quotes/neurogenetics_quote_v1.2.html` → PDF.

**Regenerate PDF from HTML quote:**
```bash
# Using wkhtmltopdf (preferred — handles logo scaling correctly)
wkhtmltopdf --enable-local-file-access quotes/neurogenetics_quote_v1.2.html quotes/neurogenetics_quote_v1.2.pdf

# Using Python pdfkit wrapper (scripts/generate_pdf.py)
# NOTE: hardcoded paths inside script point to Gemini brain dir — update before use
python3 scripts/generate_pdf.py
```

**Logo:** `assets/karumbu_logo.png` — always reference as absolute `file://` path in HTML for PDF converters. Use explicit `width` attribute (not just CSS max-width) to prevent scaling bugs.

**Styling:** `scripts/style.css` — shared CSS for all PDF outputs. `scripts/header.html` / `scripts/footer.html` — wkhtmltopdf header/footer partials.

## Directory Structure

| Dir | Purpose |
|-----|---------|
| `quotes/` | Final client-facing quote (HTML + PDF) |
| `final_deliverables/` | Signed-off scope PDFs for DNA Astrology and Clinic Website |
| `documents/` | Working docs: proposal, CMS strategy, implementation notes |
| `assets/` | Karumbu logo and branding assets |
| `scripts/` | PDF generation scripts and CSS |
| `research/` | Source material: audio, WhatsApp transcripts, reference PDFs |
| `reference_materials/` | Client-provided PDFs and session notes by date |
| `project_meta/` | Task tracking, walkthrough, implementation plan |

## Key Documents

- `documents/neurogenetics_proposal.md` — full background, 4D model strategy, roadmap
- `documents/cms_strategy.md` — Agent-First CMS workflow with AI image generation detail
- `project_meta/walkthrough.md` — summary of all work accomplished and asset index
- `project_meta/task.md` — completed task checklist (historical, all done)

## Scripts Notes

`scripts/fix_docs.py` and `scripts/generate_covers.sh` reference hardcoded paths under `/home/dev-dell/.gemini/antigravity/brain/` — these are legacy scripts from prior workflow and require path updates before reuse.

`scripts/md-to-pdf.config.js` is an md-to-pdf (Node) config — requires `npm install -g md-to-pdf` if used.
