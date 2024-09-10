// Navbar

  //For user profile in nav


console.log("Hello Ishak")

// document.addEventListener("DOMContentLoaded", function() {
//     gsap.from(".animate-navbar-js",{
//         delay:0.2,
//         opacity:0,
//         duration:0.5,
//         y:-60,
        
    
//     });
//     gsap.from('#right h1',{
//         delay:0.2,
//         opacity:0,
//         duration:0.5,
//         x:60,
        
    
//     });
    
//     gsap.from("#left",{
//         delay:0.2,
//         opacity:0,
//         duration:0.5,
//         x:-60,
    
//     });
    // gsap.from("#center",{
    //     delay:0.2,
    //     opacity:0,
    //     duration:0.5,
    //     y:60,
    
    // })
    
// });
//For user profile in nav


function toggleMenu() {
    const menuLinks = document.getElementById("menu-links");
    menuLinks.classList.toggle("active");
}







// About 

document.addEventListener('DOMContentLoaded', function () {
    const containers = document.querySelectorAll('.responsive-container-block.Container');
    let activeIndex = 0;
  
    const setActiveContainer = (index) => {
      containers.forEach((container, i) => {
        if (i === index) {
          container.classList.add('active');
        } else {
          container.classList.remove('active');
        }
      });
    };
  
    const onScroll = () => {
      const scrollPosition = window.scrollY + window.innerHeight / 2;
      containers.forEach((container, index) => {
        const containerTop = container.offsetTop;
        const containerBottom = containerTop + container.offsetHeight;
        if (scrollPosition >= containerTop && scrollPosition < containerBottom) {
          activeIndex = index;
          setActiveContainer(activeIndex);
        }
      });
    };
  
    window.addEventListener('scroll', onScroll);
    setActiveContainer(activeIndex);
  });
  
  

// contact


const inputs = document.querySelectorAll(".input");

      function focusFunc() {
        let parent = this.parentNode;
        parent.classList.add("focus");
      }

      function blurFunc() {
        let parent = this.parentNode;
        if (this.value == "") {
          parent.classList.remove("focus");
        }
      }

      inputs.forEach((input) => {
        input.addEventListener("focus", focusFunc);
        input.addEventListener("blur", blurFunc);
      });

// Register page

