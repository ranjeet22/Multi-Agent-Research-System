import streamlit as st
import time
from pipeline import run_research_pipeline

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Multi Agent Research System",
    page_icon="🔬",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 2rem;
}

.agent-box {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}

.step-complete {
    color: #22c55e;
    font-weight: 600;
}

.step-running {
    color: #38bdf8;
    font-weight: 600;
}

.report-box {
    background: #111827;
    border-radius: 16px;
    padding: 20px;
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='title'>🔬 Multi Agent Research System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Powered by Tavily • BeautifulSoup • Gemini • LangChain</div>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Query Input
# -----------------------------
query = st.text_input(
    "Research Topic",
    placeholder="e.g. Impact of AI on Healthcare"
)

# -----------------------------
# Button
# -----------------------------
if st.button("🚀 Start Research", use_container_width=True):

    if not query.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    pipeline_placeholder = st.empty()

    with pipeline_placeholder.container():

        st.subheader("⚙️ Pipeline Execution")

        search_status = st.empty()
        reader_status = st.empty()
        writer_status = st.empty()
        critic_status = st.empty()

        search_status.markdown(
            "<div class='agent-box'><span class='step-running'>🔍 Search Agent Running...</span></div>",
            unsafe_allow_html=True
        )

        time.sleep(1)

        reader_status.markdown(
            "<div class='agent-box'><span class='step-running'>📖 Reader Agent Waiting...</span></div>",
            unsafe_allow_html=True
        )

        writer_status.markdown(
            "<div class='agent-box'><span class='step-running'>✍️ Writer Agent Waiting...</span></div>",
            unsafe_allow_html=True
        )

        critic_status.markdown(
            "<div class='agent-box'><span class='step-running'>🧐 Critic Agent Waiting...</span></div>",
            unsafe_allow_html=True
        )

    # -----------------------------
    # Run Pipeline
    # -----------------------------
    with st.spinner("Researching..."):

        result = run_research_pipeline(query)

    # Update statuses

    search_status.markdown(
        "<div class='agent-box'><span class='step-complete'>✅ Search Agent Completed</span></div>",
        unsafe_allow_html=True
    )

    reader_status.markdown(
        "<div class='agent-box'><span class='step-complete'>✅ Reader Agent Completed</span></div>",
        unsafe_allow_html=True
    )

    writer_status.markdown(
        "<div class='agent-box'><span class='step-complete'>✅ Writer Agent Completed</span></div>",
        unsafe_allow_html=True
    )

    critic_status.markdown(
        "<div class='agent-box'><span class='step-complete'>✅ Critic Agent Completed</span></div>",
        unsafe_allow_html=True
    )

    st.success("Research Pipeline Finished")

    st.divider()

    # -----------------------------
    # Report
    # -----------------------------
    with st.expander("📄 Research Report", expanded=True):

        st.markdown(
            f"""
            <div class='report-box'>
            {result['report']}
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------
    # Critic
    # -----------------------------
    with st.expander("🧐 Critic Review", expanded=True):

        st.markdown(
            f"""
            <div class='report-box'>
            {result['feedback']}
            </div>
            """,
            unsafe_allow_html=True
        )