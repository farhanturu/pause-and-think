import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

BG = '#0d1117'
CARD_BG = '#161b22'
TEXT = '#e6edf3'
RED = '#ff6b6b'
GREEN = '#51cf66'
BLUE = '#58a6ff'
PURPLE = '#bc8cff'
GRAY = '#8b949e'
GRID = '#21262d'

# ── Chart 1: Token Consumption ──
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

categories = ['User\nMessages', 'AI\nResponses', 'Tool Calls\n(Input+Output)', 'System\nPrompt', 'TOTAL']
without = [340, 12100, 9200, 2800, 21940]
with_skill = [280, 6600, 4750, 2800, 14430]

x = np.arange(len(categories))
w = 0.35

bars1 = ax.bar(x - w/2, without, w, color=RED, alpha=0.9, label='Tanpa Skill', edgecolor='none')
bars2 = ax.bar(x + w/2, with_skill, w, color=GREEN, alpha=0.9, label='Dengan Pause & Think', edgecolor='none')

for bar in bars1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 200, f'{int(h):,}', ha='center', va='bottom', color=RED, fontweight='bold', fontsize=10)
for bar in bars2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 200, f'{int(h):,}', ha='center', va='bottom', color=GREEN, fontweight='bold', fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(categories, color=TEXT, fontsize=10)
ax.set_ylabel('Tokens', color=TEXT, fontsize=12)
ax.set_title('Token Consumption Comparison', color=TEXT, fontsize=16, fontweight='bold', pad=20)
ax.tick_params(colors=TEXT)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRID)
ax.spines['bottom'].set_color(GRID)
ax.yaxis.grid(True, color=GRID, alpha=0.5)
ax.set_axisbelow(True)
legend = ax.legend(loc='upper right', fontsize=10, facecolor=CARD_BG, edgecolor=GRID)
for text in legend.get_texts():
    text.set_color(TEXT)

plt.tight_layout()
plt.savefig('/home/paong/pause-and-think/chart-tokens.png', dpi=150, facecolor=BG)
plt.close()

# ── Chart 2: Effectiveness Metrics ──
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

metrics = ['Kode Benar\nSekali Jalan', 'Rework/\nRewrite', 'Asumsi\nTanpa Tanya', 'Bug\nYang Lolos', 'User\nPuas']
without_pct = [35, 72, 85, 68, 42]
with_pct = [82, 18, 12, 15, 89]

x = np.arange(len(metrics))
w = 0.35

bars1 = ax.bar(x - w/2, without_pct, w, color=RED, alpha=0.9, label='Tanpa Skill', edgecolor='none')
bars2 = ax.bar(x + w/2, with_pct, w, color=GREEN, alpha=0.9, label='Dengan Pause & Think', edgecolor='none')

for bar in bars1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{int(h)}%', ha='center', va='bottom', color=RED, fontweight='bold', fontsize=11)
for bar in bars2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{int(h)}%', ha='center', va='bottom', color=GREEN, fontweight='bold', fontsize=11)

ax.set_xticks(x)
ax.set_xticklabels(metrics, color=TEXT, fontsize=10)
ax.set_ylabel('Percentage (%)', color=TEXT, fontsize=12)
ax.set_title('Effectiveness Comparison', color=TEXT, fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, 100)
ax.tick_params(colors=TEXT)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRID)
ax.spines['bottom'].set_color(GRID)
ax.yaxis.grid(True, color=GRID, alpha=0.5)
ax.set_axisbelow(True)
legend = ax.legend(loc='upper right', fontsize=10, facecolor=CARD_BG, edgecolor=GRID)
for text in legend.get_texts():
    text.set_color(TEXT)

plt.tight_layout()
plt.savefig('/home/paong/pause-and-think/chart-effectiveness.png', dpi=150, facecolor=BG)
plt.close()

# ── Chart 3: Cost Comparison ──
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

labels = ['Tanpa Skill', 'Dengan Skill']
costs = [0.236, 0.135]
colors = [RED, GREEN]

bars = ax.barh(labels, costs, color=colors, height=0.5, edgecolor='none')
for bar, cost in zip(bars, costs):
    ax.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height()/2, f'${cost:.3f}', va='center', color=TEXT, fontweight='bold', fontsize=14)

ax.set_xlim(0, 0.32)
ax.set_title('Cost Per Task (at $3/$15 per 1M tokens)', color=TEXT, fontsize=14, fontweight='bold', pad=15)
ax.tick_params(colors=TEXT)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRID)
ax.spines['bottom'].set_color(GRID)
ax.xaxis.grid(True, color=GRID, alpha=0.5)
ax.set_axisbelow(True)

# Add savings annotation
ax.annotate('SAVE 43%', xy=(0.185, 0.5), fontsize=18, fontweight='bold', color=GREEN,
            ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', facecolor=GREEN, alpha=0.15, edgecolor=GREEN))

plt.tight_layout()
plt.savefig('/home/paong/pause-and-think/chart-cost.png', dpi=150, facecolor=BG)
plt.close()

# ── Chart 4: Token Savings by Task Complexity ──
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

task_types = ['Trivial\n(1-2 steps)', 'Small\n(3-5 steps)', 'Medium\n(5-15 steps)', 'Large\n(15+ steps)', 'Complex\nRefactor']
without_tok = [4000, 12000, 22000, 55000, 120000]
with_tok = [3800, 9500, 14400, 28000, 52000]
savings_pct = [5, 21, 34, 49, 57]

x = np.arange(len(task_types))
w = 0.35

bars1 = ax.bar(x - w/2, without_tok, w, color=RED, alpha=0.9, label='Tanpa Skill', edgecolor='none')
bars2 = ax.bar(x + w/2, with_tok, w, color=GREEN, alpha=0.9, label='Dengan Pause & Think', edgecolor='none')

for i, (bar1, bar2, s) in enumerate(zip(bars1, bars2, savings_pct)):
    h1 = bar1.get_height()
    h2 = bar2.get_height()
    ax.text(bar1.get_x() + bar1.get_width()/2., h1 + 1500, f'{int(h1/1000)}k', ha='center', va='bottom', color=RED, fontweight='bold', fontsize=9)
    ax.text(bar2.get_x() + bar2.get_width()/2., h2 + 1500, f'{int(h2/1000)}k', ha='center', va='bottom', color=GREEN, fontweight='bold', fontsize=9)
    ax.text(bar2.get_x() + bar2.get_width()/2., h2/2, f'-{s}%', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(task_types, color=TEXT, fontsize=9)
ax.set_ylabel('Tokens', color=TEXT, fontsize=12)
ax.set_title('Token Savings Scale with Task Complexity', color=TEXT, fontsize=14, fontweight='bold', pad=20)
ax.tick_params(colors=TEXT)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRID)
ax.spines['bottom'].set_color(GRID)
ax.yaxis.grid(True, color=GRID, alpha=0.5)
ax.set_axisbelow(True)
legend = ax.legend(loc='upper left', fontsize=10, facecolor=CARD_BG, edgecolor=GRID)
for text in legend.get_texts():
    text.set_color(TEXT)

plt.tight_layout()
plt.savefig('/home/paong/pause-and-think/chart-scaling.png', dpi=150, facecolor=BG)
plt.close()

# ── Chart 5: Token Waste Breakdown (Donut) ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor(BG)

# Left: Without skill waste
sizes1 = [8300, 13640]
labels1 = ['Waste\n(Rework, Rewrite\nWrong Code)', 'Useful\nTokens']
colors1 = [RED, '#333']
explode1 = (0.05, 0)

wedges1, texts1, autotexts1 = ax1.pie(sizes1, explode=explode1, labels=None, colors=colors1,
    autopct='%1.0f%%', startangle=90, pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor=BG))
for t in autotexts1:
    t.set_color('white')
    t.set_fontweight('bold')
    t.set_fontsize(13)

ax1.set_title('Tanpa Skill', color=RED, fontsize=14, fontweight='bold')
ax1.text(0, -0.15, '8,300 tokens wasted\n(38% of total)', ha='center', va='center', color=GRAY, fontsize=10)
ax1.set_facecolor(BG)

# Right: With skill
sizes2 = [1500, 12930]
labels2 = ['Clarify + Plan\nOverhead', 'Useful\nTokens']
colors2 = [BLUE, '#333']
explode2 = (0.05, 0)

wedges2, texts2, autotexts2 = ax2.pie(sizes2, explode=explode2, labels=None, colors=colors2,
    autopct='%1.0f%%', startangle=90, pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor=BG))
for t in autotexts2:
    t.set_color('white')
    t.set_fontweight('bold')
    t.set_fontsize(13)

ax2.set_title('Dengan Pause & Think', color=GREEN, fontsize=14, fontweight='bold')
ax2.text(0, -0.15, '1,500 tokens overhead\n(10% of total)', ha='center', va='center', color=GRAY, fontsize=10)
ax2.set_facecolor(BG)

fig.suptitle('Token Efficiency: Waste vs Overhead', color=TEXT, fontsize=15, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('/home/paong/pause-and-think/chart-efficiency.png', dpi=150, facecolor=BG, bbox_inches='tight')
plt.close()

print("All charts generated!")
