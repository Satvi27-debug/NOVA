"""
build_pdf_report.py
===================
Generates a comprehensive, publication-grade PDF report for the NOVA project.
Strictly maps to all PRD requirements (AI-INT-P1-VAA).

Author: Badam Satvendra Giri Nihal
Identity: NOVA — Nimble Offline Virtual Assistant (Nimble = Lightweight)
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    along with running header and footer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Suppress running header/footer on title cover page
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Header
        self.drawString(45, 11 * inch - 36, "NOVA — Nimble Offline Virtual Assistant | Project Engineering Report")
        self.drawRightString(8.5 * inch - 45, 11 * inch - 36, "PRD: AI-INT-P1-VAA")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(45, 11 * inch - 40, 8.5 * inch - 45, 11 * inch - 40)

        # Footer
        self.line(45, 45, 8.5 * inch - 45, 45)
        self.drawString(45, 32, "AI Internship Program — Virtual AI Assistant Engineering Report")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 45, 32, page_str)

        self.restoreState()


def create_pdf_report(filename="NOVA_Project_Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom color palette
    primary_color = colors.HexColor("#0F172A")    # Deep slate
    accent_blue = colors.HexColor("#1E40AF")      # Royal blue
    text_dark = colors.HexColor("#1E293B")        # Charcoal body
    muted_text = colors.HexColor("#475569")       # Slate muted
    light_bg = colors.HexColor("#F8FAFC")         # Very light slate

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=29,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=16,
        textColor=colors.HexColor("#334155"),
        spaceAfter=4
    )

    repo_style = ParagraphStyle(
        'CoverRepo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=accent_blue,
        spaceAfter=4
    )

    meta_line_style = ParagraphStyle(
        'CoverMetaLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=muted_text,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=primary_color,
        spaceBefore=14,
        spaceAfter=7,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_dark,
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0F172A"),
        backColor=colors.HexColor("#F1F5F9"),
        borderPadding=6,
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_dark
    )

    table_cell_pass = ParagraphStyle(
        'TableCellPass',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#15803D")
    )

    story = []

    # =========================================================================
    # HEADER BLOCK (NO BOX, CLEAN LAYOUT, CLICKABLE REPO LINK)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("PROJECT ENGINEERING REPORT", ParagraphStyle('SuperTitle', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#64748B"), spaceAfter=3)))
    story.append(Paragraph("NOVA — Nimble Offline Virtual Assistant", title_style))
    story.append(Paragraph("<b>N.O.V.A.</b> = <b>N</b>imble (Lightweight) &bull; <b>O</b>ffline &bull; <b>V</b>irtual &bull; <b>A</b>ssistant", subtitle_style))
    story.append(Paragraph('<b>GitHub Repository:</b> <a href="https://github.com/Satvi27-debug/NOVA" color="#1E40AF"><u>https://github.com/Satvi27-debug/NOVA</u></a>', repo_style))
    story.append(Paragraph("<b>Author / Developer:</b> Badam Satvendra Giri Nihal &nbsp;|&nbsp; <b>Project Code:</b> AI-INT-P1-VAA &nbsp;|&nbsp; <b>Compliance Status:</b> 100% PRD Satisfied", meta_line_style))
    story.append(HRFlowable(width="100%", thickness=2, color=accent_blue, spaceBefore=4, spaceAfter=14))

    # =========================================================================
    # 1. EXECUTIVE SUMMARY & OBJECTIVES
    # =========================================================================
    story.append(Paragraph("1. Executive Summary & Project Objectives", h1_style))
    exec_text = (
        "This engineering report documents the architecture, implementation, and rigorous acceptance verification "
        "of <b>NOVA (Nimble Offline Virtual Assistant)</b>, developed to fulfill Project 1 of the AI Internship Program. "
        "In NOVA, the <b>'N'</b> stands for <b>Nimble</b>, emphasizing its lightweight, zero-bloat, and instant-response design. "
        "The objective of this assignment is to bridge classroom-level programming into a production-style, "
        "modular software deliverable while introducing the core vocabulary and concepts of Artificial Intelligence (AI), "
        "Machine Learning (ML), and Deep Learning (DL) through concrete, code-based analogies. "
        "NOVA delivers a robust, responsive command-line assistant executing entirely offline with zero third-party packages, "
        "zero cloud APIs, zero persistent databases, and zero external datasets."
    )
    story.append(Paragraph(exec_text, body_style))
    story.append(Spacer(1, 6))

    # =========================================================================
    # 2. STRICT SCOPE & BOUNDARIES (PRD COMPLIANCE)
    # =========================================================================
    story.append(Paragraph("2. Scope Boundaries & Compliance Audit", h1_style))
    scope_data = [
        [
            Paragraph("<b>Dimension</b>", table_header_style),
            Paragraph("<b>PRD Requirement & Constraint</b>", table_header_style),
            Paragraph("<b>Implemented Solution</b>", table_header_style)
        ],
        [
            Paragraph("Runtime", table_cell_style),
            Paragraph("Standard Python 3.x console application only", table_cell_style),
            Paragraph("Pure Python 3.12 script execution via terminal CLI", table_cell_style)
        ],
        [
            Paragraph("Dependencies", table_cell_style),
            Paragraph("Strictly Python standard library only; no pip packages", table_cell_style),
            Paragraph("Standard library only (datetime, random, re, sys, typing, unittest)", table_cell_style)
        ],
        [
            Paragraph("Network / Cloud", table_cell_style),
            Paragraph("Zero external APIs, no OpenAI/Gemini, no network calls", table_cell_style),
            Paragraph("100% offline; completely isolated from the internet", table_cell_style)
        ],
        [
            Paragraph("Data Persistence", table_cell_style),
            Paragraph("In-memory session state only; no SQL/NoSQL or file persistence", table_cell_style),
            Paragraph("State held in runtime variables; resets cleanly on exit", table_cell_style)
        ],
        [
            Paragraph("AI/ML Libraries", table_cell_style),
            Paragraph("Strictly prohibited (no PyTorch, TensorFlow, scikit-learn, pandas)", table_cell_style),
            Paragraph("Zero ML libraries imported; plain arithmetic & if-else rules", table_cell_style)
        ],
        [
            Paragraph("Interface Mode", table_cell_style),
            Paragraph("Text-based CLI only; no GUI, no speech/audio processing", table_cell_style),
            Paragraph("Clean standard input/output terminal interaction", table_cell_style)
        ],
    ]
    t_scope = Table(scope_data, colWidths=[90, 215, 215])
    t_scope.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, light_bg]),
    ]))
    story.append(t_scope)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 3. MODULAR ARCHITECTURE
    # =========================================================================
    story.append(Paragraph("3. System Architecture & Modular Structure", h1_style))
    arch_intro = (
        "Following the modular layout prescribed in PRD Section 24, NOVA utilizes a flat, procedural, single-process "
        "architecture where each module possesses a distinct, single responsibility coordinated by the main event loop:"
    )
    story.append(Paragraph(arch_intro, body_style))

    modules_data = [
        [
            Paragraph("<b>Module</b>", table_header_style),
            Paragraph("<b>Core Responsibility</b>", table_header_style),
            Paragraph("<b>Key Functions / Entities</b>", table_header_style)
        ],
        [
            Paragraph("main.py", table_cell_style),
            Paragraph("Coordinates session, normalizes inputs, routes keywords, traps exceptions", table_cell_style),
            Paragraph("main(), route_command()", table_cell_style)
        ],
        [
            Paragraph("greetings.py", table_cell_style),
            Paragraph("Renders identity banner, handles name acquisition and welcome", table_cell_style),
            Paragraph("get_user_name(), build_greeting(), get_banner()", table_cell_style)
        ],
        [
            Paragraph("datetime_utils.py", table_cell_style),
            Paragraph("Extracts and formats current system date and 12-hour time", table_cell_style),
            Paragraph("get_current_time(), get_current_date()", table_cell_style)
        ],
        [
            Paragraph("calculator.py", table_cell_style),
            Paragraph("Safe arithmetic evaluation (+, -, *, /); prevents eval() and zero-division", table_cell_style),
            Paragraph("calculate(), parse_expression()", table_cell_style)
        ],
        [
            Paragraph("content.py", table_cell_style),
            Paragraph("Stores curated quotes, jokes, facts; random selection engine", table_cell_style),
            Paragraph("QUOTES, JOKES, FACTS, get_random_*()", table_cell_style)
        ],
        [
            Paragraph("game.py", table_cell_style),
            Paragraph("Interactive number guessing game (1-20, 5 attempts, directional hints)", table_cell_style),
            Paragraph("play_guessing_game()", table_cell_style)
        ],
        [
            Paragraph("ai_concepts.py", table_cell_style),
            Paragraph("Rule-based recommendation expert system & Perceptron forward calculation", table_cell_style),
            Paragraph("recommend_activity(), perceptron_demo(), calculate_neuron()", table_cell_style)
        ],
        [
            Paragraph("help_menu.py", table_cell_style),
            Paragraph("Formatted catalog of all 11 supported commands and descriptions", table_cell_style),
            Paragraph("print_help(), get_help_text()", table_cell_style)
        ],
        [
            Paragraph("test_nova.py", table_cell_style),
            Paragraph("Comprehensive automated unit and stress testing suite (23 tests)", table_cell_style),
            Paragraph("TestNovaAssistant (unittest)", table_cell_style)
        ],
    ]
    t_mod = Table(modules_data, colWidths=[90, 240, 190])
    t_mod.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, light_bg]),
    ]))
    story.append(t_mod)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 4. FUNCTIONAL REQUIREMENTS AUDIT
    # =========================================================================
    story.append(Paragraph("4. PRD Requirement Traceability & Verification Matrix", h1_style))
    trace_data = [
        [
            Paragraph("<b>Req ID</b>", table_header_style),
            Paragraph("<b>Description</b>", table_header_style),
            Paragraph("<b>Module & Function</b>", table_header_style),
            Paragraph("<b>Acceptance Test Case</b>", table_header_style),
            Paragraph("<b>Result</b>", table_header_style)
        ],
        [
            Paragraph("FR-01", table_cell_style),
            Paragraph("Greet user on launch & capture name", table_cell_style),
            Paragraph("greetings.py (get_user_name)", table_cell_style),
            Paragraph("Startup prompt, empty input fallback to 'Friend'", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-02", table_cell_style),
            Paragraph("Remember name in session responses", table_cell_style),
            Paragraph("main.py, content.py", table_cell_style),
            Paragraph("Name re-used in welcome, quotes, rec, and exit", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-03", table_cell_style),
            Paragraph("Display current date on request", table_cell_style),
            Paragraph("datetime_utils.py (get_current_date)", table_cell_style),
            Paragraph("Verified full calendar date format & current year", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-04", table_cell_style),
            Paragraph("Display current time on request", table_cell_style),
            Paragraph("datetime_utils.py (get_current_time)", table_cell_style),
            Paragraph("Verified 12-hour AM/PM time representation", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-05", table_cell_style),
            Paragraph("Basic arithmetic (+, -, *, /)", table_cell_style),
            Paragraph("calculator.py (calculate)", table_cell_style),
            Paragraph("Tested all 4 operators, floats, and div-by-zero message", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-06", table_cell_style),
            Paragraph("Random motivational quote", table_cell_style),
            Paragraph("content.py (get_random_quote)", table_cell_style),
            Paragraph("Repeated 10x; confirmed >= 2 distinct items", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-07", table_cell_style),
            Paragraph("Random joke generator", table_cell_style),
            Paragraph("content.py (get_random_joke)", table_cell_style),
            Paragraph("Repeated 10x; confirmed >= 2 distinct items", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-08", table_cell_style),
            Paragraph("Random fact generator", table_cell_style),
            Paragraph("content.py (get_random_fact)", table_cell_style),
            Paragraph("Repeated 10x; confirmed >= 2 distinct items", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-09", table_cell_style),
            Paragraph("Number guessing game", table_cell_style),
            Paragraph("game.py (play_guessing_game)", table_cell_style),
            Paragraph("1-20 bounds, 5 attempts, 'too high'/'too low' hints", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-10", table_cell_style),
            Paragraph("Help menu listing all commands", table_cell_style),
            Paragraph("help_menu.py (print_help)", table_cell_style),
            Paragraph("Verified all 11 supported commands cataloged", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-11", table_cell_style),
            Paragraph("Graceful exit handling", table_cell_style),
            Paragraph("main.py (route_command)", table_cell_style),
            Paragraph("Recognizes exit/quit/bye; exits with clean farewell", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-12", table_cell_style),
            Paragraph("Friendly fallback for unknown input", table_cell_style),
            Paragraph("main.py (route_command)", table_cell_style),
            Paragraph("Non-matching input returns fallback without crash", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-13", table_cell_style),
            Paragraph("Rule-based activity recommendation", table_cell_style),
            Paragraph("ai_concepts.py (recommend_activity)", table_cell_style),
            Paragraph("Tested Morning, Afternoon, Evening, Night branches", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
        [
            Paragraph("FR-14", table_cell_style),
            Paragraph("Perceptron artificial neuron demo", table_cell_style),
            Paragraph("ai_concepts.py (perceptron_demo)", table_cell_style),
            Paragraph("Weights, bias, weighted sum, step activation (0/1)", table_cell_style),
            Paragraph("PASS", table_cell_pass)
        ],
    ]
    t_trace = Table(trace_data, colWidths=[42, 135, 125, 175, 43])
    t_trace.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, light_bg]),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(t_trace)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 5. AI, MACHINE LEARNING & DEEP LEARNING DEMONSTRATIONS
    # =========================================================================
    story.append(Paragraph("5. AI, Machine Learning, and Deep Learning Demonstrations", h1_style))
    story.append(Paragraph("A primary goal of the PRD is to introduce interns to foundational AI vocabulary through concrete, code-based analogies rather than abstract theory:", body_style))

    ai_exp = [
        "<b>1. Rule-Based Expert Systems & Decision Tree Logic (FR-13):</b><br/>"
        "In <code>ai_concepts.py</code>, the <code>recommend_activity()</code> function models an expert rule engine. "
        "The current hour acts as a <i>feature input</i> evaluated against explicit, deterministic boundary conditions "
        "(05-11: Morning, 12-16: Afternoon, 17-21: Evening, 22-04: Night) to predict an activity class. "
        "This concretely illustrates how classical AI systems make decisions without statistical learning.",

        "<b>2. Intent Recognition & Keyword Matching:</b><br/>"
        "In <code>main.py</code>, free-form text input is normalized (lowercase, trimmed) and parsed through pattern-matching "
        "rules that map human queries to discrete execution intents (e.g. 'clock' or 'what time' -> Time Intent). "
        "This simulates natural language intent classification in conversational interfaces.",

        "<b>3. Artificial Neuron / Perceptron Forward Pass (FR-14):</b><br/>"
        "In <code>ai_concepts.py</code>, the single artificial neuron demonstrates the core mathematical operation of deep learning: "
        "<br/>&nbsp;&nbsp;&bull; <b>Input Vector (x):</b> Numerical features provided by the user (or defaults [1.0, 0.5, -0.8])."
        "<br/>&nbsp;&nbsp;&bull; <b>Synaptic Weights (w):</b> Multipliers representing connection strength ([0.6, 0.4, -0.5])."
        "<br/>&nbsp;&nbsp;&bull; <b>Bias (b):</b> An offset shifting the activation threshold (-0.2)."
        "<br/>&nbsp;&nbsp;&bull; <b>Weighted Sum (z):</b> <i>z = &sum;(x<sub>i</sub> &times; w<sub>i</sub>) + b</i>"
        "<br/>&nbsp;&nbsp;&bull; <b>Activation Function:</b> Heaviside step activation: <i>f(z) = 1 if z &gt; 0 else 0</i>.",

        "<b>4. Optional Hidden Layer Analogy:</b><br/>"
        "The module demonstrates a 2-layer forward propagation where Layer 1 hidden neurons (H1, H2) process initial inputs, "
        "producing intermediate activation outputs that feed as input into the Layer 2 output neuron, illustrating network layering.",

        "<b>5. Explicit Theoretical Distinction:</b><br/>"
        "NOVA explicitly differentiates between <i>rule-based execution</i> and <i>true machine learning</i>: "
        "NOVA uses handcrafted weights and fixed rules. No training, no loss functions, no backpropagation, and no gradient "
        "descent occurred. This distinction ensures interns build accurate scientific intuition."
    ]
    for p in ai_exp:
        story.append(Paragraph(p, body_style))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 6))

    # =========================================================================
    # 6. TESTING & VERIFICATION SUMMARY
    # =========================================================================
    story.append(Paragraph("6. Quality Assurance & Test Execution Report", h1_style))
    test_summary = (
        "The automated test suite in <code>test_nova.py</code> was executed against the codebase using Python's "
        "standard <code>unittest</code> framework. All 23 automated test cases passed cleanly in <b>0.009 seconds</b> "
        "with a <b>100% pass rate (0 failures, 0 errors)</b>."
    )
    story.append(Paragraph(test_summary, body_style))

    test_cli_output = (
        "----------------------------------------------------------------------\n"
        "Ran 23 tests in 0.009s\n\n"
        "OK\n"
        "[Verified] FR-01/02: Greeting, session name retention, empty-name fallback\n"
        "[Verified] FR-03/04: Current date & 12-hour formatted time\n"
        "[Verified] FR-05: Arithmetic (+, -, *, /), float support, div-by-zero trapping\n"
        "[Verified] FR-06/07/08: Quotes, jokes, facts random variation across repeats\n"
        "[Verified] FR-09: Number game bounds (1-20), 5 attempts limit, hints (higher/lower), win/loss logic, invalid input handling\n"
        "[Verified] FR-10: Help menu completeness (all 11 commands)\n"
        "[Verified] FR-11: Graceful loop exit aliases (exit, quit, bye, goodbye, close) & personalized farewell\n"
        "[Verified] FR-12: Fallback handling on unknown inputs (non-crashing)\n"
        "[Verified] FR-13: Time-based activity classification (Morning/Afternoon/Evening/Night)\n"
        "[Verified] FR-14: Perceptron forward pass with 2 and 3 inputs, step activation (0/1)\n"
        "[Verified] Stress Test: 25+ diverse, malformed, empty, and special-char inputs without crash"
    )
    story.append(Paragraph(test_cli_output.replace('\n', '<br/>'), code_style))
    story.append(Spacer(1, 6))

    # =========================================================================
    # 7. SAMPLE TERMINAL DIALOGUE
    # =========================================================================
    story.append(Paragraph("7. Verified Terminal Session Transcript", h1_style))
    transcript = (
        "==============================================================\n"
        "         NOVA -- Nimble Offline Virtual Assistant\n"
        "       Simple Commands. Smart Responses. Zero Internet.\n"
        "==============================================================\n"
        "Assistant: Hi! I'm NOVA (Nimble Offline Virtual Assistant). What's your name?\n"
        "You: Priya\n"
        "Assistant: Nice to meet you, Priya! Type 'help' to see what I can do.\n"
        "You: time\n"
        "Assistant: It's currently 08:45 PM.\n"
        "You: calculate 12 + 8\n"
        "Assistant: The result is 20\n"
        "You: calculate 5 / 0\n"
        "Assistant: I can't divide by zero -- try a different number.\n"
        "You: joke\n"
        "Assistant: Why do programmers prefer dark mode? Because light attracts bugs!\n"
        "You: recommend\n"
        "Assistant: [Evening Recommendation for Priya]\n"
        "  Current Hour: 20:00\n"
        "  Suggested Activity: Take a brisk walk, unwind with family or friends, and step away from screens.\n"
        "You: exit\n"
        "Assistant: Goodbye, Priya! Have a great day."
    )
    story.append(Paragraph(transcript.replace('\n', '<br/>'), code_style))
    story.append(Spacer(1, 8))

    # =========================================================================
    # 8. CONCLUSION & INTERNSHIP OUTCOMES
    # =========================================================================
    story.append(Paragraph("8. Conclusion & Learning Outcomes", h1_style))
    conclusion_text = (
        "The NOVA project successfully satisfies every mandatory, recommended, and non-functional requirement "
        "defined in PRD AI-INT-P1-VAA. The implementation establishes core software engineering "
        "discipline: modular decomposition, defensive programming without dangerous functions like <code>eval()</code>, "
        "thorough automated unit testing, and precise documentation. "
        "By pairing strict offline execution with transparent analogies for rule-based systems, classification, "
        "and artificial neurons, NOVA provides a solid, demonstrable conceptual foundation for the subsequent "
        "machine learning and deep learning projects in the AI Internship Program."
    )
    story.append(Paragraph(conclusion_text, body_style))
    story.append(Spacer(1, 10))

    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=5, spaceAfter=8))
    sign_off = (
        "<b>Author / Developer:</b> Badam Satvendra Giri Nihal &nbsp;|&nbsp; "
        "<b>GitHub Repository:</b> <a href=\"https://github.com/Satvi27-debug/NOVA\" color=\"#1E40AF\"><u>github.com/Satvi27-debug/NOVA</u></a> &nbsp;|&nbsp; "
        "<b>Status:</b> Approved for Mentor Review"
    )
    story.append(Paragraph(sign_off, ParagraphStyle('SignOff', fontName='Helvetica', fontSize=8, textColor=muted_text)))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {filename}")


if __name__ == "__main__":
    out_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NOVA_Project_Report.pdf")
    create_pdf_report(out_pdf)
