# Black Women Rising

Website for [Black Women Rising](https://blackwomenrising-org.com), a professional community for Black women navigating unemployment.

## Structure

Static site, no build step.

```
index.html          Home
about.html           Founder story + org background
membership.html      Membership tiers + community resources
coaching.html        Career coaching (offering in development)
contact.html         Contact info
assets/css/style.css Design system
assets/js/main.js    Nav toggle + active-link highlighting
```

## Local preview

Open `index.html` directly in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Deploying

Enable GitHub Pages in repo Settings → Pages → Deploy from branch `main` / root. No build step required.

## Known placeholders to swap in

- Founder headshot (currently a monogram) in `about.html` / `index.html`
- "Community in Action" gallery tiles in `about.html`
- Career coaching deliverables + pricing in `coaching.html`
- "At the Table" tier pricing once finalized
