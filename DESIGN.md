# Design System

## SmartStock – Clean. Fast. Professional.

This document defines the visual design system, UI components, layout conventions, and user experience guidelines for SmartStock. The goal is a clean, professional interface appropriate for a local shop environment.

---

## 1. Design Principles

**Professional & Trustworthy**
The interface should feel reliable and business-grade, not like a toy project.

**Speed First**
The Billing/POS screen is used many times per day. Every interaction must be fast.

**Minimal Friction**
Reduce clicks and form fields where possible. Show the right information at the right time.

**Responsive**
Works correctly on desktops, tablets, and mobile screens.

**Consistent**
All pages follow the same layout, component, and spacing conventions.

---

## 2. Color Palette

| Name             | Value     | Usage                                         |
|------------------|-----------|-----------------------------------------------|
| Primary          | `#0d6efd` | Buttons, links, active nav items (Bootstrap primary) |
| Success          | `#198754` | Stock OK, sale completed, positive amounts    |
| Warning          | `#ffc107` | Low stock alerts, caution states              |
| Danger           | `#dc3545` | Out of stock, errors, destructive actions     |
| Info             | `#0dcaf0` | UPI payment badge, informational states       |
| Dark             | `#212529` | Navbar background                             |
| Light            | `#f8f9fa` | Page background, table header, card background|
| Text Primary     | `#212529` | Main headings and body text                   |
| Text Muted       | `#6c757d` | Labels, subtitles, secondary information      |

---

## 3. Typography

**Font Family:** Bootstrap default system font stack (native OS fonts for performance)

| Element       | Bootstrap Class     | Usage                          |
|---------------|---------------------|--------------------------------|
| Page Title    | `h2` / `fw-bold`    | Main page headings             |
| Card Title    | `h4` / `fw-bold`    | Section headings               |
| Table Header  | `th` (table-light)  | Column headers                 |
| Body Text     | Default             | General text                   |
| Muted Text    | `text-muted small`  | Labels, secondary descriptions |
| Monospace     | `font-monospace`    | Invoice numbers, SKUs          |
| Currency      | `₹` + `"%.2f"`      | All monetary values            |

---

## 4. Layout Convention

Every page follows this consistent layout structure:

```
[Navbar – dark bg, full width]
[Container]
  [Page Header Row]
    [Col: Title + Subtitle]          [Col-auto: Action Button (Add/Filter)]
  [Filter Card (where applicable)]
  [Content Card (table / form)]
[/Container]
```

**Container:** All content uses Bootstrap `.container` (not `.container-fluid`).
**Spacing:** Use Bootstrap spacing utilities (`mb-4`, `py-3`, `p-4`, etc.). Avoid custom inline styles.
**Cards:** All content blocks use `.card.shadow-sm.border-0` for consistency.

---

## 5. UI Components

### Buttons

| Type        | Class                      | Usage                            |
|-------------|----------------------------|----------------------------------|
| Primary     | `btn btn-primary`          | Main action (Save, Submit)       |
| Success     | `btn btn-success`          | Complete sale, confirm positive  |
| Outline     | `btn btn-outline-primary`  | Secondary actions (View, Adjust) |
| Outline Danger | `btn btn-outline-danger` | Deactivate, remove item         |
| Small       | `btn btn-sm`               | Table row actions                |

### Badges (Status Indicators)

| State       | Class          | Usage                           |
|-------------|----------------|---------------------------------|
| Active      | `badge bg-success` | Product/Category active     |
| Inactive    | `badge bg-secondary` | Deactivated items         |
| Low Stock   | `badge bg-danger` | Stock ≤ min_stock_level      |
| Completed   | `badge bg-success` | Sale status                 |
| Cash        | `badge bg-success` | Payment method              |
| UPI         | `badge bg-info text-dark` | Payment method        |
| Card        | `badge bg-secondary` | Payment method            |
| Stock-in    | `badge bg-success` | Inventory transaction type  |
| Stock-out   | `badge bg-warning text-dark` | Inventory transaction |
| Sale        | `badge bg-primary` | Inventory transaction type  |

### Tables

All data tables use:
```html
<table class="table table-hover mb-0 align-middle">
  <thead class="table-light"> ... </thead>
  <tbody> ... </tbody>
</table>
```
Wrapped in `.card.shadow-sm.border-0 > .card-body.p-0 > .table-responsive`.

### Forms

- Labels: `class="form-label fw-bold"`
- Inputs: `class="form-control"` or `class="form-select"`
- Required fields marked with `*` in the label
- Forms inside `.card.shadow-sm.border-0` with `.card-body.p-4`
- Submit button: `.btn.btn-primary.btn-lg` at the bottom

### Flash Messages

Bootstrap dismissible alerts:
```html
<div class="alert alert-{{ category }} alert-dismissible fade show shadow-sm" role="alert">
    {{ message }}
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>
```
Categories map: `success`, `danger`, `warning`, `info`.

---

## 6. Navigation

**Navbar order (left to right):**
```
SmartStock (brand) | Dashboard | 🛒 Billing POS | Categories | Products | Inventory | Customers | Sales | Reports (planned) | User: username | Logout
```

- Navbar: `navbar-dark bg-dark`
- Active billing link highlighted: `text-warning fw-bold`
- User display: right-aligned, separated by a border
- Logout: `text-danger`

---

## 7. POS (Billing) Screen Specifics

The billing screen is high-priority for usability:

- **Search input:** Large (`form-control-lg`), auto-focused, full-width
- **Dropdown results:** Appear below the search bar, show product name, stock, price
- **Cart table:** Large font for quick reading during fast-paced billing
- **Quantity input:** `form-control-lg` centered with min/max validation
- **Summary panel:** Right-aligned sticky card, shows Subtotal → Total prominently
- **Checkout button:** Full-width, large, green (`btn-success btn-lg`), disabled when cart empty

---

## 8. Invoice Design

Print-friendly invoice (`@media print` hides navbar, buttons, alerts):
- Dark header with shop name
- Two-column meta section (invoice number, date vs. payment, status)
- Bordered item table with line totals
- Footer total row highlighted in `table-success`
- Thank-you message at bottom
