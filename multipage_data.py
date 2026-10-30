# A1 Hospital - Streamlined Authentic Clinical Data
# Matches EXACTLY the real doctor nameplates and photos provided by the user.

HOSPITAL_CONTACT = {
    "website": "https://www.a1hospitalsrikakulam.com",
    "domain": "www.a1hospitalsrikakulam.com",
    "phone_1": "08942-228234",
    "phone_2": "08942-227234",
    "whatsapp_number": "6399144444",
    "whatsapp_link": "https://wa.me/916399144444?text=Hello%20A1%20Hospital,%20I%20would%20like%20to%20inquire%20about%20an%20appointment.",
    "email": "a1hospitalsrikakulam@gmail.com",
    "address": "Opposite Rama Temple, Bondilipuram Main Road, Srikakulam, AP",
    "map_embed": "https://maps.google.com/maps?q=Opposite+Rama+Temple,+Bondilipuram+Main+Road,+Srikakulam,+AP&t=&z=16&ie=UTF8&iwloc=&output=embed"
}

# The Verified Doctors from user's photos & leadership
DOCTORS_DATA = [
    {
        "id": "dr-mula-venkatarao",
        "name": "Dr. Mula Venkatarao",
        "qual": "M.D (PAED) NILOUFER",
        "title": "Children Specialist (Founder)",
        "dept": "Pediatrics & Child Health",
        "exp": "13+ Years Pediatric Excellence",
        "desc": "Hospital Founder with 13+ years of clinical excellence in newborn care, childhood illnesses, and pediatric wellness.",
        "image": "dr_rao.jpeg",
        "icon": "baby"
    },
    {
        "id": "dr-g-prameela",
        "name": "Dr. G. Prameela",
        "qual": "M.S. (OBG) FART, FMAS",
        "title": "Senior Obstetrician & Gynaecologist (IVF Specialist)",
        "dept": "Obstetrics, Gynaecology & IVF Clinic",
        "exp": "13+ Years Women's Care & IVF",
        "desc": "Senior Specialist in high-risk pregnancy, infertility evaluation, advanced reproductive technology (IVF/FART), and laparoscopy.",
        "image": "dr_prameela.png",
        "icon": "heart-pulse"
    },
    {
        "id": "dr-kannepalli-srinivas",
        "name": "Dr. Kannepalli Srinivas",
        "qual": "M.S., M.CH. PAEDIATRIC SURGERY",
        "title": "Pediatric Surgeon",
        "dept": "Pediatrics & Child Health",
        "exp": "Pediatric Surgical Specialist",
        "desc": "Specialist in pediatric surgical care, neonatal interventions, and congenital anomaly corrections.",
        "image": None,
        "icon": "baby"
    },
    {
        "id": "dr-sattaru-kishore-babu",
        "name": "Dr. Sattaru. Kishore Babu",
        "qual": "M.S., (ORTHO)",
        "title": "Orthopaedic Surgeon",
        "dept": "Orthopedics & Joint Surgery",
        "exp": "Senior Orthopedic Surgeon",
        "desc": "Senior orthopedic surgeon specializing in fracture fixation, joint care, and musculoskeletal trauma.",
        "image": None,
        "icon": "bone"
    },
    {
        "id": "dr-bammidi-sai-theja",
        "name": "Dr. Bammidi Sai Theja",
        "qual": "MS Ortho, FIJR, FIASM",
        "title": "Orthopaedic Surgeon",
        "dept": "Orthopedics & Joint Surgery",
        "exp": "Joint Replacement Fellow",
        "desc": "Fellow in Joint Replacement and Arthroscopic Sports Surgery, managing arthritis, knee, and ligament repairs.",
        "image": None,
        "icon": "activity"
    },
    {
        "id": "dr-hanumanthu-anilkumar",
        "name": "Dr. Hanumanthu Anilkumar",
        "qual": "M.D (General Medicine)",
        "title": "General Physician",
        "dept": "General Medicine",
        "exp": "Consultant Physician",
        "desc": "Consultant physician managing adult fevers, diabetes, hypertension, and multi-system medical illnesses.",
        "image": None,
        "icon": "stethoscope"
    },
    {
        "id": "dr-chittipotula-balaji",
        "name": "Dr. Chittipotula Balaji",
        "qual": "M.B.B.S., MS (GENERAL SURGERY)",
        "title": "General Surgeon",
        "dept": "General Surgery",
        "exp": "General & Laparoscopic Surgeon",
        "desc": "Expert surgeon performing hernia repairs, appendectomy, piles/fissure procedures, and emergency abdominal care.",
        "image": None,
        "icon": "scissors"
    },
    {
        "id": "dr-korla-vidya-sagar",
        "name": "Dr. Korla Vidya Sagar",
        "qual": "M.D., DM, NEPHROLOGY",
        "title": "Nephrologist",
        "dept": "Nephrology (Kidney Care)",
        "exp": "Nephrology Specialist",
        "desc": "Kidney specialist managing chronic kidney disease, dialysis care, and diabetic nephropathy.",
        "image": None,
        "icon": "filter"
    },
    {
        "id": "dr-budumuru-ramana",
        "name": "Dr. Budumuru Ramana",
        "qual": "M.S., MCH",
        "title": "Urologist",
        "dept": "Urology",
        "exp": "Consultant Urologist",
        "desc": "Specialist in urinary tract conditions, kidney stones, and minimally invasive endourology.",
        "image": None,
        "icon": "shield-plus"
    },
    {
        "id": "dr-palepu-srikanthi",
        "name": "Dr. Palepu Srikanthi",
        "qual": "M.S., OPHTHALMOLOGY",
        "title": "Ophthalmologist",
        "dept": "Ophthalmology (Eye Care)",
        "exp": "Eye Specialist",
        "desc": "Eye specialist providing vision evaluations, cataract assessments, glaucoma checks, and eye care.",
        "image": None,
        "icon": "eye"
    },
    {
        "id": "dr-navya-madabatula",
        "name": "Dr. Navya Madabatula",
        "qual": "M.B.B.S, M.D., M.D.",
        "title": "Senior Consultant Radiation & Clinical Oncologist",
        "dept": "Oncology (Cancer Care)",
        "exp": "Clinical Oncologist",
        "desc": "Consultant oncologist guiding cancer evaluations, early screenings, and radiation therapy planning.",
        "image": None,
        "icon": "crosshair"
    }
]

# The Real Clinical Departments Matching the Doctors (Crisp 1-2 sentence descriptions & high quality imagery)
DEPARTMENTS_DATA = {
    "pediatrics": {
        "id": "pediatrics",
        "file": "department-pediatrics.html",
        "title": "Pediatrics & Child Health",
        "tag": "Children & Newborn Care",
        "icon": "baby",
        "image": "dept_pediatrics.jpg",
        "meaning": "Dedicated healthcare for infants, children, and adolescents, providing routine immunizations, fever management, and specialized pediatric surgery.",
        "highlights": [
            "13+ Years of Dedicated Pediatric Clinical Excellence",
            "Specialized Pediatric Surgical Care & Emergency Interventions",
            "Complete Child Immunization & Vaccination Schedules",
            "Dedicated Newborn & Neonatal Monitoring"
        ],
        "doctors": [
            {
                "name": "Dr. Mula Venkatarao",
                "qual": "M.D (PAED) NILOUFER",
                "title": "Children Specialist (Founder)",
                "image": "dr_rao.jpeg"
            },
            {
                "name": "Dr. Kannepalli Srinivas",
                "qual": "M.S., M.CH. PAEDIATRIC SURGERY",
                "title": "Pediatric Surgeon",
                "image": None
            }
        ]
    },
    "obstetrics": {
        "id": "obstetrics",
        "file": "department-obstetrics.html",
        "title": "Obstetrics, Gynaecology & IVF Clinic",
        "tag": "Women's Health & Fertility Care",
        "icon": "heart-pulse",
        "image": "dept_obstetrics.jpg",
        "meaning": "Comprehensive women's healthcare offering compassionate antenatal care, normal delivery, infertility evaluation, IVF guidance, and laparoscopic procedures.",
        "highlights": [
            "Comprehensive Antenatal & Safe Childbirth Care",
            "Infertility Evaluation & Advanced Reproductive Technology (FART)",
            "Laparoscopic Gynaecological Surgery (FMAS)",
            "High-Risk Pregnancy & Women's Health Consultations"
        ],
        "doctors": [
            {
                "name": "Dr. G. Prameela",
                "qual": "M.S. (OBG) FART, FMAS",
                "title": "Senior Obstetrician & Gynaecologist (IVF Specialist)",
                "image": "dr_prameela.png"
            }
        ]
    },
    "orthopedics": {
        "id": "orthopedics",
        "file": "department-orthopedics.html",
        "title": "Orthopedics & Joint Surgery",
        "tag": "Bone, Joint & Spine Care",
        "icon": "bone",
        "image": "dept_orthopedics.jpg",
        "meaning": "Advanced diagnosis and surgical treatment for accidental bone fractures, joint arthritis, knee replacements, and sports injuries.",
        "highlights": [
            "Advanced Joint Replacements & Arthroscopy Care",
            "24/7 Fracture Fixation & Accident Trauma Care",
            "Care for Knee Arthritis, Shoulder & Hip Problems",
            "Sterile Operation Theatres for Safe Bone Surgeries"
        ],
        "doctors": [
            {
                "name": "Dr. Sattaru. Kishore Babu",
                "qual": "M.S., (ORTHO)",
                "title": "Orthopaedic Surgeon",
                "image": None
            },
            {
                "name": "Dr. Bammidi Sai Theja",
                "qual": "MS Ortho, FIJR, FIASM",
                "title": "Orthopaedic Surgeon",
                "image": None
            }
        ]
    },
    "generalmedicine": {
        "id": "generalmedicine",
        "file": "department-generalmedicine.html",
        "title": "General Medicine",
        "tag": "Adult Physician & Internal Care",
        "icon": "stethoscope",
        "image": "dept_generalmedicine.jpg",
        "meaning": "Comprehensive diagnosis and medical management for diabetes, hypertension, seasonal fevers, respiratory infections, and adult wellness.",
        "highlights": [
            "Comprehensive Medical Diagnosis & Treatment",
            "Management of Diabetes, Hypertension & Fevers",
            "Continuous Inpatient Medical Supervision",
            "Preventive Health Checkups & Lifestyle Guidance"
        ],
        "doctors": [
            {
                "name": "Dr. Hanumanthu Anilkumar",
                "qual": "M.D (General Medicine)",
                "title": "General Physician",
                "image": None
            }
        ]
    },
    "generalsurgery": {
        "id": "generalsurgery",
        "file": "department-generalsurgery.html",
        "title": "General Surgery",
        "tag": "Operative & Surgical Treatments",
        "icon": "scissors",
        "image": "dept_generalsurgery.jpg",
        "meaning": "Precision operative procedures for hernia repairs, appendectomy, gallbladder stones, piles/fissures, and emergency surgical care.",
        "highlights": [
            "Hernia Repairs, Appendectomy & Gallbladder Procedures",
            "Treatments for Piles, Anal Fissures & Fistulas",
            "Emergency Surgical Care & Abscess Drainage",
            "Clean Post-Operative Inpatient Recovery"
        ],
        "doctors": [
            {
                "name": "Dr. Chittipotula Balaji",
                "qual": "M.B.B.S., MS (GENERAL SURGERY)",
                "title": "General Surgeon",
                "image": None
            }
        ]
    },
    "nephrology": {
        "id": "nephrology",
        "file": "department-nephrology.html",
        "title": "Nephrology (Kidney Care)",
        "tag": "Kidney & Renal Health",
        "icon": "filter",
        "image": "dept_nephrology.jpg",
        "meaning": "Specialized renal medicine focusing on chronic kidney disease management, dialysis support, hypertension control, and diabetic kidney health.",
        "highlights": [
            "Specialized Kidney Disease Diagnosis & Treatment",
            "Diabetic Kidney Disease Management",
            "Dialysis Support & Fluid Balance Care",
            "Electrolyte & Proteinuria Management"
        ],
        "doctors": [
            {
                "name": "Dr. Korla Vidya Sagar",
                "qual": "M.D., DM, NEPHROLOGY",
                "title": "Nephrologist",
                "image": None
            }
        ]
    },
    "urology": {
        "id": "urology",
        "file": "department-urology.html",
        "title": "Urology",
        "tag": "Urinary & Stone Treatments",
        "icon": "shield-plus",
        "image": "dept_urology.jpg",
        "meaning": "Advanced medical and surgical treatment for kidney stones, urinary tract disorders, prostate conditions, and minimally invasive endourology.",
        "highlights": [
            "Diagnosis & Treatment of Kidney & Bladder Stones",
            "Care for Prostate Enlargement & Urinary Flow Issues",
            "Recurrent Urinary Tract Infection (UTI) Management",
            "Minimally Invasive Endourological Procedures"
        ],
        "doctors": [
            {
                "name": "Dr. Budumuru Ramana",
                "qual": "M.S., MCH",
                "title": "Urologist",
                "image": None
            }
        ]
    },
    "ophthalmology": {
        "id": "ophthalmology",
        "file": "department-ophthalmology.html",
        "title": "Ophthalmology (Eye Care)",
        "tag": "Vision & Optical Care",
        "icon": "eye",
        "image": "dept_ophthalmology.jpg",
        "meaning": "Comprehensive eyesight evaluations, cataract assessments, glaucoma screenings, and targeted medical treatment for ocular conditions.",
        "highlights": [
            "Eye Health Assessments & Vision Testing",
            "Cataract Evaluation & Treatment Planning",
            "Glaucoma Pressure Screening & Dry Eye Care",
            "Treatment for Eye Allergies & Infections"
        ],
        "doctors": [
            {
                "name": "Dr. Palepu Srikanthi",
                "qual": "M.S., OPHTHALMOLOGY",
                "title": "Ophthalmologist",
                "image": None
            }
        ]
    },
    "oncology": {
        "id": "oncology",
        "file": "department-oncology.html",
        "title": "Oncology (Cancer Care)",
        "tag": "Radiation & Clinical Oncology",
        "icon": "crosshair",
        "image": "dept_oncology.jpg",
        "meaning": "Compassionate cancer evaluations providing early cancer detection screenings, clinical oncology reviews, and radiation planning.",
        "highlights": [
            "Expert Clinical Oncology Consultations",
            "Early Cancer Screening & Diagnosis Guidance",
            "Radiation Oncology Consultation & Planning",
            "Supportive & Palliative Patient Counseling"
        ],
        "doctors": [
            {
                "name": "Dr. Navya Madabatula",
                "qual": "M.B.B.S, M.D., M.D.",
                "title": "Senior Consultant Radiation & Clinical Oncologist",
                "image": None
            }
        ]
    }
}

# The 5 Core Real Hospital Services (Facility-focused, now includes Pharmacy Services)
SERVICES_DATA = {
    "beds": {
        "id": "beds",
        "file": "service-beds.html",
        "title": "100+ Beds Available",
        "tag": "Inpatient Accommodation",
        "icon": "bed-double",
        "image": None,
        "meaning": "100+ Inpatient Beds refers to our hospital's capacity to admit and care for patients who need overnight observation, post-surgery recovery, or continuous medical treatment. It offers private, semi-private, and sterile general wards.",
        "highlights": [
            "100+ Clean, Air-Conditioned Inpatient Beds",
            "24/7 Central Oxygen & Bedside Nurse Bell System",
            "Continuous Patient Monitoring & Round-the-Clock Nursing",
            "Hygienic En-Suite Facilities & Attendant Comfort Amenities"
        ],
        "readiness": "24/7 Admitting Facility",
        "features": [
            "Sterile Air-Conditioned Patient Rooms",
            "Deluxe Private Suites & General Care Units",
            "Round-the-Clock Dedicated Nursing Staff",
            "Immediate Inpatient Medical Attention"
        ]
    },
    "emergency": {
        "id": "emergency",
        "file": "service-emergency.html",
        "title": "24/7 Emergency Care",
        "tag": "Round-the-Clock Emergency",
        "icon": "clock",
        "image": None,
        "meaning": "24/7 Emergency Care means our casualty department is open day and night, 365 days a year, ready to provide immediate medical attention for sudden accidents, acute chest pain, breathlessness, injuries, and critical medical emergencies without delay.",
        "highlights": [
            "Always Open: 24 Hours a Day, 365 Days a Year",
            "Immediate Triage & Resuscitation Equipment Ready",
            "Direct Support for Road Traffic Accidents & Trauma",
            "Direct Access to Oxygen, Defibrillators & Emergency Treatment"
        ],
        "readiness": "Always Open 24/7",
        "features": [
            "Immediate Patient Triage & Assessment",
            "Trauma Care & Resuscitation Bays",
            "Advanced Multi-Parameter Vital Monitoring",
            "24/7 On-Duty Critical Care Medical Staff"
        ]
    },
    "ambulance": {
        "id": "ambulance",
        "file": "service-ambulance.html",
        "title": "24/7 Ambulance Service",
        "tag": "Emergency Patient Transfer",
        "icon": "ambulance",
        "image": None,
        "meaning": "Our 24/7 Ambulance Service provides rapid emergency patient pickup and transfer directly to A1 Hospital. Equipped with oxygen support, stretcher, and emergency paramedic assistance, it ensures patients arrive safely and quickly during medical crises.",
        "highlights": [
            "24/7 Emergency Dispatch Helpline: 08942-228234",
            "Equipped with Oxygen Cylinders & Emergency Stretchers",
            "Safe Inter-Hospital & Doorstep Patient Retrieval",
            "Direct Communication with Hospital Casualty on Arrival"
        ],
        "readiness": "24/7 Rapid Response",
        "features": [
            "Continuous Oxygen & Airway Support System",
            "Foldable Hydraulic Stretchers & Wheelchairs",
            "Trained Paramedic & First-Aid Assistance",
            "Fastest Route Dispatch Across Srikakulam"
        ]
    },
    "icu": {
        "id": "icu",
        "file": "service-icu.html",
        "title": "Intensive Care Unit (ICU & NICU)",
        "tag": "Critical Patient Monitoring",
        "icon": "activity",
        "image": None,
        "meaning": "The ICU (Intensive Care Unit) and NICU (Neonatal Intensive Care Unit) are specialized hospital units for critically ill patients and newborn infants needing close, continuous monitoring. Beds have real-time vitals monitors and dedicated nurses.",
        "highlights": [
            "Continuous 24/7 Vitals & Cardiac Rhythm Monitoring",
            "Dedicated Neonatal Intensive Care (NICU) with Warmers",
            "Mechanical Ventilators & High-Flow Oxygen Support",
            "Close 1:1 and 1:2 Nurse-to-Patient Critical Care Ratio"
        ],
        "readiness": "24/7 Intensive Monitoring",
        "features": [
            "High-Precision Ventilators & Infusion Pumps",
            "Neonatal Warmers & Phototherapy Units",
            "Continuous Multi-Channel ECG & Blood Gas Tracking",
            "Strict Infection Control & Sterile Protocols"
        ]
    },
    "pharmacy": {
        "id": "pharmacy",
        "file": "service-pharmacy.html",
        "title": "Pharmacy Services",
        "tag": "In-House Medical Store",
        "icon": "pill",
        "image": "pharmacy_service.jpg",
        "meaning": "Access essential medications and prescribed treatments conveniently through our hospital pharmacy, supporting safe and continuous patient care.",
        "highlights": [
            "24/7 In-House Hospital Pharmacy Dispensary",
            "100% Genuine Prescription Medications & Disposables",
            "Cold-Chain Stored Vaccines & Critical Injectables",
            "Direct Support for Inpatient & Outpatient Needs"
        ],
        "readiness": "24/7 In-House Availability",
        "features": [
            "Direct Doctor Prescription Integration",
            "Emergency Resuscitation & Critical Care Drugs",
            "Certified Pharmacists on Duty Around the Clock",
            "Accredited Temperature-Controlled Medicine Storage"
        ]
    }
}
