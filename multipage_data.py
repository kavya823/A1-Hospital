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
        "qual": "M.D. (Paed), Niloufer",
        "title": "Children Specialist (Founder & Managing Partner)",
        "dept": "Pediatrics & Child Health",
        "exp": "15+ Years of Experience",
        "desc": "Hospital Founder & Managing Partner with 15+ years of clinical excellence in newborn care, childhood illnesses, and pediatric wellness.",
        "image": "dr_rao.jpeg",
        "icon": "baby"
    },
    {
        "id": "dr-guruvelli-pramela",
        "name": "Dr. Guruvelli Pramela",
        "qual": "M.S. (OBG), FART, FMAS",
        "title": "Senior Obstetrician & Gynaecologist (Co-Founder & Managing Partner)",
        "dept": "Obstetrics, Gynaecology & IVF Clinic",
        "exp": "13+ Years of Experience",
        "desc": "Co-Founder & Managing Partner with 13+ years of clinical excellence specializing in high-risk pregnancy, infertility evaluation, advanced reproductive technology (IVF/FART), and laparoscopy.",
        "image": "dr_prameela.png",
        "icon": "heart-pulse"
    },
    {
        "id": "dr-kannepalli-srinivas",
        "name": "Dr. Kannepalli Srinivas",
        "qual": "M.S., M.Ch. (Paediatric Surgery)",
        "title": "Pediatric Surgeon",
        "dept": "Pediatrics & Child Health",
        "exp": "Pediatric Surgical Specialist",
        "desc": "Specialist in pediatric surgical care, neonatal interventions, and congenital anomaly corrections.",
        "image": None,
        "icon": "baby"
    },
    {
        "id": "dr-naveen-goddu",
        "name": "Dr. Naveen Goddu",
        "qual": "M.D. (Pediatrics)",
        "title": "Pediatrician",
        "dept": "Pediatrics & Child Health",
        "exp": "Pediatric Specialist",
        "desc": "Consultant pediatrician providing comprehensive newborn and child healthcare, fever management, immunizations, and adolescent wellness.",
        "image": None,
        "icon": "baby"
    },
    {
        "id": "dr-sattaru-kishore-babu",
        "name": "Dr. Sattaru Kishore Babu",
        "qual": "M.S. (Ortho)",
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
        "qual": "M.S. (Ortho), FIJR, FIASM",
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
        "qual": "M.D. (General Medicine)",
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
        "qual": "M.B.B.S., M.S. (General Surgery)",
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
        "qual": "M.D., D.M. (Nephrology)",
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
        "qual": "M.S., M.Ch. (Urology)",
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
        "qual": "M.S. (Ophthalmology)",
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
        "qual": "M.B.B.S., M.D., M.D.",
        "title": "Senior Consultant Radiation Oncologist & Clinical Oncologist",
        "dept": "Oncology (Cancer Care)",
        "exp": "Clinical & Radiation Oncologist",
        "desc": "Consultant oncologist guiding cancer evaluations, early screenings, and radiation therapy planning.",
        "image": None,
        "icon": "crosshair"
    }
]

# The Real Clinical Departments Matching the Doctors (Exact Photo Names & Verified Facility Photography)
DEPARTMENTS_DATA = {
    "pediatrics": {
        "id": "pediatrics",
        "file": "department-pediatrics.html",
        "title": "Pediatrics & Child Health",
        "tag": "NICU",
        "icon": "baby",
        "image": "hospital_nicu.jpg",
        "short_desc": "Sterile Level-III NICU, digital radiant warmers, child surgeries, and routine vaccinations.",
        "meaning": "Specialized infant, child, and adolescent healthcare offering 24/7 Level-III NICU care, routine vaccinations, and emergency pediatric surgery.",
        "highlights": [
            "Sterile Level-III Neonatal ICU (NICU)",
            "Digital Radiant Warmers & Phototherapy Units",
            "Complete Child Immunization Schedules",
            "Specialized Pediatric Surgical Care"
        ],
        "gallery": [
            {
                "image": "hospital_nicu.jpg",
                "title": "NICU",
                "tag": "NICU",
                "desc": "Sterile high-dependency unit equipped for premature and critically ill newborns."
            },
            {
                "image": "hospital_neonatal_warmers.jpg",
                "title": "Neonatal Radiant Warmers",
                "tag": "Warmers",
                "desc": "Advanced temperature-regulated radiant warmers with vital monitors and phototherapy."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Mula Venkatarao",
                "qual": "M.D. (Paed), Niloufer",
                "title": "Children Specialist (Founder & Managing Partner)",
                "image": "dr_rao.jpeg"
            },
            {
                "name": "Dr. Kannepalli Srinivas",
                "qual": "M.S., M.Ch. (Paediatric Surgery)",
                "title": "Pediatric Surgeon",
                "image": None
            },
            {
                "name": "Dr. Naveen Goddu",
                "qual": "M.D. (Pediatrics)",
                "title": "Pediatrician",
                "image": None
            }
        ]
    },
    "obstetrics": {
        "id": "obstetrics",
        "file": "department-obstetrics.html",
        "title": "Obstetrics, Gynaecology & IVF Clinic",
        "tag": "Gynecology OT",
        "icon": "heart-pulse",
        "image": "hospital_gynecology_ot.jpg",
        "short_desc": "Gynecology OT, Labour Room, IVF Theatre & Area, and Gynecologist Consultation Chamber.",
        "meaning": "Comprehensive women's healthcare providing safe deliveries, high-risk pregnancy management, advanced IVF embryology, and minimally invasive laparoscopy.",
        "highlights": [
            "Dedicated Gynecology OT for Laparoscopic Surgery",
            "Modern Labour Room for Painless Deliveries",
            "Dedicated IVF Theatre for Embryo Transfers",
            "Sterile IVF Area & Cleanroom Embryology Lab"
        ],
        "gallery": [
            {
                "image": "hospital_gynecology_ot.jpg",
                "title": "Gynecology OT",
                "tag": "Gynecology OT",
                "desc": "Equipped with high-definition laparoscopy towers, anesthesia stations, and LED surgical lighting."
            },
            {
                "image": "hospital_labour_room.jpg",
                "title": "Labour Room",
                "tag": "Labour Room",
                "desc": "Comfortable birthing bed with continuous fetal Doppler monitors and newborn resuscitation station."
            },
            {
                "image": "hospital_ivf_theatre.jpg",
                "title": "IVF Theatre",
                "tag": "IVF Theatre",
                "desc": "Dedicated sterile procedure theatre for egg retrieval, embryo transfers, and fertility interventions."
            },
            {
                "image": "hospital_ivf_lab.jpg",
                "title": "IVF Area",
                "tag": "IVF Area",
                "desc": "Sterile cleanroom with micromanipulator ICSI workstation, CO2 incubators, and stereo microscopes."
            },
            {
                "image": "hospital_gynec_chamber.jpg",
                "title": "Gynecologist Chamber",
                "tag": "Gynecologist Chamber",
                "desc": "Executive consultation chamber for senior gynaecologist Dr. Guruvelli Pramela."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Guruvelli Pramela",
                "qual": "M.S. (OBG), FART, FMAS",
                "title": "Senior Obstetrician & Gynaecologist (Co-Founder & Managing Partner)",
                "image": "dr_prameela.png"
            }
        ]
    },
    "orthopedics": {
        "id": "orthopedics",
        "file": "department-orthopedics.html",
        "title": "Orthopedics & Joint Surgery",
        "tag": "Orthopedic OT",
        "icon": "bone",
        "image": "hospital_ortho_ot.jpg",
        "short_desc": "Dedicated Orthopedic OT with Allengers C-Arm for fracture fixation and joint surgery.",
        "meaning": "Expert orthopedic surgical care for complex fractures, joint replacements, arthroscopic sports injuries, and spine rehabilitation.",
        "highlights": [
            "Orthopedic OT with Allengers High-Resolution C-Arm",
            "24/7 Fracture Fixation & Accident Trauma Surgery",
            "Precision Total Knee & Hip Replacement Procedures",
            "Minimally Invasive Arthroscopic Ligament Repair"
        ],
        "gallery": [
            {
                "image": "hospital_ortho_ot.jpg",
                "title": "Orthopedic OT",
                "tag": "Orthopedic OT",
                "desc": "Laminar airflow operation theatre equipped with real-time fluoroscopic C-Arm imaging."
            },
            {
                "image": "dept_orthopedics.jpg",
                "title": "Orthopedic & Joint Care Suite",
                "tag": "Joint Care",
                "desc": "Specialized clinic for arthritis evaluation, fracture trauma management, and post-op care."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Sattaru Kishore Babu",
                "qual": "M.S. (Ortho)",
                "title": "Orthopaedic Surgeon",
                "image": None
            },
            {
                "name": "Dr. Bammidi Sai Theja",
                "qual": "M.S. (Ortho), FIJR, FIASM",
                "title": "Orthopaedic Surgeon",
                "image": None
            }
        ]
    },
    "generalmedicine": {
        "id": "generalmedicine",
        "file": "department-generalmedicine.html",
        "title": "General Medicine",
        "tag": "Physician Care",
        "icon": "stethoscope",
        "image": "dept_generalmedicine.jpg",
        "short_desc": "Adult physician evaluations for fevers, BP, diabetes, infection management, and internal care.",
        "meaning": "Comprehensive diagnosis and continuous inpatient medical care for diabetes, hypertension, acute fevers, and multi-system illnesses.",
        "highlights": [
            "Comprehensive Outpatient Physician Consultations",
            "Diabetes, Blood Pressure & Chronic Illness Control",
            "24/7 Acute Seasonal Fever & Infection Supervision",
            "Continuous Inpatient Medical Care & Supervision"
        ],
        "gallery": [
            {
                "image": "dept_generalmedicine.jpg",
                "title": "Physician Consultation Suite",
                "tag": "Physician Care",
                "desc": "Comprehensive clinical evaluations and personalized care for adult fevers, diabetes, and hypertension."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Hanumanthu Anilkumar",
                "qual": "M.D. (General Medicine)",
                "title": "General Physician",
                "image": None
            }
        ]
    },
    "generalsurgery": {
        "id": "generalsurgery",
        "file": "department-generalsurgery.html",
        "title": "General & Laparoscopic Surgery",
        "tag": "Modular Theatre",
        "icon": "scissors",
        "image": "hospital_modular_ot.jpg",
        "short_desc": "Modular Theatre and Septic OT for laparoscopic hernia, appendix, and acute surgeries.",
        "meaning": "Advanced laparoscopic and open surgical interventions for hernia, gallbladder stones, appendectomy, piles, and acute surgical emergencies.",
        "highlights": [
            "Ultra-Modern Modular Theatre with Laminar Air Flow",
            "Dedicated Septic OT for Clean & Contaminated Cases",
            "Advanced Laparoscopic (Keyhole) Abdominal Surgery",
            "Rapid Post-Surgical Healing Protocols & Clean Wards"
        ],
        "gallery": [
            {
                "image": "hospital_modular_ot.jpg",
                "title": "Modular Theatre",
                "tag": "Modular Theatre",
                "desc": "Laminar airflow sterile environment with ceiling pendants and high-intensity LED surgical lights."
            },
            {
                "image": "hospital_septic_ot.jpg",
                "title": "Septic OT",
                "tag": "Septic OT",
                "desc": "Independent operation theatre dedicated to minor procedures, abscess management, and emergency cleanups."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Chittipotula Balaji",
                "qual": "M.B.B.S., M.S. (General Surgery)",
                "title": "General Surgeon",
                "image": None
            }
        ]
    },
    "nephrology": {
        "id": "nephrology",
        "file": "department-nephrology.html",
        "title": "Nephrology (Kidney Care)",
        "tag": "Kidney Care",
        "icon": "filter",
        "image": "dept_nephrology.jpg",
        "short_desc": "Specialized kidney health, chronic renal disease care, dialysis guidance, and fluid management.",
        "meaning": "Specialized renal healthcare providing diagnosis and medical management for chronic kidney disease, diabetic nephropathy, and fluid electrolyte balance.",
        "highlights": [
            "Chronic Kidney Disease Management & Follow-up",
            "Diabetic Kidney Disease Prevention & Care",
            "Dialysis Guidance & Fluid Balance Optimization",
            "Continuous Physician & Clinical Supervision"
        ],
        "gallery": [
            {
                "image": "dept_nephrology.jpg",
                "title": "Nephrology & Renal Care Suite",
                "tag": "Kidney Care",
                "desc": "Specialized clinical consultations for kidney function, electrolyte monitoring, and dialysis guidance."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Korla Vidya Sagar",
                "qual": "M.D., D.M. (Nephrology)",
                "title": "Nephrologist",
                "image": None
            }
        ]
    },
    "urology": {
        "id": "urology",
        "file": "department-urology.html",
        "title": "Urology & Stone Care",
        "tag": "Urology Care",
        "icon": "shield-plus",
        "image": "dept_urology.jpg",
        "short_desc": "Laser kidney stone fragmentation, prostate wellness, and advanced endourology care.",
        "meaning": "Advanced medical and surgical solutions for kidney stones, prostate enlargement, and urinary tract disorders using minimally invasive endoscopy.",
        "highlights": [
            "Endoscopic Kidney & Bladder Stone Fragmentation",
            "Prostate Enlargement (BPH) Diagnostic & Medical Care",
            "Recurrent Urinary Tract Infection (UTI) Treatment",
            "Dedicated Septic OT for Endourology Procedures"
        ],
        "gallery": [
            {
                "image": "dept_urology.jpg",
                "title": "Urology & Stone Care Suite",
                "tag": "Urology Care",
                "desc": "Specialized evaluation and treatment for kidney stones, prostate issues, and urinary conditions."
            },
            {
                "image": "hospital_septic_ot.jpg",
                "title": "Septic OT / Endourology Suite",
                "tag": "Endourology",
                "desc": "Sterile procedure suite equipped for endoscopic stone fragmentation, cystoscopy, and stenting."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Budumuru Ramana",
                "qual": "M.S., M.Ch. (Urology)",
                "title": "Urologist",
                "image": None
            }
        ]
    },
    "ophthalmology": {
        "id": "ophthalmology",
        "file": "department-ophthalmology.html",
        "title": "Ophthalmology (Eye Care)",
        "tag": "Eye Care",
        "icon": "eye",
        "image": "dept_ophthalmology.jpg",
        "short_desc": "Refraction testing, cataract assessments, glaucoma checks, and comprehensive eye health.",
        "meaning": "Comprehensive vision testing, cataract assessments, glaucoma checks, and targeted medical therapies for clear, healthy vision.",
        "highlights": [
            "Refraction & Complete Eyesight Evaluations",
            "Cataract Diagnosis & Surgical Planning",
            "Glaucoma Pressure Screening & Dry Eye Therapy",
            "Infection, Allergy & Corneal Health Management"
        ],
        "gallery": [
            {
                "image": "dept_ophthalmology.jpg",
                "title": "Ophthalmology & Eye Care Suite",
                "tag": "Eye Care",
                "desc": "Dedicated consultation suite equipped for thorough clinical eye examinations and vision checks."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Palepu Srikanthi",
                "qual": "M.S. (Ophthalmology)",
                "title": "Ophthalmologist",
                "image": None
            }
        ]
    },
    "oncology": {
        "id": "oncology",
        "file": "department-oncology.html",
        "title": "Oncology (Cancer Care)",
        "tag": "Cancer Care",
        "icon": "crosshair",
        "image": "dept_oncology.jpg",
        "short_desc": "Early cancer screenings, clinical reviews, and evidence-based radiation therapy planning.",
        "meaning": "Compassionate cancer evaluations providing early detection screenings, clinical oncology consultations, and radiation therapy planning.",
        "highlights": [
            "Clinical Oncology Reviews & Early Cancer Screening",
            "Evidence-Based Radiation Oncology Consultations",
            "Personalized Multi-Disciplinary Tumor Care Plans",
            "Compassionate Inpatient Recovery & Guidance"
        ],
        "gallery": [
            {
                "image": "dept_oncology.jpg",
                "title": "Clinical Oncology Suite",
                "tag": "Cancer Care",
                "desc": "Quiet, compassionate consultation suite for cancer evaluations, tumor boards, and treatment planning."
            }
        ],
        "doctors": [
            {
                "name": "Dr. Navya Madabatula",
                "qual": "M.B.B.S., M.D., M.D.",
                "title": "Senior Consultant Radiation Oncologist & Clinical Oncologist",
                "image": None
            }
        ]
    }
}

# The Core Real Hospital Services (Exact Photo Names & Verified Hospital Photography)
SERVICES_DATA = {
    "waitinghall": {
        "id": "waitinghall",
        "file": "service-waiting-hall.html",
        "title": "Waiting Hall",
        "tag": "Waiting Hall",
        "icon": "users",
        "image": "hospital_waiting_area.jpg",
        "short_desc": "Spacious, air-conditioned patient and visitor waiting hall with comfortable seating.",
        "meaning": "Spacious, fully air-conditioned patient and visitor waiting hall equipped with comfortable seating, digital status screens, and patient assistance desks.",
        "highlights": [
            "Spacious Air-Conditioned Patient Waiting Hall",
            "Ergonomic Seating for Patients & Attendants",
            "Digital Information & Queue Assistance Desks",
            "Immediate Access to Consultation Chambers & Pharmacy"
        ],
        "gallery": [
            {
                "image": "hospital_waiting_area.jpg",
                "title": "Waiting Hall",
                "tag": "Waiting Hall",
                "desc": "Spacious air-conditioned waiting hall with comfortable seating and assistance desks."
            },
            {
                "image": "reception_desk.jpg",
                "title": "Reception & Helpdesk",
                "tag": "Reception",
                "desc": "24/7 hospital reception desk for patient registrations and guidance."
            }
        ],
        "readiness": "Hospital Facility",
        "features": [
            "Fully Air-Conditioned Waiting Hall",
            "Comfortable Patient Seating",
            "Digital Queue Displays",
            "24/7 Patient Help Desk"
        ]
    },
    "beds": {
        "id": "beds",
        "file": "service-beds.html",
        "title": "100+ Beds (Sharing & Single Rooms)",
        "tag": "100+ Beds Facility",
        "icon": "bed-double",
        "image": "hospital_casualty.jpg",
        "short_desc": "100+ Beds facility featuring spacious Sharing Rooms and deluxe Single Rooms with 24/7 nursing.",
        "meaning": "Over 100+ inpatient beds across spacious sharing wards and private single rooms equipped with central oxygen and round-the-clock nursing supervision.",
        "highlights": [
            "100+ Inpatient Bed Capacity Across Spacious Wards",
            "Multi-Bed Sharing Rooms with Privacy Curtains",
            "Deluxe AC Single Rooms with Motorized Beds",
            "24/7 Floor Nursing Station with Emergency Call Systems"
        ],
        "gallery": [
            {
                "image": "hospital_casualty.jpg",
                "title": "100+ Beds Sharing Ward",
                "tag": "100+ Beds Facility",
                "desc": "Spacious multi-bed inpatient sharing ward with antibacterial curtains and bedside oxygen ports."
            },
            {
                "image": "hospital_sharing_room.jpg",
                "title": "Sharing Room",
                "tag": "Sharing Room",
                "desc": "Spacious room with antibacterial privacy curtains, bedside lockers, and attendant seating."
            },
            {
                "image": "hospital_single_room.jpg",
                "title": "Single Room",
                "tag": "Single Room",
                "desc": "Air-conditioned private room with motorized bed, en-suite washroom, and attendant setup."
            },
            {
                "image": "hospital_nursing_station.jpg",
                "title": "Nursing Station",
                "tag": "Nursing Station",
                "desc": "Round-the-clock nursing desk for immediate patient attention, monitoring, and medication delivery."
            }
        ],
        "readiness": "Inpatient Facility",
        "features": [
            "100+ Inpatient Beds Facility",
            "Spacious Sharing Rooms with Curtains",
            "Deluxe AC Single Rooms",
            "24/7 Dedicated Nursing Station"
        ]
    },
    "emergency": {
        "id": "emergency",
        "file": "service-emergency.html",
        "title": "24/7 Emergency & Casualty",
        "tag": "24/7 Emergency",
        "icon": "clock",
        "image": "reception_desk.jpg",
        "short_desc": "24/7 Emergency and Casualty triage desk with rapid response doctors and critical care.",
        "meaning": "24/7 emergency response, immediate patient triage, and critical casualty admissions supported by on-duty medical officers.",
        "highlights": [
            "24/7 Emergency Casualty Triage & Reception Desk",
            "Immediate On-Duty Emergency Medical Officers",
            "Direct Ambulance Ramp & Stretcher Access",
            "Rapid Multi-Parameter Vital Stabilization"
        ],
        "gallery": [
            {
                "image": "reception_desk.jpg",
                "title": "24/7 Emergency Triage Desk",
                "tag": "Emergency Desk",
                "desc": "Round-the-clock emergency admission and immediate casualty triage desk."
            },
            {
                "image": "service_ambulance.jpg",
                "title": "24/7 Emergency Ambulance",
                "tag": "Ambulance",
                "desc": "Equipped with transport oxygen, emergency stretcher, and paramedic first-aid kit."
            },
            {
                "image": "hospital_building.jpg",
                "title": "Emergency Access & Building",
                "tag": "Hospital Access",
                "desc": "Direct ramp entrance for immediate emergency retrieval and patient drop-off."
            }
        ],
        "readiness": "Emergency Services",
        "features": [
            "24/7 Emergency Triage Desk",
            "Immediate Patient Assessment",
            "Direct Ambulance Ramp Access",
            "On-Duty Critical Care Medical Staff"
        ]
    },
    "icu": {
        "id": "icu",
        "file": "service-icu.html",
        "title": "NICU (Neonatal ICU)",
        "tag": "NICU",
        "icon": "activity",
        "image": "hospital_nicu.jpg",
        "short_desc": "Sterile Level-III NICU with digital radiant warmers, incubators, and intensive monitoring.",
        "meaning": "Sterile Level-III Neonatal Intensive Care Unit (NICU) with digital radiant warmers, mechanical ventilators, and continuous vital monitoring.",
        "highlights": [
            "Dedicated Sterile Level-III Neonatal ICU (NICU)",
            "Advanced Infant Radiant Warmers & Phototherapy Units",
            "Mechanical Ventilators, Infusion Pumps & Central Oxygen",
            "1:1 and 1:2 Critical Care Nurse-to-Patient Supervision"
        ],
        "gallery": [
            {
                "image": "hospital_nicu.jpg",
                "title": "NICU",
                "tag": "NICU",
                "desc": "Sterile neonatal unit with observation corridors, infusion pumps, and critical monitoring."
            },
            {
                "image": "hospital_neonatal_warmers.jpg",
                "title": "Neonatal Radiant Warmers",
                "tag": "Warmers",
                "desc": "High-precision digital radiant warmers with integrated phototherapy for neonatal care."
            }
        ],
        "readiness": "Critical Care",
        "features": [
            "Level-III Sterile NICU Environment",
            "Neonatal Radiant Warmers & Incubators",
            "Continuous Multi-Channel Vital Tracking",
            "Strict Infection Control & Sterile Protocols"
        ]
    },
    "ambulance": {
        "id": "ambulance",
        "file": "service-ambulance.html",
        "title": "24/7 Ambulance Service",
        "tag": "Ambulance",
        "icon": "ambulance",
        "image": "service_ambulance.jpg",
        "short_desc": "24/7 emergency ambulance with transport oxygen, stretcher, and direct Casualty handover.",
        "meaning": "Emergency ambulance fleet equipped with transport oxygen and paramedics for rapid patient transfer and direct Casualty handover.",
        "highlights": [
            "24/7 Emergency Dispatch Helpline: 08942-228234",
            "Equipped with Oxygen Cylinders & Hydraulic Stretchers",
            "Trained Paramedic & First-Aid Assistance En Route",
            "Direct Ramp Handover to Casualty Trauma Bay"
        ],
        "gallery": [
            {
                "image": "service_ambulance.jpg",
                "title": "24/7 Ambulance",
                "tag": "Ambulance",
                "desc": "Fully equipped emergency vehicle ready for immediate roadside, doorstep, or inter-hospital transfer."
            },
            {
                "image": "reception_desk.jpg",
                "title": "Emergency Reception & Triage",
                "tag": "Emergency Triage",
                "desc": "Immediate patient intake and emergency triage desk upon ambulance arrival."
            }
        ],
        "readiness": "Ambulance Dispatch",
        "features": [
            "Continuous Oxygen & Airway Support System",
            "Foldable Hydraulic Stretchers & Wheelchairs",
            "Trained Paramedic & First-Aid Assistance",
            "Fastest Route Dispatch Across Srikakulam"
        ]
    },
    "pharmacy": {
        "id": "pharmacy",
        "file": "service-pharmacy.html",
        "title": "Pharmacy (24/7)",
        "tag": "Pharmacy",
        "icon": "pill",
        "image": "pharmacy.jpg",
        "short_desc": "24/7 in-house Pharmacy with 100% genuine prescription medications, injectables, and surgicals.",
        "meaning": "In-house hospital Pharmacy providing genuine medications, critical injectables, vaccines, and surgical consumables.",
        "highlights": [
            "24/7 In-House Hospital Pharmacy Dispensary",
            "100% Genuine Prescription Medications & Disposables",
            "Cold-Chain Stored Vaccines & Critical Injectables",
            "Direct Integration with Inpatient & Casualty Desks"
        ],
        "gallery": [
            {
                "image": "pharmacy.jpg",
                "title": "Pharmacy",
                "tag": "Pharmacy",
                "desc": "Full stock of authentic medications, antibiotics, cardiac drugs, and pediatric formulations."
            }
        ],
        "readiness": "In-House Pharmacy",
        "features": [
            "Direct Doctor Prescription Integration",
            "Emergency Resuscitation & Critical Care Drugs",
            "Certified Pharmacists on Duty Around the Clock",
            "Accredited Temperature-Controlled Medicine Storage"
        ]
    }
}