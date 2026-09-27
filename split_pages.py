import re
import os

def process():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    def set_title(html_str, title):
        return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_str)

    nav_match = re.search(r'(<!DOCTYPE html>.*?(?=<header id="home"))', html, re.DOTALL)
    contact_footer_match = re.search(r'(<section id="contact".*?</html>)', html, re.DOTALL)

    services_match = re.search(r'(<section id="services".*?</section>\s*)\n\s*<section id="departments"', html, re.DOTALL)
    departments_match = re.search(r'(<section id="departments".*?</section>\s*)\n\s*<section id="lab"', html, re.DOTALL)
    doctors_match = re.search(r'(<section id="doctors".*?</section>\s*)\n\s*<section id="contact"', html, re.DOTALL)

    spacer = '\n    <div style="margin-top: 140px;"></div>\n'

    if nav_match and contact_footer_match and services_match:
        services_html = nav_match.group(1) + spacer + services_match.group(1) + contact_footer_match.group(1)
        services_html = set_title(services_html, 'Services | A1 Hospital')
        
        # Hide home view and show all view
        services_html = services_html.replace('id="home-services-view"', 'id="home-services-view" style="display: none;"')
        services_html = services_html.replace('id="all-services-view" style="display: none;"', 'id="all-services-view"')
        
        # Remove the "View All Services" button container
        services_html = re.sub(r'<div[^>]*id="view-all-srv-btn-container"[^>]*>.*?</div>', '', services_html, flags=re.DOTALL)
        
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(services_html)
        print("Successfully created services.html")
    else:
        print(f"Failed to create services.html. Matches - Nav: {bool(nav_match)}, Footer: {bool(contact_footer_match)}, Services: {bool(services_match)}")

    if nav_match and contact_footer_match and departments_match:
        dept_html = nav_match.group(1) + spacer + departments_match.group(1) + contact_footer_match.group(1)
        dept_html = set_title(dept_html, 'Departments | A1 Hospital')
        
        # Hide home view and show all view
        dept_html = dept_html.replace('id="home-dept-view"', 'id="home-dept-view" style="display: none;"')
        dept_html = dept_html.replace('id="all-dept-view" style="display: none;"', 'id="all-dept-view"')
        
        # Remove the "View All Departments" button container
        dept_html = re.sub(r'<div[^>]*id="view-all-dept-btn-container"[^>]*>.*?</div>', '', dept_html, flags=re.DOTALL)
        
        with open('departments.html', 'w', encoding='utf-8') as f:
            f.write(dept_html)
        print("Successfully created departments.html")
    else:
        print(f"Failed to create departments.html. Matches - Nav: {bool(nav_match)}, Footer: {bool(contact_footer_match)}, Departments: {bool(departments_match)}")

    if nav_match and contact_footer_match and doctors_match:
        doc_html = nav_match.group(1) + spacer + doctors_match.group(1) + contact_footer_match.group(1)
        doc_html = set_title(doc_html, 'Doctors | A1 Hospital')
        # Remove the "View All Doctors" button
        doc_html = re.sub(r'<div[^>]*>\s*<a href="doctors\.html"[^>]*>View All Doctors</a>\s*</div>', '', doc_html)
        with open('doctors.html', 'w', encoding='utf-8') as f:
            f.write(doc_html)
        print("Successfully created doctors.html")
    else:
        print(f"Failed to create doctors.html. Matches - Nav: {bool(nav_match)}, Footer: {bool(contact_footer_match)}, Doctors: {bool(doctors_match)}")

if __name__ == '__main__':
    process()
