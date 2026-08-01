from pathlib import Path
from xml.sax.saxutils import escape


# Repository root: E:\Projects\GURUSARAN01
REPO_ROOT = Path(__file__).resolve().parents[1]

# Output location
OUTPUT_FILE = REPO_ROOT / "assets" / "info-card.svg"


PROFILE_LINES = [
    ("Role", "Data Analyst | Applied Data Scientist"),
    ("Education", "MSc Data Analytics & Decision Science"),
    ("Experience", "Business Intelligence | Software Engineering"),
    ("Building", "Customer Intelligence & AI Decision Platform"),
    ("Stack", "Python | SQL | Power BI | Machine Learning"),
    ("Tools", "FastAPI | Streamlit | Docker | Git"),
    ("Focus", "Analytics | Decision Systems | Generative AI"),
    ("Location", "Germany"),
    ("Status", "Open to Data and AI opportunities"),
]


def create_svg() -> str:
    width = 760
    height = 405

    label_x = 45
    value_x = 175
    first_line_y = 125
    line_spacing = 28

    text_elements = []

    for index, (label, value) in enumerate(PROFILE_LINES):
        y_position = first_line_y + index * line_spacing
        animation_delay = 0.2 + index * 0.18

        text_elements.append(
            f"""
            <g opacity="0">
                <animate
                    attributeName="opacity"
                    from="0"
                    to="1"
                    dur="0.45s"
                    begin="{animation_delay:.2f}s"
                    fill="freeze"
                />

                <text
                    x="{label_x}"
                    y="{y_position}"
                    class="label"
                >
                    {escape(label)}
                </text>

                <text
                    x="{value_x}"
                    y="{y_position}"
                    class="value"
                >
                    {escape(value)}
                </text>
            </g>
            """
        )

    lines_svg = "\n".join(text_elements)

    return f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}"
    role="img"
    aria-label="Gurusaran GitHub profile information"
>
    <defs>
        <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#0d1117" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>

        <filter id="shadow">
            <feDropShadow
                dx="0"
                dy="5"
                stdDeviation="8"
                flood-color="#000000"
                flood-opacity="0.35"
            />
        </filter>

        <style>
            .window-title {{
                fill: #c9d1d9;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 15px;
            }}

            .command {{
                fill: #58a6ff;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 18px;
                font-weight: 700;
            }}

            .label {{
                fill: #7ee787;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 15px;
                font-weight: 700;
            }}

            .value {{
                fill: #c9d1d9;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 15px;
            }}

            .cursor {{
                fill: #7ee787;
                animation: blink 1s steps(2, start) infinite;
            }}

            @keyframes blink {{
                50% {{
                    opacity: 0;
                }}
            }}
        </style>
    </defs>

    <rect
        x="10"
        y="10"
        width="{width - 20}"
        height="{height - 20}"
        rx="14"
        fill="url(#background)"
        stroke="#30363d"
        filter="url(#shadow)"
    />

    <!-- Terminal buttons -->
    <circle cx="38" cy="38" r="7" fill="#ff5f56" />
    <circle cx="60" cy="38" r="7" fill="#ffbd2e" />
    <circle cx="82" cy="38" r="7" fill="#27c93f" />

    <text x="110" y="44" class="window-title">
        gurusaran@github
    </text>

    <line
        x1="25"
        y1="62"
        x2="{width - 25}"
        y2="62"
        stroke="#30363d"
    />

    <text x="40" y="94" class="command">
        $ whoami
    </text>

    {lines_svg}

    <text x="40" y="{height - 30}" class="command">
        $<tspan class="cursor">_</tspan>
    </text>
</svg>
"""


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    svg_content = create_svg()
    OUTPUT_FILE.write_text(svg_content, encoding="utf-8")

    print("Animated information card created successfully.")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()