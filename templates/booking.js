<script>
    function myFunction() {
      var x = document.getElementById("myLinks");
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
      }
    }
    </script>
  
    <section id="hero">
      <div class="hero-content">
        <h1>Welcome Azeya
        </h1>
        <p>Pamper yourself with our professional services</p>
        <a href="#" onclick="goToLandingPage3('Book Now')" class="btn">Book Now</a>
      </div>
    </section>
  
    <section id="services">
      <h2>Our Services</h2>
      <div class="service">
        <!-- <img src="service1.jpg" alt="Service 1"> -->
        <h3>Family shoots in studio or locations</h3>
      </div>
      <div class="service">
        <!-- <img src="service2.jpg" alt="Service 2"> -->
        <h3>Weddings</h3>
      </div>
      <div class="service">
        <!-- <img src="service3.jpg" alt="Service 3"> -->
        <h3>New born & Meternity</h3>
      </div>
    </section>
  
    <section id="about">
      <h2>About Us</h2>
      <p>Azeya is one of the most well-known photo apps and can be a profitable selling platform since some large brands buy photos from there. The commission structure is set up where the photographer gets 50% of the profits. One unique aspect is that for every photo you upload, you have to rate 5 photos from other people</p>
    </section>
  
    <section id="contact">
      <h2>Contact Us</h2>
      <p>3246 Tsipa Street Soweto, Johannesburg, South Africa</p>
      <p>Email: info@salonartofhair.com</p>
      <p>Phone: +1 101 456 7890</p>
    </section>
  
    <footer>
      <p>&copy; 2024 Salon Name. All rights reserved.</p>
    </footer>
  
    <script src="{{ url_for('static', filename='script.js') }}"></script>
  </body>
  </html>