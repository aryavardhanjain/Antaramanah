const slider = document.querySelector('.gallery');
const sliderItems = document.querySelectorAll('.image-container');
const autoScrollInterval = 2000; // Adjust the interval as needed (in milliseconds)
let currentIndex = 0;

function scrollNext() {
  const nextIndex = (currentIndex + 1) % sliderItems.length;
  slider.scrollTo({
    left: nextIndex * sliderItems[0].offsetWidth,
    behavior: 'smooth',
  });
  currentIndex = nextIndex;
}

setInterval(scrollNext, autoScrollInterval);


  // Function to continuously flip the cards
  function autoFlipCards() {
    // Get the flip card elements by their IDs
    const meghaProfile = document.getElementById("megha-profile");
    const aryavardhanProfile = document.getElementById("aryavardhan-profile");

    // Toggle the transform property for Megha's profile
    const meghaCardInner = meghaProfile.querySelector('.flip-card-inner');
    meghaCardInner.style.transform = meghaCardInner.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';
    
    // Toggle the transform property for Aryavardhan's profile
    const aryavardhanCardInner = aryavardhanProfile.querySelector('.flip-card-inner-1');
    aryavardhanCardInner.style.transform = aryavardhanCardInner.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';
  }

  // Set an interval to trigger the flip every 5 seconds (5000 milliseconds)
  setInterval(autoFlipCards, 1500);

  document.addEventListener("DOMContentLoaded", function() {
    const faqQuestions = document.querySelectorAll(".faq-question");

    faqQuestions.forEach(function(question) {
        question.addEventListener("click", function(){
            this.classList.toggle("active");
            const answer = this.nextElementSibling;
            
            if (this.classList.contains("active")){
                answer.style.maxHeight = answer.scrollHeight + "px";
                answer.style.opacity = 1;
            }
            else{
                answer.style.maxHeight = "0";
                answer.style.opacity = 0;
            }
        });
    });
});