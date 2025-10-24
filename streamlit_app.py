import csv
import re
from datetime import datetime
from pathlib import Path

import streamlit as st


def configure_page() -> None:
    st.set_page_config(
        page_title="ContentForge – AI-Powered Content Creation Agency",
        page_icon="🖋️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def inject_css() -> None:
    st.markdown(
        """
        <style>
          :root {
            --primary: #6c5ce7;
            --primary-dark: #5a4bd6;
            --bg-hero-start: #0f1226;
            --bg-hero-end: #1b1f3a;
            --text-strong: #0f1226;
            --muted: #6b7280;
            --card: #ffffff;
            --success: #10b981;
          }

          .app-header { 
            position: sticky; top: 0; z-index: 999;
            background: rgba(255,255,255,0.75);
            backdrop-filter: saturate(180%) blur(10px);
            border-bottom: 1px solid rgba(0,0,0,0.06);
            padding: 0.5rem 0.25rem; margin-bottom: 0.5rem;
          }

          .brand { font-weight: 800; letter-spacing: 0.2px; }
          .nav a { text-decoration: none; color: var(--text-strong); margin-left: 1rem; }
          .nav a:hover { color: var(--primary); }

          .hero {
            border-radius: 18px;
            padding: 3.2rem 2.2rem;
            background: linear-gradient(135deg, var(--bg-hero-start), var(--bg-hero-end));
            color: #eef2ff;
            border: 1px solid rgba(255,255,255,0.08);
          }

          .hero h1 { font-size: 2.4rem; line-height: 1.2; margin: 0 0 0.6rem 0; }
          .hero p  { font-size: 1.1rem; color: #c7ccff; }
          .hero .ctas { margin-top: 1.2rem; }
          .cta-primary { 
            background: var(--primary); color: white; padding: 0.7rem 1.1rem; 
            border-radius: 10px; display: inline-block; margin-right: 0.6rem;
          }
          .cta-primary:hover { background: var(--primary-dark); color: #fff; }
          .cta-secondary { 
            background: transparent; color: #eef2ff; padding: 0.7rem 1.1rem; 
            border: 1px solid rgba(255,255,255,0.18); border-radius: 10px; display: inline-block;
          }
          .cta-secondary:hover { border-color: #fff; color: #fff; }

          .card {
            background: var(--card);
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 14px;
            padding: 1.25rem;
            height: 100%;
          }

          .pricing .tier { border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 1.25rem; background: #fff; }
          .pricing .price { font-size: 2rem; font-weight: 800; }
          .pricing .badge { font-size: 0.75rem; color: #6b7280; }

          .muted { color: var(--muted); }

          /* Hide Streamlit default header/footer */
          header[data-testid="stHeader"] { visibility: hidden; height: 0; }
          footer { visibility: hidden; height: 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    with st.container():
        st.markdown('<div class="app-header">', unsafe_allow_html=True)
        left_col, right_col = st.columns([1, 2])
        with left_col:
            st.markdown(
                "<div class='brand'>🖋️ ContentForge</div>",
                unsafe_allow_html=True,
            )
        with right_col:
            st.markdown(
                """
                <div class="nav" style="text-align:right;">
                  <a href="#features">Features</a>
                  <a href="#pricing">Pricing</a>
                  <a href="#testimonials">Testimonials</a>
                  <a href="#faq">FAQ</a>
                  <a href="#contact">Get a demo</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


def render_hero() -> None:
    with st.container():
        st.markdown('<a id="top"></a>', unsafe_allow_html=True)
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        left_col, right_col = st.columns([1.2, 1])
        with left_col:
            st.markdown(
                "<h1>Create content that converts, at scale.</h1>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p>ContentForge blends expert workflows with AI to plan, draft, and optimize articles, social posts, and landing pages that rank and drive revenue.</p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                """
                <div class="ctas">
                  <a class="cta-primary" href="#contact">Get a personalized demo</a>
                  <a class="cta-secondary" href="#pricing">See pricing</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption("Trusted by growth teams, agencies, and B2B startups")
        with right_col:
            st.metric("Avg. time to publish", "3.2 days", "-58%")
            st.metric("Avg. SEO uplift", "+38%", "+12 pts")
            st.metric("Content throughput", "5x", "+400%")
        st.markdown("</div>", unsafe_allow_html=True)


def render_features() -> None:
    st.markdown('<a id="features"></a>', unsafe_allow_html=True)
    st.subheader("Why teams choose ContentForge")
    st.caption("Everything you need to run a modern content operation")
    row1 = st.columns(3)
    with row1[0]:
        st.markdown("### 🧭 Strategy co-pilot")
        st.markdown(
            "Generate data-backed content calendars from ICP, keywords, and goals."
        )
        st.markdown("- Clustered keywords and SERP insights")
        st.markdown("- Gap and opportunity analysis")
    with row1[1]:
        st.markdown("### ✍️ Drafts that sound on-brand")
        st.markdown(
            "Brief-to-publish workflows with tone, structure, and SME inputs."
        )
        st.markdown("- Brand voice and style guardrails")
        st.markdown("- Multi-step human-in-the-loop editing")
    with row1[2]:
        st.markdown("### 🚀 SEO + distribution built-in")
        st.markdown(
            "Optimize for search and ship across channels in one click."
        )
        st.markdown("- On-page SEO and internal linking")
        st.markdown("- Auto-snippets for social and email")

    st.divider()


def render_pricing() -> None:
    st.markdown('<a id="pricing"></a>', unsafe_allow_html=True)
    st.subheader("Transparent pricing that scales with you")
    st.caption("Switch plans anytime. Annual billing saves 15%.")

    col_basic, col_growth, col_scale = st.columns([1, 1.1, 1])

    with col_basic:
        st.markdown("#### Starter")
        st.markdown("<div class='pricing tier'>", unsafe_allow_html=True)
        st.markdown("<div class='price'>$149<span class='badge'>/mo</span></div>", unsafe_allow_html=True)
        st.markdown("- 8 long-form pieces / month")
        st.markdown("- 1 brand voice profile")
        st.markdown("- Brief → draft workflow")
        st.markdown("- Basic SEO checks")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_growth:
        st.markdown("#### Growth 🚀")
        st.markdown("<div class='pricing tier'>", unsafe_allow_html=True)
        st.markdown("<div class='price'>$399<span class='badge'>/mo</span></div>", unsafe_allow_html=True)
        st.markdown("- 25 long-form pieces / month")
        st.markdown("- 3 brand voice profiles")
        st.markdown("- SEO optimizer + internal links")
        st.markdown("- Social + email auto-snippets")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_scale:
        st.markdown("#### Scale")
        st.markdown("<div class='pricing tier'>", unsafe_allow_html=True)
        st.markdown("<div class='price'>$999<span class='badge'>/mo</span></div>", unsafe_allow_html=True)
        st.markdown("- Unlimited drafts")
        st.markdown("- Dedicated strategist")
        st.markdown("- Advanced workflows & SSO")
        st.markdown("- Priority support")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<p class='muted'>Need a custom plan or enterprise security? <a href='#contact'>Talk to us →</a></p>",
        unsafe_allow_html=True,
    )


def render_testimonials() -> None:
    st.markdown('<a id="testimonials"></a>', unsafe_allow_html=True)
    st.subheader("What customers say")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='card'>
              <p>“We 4x'd output and maintained quality. SEO results showed up fast.”</p>
              <p class='muted'>— Maya L., Head of Content, B2B SaaS</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card'>
              <p>“Brief-to-publish workflow finally aligned our SMEs and writers.”</p>
              <p class='muted'>— Erik P., Marketing Director</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='card'>
              <p>“Distribution snippets are a game-changer for our lean team.”</p>
              <p class='muted'>— Dana R., Growth Lead</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_faq() -> None:
    st.markdown('<a id="faq"></a>', unsafe_allow_html=True)
    st.subheader("FAQ")
    with st.expander("How is this different from using a generic AI writer?"):
        st.write(
            "ContentForge combines expert playbooks with AI and human-in-the-loop review to preserve brand voice and accuracy."
        )
    with st.expander("Do you offer human editing?"):
        st.write(
            "Yes. Our workflows are designed for SMEs and editors to review drafts before publishing."
        )
    with st.expander("What CMSes do you support?"):
        st.write("Native exports for Webflow, WordPress, Notion; others via Markdown/HTML.")
    with st.expander("Can you work with our existing content calendar?"):
        st.write("Absolutely. Import CSV/Sheets or build a fresh plan with our co-pilot.")


def validate_email(email: str) -> bool:
    if not email:
        return False
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))


def save_lead_to_csv(row: dict) -> None:
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "leads.csv"
    file_exists = csv_path.exists()
    field_names = [
        "timestamp_iso",
        "name",
        "email",
        "company",
        "role",
        "budget",
        "interest",
        "message",
    ]
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def render_contact_form() -> None:
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.subheader("Get a personalized demo")
    st.caption("Tell us about your goals and we'll tailor a walkthrough.")

    with st.form("lead_form", clear_on_submit=True):
        name = st.text_input("Full name")
        email = st.text_input("Work email")
        cols = st.columns(2)
        with cols[0]:
            company = st.text_input("Company")
        with cols[1]:
            role = st.text_input("Role")

        budget = st.selectbox(
            "Monthly content budget",
            ["<$2k", "$2k–$5k", "$5k–$15k", ">$15k", "Not sure"],
        )
        interest = st.multiselect(
            "What are you interested in?",
            [
                "Content strategy",
                "SEO articles",
                "Product marketing",
                "Thought leadership",
                "Social + email snippets",
            ],
        )
        message = st.text_area("Anything else we should know?", height=120)

        submit = st.form_submit_button("Request demo")
        if submit:
            errors = []
            if len(name.strip()) < 2:
                errors.append("Enter your full name.")
            if not validate_email(email):
                errors.append("Enter a valid work email.")
            if errors:
                st.error("\n".join(errors))
            else:
                lead_row = {
                    "timestamp_iso": datetime.utcnow().isoformat(),
                    "name": name.strip(),
                    "email": email.strip(),
                    "company": company.strip(),
                    "role": role.strip(),
                    "budget": budget,
                    "interest": ", ".join(interest),
                    "message": message.strip(),
                }
                try:
                    save_lead_to_csv(lead_row)
                except Exception as exc:  # Non-fatal reporting to user
                    st.error(f"Could not save your request. Please try again. ({exc})")
                else:
                    st.success("Thanks! We'll reach out within 1 business day.")
                    st.balloons()


def main() -> None:
    configure_page()
    inject_css()
    render_header()
    render_hero()
    render_features()
    render_pricing()
    render_testimonials()
    render_faq()
    render_contact_form()


if __name__ == "__main__":
    main()
