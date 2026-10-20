# Instructions for Claude working on this repo / BWR content

## Background info vs. output content — hard rule

When the user gives context, status, or instructions in chat (e.g. "there will be three
panelists," "we don't have a photo yet," "pricing isn't public"), that information is for
decision-making only. It must never be transcribed, paraphrased, or summarized directly into
a deliverable (website copy, social graphics, flyers, etc.) unless the user is explicitly
giving you copy to use verbatim.

Concretely, never write things like:
- "Also on the panel: [Name], and one more member to be announced" (process note)
- "No prep needed" (recruiting language, not audience-facing copy)
- Any sentence that reads as a note *about* how the piece was assembled, what's still missing,
  or what the user told Claude, rather than content meant for the end audience.

If information is incomplete (e.g. a third panelist isn't confirmed), either leave it out of
the piece entirely, use a clearly-marked placeholder (e.g. "[Date]"), or ask the user — don't
narrate the gap in the output itself. Every line on a finished piece should be something the
intended audience is meant to read, not a note to/from the user.

## "Bouncing Back" panelist content — required fields

Every panelist-facing piece (speaker spotlight card, the main flyer's photo card, any future
per-panelist graphic) must include all three of:
1. Name
2. Time spent searching/unemployed before landing the role
3. New job title

Don't drop the "time spent searching" figure just because space is tight — it's the point of
the story (the comeback), not optional detail.

## "Bouncing Back" visual template — use the bold poster style

The user explicitly rejected the quiet dark-panel/circle-avatar template (plain forest
background, small circular photo, centered text) for this series. The approved template is
the bold poster style matching the DC Startup & Tech Week reference the user shared: color-
block background shapes (gold diagonal, etc.), a large gold-bordered photo frame with a
semi-transparent name/journey bar overlaid directly on the bottom of the photo, and stacked
color info-bands (oxblood date/time band, gold RSVP band) at the very bottom of the canvas.

This is implemented in `bold-poster-styles.css` in the social-templates scratchpad folder.
Every piece in the "Bouncing Back" series (the main flyer and each individual speaker card)
should use this shared stylesheet/structure — don't reintroduce the old dark-panel template.
