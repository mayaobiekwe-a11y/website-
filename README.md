# Jane & John — Wedding Website

A simple, static wedding website: hero with countdown, our story, event
details, photo gallery, travel info, registry links, and an RSVP form.
No build step required — just HTML, CSS, and vanilla JS.

## Structure

```
index.html      All page content and sections
css/style.css   Styling (colors, fonts, layout)
js/script.js    Countdown timer, mobile nav, RSVP form handling
```

## Customize your content

Everything is placeholder content — replace it before publishing:

- **Names, date, location** — `index.html`: hero section (`#top`) and
  `<title>`/meta description at the top of the file.
- **Countdown target** — `js/script.js`: update the `WEDDING_DATE`
  constant to match the date/time in the hero section.
- **Our Story** — `index.html`: `#story` section.
- **Ceremony/reception details, dress code** — `index.html`: `#details`
  section. Update the map links to point at your actual venues.
- **Photos** — `index.html`: `#gallery` section currently uses colored
  placeholder tiles (`.gallery-item`). Replace each `<div class="gallery-item ...">`
  with an `<img>` tag pointing at your own photos (add them to an
  `images/` folder), e.g.:
  ```html
  <div class="gallery-item">
    <img src="images/photo-1.jpg" alt="Description of the photo" />
  </div>
  ```
- **Travel & hotel info** — `index.html`: `#travel` section.
- **Registry links** — `index.html`: `#registry` section, update the
  `href` on each button.

## Setting up the RSVP form

The form is static and needs a form-handling service since there's no
backend. The easiest free option is [Formspree](https://formspree.io):

1. Create a free Formspree account and a new form.
2. Copy your form endpoint (looks like `https://formspree.io/f/xxxxxxx`).
3. In `index.html`, find the `<form id="rsvp-form" ...>` element and
   replace `YOUR_FORM_ID` in the `action` attribute with your endpoint.

Until you do this, submitting the form will show a friendly message
telling visitors the form isn't connected yet instead of failing silently.

Alternatives to Formspree: [Getform](https://getform.io),
[Netlify Forms](https://docs.netlify.com/forms/setup/) (if hosting on
Netlify), or a Google Form embedded/linked instead.

## Running locally

No build step — just open `index.html` in a browser, or serve the
folder locally, e.g.:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## Deploying

This site is fully static and can be hosted for free on:

- **GitHub Pages** — enable Pages on this repo (Settings → Pages),
  serving from the `main` branch root.
- **Netlify** or **Vercel** — connect the repo and deploy with default
  static settings (no build command needed).
