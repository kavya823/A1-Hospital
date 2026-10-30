import os
import re
import urllib.parse
from multipage_data import SERVICES_DATA, DEPARTMENTS_DATA, DOCTORS_DATA, HOSPITAL_CONTACT

BLOG_POSTS = [
    {
        "id": "childhood-vaccination-guide",
        "category": "pediatrics",
        "category_name": "Pediatrics & Child Health",
        "title": "Essential Child Immunization & Vaccination Milestones: A Parent's Guide",
        "read_time": "5 min read",
        "date": "Oct 2026",
        "icon": "baby",
        "excerpt": "Timely vaccinations protect infants from life-threatening infections. Learn about the essential immunization schedule from birth through age five.",
        "full_content": """
        <h4>Why Childhood Vaccination is Critical</h4>
        <p>Vaccination is one of the most effective medical safeguards developed to protect infants and children from serious preventable illnesses such as polio, hepatitis B, rotavirus, measles, and diphtheria. In the early months of life, a baby’s immune system is still developing, making prompt adherence to the pediatric immunization calendar vital.</p>
        <h4>Core Immunization Milestones</h4>
        <ul>
            <li><strong>At Birth:</strong> BCG, OPV-0, and Hepatitis B birth dose.</li>
            <li><strong>6, 10, &amp; 14 Weeks:</strong> Pentavalent vaccine, Rotavirus, Inactivated Polio Vaccine (IPV), and PCV.</li>
            <li><strong>9 to 12 Months:</strong> Measles &amp; Rubella (MR-1), Vitamin A, and JE (if endemic).</li>
            <li><strong>16 to 24 Months:</strong> DPT booster and MR-2.</li>
            <li><strong>5 Years:</strong> DPT-2 booster for sustained immunity before starting school.</li>
        </ul>
        <h4>Managing Mild Post-Vaccine Reactions</h4>
        <p>It is normal for children to experience slight fever, mild fussiness, or localized redness at the injection site. Simple comfort measures, cold compresses, and doctor-prescribed pediatric paracetamol drops will keep your child comfortable. Always consult our pediatric outpatient department for customized immunization schedules.</p>
        """
    },
    {
        "id": "understanding-ivf-fertility",
        "category": "obstetrics",
        "category_name": "Women's Health & IVF",
        "title": "Understanding IVF & Modern Reproductive Solutions: A Compassionate Overview",
        "read_time": "6 min read",
        "date": "Oct 2026",
        "icon": "heart-pulse",
        "excerpt": "Fertility challenges are common and treatable. Discover modern reproductive techniques including ovulation tracking, IUI, and IVF.",
        "full_content": """
        <h4>The Evolution of Reproductive Medicine</h4>
        <p>Infertility affects approximately one in six couples worldwide. With modern clinical reproductive medicine, couples have access to scientific, evidence-based diagnostic pathways that identify underlying factors early and personalize treatment.</p>
        <h4>When Should Couples Seek Fertility Evaluation?</h4>
        <p>Couples under 35 who have been attempting conception for 12 months (or 6 months if 35 or older) are advised to undergo a baseline reproductive evaluation. This includes hormone profiling, pelvic ultrasonography, tubal patency checks, and semen analysis.</p>
        <h4>Treatment Steps: From Basic to Advanced</h4>
        <ul>
            <li><strong>Ovulation Induction &amp; Timed Intercourse:</strong> Safe medications to stimulate natural egg release.</li>
            <li><strong>Intrauterine Insemination (IUI):</strong> Concentrated, washed sperm placed into the uterus around ovulation.</li>
            <li><strong>In-Vitro Fertilization (IVF):</strong> Controlled stimulation, egg retrieval, fertilization in a sterile embryology setting, and embryo transfer.</li>
            <li><strong>Minimal Access Laparoscopy (FMAS):</strong> Correcting fibroids, endometriosis, and tubal blocks with minimal recovery time.</li>
        </ul>
        <p>Compassionate emotional support, lifestyle balance, and qualified clinical guidance make the journey to parenthood hopeful and achievable.</p>
        """
    },
    {
        "id": "joint-health-arthritis-mobility",
        "category": "orthopedics",
        "category_name": "Orthopedics & Joint Care",
        "title": "Preventing Knee Arthritis & Maintaining Joint Mobility After 40",
        "read_time": "4 min read",
        "date": "Oct 2026",
        "icon": "bone",
        "excerpt": "Protect your knees, spine, and joints with ergonomic daily habits, low-impact exercise, and early orthopedic evaluation.",
        "full_content": """
        <h4>Why Do Joints Deteriorate with Age?</h4>
        <p>Articular cartilage covers the ends of bones to provide smooth, frictionless movement. Over decades of repetitive impact, obesity, or injury, this cartilage can thin, causing stiffness, swelling, and localized pain known as osteoarthritis.</p>
        <h4>Actionable Steps for Lifelong Joint Health</h4>
        <ul>
            <li><strong>Weight Management:</strong> Every kilogram of body weight reduced removes roughly 4 kilograms of mechanical pressure from your knee joints during walking.</li>
            <li><strong>Low-Impact Quadriceps Strengthening:</strong> Swimming, stationary cycling, and straight-leg raises strengthen the thigh muscles that absorb knee shock.</li>
            <li><strong>Vitamin D3 &amp; Calcium Balance:</strong> Bone density directly supports joint cartilage longevity. Periodic checks prevent accelerated bone loss.</li>
            <li><strong>Avoid Prolonged Squatting &amp; Cross-Legged Sitting:</strong> If you experience early knee crepitus (grinding sound), avoid deep knee flexion on hard floors.</li>
        </ul>
        <p>If knee pain interrupts sleep or everyday walking, early orthopedic assessment and modern physiotherapy can prevent the need for advanced joint replacement.</p>
        """
    },
    {
        "id": "golden-hour-emergency-care",
        "category": "emergency",
        "category_name": "Emergency & Trauma Care",
        "title": "The Golden Hour: Why Rapid Response in Emergencies Saves Lives",
        "read_time": "5 min read",
        "date": "Oct 2026",
        "icon": "clock",
        "excerpt": "In medical crises like heart attacks, stroke, or road trauma, the first 60 minutes determine patient recovery. Know what immediate steps to take.",
        "full_content": """
        <h4>What is the Medical 'Golden Hour'?</h4>
        <p>The Golden Hour refers to the critical window of time immediately following acute medical trauma, severe injury, or cardiac/stroke onset. Prompt medical intervention during this period dramatically increases survival rates and prevents permanent organ damage.</p>
        <h4>Recognizing Immediate Emergencies</h4>
        <ul>
            <li><strong>Cardiac Symptoms:</strong> Heavy chest pressure radiating to the jaw, left shoulder, or back accompanied by cold sweating and shortness of breath.</li>
            <li><strong>Stroke Warning Signs (FAST):</strong> Face drooping, Arm weakness, Slurred speech, Time to call emergency.</li>
            <li><strong>Severe Trauma &amp; Fractures:</strong> Profuse bleeding, head injury with disorientation, or inability to move a limb following an accident.</li>
        </ul>
        <h4>What to Do While Help is on the Way</h4>
        <p>Keep the patient calm, ensure their airway is clear, do not offer food or oral liquids, and call our 24/7 Emergency Casualty Reception at <strong>08942-228234</strong> immediately to dispatch ambulance transport and alert the trauma team.</p>
        """
    },
    {
        "id": "kidney-health-hydration-habits",
        "category": "nephrology",
        "category_name": "Nephrology & Renal Health",
        "title": "Protecting Your Kidneys: Hydration, Diet, & Kidney Stone Prevention",
        "read_time": "4 min read",
        "date": "Oct 2026",
        "icon": "filter",
        "excerpt": "Kidneys filter over 180 liters of blood every single day. Simple hydration and dietary discipline prevent kidney stone formation and renal strain.",
        "full_content": """
        <h4>The Vital Functions of Human Kidneys</h4>
        <p>Your kidneys filter waste products, balance blood pressure, regulate red blood cell production, and maintain critical electrolytes (sodium, potassium, calcium). Chronic dehydration and high salt intake put immense strain on the renal filtration units.</p>
        <h4>Preventing Kidney Stones &amp; Chronic Renal Stress</h4>
        <ul>
            <li><strong>Optimal Daily Hydration:</strong> Drink 2.5 to 3 liters of clean water daily. Your urine should remain pale clear rather than dark yellow.</li>
            <li><strong>Moderate Sodium Intake:</strong> Excessive dietary salt elevates urinary calcium excretion, triggering oxalate stone crystallization.</li>
            <li><strong>Manage Blood Sugar &amp; Blood Pressure:</strong> Diabetes and hypertension remain the two leading causes of chronic kidney disease (CKD) worldwide.</li>
            <li><strong>Avoid Self-Medicating with Painkillers:</strong> Over-the-counter NSAIDs taken habitually without prescription can cause acute tubular and kidney damage.</li>
        </ul>
        <p>Annual screening for serum creatinine and urine albumin is strongly recommended for anyone with diabetes or a family history of kidney disorders.</p>
        """
    },
    {
        "id": "adult-medicine-fevers-lifestyle",
        "category": "generalmedicine",
        "category_name": "General Medicine",
        "title": "Managing Seasonal Fevers, Diabetes & Hypertension: A Physician's Guide",
        "read_time": "5 min read",
        "date": "Oct 2026",
        "icon": "stethoscope",
        "excerpt": "Practical physician advice on managing chronic lifestyle conditions and safe protocols for dealing with acute seasonal viral fevers.",
        "full_content": """
        <h4>Combating Seasonal Viral &amp; Vector Fevers</h4>
        <p>During seasonal transitions, monsoon rains, and climate shifts, viral infections, dengue, and typhoid fevers spike. Hydration with oral electrolytes, complete bed rest, and avoiding self-medication are paramount. If fever persists past 48 hours or is accompanied by chills, vomiting, or rashes, seek laboratory blood counts immediately.</p>
        <h4>Managing Chronic Conditions (Diabetes &amp; BP)</h4>
        <ul>
            <li><strong>Regular Monitoring:</strong> Log fasting and post-prandial blood sugar levels as well as weekly resting blood pressure readings.</li>
            <li><strong>Consistent Medication:</strong> Never skip prescribed antihypertensives or insulin doses without clinical supervision.</li>
            <li><strong>Fiber-Rich Dietary Habits:</strong> Whole grains, green vegetables, and balanced portions prevent acute glycemic spikes.</li>
            <li><strong>Daily 30-Minute Aerobic Walking:</strong> Boosts natural insulin sensitivity and helps maintain healthy vascular elasticity.</li>
        </ul>
        <p>Our General Medicine department provides comprehensive outpatient physician evaluations and continuous inpatient supervision for adult health.</p>
        """
    }
]

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
                        <strong style="color: var(--text-dark); display: block; font-size: 0.95rem;">24/7 Hospital Reception</strong>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" style="color: var(--text-dark); text-decoration: none; font-size: 0.88rem; font-weight: 700;">{HOSPITAL_CONTACT['phone_1']}</a>, <a href="tel:{HOSPITAL_CONTACT['phone_2'].replace('-', '')}" style="color: var(--text-dark); text-decoration: none; font-size: 0.88rem; font-weight: 700;">{HOSPITAL_CONTACT['phone_2']}</a>
                    </div>
                </div>
            </div>

            <!-- Modern Hospital Reception & Patient Registration Desk Showcase -->
            <div class="reception-facility-card animate-up">
                <div class="reception-img-frame">
                    <img src="reception_desk.jpg" alt="A1 Hospital Reception and Patient Registration Desk">
                    <div class="reception-badge-pill">
                        <i data-lucide="clock"></i> 24/7 Patient Assistance
                    </div>
                </div>
                <div class="reception-facility-info">
                    <div class="section-eyebrow">
                        <span class="eyebrow-dot"></span> PATIENT ADMISSIONS &amp; ENQUIRIES
                    </div>
                    <h3>Hospital Reception &amp; Registration Desk</h3>
                    <p>Our modern reception and patient care desk is staffed 24 hours a day to welcome you, facilitate rapid outpatient registrations, assist with doctor appointments, and provide immediate inpatient admissions guidance.</p>
                    <div class="reception-quick-contact">
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="reception-phone-pill">
                            <i data-lucide="phone-call"></i>
                            <span>Desk Line 1: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                        <a href="tel:{HOSPITAL_CONTACT['phone_2'].replace('-', '')}" class="reception-phone-pill">
                            <i data-lucide="phone"></i>
                            <span>Desk Line 2: {HOSPITAL_CONTACT['phone_2']}</span>
                        </a>
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
    # 1. BUILD SERVICES.HTML (Purely Facility & Hospital Readiness - No Doctor Details)
    # -------------------------------------------------------------
    services_grid_items = ""
    for s_id, s in SERVICES_DATA.items():
        readiness_badge = s.get('readiness', '24/7 Available')
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
                    <span style="font-size:0.82rem; color:var(--primary-accent); font-weight:700;"><i data-lucide="shield-check" style="width:14px; vertical-align:middle;"></i> {readiness_badge}</span>
                    <span class="service-card-cta"><span>Explore Facility</span> <i data-lucide="arrow-right"></i></span>
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
    # 2. BUILD DEPARTMENTS.HTML (Authentic Specialities - No Doctor Names)
    # -------------------------------------------------------------
    dept_grid_items = ""
    for d_id, d in DEPARTMENTS_DATA.items():
        img_src = d.get('image') or 'dept_pediatrics.jpg'
        dept_grid_items += f'''
        <a href="{d['file']}" class="dept-showcase-card animate-up" style="text-decoration:none; color:inherit; display:flex; flex-direction:column; overflow:hidden; border-radius:var(--radius-lg); background:var(--bg-surface); border:1.5px solid var(--border-warm); box-shadow:var(--shadow-sm); transition:var(--transition-bounce);">
            <div class="dept-showcase-header-box" style="height:190px; position:relative; overflow:hidden; background:#fff5f2;">
                <img src="{img_src}" alt="{d['title']}" style="width:100%; height:100%; object-fit:cover; transition:transform 0.5s ease;">
                <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.45) 100%);"></div>
                <div style="position:absolute; top:12px; left:12px; width:40px; height:40px; border-radius:12px; background:rgba(255,255,255,0.92); backdrop-filter:blur(6px); color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
                    <i data-lucide="{d['icon']}" style="width:20px; height:20px;"></i>
                </div>
                <div style="position:absolute; bottom:12px; right:12px; background:rgba(255,255,255,0.95); backdrop-filter:blur(8px); font-size:0.75rem; font-weight:700; color:var(--primary-accent); padding:4px 12px; border-radius:14px; box-shadow:0 4px 10px rgba(0,0,0,0.12);">
                    {d['tag']}
                </div>
            </div>
            <div class="dept-showcase-content" style="padding:1.4rem; display:flex; flex-direction:column; flex:1;">
                <h3 style="font-size:1.22rem; margin:0 0 0.5rem 0; color:var(--text-dark);">{d['title']}</h3>
                <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.55; margin:0 0 1rem 0; flex:1;">{d['meaning']}</p>
                <div style="margin-top:auto; padding-top:0.8rem; border-top:1px solid var(--border-warm); display:flex; align-items:center; justify-content:space-between;">
                    <span style="font-size:0.82rem; color:var(--primary-accent); font-weight:700;"><i data-lucide="shield-check" style="width:14px; vertical-align:middle;"></i> In-Hospital Care</span>
                    <span class="dept-card-cta" style="color:var(--primary-accent); font-weight:700; font-size:0.85rem; display:flex; align-items:center; gap:4px;"><span>Explore Speciality</span> <i data-lucide="arrow-right" style="width:15px; height:15px;"></i></span>
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
            <p>Authentic, expert medical care and advanced clinical facilities serving Srikakulam.</p>
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
    # 3. BUILD ALL 4 DEDICATED SERVICE PAGES (Purely Facility & Hospital Readiness - No Doctor Details)
    # -------------------------------------------------------------
    for s_id, s in SERVICES_DATA.items():
        # Highlights pills
        highlights_html = ""
        for hl in s['highlights']:
            highlights_html += f'''
            <li style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.6rem; color:var(--text-dark); font-weight:600; font-size:0.95rem;">
                <i data-lucide="check-circle-2" style="color:var(--primary-accent); width:18px; height:18px; flex-shrink:0;"></i>
                <span>{hl}</span>
            </li>'''

        # Feature items
        features_html = ""
        for feat in s.get('features', []):
            features_html += f'''
            <div style="background:#ffffff; border:1.5px solid var(--border-warm); border-radius:var(--radius-md); padding:1.25rem 1.4rem; box-shadow:var(--shadow-sm); display:flex; align-items:center; gap:0.75rem;">
                <div class="card-icon-badge" style="width:36px; height:36px; margin:0;"><i data-lucide="check" style="width:18px; height:18px;"></i></div>
                <strong style="color:var(--text-dark); font-size:0.95rem;">{feat}</strong>
            </div>'''

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

        if s.get('image'):
            service_visual_html = f'''
                <div class="detail-hero-visual">
                    <div class="detail-arch-frame" style="height:380px; border-radius:var(--radius-lg); overflow:hidden; position:relative; box-shadow:0 14px 36px rgba(128,0,0,0.12); border:2px solid var(--border-warm); background:#fff5f2;">
                        <img src="{s['image']}" alt="{s['title']}" style="width:100%; height:100%; object-fit:cover; display:block;">
                        <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,0.02) 0%, rgba(0,0,0,0.5) 100%);"></div>
                        <div class="detail-floating-badge" style="position:absolute; bottom:20px; left:20px; right:20px; background:rgba(255,255,255,0.95); backdrop-filter:blur(8px); padding:0.75rem 1.2rem; border-radius:14px; display:flex; align-items:center; gap:10px; box-shadow:0 6px 20px rgba(0,0,0,0.15);">
                            <div class="card-icon-badge" style="width:38px; height:38px; font-size:1rem; margin:0; flex-shrink:0;">
                                <i data-lucide="{s['icon']}"></i>
                            </div>
                            <div>
                                <strong style="display:block; font-size:0.95rem; color:var(--text-dark);">{s['title']}</strong>
                                <span style="font-size:0.78rem; color:var(--text-muted);">A1 Hospital Srikakulam</span>
                            </div>
                        </div>
                    </div>
                </div>'''
        else:
            service_visual_html = f'''
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
                            <i data-lucide="calendar"></i> <span>Inquire / Request Service</span>
                        </a>
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp: {HOSPITAL_CONTACT['whatsapp_number']}</span>
                        </a>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="btn-emergency-call" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>Call: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                    </div>
                </div>

                {service_visual_html}
            </div>

            <!-- Hospital Facility Standards & 24/7 Readiness (Purely Service & Quality) -->
            <div class="detail-doctor-spotlight animate-up" style="margin-top:2.5rem;">
                <div class="detail-doc-img-wrap" style="display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, #fdf8f5 0%, #f7ece6 100%);">
                    <div class="doctor-emblem-badge" style="width:68px; height:68px; margin:0;">
                        <i data-lucide="{s['icon']}"></i>
                    </div>
                </div>
                <div class="detail-doc-info">
                    <span class="detail-doc-badge">Hospital Facility Protocol</span>
                    <h3>24/7 Operational Readiness &amp; Clinical Safety</h3>
                    <div class="doc-qual">Equipped with Continuous Supervision &amp; Sterile Standards</div>
                    <p>Maintained under strict hospital hygiene protocols, real-time vital monitoring, and continuous nursing supervision for uninterrupted patient care.</p>
                    <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('', '{s['title']}')">
                        <i data-lucide="calendar"></i> <span>Inquire About This Service</span>
                    </a>
                </div>
            </div>

            <!-- Key Facility Highlights -->
            <div style="margin-top:2rem; display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem;">
                {features_html}
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
    # 4. BUILD ALL 8 DEDICATED DEPARTMENT PAGES (Focus on Clinical Specialities - No Doctor Names)
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
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.75rem 1.4rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                            <i data-lucide="message-circle"></i> <span>WhatsApp Help Desk</span>
                        </a>
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="btn-primary" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>Call: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                    </div>
                </div>

                <div class="detail-hero-visual">
                    <div class="detail-arch-frame" style="height:380px; border-radius:var(--radius-lg); overflow:hidden; position:relative; box-shadow:0 14px 36px rgba(128,0,0,0.12); border:2px solid var(--border-warm); background:#fff5f2;">
                        <img src="{d.get('image', 'dept_pediatrics.jpg')}" alt="{d['title']}" style="width:100%; height:100%; object-fit:cover; display:block;">
                        <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,0.02) 0%, rgba(0,0,0,0.5) 100%);"></div>
                        <div class="detail-floating-badge" style="position:absolute; bottom:20px; left:20px; right:20px; background:rgba(255,255,255,0.95); backdrop-filter:blur(8px); padding:0.75rem 1.2rem; border-radius:14px; display:flex; align-items:center; gap:10px; box-shadow:0 6px 20px rgba(0,0,0,0.15);">
                            <div class="card-icon-badge" style="width:38px; height:38px; font-size:1rem; margin:0; flex-shrink:0;">
                                <i data-lucide="{d['icon']}"></i>
                            </div>
                            <div>
                                <strong style="display:block; font-size:0.95rem; color:var(--text-dark);">{d['title']}</strong>
                                <span style="font-size:0.78rem; color:var(--text-muted);">A1 Hospital Srikakulam</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Clinical Scope & Diagnostic Care (Zero Doctor Names) -->
            <div style="margin-top:2.5rem;">
                <div class="section-eyebrow" style="margin-bottom:0.75rem;">
                    <span class="eyebrow-dot"></span> CLINICAL SCOPE &amp; PROTOCOL
                </div>
                <h2 style="font-size:1.8rem; color:var(--text-dark); margin-bottom:1.5rem;">Specialized Care &amp; <span class="serif-italic">Clinical Facilities</span></h2>
                
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.5rem;">
                    <div style="background:#ffffff; border:1.5px solid var(--border-warm); border-radius:var(--radius-md); padding:1.5rem; box-shadow:var(--shadow-sm);">
                        <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.8rem;">
                            <div class="card-icon-badge" style="width:36px; height:36px; margin:0;"><i data-lucide="stethoscope"></i></div>
                            <h4 style="margin:0; font-size:1.05rem; color:var(--text-dark);">Comprehensive OPD &amp; Inpatient Care</h4>
                        </div>
                        <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6; margin:0;">Daily outpatient consultations, accurate diagnostic evaluations, and continuous inpatient monitoring with modern medical technology.</p>
                    </div>
                    
                    <div style="background:#ffffff; border:1.5px solid var(--border-warm); border-radius:var(--radius-md); padding:1.5rem; box-shadow:var(--shadow-sm);">
                        <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.8rem;">
                            <div class="card-icon-badge" style="width:36px; height:36px; margin:0;"><i data-lucide="shield-check"></i></div>
                            <h4 style="margin:0; font-size:1.05rem; color:var(--text-dark);">Sterile Protocols &amp; Safety</h4>
                        </div>
                        <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6; margin:0;">Sterilized operation suites, advanced diagnostic testing, and evidence-based clinical recovery pathways tailored to patient needs.</p>
                    </div>
                </div>

                <div style="margin-top:1.8rem; background:linear-gradient(135deg, #fdf5f3 0%, #faece9 100%); border:1.5px solid rgba(128,0,0,0.15); border-radius:var(--radius-md); padding:1.5rem 1.8rem; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:1rem;">
                    <div>
                        <strong style="display:block; font-size:1.1rem; color:var(--text-dark); margin-bottom:0.25rem;">Need Clinical Guidance for {d['title']}?</strong>
                        <span style="font-size:0.88rem; color:var(--text-charcoal);">Contact our 24/7 reception desk or chat via WhatsApp for guidance and scheduling.</span>
                    </div>
                    <div style="display:flex; gap:0.8rem; flex-wrap:wrap;">
                        <a href="tel:{HOSPITAL_CONTACT['phone_1'].replace('-', '')}" class="btn-primary" style="text-decoration:none;">
                            <i data-lucide="phone"></i> <span>Call Helpline: {HOSPITAL_CONTACT['phone_1']}</span>
                        </a>
                        <a href="{HOSPITAL_CONTACT['whatsapp_link']}" target="_blank" class="btn-secondary" style="background:#fff; text-decoration:none;">
                            <i data-lucide="message-circle" style="color:#25D366;"></i> <span>WhatsApp Desk</span>
                        </a>
                    </div>
                </div>
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
    # 5. BUILD DOCTORS.HTML (Verified Doctors - No Overlay Tags on Top of Photos)
    # -------------------------------------------------------------
    doc_cards_html = ""
    for doc in DOCTORS_DATA:
        is_founder = "Founder" in doc['title']
        is_senior_specialist = doc['id'] in ['dr-g-prameela', 'dr-co-founder-wife'] or "Senior" in doc['title']
        if doc.get('image'):
            img_pos = "object-position: top center;"
            img_or_avatar = f'''
            <div style="height:270px; width:100%; overflow:hidden; position:relative; background:#fff5f2;">
                <img src="{doc['image']}" alt="{doc['name']}" style="width:100%; height:100%; object-fit:cover; {img_pos} transition:transform 0.5s ease;">
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

        exp_badge_html = f'<div class="doc-exp-chip"><i data-lucide="award" style="width:14px; height:14px;"></i> {doc.get("exp", "Clinical Specialist")}</div>'

        doc_cards_html += f'''
        <div class="doctor-card animate-up"{card_custom_id} style="display:flex; flex-direction:column; background:var(--bg-surface); border-radius:var(--radius-lg); {card_border_style} overflow:hidden; box-shadow:var(--shadow-sm); transition:var(--transition-bounce);">
            {img_or_avatar}
            <div style="padding:1.4rem; display:flex; flex-direction:column; flex:1;">
                <h3 style="font-size:1.25rem; margin:0 0 0.3rem 0; color:var(--text-dark);">{doc['name']}</h3>
                <div style="font-size:0.86rem; color:var(--primary-accent); font-weight:700; margin-bottom:0.25rem;">{doc['qual']}</div>
                <div style="font-size:0.82rem; font-weight:600; color:var(--text-charcoal); margin-bottom:0.4rem;">{doc['title']}</div>
                {exp_badge_html}
                <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.55; margin:0.6rem 0 0 0; flex:1;">{doc['desc']}</p>
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
    # 6. BUILD BLOG.HTML (Health Insights & Awareness Guides)
    # -------------------------------------------------------------
    blog_cards_html = ""
    for post in BLOG_POSTS:
        encoded_content = urllib.parse.quote(post['full_content'])
        safe_title = post['title'].replace("'", "\\'")
        blog_cards_html += f'''
        <div class="blog-card animate-up" data-category="{post['category']}">
            <div class="blog-card-visual">
                <div style="width:64px; height:64px; border-radius:18px; background:#ffffff; color:var(--primary-accent); display:flex; align-items:center; justify-content:center; box-shadow:0 8px 22px rgba(128,0,0,0.12);">
                    <i data-lucide="{post['icon']}" style="width:32px; height:32px;"></i>
                </div>
                <span class="blog-card-badge">{post['category_name']}</span>
                <span class="blog-card-time">{post['read_time']}</span>
            </div>
            <div class="blog-card-content">
                <h3>{post['title']}</h3>
                <p>{post['excerpt']}</p>
                <div class="blog-card-footer">
                    <span style="font-size:0.8rem; color:var(--text-muted); font-weight:600;"><i data-lucide="calendar" style="width:13px; vertical-align:middle;"></i> {post['date']}</span>
                    <button class="blog-read-btn" onclick="openArticleModal('{safe_title}', '{post['category_name']}', '{post['date']}', '{post['read_time']}', '{encoded_content}')">
                        <span>Read Article</span> <i data-lucide="arrow-right" style="width:15px; height:15px;"></i>
                    </button>
                </div>
            </div>
        </div>'''

    blog_body = f'''
    {spacer}
    <section class="framed-section animate-up" style="margin-top:1.5rem;">
        <div class="section-title">
            <div class="section-eyebrow">
                <span class="eyebrow-dot"></span> HEALTH &amp; WELLNESS AWARENESS
            </div>
            <h2>A1 Hospital <span class="serif-italic">Health Insights</span></h2>
            <p>Practical medical knowledge, disease prevention tips, and verified clinical guidance from our medical center in Srikakulam.</p>
        </div>

        <!-- Category Filter Pills -->
        <div class="blog-filter-bar">
            <button class="blog-filter-pill active" onclick="filterBlog('all', this)">All Articles</button>
            <button class="blog-filter-pill" onclick="filterBlog('pediatrics', this)">Pediatrics &amp; Child Health</button>
            <button class="blog-filter-pill" onclick="filterBlog('obstetrics', this)">Women's Health &amp; IVF</button>
            <button class="blog-filter-pill" onclick="filterBlog('orthopedics', this)">Orthopedics &amp; Joint Care</button>
            <button class="blog-filter-pill" onclick="filterBlog('emergency', this)">Emergency Care</button>
            <button class="blog-filter-pill" onclick="filterBlog('nephrology', this)">Kidney Health</button>
            <button class="blog-filter-pill" onclick="filterBlog('generalmedicine', this)">General Medicine</button>
        </div>

        <!-- Blog Articles Grid -->
        <div class="blog-grid">
            {blog_cards_html}
        </div>

        <!-- Health Consultation Prompt Banner -->
        <div style="margin-top:3.5rem; background:linear-gradient(135deg, #fdf5f3 0%, #faece9 100%); border:1.5px solid rgba(128,0,0,0.18); border-radius:var(--radius-lg); padding:2rem 2.5rem; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:1.5rem;">
            <div>
                <span style="font-size:0.75rem; font-weight:800; color:var(--primary-accent); text-transform:uppercase; letter-spacing:1px; display:block; margin-bottom:0.3rem;">CLINICAL SUPPORT DESK</span>
                <h3 style="font-size:1.45rem; font-family:'Playfair Display', serif; color:var(--text-dark); margin:0 0 0.4rem 0;">Have a Health Question or Need Consultation?</h3>
                <p style="margin:0; font-size:0.95rem; color:var(--text-charcoal); line-height:1.5;">Our hospital doctors and outpatient clinics are here to help you and your family.</p>
            </div>
            <div style="display:flex; gap:1rem; flex-wrap:wrap;">
                <a href="#appointment" class="btn-primary" onclick="openAppointmentModal('', 'General Health Inquiry')">
                    <i data-lucide="calendar"></i> <span>Book an Appointment</span>
                </a>
                <a href="https://wa.me/91{HOSPITAL_CONTACT['whatsapp_number']}" target="_blank" class="btn-whatsapp-pill" style="display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.25rem; background:#25D366; color:#fff; border-radius:30px; font-weight:700; text-decoration:none;">
                    <i data-lucide="message-circle"></i> <span>WhatsApp Help Desk</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Full Article Reading Modal -->
    <div id="article-modal" class="article-modal-overlay">
        <div class="article-modal-container">
            <button class="article-modal-close" onclick="closeArticleModal()" aria-label="Close modal">&times;</button>
            <div style="margin-bottom:1.25rem;">
                <span id="modal-article-category" style="display:inline-block; font-size:0.75rem; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:var(--primary-accent); background:rgba(128,0,0,0.08); padding:3px 12px; border-radius:20px; margin-bottom:0.6rem;"></span>
                <h2 id="modal-article-title" style="font-size:1.6rem; color:var(--text-dark); margin:0 0 0.5rem 0; line-height:1.35; font-family:'Playfair Display', serif;"></h2>
                <span id="modal-article-meta" style="font-size:0.82rem; color:var(--text-muted); font-weight:600;"></span>
            </div>
            <div id="modal-article-body" style="font-size:0.98rem; line-height:1.75; color:var(--text-charcoal); border-top:1px solid var(--border-warm); padding-top:1.25rem;">
            </div>
            <div style="margin-top:2rem; padding-top:1.25rem; border-top:1px solid var(--border-warm); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
                <a href="#appointment" class="btn-primary" onclick="closeArticleModal(); openAppointmentModal('', 'Blog Consultation')">
                    <i data-lucide="calendar"></i> <span>Book Priority Appointment</span>
                </a>
                <button class="btn-secondary" onclick="closeArticleModal()">
                    <span>Close Article</span>
                </button>
            </div>
        </div>
    </div>
    '''

    blog_html = set_meta(common_nav + blog_body + page_footer, "Health Insights & Blog | A1 Hospital", "blog", "blog.html")
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)
    print("[OK] Created blog.html")

    # -------------------------------------------------------------
    # 7. ROUTER PAGES (service-detail.html & department-detail.html)
    # -------------------------------------------------------------
    router_script = '''
    <script>
        const params = new URLSearchParams(window.location.search);
        const hash = window.location.hash ? window.location.hash.replace('#', '').replace('service-', '').replace('dept-', '') : '';
        const id = params.get('id') || hash || 'beds';
        const targetMap = {
            'beds': 'service-beds.html',
            'emergency': 'service-emergency.html',
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
