import os
import re
from multipage_data import SERVICES_DATA, DEPARTMENTS_DATA, DOCTORS_DATA, HOSPITAL_CONTACT

def build_all_pages():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract header / navigation / topbar / marquee
    nav_match = re.search(r'(<!DOCTYPE html>.*?(?=<header id="home"))', html, re.DOTALL)
    if not nav_match:
        print("ERROR: Could not match nav in index.html")
        return
    common_nav = nav_match.group(1)

    # Extract contact section, footer, modal, and script tags
    contact_footer_match = re.search(r'(<section id="contact".*?</html>)', html, re.DOTALL)
    if not contact_footer_match:
        print("ERROR: Could not match contact/footer in index.html")
        return
    common_footer = contact_footer_match.group(1)

    def set_meta(html_str, title, page_name, page_file=""):
        res = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_str)
        res = re.sub(r'<body[^>]*>', f'<body data-page="{page_name}">', res)
        if page_file:
            res = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://www.a1hospitalsrikakulam.com/{page_file}"', res)
            res = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://www.a1hospitalsrikakulam.com/{page_file}"', res)
            res = re.sub(r'<meta name="twitter:url" content="[^"]*"', f'<meta name="twitter:url" content="https://www.a1hospitalsrikakulam.com/{page_file}"', res)
        return res

    spacer = '\n    <div style="margin-top: 1.5rem;"></div>\n'

    # Realtime Map Section HTML
    map_section_html = f'''
    <!-- Realtime Location Map Section -->
    <section id="location" class="location-section framed-section animate-up" style="margin-top: 3.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> HOSPITAL LOCATION &amp; DIRECTIONS
            </div>
            <h2>Visit <span class="serif-italic">A1 Hospital</span></h2>
            <p>{HOSPITAL_CONTACT['address']}</p>
        </div>
        <div class="map-wrapper" style="border-radius: var(--radius-lg); overflow: hidden; border: 1.5px solid var(--border-warm); box-shadow: var(--shadow-sm); background: var(--bg-surface); padding: 1.25rem;">
            <iframe 
                src="{HOSPITAL_CONTACT['map_embed']}" 
                width="100%" 
                height="380" 
                style="border:0; border-radius: 12px; display: block;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade"
                title="A1 Hospital Realtime Map">
            </iframe>
            <div class="map-details-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; padding-top: 1.2rem; border-top: 1px solid var(--border-warm);">
                <div class="map-detail-item" style="display: flex; gap: 0.8rem; align-items: flex-start;">
                    <i data-lucide="map-pin" style="color: var(--primary-accent); width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                    <div>
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">Address</strong>
                        <span style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5;">{HOSPITAL_CONTACT['address']}</span>
                    </div>
                </div>
                <div class="map-detail-item" style="display: flex; gap: 0.8rem; align-items: flex-start;">
                    <i data-lucide="mail" style="color: var(--primary-accent); width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                    <div>
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">Online Appointments Email</strong>
                        <a href="mailto:{HOSPITAL_CONTACT['email']}" style="color: var(--primary-accent); text-decoration: none; font-size: 0.88rem; font-weight: 600;">{HOSPITAL_CONTACT['email']}</a>
                    </div>
                </div>
                <div class="map-detail-item" style="display: flex; gap: 0.8rem; align-items: flex-start;">
                    <i data-lucide="message-circle" style="color: #25D366; width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                    <div>
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">WhatsApp Help Desk</strong>
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" style="color: #25D366; text-decoration: none; font-size: 0.88rem; font-weight: 700;">+91 {HOSPITAL_CONTACT['whatsapp_number']}</a>
                    </div>
                </div>
                <div class="map-detail-item" style="display: flex; gap: 0.8rem; align-items: flex-start;">
                    <i data-lucide="phone-call" style="color: var(--primary-accent); width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                    <div>
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">24/7 Casualty Reception</strong>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" style="color: var(--text-dark); text-decoration: none; font-size: 0.88rem; font-weight: 700;">{HOSPITAL_CONTACT['phone_1']}</a>
                    </div>
                </div>
                <div class="map-detail-item" style="display: flex; gap: 0.8rem; align-items: flex-start;">
                    <i data-lucide="globe" style="color: var(--primary-accent); width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                    <div>
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">Official Website</strong>
                        <a href="{HOSPITAL_CONTACT['website']}" target="_blank" rel="noopener noreferrer" style="color: var(--primary-accent); text-decoration: none; font-size: 0.88rem; font-weight: 600;">{HOSPITAL_CONTACT['domain']}</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

    # Ensure map is inserted before footer if not present
    page_footer = common_footer
    if 'id="location"' not in page_footer:
        page_footer = page_footer.replace('<section id="contact"', map_section_html + '\n    <section id="contact"')

    # -------------------------------------------------------------
    # 1. BUILD SERVICES.HTML (Only 5 Essential Core Services)
    # -------------------------------------------------------------
    services_grid_items = ""
    for s_id, s in SERVICES_DATA.items():
        doc_lead = s['lead_doctor']
        services_grid_items += f'''
        <a href="{s['file']}" class="service-showcase-card animate-up" style="text-decoration:none; color:inherit; display:flex; flex-direction:column;">
            <div class="service-showcase-header-box" style="height:150px; background:linear-gradient(135deg, #fdf5f3 0%, #faece9 100%); display:flex; align-items:center; justify-content:center; position:relative; border-bottom:1.5px solid var(--border-warm);">
                <div style="width:68px; height:68px; border-radius:18px; background:#ffffff; color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 8px 22px rgba(128,0,0,0.12);">
                    <i data-lucide="{s['icon']}" style="width:34px; height:34px;"></i>
                </div>
                <div style="position:absolute; bottom:10px; right:12px; background:rgba(255,255,255,0.92); font-size:0.75rem; font-weight:700; color:var(--primary-accent); padding:3px 12px; border-radius:12px; border:1px solid rgba(128,0,0,0.08);">
                    {s['tag']}
                </div>
            </div>
            <div class="service-showcase-content">
                <span class="service-pill-tag">{s['tag']}</span>
                <h3>{s['title']}</h3>
                <p>{s['meaning']}</p>
                <div style="margin-top:auto; padding-top:0.8rem; border-top:1px solid var(--border-warm); display:flex; align-items:center; justify-content:space-between;">
                    <span style="font-size:0.82rem; color:var(--text-muted); font-weight:600;"><i data-lucide="user-check" style="width:13px; vertical-align:middle;"></i> {doc_lead['name'].split('&')[0].strip()}</span>
                    <span class="service-card-cta"><span>Explore Details</span> <i data-lucide="arrow-right"></i></span>
                </div>
            </div>
        </a>'''

    services_carousel_items = ""
    for s_id, s in SERVICES_DATA.items():
        services_carousel_items += f'''
        <a href="{s['file']}" style="text-decoration:none; color:inherit; display:block;">
            <div class="dept-card-photo" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.8rem 1.4rem; background:var(--bg-surface); min-width:240px; height:180px; text-align:center;">
                <div class="card-icon-badge" style="width:54px; height:54px; margin-bottom:1rem;">
                    <i data-lucide="{s['icon']}"></i>
                </div>
                <div class="dept-info" style="border:none; padding:0; background:transparent;"><h3>{s['title']}</h3></div>
            </div>
        </a>'''

    services_body = f'''
    {spacer}
    <section class="services framed-section animate-up" style="margin-top: 1.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> CORE HOSPITAL FACILITIES
            </div>
            <h2>Essential Medical <span class="serif-italic">Services</span></h2>
            <p>Reliable, patient-focused medical and inpatient facilities operating with 24/7 readiness in Srikakulam.</p>
        </div>

        <!-- Full Interactive Services Showcase Grid -->
        <div class="services-showcase-grid">
            {services_grid_items}
        </div>

        <div style="margin-top: 3.5rem;">
            <div class="section-eyebrow" style="text-align:center; margin-bottom: 0.5rem;">
                <span class="eyebrow-dot"></span> QUICK NAVIGATION
            </div>
            <h3 style="text-align:center; font-size:1.45rem; margin-bottom: 1.75rem; color:var(--text-dark);">Browse All Services</h3>
            <div class="carousel-container animate-up">
                <button class="carousel-btn left-btn" onclick="scrollCarousel('services-page-carousel', -1)" aria-label="Scroll Left">◀</button>
                <div class="carousel-track" id="services-page-carousel">
                    {services_carousel_items}
                </div>
                <button class="carousel-btn right-btn" onclick="scrollCarousel('services-page-carousel', 1)" aria-label="Scroll Right">▶</button>
            </div>
        </div>
    </section>
    '''

    services_html = set_meta(common_nav + services_body + page_footer, "Services | A1 Hospital", "services", "services.html")
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(services_html)
    print("[OK] Created services.html")

    # -------------------------------------------------------------
    # 2. BUILD DEPARTMENTS.HTML (Only 8 Real Departments from User's Photos)
    # -------------------------------------------------------------
    dept_grid_items = ""
    for d_id, d in DEPARTMENTS_DATA.items():
        doc_names = ", ".join([doc['name'] for doc in d['doctors']])
        dept_grid_items += f'''
        <a href="{d['file']}" class="dept-showcase-card animate-up" style="text-decoration:none; color:inherit; display:flex; flex-direction:column;">
            <div class="dept-showcase-header-box" style="height:150px; background:linear-gradient(135deg, #fdf5f3 0%, #faece9 100%); display:flex; align-items:center; justify-content:center; position:relative; border-bottom:1.5px solid var(--border-warm);">
                <div style="width:68px; height:68px; border-radius:18px; background:#ffffff; color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 8px 22px rgba(128,0,0,0.12);">
                    <i data-lucide="{d['icon']}" style="width:34px; height:34px;"></i>
                </div>
                <div style="position:absolute; bottom:10px; right:12px; background:rgba(255,255,255,0.92); font-size:0.75rem; font-weight:700; color:var(--primary-accent); padding:3px 12px; border-radius:12px; border:1px solid rgba(128,0,0,0.08);">
                    {d['tag']}
                </div>
            </div>
            <div class="dept-showcase-content">
                <span class="service-pill-tag">{d['tag']}</span>
                <h3>{d['title']}</h3>
                <p>{d['meaning']}</p>
                <div style="margin-top:auto; padding-top:0.8rem; border-top:1px solid var(--border-warm); display:flex; align-items:center; justify-content:space-between;">
                    <span style="font-size:0.82rem; color:var(--primary-accent); font-weight:700;"><i data-lucide="stethoscope" style="width:13px; vertical-align:middle;"></i> {doc_names}</span>
                    <span class="dept-card-cta"><span>Explore</span> <i data-lucide="arrow-right"></i></span>
                </div>
            </div>
        </a>'''

    dept_carousel_items = ""
    for d_id, d in DEPARTMENTS_DATA.items():
        dept_carousel_items += f'''
        <a href="{d['file']}" style="text-decoration:none; color:inherit; display:block;">
            <div class="dept-card-photo" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.8rem 1.4rem; background:var(--bg-surface); min-width:240px; height:180px; text-align:center;">
                <div class="card-icon-badge" style="width:54px; height:54px; margin-bottom:1rem;">
                    <i data-lucide="{d['icon']}"></i>
                </div>
                <div class="dept-info" style="border:none; padding:0; background:transparent;"><h3>{d['title']}</h3></div>
            </div>
        </a>'''

    departments_body = f'''
    {spacer}
    <section class="departments framed-section animate-up" style="margin-top: 1.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> CLINICAL SPECIALITIES
            </div>
            <h2>Our Specialized <span class="serif-italic">Clinical Departments</span></h2>
            <p>Authentic, expert medical care led by verified resident and visiting clinical specialists in Srikakulam.</p>
        </div>

        <!-- Full Interactive Departments Showcase Grid -->
        <div class="departments-showcase-grid">
            {dept_grid_items}
        </div>

        <div style="margin-top: 3.5rem;">
            <div class="section-eyebrow" style="text-align:center; margin-bottom: 0.5rem;">
                <span class="eyebrow-dot"></span> SPECIALITY CAROUSEL
            </div>
            <h3 style="text-align:center; font-size:1.45rem; margin-bottom: 1.75rem; color:var(--text-dark);">Browse All Departments</h3>
            <div class="carousel-container animate-up">
                <button class="carousel-btn left-btn" onclick="scrollCarousel('departments-page-carousel', -1)" aria-label="Scroll Left">◀</button>
                <div class="carousel-track" id="departments-page-carousel">
                    {dept_carousel_items}
                </div>
                <button class="carousel-btn right-btn" onclick="scrollCarousel('departments-page-carousel', 1)" aria-label="Scroll Right">▶</button>
            </div>
        </div>
    </section>
    '''

    departments_html = set_meta(common_nav + departments_body + page_footer, "Departments | A1 Hospital", "departments", "departments.html")
    with open('departments.html', 'w', encoding='utf-8') as f:
        f.write(departments_html)
    print("[OK] Created departments.html")

    # -------------------------------------------------------------
    # 3. BUILD ALL 5 DEDICATED SERVICE PAGES (Concise & Focused)
    # -------------------------------------------------------------
    for s_id, s in SERVICES_DATA.items():
        doc_lead = s['lead_doctor']
        
        # Highlights pills
        highlights_html = ""
        for hl in s['highlights']:
            highlights_html += f'''
            <li style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.6rem; color:var(--text-dark); font-weight:600; font-size:0.95rem;">
                <i data-lucide="check-circle-2" style="color:var(--primary-accent); width:18px; height:18px; flex-shrink:0;"></i>
                <span>{hl}</span>
            </li>'''

        # Other services carousel
        other_services_carousel = ""
        for other_id, other_s in SERVICES_DATA.items():
            if other_id == s_id:
                continue
            other_services_carousel += f'''
            <a href="{other_s['file']}" style="text-decoration:none; color:inherit; display:block;">
                <div class="dept-card-photo" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.8rem 1.4rem; background:var(--bg-surface); min-width:240px; height:180px; text-align:center;">
                    <div class="card-icon-badge" style="width:52px; height:52px; margin-bottom:0.85rem;">
                        <i data-lucide="{other_s['icon']}"></i>
                    </div>
                    <div class="dept-info" style="border:none; padding:0; background:transparent;"><h3>{other_s['title']}</h3></div>
                </div>
            </a>'''

        service_page_content = f'''
        {spacer}
        <section class="detail-page-wrapper framed-section animate-up">
            <!-- Breadcrumbs and Back Button -->
            <div class="detail-nav-header">
                <a href="services.html" class="detail-back-btn">
                    <i data-lucide="arrow-left"></i> <span>Back to All Services</span>
                </a>
                <div class="detail-crumbs">
                    <a href="index.html">Home</a>
                    <i data-lucide="chevron-right" style="width:14px;"></i>
                    <a href="services.html">Services</a>
                    <i data-lucide="chevron-right" style="width:14px;"></i>
                    <span class="active-crumb">{s['title']}</span>
                </div>
            </div>

            <!-- Hero Spotlight -->
            <div class="detail-hero-grid">
                <div class="detail-hero-info">
                    <div class="section-eyebrow">
                        <span class="eyebrow-dot"></span> {s['tag']}
                    </div>
                    <h1 class="detail-title">{s['title']}</h1>
                    
                    <!-- Meaning / Explanation -->
                    <div style="background:var(--bg-cream); border-left:4px solid var(--primary-accent); padding:1.25rem 1.4rem; border-radius:0 12px 12px 0; margin-bottom:1.5rem;">
                        <strong style="display:block; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.8px; color:var(--primary-accent); margin-bottom:0.35rem;">What This Service Means</strong>
                        <p style="margin:0; font-size:1.05rem; line-height:1.65; color:var(--text-charcoal);">{s['meaning']}</p>
                    </div>

                    <!-- Key Highlights List -->
                    <ul style="list-style:none; padding:0; margin:0 0 2rem 0;">
                        {highlights_html}
                    </ul>

                    <div class="detail-hero-actions">
                        <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('', '{s['title']}')">
                            <i data-lucide="calendar"></i> <span>Book an Appointment</span>
                        </a>
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp: {HOSPITAL_CONTACT['whatsapp_number']}</span>
                        </a>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="btn-emergency-call" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>Call: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                    </div>
                </div>

                <div class="detail-hero-visual">
                    <div class="detail-arch-frame" style="background:linear-gradient(145deg, #fdf5f3 0%, #f7e8e5 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; padding:2.5rem 2rem; text-align:center; position:relative;">
                        <div style="width:105px; height:105px; border-radius:50%; background:#ffffff; color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 12px 30px rgba(128,0,0,0.13); margin-bottom:1.5rem;">
                            <i data-lucide="{s['icon']}" style="width:48px; height:48px;"></i>
                        </div>
                        <div style="font-size:0.82rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:var(--primary-accent); margin-bottom:0.4rem;">A1 Hospital Srikakulam</div>
                        <h3 style="font-size:1.45rem; font-family:'Playfair Display', serif; color:var(--text-dark); margin:0 0 0.75rem 0;">{s['title']}</h3>
                        <span style="display:inline-block; font-size:0.8rem; font-weight:700; background:rgba(128,0,0,0.08); color:var(--primary-accent); padding:0.3rem 0.9rem; border-radius:20px;">{s['tag']}</span>
                        <div class="detail-floating-badge" style="position:absolute; bottom:20px; left:20px; right:20px; margin:0 auto; width:calc(100% - 40px);">
                            <div class="card-icon-badge" style="width:40px; height:40px; font-size:1.1rem; margin:0;">
                                <i data-lucide="{s['icon']}"></i>
                            </div>
                            <div>
                                <strong>{s['title']}</strong>
                                <span>A1 Hospital Srikakulam</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Related Doctor Details & Photo -->
            <div class="detail-doctor-spotlight animate-up" style="margin-top:2rem;">
                <div class="detail-doc-img-wrap" style="display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, #fdf8f5 0%, #f7ece6 100%);">
                    <div class="doctor-emblem-badge" style="width:68px; height:68px; margin:0;">
                        <i data-lucide="{s['icon']}"></i>
                    </div>
                </div>
                <div class="detail-doc-info">
                    <span class="detail-doc-badge">Associated Clinical Supervision</span>
                    <h3>{doc_lead['name']}</h3>
                    <div class="doc-qual">{doc_lead['qual']} · {doc_lead['title']}</div>
                    <p>Ensuring hospital medical protocols, patient safety, and immediate clinical oversight for this service facility.</p>
                    <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{doc_lead['name'].split('&')[0].strip()}', '{s['title']}')">
                        <i data-lucide="calendar"></i> <span>Book an Appointment with Doctor</span>
                    </a>
                </div>
            </div>

            <!-- Explore Other Services Carousel -->
            <div class="detail-explore-others">
                <div class="detail-explore-header">
                    <h3>Explore Other Hospital Services</h3>
                    <div class="explore-nav-arrows">
                        <button class="carousel-btn left-btn" onclick="scrollCarousel('other-services-carousel', -1)" aria-label="Previous">◀</button>
                        <button class="carousel-btn right-btn" onclick="scrollCarousel('other-services-carousel', 1)" aria-label="Next">▶</button>
                    </div>
                </div>
                <div class="carousel-track" id="other-services-carousel">
                    {other_services_carousel}
                </div>
            </div>
        </section>
        '''

        full_service_page = set_meta(common_nav + service_page_content + page_footer, f"{s['title']} | A1 Hospital", "service-detail", s['file'])
        with open(s['file'], 'w', encoding='utf-8') as f:
            f.write(full_service_page)
        print(f"[OK] Created {s['file']}")

    # -------------------------------------------------------------
    # 4. BUILD ALL 8 DEDICATED DEPARTMENT PAGES (Concise & Focused)
    # -------------------------------------------------------------
    for d_id, d in DEPARTMENTS_DATA.items():
        # Highlights pills
        highlights_html = ""
        for hl in d['highlights']:
            highlights_html += f'''
            <li style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.6rem; color:var(--text-dark); font-weight:600; font-size:0.95rem;">
                <i data-lucide="check-circle-2" style="color:var(--primary-accent); width:18px; height:18px; flex-shrink:0;"></i>
                <span>{hl}</span>
            </li>'''

        # Doctors cards for this department
        doctors_html = ""
        for doc in d['doctors']:
            if doc.get('image'):
                doc_img_or_avatar = f'''
                <div class="detail-doc-img-wrap">
                    <img src="{doc['image']}" alt="{doc['name']}">
                </div>'''
            else:
                doc_img_or_avatar = f'''
                <div class="detail-doc-img-wrap" style="display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, #fdf8f5 0%, #f7ece6 100%);">
                    <div class="doctor-emblem-badge" style="width:68px; height:68px; margin:0;">
                        <i data-lucide="{d.get('icon', 'stethoscope')}"></i>
                    </div>
                </div>'''
            doctors_html += f'''
            <div class="detail-doctor-spotlight animate-up" style="margin-top:1.5rem;">
                {doc_img_or_avatar}
                <div class="detail-doc-info">
                    <span class="detail-doc-badge">Verified Specialist Doctor</span>
                    <h3>{doc['name']}</h3>
                    <div class="doc-qual">{doc['qual']}</div>
                    <p style="font-weight:700; color:var(--text-dark);">{doc['title']}</p>
                    <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{doc['name']}', '{d['title']}')">
                        <i data-lucide="calendar"></i> <span>Book an Appointment with {doc['name']}</span>
                    </a>
                </div>
            </div>'''

        # Other departments carousel
        other_dept_carousel = ""
        for other_id, other_d in DEPARTMENTS_DATA.items():
            if other_id == d_id:
                continue
            other_dept_carousel += f'''
            <a href="{other_d['file']}" style="text-decoration:none; color:inherit; display:block;">
                <div class="dept-card-photo" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.8rem 1.4rem; background:var(--bg-surface); min-width:240px; height:180px; text-align:center;">
                    <div class="card-icon-badge" style="width:52px; height:52px; margin-bottom:0.85rem;">
                        <i data-lucide="{other_d['icon']}"></i>
                    </div>
                    <div class="dept-info" style="border:none; padding:0; background:transparent;"><h3>{other_d['title']}</h3></div>
                </div>
            </a>'''

        dept_page_content = f'''
        {spacer}
        <section class="detail-page-wrapper framed-section animate-up">
            <!-- Breadcrumbs and Back Button -->
            <div class="detail-nav-header">
                <a href="departments.html" class="detail-back-btn">
                    <i data-lucide="arrow-left"></i> <span>Back to All Departments</span>
                </a>
                <div class="detail-crumbs">
                    <a href="index.html">Home</a>
                    <i data-lucide="chevron-right" style="width:14px;"></i>
                    <a href="departments.html">Departments</a>
                    <i data-lucide="chevron-right" style="width:14px;"></i>
                    <span class="active-crumb">{d['title']}</span>
                </div>
            </div>

            <!-- Hero Spotlight -->
            <div class="detail-hero-grid">
                <div class="detail-hero-info">
                    <div class="section-eyebrow">
                        <span class="eyebrow-dot"></span> {d['tag']}
                    </div>
                    <h1 class="detail-title">{d['title']}</h1>
                    
                    <!-- Meaning / Explanation -->
                    <div style="background:var(--bg-cream); border-left:4px solid var(--primary-accent); padding:1.25rem 1.4rem; border-radius:0 12px 12px 0; margin-bottom:1.5rem;">
                        <strong style="display:block; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.8px; color:var(--primary-accent); margin-bottom:0.35rem;">What This Department Means</strong>
                        <p style="margin:0; font-size:1.05rem; line-height:1.65; color:var(--text-charcoal);">{d['meaning']}</p>
                    </div>

                    <!-- Key Highlights List -->
                    <ul style="list-style:none; padding:0; margin:0 0 2rem 0;">
                        {highlights_html}
                    </ul>

                    <div class="detail-hero-actions">
                        <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{d['doctors'][0]['name']}', '{d['title']}')">
                            <i data-lucide="calendar"></i> <span>Book an Appointment</span>
                        </a>
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp: {HOSPITAL_CONTACT['whatsapp_number']}</span>
                        </a>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="btn-emergency-call" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>Call: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                    </div>
                </div>

                <div class="detail-hero-visual">
                    <div class="detail-arch-frame" style="background:linear-gradient(145deg, #fdf5f3 0%, #f7e8e5 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; padding:2.5rem 2rem; text-align:center; position:relative;">
                        <div style="width:105px; height:105px; border-radius:50%; background:#ffffff; color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 12px 30px rgba(128,0,0,0.13); margin-bottom:1.5rem;">
                            <i data-lucide="{d['icon']}" style="width:48px; height:48px;"></i>
                        </div>
                        <div style="font-size:0.82rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:var(--primary-accent); margin-bottom:0.4rem;">A1 Hospital Srikakulam</div>
                        <h3 style="font-size:1.45rem; font-family:'Playfair Display', serif; color:var(--text-dark); margin:0 0 0.75rem 0;">{d['title']}</h3>
                        <span style="display:inline-block; font-size:0.8rem; font-weight:700; background:rgba(128,0,0,0.08); color:var(--primary-accent); padding:0.3rem 0.9rem; border-radius:20px;">{d['tag']}</span>
                        <div class="detail-floating-badge" style="position:absolute; bottom:20px; left:20px; right:20px; margin:0 auto; width:calc(100% - 40px);">
                            <div class="card-icon-badge" style="width:40px; height:40px; font-size:1.1rem; margin:0;">
                                <i data-lucide="{d['icon']}"></i>
                            </div>
                            <div>
                                <strong>{d['title']}</strong>
                                <span>A1 Hospital Srikakulam</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Related Doctor(s) Details & Photo -->
            <div style="margin-top:2.5rem;">
                <div class="section-eyebrow" style="margin-bottom:0.75rem;">
                    <span class="eyebrow-dot"></span> SPECIALIST DOCTOR DETAILS
                </div>
                <h2 style="font-size:1.8rem; color:var(--text-dark); margin-bottom:1.5rem;">Consult Our <span class="serif-italic">Department Doctors</span></h2>
                {doctors_html}
            </div>

            <!-- Explore Other Departments Carousel -->
            <div class="detail-explore-others">
                <div class="detail-explore-header">
                    <h3>Explore Other Clinical Departments</h3>
                    <div class="explore-nav-arrows">
                        <button class="carousel-btn left-btn" onclick="scrollCarousel('other-dept-carousel', -1)" aria-label="Previous">◀</button>
                        <button class="carousel-btn right-btn" onclick="scrollCarousel('other-dept-carousel', 1)" aria-label="Next">▶</button>
                    </div>
                </div>
                <div class="carousel-track" id="other-dept-carousel">
                    {other_dept_carousel}
                </div>
            </div>
        </section>
        '''

        full_dept_page = set_meta(common_nav + dept_page_content + page_footer, f"{d['title']} | A1 Hospital", "department-detail", d['file'])
        with open(d['file'], 'w', encoding='utf-8') as f:
            f.write(full_dept_page)
        print(f"[OK] Created {d['file']}")

    # -------------------------------------------------------------
    # 5. BUILD DOCTORS.HTML (Verified Doctors from User's Photos)
    # -------------------------------------------------------------
    doc_cards_html = ""
    for doc in DOCTORS_DATA:
        is_founder = "Founder" in doc['title']
        is_senior_specialist = doc['id'] in ['dr-g-prameela', 'dr-co-founder-wife'] or "Senior" in doc['title']
        if doc.get('image'):
            badge_title = "FOUNDER" if is_founder else ("★ SENIOR SPECIALIST" if is_senior_specialist else "")
            badge_bg = "linear-gradient(135deg, var(--primary-accent), var(--primary-red))" if is_founder else "linear-gradient(135deg, #b8860b 0%, #800000 100%)"
            badge_html = f'''<div style="position:absolute; top:12px; right:12px; background:{badge_bg}; color:#fff; font-size:0.72rem; font-weight:700; padding:4px 11px; border-radius:20px; box-shadow:0 4px 12px rgba(128,0,0,0.28); text-transform:uppercase; letter-spacing:0.5px;">{badge_title}</div>''' if badge_title else ""
            img_pos = "object-position: top center;"
            img_or_avatar = f'''
            <div style="height:270px; width:100%; overflow:hidden; position:relative; background:#fff5f2;">
                <img src="{doc['image']}" alt="{doc['name']}" style="width:100%; height:100%; object-fit:cover; {img_pos} transition:transform 0.5s ease;">
                {badge_html}
                <div style="position:absolute; bottom:12px; left:12px; background:rgba(255,255,255,0.92); backdrop-filter:blur(8px); padding:0.25rem 0.75rem; border-radius:20px; font-size:0.75rem; font-weight:700; color:var(--primary-accent); border:1px solid rgba(128,0,0,0.08);">
                    {doc['dept']}
                </div>
            </div>'''
        else:
            icon_name = doc.get('icon', 'stethoscope')
            clean_title = doc['title'].split('(')[0].strip()
            img_or_avatar = f'''
            <div class="doctor-avatar-header">
                <div class="doctor-emblem-badge">
                    <i data-lucide="{icon_name}"></i>
                </div>
                <div class="doctor-avatar-title">{clean_title}</div>
                <div class="doctor-dept-pill">{doc['dept']}</div>
            </div>'''

        card_custom_id = ' id="card-dr-prameela"' if is_senior_specialist else ''
        card_border_style = 'border: 2px solid rgba(184,134,11,0.35); box-shadow: 0 8px 24px rgba(184,134,11,0.08);' if is_senior_specialist else ('border: 2px solid rgba(128,0,0,0.22);' if is_founder else 'border: 1.5px solid var(--border-warm);')

        doc_cards_html += f'''
        <div class="doctor-card animate-up"{card_custom_id} style="display:flex; flex-direction:column; background:var(--bg-surface); border-radius:var(--radius-lg); {card_border_style} overflow:hidden; box-shadow:var(--shadow-sm); transition:var(--transition-bounce);">
            {img_or_avatar}
            <div style="padding:1.6rem; display:flex; flex-direction:column; flex:1;">
                <h3 style="font-size:1.3rem; margin:0 0 0.35rem 0; color:var(--text-dark);">{doc['name']}</h3>
                <div style="font-size:0.88rem; color:var(--primary-accent); font-weight:700; margin-bottom:0.35rem;">{doc['qual']}</div>
                <div style="font-size:0.82rem; font-weight:600; color:var(--text-charcoal); margin-bottom:0.85rem;">{doc['title']}</div>
                <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6; margin-bottom:1.4rem; flex:1;">{doc['desc']}</p>
                <a href="#appointment" class="btn-primary small" onclick="openAppointmentModal('{doc['name']}', '{doc['dept']}')" style="margin-top:auto; width:100%; justify-content:center;">
                    <i data-lucide="calendar"></i> <span>Book an Appointment</span>
                </a>
            </div>
        </div>'''

    doctors_body = f'''
    {spacer}
    <section class="doctors framed-section animate-up" style="margin-top:1.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> VERIFIED MEDICAL COUNCIL
            </div>
            <h2>Meet Our <span class="serif-italic">Specialist Doctors</span></h2>
            <p>Our dedicated team of renowned clinicians, pediatricians, and surgeons serving Srikakulam with clinical mastery.</p>
        </div>

        <div class="doctors-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2.25rem; margin-top:2.5rem;">
            {doc_cards_html}
        </div>
    </section>
    '''

    doctors_html = set_meta(common_nav + doctors_body + page_footer, "Doctors | A1 Hospital", "doctors", "doctors.html")
    with open('doctors.html', 'w', encoding='utf-8') as f:
        f.write(doctors_html)
    print("[OK] Created doctors.html")

    # -------------------------------------------------------------
    # 6. ROUTER PAGES (service-detail.html & department-detail.html)
    # -------------------------------------------------------------
    router_script = '''
    <script>
        const params = new URLSearchParams(window.location.search);
        const hash = window.location.hash ? window.location.hash.replace('#', '').replace('service-', '').replace('dept-', '') : '';
        const id = params.get('id') || hash || 'beds';
        const targetMap = {
            'beds': 'service-beds.html',
            'emergency': 'service-emergency.html',
            'pharmacy': 'service-pharmacy.html',
            'ambulance': 'service-ambulance.html',
            'icu': 'service-icu.html'
        };
        const dest = targetMap[id] || 'service-beds.html';
        window.location.replace(dest);
    </script>
    '''
    with open('service-detail.html', 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Loading Service Details...</title>{router_script}</head><body><p style="text-align:center; padding:3rem; font-family:sans-serif;">Redirecting to service details...</p></body></html>')

    dept_router_script = '''
    <script>
        const params = new URLSearchParams(window.location.search);
        const hash = window.location.hash ? window.location.hash.replace('#', '').replace('dept-', '') : '';
        const id = params.get('id') || hash || 'pediatrics';
        const targetMap = {
            'pediatrics': 'department-pediatrics.html',
            'obstetrics': 'department-obstetrics.html',
            'orthopedics': 'department-orthopedics.html',
            'generalmedicine': 'department-generalmedicine.html',
            'generalsurgery': 'department-generalsurgery.html',
            'nephrology': 'department-nephrology.html',
            'urology': 'department-urology.html',
            'ophthalmology': 'department-ophthalmology.html',
            'oncology': 'department-oncology.html'
        };
        const dest = targetMap[id] || 'department-pediatrics.html';
        window.location.replace(dest);
    </script>
    '''
    with open('department-detail.html', 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Loading Department Details...</title>{dept_router_script}</head><body><p style="text-align:center; padding:3rem; font-family:sans-serif;">Redirecting to department details...</p></body></html>')

    print("\nALL PAGES SUCCESSFULLY CREATED!")

if __name__ == '__main__':
    build_all_pages()
