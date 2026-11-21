from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36

BG = (247, 243, 234)
CARD = (255, 253, 246)
CARD_EDGE = (203, 192, 168)
HERO_BG = (255, 253, 246)
TEXT = (26, 26, 26)
MUTED = (90, 83, 72)
ACCENT = (176, 58, 46)
DATE_LINE = (176, 58, 46)

F_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

STORIES = [
    ("DIPLOMACY · SHENZHEN", "Trump, Xi and Putin issue joint peace declaration", "First trilateral summit ends with a symbolic declaration; no binding arms deal."),
    ("UKRAINE · KYIV", "Russia pounds Kyiv, three Dnipro bridges hit", "Missiles kill at least 3, wound 15"),
    ("UKRAINE", "Ukraine drones hit Russian chemical plant", "Dorogobuzh plant ablaze in Smolensk"),
    ("GERMANY", "Merz rejects 'new Yalta' over Europe's future", "Europe demands seat at settlement talks"),
    ("EU–UK SUMMIT", "EU and UK hold summit in Brussels", "Trade, energy, security, youth mobility"),
    ("DENMARK · GREENLAND", "Denmark OKs Greenland–US Arctic pact", "US presence up, sovereignty kept"),
    ("MYANMAR · ICJ", "Court: Myanmar committed Rohingya genocide", "Reparations ordered; 1m+ displaced"),
    ("TAIWAN", "Taiwan flags 2,700 alleged China accounts", "Election interference on Meta apps"),
    ("AUSTRALIA–JAPAN", "Australia, Japan deepen security ties", "Indo-Pacific coordination grows"),
    ("NVIDIA · US", "California subpoenas Nvidia over China", "Probe into chips and confidential data"),
    ("INDIA · CYCLONE", "Cyclone Akvan makes landfall in Odisha", "Flooding feared on eastern coast"),
    ("SOUTH KOREA", "First cholera case in a decade confirmed", "Health authorities trace the source"),
    ("BANGLADESH", "Bangladesh tense amid protests, factories shut", "341 garment factories shut in protests"),
    ("IMF · DEBT", "IMF warns global debt nearing 100% of GDP", "Highest level since World War II"),
    ("JAPAN · INFLATION", "Japan core inflation accelerates to 2.2%", "October rise fuels rate-hike debate"),
    ("IRAQ", "Iraq compromises with Kataib Hezbollah", "Forces to enter Jurf al-Sakhar"),
    ("HORMUZ", "Tanker ablaze after mine strike in Hormuz", "Iran war enters ninth month"),
    ("SAUDI ARABIA", "Houthi missiles damage Riyadh financial tower", "PIF tower hit; interceptions reported"),
    ("IRAN · US COST", "US Iran campaign cost put at $48.3 billion", "Pentagon figure stirs spending debate"),
    ("GAZA", "Israeli forces cross Yellow Line in Gaza", "First incursion since the truce began"),
    ("SOMALIA · UAE", "Somalia expels UAE ambassador", "Given 72 hours to leave amid dispute"),
    ("PACIFIC · CLIMATE", "Pacific islands face climate pressure", "Drought, storms and rising seas"),
    ("COP31 · CLIMATE", "COP31 draft drops fossil-fuel phase-out", "Africa presses for climate finance"),
    ("KENYA · EBOLA", "Kenya discharges last Ebola patient", "42-day countdown to Ebola-free status"),
    ("US · CYBER", "White House cyber chief out after outages", "Cairncross leaves amid disruptions"),
    ("HAITI", "34 suspected gang members killed in raid", "Police operation in Martissant"),
    ("EL SALVADOR", "Bukele moves toward third presidential bid", "Constitutional limits debated anew"),
    ("BRAZIL · AMAZON", "Lula advances Indigenous land rights", "Territory recognition with Chief Raoni"),
    ("US SENATE", "Senate passes energy bill 62–33", "Permitting reform heads to the House"),
    ("CYCLONE XAVIER", "Severe Cyclone Xavier churns in South Pacific", "Category 4 storm tracked by Fiji Met"),
    ("MARKETS · AI", "Stocks slide as AI valuations questioned", "S&P 500 down a fifth straight session"),
    ("VOYAGER 1", "Voyager 1 signals now take a day to Earth", "Probe at 24-hour light distance"),
    ("FIONA", "Fiona the hippo dies at Cincinnati Zoo", "Beloved animal ambassador mourned"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(draw, text, fnt, max_w, max_lines):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = (cur + " " + word) if cur else word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    truncated = len(lines) > max_lines
    lines = lines[:max_lines]
    if truncated and lines:
        last = lines[-1]
        while last and draw.textlength(last + "…", font=fnt) > max_w:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines


def fit_line(draw, text, fnt, max_w):
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + "…", font=fnt) > max_w:
        text = text[:-1]
    return text + "…"


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

draw.text((MARGIN, 28), "WORLD NEWS DIGEST", font=font(F_SERIF_B, 32), fill=TEXT)
draw.text((MARGIN, 68), "FRIDAY, 20 NOVEMBER 2026", font=font(F_SANS_B, 15), fill=DATE_LINE)
count_text = "33 stories"
count_fnt = font(F_SANS, 12)
draw.text((W - MARGIN - draw.textlength(count_text, font=count_fnt), 68), count_text, font=count_fnt, fill=MUTED)
draw.line([(MARGIN, 92), (W - MARGIN, 92)], fill=TEXT, width=3)
draw.line([(MARGIN, 97), (W - MARGIN, 97)], fill=TEXT, width=1)

hero_cat, hero_head, hero_sum = STORIES[0]
draw.rectangle([(MARGIN, 104), (W - MARGIN, 208)], fill=HERO_BG, outline=CARD_EDGE, width=1)
draw.text((MARGIN + 14, 116), hero_cat, font=font(F_SANS_B, 11), fill=ACCENT)
head_fnt = font(F_SERIF_B, 25)
sum_fnt = font(F_SANS, 13)
head_max_w = W - 2 * MARGIN - 28
y = 132
for line in wrap_lines(draw, hero_head, head_fnt, head_max_w, 2):
    draw.text((MARGIN + 14, y), line, font=head_fnt, fill=TEXT)
    y += 29
for line in wrap_lines(draw, hero_sum, sum_fnt, head_max_w, 2):
    draw.text((MARGIN + 14, y), line, font=sum_fnt, fill=MUTED)
    y += 16

gx, gy = MARGIN, 216
cw, ch = 230, 87
p = 9
iw = cw - 2 * p
cat_fnt = font(F_SANS_B, 9)
card_head_fnt = font(F_SANS_B, 15)
try:
    card_sum_fnt = font(F_SANS, 10.5)
except Exception:
    card_sum_fnt = font(F_SANS, 10)

for i, (cat, head, summ) in enumerate(STORIES[1:]):
    col = i % 4
    row = i // 4
    x0 = gx + col * (cw + 10)
    y0 = gy + row * (ch + 8)
    x1 = x0 + cw
    y1 = y0 + ch
    draw.rectangle([(x0, y0), (x1, y1)], fill=CARD, outline=CARD_EDGE, width=1)
    draw.text((x0 + p, y0 + 7), fit_line(draw, cat, cat_fnt, iw), font=cat_fnt, fill=ACCENT)
    hy = y0 + 21
    for line in wrap_lines(draw, head, card_head_fnt, iw, 2):
        draw.text((x0 + p, hy), line, font=card_head_fnt, fill=TEXT)
        hy += 17
    draw.text((x0 + p, y0 + 60), fit_line(draw, summ, card_sum_fnt, iw), font=card_sum_fnt, fill=MUTED)

draw.text((MARGIN, 978), "Sources: Open Chronicle Global News Brief · Friday 20 November 2026", font=font(F_SANS, 10), fill=MUTED)

img.save("entry.png", "PNG", optimize=True)
import os
print(os.path.getsize("entry.png"))
