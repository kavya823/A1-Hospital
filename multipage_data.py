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
        "desc": "Founder of A1 Hospital with over 13+ years of clinical excellence in pediatric care, child health, and newborn wellness in Srikakulam.",
        "image": "dr_rao.jpeg",
        "icon": "baby"
    },
    {
        "id": "dr-g-prameela",
        "name": "Dr. G. Prameela",
        "qual": "M.S. (OBG) FART, FMAS",
        "title": "Senior Obstetrician & Gynaecologist (IVF Specialist)",
        "dept": "Obstetrics, Gynaecology & IVF Clinic",
        "desc": "Senior Consultant Obstetrician & Gynaecologist. Specialist in high-risk pregnancy, infertility evaluation, advanced reproductive technology (FART), and minimal access laparoscopic surgery (FMAS).",
        "image": "dr_prameela.png",
        "icon": "heart-pulse"
    },
    {
        "id": "dr-kannepalli-srinivas",
        "name": "Dr. Kannepalli Srinivas",
        "qual": "M.S., M.CH. PAEDIATRIC SURGERY",
        "title": "Pediatric Surgeon",
        "dept": "Pediatrics & Child Health",
        "desc": "Specialist in pediatric surgical interventions, neonatal surgeries, and congenital anomaly corrections in children.",
        "image": None,
        "icon": "baby"
    },
    {
        "id": "dr-sattaru-kishore-babu",
        "name": "Dr. Sattaru. Kishore Babu",
        "qual": "M.S., (ORTHO)",
        "title": "Orthopaedic Surgeon",
        "dept": "Orthopedics & Joint Surgery",
        "desc": "Senior orthopedic surgeon specializing in bone fracture management, joint replacement, and complex musculoskeletal trauma.",
        "image": None,
        "icon": "bone"
    },
    {
        "id": "dr-bammidi-sai-theja",
        "name": "Dr. Bammidi Sai Theja",
        "qual": "MS Ortho, FIJR, FIASM",
        "title": "Orthopaedic Surgeon",
        "dept": "Orthopedics & Joint Surgery",
        "desc": "Fellow in Joint Replacement and Arthroscopic Sports Surgery, treating joint arthritis, knee, hip, and ligament injuries.",
        "image": None,
        "icon": "activity"
    },
    {
        "id": "dr-hanumanthu-anilkumar",
        "name": "Dr. Hanumanthu Anilkumar",
        "qual": "M.D (General Medicine)",
        "title": "General Physician",
        "dept": "General Medicine",
        "desc": "Consultant physician managing adult fevers, diabetes, hypertension, respiratory infections, and general medical illnesses.",
        "image": None,
        "icon": "stethoscope"
    },
    {
        "id": "dr-chittipotula-balaji",
        "name": "Dr. Chittipotula Balaji",
        "qual": "M.B.B.S., MS (GENERAL SURGERY)",
        "title": "General Surgeon",
        "dept": "General Surgery",
        "desc": "Expert general surgeon performing hernia repairs, appendectomy, piles/fissure procedures, trauma wound care, and abdominal surgeries.",
        "image": None,
        "icon": "scissors"
    },
    {
        "id": "dr-korla-vidya-sagar",
        "name": "Dr. Korla Vidya Sagar",
        "qual": "M.D., DM, NEPHROLOGY",
        "title": "Nephrologist",
        "dept": "Nephrology (Kidney Care)",
        "desc": "Kidney specialist managing chronic kidney disease (CKD), acute renal failure, dialysis care, and diabetic nephropathy.",
        "image": None,
        "icon": "filter"
    },
    {
        "id": "dr-budumuru-ramana",
        "name": "Dr. Budumuru Ramana",
        "qual": "M.S., MCH",
        "title": "Urologist",
        "dept": "Urology",
        "desc": "Specialist in urinary tract disorders, kidney stones, prostate conditions, and minimally invasive endourological procedures.",
        "image": None,
        "icon": "shield-plus"
    },
    {
        "id": "dr-palepu-srikanthi",
        "name": "Dr. Palepu Srikanthi",
        "qual": "M.S., OPHTHALMOLOGY",
        "title": "Ophthalmologist",
        "dept": "Ophthalmology (Eye Care)",
        "desc": "Eye specialist providing comprehensive vision evaluations, cataract assessments, glaucoma checks, and medical eye treatments.",
        "image": None,
        "icon": "eye"
    },
    {
        "id": "dr-navya-madabatula",
        "name": "Dr. Navya Madabatula",
        "qual": "M.B.B.S, M.D., M.D.",
        "title": "Senior Consultant Radiation & Clinical Oncologist",
        "dept": "Oncology (Cancer Care)",
        "desc": "Consultant oncologist guiding cancer evaluations, clinical oncology reviews, early cancer screenings, and radiation planning.",
        "image": None,
        "icon": "crosshair"
    }
]

# The 8 Real Clinical Departments Matching the Doctors
DEPARTMENTS_DATA = {
    "pediatrics": {
        "id": "pediatrics",
        "file": "department-pediatrics.html",
        "title": "Pediatrics & Child Health",
        "tag": "Children & Newborn Care",
        "icon": "baby",
        "image": None,
        "meaning": "Pediatrics is the branch of medicine focused on the physical, emotional, and social health of infants, children, and young adolescents. It covers preventive vaccinations, childhood fever management, growth assessments, and specialized pediatric surgery.",
        "highlights": [
            "13+ Years Pediatric Excellence led by Founder Dr. Mula Venkatarao",
            "Specialized Pediatric Surgical Care by Dr. Kannepalli Srinivas",
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
        "image": "dr_prameela.png",
        "meaning": "Obstetrics & Gynaecology covers comprehensive women's health, safe pregnancy care, and childbirth. The advanced reproductive technology (FART) and minimal access surgery (FMAS) unit delivers dedicated infertility treatments, IVF guidance, and laparoscopic surgeries.",
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
        "image": None,
        "meaning": "Orthopedics focuses on diagnosing, treating, and operating on disorders of the bones, joints, ligaments, tendons, and muscles. This includes fixing accidental fractures, treating chronic joint pain, and performing joint replacement surgeries.",
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
        "image": None,
        "meaning": "General Medicine deals with the prevention, diagnosis, and non-surgical treatment of adult diseases. It covers chronic health conditions like diabetes, high blood pressure, respiratory infections, seasonal viral fevers, and multi-system medical illnesses.",
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
        "image": None,
        "meaning": "General Surgery involves surgical procedures to treat abdominal organs, hernias, gallbladder stones, appendicitis, piles, fissures, cysts, and accidental wounds. It focuses on safe operative intervention and smooth patient recovery.",
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
        "image": None,
        "meaning": "Nephrology is the medical specialty that deals with kidney diseases, kidney damage prevention, fluid imbalances, and dialysis care. It focuses on keeping kidneys functioning and managing conditions caused by diabetes or high blood pressure.",
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
        "image": None,
        "meaning": "Urology focuses on the medical and surgical management of the urinary tract (kidneys, ureters, bladder, and urethra) in men and women, as well as male reproductive health. Common treatments include kidney stone management and prostate care.",
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
        "image": None,
        "meaning": "Ophthalmology is the branch of medicine and surgery that treats disorders of the eye and vision. It includes comprehensive eyesight testing, cataract evaluation, glaucoma screening, and medical treatment for ocular infections and allergies.",
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
        "image": None,
        "meaning": "Oncology is the medical specialty devoted to diagnosing, staging, and treating cancer. Radiation and clinical oncology focuses on targeted cancer treatment planning, early cancer detection screenings, and supportive compassionate patient guidance.",
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

# The 5 Core Real Services
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
            "Continuous Patient Monitoring & Nursing Care",
            "Hygienic En-Suite Facilities & Attendant Couches"
        ],
        "lead_doctor": {
            "name": "Dr. Mula Venkatarao & Dr. Hanumanthu Anilkumar",
            "qual": "Founder & Consultant Physician",
            "title": "Inpatient Medical Care Supervision",
            "image": None
        }
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
            "Immediate Doctor Triage & Resuscitation Equipment",
            "Direct Support for Road Traffic Accidents & Trauma",
            "Direct Access to Oxygen, Defibrillators & Medication"
        ],
        "lead_doctor": {
            "name": "Dr. Hanumanthu Anilkumar & Emergency Medical Team",
            "qual": "M.D (General Medicine)",
            "title": "Emergency Casualty & Critical Response",
            "image": None
        }
    },
    "pharmacy": {
        "id": "pharmacy",
        "file": "service-pharmacy.html",
        "title": "24/7 In-House Pharmacy",
        "tag": "Authentic Medications",
        "icon": "pill",
        "image": None,
        "meaning": "An in-house pharmacy is an on-premises hospital medical store open 24 hours. Patients and families do not need to search outside for medicines; genuine, doctor-prescribed tablets, injections, and child syrups are available instantly inside the hospital.",
        "highlights": [
            "Open 24/7 Right Inside the Hospital Premises",
            "100% Genuine, Batch-Verified Brand & Generic Medicines",
            "Refrigerated Cold-Storage for Vaccines & Insulin",
            "Stock of Emergency Injections & Surgical Disposables"
        ],
        "lead_doctor": {
            "name": "A1 Hospital Pharmacy Team",
            "qual": "Registered Clinical Pharmacists",
            "title": "24/7 In-House Medicine Dispensation",
            "image": None
        }
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
        "lead_doctor": {
            "name": "Emergency Ambulance Dispatch Team",
            "qual": "Trained Emergency Medical Technicians (EMT)",
            "title": "24/7 Emergency Transport Service",
            "image": None
        }
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
            "Dedicated Neonatal Care (NICU) under Dr. Mula Venkatarao",
            "Mechanical Ventilators & High-Flow Oxygen Support",
            "Close Nurse-to-Patient Care Ratio"
        ],
        "lead_doctor": {
            "name": "Dr. Mula Venkatarao & Dr. Hanumanthu Anilkumar",
            "qual": "M.D (PAED) NILOUFER & M.D (General Medicine)",
            "title": "Intensive Care & Neonatal Supervision",
            "image": None
        }
    }
}
