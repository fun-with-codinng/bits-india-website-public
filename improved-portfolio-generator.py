import json
import os
from PIL import Image

def resize_and_pad_image(image_path, output_path, size=(800, 600)):
    """
    Resize and pad images with improved dimensions and 4:3 aspect ratio
    Common aspect ratios for e-commerce:
    - 4:3 (1.33:1) - Traditional product imagery
    - 1:1 - Square format for consistent grid layout
    - 16:9 (1.77:1) - Landscape mode for hero images
    We're using 4:3 as it's ideal for product showcase while maintaining detail
    """
    # [Previous image processing code remains unchanged]
    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            aspect = img.width / img.height
            target_aspect = 4/3
            
            if aspect > target_aspect:
                new_width = size[0]
                new_height = int(size[0] / target_aspect)
            else:
                new_height = size[1]
                new_width = int(size[1] * target_aspect)
            
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            new_img = Image.new('RGB', size, (248, 249, 250))
            
            x = (size[0] - new_width) // 2
            y = (size[1] - new_height) // 2
            
            new_img.paste(img, (x, y))
            new_img.save(output_path, quality=95, optimize=True)
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def resize_and_maintain_ratio(image_path, output_path, max_size=(800, 600)):
    """
    Resize image maintaining original ratio and place on white background
    """
    # [Previous ratio maintenance code remains unchanged]
    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            ratio = min(max_size[0]/img.width, max_size[1]/img.height)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            background = Image.new('RGB', max_size, (255, 255, 255))
            
            x = (max_size[0] - new_size[0]) // 2
            y = (max_size[1] - new_size[1]) // 2
            
            background.paste(img, (x, y))
            background.save(output_path, quality=95, optimize=True)
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
        padding: 60px 0;
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

    .custom-portfolio-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .custom-portfolio-grid {
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        
        .custom-portfolio-link img {
            height: 200px;
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

    <title>BITS India - Business & IT Solutions</title>
    <meta content="" name="BITS India - Business & IT Solutions">
    <meta name="description" content="BITS India - Business & IT Solutions">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    
    <!-- Favicons -->
    <link href="assets/images/favicon.png" rel="icon">
    <link href="assets/images/apple-touch-icon.png" rel="apple-touch-icon">
    
    <!-- Google Fonts -->
    <link
        href="../../../css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="../../../css2-1?family=Oswald:wght@500&amp;display=swap" rel="stylesheet">
    <link href="../../../css2-2?family=Poppins:wght@300;400&amp;display=swap" rel="stylesheet">
    <!-- Vendor CSS Files -->
    <!-- <link href="assets/vendor/aos/aos.css" rel="stylesheet"> -->
    <link href="assets/stylesheets/font-awesome.min.css" rel="stylesheet">
    <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
    <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    <!-- Main CSS File -->
    <link href="assets/stylesheets/styles.css" rel="stylesheet">

    <style>
'''
    
    # Add improved CSS
    html_content += generate_portfolio_css()
    html_content += '''
    </style>
</head>
<body>
    <!-- ======= Header ======= -->
    <header id="header" class="header d-flex align-items-center sticked">
        <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
            <a href="index.html" class="logo d-flex align-items-center">
                <img src="assets/images/Logo-new.png" alt="logo">
            </a>
            <nav id="navbar" class="navbar">
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="portfolio.html" class="active">Portfolio</a></li>
                    <li><a href="testimonials.html">Testimonials</a></li>
                    <li class="dropdown">
                        <a href="#"><span>Menu</span> <i class="bi bi-chevron-down"></i></a>
                        <ul>
                            <li><a href="about.html">About</a></li>
                            <li><a href="packages.html">Pricing</a></li>
                            <li><a href="faqs.html">FAQs</a></li>
                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                            <li><a href="blogs.html">Blogs</a></li>
                        </ul>
                    </li>
                    <li><a href="blogs.html">News</a></li>
                </ul>
            </nav>
            <a href="contact.html" class="btn-get-started">Get Quotes</a>
        </div>
    </header>

    <!-- ======= Breadcrumbs ======= -->
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
'''

    # Generate portfolio items with improved structure
    html_content += '''
    <section id="portfolio" class="custom-portfolio-section">
        <div class="custom-container" data-aos="fade-up">
            <div class="custom-portfolio-grid">
    '''

    # Generate portfolio items with links to dedicated pages
    for project in projects:
        category_class = project['project_category'].lower().replace(' ', '-')
        
        # Process images
        image_folder = os.path.join("portfolio", project['image_folder'])
        resized_folder = os.path.join(image_folder, "resized")
        os.makedirs(resized_folder, exist_ok=True)

        # Handle images
        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        if images:
            main_image = images[0]
            original_path = os.path.join(image_folder, main_image)
            resized_path = os.path.join(resized_folder, main_image)
            resize_and_maintain_ratio(original_path, resized_path)
            
            # Generate portfolio item HTML with link to dedicated page
            html_content += f'''
                <div class="custom-portfolio-card {category_class}" data-aos="fade-up" data-aos-delay="100">
                    <a href="portfolio/{project['file_name']}" class="custom-portfolio-link">
                        <img src="{resized_path}" class="img-fluid" alt="{project['project_name']}">
                        <div class="custom-portfolio-details">
                            <h3>{project['project_name']}</h3>
                            <p>{project['project_category']}</p>
                        </div>
                    </a>
                </div>
            '''

    # Close portfolio container and add remaining HTML structure
    html_content += '''
            </div>
        </div>
    </section>
    '''

    # Add footer and scripts
    html_content += '''

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

    </body>
    </html>
    '''

    # Write the final HTML to file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Usage remains the same
if __name__ == "__main__":
    json_file = 'portfolio/projects.json'
    output_file = 'portfolio.html'
    generate_html(json_file, output_file)