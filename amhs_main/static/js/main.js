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

const doughnutData = {
  labels: ['Help seekers', 'People affected by mental disorders'],
  datasets: [{
    data: [30, 150],
    backgroundColor: ['#e10de1', '#FFCE56'],
  }]
};

const doughnutCanvas = document.getElementById('doughnutChart').getContext('2d');

new Chart(doughnutCanvas, {
    type: 'doughnut',
    data: doughnutData,
});

const doughnutData1 = {
  labels: ['World Population', 'People affected by depressive disorders'],
  datasets: [{
    data: [7840952880, 322480000],
    backgroundColor: ['#FFCE56', '#e10de1'],
  }]
};

const doughnutCanvas1 = document.getElementById('doughnutChart1').getContext('2d');

new Chart(doughnutCanvas1, {
    type: 'doughnut',
    data: doughnutData1,
});

const doughnutData2 = {
  labels: ['Population of India', 'People affected by mental disorders'],
  datasets: [{
    data: [1354195680, 189587395],
    backgroundColor: ['#FFCE56', '#e10de1'],
  }]
};

const doughnutCanvas2 = document.getElementById('doughnutChart2').getContext('2d');

new Chart(doughnutCanvas2, {
    type: 'doughnut',
    data: doughnutData2,
});

const doughnutData3 = {
  labels: ['Population of age 15-24 in India', 'Mental Health Advocates'],
  datasets: [{
    data: [248550000, 101905500],
    backgroundColor: ['#FFCE56', '#e10de1'],
  }]
};

const doughnutCanvas3 = document.getElementById('doughnutChart3').getContext('2d');

new Chart(doughnutCanvas3, {
    type: 'doughnut',
    data: doughnutData3,
});

const doughnutData4 = {
  labels: ['Child Population of India', 'Children with mental disorders', 'Children not seeking support'],
  datasets: [{
    data: [248550000, 50000000, 42500000],
    backgroundColor: ['#FFCE56', '#e10de1', '#23246c'],
  }]
};

const doughnutCanvas4 = document.getElementById('doughnutChart4').getContext('2d');

new Chart(doughnutCanvas4, {
    type: 'doughnut',
    data: doughnutData4,
});



