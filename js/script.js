(function () {
  'use strict';

  // ---------- Mobile nav toggle ----------
  var navToggle = document.getElementById('nav-toggle');
  var navLinks = document.getElementById('nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---------- Countdown ----------
  // Update this to match the wedding date/time set in index.html.
  var WEDDING_DATE = new Date('2026-10-17T16:00:00-04:00');

  var elDays = document.getElementById('cd-days');
  var elHours = document.getElementById('cd-hours');
  var elMinutes = document.getElementById('cd-minutes');
  var elSeconds = document.getElementById('cd-seconds');

  function pad(num) {
    return String(num).padStart(2, '0');
  }

  function updateCountdown() {
    if (!elDays) return;

    var now = new Date();
    var diff = WEDDING_DATE - now;

    if (diff <= 0) {
      elDays.textContent = '00';
      elHours.textContent = '00';
      elMinutes.textContent = '00';
      elSeconds.textContent = '00';
      return;
    }

    var seconds = Math.floor(diff / 1000);
    var days = Math.floor(seconds / 86400);
    seconds -= days * 86400;
    var hours = Math.floor(seconds / 3600);
    seconds -= hours * 3600;
    var minutes = Math.floor(seconds / 60);
    seconds -= minutes * 60;

    elDays.textContent = pad(days);
    elHours.textContent = pad(hours);
    elMinutes.textContent = pad(minutes);
    elSeconds.textContent = pad(seconds);
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);

  // ---------- RSVP form ----------
  var form = document.getElementById('rsvp-form');
  var status = document.getElementById('form-status');

  if (form && status) {
    form.addEventListener('submit', function (event) {
      var action = form.getAttribute('action') || '';

      // Placeholder Formspree endpoint hasn't been configured yet.
      if (action.indexOf('YOUR_FORM_ID') !== -1) {
        event.preventDefault();
        status.textContent = 'RSVP form is not connected yet — see README.md for setup instructions.';
        status.className = 'form-status error';
        return;
      }

      event.preventDefault();
      status.textContent = 'Sending...';
      status.className = 'form-status';

      var data = new FormData(form);

      fetch(action, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' }
      })
        .then(function (response) {
          if (response.ok) {
            form.reset();
            status.textContent = 'Thank you! Your RSVP has been received.';
            status.className = 'form-status success';
          } else {
            status.textContent = 'Something went wrong. Please try again or contact us directly.';
            status.className = 'form-status error';
          }
        })
        .catch(function () {
          status.textContent = 'Something went wrong. Please check your connection and try again.';
          status.className = 'form-status error';
        });
    });
  }

  // ---------- Header shadow on scroll ----------
  var header = document.getElementById('site-header');
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 8) {
        header.style.borderBottomColor = 'rgba(0,0,0,0.08)';
      } else {
        header.style.borderBottomColor = 'transparent';
      }
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
})();
