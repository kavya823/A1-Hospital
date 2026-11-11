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

# The Real Clinical Departments Matching the Doctors (Crisp concise summaries & verified facility photography)
DEPARTMENTS_DATA = {
    "pediatrics": {
        "id": "pediatrics",
        "file": "department-pediatrics.html",
        "title": "Pediatrics & Child Health",
        "tag": "Children & Newborn Care",
        "icon": "baby",
        "image": "hospital_neonatal_warmers.jpg",
        "short_desc": "Specialized infant warmers, Level-III NICU, child surgeries, and routine vaccinations.",
        "meaning": "Specialized infant, child, and adolescent healthcare offering 24/7 Level-III NICU care, routine vaccinations, and emergency pediatric surgery.",
        "highlights": [
            "Digital Radiant Warmers & Phototherapy Units",
            "Level-III Sterile Neonatal ICU (NICU)",
            "Complete Child Immunization Schedules",
            "Specialized Pediatric Surgical Care"
        ],
        "gallery": [
            {
                "image": "hospital_neonatal_warmers.jpg",
                "title": "Infant Radiant Warmers & Incubators",
                "tag": "Neonatal Care",
                "desc": "Advanced temperature-regulated radiant warmers with vital monitors and phototherapy."
            },
            {
                "image": "hospital_nicu.jpg",
                "title": "Level-III Neonatal ICU (NICU)",
                "tag": "Critical Care",
                "desc": "Sterile high-dependency unit equipped for premature and critically ill newborns."
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
        "tag": "Women's Health & Fertility",
        "icon": "heart-pulse",
        "image": "hospital_gynecology_ot.jpg",
        "short_desc": "Painless deliveries, laparoscopy theatre, advanced IVF embryology lab, and maternity care.",
        "meaning": "Comprehensive women's healthcare providing safe deliveries, high-risk pregnancy management, advanced IVF embryology, and minimally invasive laparoscopy.",
        "highlights": [
            "Modern Labour & Painless Delivery Suite",
            "Dedicated Gynaecology & Laparoscopy OT",
            "Advanced IVF & Embryology Cleanroom Lab",
            "High-Risk Pregnancy & Antenatal Support"
        ],
        "gallery": [
            {
                "image": "hospital_gynecology_ot.jpg",
                "title": "Gynecology & Laparoscopy OT",
                "tag": "Advanced Surgery",
                "desc": "Equipped with high-definition laparoscopy towers, anesthesia stations, and LED surgical lighting."
            },
            {
                "image": "hospital_labour_room.jpg",
                "title": "Modern Labour & Delivery Suite",
                "tag": "Maternity",
                "desc": "Comfortable birthing bed with continuous fetal Doppler monitors and newborn resuscitation station."
            },
            {
                "image": "hospital_ivf_lab.jpg",
                "title": "Advanced IVF & Embryology Lab",
                "tag": "Fertility Care",
                "desc": "Sterile cleanroom with micromanipulator ICSI workstation, CO2 incubators, and stereo microscopes."
            },
            {
                "image": "hospital_ivf_theatre.jpg",
                "title": "IVF Procedure Suite",
                "tag": "Reproductive Suite",
                "desc": "Dedicated sterile procedure theatre for egg retrieval, embryo transfers, and fertility interventions."
            },
            {
                "image": "hospital_gynec_chamber.jpg",
                "title": "Executive Consultation Chamber",
                "tag": "OPD Suite",
                "desc": "Private consultation suite for senior gynaecologist Dr. Guruvelli Pramela."
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
        "tag": "Bone, Joint & Spine Care",
        "icon": "bone",
        "image": "hospital_ortho_ot.jpg",
        "short_desc": "C-Arm guided fracture surgeries, joint replacements, and sports injury rehabilitation.",
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
                "title": "Dedicated Orthopedic OT with C-Arm",
                "tag": "Surgical OT",
                "desc": "Laminar airflow operation theatre equipped with real-time fluoroscopic C-Arm imaging."
            },
            {
                "image": "hospital_single_room.jpg",
                "title": "Comfortable Post-Op Recovery",
                "tag": "Inpatient Wards",
                "desc": "Ergonomic inpatient rooms designed for rapid post-operative orthopedic recovery and mobility."
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
        "tag": "Adult Physician & Internal Care",
        "icon": "stethoscope",
        "image": "hospital_waiting_area.jpg",
        "short_desc": "Adult physician evaluations for diabetes, hypertension, acute fevers, and inpatient supervision.",
        "meaning": "Comprehensive diagnosis and continuous inpatient medical care for diabetes, hypertension, acute fevers, and multi-system illnesses.",
        "highlights": [
            "Comprehensive Outpatient & Inpatient Evaluations",
            "Diabetes, Blood Pressure & Lifestyle Disease Control",
            "24/7 Acute Seasonal Fever & Infection Supervision",
            "Preventive Health Checkups & Systemic Wellness"
        ],
        "gallery": [
            {
                "image": "hospital_waiting_area.jpg",
                "title": "Spacious Patient Reception & Waiting Lounge",
                "tag": "Hospital Amenity",
                "desc": "Air-conditioned, comfortable waiting hall with digital queue systems and amenities."
            },
            {
                "image": "hospital_single_room.jpg",
                "title": "Deluxe Inpatient Medical Care",
                "tag": "Inpatient Ward",
                "desc": "Private rooms with continuous physician supervision and bedside nursing."
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
        "tag": "Operative & Surgical Treatments",
        "icon": "scissors",
        "image": "hospital_modular_ot.jpg",
        "short_desc": "Modular laminar flow OT for laparoscopic hernia, appendix, gallbladder, and trauma surgeries.",
        "meaning": "Advanced laparoscopic and open surgical interventions for hernia, gallbladder stones, appendectomy, piles, and acute surgical emergencies.",
        "highlights": [
            "Ultra-Modern Modular OT with Laminar Air Flow",
            "Dedicated Septic & Minor Procedure Theatre",
            "Advanced Laparoscopic (Keyhole) Abdominal Surgery",
            "Rapid Post-Surgical Healing Protocols & Clean Wards"
        ],
        "gallery": [
            {
                "image": "hospital_modular_ot.jpg",
                "title": "Modular Operation Theatre",
                "tag": "Major OT",
                "desc": "Laminar airflow sterile environment with ceiling pendants and high-intensity LED surgical lights."
            },
            {
                "image": "hospital_septic_ot.jpg",
                "title": "Dedicated Septic & Minor OT",
                "tag": "Procedure Suite",
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
        "tag": "Kidney & Renal Health",
        "icon": "filter",
        "image": "hospital_nursing_station.jpg",
        "short_desc": "Specialized kidney health, chronic renal disease care, diabetic nephropathy, and fluid balance.",
        "meaning": "Specialized renal healthcare providing diagnosis and medical management for chronic kidney disease, diabetic nephropathy, and fluid electrolyte balance.",
        "highlights": [
            "Chronic Kidney Disease Management & Follow-up",
            "Diabetic Kidney Disease Prevention & Care",
            "Dialysis Guidance & Fluid Balance Optimization",
            "24/7 Monitored Inpatient Renal Protocol"
        ],
        "gallery": [
            {
                "image": "hospital_nursing_station.jpg",
                "title": "24/7 Renal Care Floor Station",
                "tag": "Nursing Station",
                "desc": "Continuous floor nursing monitoring for renal fluid balance, vitals, and medication administration."
            },
            {
                "image": "hospital_single_room.jpg",
                "title": "Monitored Inpatient Room",
                "tag": "Inpatient Care",
                "desc": "Quiet, comfortable private inpatient room with continuous clinical monitoring."
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
        "tag": "Urinary & Stone Treatments",
        "icon": "shield-plus",
        "image": "hospital_septic_ot.jpg",
        "short_desc": "Minimally invasive laser stone fragmentation, prostate care, and day-care endourology.",
        "meaning": "Advanced medical and surgical solutions for kidney stones, prostate enlargement, and urinary tract disorders using minimally invasive endoscopy.",
        "highlights": [
            "Endoscopic Kidney & Bladder Stone Fragmentation",
            "Prostate Enlargement (BPH) Diagnostic & Medical Care",
            "Recurrent Urinary Tract Infection (UTI) Treatment",
            "Dedicated Procedure Theatre for Endourology"
        ],
        "gallery": [
            {
                "image": "hospital_septic_ot.jpg",
                "title": "Endourology & Minor Procedure Theatre",
                "tag": "Procedure OT",
                "desc": "Sterile procedure suite equipped for endoscopic stone fragmentation, cystoscopy, and stenting."
            },
            {
                "image": "hospital_modular_ot.jpg",
                "title": "Advanced Surgical Modular OT",
                "tag": "Major OT",
                "desc": "Ultra-clean laminar flow operating theatre for complex reconstructive urology."
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
        "tag": "Vision & Optical Care",
        "icon": "eye",
        "image": "hospital_gynec_chamber.jpg",
        "short_desc": "Complete vision testing, cataract assessments, glaucoma checks, and eye health therapies.",
        "meaning": "Comprehensive vision testing, cataract assessments, glaucoma checks, and targeted medical therapies for clear, healthy vision.",
        "highlights": [
            "Refraction & Complete Eyesight Evaluations",
            "Cataract Diagnosis & Surgical Planning",
            "Glaucoma Pressure Screening & Dry Eye Therapy",
            "Infection, Allergy & Corneal Health Management"
        ],
        "gallery": [
            {
                "image": "hospital_gynec_chamber.jpg",
                "title": "Specialist Consultation Chamber",
                "tag": "Clinical Suite",
                "desc": "Quiet, private consultation suite equipped for thorough clinical eye examinations and vision checks."
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
        "tag": "Radiation & Clinical Oncology",
        "icon": "crosshair",
        "image": "hospital_single_room.jpg",
        "short_desc": "Early cancer screenings, evidence-based radiation planning, and compassionate support.",
        "meaning": "Compassionate cancer evaluations providing early detection screenings, clinical oncology consultations, and radiation therapy planning.",
        "highlights": [
            "Clinical Oncology Reviews & Early Cancer Screening",
            "Evidence-Based Radiation Oncology Consultations",
            "Personalized Multi-Disciplinary Tumor Care Plans",
            "Compassionate Palliative & Supportive Inpatient Care"
        ],
        "gallery": [
            {
                "image": "hospital_single_room.jpg",
                "title": "Comfort Inpatient Recovery Suite",
                "tag": "Private Suite",
                "desc": "Air-conditioned private room providing a tranquil, sterile setting for supportive oncology care."
            },
            {
                "image": "hospital_nursing_station.jpg",
                "title": "Dedicated Floor Nursing Supervision",
                "tag": "Nursing Desk",
                "desc": "24/7 nursing station delivering compassionate bedside medication and patient monitoring."
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

# The 5 Core Real Hospital Services (Updated with Verified Hospital Photography)
SERVICES_DATA = {
    "beds": {
        "id": "beds",
        "file": "service-beds.html",
        "title": "100+ Inpatient Beds",
        "tag": "Inpatient Accommodation",
        "icon": "bed-double",
        "image": "hospital_single_room.jpg",
        "short_desc": "Deluxe private suites and twin-sharing wards with dedicated nursing.",
        "meaning": "Deluxe private rooms and twin-sharing wards equipped with central oxygen and round-the-clock nursing supervision.",
        "highlights": [
            "Deluxe AC Single Rooms with Electric Motorized Beds",
            "Clean, Spacious Twin Sharing Wards with Privacy Curtains",
            "24/7 Dedicated Floor Nursing Station with Rapid Call Bells",
            "Central Medical Gas, Oxygen Lines & Emergency Power Backup"
        ],
        "gallery": [
            {
                "image": "hospital_single_room.jpg",
                "title": "Deluxe AC Single Room",
                "tag": "Private Room",
                "desc": "Air-conditioned private room with motorized bed, en-suite washroom, handwash sink, and attendant setup."
            },
            {
                "image": "hospital_sharing_room.jpg",
                "title": "Twin Sharing Inpatient Room",
                "tag": "Semi-Private",
                "desc": "Spacious room with antibacterial privacy curtains, bedside lockers, and attendant seating."
            },
            {
                "image": "hospital_nursing_station.jpg",
                "title": "24/7 Floor Nursing Station",
                "tag": "Nursing Care",
                "desc": "Round-the-clock nursing desk for immediate patient attention, monitoring, and medication delivery."
            }
        ],
        "readiness": "Inpatient Facility",
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
        "title": "24/7 Casualty & Emergency",
        "tag": "Round-the-Clock Emergency",
        "icon": "clock",
        "image": "hospital_casualty.jpg",
        "short_desc": "Rapid trauma resuscitation, casualty bays, and immediate emergency care.",
        "meaning": "Fully equipped emergency casualty and trauma bays staffed by critical care doctors for rapid crisis response.",
        "highlights": [
            "Immediate Emergency Triage & Rapid Resuscitation Bays",
            "Multi-Bed Casualty Ward with Central Oxygen & Multipara Monitors",
            "Rapid Trauma Resuscitation, Defibrillators & Emergency Crash Carts",
            "Direct Ambulance Ramp Access for Instant Wheelchair & Stretcher Triage"
        ],
        "gallery": [
            {
                "image": "hospital_casualty.jpg",
                "title": "24/7 Casualty & Trauma Ward",
                "tag": "Emergency Bays",
                "desc": "Spacious casualty with multi-parameter cardiac monitors, oxygen ports, and emergency treatment beds."
            },
            {
                "image": "service_ambulance.jpg",
                "title": "Emergency Ambulance Service",
                "tag": "Rapid Retrieval",
                "desc": "Equipped with transport oxygen, emergency stretcher, and paramedic first-aid kit."
            }
        ],
        "readiness": "Emergency Services",
        "features": [
            "Immediate Patient Triage & Assessment",
            "Trauma Care & Resuscitation Bays",
            "Advanced Multi-Parameter Vital Monitoring",
            "24/7 On-Duty Critical Care Medical Staff"
        ]
    },
    "icu": {
        "id": "icu",
        "file": "service-icu.html",
        "title": "Intensive Care (ICU & NICU)",
        "tag": "Critical Patient Monitoring",
        "icon": "activity",
        "image": "hospital_nicu.jpg",
        "short_desc": "Level-3 NICU infant warmers and advanced adult intensive monitoring.",
        "meaning": "Advanced adult intensive care bays and Level-III Neonatal Intensive Care Unit (NICU) with continuous vital monitoring.",
        "highlights": [
            "Dedicated Level-III Neonatal Intensive Care Unit (NICU)",
            "Advanced Infant Radiant Warmers & Phototherapy Units",
            "Mechanical Ventilators, Infusion Pumps & Central Oxygen",
            "1:1 and 1:2 Critical Care Nurse-to-Patient Supervision"
        ],
        "gallery": [
            {
                "image": "hospital_nicu.jpg",
                "title": "Neonatal Intensive Care Unit (NICU)",
                "tag": "NICU Suite",
                "desc": "Sterile neonatal unit with observation corridors, infusion pumps, and critical monitoring."
            },
            {
                "image": "hospital_neonatal_warmers.jpg",
                "title": "Infant Radiant Warmers & Incubators",
                "tag": "Warmers",
                "desc": "High-precision digital radiant warmers with integrated phototherapy for neonatal jaundice and temperature control."
            }
        ],
        "readiness": "Critical Care",
        "features": [
            "High-Precision Ventilators & Infusion Pumps",
            "Neonatal Warmers & Phototherapy Units",
            "Continuous Multi-Channel ECG & Blood Gas Tracking",
            "Strict Infection Control & Sterile Protocols"
        ]
    },
    "ambulance": {
        "id": "ambulance",
        "file": "service-ambulance.html",
        "title": "24/7 Ambulance Service",
        "tag": "Emergency Patient Transfer",
        "icon": "ambulance",
        "image": "service_ambulance.jpg",
        "short_desc": "Rapid doorstep patient retrieval and safe hospital transfer.",
        "meaning": "Emergency ambulance fleet equipped with transport oxygen and paramedics for rapid patient transfer.",
        "highlights": [
            "24/7 Emergency Dispatch Helpline: 08942-228234",
            "Equipped with Oxygen Cylinders & Hydraulic Stretchers",
            "Trained Paramedic & First-Aid Assistance En Route",
            "Direct Communication with Hospital Casualty on Arrival"
        ],
        "gallery": [
            {
                "image": "service_ambulance.jpg",
                "title": "24/7 Rapid Ambulance",
                "tag": "Fleet",
                "desc": "Fully equipped emergency vehicle ready for immediate roadside, doorstep, or inter-hospital transfer."
            },
            {
                "image": "hospital_casualty.jpg",
                "title": "Direct Casualty Triage Handover",
                "tag": "Casualty",
                "desc": "Direct ramp transfer from ambulance into the hospital's trauma resuscitation bay."
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
        "title": "24/7 Pharmacy Services",
        "tag": "In-House Medical Store",
        "icon": "pill",
        "image": "pharmacy.jpg",
        "short_desc": "100% genuine prescription medications, injectables, and consumables.",
        "meaning": "In-house hospital dispensary providing genuine medications, critical injectables, and surgical consumables.",
        "highlights": [
            "24/7 In-House Hospital Pharmacy Dispensary",
            "100% Genuine Prescription Medications & Disposables",
            "Cold-Chain Stored Vaccines & Critical Injectables",
            "Direct Integration with Inpatient & Emergency Desks"
        ],
        "gallery": [
            {
                "image": "pharmacy.jpg",
                "title": "24/7 In-House Hospital Pharmacy",
                "tag": "Dispensary",
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

