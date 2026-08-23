# Python OOP入门 - Design Spec

> Python 面向对象编程入门课件，7页精简风格。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | python_oop_ppt169_20260630 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 7 |
| **Design Style** | clean-minimal — dark coding theme |
| **Target Audience** | Python 初学者 |
| **Use Case** | 课堂教学投屏，3分钟概述 |
| **Delivery Purpose** | presentation |
| **Content Strategy** | balanced — 跟随笔记结构，精炼表达 |
| **Created Date** | 2026-06-30 |

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 60px, top/bottom 50px |
| **Content Area** | 1160×620 |

## III. Visual Theme

### Theme Style
- **Mode**: instructional
- **Visual style**: clean-minimal
- **Theme**: Dark theme
- **Tone**: Tech, modern, educational

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#1A1A2E` | Page background |
| **Secondary bg** | `#252540` | Card/section backgrounds |
| **Code bg** | `#141428` | Code block background |
| **Primary** | `#00BFA5` | Accent — titles, icons, highlights |
| **Secondary accent** | `#448AFF` | Blue emphasis |
| **Tertiary accent** | `#FF6D00` | Orange — warnings, contrast |
| **Alert** | `#FF5252` | Red — danger/risk indicators |
| **Body text** | `#FFFFFF` | Main text on dark bg |
| **Secondary text** | `#B0B0C0` | Descriptions, captions |
| **Border** | `#333355` | Card borders, dividers |

## IV. Typography

| Element | Font | Size |
|---------|------|------|
| **Title** | Arial Black | 36-44px bold |
| **Section header** | Calibri | 20-24px bold |
| **Body** | Calibri Light | 16px |
| **Code** | Consolas | 13px |
| **Caption** | Calibri Light | 11px |

## V. Layout

- **Rhythm**: breathing — one idea per page, generous whitespace
- **Card style**: Rounded rectangles with subtle shadow, left accent bar
- **Icon treatment**: White icons in colored circles (60px diameter)
- **Code blocks**: Darker bg (`#141428`), Consolas font, left padding

## VI. Icon

- **Library**: Feather-style SVG icons
- **Style**: Stroke-based, white fill in colored circles
- **Usage**: One icon per concept card, semantic pairing

## VII. Visualization

No data charts in this deck.

## VIII. Image Resource List

No external images — pure vector/icon graphics.

## IX. Content Outline

| Page | Title | Key Visual | Content |
|------|-------|------------|---------|
| 1 | 封面 | Python logo + accent circles | Python 面向对象入门 — 从"自己干"到"让别人干" |
| 2 | 编程思想 | Left/Right comparison cards + VS circle | 过程（扫地拖地擦桌子）vs 对象（喊胖虎干活） |
| 3 | OOP三步走 | 3 numbered cards + arrows | 设计class → 创建对象 → 对象干活 |
| 4 | self 的作用 | Two character circles + center method box | stu1 vs stu2，同一个sleep(self)，self指向不同 |
| 5 | 四个魔法方法 | 2×2 grid cards | __init__ / __str__ / __eq__ / __del__ |
| 6 | 封装私有 | Before/After comparison | 无私有（危险）vs 有私有（安全） |
| 7 | 总结 | 3 stat cards + green bar | 3步走 / 4魔法方法 / 3大特征 + 谢谢 |

## X. Speaker Notes

Brief Chinese narration for each page, ~25 seconds per page.

## XI. Tech Constraints

- viewBox: 0 0 1280 720
- No external images — all vector graphics
- PPT-safe fonts: Arial Black, Calibri, Consolas
- No accent lines under titles
