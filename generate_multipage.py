import os
import re
from multipage_data import SERVICES_DATA, DEPARTMENTS_DATA

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

    def set_meta(html_str, title, page_name):
        res = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_str)
        res = re.sub(r'<body[^>]*>', f'<body data-page="{page_name}">', res)
        return res

    spacer = '\n    <div style="margin-top: 1.5rem;"></div>\n'

    # -------------------------------------------------------------
    # 1. BUILD SERVICES.HTML
    # -------------------------------------------------------------
    services_grid_items = ""
    for s_id, s in SERVICES_DATA.items():
        services_grid_items += f'''
        <a href="{s['file']}" class="service-showcase-card animate-up" style="text-decoration:none; color:inherit; display:flex; flex-direction:column;">
            <div class="service-showcase-img-wrap">
                <img src="{s['image']}" alt="{s['title']}">
                <div class="service-showcase-badge">
                    <i data-lucide="{s['icon']}"></i>
                </div>
            </div>
            <div class="service-showcase-content">
                <span class="service-pill-tag">{s['badge_title']}</span>
                <h3>{s['title']}</h3>
                <p>{s['subtitle']}</p>
                <div class="service-card-cta">
                    <span>Explore Service Details</span>
                    <i data-lucide="arrow-right"></i>
                </div>
            </div>
        </a>'''

    services_carousel_items = ""
    for s_id, s in SERVICES_DATA.items():
        services_carousel_items += f'''
        <a href="{s['file']}" style="text-decoration:none; color:inherit; display:block;">
            <div class="dept-card-photo">
                <img src="{s['image']}" alt="{s['title']}">
                <div class="dept-info"><h3>{s['title']}</h3></div>
            </div>
        </a>'''

    services_body = f'''
    {spacer}
    <section class="services framed-section animate-up" style="margin-top: 1.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> WORLD-CLASS MEDICAL FACILITIES
            </div>
            <h2>Our Comprehensive <span class="serif-italic">Services</span></h2>
            <p>Exceptional medical and surgical facilities with advanced technology, providing compassionate comfort and care in Srikakulam.</p>
        </div>

        <!-- Full Interactive Services Showcase Grid -->
        <div class="services-showcase-grid">
            {services_grid_items}
        </div>

        <div style="margin-top: 3.5rem;">
            <div class="section-eyebrow" style="text-align:center; margin-bottom: 0.5rem;">
                <span class="eyebrow-dot"></span> QUICK NAVIGATION CAROUSEL
            </div>
            <h3 style="text-align:center; font-size:1.45rem; margin-bottom: 1.75rem; color:var(--text-dark);">Browse All Facility Wings</h3>
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

    services_html = set_meta(common_nav + services_body + common_footer, "Services | A1 Hospital", "services")
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(services_html)
    print("[OK] Created services.html")

    # -------------------------------------------------------------
    # 2. BUILD DEPARTMENTS.HTML
    # -------------------------------------------------------------
    dept_grid_items = ""
    for d_id, d in DEPARTMENTS_DATA.items():
        dept_grid_items += f'''
        <a href="{d['file']}" class="dept-showcase-card animate-up" style="text-decoration:none; color:inherit; display:flex; flex-direction:column;">
            <div class="dept-showcase-img-wrap">
                <img src="{d['image']}" alt="{d['title']}">
                <div class="dept-showcase-badge">
                    <i data-lucide="{d['icon']}"></i>
                </div>
            </div>
            <div class="dept-showcase-content">
                <span class="service-pill-tag">{d['badge_title']}</span>
                <h3>{d['title']}</h3>
                <p>{d['subtitle']}</p>
                <div class="dept-card-cta">
                    <span>Explore Speciality</span>
                    <i data-lucide="arrow-right"></i>
                </div>
            </div>
        </a>'''

    dept_carousel_items = ""
    for d_id, d in DEPARTMENTS_DATA.items():
        dept_carousel_items += f'''
        <a href="{d['file']}" style="text-decoration:none; color:inherit; display:block;">
            <div class="dept-card-photo">
                <img src="{d['image']}" alt="{d['title']}">
                <div class="dept-info"><h3>{d['title']}</h3></div>
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
            <p>Comprehensive medical, pediatric, and surgical expertise tailored to your clinical needs in Srikakulam.</p>
        </div>

        <!-- Full Interactive Departments Showcase Grid -->
        <div class="departments-showcase-grid">
            {dept_grid_items}
        </div>

        <div style="margin-top: 3.5rem;">
            <div class="section-eyebrow" style="text-align:center; margin-bottom: 0.5rem;">
                <span class="eyebrow-dot"></span> SPECIALITY CAROUSEL
            </div>
            <h3 style="text-align:center; font-size:1.45rem; margin-bottom: 1.75rem; color:var(--text-dark);">Browse All 14 Specialities</h3>
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

    departments_html = set_meta(common_nav + departments_body + common_footer, "Departments | A1 Hospital", "departments")
    with open('departments.html', 'w', encoding='utf-8') as f:
        f.write(departments_html)
    print("[OK] Created departments.html")

    # -------------------------------------------------------------
    # 3. BUILD ALL 8 DEDICATED SERVICE PAGES
    # -------------------------------------------------------------
    for s_id, s in SERVICES_DATA.items():
        # Capability cards
        cap_cards_html = ""
        for title, desc, icon in s['capabilities']:
            cap_cards_html += f'''
            <div class="detail-cap-card">
                <div class="cap-icon-box"><i data-lucide="{icon}"></i></div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>'''

        # Amenities chips
        amenities_chips_html = ""
        for amen in s['amenities']:
            amenities_chips_html += f'''
            <span class="detail-condition-chip">
                <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i>
                <span>{amen}</span>
            </span>'''

        # Stats pills
        stats_pills_html = ""
        for stat_text, stat_icon in s['stats']:
            stats_pills_html += f'''
            <div class="detail-stat-pill">
                <i data-lucide="{stat_icon}" style="width:15px; color:var(--primary-accent);"></i>
                <span>{stat_text}</span>
            </div>'''

        # Other services carousel
        other_services_carousel = ""
        for other_id, other_s in SERVICES_DATA.items():
            if other_id == s_id:
                continue
            other_services_carousel += f'''
            <a href="{other_s['file']}" style="text-decoration:none; color:inherit; display:block;">
                <div class="dept-card-photo">
                    <img src="{other_s['image']}" alt="{other_s['title']}">
                    <div class="dept-info"><h3>{other_s['title']}</h3></div>
                </div>
            </a>'''

        # Doctor profile
        doc = s['doctor']
        doctor_html = f'''
        <div class="detail-doctor-spotlight animate-up">
            <div class="detail-doc-img-wrap">
                <img src="{doc['img']}" alt="{doc['name']}" onerror="this.src='https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'">
            </div>
            <div class="detail-doc-info">
                <span class="detail-doc-badge">Clinical Leadership</span>
                <h3>{doc['name']}</h3>
                <div class="doc-qual">{doc['qual']}</div>
                <p>{doc['desc']}</p>
                <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{doc['name']}', '{doc['dept']}')">
                    <i data-lucide="calendar"></i> <span>Book Consultation with Specialist</span>
                </a>
            </div>
        </div>'''

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
                        <span class="eyebrow-dot"></span> {s['eyebrow']}
                    </div>
                    <h1 class="detail-title">{s['title_formatted']}</h1>
                    <p class="detail-lead">{s['subtitle']}</p>
                    
                    <div class="detail-quick-stats">
                        {stats_pills_html}
                    </div>

                    <div class="detail-hero-actions">
                        <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('', '{s['title']}')">
                            <i data-lucide="calendar"></i> <span>Book Consultation</span>
                        </a>
                        <a href="tel:08942228234" class="btn-emergency-call" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>24/7 Desk: 08942-228234</span>
                        </a>
                        <a href="https://wa.me/919193774444" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp Desk</span>
                        </a>
                    </div>
                </div>

                <div class="detail-hero-visual">
                    <div class="detail-arch-frame">
                        <img src="{s['image']}" alt="{s['title']}">
                        <div class="detail-floating-badge">
                            <div class="card-icon-badge" style="width:40px; height:40px; font-size:1.1rem; margin:0;">
                                <i data-lucide="{s['icon']}"></i>
                            </div>
                            <div>
                                <strong>{s['badge_title']}</strong>
                                <span>{s['badge_sub']}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- In-Depth Overview -->
            <div class="detail-content-block">
                <div class="detail-block-header">
                    <div class="section-eyebrow"><span class="eyebrow-dot"></span> IN-DEPTH FACILITY PROFILE</div>
                    <h2>Clinical Readiness &amp; <span class="serif-italic">Patient Standards</span></h2>
                </div>
                <div class="detail-text-narrative">
                    <p class="lead-paragraph">{s['lead_para']}</p>
                    <p>{s['body_para']}</p>
                </div>

                <!-- 4 Capability Cards -->
                <div class="detail-capabilities-grid">
                    {cap_cards_html}
                </div>
            </div>

            <!-- Amenities & Highlights -->
            <div class="detail-chips-section animate-up">
                <div class="detail-chips-header">
                    <i data-lucide="check-circle-2" style="color:var(--primary-accent); width:22px; height:22px;"></i>
                    <h3>{s['amenities_title']}</h3>
                </div>
                <div class="detail-chips-cloud">
                    {amenities_chips_html}
                </div>
            </div>

            <!-- Doctor Spotlight -->
            {doctor_html}

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

        full_service_page = set_meta(common_nav + service_page_content + common_footer, f"{s['title']} | A1 Hospital", "service-detail")
        with open(s['file'], 'w', encoding='utf-8') as f:
            f.write(full_service_page)
        print(f"[OK] Created {s['file']}")

    # -------------------------------------------------------------
    # 4. BUILD ALL 14 DEDICATED DEPARTMENT PAGES
    # -------------------------------------------------------------
    for d_id, d in DEPARTMENTS_DATA.items():
        # Capability cards
        cap_cards_html = ""
        for title, desc, icon in d['capabilities']:
            cap_cards_html += f'''
            <div class="detail-cap-card">
                <div class="cap-icon-box"><i data-lucide="{icon}"></i></div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>'''

        # Conditions / Amenities chips
        amenities_chips_html = ""
        for amen in d['amenities']:
            amenities_chips_html += f'''
            <span class="detail-condition-chip">
                <i data-lucide="activity" style="width:14px; color:var(--primary-accent);"></i>
                <span>{amen}</span>
            </span>'''

        # Stats pills
        stats_pills_html = ""
        for stat_text, stat_icon in d['stats']:
            stats_pills_html += f'''
            <div class="detail-stat-pill">
                <i data-lucide="{stat_icon}" style="width:15px; color:var(--primary-accent);"></i>
                <span>{stat_text}</span>
            </div>'''

        # Other departments carousel
        other_dept_carousel = ""
        for other_id, other_d in DEPARTMENTS_DATA.items():
            if other_id == d_id:
                continue
            other_dept_carousel += f'''
            <a href="{other_d['file']}" style="text-decoration:none; color:inherit; display:block;">
                <div class="dept-card-photo">
                    <img src="{other_d['image']}" alt="{other_d['title']}">
                    <div class="dept-info"><h3>{other_d['title']}</h3></div>
                </div>
            </a>'''

        # Doctor profile
        doc = d['doctor']
        doctor_html = f'''
        <div class="detail-doctor-spotlight animate-up">
            <div class="detail-doc-img-wrap">
                <img src="{doc['img']}" alt="{doc['name']}" onerror="this.src='https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'">
            </div>
            <div class="detail-doc-info">
                <span class="detail-doc-badge">Lead Specialist</span>
                <h3>{doc['name']}</h3>
                <div class="doc-qual">{doc['qual']}</div>
                <p>{doc['desc']}</p>
                <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{doc['name']}', '{doc['dept']}')">
                    <i data-lucide="calendar"></i> <span>Book Consultation with Dr. {doc['name'].split()[1] if len(doc['name'].split()) > 1 else doc['name']}</span>
                </a>
            </div>
        </div>'''

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
                        <span class="eyebrow-dot"></span> {d['eyebrow']}
                    </div>
                    <h1 class="detail-title">{d['title_formatted']}</h1>
                    <p class="detail-lead">{d['subtitle']}</p>
                    
                    <div class="detail-quick-stats">
                        {stats_pills_html}
                    </div>

                    <div class="detail-hero-actions">
                        <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('{doc['name']}', '{d['title']}')">
                            <i data-lucide="calendar"></i> <span>Book Appointment</span>
                        </a>
                        <a href="tel:08942228234" class="btn-emergency-call" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>24/7 Helpline: 08942-228234</span>
                        </a>
                        <a href="https://wa.me/919193774444" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp Help Desk</span>
                        </a>
                    </div>
                </div>

                <div class="detail-hero-visual">
                    <div class="detail-arch-frame">
                        <img src="{d['image']}" alt="{d['title']}">
                        <div class="detail-floating-badge">
                            <div class="card-icon-badge" style="width:40px; height:40px; font-size:1.1rem; margin:0;">
                                <i data-lucide="{d['icon']}"></i>
                            </div>
                            <div>
                                <strong>{d['badge_title']}</strong>
                                <span>{d['badge_sub']}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- In-Depth Overview -->
            <div class="detail-content-block">
                <div class="detail-block-header">
                    <div class="section-eyebrow"><span class="eyebrow-dot"></span> CLINICAL SCOPE &amp; CARE</div>
                    <h2>Specialized Medical Care &amp; <span class="serif-italic">Procedures</span></h2>
                </div>
                <div class="detail-text-narrative">
                    <p class="lead-paragraph">{d['lead_para']}</p>
                    <p>{d['body_para']}</p>
                </div>

                <!-- 4 Capability Cards -->
                <div class="detail-capabilities-grid">
                    {cap_cards_html}
                </div>
            </div>

            <!-- Conditions Managed -->
            <div class="detail-chips-section animate-up">
                <div class="detail-chips-header">
                    <i data-lucide="check-circle-2" style="color:var(--primary-accent); width:22px; height:22px;"></i>
                    <h3>{d['amenities_title']}</h3>
                </div>
                <div class="detail-chips-cloud">
                    {amenities_chips_html}
                </div>
            </div>

            <!-- Doctor Spotlight -->
            {doctor_html}

            <!-- Explore Other Departments Carousel -->
            <div class="detail-explore-others">
                <div class="detail-explore-header">
                    <h3>Explore Other Clinical Specialities</h3>
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

        full_dept_page = set_meta(common_nav + dept_page_content + common_footer, f"{d['title']} | A1 Hospital", "department-detail")
        with open(d['file'], 'w', encoding='utf-8') as f:
            f.write(full_dept_page)
        print(f"[OK] Created {d['file']}")

    # -------------------------------------------------------------
    # 5. DYNAMIC ROUTER PAGES (service-detail.html & department-detail.html)
    # -------------------------------------------------------------
    router_script = '''
    <script>
        const params = new URLSearchParams(window.location.search);
        const hash = window.location.hash ? window.location.hash.replace('#', '').replace('service-', '').replace('dept-', '') : '';
        const id = params.get('id') || hash || 'beds';
        const targetMap = {
            'beds': 'service-beds.html',
            'emergency': 'service-emergency.html',
            'equipment': 'service-equipment.html',
            'doctors': 'service-doctors.html',
            'pharmacy': 'service-pharmacy.html',
            'ambulance': 'service-ambulance.html',
            'bloodbank': 'service-bloodbank.html',
            'icu': 'service-icu.html'
        };
        const dest = targetMap[id] || 'service-beds.html';
        window.location.replace(dest);
    </script>
    '''
    with open('service-detail.html', 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Loading Service Details...</title>{router_script}</head><body><p style="text-align:center; padding:3rem; font-family:sans-serif;">Redirecting to service details...</p></body></html>')
    print("[OK] Created service-detail.html router")

    dept_router_script = '''
    <script>
        const params = new URLSearchParams(window.location.search);
        const hash = window.location.hash ? window.location.hash.replace('#', '').replace('dept-', '') : '';
        const id = params.get('id') || hash || 'cardiology';
        const targetMap = {
            'cardiology': 'department-cardiology.html',
            'neurology': 'department-neurology.html',
            'pediatrics': 'department-pediatrics.html',
            'orthopedics': 'department-orthopedics.html',
            'generalsurgery': 'department-generalsurgery.html',
            'radiology': 'department-radiology.html',
            'obg': 'department-obg.html',
            'pulmonology': 'department-pulmonology.html',
            'dermatology': 'department-dermatology.html',
            'urology': 'department-urology.html',
            'criticalcare': 'department-criticalcare.html',
            'oncology': 'department-oncology.html',
            'nephrology': 'department-nephrology.html',
            'ophthalmology': 'department-ophthalmology.html'
        };
        const dest = targetMap[id] || 'department-cardiology.html';
        window.location.replace(dest);
    </script>
    '''
    with open('department-detail.html', 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Loading Department Details...</title>{dept_router_script}</head><body><p style="text-align:center; padding:3rem; font-family:sans-serif;">Redirecting to department details...</p></body></html>')
    print("[OK] Created department-detail.html router")

    # 6. BUILD DOCTORS.HTML
    doctors_match = re.search(r'(<section id="doctors".*?</section>)\s*(?:<!--.*?-->\s*)?<section id="contact"', html, re.DOTALL)
    if doctors_match:
        doc_html = common_nav + spacer + doctors_match.group(1) + common_footer
        doc_html = set_meta(doc_html, 'Doctors | A1 Hospital', 'doctors')
        doc_html = doc_html.replace('id="home-doctors-view"', 'id="home-doctors-view" style="display: none;"')
        doc_html = doc_html.replace('id="all-doctors-view" style="display: none;"', 'id="all-doctors-view"')
        doc_html = re.sub(r'<div[^>]*id="view-all-docs-btn-container"[^>]*>.*?</div>', '', doc_html, flags=re.DOTALL)
        with open('doctors.html', 'w', encoding='utf-8') as f:
            f.write(doc_html)
        print("[OK] Created doctors.html")

    print("\nALL PAGES SUCCESSFULLY CREATED!")

if __name__ == '__main__':
    build_all_pages()
