# STRUGAL redesign validation

## Critique findings addressed

| Finding | Severity | Implemented change |
|---|---|---|
| Unexplained product names | High | Six system pages with distinguishing specifications, application guidance, comparison table and official PDFs. |
| Main journeys leave the site | High | Internal family, service, audience, industry, project and contact pages; official documents remain external and labelled. |
| Missing project evidence | High | Three Moroccan project pages with actual photographs, published credits and installed systems. |
| Small text and controls | High | 16px body copy, larger labels, 44px or larger primary controls, readable mobile product cards. |
| Low contrast gold text | High | Dark bronze for text on light backgrounds; gold retained as a brand surface and decorative accent. |
| Undifferentiated catalogue | Medium | Category filters and three groups: openings, envelope, interiors. |
| Late audience paths | Medium | Architect, installer and homeowner paths directly below the hero. |
| Inactive city labels | Medium | Seven locations with verified addresses, telephone links and Google Maps directions. |
| Repetitive visual rhythm | Medium | Video hero, audience shortcuts, technical sections, project photography and location selector. |

## Accessibility coverage

| Category / criterion | Change | Validation |
|---|---|---|
| Perceivable — 1.1.1, 1.3.1 | Alternative text, semantic headings, labels and comparison headers | Static checks across all 40 pages |
| Perceivable — 1.4.3 | Dark text, bronze links and readable brand buttons | Contrast calculations below |
| Operable — 2.1.1, 2.4.1, 2.4.7 | Skip link, visible focus, native controls, Escape dismisses navigation | Browser keyboard menu check and labelled control inspection |
| Motion — 2.2.2 | Native video without visible controls as requested; reduced-motion still image; pause out of view | Native 3840 × 2160 playback verified locally |
| Understandable — 3.3.1, 3.3.2 | Required form fields, clear labels, no false submission confirmation | Brief generation tested with sample input |
| Robust — 4.1.2 | Expanded/pressed state, location and filter status announcements | Browser accessibility tree inspected |

## Contrast checks

| Element | Foreground | Background | Ratio | Normal text |
|---|---|---|---|---|
| Body text | #242424 | #ffffff | 15.52:1 | Pass |
| Secondary text | #58585a | #ffffff | 7.10:1 | Pass |
| Bronze links | #77602f | #ffffff | 6.00:1 | Pass |
| Gold button text | #242424 | #ceb172 | 7.51:1 | Pass |
| Service links | #e2c78e | #242424 | 9.46:1 | Pass |

## Functional checks

- Local JavaScript syntax validation passed.
- All internal destinations, anchors, local assets, unique IDs, H1 counts and control labels passed across 40 pages.
- Desktop product page, mobile product page, family filtering, system filtering, location selection and project brief tested.
- Layout checked at 320px, 390px, 768px and 1280px. No page-wide horizontal overflow at 320px. Comparison table intentionally scrolls within its own region.
- User-supplied STRUGAL corporate film downloaded at its highest available resolution: 3840 × 2160, 25 fps. Original 4K video stream repackaged without re-encoding; H.264 compatibility versions added. Browser confirms native video, no iframe, controls=false and zero caption tracks.
- The rejected 3D window section remains removed.

## Limits

This is not a WCAG certification. VoiceOver/NVDA and real-device assistive technology testing have not been completed. Text over changing video frames requires ongoing visual review; an overlay maintains legibility. The project brief stays in the browser and can be copied; there is no email/CRM submission backend. Native playback depends on network availability, codec support and browser autoplay policy; a still image is retained when playback is unavailable. Addresses and specifications are sourced from the manufacturer and must be confirmed for a real order or visit.
