// This script reads from data.js and places it into HTML
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("brandname").textContent = brand.brandname;

   // Top Section
    document.getElementById("title").textContent = topSection.title;
    document.getElementById("subtitle").textContent = topSection.subtitle;

    // Home Page Video Description
    document.getElementById("videodescription").textContent = home.videodescription;

    // Footer
    document.getElementById("footeraddress").textContent = footer.address;
    document.getElementById("footerphone").textContent = footer.phone;
    document.getElementById("footeremail").textContent = footer.email;

    // Contact Us Page
    document.getElementById("contact-description").textContent = contact.contactdescription;
    document.getElementById("contact-address").textContent = contact.contactAddress;
    document.getElementById("contact-phone").textContent = contact.contactPhone;
    document.getElementById("contact-email").textContent = contact.contactEmail;

    // Team Page
    document.getElementById("name1").textContent = team.name1;
    document.getElementById("role1").textContent = team.role1;
    document.getElementById("college1").textContent = team.college1;
    document.getElementById("mail1").textContent = team.mail1;
    document.getElementById("desc1").textContent = team.desc1;

    document.getElementById("name2").textContent = team.name2;
    document.getElementById("role2").textContent = team.role2;
    document.getElementById("college2").textContent = team.college2;
    document.getElementById("mail2").textContent = team.mail2;
    document.getElementById("desc2").textContent = team.desc2;

    document.getElementById("name3").textContent = team.name3;
    document.getElementById("role3").textContent = team.role3;
    document.getElementById("college3").textContent = team.college3;
    document.getElementById("mail3").textContent = team.mail3;
    document.getElementById("desc3").textContent = team.desc3;

});
