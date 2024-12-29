import json
import os
from PIL import Image

def resize_and_pad_image(image_path, output_path, size=(816, 582), padding=10):
    """
    Resize and pad an image while maintaining aspect ratio
    """
    try:
        with Image.open(image_path) as img:
            # Convert image to RGB mode if it's not
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate aspect ratios
            target_ratio = (size[0] - 2*padding) / (size[1] - 2*padding)
            img_ratio = img.width / img.height
            
            if img_ratio > target_ratio:
                # Width is the limiting factor
                new_width = size[0] - 2*padding
                new_height = int(new_width / img_ratio)
            else:
                # Height is the limiting factor
                new_height = size[1] - 2*padding
                new_width = int(new_height * img_ratio)
            
            # Resize image
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Create white background
            canvas = Image.new('RGB', size, (255, 255, 255))
            
            # Calculate paste position
            x = (size[0] - new_width) // 2
            y = (size[1] - new_height) // 2
            
            # Paste resized image onto canvas
            canvas.paste(img, (x, y))
            canvas.save(output_path, 'JPEG', quality=95)
            return True
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False

def get_relative_path(path, base_path):
    """
    Convert absolute path to relative path based on the HTML file location
    """
    return os.path.relpath(path, os.path.dirname(base_path))

def generate_portfolio_pages(json_file):
    """
    Generate portfolio pages from JSON data
    """
    try:
        # Load and validate JSON data
        with open(json_file, 'r', encoding='utf-8') as file:
            projects = json.load(file)
        
        if not isinstance(projects, list):
            raise ValueError("JSON file must contain a list of projects")

        # Group projects by category
        category_projects = {}
        for project in projects:
            if not all(key in project for key in ['project_category', 'project_name', 'file_name', 'image_folder', 'description', 'pointers']):
                raise ValueError(f"Missing required fields in project: {project.get('project_name', 'Unknown')}")
            category_projects.setdefault(project['project_category'], []).append(project)

        # Process each project
        for project in projects:
            file_name = project['file_name']
            image_folder = project['image_folder']
            
            # Ensure image folder exists
            if not os.path.exists(image_folder):
                print(f"Warning: Image folder not found: {image_folder}")
                continue

            # Create resized images folder
            resized_folder = os.path.join(image_folder, "resized")
            os.makedirs(resized_folder, exist_ok=True)

            # Process images
            images = [img for img in os.listdir(image_folder) 
                     if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
            
            if not images:
                print(f"Warning: No images found in {image_folder}")
                continue

            # Resize images
            resized_images = []
            for img in images:
                original_path = os.path.join(image_folder, img)
                resized_path = os.path.join(resized_folder, f"resized_{img}")
                if resize_and_pad_image(original_path, resized_path):
                    resized_images.append(get_relative_path(resized_path, file_name))

            main_image = resized_images[0] if resized_images else ""
            small_images = resized_images[:4]

            # Generate related projects HTML
            related_projects = [p for p in category_projects[project['project_category']] 
                              if p != project][:3]
            
            related_html = ""
            for rel in related_projects:
                rel_image_folder = os.path.join(rel['image_folder'], "resized")
                rel_images = [f for f in os.listdir(rel_image_folder) 
                            if f.startswith("resized_")] if os.path.exists(rel_image_folder) else []
                
                if rel_images:
                    rel_image_path = get_relative_path(
                        os.path.join(rel_image_folder, rel_images[0]), 
                        file_name
                    )
                    
                    related_html += f"""
                    <div class='col-sm-12 col-md-4 project-card'>
                        <a href='{rel['file_name']}' class="project-link">
                            <div class="project-image">
                                <img loading="lazy" src='{rel_image_path}' 
                                     alt='{rel['project_name']}'>
                            </div>
                            <div class="project-info">
                                <h4>{rel['project_name']}</h4>
                                <span class="category">{rel['project_category']}</span>
                            </div>
                        </a>
                    </div>
                    """

            # Generate image gallery HTML
            small_images_html = ""
            for i, img in enumerate(small_images):
                small_images_html += f"""
                <div class='col-3 small-img-col'>
                    <img loading="lazy" src='{img}' class='small-img w-100' 
                         alt='Project image {i+1}' onclick="changeImage(this)">
                </div>
                """

            # Generate HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{project['project_name']}</title>
                <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
                <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
                <link href="../assets/css/styles.css" rel="stylesheet">
                
                <style>
                    .project-details {{
                        padding: 2rem;
                        background: #f8f9fa;
                        border-radius: 8px;
                        margin-top: 2rem;
                    }}
                    
                    .small-img-col {{
                        transition: transform 0.3s ease;
                        cursor: pointer;
                    }}
                    
                    .small-img-col:hover {{
                        transform: scale(1.05);
                    }}
                    
                    .project-card {{
                        transition: transform 0.3s ease;
                        margin-bottom: 2rem;
                        box-shadow: 0 2px 15px rgba(0,0,0,0.1);
                        border-radius: 8px;
                        overflow: hidden;
                    }}
                    
                    .project-card:hover {{
                        transform: translateY(-5px);
                    }}
                    
                    .project-image img {{
                        width: 100%;
                        height: 200px;
                        object-fit: cover;
                    }}
                    
                    .project-info {{
                        padding: 1rem;
                    }}
                    
                    #ProductImg {{
                        transition: opacity 0.3s ease;
                        max-height: 500px;
                        object-fit: contain;
                    }}
                    
                    .back-button {{
                        position: fixed;
                        bottom: 2rem;
                        right: 2rem;
                        background: #007bff;
                        color: white;
                        width: 50px;
                        height: 50px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        border-radius: 50%;
                        box-shadow: 0 2px 15px rgba(0,0,0,0.2);
                        z-index: 1000;
                        transition: transform 0.3s ease;
                    }}
                    
                    .back-button:hover {{
                        transform: scale(1.1);
                    }}
                </style>
              </head>
              <body>
                <div class="container mt-5">
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><a href="../index.html">Home</a></li>
                            <li class="breadcrumb-item"><a href="../portfolio.html">Portfolio</a></li>
                            <li class="breadcrumb-item active">{project['project_name']}</li>
                        </ol>
                    </nav>

                    <div class="row">
                        <div class="col-md-6">
                            <div class="main-image-container">
                                <img src="{main_image}" class="w-100" id="ProductImg" alt="{project['project_name']}">
                            </div>
                            <div class="row mt-3">
                                {small_images_html}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="project-details">
                                <h1>{project['project_name']}</h1>
                                <p class="lead">{project['description']}</p>
                                
                                <div class="mt-4">
                                    <h3>Project Features</h3>
                                    <ul class="list-unstyled">
                                        {"".join(f'<li class="mb-2"><i class="bi bi-check-circle-fill text-success me-2"></i>{pointer}</li>' for pointer in project['pointers'])}
                                    </ul>
                                </div>
                                
                                <a href="../contact.html" class="btn btn-primary btn-lg mt-4">Get a Quote</a>
                            </div>
                        </div>
                    </div>

                    <div class="related-projects mt-5">
                        <h2 class="mb-4">Related Projects</h2>
                        <div class="row">
                            {related_html}
                        </div>
                    </div>
                </div>

                <a href="../portfolio.html" class="back-button">
                    <i class="bi bi-arrow-left"></i>
                </a>

                <script>
                    function changeImage(element) {{
                        const mainImg = document.getElementById('ProductImg');
                        mainImg.style.opacity = '0';
                        
                        setTimeout(() => {{
                            mainImg.src = element.src;
                            mainImg.style.opacity = '1';
                        }}, 300);
                    }}

                    // Lazy loading
                    if ('IntersectionObserver' in window) {{
                        const lazyImages = document.querySelectorAll('img[loading="lazy"]');
                        const imageObserver = new IntersectionObserver((entries, observer) => {{
                            entries.forEach(entry => {{
                                if (entry.isIntersecting) {{
                                    const img = entry.target;
                                    img.src = img.src;
                                    img.removeAttribute('loading');
                                    observer.unobserve(img);
                                }}
                            }});
                        }});

                        lazyImages.forEach(img => imageObserver.observe(img));
                    }}
                </script>
              </body>
            </html>
            """

            # Create output directory if it doesn't exist
            # os.makedirs(os.path.dirname(file_name), exist_ok=True)

            # Write the HTML file
            with open(file_name, 'w', encoding='utf-8') as page_file:
                page_file.write(html_content)
            
            print(f"Successfully generated: {file_name}")

    except Exception as e:
        print(f"Error generating portfolio pages: {e}")
        raise

if __name__ == "__main__":
    json_file = 'projects.json'
    generate_portfolio_pages(json_file)