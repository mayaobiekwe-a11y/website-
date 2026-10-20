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
