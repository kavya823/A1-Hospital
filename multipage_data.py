import os
import re

# Comprehensive Data for All 8 Medical Services
SERVICES_DATA = {
    "beds": {
        "id": "beds",
        "file": "service-beds.html",
        "title": "100+ Advanced Inpatient Beds",
        "title_formatted": "100+ Inpatient Beds &amp; <span class=\"serif-italic\">Healing Suites</span>",
        "eyebrow": "WORLD-CLASS INPATIENT HOSPITALITY",
        "subtitle": "Spacious, hygienic, and technologically equipped patient suites engineered for restorative comfort, round-the-clock monitoring, and clinical safety.",
        "icon": "bed-double",
        "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "100+ Bed Capacity",
        "badge_sub": "Deluxe & Semi-Private Suites",
        "stats": [
            ("100+ Total Beds", "shield-check"),
            ("Central O2 Pipeline", "wind"),
            ("24/7 Nurse Station", "bell"),
            ("Zero-Infection Protocol", "sparkles")
        ],
        "lead_para": "At A1 Hospital, our inpatient accommodation has been architected to merge the sterile rigor of a tertiary hospital with the serene comfort of modern hospitality. Accommodating over 100 inpatients across multiple care tiers, our facility offers private luxury suites, air-conditioned twin-sharing rooms, general healing wards, and dedicated surgical recovery spaces.",
        "body_para": "Each room is fitted with motorized multi-position patient beds, continuous biometric vitals tracking, centralized high-flow oxygen supply, ergonomic attendant couches, and sterile anti-microbial surfaces. Our infection-control team enforces daily multi-stage sanitation regimens to guarantee a spotless and restful healing environment.",
        "capabilities": [
            ("Motorized Ergonomic Beds", "Ergonomic multi-angle adjustments allowing patients optimal posture during post-op recovery and meals.", "bed"),
            ("Centralized Gas & O2", "Instantaneous bedside access to oxygen and medical suction pipelines connected directly to central oxygen banks.", "wind"),
            ("24/7 Vitals & Nurse Call", "Rapid digital bell system connecting every bed directly to the central nursing station for prompt responses.", "activity"),
            ("Attendant Comforts", "Dedicated living space and sleeper sofas for loved ones accompanying the patient throughout their hospital stay.", "heart")
        ],
        "amenities_title": "Inpatient Room Amenities & Standards",
        "amenities": [
            "Executive Deluxe Private Rooms", "Air-Conditioned Semi-Private Sharing", "24/7 Biometric Monitoring",
            "Sanitized En-Suite Washrooms", "Continuous Nursing Oversight", "Custom Therapeutic Diet Plans",
            "High-Speed Wi-Fi & Television", "Daily Linen Change & Sterilization"
        ],
        "doctor": {
            "name": "Dr. Mula Venkatarao & Clinical Care Faculty",
            "qual": "M.D (PAED Niloufer) · Founder & Clinical Director",
            "desc": "Overseeing daily inpatient rounds, multispeciality medical consultations, and strict infection-prevention safety protocols.",
            "img": "dr_rao.jpeg",
            "dept": "Inpatient Care & Pediatrics"
        }
    },
    "emergency": {
        "id": "emergency",
        "file": "service-emergency.html",
        "title": "24/7 Critical Emergency & Trauma Care",
        "title_formatted": "24/7 Critical Emergency &amp; <span class=\"serif-italic\">Trauma Center</span>",
        "eyebrow": "IMMEDIATE ACCIDENT & CRITICAL RESPONSE",
        "subtitle": "Uncompromising round-the-clock emergency medicine backed by on-duty trauma surgeons, resuscitation bays, and emergency surgical theatres.",
        "icon": "clock",
        "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "24/7 Trauma Active",
        "badge_sub": "Immediate Zero-Wait Triage",
        "stats": [
            ("24/7/365 Open", "clock"),
            ("< 3 Min Triage", "zap"),
            ("Trauma OTs Ready", "shield"),
            ("Mobile ICU Fleet", "ambulance")
        ],
        "lead_para": "When emergencies strike, seconds make the difference between life and death. The 24/7 Emergency and Trauma Center at A1 Hospital operates with uninterrupted readiness 365 days a year, staffed by dedicated emergency physicians, critical care anaesthetists, and seasoned trauma specialists.",
        "body_para": "Our emergency bay is engineered with high-efficiency triage workflows, multi-channel cardiac defibrillators, crash carts, continuous pulse-oximetry, and immediate access to emergency radiological imaging and blood components. From acute myocardial infarctions and brain strokes to severe polytrauma and pediatric crises, our teams deliver rapid life-saving intervention.",
        "capabilities": [
            ("Zero-Delay Triage", "Patients are assessed immediately by triage nurses and doctors upon arrival with no bureaucratic delays.", "zap"),
            ("ACLS Resuscitation Bay", "Equipped with advanced multi-channel defibrillators, mechanical ventilators, and emergency crash carts.", "heart-pulse"),
            ("Dedicated Trauma OTs", "Direct access to laminar air-flow surgical theatres prepared for immediate emergency surgical intervention.", "scissors"),
            ("Pediatric Emergency Care", "Specialized pediatric emergency protocols supervised by Founder Dr. Mula Venkatarao.", "baby")
        ],
        "amenities_title": "Emergency Capabilities & Protocols",
        "amenities": [
            "Acute Heart Attack Fast-Track", "Stroke Thrombolysis Protocol", "Polytrauma & Fracture Stabilization",
            "Burn & Wound Care Bay", "Pediatric Emergency Resuscitation", "Immediate Blood Component Access",
            "Emergency Multi-Slice CT Scanning", "Direct 24/7 Ambulance Hotline"
        ],
        "doctor": {
            "name": "Dr. P. Siva Kumar",
            "qual": "M.D (GEN. MED) · Consultant Physician & Critical Care",
            "desc": "Leading emergency resuscitations, sepsis management, and multi-organ critical stabilization protocols.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Critical Care"
        }
    },
    "equipment": {
        "id": "equipment",
        "file": "service-equipment.html",
        "title": "Modern Diagnostic & Surgical Equipment",
        "title_formatted": "Modern Diagnostic &amp; <span class=\"serif-italic\">Surgical Technology</span>",
        "eyebrow": "ADVANCED MEDICAL INFRASTRUCTURE",
        "subtitle": "High-precision diagnostic imaging, computer-analyzed pathology, and minimally invasive laparoscopic suites ensuring diagnostic accuracy.",
        "icon": "microscope",
        "image": "https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "State-of-the-Art Tech",
        "badge_sub": "Precision Clinical Imaging",
        "stats": [
            ("Multi-Slice Digital CT", "scan"),
            ("4D Color Doppler", "eye"),
            ("HD Laparoscopic Towers", "layers"),
            ("Laminar Flow OTs", "shield-check")
        ],
        "lead_para": "Clinical excellence relies on diagnostic clarity. A1 Hospital continuously invests in modern diagnostic scanners and surgical infrastructure to give our doctors clear insight and our surgeons millimeter precision during delicate operations.",
        "body_para": "Our medical equipment suite encompasses multi-slice high-resolution CT imaging, 4D ultrasound with high-definition color Doppler, digital high-frequency radiography, C-arm intraoperative fluoroscopy, and Karl Storz laparoscopic surgical towers. Operating theatres feature positive-pressure laminar airflow systems that eliminate airborne particulates and maintain sterile integrity.",
        "capabilities": [
            ("Multi-Slice CT Scanner", "High-speed cross-sectional imaging for neurological, thoracic, abdominal, and skeletal diagnosis.", "scan"),
            ("4D Color Doppler Ultrasound", "Advanced obstetric fetal anomaly scans, abdominal evaluations, and peripheral vascular Doppler studies.", "eye"),
            ("HD Laparoscopy Towers", "Enables minimally invasive keyhole surgeries with microscopic incisions, zero bleeding, and fast recovery.", "layers"),
            ("Laminar Air-Flow OTs", "Class 100 HEPA air-filtration systems safeguarding orthopedic implants and complex surgeries against infection.", "shield-check")
        ],
        "amenities_title": "Technology & Diagnostic Assets",
        "amenities": [
            "Multi-Slice Digital CT", "4D Obstetric Anomaly Ultrasound", "High-Frequency Digital X-Ray",
            "Intraoperative C-Arm Fluoroscopy", "Automated Hematology Analyzers", "Fully Motorized OT Tables",
            "Central Medical Vacuum & Gases", "Electronic Health Records (EHR)"
        ],
        "doctor": {
            "name": "Dr. G. Sandeep",
            "qual": "M.D (RADIOLOGY) · Consultant Radiologist",
            "desc": "Overseeing digital CT diagnostics, 4D obstetric scans, and interventional radiological evaluations.",
            "img": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Radiology"
        }
    },
    "doctors": {
        "id": "doctors",
        "file": "service-doctors.html",
        "title": "Experienced Specialist Doctors",
        "title_formatted": "Multidisciplinary Team of <span class=\"serif-italic\">Specialist Clinicians</span>",
        "eyebrow": "15+ YEARS OF CLINICAL DISTINCTION",
        "subtitle": "Distinguished physicians, super-specialists, and surgical innovators collaborating across integrated clinical boards for individualized patient care.",
        "icon": "stethoscope",
        "image": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "11+ Senior Specialists",
        "badge_sub": "Evidence-Based Compassion",
        "stats": [
            ("15+ Years Legacy", "award"),
            ("50,000+ Families", "users"),
            ("Multidisciplinary Care", "heart"),
            ("Verified Credentials", "check-circle-2")
        ],
        "lead_para": "At the heart of A1 Hospital's reputation is our exceptional medical faculty. Founded by acclaimed pediatrician Dr. Mula Venkatarao (M.D PAED Niloufer), the institution brings together over 11 credentialed medical and surgical specialists spanning cardiology, orthopedics, fertility, neurology, oncology, radiology, and general surgery.",
        "body_para": "Our consultants emphasize collaborative treatment planning. Complex patient cases undergo multidisciplinary medical board review, ensuring treatments adhere to national clinical guidelines while prioritizing patient comfort, safety, and rapid recovery.",
        "capabilities": [
            ("Pediatric & Neonatal Leads", "Pioneering pediatric critical care and developmental tracking led by Founder Dr. Mula Venkatarao.", "baby"),
            ("Orthopedics & Joint Surgery", "Led by Dr. Sattaru Kishore Babu and Dr. Bammidi Sai Theja for total knee, hip, and spine surgeries.", "bone"),
            ("Obstetrics, Gynecology & IVF", "Dr. G. Prameela provides comprehensive maternal and reproductive healthcare.", "heart-handshake"),
            ("Minimally Invasive Surgery", "Dr. K. Chaitanya Kishore performs laparoscopic procedures with minimal discomfort and hospital stay.", "scissors")
        ],
        "amenities_title": "Clinical Strengths & Consultations",
        "amenities": [
            "Daily Specialist Outpatient Clinics", "Second Opinion Consultations", "Pre-Operative Fitness Evaluations",
            "Comprehensive Wellness Screenings", "Dedicated Fertility Counseling", "Pediatric Immunization Schedules",
            "Emergency Trauma Surgical Response", "Post-Discharge Tele-Consultation"
        ],
        "doctor": {
            "name": "Dr. Mula Venkatarao",
            "qual": "M.D (PAED Niloufer) · Founder & Children Specialist",
            "desc": "Leading A1 Hospital with over 15+ years of clinical excellence, serving thousands of families in Srikakulam.",
            "img": "dr_rao.jpeg",
            "dept": "Pediatrics"
        }
    },
    "pharmacy": {
        "id": "pharmacy",
        "file": "service-pharmacy.html",
        "title": "24/7 In-House Certified Pharmacy",
        "title_formatted": "24/7 Certified In-House <span class=\"serif-italic\">Pharmacy</span>",
        "eyebrow": "AUTHENTIC PHARMACEUTICAL CARE",
        "subtitle": "Continuously stocked with genuine, batch-certified medications, emergency life-saving injectables, and strict cold-chain biological storage.",
        "icon": "pill",
        "image": "https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "24/7 Open Always",
        "badge_sub": "100% Genuine Certified Drugs",
        "stats": [
            ("24 Hours / 365 Days", "clock"),
            ("Cold Chain Preserved", "thermometer"),
            ("Direct Hospital Access", "shield-plus"),
            ("Fast Dispensation", "check")
        ],
        "lead_para": "Immediate medication accessibility is critical in inpatient and emergency management. A1 Hospital operates a fully integrated, licensed in-house pharmacy located on the hospital ground floor, operating seamlessly 24 hours a day, 7 days a week.",
        "body_para": "Every pharmaceutical formulation is sourced directly from certified manufacturers, undergoing strict batch verification and cold-chain temperature monitoring. Our pharmacy stocks specialized emergency critical care injectables, pediatric formulations, cardiac therapeutics, and surgical consumables.",
        "capabilities": [
            ("Cold-Chain Vaccine Vault", "Monitored refrigeration units preserving biological efficacy of sensitive pediatric vaccines and insulin.", "thermometer"),
            ("Emergency Critical Injections", "Immediate stock of anti-thrombotics, inotropes, emergency anti-hypertensives, and anti-venoms.", "shield-alert"),
            ("Pediatric & Neonatal Doses", "Specialized liquid suspensions and precisely calibrated dosages tailored for pediatric patients.", "baby"),
            ("Computerized Verification", "Digital cross-checking of prescriptions to eliminate medication errors and speed up dispensing.", "layers")
        ],
        "amenities_title": "Pharmacy Highlights & Assurances",
        "amenities": [
            "100% Genuine Manufacturer Guarantee", "Strict 2°C - 8°C Cold Storage", "Round-the-Clock On-Duty Pharmacists",
            "Surgical Implants & Consumables", "Emergency Bedside Delivery for Inpatients", "Digital Billing & Itemized Receipts",
            "Generic & Branded Formulations", "Pediatric Immunization Supplies"
        ],
        "doctor": {
            "name": "Clinical Pharmacist & Quality Team",
            "qual": "B.Pharm, Pharm.D · Registered Hospital Pharmacists",
            "desc": "Ensuring prescription safety, dosage accuracy, and sterile storage of all hospital pharmaceuticals.",
            "img": "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Pharmacy Services"
        }
    },
    "ambulance": {
        "id": "ambulance",
        "file": "service-ambulance.html",
        "title": "24/7 Advanced Life Support Ambulance",
        "title_formatted": "24/7 Advanced Life Support <span class=\"serif-italic\">Ambulance Fleet</span>",
        "eyebrow": "RAPID CRITICAL PATIENT TRANSPORT",
        "subtitle": "Mobile ICU ambulances equipped with portable mechanical ventilators, multi-parameter monitors, oxygen banks, and trained paramedics.",
        "icon": "ambulance",
        "image": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Mobile ICU Fleet",
        "badge_sub": "Immediate Dispatch Response",
        "stats": [
            ("Rapid Dispatch", "zap"),
            ("Transport Ventilator", "wind"),
            ("ACLS Paramedics", "user-check"),
            ("GPS Emergency Tracking", "map-pin")
        ],
        "lead_para": "For critically ill patients and trauma victims, safe transportation with active resuscitation is paramount. A1 Hospital maintains dedicated Advanced Life Support (ALS) and Basic Life Support (BLS) ambulances on standby 24 hours a day.",
        "body_para": "Our ambulances function as mobile intensive care units, outfitted with transport ventilators, continuous defibrillator monitors, medical suction, oxygen banks, and emergency trauma splints. Each ALS dispatch is accompanied by certified paramedics in direct contact with the hospital emergency room.",
        "capabilities": [
            ("Transport Ventilators", "Enables safe transfer of intubated and mechanically ventilated patients between facilities.", "wind"),
            ("Continuous Cardiac Defibrillator", "Real-time monitoring of ECG, SpO2, and blood pressure with immediate pacing capabilities.", "heart-pulse"),
            ("Direct ER Notification", "Paramedics communicate patient vitals to the trauma team en route so surgical suites are primed before arrival.", "phone-call"),
            ("Accident & Trauma Splints", "Spinal backboards, vacuum splints, and cervical collars to prevent secondary spinal cord injury.", "shield")
        ],
        "amenities_title": "Ambulance Equipment & Services",
        "amenities": [
            "Advanced Life Support (ALS) Unit", "Basic Life Support (BLS) Transport", "Oxygen Delivery Systems & Regulators",
            "Portable Suction & Intubation Kit", "Emergency Fracture Splints & Stretcher", "Direct Hospital Dispatch Line",
            "Inter-City & Home Retrieval", "24/7 Certified Paramedic Escort"
        ],
        "doctor": {
            "name": "Emergency Medical Dispatch Team",
            "qual": "Certified Emergency Medicine Technicians (EMT)",
            "desc": "Trained in Advanced Cardiac Life Support (ACLS) and Pediatric Advanced Life Support (PALS).",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Emergency Response"
        }
    },
    "bloodbank": {
        "id": "bloodbank",
        "file": "service-bloodbank.html",
        "title": "Emergency Blood Storage & Bank",
        "title_formatted": "Emergency Blood Storage &amp; <span class=\"serif-italic\">Transfusion Services</span>",
        "eyebrow": "LIFE-SAVING BLOOD SUPPORT",
        "subtitle": "24/7 temperature-controlled storage of screened whole blood, packed red cells, fresh frozen plasma, and platelets for surgical and trauma readiness.",
        "icon": "droplet",
        "image": "https://images.unsplash.com/photo-1579154204601-01588f351e67?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Safe Blood Storage",
        "badge_sub": "24/7 Rapid Cross-Matching",
        "stats": [
            ("Zero-Delay Transfusion", "zap"),
            ("Stringent Screening", "shield-check"),
            ("Cryo-Temp Monitored", "thermometer"),
            ("All Blood Groups Stocked", "droplet")
        ],
        "lead_para": "Surgeries, severe postpartum hemorrhage, road traffic trauma, and acute anemia demand immediate, safe blood transfusions. A1 Hospital maintains a dedicated, certified blood storage facility operating under national regulatory benchmarks.",
        "body_para": "All units undergo multi-tier testing for infectious markers, automated antibody screening, and precision cross-matching. Maintained inside calibrated blood bank refrigerators with continuous electronic temperature charting and backup power, blood components are prepared for instant clinical deployment.",
        "capabilities": [
            ("Rapid Cross-Matching", "Computerized and gel-card cross-matching to ensure complete compatibility in minimal turnaround time.", "check-circle-2"),
            ("Packed Red Cells (PRBC)", "Concentrated red blood cells for trauma resuscitation and surgical blood loss correction.", "droplet"),
            ("Fresh Frozen Plasma (FFP)", "Rich in coagulation factors to manage severe bleeding, liver dysfunction, and coagulopathies.", "layers"),
            ("Platelet Concentrate", "Essential for severe dengue, thrombocytopenia, and oncological bleeding prophylaxis.", "activity")
        ],
        "amenities_title": "Blood Storage & Safety Protocols",
        "amenities": [
            "24/7 Rapid Blood Component Release", "Mandatory Multi-Marker Infection Screen", "Calibrated 2°C - 6°C Storage Units",
            "Emergency O-Negative Trauma Reserves", "Automated Gel Card Cross-Matching", "Pediatric Micro-Transfusion Aliquots",
            "Continuous Temperature Data-Logging", "Strict Blood Transfusion Auditing"
        ],
        "doctor": {
            "name": "Dr. G. Prameela & Surgical Council",
            "qual": "M.S (OBG), FART · Senior Consultant Obstetrician",
            "desc": "Ensuring zero-delay blood component availability during high-risk deliveries and emergency surgical operations.",
            "img": "https://images.unsplash.com/photo-1594824813591-9a74b01d0a51?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Obstetrics & Surgery"
        }
    },
    "icu": {
        "id": "icu",
        "file": "service-icu.html",
        "title": "Intensive Care Unit (ICU & NICU)",
        "title_formatted": "Multidisciplinary Intensive Care Unit <span class=\"serif-italic\">(ICU &amp; NICU)</span>",
        "eyebrow": "ADVANCED CRITICAL CARE SURVEILLANCE",
        "subtitle": "High-dependency adult ICU and specialized Neonatal ICU (NICU) with invasive mechanical ventilation, 1:1 nurse oversight, and continuous intensivist care.",
        "icon": "activity",
        "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "ICU & NICU Active",
        "badge_sub": "1:1 Dedicated Nursing Ratio",
        "stats": [
            ("Advanced Ventilators", "wind"),
            ("1:1 Nursing Care", "user-check"),
            ("Dedicated Neonatal ICU", "baby"),
            ("Positive Pressure HEPA", "shield")
        ],
        "lead_para": "The Intensive Care Unit at A1 Hospital represents the highest echelon of clinical vigilance. Designed to support critically unstable patients with single or multi-organ failure, our ICU integrates sophisticated life-support technologies with compassionate, round-the-clock intensivist guidance.",
        "body_para": "Our facility is divided into dedicated Adult Intensive Care and a specialized Neonatal Intensive Care Unit (NICU). Equipped with invasive and non-invasive mechanical ventilators, central venous pressure lines, arterial blood gas analyzers, radiant warmers, and phototherapy suites, every bed is monitored continuously.",
        "capabilities": [
            ("Invasive Mechanical Ventilation", "State-of-the-art ventilators delivering lung-protective ventilation modes for severe ARDS and pneumonia.", "wind"),
            ("Neonatal ICU (NICU)", "Led by pediatrician Dr. Mula Venkatarao, featuring incubators, phototherapy, and micro-infusion pumps for newborns.", "baby"),
            ("Continuous Hemodynamics", "Real-time arterial line monitoring, central venous pressure, and cardiac output telemetry.", "activity"),
            ("Isolation & Infection Control", "Positive-pressure airflow and HEPA filtration safeguarding immunocompromised patients.", "shield-check")
        ],
        "amenities_title": "Critical Care Infrastructure",
        "amenities": [
            "Continuous 1:1 Bedside Nursing", "High-End Hamilton Mechanical Ventilators", "Radiant Warmers & Incubators in NICU",
            "Arterial Blood Gas (ABG) Lab", "Centralized Multiparameter Monitoring", "Continuous Renal Replacement Setup",
            "Daily Intensivist Family Counseling", "Negative/Positive Pressure Isolation"
        ],
        "doctor": {
            "name": "Dr. P. Siva Kumar & Dr. Mula Venkatarao",
            "qual": "M.D (GEN MED) & M.D (PAED Niloufer)",
            "desc": "Leading adult critical care medicine and neonatal intensive care with over two decades of combined expertise.",
            "img": "dr_rao.jpeg",
            "dept": "Critical Care & Pediatrics"
        }
    }
}

# Comprehensive Data for All 14 Clinical Departments
DEPARTMENTS_DATA = {
    "cardiology": {
        "id": "cardiology",
        "file": "department-cardiology.html",
        "title": "Cardiology & Vascular Medicine",
        "title_formatted": "Department of Cardiology &amp; <span class=\"serif-italic\">Heart Health</span>",
        "eyebrow": "CARDIOVASCULAR EXCELLENCE",
        "subtitle": "Comprehensive preventive, diagnostic, and therapeutic cardiology care dedicated to safeguarding cardiac vitality and managing acute chest pain.",
        "icon": "heart",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Cardiology Center",
        "badge_sub": "Rapid Heart Attack Protocol",
        "stats": [
            ("2D Echocardiography", "activity"),
            ("Treadmill Stress Test", "zap"),
            ("Holter Telemetry", "heart"),
            ("Zero-Delay Chest Pain ER", "clock")
        ],
        "lead_para": "Cardiovascular diseases require rapid diagnostic precision and attentive therapeutic oversight. The Department of Cardiology at A1 Hospital delivers evidence-based cardiovascular medicine, from early hypertension detection to acute coronary crisis stabilization.",
        "body_para": "Equipped with high-definition digital 2D Echocardiography with Color Doppler, computerized Treadmill Stress Testing (TMT), and multi-day ambulatory Holter monitoring, our clinicians uncover early vascular anomalies before they escalate. In emergency scenarios, our fast-track chest pain protocol coordinates instant triage, emergency pharmacotherapy, and ICU stabilization.",
        "capabilities": [
            ("2D Echo & Color Doppler", "Comprehensive assessment of cardiac chamber dimensions, valvular function, and myocardial contractility.", "activity"),
            ("Treadmill Stress Test (TMT)", "Computerized stress testing evaluating coronary artery perfusion during controlled physical exertion.", "zap"),
            ("Ambulatory Holter Monitoring", "Continuous 24-48 hour ECG recording capturing transient arrhythmias and occult palpitations.", "heart"),
            ("Heart Failure Management", "Personalized pharmacotherapy, fluid management, and lifestyle rehabilitation protocols.", "shield-check")
        ],
        "amenities_title": "Conditions Managed & Clinical Procedures",
        "amenities": [
            "Acute Coronary Syndrome & Angina", "Hypertension & Vascular Disease", "Cardiac Arrhythmias & Palpitations",
            "Congestive Heart Failure", "Valvular Heart Disorders", "Post-Infarction Rehabilitation",
            "Lipid Disorder Optimization", "2D Color Doppler Echocardiography"
        ],
        "doctor": {
            "name": "Senior Cardiology Consultation Panel",
            "qual": "M.D (Cardiology), DM (Cardio) Visiting Consultants",
            "desc": "Experienced cardiologists delivering thorough cardiovascular evaluations and non-invasive cardiac care.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Cardiology"
        }
    },
    "neurology": {
        "id": "neurology",
        "file": "department-neurology.html",
        "title": "Neurology & Brain Sciences",
        "title_formatted": "Department of Neurology &amp; <span class=\"serif-italic\">Neuro-Rehabilitation</span>",
        "eyebrow": "ADVANCED NEUROLOGICAL CARE",
        "subtitle": "Expert diagnosis and medical intervention for stroke, epilepsy, chronic migraines, neuropathy, and degenerative brain disorders.",
        "icon": "brain",
        "image": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Neurology Clinic",
        "badge_sub": "Stroke Care & Digital EEG",
        "stats": [
            ("Acute Stroke Protocol", "zap"),
            ("Digital EEG & NCS", "activity"),
            ("Migraine Clinic", "smile"),
            ("Neuro-ICU Care", "shield")
        ],
        "lead_para": "The human nervous system demands sophisticated clinical nuance. The Neurology Department at A1 Hospital manages acute and chronic conditions of the central and peripheral nervous system, supported by modern neuro-imaging and electrophysiological diagnostics.",
        "body_para": "Our team maintains a rapid-response acute ischemic stroke protocol, administering prompt thrombolytic therapies within the vital golden hour window. We treat seizure disorders, peripheral neuropathies, Parkinson's disease, and neuro-infectious conditions with customized medical and physiotherapeutic rehabilitation.",
        "capabilities": [
            ("Acute Stroke Fast-Track", "High-speed CT brain evaluation and immediate intravenous thrombolysis to restore cerebral blood flow.", "zap"),
            ("Digital EEG Diagnostics", "High-resolution electroencephalography recording cerebral electrical patterns to classify seizures.", "activity"),
            ("Nerve Conduction Studies (NCS)", "Precision evaluation of peripheral nerve integrity to diagnose diabetic neuropathies and entrapments.", "layers"),
            ("Comprehensive Migraine Clinic", "Individualized preventive and acute abortive therapies for debilitating headache disorders.", "smile")
        ],
        "amenities_title": "Conditions Managed & Specialities",
        "amenities": [
            "Acute Ischemic & Hemorrhagic Stroke", "Epilepsy & Complex Seizure Disorders", "Chronic Migraine & Cluster Headaches",
            "Peripheral Neuropathy & Sciatica", "Parkinsonism & Movement Disorders", "Myasthenia Gravis & Muscle Diseases",
            "Cerebral Infections & Meningitis", "Neuro-Rehabilitation & Physiotherapy"
        ],
        "doctor": {
            "name": "Senior Neuro-Medical Council",
            "qual": "M.D, DM (Neurology) Consultants",
            "desc": "Specialized in stroke rehabilitation, seizure optimization, and peripheral nerve disorders.",
            "img": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Neurology"
        }
    },
    "pediatrics": {
        "id": "pediatrics",
        "file": "department-pediatrics.html",
        "title": "Pediatrics & Neonatology",
        "title_formatted": "Department of Pediatrics &amp; <span class=\"serif-italic\">Neonatal Care</span>",
        "eyebrow": "LOVING CHILD HEALTHCARE",
        "subtitle": "Pioneered by Founder Dr. Mula Venkatarao, delivering compassionate, world-class healthcare for newborns, infants, children, and teenagers.",
        "icon": "baby",
        "image": "dr_rao.jpeg",
        "badge_title": "Dr. Mula Venkatarao",
        "badge_sub": "Founder & Children Specialist",
        "stats": [
            ("15+ Years Ped. Legacy", "award"),
            ("Dedicated NICU", "baby"),
            ("Complete Vaccination", "shield-check"),
            ("24/7 Child Emergency", "clock")
        ],
        "lead_para": "Children require gentle hands, intuitive diagnosis, and warm emotional care. Founded and directly overseen by Dr. Mula Venkatarao (M.D PAED Niloufer), our Department of Pediatrics is celebrated across Srikakulam for over 15+ years of trusted pediatric excellence.",
        "body_para": "From tender neonatal care for low birth-weight infants to adolescent wellness, our team delivers preventive immunizations, asthma care, infection management, and developmental milestone assessments. Our Neonatal ICU provides radiant warmers, phototherapy, and micro-infusion monitoring for fragile newborns.",
        "capabilities": [
            ("Neonatal Intensive Care (NICU)", "Specialized intensive care for premature infants, neonatal jaundice, and respiratory distress.", "baby"),
            ("Immunization Programs", "Strict cold-chain storage of all pediatric vaccines in accordance with national IAP immunization schedules.", "shield-check"),
            ("Pediatric Respiratory & Asthma", "Specialized nebulization suites and pediatric pulmonary management for wheezing and childhood asthma.", "wind"),
            ("Growth & Developmental Audits", "Comprehensive screening for nutritional optimization, speech milestones, and adolescent health.", "heart")
        ],
        "amenities_title": "Pediatric Treatments & Programs",
        "amenities": [
            "Complete IAP Pediatric Vaccination", "Childhood Asthma & Wheezing Care", "Neonatal Jaundice & Phototherapy",
            "Pediatric Acute Fevers & Dengue", "Gastroenteritis & Dehydration Care", "Nutritional Audits & Failure to Thrive",
            "Pediatric Emergency Trauma Response", "Adolescent Health Counseling"
        ],
        "doctor": {
            "name": "Dr. MULA VENKATARAO",
            "qual": "M.D (PAED Niloufer) · Founder & Chief Pediatrician",
            "desc": "Beloved children's doctor in Srikakulam with 15+ years of distinguished standing, treating generations of healthy children.",
            "img": "dr_rao.jpeg",
            "dept": "Pediatrics"
        }
    },
    "orthopedics": {
        "id": "orthopedics",
        "file": "department-orthopedics.html",
        "title": "Orthopedics & Joint Replacement",
        "title_formatted": "Department of Orthopedics &amp; <span class=\"serif-italic\">Joint Reconstruction</span>",
        "eyebrow": "BONES, JOINTS & SPINE EXCELLENCE",
        "subtitle": "Advanced total joint replacements, arthroscopic sports injury repair, complex trauma surgery, and comprehensive spine disorder care.",
        "icon": "bone",
        "image": "https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Joint Replacement Team",
        "badge_sub": "Minimally Invasive Ortho Surgeries",
        "stats": [
            ("Total Knee & Hip Replacements", "bone"),
            ("Arthroscopic Keyhole Surgery", "layers"),
            ("24/7 Trauma Fracture Fixation", "zap"),
            ("Class 100 Laminar OTs", "shield-check")
        ],
        "lead_para": "Restoring painless mobility and structural strength is our mission. The Department of Orthopedics at A1 Hospital is led by distinguished surgeons Dr. Sattaru Kishore Babu and Dr. Bammidi Sai Theja, delivering modern musculoskeletal solutions.",
        "body_para": "Operating inside Class 100 laminar airflow theatres to ensure absolute implant sterility, our surgeons perform primary and revision total knee and hip replacements using anatomical alignment techniques. We provide keyhole arthroscopy for ligament tears and round-the-clock fixation for complex trauma fractures.",
        "capabilities": [
            ("Total Knee & Hip Replacement", "State-of-the-art prosthetic joint reconstruction restoring natural joint motion and relieving arthritis pain.", "bone"),
            ("Keyhole Arthroscopic Surgery", "Minimally invasive repair of ACL/PCL tears, meniscus injuries, and recurrent shoulder dislocations.", "layers"),
            ("Complex Polytrauma Fixation", "Immediate biological plating, intramedullary nailing, and external fixation of severe accident fractures.", "zap"),
            ("Spine Disorder Care", "Conservative and surgical management of lumbar disc herniation, sciatica, and cervical spondylosis.", "activity")
        ],
        "amenities_title": "Orthopedic Procedures & Specialties",
        "amenities": [
            "Total Knee Arthroplasty (TKR)", "Total Hip Replacement (THR)", "Arthroscopic ACL & Meniscus Repair",
            "Complex Pelvic & Acetabular Trauma", "Pediatric Fracture Management", "Cervical & Lumbar Spondylosis Care",
            "Osteoporosis Screenings & Bone Density", "Post-Surgical Physiotherapy Unit"
        ],
        "doctor": {
            "name": "Dr. Sattaru Kishore Babu & Dr. Bammidi Sai Theja",
            "qual": "M.S. (Ortho) & MS Ortho, FIJR, FIASM (Fellow in Joint Replacement)",
            "desc": "Renowned orthopedic surgeons specializing in high-flexion joint replacements, arthroscopy, and trauma stabilization.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Orthopedics"
        }
    },
    "generalsurgery": {
        "id": "generalsurgery",
        "file": "department-generalsurgery.html",
        "title": "General & Laparoscopic Surgery",
        "title_formatted": "Department of General &amp; <span class=\"serif-italic\">Laparoscopic Surgery</span>",
        "eyebrow": "PRECISION SURGICAL CARE",
        "subtitle": "Minimally invasive keyhole surgeries, emergency gastrointestinal procedures, hernia repairs, and advanced day-care surgical interventions.",
        "icon": "scissors",
        "image": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Laparoscopic Suite",
        "badge_sub": "Minimal Pain & Quick Recovery",
        "stats": [
            ("HD Laparoscopic Surgery", "layers"),
            ("Day-Care Discharge", "clock"),
            ("Zero-Infection Standards", "shield-check"),
            ("24/7 Acute Abdomen ER", "zap")
        ],
        "lead_para": "Modern surgical care has transitioned from large painful incisions to refined, precision-targeted interventions. The Department of General and Laparoscopic Surgery at A1 Hospital is led by Dr. K. Chaitanya Kishore (M.S GEN. SURGERY, FMAS).",
        "body_para": "Utilizing high-definition video laparoscopic towers, our surgical team performs minimally invasive procedures with microscopic incisions, minimal tissue trauma, zero blood loss, and rapid discharge within 24 to 48 hours. From appendicitis and gallstones to complex hernia repairs, patient safety is supreme.",
        "capabilities": [
            ("Laparoscopic Cholecystectomy", "Keyhole gallstone removal allowing patients to return home comfortably within 24-48 hours.", "layers"),
            ("Advanced Hernia Repair", "Tension-free mesh hernia repairs performed laparoscopically with minimal post-op discomfort.", "shield"),
            ("Emergency Acute Abdomen", "Rapid surgical management for acute appendicitis, bowel perforations, and intestinal obstructions.", "zap"),
            ("Proctology & Day Care", "Painless laser and surgical treatments for piles, anal fissures, fistulas, and pilonidal sinuses.", "heart")
        ],
        "amenities_title": "Surgical Procedures Performed",
        "amenities": [
            "Laparoscopic Appendectomy", "Laparoscopic Gallbladder Removal", "Inguinal & Ventral Mesh Hernioplasty",
            "Laser Proctology (Piles, Fissure, Fistula)", "Thyroid & Parathyroid Surgeries", "Diabetic Foot Ulcer Debridement",
            "Hydrocele & Varicocele Corrections", "Breast Lump & Soft Tissue Excision"
        ],
        "doctor": {
            "name": "Dr. K. Chaitanya Kishore & Dr. C. Balaji",
            "qual": "M.S (GEN. SURGERY), FMAS (Fellow in Minimal Access Surgery)",
            "desc": "Experienced laparoscopic and gastrointestinal surgeons dedicated to painless, minimally invasive surgical outcomes.",
            "img": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "General Surgery"
        }
    },
    "radiology": {
        "id": "radiology",
        "file": "department-radiology.html",
        "title": "Radiology & Medical Imaging",
        "title_formatted": "Department of Radiology &amp; <span class=\"serif-italic\">Medical Imaging</span>",
        "eyebrow": "PRECISION DIAGNOSTIC SCANS",
        "subtitle": "High-resolution multi-slice CT scanning, 4D obstetric ultrasound, color Doppler hemodynamics, and digital radiography.",
        "icon": "scan",
        "image": "https://images.unsplash.com/photo-1538108149393-fbbd81895907?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Digital Imaging Center",
        "badge_sub": "Quick Accurate Scan Reports",
        "stats": [
            ("Multi-Slice Digital CT", "scan"),
            ("4D Color Doppler USG", "eye"),
            ("Digital X-Ray Systems", "layers"),
            ("Same-Day Reporting", "check-circle-2")
        ],
        "lead_para": "Prompt and unambiguous medical imaging is the backbone of clinical decision-making. Headed by Dr. G. Sandeep (M.D RADIOLOGY), the Department of Radiology at A1 Hospital delivers high-clarity diagnostic scans across all clinical specialties.",
        "body_para": "Our digital CT scanner captures razor-sharp anatomical cross-sections for immediate stroke triage, polytrauma evaluation, and abdominal diagnosis. In maternal care, our 4D high-definition ultrasound provides comprehensive fetal anomaly evaluations and color Doppler scans.",
        "capabilities": [
            ("Digital Multi-Slice CT", "Instantaneous non-invasive visualization of brain, thorax, abdomen, and skeletal structures.", "scan"),
            ("4D Obstetric Ultrasound", "Detailed high-resolution fetal morphology scans detecting congenital anomalies early in gestation.", "eye"),
            ("Vascular Color Doppler", "Non-invasive assessment of carotid, arterial, and deep venous circulation to detect blood clots.", "activity"),
            ("High-Frequency Digital X-Ray", "Low-radiation digital radiography for accurate skeletal fracture detection and chest pathology.", "layers")
        ],
        "amenities_title": "Diagnostic Scans & Imaging Portfolio",
        "amenities": [
            "Whole-Body Multi-Slice CT Scanning", "4D Fetal Anomaly Obstetric Ultrasound", "Abdominal & Pelvic Ultrasound",
            "Peripheral Arterial & Venous Doppler", "High-Definition Digital Chest X-Rays", "CT Angiography Protocols",
            "USG-Guided Fine Needle Aspirations", "Emergency Trauma Scan Reporting"
        ],
        "doctor": {
            "name": "Dr. G. SANDEEP",
            "qual": "M.D (RADIOLOGY) · Consultant Radiologist",
            "desc": "Leading expert in diagnostic radiology, CT multi-slice interpretation, and fetal anomaly ultrasound assessments.",
            "img": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Radiology"
        }
    },
    "obg": {
        "id": "obg",
        "file": "department-obg.html",
        "title": "Obstetrics, Gynecology & Fertility (IVF)",
        "title_formatted": "Department of Obstetrics, Gynecology &amp; <span class=\"serif-italic\">Fertility (IVF)</span>",
        "eyebrow": "COMPREHENSIVE WOMEN'S HEALTH",
        "subtitle": "Painless normal deliveries, high-risk pregnancy management, advanced IVF/IUI reproductive fertility treatments, and laparoscopic gynecology.",
        "icon": "heart-handshake",
        "image": "https://images.unsplash.com/photo-1551076805-e1869033e561?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Dr. G. Prameela",
        "badge_sub": "M.S (OBG), FART · Fertility & High-Risk Lead",
        "stats": [
            ("Advanced IVF Center", "sparkles"),
            ("Painless Normal Delivery", "heart"),
            ("High-Risk Pregnancy Unit", "shield-check"),
            ("Laparoscopic Gynaec Surgery", "scissors")
        ],
        "lead_para": "Every mother's journey and every woman's health deserve the highest standard of empathy and clinical mastery. Led by acclaimed obstetrician and fertility expert Dr. G. Prameela (M.S. OBG, FART), our center is Srikakulam's trusted destination for comprehensive maternal care and fertility treatments.",
        "body_para": "We offer complete maternity programs including painless natural birthing options, emergency cesarean services, high-risk pregnancy monitoring, and gestational diabetes care. Our advanced fertility laboratory provides IVF, IUI, follicular monitoring, and personalized counseling to help couples achieve their dream of parenthood.",
        "capabilities": [
            ("Advanced IVF & IUI Center", "State-of-the-art reproductive medicine laboratory helping infertile couples achieve successful conception.", "sparkles"),
            ("Painless Normal Delivery", "Epidural analgesia and continuous fetal telemetry ensuring safe, comfortable natural childbirth.", "heart"),
            ("High-Risk Pregnancy Unit", "Dedicated monitoring for pre-eclampsia, placenta previa, recurrent miscarriages, and gestational diabetes.", "shield-check"),
            ("Laparoscopic Gynaecology", "Keyhole surgeries for ovarian cysts, uterine fibroids, endometriosis, and total laparoscopic hysterectomy.", "scissors")
        ],
        "amenities_title": "Women's Healthcare & Fertility Spectrum",
        "amenities": [
            "In-Vitro Fertilization (IVF) & IUI", "Painless Delivery (Epidural Birthing)", "High-Risk Pregnancy Intensive Care",
            "Laparoscopic Hysterectomy & Myomectomy", "PCOD / PCOS Metabolic Reversal", "Comprehensive Antenatal Checkups",
            "Cervical Cancer Screening (Pap Smear)", "Postnatal Rehabilitation & Lactation Care"
        ],
        "doctor": {
            "name": "Dr. G. PRAMEELA",
            "qual": "M.S. (OBG), FART · Senior Consultant Obstetrician & Fertility Specialist",
            "desc": "Esteemed maternal-fetal medicine and reproductive fertility specialist guiding thousands of safe deliveries and successful IVF pregnancies.",
            "img": "https://images.unsplash.com/photo-1594824813591-9a74b01d0a51?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Obstetrics & Gynecology"
        }
    },
    "pulmonology": {
        "id": "pulmonology",
        "file": "department-pulmonology.html",
        "title": "Pulmonology & Respiratory Medicine",
        "title_formatted": "Department of Pulmonology &amp; <span class=\"serif-italic\">Chest Medicine</span>",
        "eyebrow": "ADVANCED RESPIRATORY CARE",
        "subtitle": "Comprehensive management of asthma, COPD, pneumonia, sleep apnea, post-COVID lung fibrosis, and acute respiratory failure.",
        "icon": "wind",
        "image": "https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Pulmonary Clinic",
        "badge_sub": "PFT Lab & Allergy Screening",
        "stats": [
            ("Pulmonary Function Tests", "wind"),
            ("Nebulization Therapy", "activity"),
            ("ICU Respiratory Support", "shield"),
            ("Allergy & Asthma Clinic", "smile")
        ],
        "lead_para": "Healthy breathing is essential for overall life vitality. The Department of Pulmonology at A1 Hospital delivers diagnosis and therapy for acute and chronic respiratory disorders affecting the lungs, bronchial tree, and pleura.",
        "body_para": "Equipped with computerized Spirometry (Pulmonary Function Testing), aerosol nebulization bays, and non-invasive BiPAP/CPAP ventilation systems, our chest specialists manage difficult asthma, chronic obstructive pulmonary disease (COPD), severe pneumonia, and sleep-related breathing disorders.",
        "capabilities": [
            ("Computerized Spirometry (PFT)", "Measures lung capacities, airway resistance, and reversibility to guide tailored inhaler therapy.", "wind"),
            ("COPD & Asthma Management", "Multi-stage therapy incorporating bronchodilators, inhaled corticosteroids, and pulmonary rehab.", "shield-check"),
            ("Non-Invasive Ventilation", "BiPAP and CPAP therapy preventing endotracheal intubation in acute hypercapnic respiratory failure.", "activity"),
            ("Pleural Effusion & Thoracentesis", "Diagnostic and therapeutic drainage of fluid collections around the lungs with ultrasound guidance.", "layers")
        ],
        "amenities_title": "Conditions Managed & Respiratory Services",
        "amenities": [
            "Chronic Bronchial Asthma", "COPD & Smoker's Cough", "Acute Bacterial & Viral Pneumonias",
            "Pleural Effusion Drainage", "Tuberculosis Diagnosis & DOTS", "Obstructive Sleep Apnea (OSA)",
            "Post-Viral Pulmonary Fibrosis", "Smoking Cessation Counseling"
        ],
        "doctor": {
            "name": "Senior Consultant Pulmonologist",
            "qual": "M.D (Pulmonary Medicine), DTCD",
            "desc": "Experienced chest physician specializing in asthma control, allergy mapping, and advanced mechanical respiratory care.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Pulmonology"
        }
    },
    "dermatology": {
        "id": "dermatology",
        "file": "department-dermatology.html",
        "title": "Dermatology & Cosmetology",
        "title_formatted": "Department of Dermatology &amp; <span class=\"serif-italic\">Skin Health</span>",
        "eyebrow": "ADVANCED DERMATOLOGICAL CARE",
        "subtitle": "Evidence-based clinical treatments for acne, psoriasis, fungal skin infections, hair loss, eczema, and skin pigmentation disorders.",
        "icon": "sparkles",
        "image": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Skin & Hair Clinic",
        "badge_sub": "Clinical & Cosmetic Dermatology",
        "stats": [
            ("Psoriasis & Eczema Care", "sparkles"),
            ("Advanced Hair Loss Therapy", "layers"),
            ("Allergy Patch Testing", "shield-check"),
            ("Medical Dermatosurgery", "scissors")
        ],
        "lead_para": "Healthy skin reflects internal wellness. The Department of Dermatology at A1 Hospital delivers evidence-based clinical and cosmetic dermatological treatments for patients of all ages, from pediatric atopic eczema to chronic adult psoriasis.",
        "body_para": "Our clinic combines clinical diagnostics with targeted medical therapies, treating stubborn fungal infections, cystic acne, autoimmune vitiligo, and hair thinning. We prioritize safe, scientifically validated treatments tailored to Indian skin types.",
        "capabilities": [
            ("Psoriasis & Chronic Eczema", "Systemic biological therapies, topical formulations, and lifestyle interventions.", "sparkles"),
            ("Acne & Pigmentation Clinic", "Medical management of severe cystic acne, melasma, and post-inflammatory hyperpigmentation.", "smile"),
            ("Trichology (Hair & Scalp)", "Comprehensive evaluation of alopecia, telogen effluvium, and dandruff with targeted medical therapies.", "layers"),
            ("Minor Dermatosurgery", "Painless electro-cautery and radiofrequency excision of skin tags, warts, moles, and epidermal cysts.", "scissors")
        ],
        "amenities_title": "Clinical Conditions Treated",
        "amenities": [
            "Severe Acne & Scarring", "Psoriasis & Autoimmune Skin Diseases", "Fungal & Bacterial Skin Infections",
            "Alopecia & Chronic Hair Thinning", "Eczema & Atopic Dermatitis", "Vitiligo & Hypopigmentation",
            "Radiofrequency Mole & Tag Removal", "Contact Dermatitis Allergy Workups"
        ],
        "doctor": {
            "name": "Senior Consultant Dermatologist",
            "qual": "M.D (DVL) · Consultant Dermatologist & Venereologist",
            "desc": "Specialized in clinical dermatology, immunological skin conditions, and modern aesthetic dermatosurgery.",
            "img": "https://images.unsplash.com/photo-1594824813591-9a74b01d0a51?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Dermatology"
        }
    },
    "urology": {
        "id": "urology",
        "file": "department-urology.html",
        "title": "Urology & Endourology",
        "title_formatted": "Department of Urology &amp; <span class=\"serif-italic\">Renal Surgery</span>",
        "eyebrow": "ADVANCED UROLOGICAL CARE",
        "subtitle": "Minimally invasive laser kidney stone fragmentation, prostate enlargement surgery (TURP), and urinary tract reconstructive care.",
        "icon": "shield-plus",
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Laser Urology Unit",
        "badge_sub": "Painless Kidney Stone Removal",
        "stats": [
            ("Holmium Laser Lithotripsy", "zap"),
            ("TURP Prostate Surgery", "shield"),
            ("Stricture Urethra Repair", "layers"),
            ("Day-Care Endourology", "clock")
        ],
        "lead_para": "Urological conditions require high-precision endoscopic optics and gentle surgical management. Headed by Dr. Budumuru Ramana (Consultant Urologist), the Department of Urology at A1 Hospital offers cutting-edge endourological procedures.",
        "body_para": "Utilizing advanced endoscopic laser lithotripsy, kidney stones are pulverized into dust through natural urinary passages without surgical cuts. We provide transurethral resection of the prostate (TURP) for benign prostatic hyperplasia and manage urinary tract infections and malignancies.",
        "capabilities": [
            ("Laser Kidney Stone Removal", "Retrograde intrarenal surgery (RIRS) and ureteroscopy (URS) destroying stones without cuts.", "zap"),
            ("Transurethral Prostate Resection", "Minimally invasive TURP relieving urinary obstruction caused by enlarged prostate glands.", "shield-plus"),
            ("Pediatric Urology", "Surgical correction of undescended testes, congenital hydronephrosis, and pelviureteric junctions.", "baby"),
            ("Recurrent UTI Management", "Thorough diagnostic microbiological workups to eradicate resistant urinary tract infections.", "activity")
        ],
        "amenities_title": "Urological Procedures & Conditions",
        "amenities": [
            "Laser Kidney & Ureteric Stone Lithotripsy (RIRS/URS)", "Transurethral Resection of Prostate (TURP)",
            "Percutaneous Nephrolithotomy (PCNL)", "Urethral Stricture Dilation & Urethroplasty",
            "Hematuria (Blood in Urine) Investigation", "Varicocelectomy & Hydrocele Repair",
            "Bladder Tumor Resection (TURBT)", "Neurogenic Bladder Management"
        ],
        "doctor": {
            "name": "Dr. Budumuru Ramana",
            "qual": "M.S, M.Ch (Urology) · Consultant Urologist & Andrologist",
            "desc": "Pioneer in laser endourology, retrograde intrarenal surgery, and minimally invasive prostate operations.",
            "img": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Urology"
        }
    },
    "criticalcare": {
        "id": "criticalcare",
        "file": "department-criticalcare.html",
        "title": "Critical Care & Emergency Medicine",
        "title_formatted": "Department of Critical Care &amp; <span class=\"serif-italic\">Intensive Medicine</span>",
        "eyebrow": "24/7 INTENSIVE CARE VIGILANCE",
        "subtitle": "High-dependency multi-bed adult intensive care unit overseen 24/7 by critical care physicians for sepsis, multi-organ shock, and respiratory failure.",
        "icon": "activity",
        "image": "https://images.unsplash.com/photo-1584516150909-c43483ee7932?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Critical Care Unit",
        "badge_sub": "24/7 Intensivist Vigilance",
        "stats": [
            ("Advanced Invasive Ventilators", "wind"),
            ("Central Venous & Arterial Lines", "activity"),
            ("Continuous Hemofiltration", "filter"),
            ("1:1 Nursing Oversight", "user-check")
        ],
        "lead_para": "When illness progresses to life-threatening stages, immediate organ support and continuous surveillance are crucial. Headed by Dr. P. Siva Kumar (M.D GEN. MED), our Department of Critical Care Medicine operates around the clock.",
        "body_para": "Staffed by trained intensivists and critical care nurses, our unit specializes in severe septic shock, acute respiratory distress syndrome (ARDS), diabetic ketoacidosis, acute poisoning, and postoperative hemodynamic instability.",
        "capabilities": [
            ("Advanced Mechanical Ventilation", "Lung-protective ventilation protocols calibrated to support compromised respiratory function.", "wind"),
            ("Invasive Hemodynamic Monitoring", "Arterial blood pressure monitoring and central line access for inotrope infusions.", "activity"),
            ("Severe Sepsis Resuscitation", "Protocolized sepsis resuscitation bundles targeting prompt antibiotic coverage and lactate clearance.", "shield-check"),
            ("Multidisciplinary Rounds", "Daily rounds integrating surgeons, cardiologists, and nephrologists to coordinate comprehensive care.", "users")
        ],
        "amenities_title": "Critical Care Protocols & Services",
        "amenities": [
            "Severe Sepsis & Septic Shock", "Acute Respiratory Distress Syndrome (ARDS)", "Diabetic Ketoacidosis & Coma",
            "Polytrauma & Post-Surgical Recovery", "Acute Poisoning & Toxic Ingestions", "Bedside Ultrasound & Echocardiography",
            "Continuous 1:1 Nursing Supervision", "Arterial Blood Gas Lab Integration"
        ],
        "doctor": {
            "name": "Dr. P. Siva Kumar",
            "qual": "M.D (GEN. MED) · Consultant Physician & Critical Care Specialist",
            "desc": "Leading intensivist recognized for clinical expertise in sepsis reversal, respiratory ventilation, and emergency resuscitation.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Critical Care"
        }
    },
    "oncology": {
        "id": "oncology",
        "file": "department-oncology.html",
        "title": "Oncology & Cancer Care",
        "title_formatted": "Department of Oncology &amp; <span class=\"serif-italic\">Cancer Center</span>",
        "eyebrow": "COMPASSIONATE CANCER MEDICINE",
        "subtitle": "Multidisciplinary cancer diagnostics, systemic chemotherapy administration, cancer screening programs, and palliative pain management.",
        "icon": "crosshair",
        "image": "https://images.unsplash.com/photo-1579154204601-01588f351e67?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Dr. Navya Madabatula",
        "badge_sub": "Radiation & Clinical Oncologist",
        "stats": [
            ("Early Cancer Screenings", "shield-check"),
            ("Day-Care Chemotherapy", "activity"),
            ("Tumor Board Consensus", "users"),
            ("Palliative & Pain Relief", "heart")
        ],
        "lead_para": "Navigating a cancer diagnosis requires medical excellence combined with emotional compassion. Headed by Dr. Navya Madabatula (Radiation & Clinical Oncologist), our Oncology Department delivers patient-centered oncology care.",
        "body_para": "We offer preventive cancer screenings for early breast, cervical, and gastrointestinal malignancies. Our outpatient chemotherapy bay is equipped with infusion safety systems for comfortable systemic chemotherapy, immunotherapy, and pain management.",
        "capabilities": [
            ("Day-Care Chemotherapy Suite", "Comfortable recliner suites with laminar safety hoods ensuring sterile infusion of antineoplastic agents.", "activity"),
            ("Comprehensive Cancer Screenings", "Mammography, ultrasound, Pap smears, and CT imaging for timely early-stage tumor detection.", "shield-check"),
            ("Multidisciplinary Tumor Board", "Collaborative review involving oncologists, surgical leads, and radiologists for every patient.", "users"),
            ("Palliative Care & Pain Therapy", "Specialized analgesic titration and supportive nutrition improving patient quality of life.", "heart")
        ],
        "amenities_title": "Oncological Services & Programs",
        "amenities": [
            "Outpatient Chemotherapy Infusions", "Breast & Cervical Cancer Screening", "Gastrointestinal Cancer Evaluations",
            "Hematological Malignancy Consultations", "Cancer Pain Management Clinic", "Palliative Care & Family Counseling",
            "Post-Chemotherapy Blood Count Monitoring", "Nutritional Support for Cancer Patients"
        ],
        "doctor": {
            "name": "Dr. Navya Madabatula",
            "qual": "M.B.B.S, DNB (Radiation & Clinical Oncology)",
            "desc": "Experienced clinical oncologist dedicated to evidence-based cancer protocols, targeted therapy, and patient comfort.",
            "img": "https://images.unsplash.com/photo-1594824813591-9a74b01d0a51?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Oncology"
        }
    },
    "nephrology": {
        "id": "nephrology",
        "file": "department-nephrology.html",
        "title": "Nephrology & Renal Dialysis",
        "title_formatted": "Department of Nephrology &amp; <span class=\"serif-italic\">Kidney Care</span>",
        "eyebrow": "ADVANCED RENAL HEALTH",
        "subtitle": "Specialized diagnosis and therapy for chronic kidney disease, diabetic nephropathy, hypertension management, and modern hemodialysis.",
        "icon": "filter",
        "image": "https://images.unsplash.com/photo-1582750433449-648ed127bb54?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Dr. Korla Vidya Sagar",
        "badge_sub": "Consultant Nephrologist",
        "stats": [
            ("Hemodialysis Units", "filter"),
            ("Diabetic Kidney Care", "activity"),
            ("Hypertension Optimization", "heart"),
            ("Vascular Access Maintenance", "shield-check")
        ],
        "lead_para": "Kidney health is vital to systemic physiological balance. Led by Dr. Korla Vidya Sagar (Consultant Nephrologist), the Department of Nephrology at A1 Hospital manages acute kidney injury and chronic renal conditions.",
        "body_para": "Our facility houses advanced computerized hemodialysis machines utilizing treated reverse-osmosis water to guarantee clean filtration. We specialize in slowing the progression of diabetic nephropathy, treating nephrotic syndrome, and optimizing blood pressure control.",
        "capabilities": [
            ("Modern Hemodialysis Unit", "Advanced hemodialysis stations operating under sterile protocols with continuous nursing surveillance.", "filter"),
            ("Diabetic Nephropathy Control", "Aggressive proteinuria reduction and metabolic control to preserve native kidney function.", "activity"),
            ("Acute Kidney Injury (AKI) Care", "Prompt identification and reversal of acute renal insults caused by infections or dehydration.", "shield-check"),
            ("Vascular Access Oversight", "Surveillance and care of AV fistulas and temporary hemodialysis catheter placements.", "layers")
        ],
        "amenities_title": "Renal Treatments & Clinical Services",
        "amenities": [
            "Outpatient Maintenance Hemodialysis", "Chronic Kidney Disease (CKD) Management", "Diabetic Nephropathy Screening",
            "Hypertension & Renal Artery Evaluations", "Glomerulonephritis & Nephrotic Syndrome", "Electrolyte & Acid-Base Imbalances",
            "Temporary Dialysis Catheter Insertion", "Renal Dietitian Nutrition Counseling"
        ],
        "doctor": {
            "name": "Dr. Korla Vidya Sagar",
            "qual": "M.D, DM (Nephrology) · Consultant Nephrologist",
            "desc": "Renowned kidney specialist pioneering advanced hemodialysis protocols and diabetic nephropathy preservation therapies.",
            "img": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Nephrology"
        }
    },
    "ophthalmology": {
        "id": "ophthalmology",
        "file": "department-ophthalmology.html",
        "title": "Ophthalmology & Eye Care",
        "title_formatted": "Department of Ophthalmology &amp; <span class=\"serif-italic\">Vision Sciences</span>",
        "eyebrow": "ADVANCED VISION CARE",
        "subtitle": "Micro-incision cataract phacoemulsification, glaucoma screening, diabetic retinopathy evaluation, and complete refractive vision correction.",
        "icon": "eye",
        "image": "https://images.unsplash.com/photo-1594824436967-4638a16fb8e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "badge_title": "Dr. Palepu Srikanthi",
        "badge_sub": "Consultant Eye Surgeon",
        "stats": [
            ("Phaco Cataract Surgery", "eye"),
            ("Diabetic Retinopathy Screening", "scan"),
            ("Glaucoma Tonometry", "activity"),
            ("Day-Care Discharge", "clock")
        ],
        "lead_para": "Clear sight illuminates every moment of life. Led by Dr. Palepu Srikanthi (Consultant Ophthalmologist), the Department of Ophthalmology delivers eye care ranging from computerized refraction to advanced micro-incision surgeries.",
        "body_para": "Equipped with slit-lamp bio-microscopes, non-contact tonometers, and operating microscopes, our ophthalmic clinic provides stitchless, painless phacoemulsification cataract surgery with premium intraocular lens (IOL) implantation.",
        "capabilities": [
            ("Phacoemulsification Cataract", "Stitchless keyhole cataract removal through a 2.2mm incision with foldable intraocular lens implantation.", "eye"),
            ("Diabetic Retinopathy Workup", "Detailed fundus examination detecting retinal micro-aneurysms and maculopathy in diabetic patients.", "scan"),
            ("Glaucoma Pressure Screening", "Applanation tonometry and optic nerve head evaluation for early detection of optic nerve damage.", "activity"),
            ("Refraction & Pediatric Eye Care", "Accurate computerized vision testing and pediatric amblyopia (lazy eye) treatments.", "smile")
        ],
        "amenities_title": "Ophthalmic Services & Procedures",
        "amenities": [
            "Stitchless Phaco Cataract Surgery", "Premium Intraocular Lens (IOL) Implants", "Diabetic Eye & Retinal Screening",
            "Glaucoma Pressure & Field Testing", "Computerized Refraction & Eyeglass Rx", "Dry Eye Syndrome & Allergy Care",
            "Pterygium Excision with Conjunctival Autograft", "Foreign Body Removal & Ocular Trauma"
        ],
        "doctor": {
            "name": "Dr. Palepu Srikanthi",
            "qual": "M.B.B.S, M.S (Ophthalmology) · Eye Surgeon",
            "desc": "Experienced eye surgeon specializing in sutureless phaco cataract surgery and diabetic retinal evaluations.",
            "img": "https://images.unsplash.com/photo-1594824813591-9a74b01d0a51?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "dept": "Ophthalmology"
        }
    }
}

print(f"Loaded {len(SERVICES_DATA)} services and {len(DEPARTMENTS_DATA)} departments.")
