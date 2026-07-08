import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Premium Page Configuration & Custom CSS Injection for Padding
st.set_page_config(
    page_title="The Indian Nobel Footprint | Editorial Workspace", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injecting clean whitespace adjustments via custom CSS to make columns breathe
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 5rem; }
    h1 { font-weight: 800; letter-spacing: -0.025em; }
    h2 { font-weight: 700; letter-spacing: -0.02em; margin-top: 2rem; }
    div[data-testid="stMetric"] { background-color: #F8FAFC; padding: 15px; border-radius: 10px; border: 1px solid #E2E8F0; }
    </style>
    """, unsafe_allow_html=True)

# Signature Economist Red Top Bar
st.markdown("<div style='background-color: #E5233D; height: 6px; margin-bottom: 30px;'></div>", unsafe_allow_html=True)

# Master Header Area (Spacious & Clean)
st.title("🇮🇳 The Indian Nobel Footprint")
st.markdown(
    """
    <p style='font-size: 1.2rem; color: #475569; max-width: 900px; line-height: 1.6;'>
    An editorial exploration mapping the historical timelines, research fields, and shifting citizenship 
    dynamics of Nobel Laureates from the Indian subcontinent and its global diaspora.
    </p>
    """, unsafe_allow_html=True
)
st.write("") # Whitespace buffer

# 2. Secure Data Loading
df = pd.read_excel("nobel_data.xlsx")

# Asset Repositories
photos = {
    "Rabindranath Tagore": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Rabindranath_Tagore_in_1909.jpg/400px-Rabindranath_Tagore_in_1909.jpg",
    "C. V. Raman": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Sir_CV_Raman.JPG/400px-Sir_CV_Raman.JPG",
    "Har Gobind Khorana": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Har_Gobind_Khorana.jpg/400px-Har_Gobind_Khorana.jpg",
    "Mother Teresa": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Mother_Teresa_1986.jpg/400px-Mother_Teresa_1986.jpg",
    "Subrahmanyan Chandrasekhar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Subrahmanyan_Chandrasekhar.jpg/400px-Subrahmanyan_Chandrasekhar.jpg",
    "Amartya Sen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Amartya_Sen_HD2015.jpg/400px-Amartya_Sen_HD2015.jpg",
    "V. S. Naipaul": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/V._S._Naipaul_2011_Shusha.jpg/400px-V._S._Naipaul_2011_Shusha.jpg",
    "Venkatraman Ramakrishnan": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Venkatraman_Ramakrishnan_LF.jpg/400px-Venkatraman_Ramakrishnan_LF.jpg",
    "Kailash Satyarthi": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Kailash_Satyarthi_2015_%28cropped%29.jpg/400px-Kailash_Satyarthi_2015_%28cropped%29.jpg",
    "Abhijit Banerjee": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Abhijit_Banerjee_at_MIT.jpg/400px-Abhijit_Banerjee_at_MIT.jpg"
}

biographies = {
    "Rabindranath Tagore": "The first non-European laureate in Literature (1913). Awarded for his profoundly sensitive, fresh, and beautiful verse in Gitanjali, establishing Indian literary traditions on the global stage.",
    "C. V. Raman": "Awarded for his groundbreaking work on the scattering of light and the discovery of the Raman Effect (1930), single-handedly placing India on the map of modern quantum physics.",
    "Har Gobind Khorana": "Awarded for his interpretation of the genetic code and its function in protein synthesis (1968), laying the absolute groundwork for modern biochemistry and gene synthesis.",
    "Mother Teresa": "Recognized for her work in bringing help to suffering humanity (1979), founding the Missionaries of Charity in Kolkata and establishing a legacy of global humanitarian service.",
    "Subrahmanyan Chandrasekhar": "Awarded for his theoretical studies of the physical processes of importance to the structure and evolution of stars (1983), defining the astrophysical 'Chandrasekhar Limit'.",
    "Amartya Sen": "Awarded for his deep contributions to welfare economics and social choice theory (1998), structurally changing how global institutions define and measure poverty indices.",
    "V. S. Naipaul": "Awarded for having united perceptive narrative and incorruptible scrutiny in works that compel us to see the presence of suppressed histories across post-colonial landscapes (2001).",
    "Venkatraman Ramakrishnan": "Awarded for his high-resolution structural mapping of the ribosome (2009), fundamentally transforming the development of modern broad-spectrum antibiotics.",
    "Kailash Satyarthi": "Awarded for his active global struggle against the suppression of children and young people (2014), liberating over 80,000 children from institutionalized forced labor.",
    "Abhijit Banerjee": "Awarded for his experimental approach to alleviating global poverty (2019), pioneering the use of randomized controlled trials (RCTs) in development economics theories."
}


# ====================================================================
# SECTION 1: EXECUTIVE BREAKDOWN (METRICS + COHORT BALANCE)
# ====================================================================
st.header("📌 Executive Summary & Cohort Balance")
st.write("") 

# We build a 4-column layout to let the baseline statistics sit cleanly next to the Bar Balance chart
kpi_col1, kpi_col2, kpi_col3, chart_col1 = st.columns([1, 1, 1, 2], gap="large")

with kpi_col1:
    st.metric(label="Total Laureates", value=len(df))
    st.caption("Complete volume of recognized historical individuals.")

with kpi_col2:
    st.metric(label="Distinct Academic Fields", value=df['Field'].nunique())
    st.caption("Distribution across Science, Literature, Economics, & Peace.")

with kpi_col3:
    st.metric(label="Historical Timeline Scale", value="1913 — 2019")
    st.caption("Century-scale tracking of regional and diaspora output.")

with chart_col1:
    # Card 1 processing
    total_w = len(df)
    citizen_w = len(df[df['Category'] == 'Citizen'])
    diaspora_w = len(df[df['Category'] == 'Origin'])
    
    summary_df = pd.DataFrame({
        'Group': ['🇮🇳 Indian Citizens  ', '🗺️ Overseas Diaspora  '],
        'Count': [citizen_w, diaspora_w],
        'ColorGroup': ['Citizen', 'Diaspora']
    })
    
    # Beautiful, spacious horizontal pastel bar
    fig1 = px.bar(
        summary_df, 
        x='Count', 
        y='Group', 
        orientation='h', 
        text='Count',
        color='ColorGroup',
        color_discrete_map={'Citizen': '#CCEBC5', 'Diaspora': '#FBB4AE'} # Crisp pastels
    )
    fig1.update_layout(
        plot_bgcolor='white', 
        showlegend=False,
        xaxis_showgrid=False, 
        xaxis_visible=False, 
        yaxis_title=None,
        height=140, 
        margin=dict(l=10, r=30, t=5, b=5)
    )
    fig1.update_traces(textposition='outside', font=dict(size=14, currentcolor='black'))
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

# Section 1 Gist Callout Box
st.info(
    f"**Editorial Gist:** The data uncovers a perfectly balanced dual-track output. "
    f"Exactly **{citizen_w} laureates are domestic citizens** who achieved breakthroughs holding Indian passports, "
    f"balanced by **{diaspora_w} global diaspora scholars** who scaled international research systems. "
    "This highlights a balanced distribution between localized institutional output and global talent migration."
)

st.write("")
st.markdown("---")
st.write("")


# ====================================================================
# SECTION 2: THE MAIN HISTORICAL MATRIX (FULL SCREEN ROOM TO BREATHE)
# ====================================================================
st.header("🗓️ The Chronological & Academic Field Matrix")
st.markdown(
    "A wide-canvas timeline positioning every award. The horizontal layout provides full "
    "spacious clarity to trace the historical spaces between breakthroughs across different centuries."
)
st.write("")

# Giving the graph full edge-to-edge layout block space (Height boosted to 480px for luxury spacing)
fig2 = px.scatter(
    df, 
    x='Field', 
    y='Year', 
    text='Icon',
    hover_name='Name',
    custom_data=['Flag', 'Category', 'Year']
)
fig2.update_traces(
    mode='text',
    textfont=dict(size=32), # Bold expansive icons
    hovertemplate="<b>%{hovertext}</b><br>📅 Award Year: %{customdata[2]}<br>🏛️ Field: %{x}<br>📍 Status: %{customdata[0]} %{customdata[1]}<extra></extra>"
)
fig2.update_layout(
    plot_bgcolor='#F8FAFC', # High-end off-white slate background
    xaxis_showgrid=True,
    xaxis_gridcolor='#E2E8F0',
    yaxis_showgrid=True,
    yaxis_gridcolor='#E2E8F0',
    yaxis=dict(
        tickvals=[1913, 1930, 1968, 1979, 1983, 1998, 2001, 2009, 2014, 2019],
        tickfont=dict(size=13, color='#475569'),
        range=[1900, 2030] # Expansive bounds so markers don't clip the edges
    ),
    xaxis=dict(
        tickfont=dict(size=14, color='#1E293B', bold=True),
        side='top' # Place labels at the top like premium data dashboards
    ),
    height=480,
    margin=dict(l=60, r=60, t=40, b=20)
)
st.plotly_chart(fig2, use_container_width=True)

st.warning(
    "**Visual Insight:** Notice the steep 'innovation drought' between C.V. Raman (1930) and Har Gobind Khorana (1968), "
    "contrasted against the modern acceleration from 1998 onward. Hover over any floating icon marker to immediately isolate "
    "the individual's passport classification and name context."
)

st.write("")
st.markdown("---")
st.write("")


# ====================================================================
# SECTION 3: HERO DEEP-DIVE CANVAS (CLEAN INTERACTIVE ROW)
# ====================================================================
st.header("🌟 The Interactive Profile Inspector")
st.write("Isolate an individual laureate from the editorial register to pull their verified historical records and media files.")
st.write("")

selected_hero = st.selectbox("Select a Laureate to inspect:", df['Name'].unique(), label_visibility="collapsed")
hero_data = df[df['Name'] == selected_hero].iloc[0]

st.write("")

# Spacious Hero Card Container Block
with st.container(border=True):
    img_col, info_col = st.columns([1, 2], gap="large")
    
    with img_col:
        img_url = photos.get(selected_hero)
        if img_url:
            st.image(img_url, use_container_width=True)
            
    with info_col:
        st.markdown(f"<h2 style='margin-top:0px;'>{hero_data['Name']} {hero_data['Icon']}</h2>", unsafe_allow_html=True)
        st.markdown(f"**Official Classification:** {hero_data['Flag']} {hero_data['Category']} Passport Stream")
        st.markdown("<div style='background-color: #E2E8F0; height: 1px; margin: 15px 0;'></div>", unsafe_allow_html=True)
        
        # Micro metric grids with crisp spatial grouping
        hm1, hm2, hm3 = st.columns(3)
        with hm1:
            st.markdown(f"<p style='color:#64748B; font-size:0.9rem; margin-bottom:2px;'>🏅 Year of Award</p><h3 style='margin-top:0px; color:#0F172A;'>{int(hero_data['Year'])}</h3>", unsafe_allow_html=True)
        with hm2:
            st.markdown(f"<p style='color:#64748B; font-size:0.9rem; margin-bottom:2px;'>🏛️ Intellectual Field</p><h3 style='margin-top:0px; color:#0F172A;'>{hero_data['Field']}</h3>", unsafe_allow_html=True)
        with hm3:
            st.markdown(f"<p style='color:#64748B; font-size:0.9rem; margin-bottom:2px;'>🌍 Regional Base</p><h3 style='margin-top:0px; color:#0F172A;'>{hero_data['Flag']} Verified</h3>", unsafe_allow_html=True)
            
        st.markdown("<div style='background-color: #E2E8F0; height: 1px; margin: 15px 0;'></div>", unsafe_allow_html=True)
        st.markdown("**📜 Verified Historical Significance & Citations:**")
        st.markdown(f"<p style='font-size:1.1rem; line-height:1.6; color:#334155;'>{biographies.get(selected_hero)}</p>", unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.write("")


# ====================================================================
# SECTION 4: COHORT PROFILES (CLEAN SIDE-BY-SIDE LEDGERS)
# ====================================================================
st.header("🌍 Comparative Jurisdictional Records")
st.write("A structured breakdown comparing localized domestic research achievements against international diaspora pipelines.")
st.write("")

col_break1, col_break2 = st.columns([1, 1], gap="large")

# Dynamic metric printer engine
def generate_metric_pointers(subset_df):
    pointers = []
    for field, group in subset_df.groupby('Field'):
        count = len(group)
        years_list = group['Year'].sort_values().astype(str).tolist()
        years_joined = ", ".join(years_list)
        icon = group['Icon'].iloc[0]
        pointers.append(f"<li style='margin-bottom: 12px; font-size:1.05rem;'>{icon} <b>{field}</b> — {count} Laureate(s) <span style='color:#64748B;'>({years_joined})</span></li>")
    return "".join(pointers)

with col_break1:
    st.markdown("### 🏡 Card 5: The Domestic Indian Cohort")
    st.markdown("<div style='background-color: #CCEBC5; height: 4px; margin-bottom: 15px;'></div>", unsafe_allow_html=True)
    
    citizen_df = df[df['Category'] == 'Citizen']
    citizen_html = generate_metric_pointers(citizen_df)
    st.markdown(f"<ul style='list-style-type:none; padding-left:0;'>{citizen_html}</ul>", unsafe_allow_html=True)
    
    st.markdown("")
    st.caption(
        "**Intent & Commentary:** The domestic cohort is anchored primarily in humanitarian, social, and "
        "foundational physical fields. These breakthroughs reflect solutions forged directly within the socioeconomic "
        "realities of the subcontinent, emphasizing cultural enrichment, welfare economics, and baseline physical discoveries."
    )

with col_break2:
    st.markdown("### 🗺️ Card 6: The Global Diaspora Pipeline")
    st.markdown("<div style='background-color: #FBB4AE; height: 4px; margin-bottom: 15px;'></div>", unsafe_allow_html=True)
    
    origin_df = df[df['Category'] == 'Origin']
    origin_html = generate_metric_pointers(origin_df)
    st.markdown(f"<ul style='list-style-type:none; padding-left:0;'>{origin_html}</ul>", unsafe_allow_html=True)
    
    st.markdown("")
    st.caption(
        "**Intent & Commentary:** The diaspora data trends completely toward capital-intensive hard sciences "
        "(*Medicine 🧬, Chemistry 🧪, Astrophysics 🔬*). These breakthroughs systematically showcase the intersection "
        "of Indian foundational talent with advanced Western research infrastructures (primarily US & UK systems) that provide multi-million dollar laboratory environments."
    )
