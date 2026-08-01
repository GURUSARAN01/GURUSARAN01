from pathlib import Path
from xml.sax.saxutils import escape


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = REPOSITORY_ROOT / "assets" / "data-ai-pipeline.svg"


WIDTH = 820
HEIGHT = 430

NODE_WIDTH = 180
NODE_HEIGHT = 72


NODES = [
    {
        "id": "raw-data",
        "x": 40,
        "y": 105,
        "title": "Raw Data",
        "subtitle": "SQL · APIs · Files",
        "icon": "01",
        "delay": 0.0,
    },
    {
        "id": "cleaning",
        "x": 320,
        "y": 105,
        "title": "Data Cleaning",
        "subtitle": "Pandas · Validation",
        "icon": "02",
        "delay": 0.6,
    },
    {
        "id": "analytics",
        "x": 600,
        "y": 105,
        "title": "Analytics",
        "subtitle": "SQL · Power BI",
        "icon": "03",
        "delay": 1.2,
    },
    {
        "id": "dashboard",
        "x": 40,
        "y": 255,
        "title": "Dashboard",
        "subtitle": "Insights · Decisions",
        "icon": "06",
        "delay": 3.0,
    },
    {
        "id": "api",
        "x": 320,
        "y": 255,
        "title": "FastAPI",
        "subtitle": "Prediction Service",
        "icon": "05",
        "delay": 2.4,
    },
    {
        "id": "model",
        "x": 600,
        "y": 255,
        "title": "ML Model",
        "subtitle": "Propensity · Profit",
        "icon": "04",
        "delay": 1.8,
    },
]


def create_node(
    x: int,
    y: int,
    title: str,
    subtitle: str,
    icon: str,
    delay: float,
) -> str:
    title = escape(title)
    subtitle = escape(subtitle)
    icon = escape(icon)

    return f"""
    <g>
        <rect
            x="{x}"
            y="{y}"
            width="{NODE_WIDTH}"
            height="{NODE_HEIGHT}"
            rx="12"
            class="node-background"
        >
            <animate
                attributeName="stroke"
                values="#30363d;#58a6ff;#30363d"
                dur="4s"
                begin="{delay}s"
                repeatCount="indefinite"
            />

            <animate
                attributeName="filter"
                values="url(#soft-shadow);url(#blue-glow);url(#soft-shadow)"
                dur="4s"
                begin="{delay}s"
                repeatCount="indefinite"
            />
        </rect>

        <circle
            cx="{x + 34}"
            cy="{y + 36}"
            r="19"
            class="number-background"
        >
            <animate
                attributeName="fill"
                values="#161b22;#1f6feb;#161b22"
                dur="4s"
                begin="{delay}s"
                repeatCount="indefinite"
            />
        </circle>

        <text
            x="{x + 34}"
            y="{y + 41}"
            text-anchor="middle"
            class="node-number"
        >
            {icon}
        </text>

        <text
            x="{x + 65}"
            y="{y + 31}"
            class="node-title"
        >
            {title}
        </text>

        <text
            x="{x + 65}"
            y="{y + 53}"
            class="node-subtitle"
        >
            {subtitle}
        </text>
    </g>
    """


def create_svg() -> str:
    nodes_svg = "\n".join(
        create_node(
            x=node["x"],
            y=node["y"],
            title=node["title"],
            subtitle=node["subtitle"],
            icon=node["icon"],
            delay=node["delay"],
        )
        for node in NODES
    )

    return f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
    role="img"
    aria-label="Animated Data and AI development pipeline"
>
    <defs>
        <linearGradient
            id="background-gradient"
            x1="0"
            y1="0"
            x2="1"
            y2="1"
        >
            <stop offset="0%" stop-color="#0d1117" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>

        <linearGradient
            id="header-gradient"
            x1="0"
            y1="0"
            x2="1"
            y2="0"
        >
            <stop offset="0%" stop-color="#58a6ff" />
            <stop offset="100%" stop-color="#7ee787" />
        </linearGradient>

        <filter id="soft-shadow">
            <feDropShadow
                dx="0"
                dy="4"
                stdDeviation="5"
                flood-color="#000000"
                flood-opacity="0.32"
            />
        </filter>

        <filter id="blue-glow">
            <feDropShadow
                dx="0"
                dy="0"
                stdDeviation="7"
                flood-color="#58a6ff"
                flood-opacity="0.75"
            />
        </filter>

        <filter id="green-glow">
            <feDropShadow
                dx="0"
                dy="0"
                stdDeviation="5"
                flood-color="#7ee787"
                flood-opacity="0.9"
            />
        </filter>

        <marker
            id="arrow"
            markerWidth="9"
            markerHeight="9"
            refX="8"
            refY="4.5"
            orient="auto"
        >
            <path
                d="M0,0 L9,4.5 L0,9 Z"
                fill="#484f58"
            />
        </marker>

        <path
            id="path-1"
            d="M220 141 H320"
        />

        <path
            id="path-2"
            d="M500 141 H600"
        />

        <path
            id="path-3"
            d="M690 177 V255"
        />

        <path
            id="path-4"
            d="M600 291 H500"
        />

        <path
            id="path-5"
            d="M320 291 H220"
        />

        <style>
            .outer-background {{
                fill: url(#background-gradient);
                stroke: #30363d;
                stroke-width: 1.5;
            }}

            .terminal-title {{
                fill: #c9d1d9;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 14px;
            }}

            .main-title {{
                fill: url(#header-gradient);
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                    Helvetica, Arial, sans-serif;
                font-size: 22px;
                font-weight: 700;
            }}

            .description {{
                fill: #8b949e;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                    Helvetica, Arial, sans-serif;
                font-size: 13px;
            }}

            .node-background {{
                fill: #161b22;
                stroke: #30363d;
                stroke-width: 1.5;
                filter: url(#soft-shadow);
            }}

            .number-background {{
                fill: #161b22;
                stroke: #30363d;
            }}

            .node-number {{
                fill: #f0f6fc;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 12px;
                font-weight: 700;
            }}

            .node-title {{
                fill: #f0f6fc;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                    Helvetica, Arial, sans-serif;
                font-size: 15px;
                font-weight: 700;
            }}

            .node-subtitle {{
                fill: #8b949e;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                    Helvetica, Arial, sans-serif;
                font-size: 11px;
            }}

            .connection {{
                fill: none;
                stroke: #484f58;
                stroke-width: 3;
                stroke-linecap: round;
                marker-end: url(#arrow);
            }}

            .moving-particle {{
                fill: #7ee787;
                filter: url(#green-glow);
            }}

            .status {{
                fill: #7ee787;
                font-family: Consolas, Monaco, "Courier New", monospace;
                font-size: 13px;
            }}

            .cursor {{
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
        x="1"
        y="1"
        width="{WIDTH - 2}"
        height="{HEIGHT - 2}"
        rx="14"
        class="outer-background"
    />

    <!-- Terminal controls -->
    <circle cx="28" cy="26" r="7" fill="#ff5f56" />
    <circle cx="51" cy="26" r="7" fill="#ffbd2e" />
    <circle cx="74" cy="26" r="7" fill="#27c93f" />

    <text
        x="100"
        y="31"
        class="terminal-title"
    >
        gurusaran@github: ~/data-ai-pipeline
    </text>

    <line
        x1="18"
        y1="49"
        x2="{WIDTH - 18}"
        y2="49"
        stroke="#30363d"
    />

    <text
        x="40"
        y="79"
        class="main-title"
    >
        Data to Decision Pipeline
    </text>

    <text
        x="40"
        y="98"
        class="description"
    >
        Building production-ready analytics and machine-learning products
    </text>

    <!-- Connection paths -->
    <path d="M220 141 H320" class="connection" />
    <path d="M500 141 H600" class="connection" />
    <path d="M690 177 V255" class="connection" />
    <path d="M600 291 H500" class="connection" />
    <path d="M320 291 H220" class="connection" />

    <!-- Moving data particles -->
    <circle r="5" class="moving-particle">
        <animateMotion
            dur="2.2s"
            begin="0s"
            repeatCount="indefinite"
        >
            <mpath href="#path-1" />
        </animateMotion>
    </circle>

    <circle r="5" class="moving-particle">
        <animateMotion
            dur="2.2s"
            begin="0.7s"
            repeatCount="indefinite"
        >
            <mpath href="#path-2" />
        </animateMotion>
    </circle>

    <circle r="5" class="moving-particle">
        <animateMotion
            dur="2.2s"
            begin="1.4s"
            repeatCount="indefinite"
        >
            <mpath href="#path-3" />
        </animateMotion>
    </circle>

    <circle r="5" class="moving-particle">
        <animateMotion
            dur="2.2s"
            begin="2.1s"
            repeatCount="indefinite"
        >
            <mpath href="#path-4" />
        </animateMotion>
    </circle>

    <circle r="5" class="moving-particle">
        <animateMotion
            dur="2.2s"
            begin="2.8s"
            repeatCount="indefinite"
        >
            <mpath href="#path-5" />
        </animateMotion>
    </circle>

    {nodes_svg}

    <text
        x="40"
        y="390"
        class="status"
    >
        $ pipeline_status: operational
        <tspan class="cursor">_</tspan>
    </text>

    <text
        x="40"
        y="412"
        class="description"
    >
        Python · SQL · Power BI · Machine Learning · FastAPI · Streamlit
    </text>
</svg>
"""


def main() -> None:
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        create_svg(),
        encoding="utf-8",
    )

    print("Animated Data and AI pipeline created successfully.")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()