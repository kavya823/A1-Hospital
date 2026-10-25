import re
import os

SERVICES_EXPLANATIONS_HTML = '''
        <!-- DETAILED SERVICES EXPLANATIONS SECTION -->
        <div class="explanation-section" id="services-explanations">
            <div class="explanation-section-title">
                <div class="section-eyebrow">
                    <span class="eyebrow-dot"></span> IN-DEPTH FACILITY DETAILS
                </div>
                <h2>Explore Our Medical <span class="serif-italic">Facilities &amp; Standards</span></h2>
                <p>Every facility at A1 Hospital is designed around patient safety, sterile protocols, and 24/7 clinical readiness.</p>
            </div>

            <div class="explanation-grid">
                <!-- 1. 100+ Beds -->
                <div class="explanation-card" id="service-beds">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="bed-double"></i>
                        </div>
                        <div>
                            <h3>100+ Inpatient Beds &amp; Suites</h3>
                            <span class="explanation-tag">Inpatient Hospitality</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Our inpatient wards feature over 100 multi-tier beds including luxury deluxe private suites, air-conditioned semi-private rooms, and sterile recovery wards. Every room is outfitted with centralized medical gas pipelines, motorized ergonomic beds, patient monitoring interfaces, and sanitized en-suite washrooms for optimal healing.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Key Highlights &amp; Comforts
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="shield"></i> Motorized Ergonomic Beds</span>
                        <span class="explanation-chip"><i data-lucide="wind"></i> Centralized O2 Pipeline</span>
                        <span class="explanation-chip"><i data-lucide="activity"></i> 24/7 Vitals Monitoring</span>
                        <span class="explanation-chip"><i data-lucide="bell"></i> Immediate Nurse Call Bell</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Inpatient Bed</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 2. 24/7 Emergency Care -->
                <div class="explanation-card" id="service-emergency">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge" style="background:#fee2e2; color:#b91c1c;">
                            <i data-lucide="clock"></i>
                        </div>
                        <div>
                            <h3>24/7 Critical Emergency &amp; Trauma</h3>
                            <span class="explanation-tag" style="background:#fee2e2; color:#b91c1c;">Emergency Protocol</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Staffed 24 hours a day, 365 days a year by experienced emergency physicians, trauma surgeons, and anaesthetists. Our emergency bay is equipped with zero-delay triage protocols, crash carts, cardiac defibrillators, dedicated resuscitation suites, and immediate access to modular operating theatres.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Emergency Capabilities
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="zap"></i> Zero-Wait Triage</span>
                        <span class="explanation-chip"><i data-lucide="heart-pulse"></i> ACLS Resuscitation</span>
                        <span class="explanation-chip"><i data-lucide="user-check"></i> On-Duty Trauma Surgeons</span>
                        <span class="explanation-chip"><i data-lucide="cross"></i> Pediatric Emergency Care</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="tel:08942228234" class="btn-emergency-call" style="padding:0.6rem 1.3rem; font-size:0.88rem;">
                            <i data-lucide="phone"></i> <span>Call 08942-228234</span>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 3. Modern Diagnostic Equipment -->
                <div class="explanation-card" id="service-equipment">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="microscope"></i>
                        </div>
                        <div>
                            <h3>Modern Diagnostic &amp; Surgical Tech</h3>
                            <span class="explanation-tag">Precision Technology</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Accurate diagnosis is the cornerstone of effective healthcare. A1 Hospital houses advanced multi-slice digital CT scanners, 4D ultrasound with color Doppler, digital high-frequency radiography, C-arm surgical fluoroscopy, and laminar-flow modular operating theatres to minimize infection risks.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Medical Equipment Suite
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="scan"></i> Multi-Slice Digital CT</span>
                        <span class="explanation-chip"><i data-lucide="eye"></i> 4D Color Doppler Ultrasound</span>
                        <span class="explanation-chip"><i data-lucide="layers"></i> High-Definition Laparoscopy</span>
                        <span class="explanation-chip"><i data-lucide="shield-check"></i> Laminar Air-Flow OTs</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Schedule Scan / Test</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 4. Experienced Doctors -->
                <div class="explanation-card" id="service-doctors">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="stethoscope"></i>
                        </div>
                        <div>
                            <h3>Experienced Specialist Doctors</h3>
                            <span class="explanation-tag">Clinical Excellence</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Our medical council brings together over 15+ years of distinguished clinical practice. Led by Founder Dr. Mula Venkatarao (M.D. Paed Niloufer) and Chief Obstetrician Dr. G. Prameela (M.S. OBG, FART), our clinicians collaborate across multidisciplinary boards to deliver evidence-based, compassionate care.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Clinical Strengths
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="award"></i> 15+ Years Clinical Standing</span>
                        <span class="explanation-chip"><i data-lucide="users"></i> Multidisciplinary Review</span>
                        <span class="explanation-chip"><i data-lucide="heart"></i> Evidence-Based Medicine</span>
                        <span class="explanation-chip"><i data-lucide="smile"></i> High Patient Satisfaction</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="doctors.html" class="btn-book-dept">
                            <span>Meet Our Doctors</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 5. 24/7 Pharmacy -->
                <div class="explanation-card" id="service-pharmacy">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="pill"></i>
                        </div>
                        <div>
                            <h3>24/7 In-House Certified Pharmacy</h3>
                            <span class="explanation-tag">Pharmacy Services</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        An integrated in-hospital pharmacy stocked with genuine, batch-certified pharmaceuticals, emergency critical-care injectables, cardiac medications, surgical supplies, and pediatric dosages. Controlled cold storage ensures the efficacy of vaccines and sensitive biopharmaceuticals.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Pharmacy Standards
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="thermometer"></i> Temperature-Controlled Storage</span>
                        <span class="explanation-chip"><i data-lucide="shield-alert"></i> Emergency Life-Saving Drugs</span>
                        <span class="explanation-chip"><i data-lucide="clock"></i> Open 24 Hours / 365 Days</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="tel:08942228234" class="btn-book-dept">
                            <span>Inquire with Pharmacy</span> <i data-lucide="phone"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 6. Ambulance Service -->
                <div class="explanation-card" id="service-ambulance">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="truck"></i>
                        </div>
                        <div>
                            <h3>24/7 Mobile ICU Ambulance Fleet</h3>
                            <span class="explanation-tag">Emergency Transport</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Equipped for rapid response across Srikakulam and surrounding districts. Our fleet includes Advanced Life Support (ALS) and Basic Life Support (BLS) ambulances outfitted with mobile mechanical ventilators, multi-channel monitors, defibrillators, suction units, and trained emergency technicians.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Mobile Fleet Equipment
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="navigation"></i> Real-Time GPS Tracking</span>
                        <span class="explanation-chip"><i data-lucide="wind"></i> Transport Ventilator</span>
                        <span class="explanation-chip"><i data-lucide="activity"></i> Cardiac Defibrillator</span>
                        <span class="explanation-chip"><i data-lucide="shield-plus"></i> Rapid Rural Dispatch</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="tel:08942228234" class="btn-emergency-call" style="padding:0.6rem 1.3rem; font-size:0.88rem;">
                            <i data-lucide="phone"></i> <span>Request Ambulance</span>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 7. Blood Bank -->
                <div class="explanation-card" id="service-bloodbank">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="droplet"></i>
                        </div>
                        <div>
                            <h3>Emergency Blood Bank &amp; Components</h3>
                            <span class="explanation-tag">Transfusion Medicine</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Our licensed blood bank and component separation center adheres to stringent screening protocols to provide safe whole blood, Packed Red Blood Cells (PRBC), Fresh Frozen Plasma (FFP), and Platelet Concentrates for emergency trauma and major surgical cases.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> Blood Bank Features
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="check-check"></i> Automated Cross-Matching</span>
                        <span class="explanation-chip"><i data-lucide="shield"></i> 100% Pathogen Screened</span>
                        <span class="explanation-chip"><i data-lucide="snowflake"></i> Cryo-Preserved Plasma</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="tel:08942228234" class="btn-book-dept">
                            <span>Contact Blood Bank</span> <i data-lucide="phone"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 8. Intensive Care Unit -->
                <div class="explanation-card" id="service-icu">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="heart-pulse"></i>
                        </div>
                        <div>
                            <h3>Intensive Care Unit (ICU &amp; NICU)</h3>
                            <span class="explanation-tag">Critical Care</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Comprehensive intensive care services including Medical ICU, Surgical ICU, and a specialized Neonatal Intensive Care Unit (NICU). With 1:1 dedicated patient-to-nurse monitoring, invasive hemodynamic pressure lines, high-frequency mechanical ventilators, and syringe infusion pumps.
                    </p>
                    <div class="explanation-features-title">
                        <i data-lucide="check-circle" style="width:14px; color:var(--primary-accent);"></i> ICU &amp; NICU Infrastructure
                    </div>
                    <div class="explanation-chips">
                        <span class="explanation-chip"><i data-lucide="user-check"></i> 24/7 Intensivist On-Duty</span>
                        <span class="explanation-chip"><i data-lucide="wind"></i> Advanced Mechanical Ventilators</span>
                        <span class="explanation-chip"><i data-lucide="sun"></i> Neonatal Radiant Warmers</span>
                        <span class="explanation-chip"><i data-lucide="lock"></i> HEPA Filter Isolation Bays</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>ICU Status Inquiry</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#services" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>
            </div>
        </div>
'''

DEPARTMENTS_EXPLANATIONS_HTML = '''
        <!-- DETAILED DEPARTMENTS EXPLANATIONS SECTION -->
        <div class="explanation-section" id="departments-explanations">
            <div class="explanation-section-title">
                <div class="section-eyebrow">
                    <span class="eyebrow-dot"></span> CLINICAL SPECIALITY PROFILES
                </div>
                <h2>Explore Our Specialized <span class="serif-italic">Clinical Departments</span></h2>
                <p>Learn about each department's clinical scope, common conditions treated, advanced surgical interventions, and dedicated medical specialists.</p>
            </div>

            <div class="explanation-grid">
                <!-- 1. Cardiology -->
                <div class="explanation-card" id="dept-cardiology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="heart"></i>
                        </div>
                        <div>
                            <h3>Cardiology</h3>
                            <span class="explanation-tag">Heart &amp; Vascular Care</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Our Cardiology department offers comprehensive preventive, diagnostic, and therapeutic management of heart and cardiovascular conditions. We provide prompt evaluation of acute chest pain, hypertension management, heart failure therapy, and cardiac rehabilitation.
                    </p>
                    <div class="explanation-features-title">Conditions Treated &amp; Services</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Heart Attack &amp; Angina</span>
                        <span class="explanation-chip">Hypertension</span>
                        <span class="explanation-chip">Arrhythmia</span>
                        <span class="explanation-chip">2D Echocardiography</span>
                        <span class="explanation-chip">Treadmill Test (TMT)</span>
                        <span class="explanation-chip">Holter Monitoring</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Cardiology Slot</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 2. Neurology -->
                <div class="explanation-card" id="dept-neurology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="brain"></i>
                        </div>
                        <div>
                            <h3>Neurology</h3>
                            <span class="explanation-tag">Brain, Nerve &amp; Spine</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Focused on the diagnosis and medical management of central and peripheral nervous system disorders. We have established rapid-response acute ischemic stroke protocols, seizure disorder management, migraine therapies, and neuro-rehabilitation.
                    </p>
                    <div class="explanation-features-title">Conditions Treated &amp; Services</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Acute Stroke Management</span>
                        <span class="explanation-chip">Epilepsy &amp; Seizures</span>
                        <span class="explanation-chip">Migraine &amp; Chronic Headache</span>
                        <span class="explanation-chip">Digital EEG &amp; NCS</span>
                        <span class="explanation-chip">Neuropathy</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Neurology Slot</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 3. Pediatrics -->
                <div class="explanation-card" id="dept-pediatrics">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="baby"></i>
                        </div>
                        <div>
                            <h3>Pediatrics &amp; Child Health</h3>
                            <span class="explanation-tag">Child &amp; Newborn Care</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Headed by Founder Dr. Mula Venkatarao (M.D PAED Niloufer), this department delivers world-class, loving care for newborns, infants, children, and adolescents. From preventive immunizations to acute pediatric emergency care and developmental milestones tracking.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. Mula Venkatarao (Founder)</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Complete Vaccination</span>
                        <span class="explanation-chip">Childhood Asthma</span>
                        <span class="explanation-chip">Neonatal Jaundice</span>
                        <span class="explanation-chip">Infections &amp; Fevers</span>
                        <span class="explanation-chip">Growth &amp; Nutrition</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Dr. Mula Venkatarao</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 4. Orthopedics -->
                <div class="explanation-card" id="dept-orthopedics">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="bone"></i>
                        </div>
                        <div>
                            <h3>Orthopedics &amp; Joint Surgery</h3>
                            <span class="explanation-tag">Bones &amp; Joint Replacement</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Sattaru Kishore Babu (M.S. Ortho) and Dr. Bammidi Sai Theja (MS Ortho, FIJR, FIASM), specializing in complex fracture fixations, primary and revision total knee and hip replacements, arthroscopy, and spine disorders.
                    </p>
                    <div class="explanation-features-title">Key Procedures &amp; Care</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Total Knee Replacement (TKR)</span>
                        <span class="explanation-chip">Total Hip Replacement (THR)</span>
                        <span class="explanation-chip">Arthroscopic Surgery</span>
                        <span class="explanation-chip">Complex Trauma &amp; Fractures</span>
                        <span class="explanation-chip">Spine Disc Herniation</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Orthopedic Slot</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 5. General Surgery -->
                <div class="explanation-card" id="dept-generalsurgery">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="scissors"></i>
                        </div>
                        <div>
                            <h3>General &amp; Laparoscopic Surgery</h3>
                            <span class="explanation-tag">Minimally Invasive Surgery</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Chittipotula Balaji (M.B.B.S., MS General Surgery), offering cutting-edge laparoscopic (keyhole) procedures and open surgical treatments ensuring reduced pain, minimal scarring, and quick return to regular activities.
                    </p>
                    <div class="explanation-features-title">Surgeries Performed</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Laparoscopic Cholecystectomy</span>
                        <span class="explanation-chip">Laparoscopic Appendectomy</span>
                        <span class="explanation-chip">Hernia Repair</span>
                        <span class="explanation-chip">Piles, Fissure &amp; Fistula</span>
                        <span class="explanation-chip">Abdominal Trauma</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult General Surgeon</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 6. Radiology -->
                <div class="explanation-card" id="dept-radiology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="scan"></i>
                        </div>
                        <div>
                            <h3>Radiology &amp; Digital Imaging</h3>
                            <span class="explanation-tag">Diagnostic Imaging</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Comprehensive diagnostic radiology services operating 24 hours a day with digital picture archiving. Accurate radiological evaluations enable swift diagnosis for emergency trauma, neurological symptoms, and abdominal conditions.
                    </p>
                    <div class="explanation-features-title">Imaging Modalities</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">High-Resolution CT Scan</span>
                        <span class="explanation-chip">4D Ultrasound &amp; Doppler</span>
                        <span class="explanation-chip">Digital X-Ray</span>
                        <span class="explanation-chip">Image-Guided Biopsies</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Radiology Scan</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 7. Obstetrics & Gynecology (IVF) -->
                <div class="explanation-card" id="dept-obg">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="heart-handshake"></i>
                        </div>
                        <div>
                            <h3>Obstetrics, Gynecology &amp; IVF</h3>
                            <span class="explanation-tag">Women's Health &amp; Fertility</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Under the expert leadership of Dr. G. Prameela (M.S. OBG, FART, FMAS), we offer holistic women's healthcare: prenatal and postnatal maternal care, painless normal deliveries, high-risk pregnancies, advanced IVF fertility solutions, and laparoscopic gynecological surgery.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. G. Prameela</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">IVF &amp; Fertility Care</span>
                        <span class="explanation-chip">Painless Delivery</span>
                        <span class="explanation-chip">High-Risk Pregnancy</span>
                        <span class="explanation-chip">PCOD / PCOS Care</span>
                        <span class="explanation-chip">Laparoscopic Hysterectomy</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Dr. G. Prameela</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 8. Pulmonology -->
                <div class="explanation-card" id="dept-pulmonology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="wind"></i>
                        </div>
                        <div>
                            <h3>Pulmonology &amp; Chest Medicine</h3>
                            <span class="explanation-tag">Lungs &amp; Respiratory</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Dedicated to the diagnosis, treatment, and ongoing care of pulmonary disorders, respiratory allergies, acute lung infections, chronic airway diseases, and occupational lung conditions.
                    </p>
                    <div class="explanation-features-title">Conditions &amp; Tests</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Asthma &amp; Bronchitis</span>
                        <span class="explanation-chip">COPD Management</span>
                        <span class="explanation-chip">Pneumonia</span>
                        <span class="explanation-chip">Spirometry (PFT)</span>
                        <span class="explanation-chip">Allergy Screening</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Pulmonology Slot</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 9. Dermatology -->
                <div class="explanation-card" id="dept-dermatology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="sparkles"></i>
                        </div>
                        <div>
                            <h3>Dermatology &amp; Cosmetology</h3>
                            <span class="explanation-tag">Skin, Hair &amp; Nails</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Specialized care for all dermatological conditions affecting the skin, scalp, hair, and nails. Treatments encompass clinical dermatology for chronic skin disorders and aesthetic cosmetic procedures.
                    </p>
                    <div class="explanation-features-title">Treatments Available</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Acne &amp; Scar Therapy</span>
                        <span class="explanation-chip">Psoriasis &amp; Eczema</span>
                        <span class="explanation-chip">Hair Fall &amp; Alopecia</span>
                        <span class="explanation-chip">Chemical Peeling</span>
                        <span class="explanation-chip">Skin Allergies</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Book Skin Consultation</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 10. Urology -->
                <div class="explanation-card" id="dept-urology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="activity"></i>
                        </div>
                        <div>
                            <h3>Urology &amp; Andrology</h3>
                            <span class="explanation-tag">Urinary &amp; Kidney Care</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Budumuru Ramana (M.S., MCH Urology), providing minimally invasive laser surgeries and medical management for kidney stones, prostate enlargement, strictures, and male urological disorders.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. Budumuru Ramana</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Laser Kidney Stone Removal</span>
                        <span class="explanation-chip">Prostate Surgery (TURP)</span>
                        <span class="explanation-chip">Urinary Tract Infections</span>
                        <span class="explanation-chip">Ureteral Stenting</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Urologist</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 11. Critical Care -->
                <div class="explanation-card" id="dept-criticalcare">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="heart-pulse"></i>
                        </div>
                        <div>
                            <h3>Critical Care &amp; Anaesthesia</h3>
                            <span class="explanation-tag">Intensive Medicine</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Providing round-the-clock intensive life-support, hemodynamic stabilization, and pain management for critically ill medical and post-operative surgical patients under trained intensivists.
                    </p>
                    <div class="explanation-features-title">Capabilities</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Invasive Hemodynamics</span>
                        <span class="explanation-chip">Mechanical Ventilation</span>
                        <span class="explanation-chip">Central Venous Access</span>
                        <span class="explanation-chip">Post-Surgical ICU</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Critical Care Inquiry</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 12. Oncology -->
                <div class="explanation-card" id="dept-oncology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="shield-plus"></i>
                        </div>
                        <div>
                            <h3>Radiation &amp; Clinical Oncology</h3>
                            <span class="explanation-tag">Comprehensive Cancer Care</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Navya Madabatula (M.B.B.S, M.D., M.D.), offering compassionate oncology evaluations, early cancer screening packages, radiation therapy consultations, and targeted chemotherapy protocols.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. Navya Madabatula</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Cancer Screening</span>
                        <span class="explanation-chip">Chemotherapy Planning</span>
                        <span class="explanation-chip">Radiation Consultation</span>
                        <span class="explanation-chip">Palliative Care</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Dr. Navya Madabatula</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 13. Nephrology -->
                <div class="explanation-card" id="dept-nephrology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="droplet"></i>
                        </div>
                        <div>
                            <h3>Nephrology &amp; Hemodialysis</h3>
                            <span class="explanation-tag">Kidney Health &amp; Dialysis</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Korla Vidya Sagar (M.D., DM Nephrology), providing state-of-the-art care for acute and chronic kidney disease (CKD), diabetic kidney damage, hypertension, and round-the-clock hemodialysis.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. Korla Vidya Sagar</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">24/7 Hemodialysis Unit</span>
                        <span class="explanation-chip">Chronic Kidney Disease (CKD)</span>
                        <span class="explanation-chip">Diabetic Nephropathy</span>
                        <span class="explanation-chip">Kidney Biopsy &amp; AV Fistula</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Dr. Korla Vidya Sagar</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>

                <!-- 14. Ophthalmology -->
                <div class="explanation-card" id="dept-ophthalmology">
                    <div class="explanation-card-header">
                        <div class="card-icon-badge">
                            <i data-lucide="eye"></i>
                        </div>
                        <div>
                            <h3>Ophthalmology</h3>
                            <span class="explanation-tag">Eye Care &amp; Vision</span>
                        </div>
                    </div>
                    <p class="explanation-desc">
                        Led by Dr. Palepu Srikanthi (M.S. Ophthalmology), offering modern eye exams, vision correction, cataract surgeries, diabetic retinopathy screenings, and glaucoma management.
                    </p>
                    <div class="explanation-features-title">Specialist: Dr. Palepu Srikanthi</div>
                    <div class="explanation-chips">
                        <span class="explanation-chip">Cataract Phaco Surgery</span>
                        <span class="explanation-chip">Diabetic Eye Screening</span>
                        <span class="explanation-chip">Glaucoma Treatment</span>
                        <span class="explanation-chip">Vision Assessment</span>
                    </div>
                    <div class="explanation-card-footer">
                        <a href="#appointment" class="btn-book-dept">
                            <span>Consult Dr. Palepu Srikanthi</span> <i data-lucide="arrow-right"></i>
                        </a>
                        <a href="#departments" class="back-to-top-link">Back to Top ↑</a>
                    </div>
                </div>
            </div>
        </div>
'''

def process():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    def set_title(html_str, title):
        return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_str)

    def set_data_page(html_str, page_name):
        return re.sub(r'<body[^>]*>', f'<body data-page="{page_name}">', html_str)

    nav_match = re.search(r'(<!DOCTYPE html>.*?(?=<header id="home"))', html, re.DOTALL)
    contact_footer_match = re.search(r'(<section id="contact".*?</html>)', html, re.DOTALL)

    services_match = re.search(r'(<section id="services".*?</section>)\s*(?:<!--.*?-->\s*)?<section id="departments"', html, re.DOTALL)
    departments_match = re.search(r'(<section id="departments".*?</section>)\s*(?:<!--.*?-->\s*)?<section id="lab"', html, re.DOTALL)
    doctors_match = re.search(r'(<section id="doctors".*?</section>)\s*(?:<!--.*?-->\s*)?<section id="contact"', html, re.DOTALL)

    spacer = '\n    <div style="margin-top: 1.5rem;"></div>\n'

    # 1. PROCESS SERVICES.HTML
    if nav_match and contact_footer_match and services_match:
        services_section = services_match.group(1)
        
        # Add detailed explanations before the closing </section>
        services_section = services_section.replace('</section>', SERVICES_EXPLANATIONS_HTML + '\n    </section>')
        
        # Replace carousel track with clean, clickable links to explanations
        services_track_old = re.search(r'<div class="carousel-track" id="services-carousel">.*?</div>\s*<button class="carousel-btn right-btn"', services_section, re.DOTALL)
        if services_track_old:
            services_track_new = '''<div class="carousel-track" id="services-carousel">
                <a href="#service-beds" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Beds Available">
                        <div class="dept-info"><h3>100+ Beds Available</h3></div>
                    </div>
                </a>
                <a href="#service-emergency" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1516549655169-df83a0774514?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="24/7 Care">
                        <div class="dept-info"><h3>24/7 Emergency Care</h3></div>
                    </div>
                </a>
                <a href="#service-equipment" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Modern Equipment">
                        <div class="dept-info"><h3>Modern Equipment</h3></div>
                    </div>
                </a>
                <a href="#service-doctors" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Qualified Doctors">
                        <div class="dept-info"><h3>Experienced Doctors</h3></div>
                    </div>
                </a>
                <a href="#service-pharmacy" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Pharmacy">
                        <div class="dept-info"><h3>24/7 In-House Pharmacy</h3></div>
                    </div>
                </a>
                <a href="#service-ambulance" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Ambulance">
                        <div class="dept-info"><h3>24/7 Ambulance Service</h3></div>
                    </div>
                </a>
                <a href="#service-bloodbank" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1579154204601-01588f351e67?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Blood Bank">
                        <div class="dept-info"><h3>Emergency Blood Bank</h3></div>
                    </div>
                </a>
                <a href="#service-icu" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1516549655169-df83a0774514?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="ICU">
                        <div class="dept-info"><h3>Intensive Care Unit (ICU)</h3></div>
                    </div>
                </a>
            </div>\n            <button class="carousel-btn right-btn"'''
            services_section = services_section.replace(services_track_old.group(0), services_track_new)

        services_html = nav_match.group(1) + spacer + services_section + contact_footer_match.group(1)
        services_html = set_title(services_html, 'Services | A1 Hospital')
        services_html = set_data_page(services_html, 'services')
        
        # Hide home view and show all view
        services_html = services_html.replace('id="home-services-view"', 'id="home-services-view" style="display: none;"')
        services_html = services_html.replace('id="all-services-view" style="display: none;"', 'id="all-services-view"')
        
        # Remove the "View All Services" button container
        services_html = re.sub(r'<div[^>]*id="view-all-srv-btn-container"[^>]*>.*?</div>', '', services_html, flags=re.DOTALL)
        
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(services_html)
        print("Successfully created services.html with rich explanations")
    else:
        print(f"Failed to create services.html")

    # 2. PROCESS DEPARTMENTS.HTML
    if nav_match and contact_footer_match and departments_match:
        dept_section = departments_match.group(1)

        # Add detailed explanations before the closing </section>
        dept_section = dept_section.replace('</section>', DEPARTMENTS_EXPLANATIONS_HTML + '\n    </section>')

        # Replace department carousel track with clickable links to explanations
        dept_track_old = re.search(r'<div class="carousel-track" id="dept-carousel">.*?</div>\s*<button class="carousel-btn right-btn"', dept_section, re.DOTALL)
        if dept_track_old:
            dept_track_new = '''<div class="carousel-track" id="dept-carousel">
                <a href="#dept-cardiology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1559757175-5700dde675bc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Cardiology">
                        <div class="dept-info"><h3>Cardiology</h3></div>
                    </div>
                </a>
                <a href="#dept-neurology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Neurology">
                        <div class="dept-info"><h3>Neurology</h3></div>
                    </div>
                </a>
                <a href="#dept-pediatrics" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Pediatrics">
                        <div class="dept-info"><h3>Pediatrics</h3></div>
                    </div>
                </a>
                <a href="#dept-orthopedics" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Orthopedics">
                        <div class="dept-info"><h3>Orthopedics</h3></div>
                    </div>
                </a>
                <a href="#dept-generalsurgery" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="General Surgery">
                        <div class="dept-info"><h3>General Surgery</h3></div>
                    </div>
                </a>
                <a href="#dept-radiology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1538108149393-fbbd81895907?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Radiology">
                        <div class="dept-info"><h3>Radiology</h3></div>
                    </div>
                </a>
                <a href="#dept-obg" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1551076805-e1869033e561?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Obstetrics &amp; Gynecology">
                        <div class="dept-info"><h3>Obstetrics &amp; Gynecology</h3></div>
                    </div>
                </a>
                <a href="#dept-pulmonology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Pulmonology">
                        <div class="dept-info"><h3>Pulmonology</h3></div>
                    </div>
                </a>
                <a href="#dept-dermatology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Dermatology">
                        <div class="dept-info"><h3>Dermatology</h3></div>
                    </div>
                </a>
                <a href="#dept-urology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Urology">
                        <div class="dept-info"><h3>Urology</h3></div>
                    </div>
                </a>
                <a href="#dept-criticalcare" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1584516150909-c43483ee7932?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Critical Care">
                        <div class="dept-info"><h3>Critical Care</h3></div>
                    </div>
                </a>
                <a href="#dept-oncology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1579154204601-01588f351e67?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Oncology">
                        <div class="dept-info"><h3>Oncology</h3></div>
                    </div>
                </a>
                <a href="#dept-nephrology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1582750433449-648ed127bb54?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Nephrology">
                        <div class="dept-info"><h3>Nephrology</h3></div>
                    </div>
                </a>
                <a href="#dept-ophthalmology" class="nav-to-explanation" style="text-decoration:none; color:inherit; display:block;">
                    <div class="dept-card-photo">
                        <img src="https://images.unsplash.com/photo-1594824436967-4638a16fb8e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Ophthalmology">
                        <div class="dept-info"><h3>Ophthalmology</h3></div>
                    </div>
                </a>
            </div>\n            <button class="carousel-btn right-btn"'''
            dept_section = dept_section.replace(dept_track_old.group(0), dept_track_new)

        dept_html = nav_match.group(1) + spacer + dept_section + contact_footer_match.group(1)
        dept_html = set_title(dept_html, 'Departments | A1 Hospital')
        dept_html = set_data_page(dept_html, 'departments')
        
        # Hide home view and show all view
        dept_html = dept_html.replace('id="home-dept-view"', 'id="home-dept-view" style="display: none;"')
        dept_html = dept_html.replace('id="all-dept-view" style="display: none;"', 'id="all-dept-view"')
        
        # Remove the "View All Departments" button container
        dept_html = re.sub(r'<div[^>]*id="view-all-dept-btn-container"[^>]*>.*?</div>', '', dept_html, flags=re.DOTALL)
        
        with open('departments.html', 'w', encoding='utf-8') as f:
            f.write(dept_html)
        print("Successfully created departments.html with rich explanations")
    else:
        print(f"Failed to create departments.html")

    # 3. PROCESS DOCTORS.HTML
    if nav_match and contact_footer_match and doctors_match:
        doc_html = nav_match.group(1) + spacer + doctors_match.group(1) + contact_footer_match.group(1)
        doc_html = set_title(doc_html, 'Doctors | A1 Hospital')
        doc_html = set_data_page(doc_html, 'doctors')
        
        # Hide home view and show all view
        doc_html = doc_html.replace('id="home-doctors-view"', 'id="home-doctors-view" style="display: none;"')
        doc_html = doc_html.replace('id="all-doctors-view" style="display: none;"', 'id="all-doctors-view"')
        
        # Remove the "View All Doctors" button container
        doc_html = re.sub(r'<div[^>]*id="view-all-docs-btn-container"[^>]*>.*?</div>', '', doc_html, flags=re.DOTALL)
        
        with open('doctors.html', 'w', encoding='utf-8') as f:
            f.write(doc_html)
        print("Successfully created doctors.html")
    else:
        print(f"Failed to create doctors.html")

if __name__ == '__main__':
    process()
