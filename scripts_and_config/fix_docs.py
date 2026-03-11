import os

base_dir = "/home/dev-dell/.gemini/antigravity/brain/fd58b605-665f-439b-8c14-ff649c6e2d59"
with open('/tmp/logo_base64.txt', 'r') as f:
    b64 = f.read().strip()

files_to_fix = [
    ("scope_dna_astrology.md", "DNA Astrology Web Application"),
    ("scope_clinic_website.md", "Professional Clinic & Coaching Website")
]

contact_info = f"""
<div style="page-break-before: always;"></div>
<div style="text-align: center; margin-top: 150px; font-family: sans-serif; color: #7f8c8d; font-size: 14px;">
    <img src="data:image/jpeg;base64,{b64}" alt="Karumbu.in Logo" style="max-width: 250px; margin-bottom: 30px;"><br>
    <strong>Karumbu.in</strong><br>
    Flat 1B, Harmony, New no 27, Old no 14, East Street, RR Colony<br>
    Ashok Nagar, Chennai 600083<br>
    Phone: +91 9025737344 | Email: gurudev@karumbu.in
</div>
"""

def generate_cover(title):
    return f"""<div style="text-align: center; margin-top: 150px; font-family: sans-serif;">
  <img src="data:image/jpeg;base64,{b64}" alt="Karumbu.in Logo" style="max-width: 400px; margin-bottom: 50px;">
  <h1 style="color: #2c3e50; font-size: 36px; margin-bottom: 10px;">Scope Document</h1>
  <h2 style="color: #34495e; font-size: 28px; font-weight: normal;">{title}</h2>
</div>
<div style="page-break-after: always;"></div>

"""

for fname, title in files_to_fix:
    path = os.path.join(base_dir, fname)
    with open(path, 'r') as f:
        content = f.read()
    
    # Strip existing cover page HTML
    idx = content.find('# Scope Document:')
    if idx != -1:
        pure_md = content[idx:]
        
        # Strip existing contact info if it somehow exists
        idx2 = pure_md.find('<div style="page-break-before: always;"></div>')
        if idx2 != -1:
            pure_md = pure_md[:idx2]
            
        new_content = generate_cover(title) + pure_md.strip() + "\n\n" + contact_info
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Updated {fname}")

def gen_config(title, filename):
    config = f"""module.exports = {{
  stylesheet: 'style.css',
  pdf_options: {{
    format: 'A4',
    margin: {{ top: '25mm', right: '20mm', bottom: '25mm', left: '20mm' }},
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="font-size: 10px; text-align: center; width: 100%; font-family: sans-serif; padding-top: 5px; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin: 0 20mm;">
        <span style="float: left; color: #7f8c8d;">Scope Document: {title}</span>
        <span style="float: right; color: #2c3e50; font-weight: bold;">Karumbu.in</span>
      </div>
    `,
    footerTemplate: `
      <div style="font-size: 9px; text-align: center; width: 100%; font-family: sans-serif; padding-bottom: 10px; color: #7f8c8d;">
        <em>Confidential & Proprietary</em> | Page <span class="pageNumber"></span> of <span class="totalPages"></span>
      </div>
    `
  }}
}};
"""
    with open(os.path.join(base_dir, filename), 'w') as f:
        f.write(config)
    print(f"Created {filename}")

gen_config("DNA Astrology App", "config_dna.js")
gen_config("Holistic Clinic Website", "config_clinic.js")
