# REALTOR Listing Dashboard Redesign Prompt

Use this prompt to turn an existing REALTOR.ca listing-statistics dashboard into
a polished, production-ready frontend without changing its underlying data or
behaviour.

Reference artifact:
<https://chat.homiesai.com/artifacts/50c0b604-ee46-4209-a5ca-bf25f5c84464>

## Prompt

Act as a world-class product designer and senior frontend engineer. Redesign
this REALTOR.ca listing performance dashboard into a premium, production-ready
analytics experience.

Do not return a plan—implement the redesign.

Preserve:

- All existing data and calculations
- The 7-day, 30-day, and 90-day/all-history filtering
- Current charts, listing information, tables, and contact functionality
- Existing framework and dependencies where practical

Do not invent metrics or trend data. Only show comparisons when supported by
the existing dataset.

### Design direction

Create a sophisticated real-estate analytics product—not a generic admin
template or marketing page.

Use:

- A warm off-white page background
- White cards
- Deep charcoal typography
- Restrained coral as the primary accent
- Muted eucalyptus green and warm gold for chart series
- Geist, Inter, or the project's existing modern sans-serif
- 16–20px card radii
- Subtle 1px borders and soft shadows
- Strong spacing, alignment, and typography hierarchy

Avoid:

- Glassmorphism
- Loud gradients
- Excessive pills and rounded containers
- Decorative elements that compete with the data
- Dense walls of equally weighted cards

### Layout

Build a centered, fluid dashboard with a max width around 1440px and generous
responsive gutters.

Desktop:

- Use a 12-column grid
- Create a polished 3-column listing sidebar and 9-column analytics area
- Keep the listing card sticky while the analytics content scrolls
- Do not use fixed viewport heights or nested scroll containers that clip
  content

Mobile and tablet:

- Stack everything in one natural page flow
- Ensure zero horizontal overflow at 375px
- Make charts, tables, tabs, and labels readable without horizontal scrolling
- Test at 375px, 768px, 1024px, and 1440px

### Listing card

Elevate the property section into a premium listing summary:

- Render the property image immediately inside a stable 4:3 container using
  `object-fit: cover`
- Prevent image collapse or layout shift with a proper aspect ratio and
  skeleton state
- Show “Active listing” and the MLS number as understated metadata
- Make the address the primary heading
- Present price and days live as the strongest facts
- Arrange updated date, property ID, location, and brokerage with clean
  hierarchy
- Keep the card compact; remove unnecessary empty space

### Dashboard header

Create a clean header containing:

- Eyebrow: “REALTOR.ca listing stats”
- Title: “Performance dashboard”
- Selected period shown clearly but not redundantly
- A refined segmented timeframe control aligned to the right on desktop and
  full-width on mobile

The active timeframe must be obvious. Add polished hover, pressed, focus, and
keyboard states.

### Executive summary

Move the existing readout near the top as an “Executive takeaway” insight card.
Make it immediately answer:

- How much attention is the listing receiving?
- What actions are users taking?
- Is engagement converting into leads?
- How does this compare with the prior listing?

Keep the language factual and concise.

### KPI hierarchy

Do not give every KPI equal visual weight.

Primary KPIs:

- Views: 131
- Actions: 60

Secondary KPIs:

- Email leads: 0
- Photo views: 56
- Directions: 2
- Favourites: 1

Make Views and Actions larger, with clearer supporting context. Use small
semantic icons and restrained accent colors. If no trend comparison exists, do
not fabricate arrows or percentages.

### Charts

Create a balanced analytics grid:

- “Views and actions by period” should be the dominant chart
- “Source distribution” should be a smaller companion card
- Keep chart heights consistent and prevent labels from clipping
- Use accessible, visually distinct colors
- Add useful hover tooltips and clear legends
- Reduce unnecessary gridlines
- Format dates more naturally
- Put the DDF percentage or total in the center of the donut chart

Use subtle 150–200ms transitions when the timeframe changes. Avoid distracting
entrance animations.

### Action breakdown

Transform the dense table into a more scannable breakdown:

- Emphasize non-zero actions first
- Show count, share, and a proportional bar
- Keep all zero-value rows available inside a collapsed “Show inactive
  metrics” section
- Preserve every reported row
- On mobile, convert rows into compact stacked items instead of squeezing the
  desktop table

### DDF sources

Replace the plain DDF table with a ranked source list:

- Source name
- View count
- Small proportional horizontal bar
- Clear empty state when no advertising-site data exists

### Prior listing comparison

Turn the inactive-listing context into a purposeful comparison card:

- Current vs. prior price
- Days live
- Views
- Interactions
- Clearly surface the $50,000 lower current price
- Explain visually that the current listing is still early in its exposure
  window
- Do not imply performance conclusions unsupported by the data

### Contact widget

Keep the USER contact function, but make it unobtrusive. Use `USER` anywhere a
personal contact name appears; do not hardcode a real person's name.

- Default to a compact floating avatar/button
- Do not cover timeframe controls, KPIs, charts, or table content
- On mobile, respect safe-area spacing and keep the expanded message
  dismissible
- Never auto-expand repeatedly after dismissal

### Quality bar

- WCAG AA contrast
- Semantic headings, navigation, tables, and buttons
- Visible focus states
- Touch targets of at least 44px
- Proper loading, empty, and zero-data states
- No layout shift
- No clipped content
- No horizontal overflow
- Smooth responsive behaviour
- Preserve functionality while substantially improving visual hierarchy and
  polish

The final result should feel like a premium analytics product built for a
top-performing real-estate professional: calm, credible, highly legible, and
immediately actionable.
