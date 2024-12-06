$(document).ready(function () {
    let selectedSymptoms = [];
    const maxSymptoms = 376;

    function openSymptomList() {
        $('.container').show();
        $('.addSymptomsButton').hide();
    }

    function toggleAddMoreButton() {
        const buttonText = selectedSymptoms.length > 0 ? "Add More Symptoms" : "Add Symptoms";
        $('.addSymptomsButton span').text(buttonText);
        $('.addSymptomsButton').show();
    }

    function updateSelectedSymptomsList() {
        $('#selectedSymptomsList').empty();
        $('.sidebar').toggleClass('show', selectedSymptoms.length > 0);

        selectedSymptoms.forEach(function (symptom) {
            $('#selectedSymptomsList').append(
                `<li>
                    <span>${symptom}</span>
                    <span class="remove-symptom" data-symptom="${symptom}">➖</span>
                </li>`
            );
        });
    }

    document.getElementById('clearAllSymptoms').addEventListener('click', function () {
        selectedSymptoms = [];
        $('.addSymptomsButton').show();
        updateSelectedSymptomsList();
        updateSymptomDropdown();
        $('.result-container').removeClass('show');
        $('.disease-result').html('<p>No symptoms analyzed yet</p>');
    });

    function updateSymptomDropdown() {
        $('#symptomDropdown option').each(function () {
            $(this).toggle(!selectedSymptoms.includes($(this).val()));
        });
    }

    $('#selectButton').on('click', function () {
        if (selectedSymptoms.length > maxSymptoms) {
            alert('You can select a maximum of 376 symptoms.');
            return;
        }
        $('.container').hide();
        toggleAddMoreButton();
    });

    // Update only this part in your existing scripts.js
$('#searchButton').on('click', function () {
    if (selectedSymptoms.length === 0) {
        alert('Please select at least one symptom');
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/submit_symptoms', 
        contentType: 'application/json',
        data: JSON.stringify({ symptoms: selectedSymptoms }),
        success: function (response) {
            if (response.error) {
                $('.disease-result').html(`<p>Error: ${response.error}</p>`);
                $('.learn-more-btn, .rediagnose-btn').hide();
            } else {
                $('.disease-result').html(`<p>You might be suffering from ${response.disease}</p>`);
                
                // Hide the Add Symptoms button
                $('.addSymptomsButton').hide();
                
                // Show and update Learn More button
                $('.learn-more-btn')
                    .show()
                    .off('click')
                    .on('click', function() {
                        const searchQuery = encodeURIComponent(`${response.disease} disease symptoms treatment`);
                        window.open(`https://www.google.com/search?q=${searchQuery}`, '_blank');
                    });
                
                // Show and update Diagnose Again button
                $('.rediagnose-btn')
                    .show()
                    .off('click')
                    .on('click', function() {
                        location.reload();
                        $('.addSymptomsButton').show();
                    });
            }
            $('.result-container').addClass('show');
        },
        error: function (error) {
            console.error('Error:', error);
            $('.disease-result').html('<p>An error occurred while analyzing symptoms</p>');
            $('.learn-more-btn, .rediagnose-btn').hide();
            $('.result-container').addClass('show');
        }
    });
});

    $('#symptomDropdown').on('change', function () {
        const selectedOption = $(this).val();
        selectedOption.forEach(function (symptom) {
            if (!selectedSymptoms.includes(symptom) && selectedSymptoms.length < maxSymptoms) {
                selectedSymptoms.push(symptom);
            }
        });
        updateSelectedSymptomsList();
        updateSymptomDropdown();
    });

    function filterSymptoms() {
        const searchText = $('#searchBox').val().toLowerCase();
        $('#symptomDropdown option').each(function () {
            const symptom = $(this).text().toLowerCase();
            $(this).toggle(symptom.includes(searchText) && !selectedSymptoms.includes($(this).val()));
        });
    }

    $('#searchBox').on('input', filterSymptoms);

    $('#selectedSymptomsList').on('click', '.remove-symptom', function () {
        const symptom = $(this).data('symptom');
        selectedSymptoms = selectedSymptoms.filter(s => s !== symptom);
        updateSelectedSymptomsList();
        updateSymptomDropdown();
    });

    $('.addSymptomsButton').on('click', openSymptomList);
    toggleAddMoreButton();

    // FAQ button toggle
    document.querySelector('.faq-button').addEventListener('click', function () {
        document.querySelector('.help-sidebar').classList.toggle('show');
    });

    function showAnswer(answerId) {
        // Get the clicked answer element
        const answer = $(`#${answerId}`);
        
        // Toggle the clicked answer with animation
        answer.slideToggle(300);
        
        // Get the arrow icon for the clicked item
        const arrowIcon = answer.prev('.help-sidebar-item').find('.arrow-icon');
        
        // Toggle arrow direction
        if (answer.is(':visible')) {
            arrowIcon.html('&#x25BC;');
        } else {
            arrowIcon.html('&#x25B6;');
        }
        
        // Hide other answers
        $('.help-sidebar-answer-popup').not(answer).slideUp(300);
        $('.help-sidebar-item').not(answer.prev()).find('.arrow-icon').html('&#x25B6;');
    }

    // Initialize FAQ functionality when document is ready
    $(document).ready(function() {
        // Add click handlers to FAQ items
        $('.help-sidebar-item').click(function() {
            const answerId = $(this).next('.help-sidebar-answer-popup').attr('id');
            showAnswer(answerId);
        });
        
        // Close FAQs when clicking outside
        $(document).click(function(event) {
            if (!$(event.target).closest('.help-sidebar').length) {
                $('.help-sidebar-answer-popup').slideUp(300);
                $('.arrow-icon').html('&#x25B6;');
            }
        });
    });

    document.querySelector('.about-section').addEventListener('click', function () {
        document.querySelector('.card').classList.toggle('show');
    });

    document.querySelector('.about-close').addEventListener('click', function () {
        document.querySelector('.card').classList.toggle('show');
    });

    document.querySelector('.contact-section').addEventListener('click', function () {
        document.querySelector('.form').classList.toggle('show');
    });

    document.querySelector('.contact-submit').addEventListener('click', function () {
        const email = document.querySelector('input[type="email"]').value;
        const message = document.querySelector('textarea').value;
        alert(`Email: ${email}\nMessage: ${message}`);
        document.querySelector('.form').classList.toggle('show');
    });

    document.querySelector('.help-section').addEventListener('click', function () {
        document.querySelector('.help-sidebar').classList.toggle('show');
    });

    // News and Slider Functions
    function fetchAndDisplayNews() {
        $.ajax({
            url: '/get-news',
            method: 'GET',
            success: function(response) {
                const articles = response.articles || [];
                if (articles.length > 0) {
                    updateSlider(articles);
                } else {
                    console.log('No news articles available');
                }
            },
            error: function(error) {
                console.error('Error fetching news:', error);
                // Show default slides if news fetch fails
                showDefaultSlides();
            }
        });
    }

    function updateSlider(articles) {
        const sliderContainer = $('#sliderContainer');
        sliderContainer.empty();
        
        articles.forEach((article, index) => {
            const slide = $(`
                <div class="slide ${index === 0 ? 'active' : ''}">
                    <img src="${article.urlToImage}" 
                         alt="${article.title}">
                    <div class="slide-content">
                        <div class="slide-title">${article.title}</div>
                        <div class="slide-description">${article.description || ''}</div>
                    </div>
                </div>
            `);
            sliderContainer.append(slide);
        });

        // Update pagination
        const pagination = $('#pagination');
        pagination.empty();
        articles.forEach((_, index) => {
            pagination.append(`<span class="dot ${index === 0 ? 'active' : ''}" data-index="${index}"></span>`);
        });

        // Initialize slider functionality
        initializeSlider();
    }

    function showDefaultSlides() {
        const defaultSlides = [
            {
                title: 'Welcome to Health Check',
                description: 'Your personal health assistant for preliminary disease identification.',
                image: 'static/images/slide1.jpg'
            },
            {
                title: 'How It Works',
                description: 'Select your symptoms and let our AI analyze potential conditions.',
                image: 'static/images/slide2.jpg'
            },
            {
                title: 'Important Note',
                description: 'This tool is for informational purposes only. Always consult a healthcare professional.',
                image: 'static/images/slide3.jpg'
            }
        ];

        updateSlider(defaultSlides.map(slide => ({
            title: slide.title,
            description: slide.description,
            urlToImage: slide.image
        })));
    }

    function initializeSlider() {
        let currentSlide = 0;
        const slides = $('.slide');
        const dots = $('.dot');
        const totalSlides = slides.length;

        function showSlide(index) {
            slides.removeClass('active');
            dots.removeClass('active');
            $(slides[index]).addClass('active');
            $(dots[index]).addClass('active');
        }

        // Auto advance slides
        setInterval(() => {
            currentSlide = (currentSlide + 1) % totalSlides;
            showSlide(currentSlide);
        }, 5000);

        // Click handlers for pagination dots
        dots.click(function() {
            currentSlide = $(this).data('index');
            showSlide(currentSlide);
        });
    }

    // Initialize news slider
    fetchAndDisplayNews();

    // Add this for FAQ functionality
    $(document).ready(function() {
        $('.faq-question').click(function() {
            // Close all other answers
            $('.faq-answer').not($(this).next()).slideUp();
            $('.faq-question').not($(this)).removeClass('active');
            
            // Toggle current answer
            $(this).next().slideToggle();
            $(this).toggleClass('active');
        });
    });
});
