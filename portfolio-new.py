import json
import os
from PIL import Image

def optimize_image(image_path, output_path, max_dimension=1200):
    """
    Optimize image while maintaining aspect ratio
    Only resize if image is too large, focus on quality optimization
    """
    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate new size while maintaining aspect ratio
            ratio = min(max_dimension/max(img.width, img.height), 1.0)
            if ratio < 1.0:  # Only resize if image is too large
                new_size = (int(img.width * ratio), int(img.height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save with optimization
            img.save(output_path, 'WEBP', quality=85, optimize=True)
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def generate_portfolio_css():
    return """
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* Portfolio section specific styles */
    .custom-portfolio-section {
        padding: 30px 0;
        background: #f8f9fa;
    }

    .custom-portfolio-section .custom-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 15px;
    }

    .custom-portfolio-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 25px;
        padding: 20px 0;
    }

    .custom-portfolio-card {
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        background: #fff;
        transition: all 0.3s ease;
        cursor: pointer;
        display: block;
    }

    .custom-portfolio-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }

    .custom-portfolio-link {
        position: relative;
        display: block;
        text-decoration: none;
        color: inherit;
        background: #fff;
    }

    .custom-portfolio-link img {
        width: 100%;
        height: 250px;
        object-fit: contain;
        background: #fff;
        transition: transform 0.3s ease;
        display: block;
    }

    .custom-portfolio-card:hover .custom-portfolio-link img {
        transform: scale(1.05);
    }

    .custom-portfolio-details {
        padding: 20px;
        background: #fff;
    }

    .custom-portfolio-details h3 {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
        margin: 0 0 8px 0;
        letter-spacing: -0.02em;
    }

    .custom-portfolio-details p {
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        color: #666;
        margin: 0;
        font-weight: 400;
    }

    .custom-portfolio-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #0ea2bd, #2196F3);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.3s ease;
    }

    .custom-portfolio-link .image-container {
        position: relative;
        width: 100%;
        padding-top: 75%; /* 4:3 aspect ratio container */
        overflow: hidden;
    }
    
    .custom-portfolio-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }

    .custom-portfolio-link img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover; /* This will cover the area while maintaining aspect ratio */
        object-position: center;
        transition: transform 0.3s ease, opacity 0.3s ease;
    }

    /* Portfolio filters styles */
    .portfolio-filters-container {
        background: rgba(2, 90, 221, 0.03);
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 40px;
    }

    .portfolio-flters {
        padding: 0;
        margin: 0;
        list-style: none;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .portfolio-flters li {
        margin: 0;
    }

    .portfolio-flters li a {
        display: inline-flex;
        align-items: center;
        padding: 8px 18px;
        font-size: 14px;
        font-weight: 500;
        line-height: 1;
        color: #025add;
        text-decoration: none;
        transition: all 0.2s ease;
        border-radius: 8px;
        background: transparent;
        border: 1px solid #025add;
    }

    .portfolio-flters li a:hover {
        background: rgba(2, 90, 221, 0.1);
    }

    .portfolio-flters li a.filter-active {
        background: #025add;
        color: white;
    }

    @media (max-width: 768px) {
        .portfolio-filters-container {
            padding: 15px;
            border-radius: 12px;
            margin: 0 15px 30px 15px;
        }

        .portfolio-flters {
            gap: 8px;
        }
        
        .portfolio-flters li a {
            padding: 6px 14px;
            font-size: 13px;
        }
    }
    """

def generate_html(json_file, output_file):
    # Load project data
    with open(json_file, 'r') as file:
        projects = json.load(file)

    # Start HTML content
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>BITS India - Business & IT Solution</title>
    <meta content="" name="BITS India - Business & IT Solution">
    <meta name="description" content="BITS India - Business & IT Solution">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    
    <!-- Favicons -->
    <link href="assets/images/favicon.png" rel="icon">
    <link href="assets/images/apple-touch-icon.png" rel="apple-touch-icon">
    
    <!-- Google Fonts -->
    <link href="../../../css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="../../../css2-1?family=Oswald:wght@500&amp;display=swap" rel="stylesheet">
    <link href="../../../css2-2?family=Poppins:wght@300;400&amp;display=swap" rel="stylesheet">
    
    <!-- Vendor CSS Files -->
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    <link href="assets/stylesheets/font-awesome.min.css" rel="stylesheet">
    <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
    <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
    
    <!-- Main CSS -->
    <link href="assets/stylesheets/styles.css" rel="stylesheet">

    <style>
'''
    
    # Add CSS
    html_content += generate_portfolio_css()
    html_content += '''
    </style>
</head>
<body>
    <!-- Header -->
  <header id="header" class="header d-flex align-items-center sticked stikcy-menu">
    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center">
        <img src="assets/images/Logo-new.png" alt="logo">
      </a>
      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="index.html" class="">Home</a></li>
          <li><a href="services.html" class="">Services</a></li>
          <li><a href="portfolio.html" class="">Portfolio</a></li>
          <li><a href="testimonials.html" class="">Testimonials</a></li>
          <!-- <li><a href="team.html" class="">Team</a></li> -->
          <li class="dropdown"><a href="#"><span>Menu</span> <i class="bi bi-chevron-down dropdown-indicator"></i></a>
            <ul>
              <li><a href="about.html">About</a></li>
              <li><a href="packages.html">Pricing</a></li>
              <li><a href="faqs.html">FAQs</a></li>
              <!-- <li><a href="privacy-policy.html">Terms &amp; Conditions</a></li> -->
              <li><a href="privacy-policy.html">Privacy Policy</a></li>
              <li><a href="blogs.html">Blogs</a></li>
              <!-- <li><a href="blog-details.html">Blog Detail Page</a></li> -->
            </ul>
          </li>
          <li><a href="blogs.html">News</a></li>
        </ul>
      </nav><!-- .navbar -->
      <a href="contact.html" class="btn-get-started hide-on-mobile">Get Quotes</a>
      <button id="darkmode-button"><i class="bi bi-moon-fill"></i></button>
      <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
      <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>
    </div>
  </header>

    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="page-header d-flex align-items-center">
            <div class="container position-relative">
                <div class="row d-flex justify-content-center">
                    <div class="col-lg-6 text-center">
                        <h2>Our Portfolio</h2>
                        <p>Discover our innovative solutions across various domains</p>
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <div class="container">
                <ol>
                    <li><a href="index.html">Home</a></li>
                    <li>Portfolio</li>
                </ol>
            </div>
        </nav>
    </div>

    <!-- Portfolio Section -->
    <section id="portfolio" class="custom-portfolio-section">
        <div class="custom-container" data-aos="fade-up">
            <div style="margin-bottom: 20px;">
                <ul class="portfolio-flters">
                    <li><a href="portfolio.html?filter=all" class="filter-active">All</a></li>
                    <li><a href="portfolio.html?filter=application-design">Application Design</a></li>
                    <li><a href="portfolio.html?filter=web-designing">Web Designing</a></li>
                    <li><a href="portfolio.html?filter=surveillance-solutions">Surveillance Solutions</a></li>
                    <li><a href="portfolio.html?filter=ai-solutions">AI Solutions</a></li>
                    <li><a href="portfolio.html?filter=cybersecurity-solutions">Cybersecurity Solutions</a></li>
                    <li><a href="portfolio.html?filter=iot-and-smart-systems">IoT and Smart Systems</a></li>
                </ul>
            </div>
            <div class="custom-portfolio-grid">
'''

    # Generate portfolio items
    for project in projects:
        category_class = project['project_category'].lower().replace(' ', '-')
        
        # Process images
        image_folder = os.path.join("portfolio", project['image_folder'])
        resized_folder = os.path.join(image_folder, "resized")
        os.makedirs(resized_folder, exist_ok=True)

        # Handle images

        # In the generate_html function, update the image processing section:
        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        main_image = 'cover.webp' if 'cover.webp' in images else images[0]
        original_path = os.path.join(image_folder, main_image)
        resized_path = os.path.join(resized_folder, f"optimized_{main_image}")
        optimize_image(original_path, resized_path)
        
        # In the generate_html function, update the portfolio item HTML generation:
        html_content += f'''
            <div class="custom-portfolio-card {category_class}" data-aos="fade-up" data-aos-delay="100">
                <a href="portfolio/{project['file_name']}" class="custom-portfolio-link">
                    <div class="image-container">
                        <img src="{resized_path}" class="img-fluid" alt="{project['project_name']}">
                    </div>
                    <div class="custom-portfolio-details">
                        <h3>{project['project_name']}</h3>
                        <p>{project['project_category']}</p>
                    </div>
                </a>
            </div>
        '''

    # Close portfolio section
    html_content += '''
            </div>
        </div>
    </section>

    <!-- Footer -->

      <footer id="footer" class="footer-section">
        <div class="container">
        <div class="footer-content pt-5 pb-5">
            <div class="row">
            <div class="col-xl-4 col-lg-4 mb-50">
                <div class="footer-widget">
                <div class="footer-logo">
                    <a href="index.html" class="logo d-flex align-items-center">
                    <img src="assets/images/Logo-new-2.png" alt="logo">
                    </a>
                </div>
                <div class="footer-text">
                    <p>Lorem ipsum dolor sit amet, consec tetur adipisicing elit, sed do eiusmod tempor incididuntut consec
                    tetur adipisicing
                    elit,Lorem ipsum dolor sit amet.</p>
                </div>
                <div class="footer-social-icon">
                    <span>Follow us</span>
                    <a href="#" class="twitter"><i class="bi bi-twitter"></i></a>
                    <a href="#" class="facebook"><i class="bi bi-facebook"></i></a>
                    <a href="#" class="instagram"><i class="bi bi-instagram"></i></a>
                    <a href="#" class="linkedin"><i class="bi bi-linkedin"></i></a>
                </div>
                </div>
            </div>

            <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                <div class="service-widget footer-widget">
                <div class="footer-widget-heading">
                    <h3>Services</h3>
                </div>
                <ul class="list">
                    <li><a href="services.html">Web Design</a></li>
                    <li><a href="services.html">App Developemnt</a></li>
                    <li><a href="services.html">Cloud Services</a></li>
                    <li><a href="services.html">Domain adn Hosting</a></li>
                    <li><a href="services.html">Seo Optimization</a></li>
                    <li><a href="services.html">Social Media</a></li>
                </ul>
                </div>
            </div>
            <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                <div class="service-widget footer-widget">
                <div class="footer-widget-heading">
                    <h3>Information</h3>
                </div>
                <ul class="list">
                    <li><a href="about.html">About</a></li>
                    <!-- <li><a href="packages.html">Pricing</a></li> -->
                    <!-- <li><a href="team.html">Team</a></li> -->
                    <li><a href="porfolio.html">Portfolio</a></li>
                    <li><a href="faq.html">FAQs</a></li>
                    <!-- <li><a href="team.html">Team</a></li> -->
                    <li><a href="blogs.html">Blogs</a></li>
                    <!-- <li><a href="blogs-details.html">Blog Details</a></li> -->
                    <!-- <li><a href="coming-soon.html">Coming Soon</a></li> -->
                    <li><a href="privacy-policy.html">Terms & Conditions</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                </ul>
                </div>
            </div>
            <div class="col-xl-4 col-lg-4 col-md-6 mb-50">
                <div class="contact-widget footer-widget">
                <div class="footer-widget-heading">
                    <h3>Contacts</h3>
                </div>
                <div class="footer-text">
                    <p><i class="bi bi-geo-alt-fill mr-15"></i> 101 West Town , PBO 12345, United States</p>
                    <p><i class="bi bi-telephone-inbound-fill mr-15"></i> +1 1234 56 789</p>
                    <p><i class="bi bi-envelope-fill mr-15"></i> contact@example.com</p>
                </div>
                </div>
                <div class="footer-widget">
                <div class="footer-widget-heading">
                    <h3>Newsletter</h3>
                </div>
                <div class="footer-text mb-25">
                    <p>Don't miss to subscribe to our new feeds, kindly fill the form below.</p>
                </div>
                <div class="subscribe-form">
                    <form action="#">
                    <input type="text" placeholder="Email Address">
                    <button><i class="bi bi-telegram"></i></button>
                    </form>
                </div>
                </div>
            </div>
            </div>
            <div class="row">
            <div class="col-xl-6 col-lg-6 text-left text-lg-left">
                <div class="copyright-text">
                <p>BITS India © 2025 - Business & IT Solutions
                </p>
                </div>
            </div>
            </div>
        </div>
        </div>
    </footer>

    <!-- Filter script -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Get all filter buttons and portfolio items
        const filterButtons = document.querySelectorAll('.portfolio-flters li a');
        const portfolioItems = document.querySelectorAll('.custom-portfolio-card');
        
        // Function to handle filter click
        function handleFilterClick(e) {
            e.preventDefault();
            
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('filter-active'));
            
            // Add active class to clicked button
            e.target.classList.add('filter-active');
            
            // Get filter value from href
            const filterValue = e.target.getAttribute('href').split('=')[1];
            
            // Show/hide items based on filter
            portfolioItems.forEach(item => {
                if (filterValue === 'all') {
                    item.style.display = 'block';
                } else {
                    if (item.classList.contains(filterValue)) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
            
            // Update URL without page refresh
            const newUrl = new URL(window.location);
            newUrl.searchParams.set('filter', filterValue);
            window.history.pushState({}, '', newUrl);
        }
        
        // Add click event listeners to filter buttons
        filterButtons.forEach(button => {
            button.addEventListener('click', handleFilterClick);
        });
        
        // Handle initial load with URL parameters
        const urlParams = new URLSearchParams(window.location.search);
        const initialFilter = urlParams.get('filter') || 'all';
        const activeFilterButton = document.querySelector(`[href="portfolio.html?filter=${initialFilter}"]`);
        if (activeFilterButton) {
            activeFilterButton.click();
        }
    });
    </script>

    </body>
    </html>'''

    # Write the final HTML to file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Usage remains the same
if __name__ == "__main__":
    json_file = 'portfolio/projects.json'
    output_file = 'portfolio.html'
    generate_html(json_file, output_file)