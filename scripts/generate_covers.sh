#!/bin/bash
BASE_DIR="/home/dev-dell/.gemini/antigravity/brain/fd58b605-665f-439b-8c14-ff649c6e2d59"
LOGO_PATH="/home/dev-dell/Insync/devanathan.n@viewzenlabs.com/Google Drive/backup/Personal/Karumbu/ref/karumbu.in Logo.jpg"

function prepend_cover() {
  local FILE=$1
  local TITLE=$2
  
  cat << HTML > temp_cover.html
<div style="text-align: center; margin-top: 150px; font-family: sans-serif;">
  <img src="file://${LOGO_PATH}" alt="Karumbu.in Logo" style="max-width: 400px; margin-bottom: 50px;">
  <h1 style="color: #2c3e50; font-size: 36px; margin-bottom: 10px;">Scope Document</h1>
  <h2 style="color: #34495e; font-size: 28px; font-weight: normal;">${TITLE}</h2>
  <div style="margin-top: 200px; color: #7f8c8d; font-size: 14px;">
    <strong>Karumbu.in</strong><br>
    Flat 1B, Harmony, New no 27, Old no 14, East Street, RR Colony<br>
    Ashok Nagar, Chennai 600083<br>
    Phone: +91 9025737344 | Email: gurudev@karumbu.in
  </div>
</div>
<div style="page-break-after: always;"></div>

HTML

  cat temp_cover.html "$FILE" > temp_combined.md
  mv temp_combined.md "$FILE"
}

# Only run if not already prepended
if ! grep -q "temp_cover.html" "${BASE_DIR}/scope_dna_astrology.md"; then
  prepend_cover "${BASE_DIR}/scope_dna_astrology.md" "DNA Astrology Web Application"
fi

if ! grep -q "temp_cover.html" "${BASE_DIR}/scope_clinic_website.md"; then
  prepend_cover "${BASE_DIR}/scope_clinic_website.md" "Professional Clinic & Coaching Website"
fi

rm -f temp_cover.html
