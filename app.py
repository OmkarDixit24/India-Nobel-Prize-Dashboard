import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="The Indian Nobel Footprint | Executive Dashboard", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Signature Economist Red Top Bar
st.markdown("<div style='background-color: #E5233D; height: 6px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# Main Title block with integrated flag iconography
st.title("🇮🇳 Executive Record: India’s Nobel Laureates")
st.markdown(
    """
    An editorial and analytical study exploring the historical timeline, field distributions, and citizenship 
    pivots of Nobel winners from the Indian subcontinent. *Data scaled from 1913 to modern metrics.*
    """
)
st.markdown("---")

# 2. Secure Data Loading
df = pd.read_excel("nobel_data.xlsx")

# Stable Public Domain Profile Image Repository (Wikimedia Ecosystem)
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

# Detailed descriptions for the Hero Card
biographies = {
    "Rabindranath Tagore": "The first non-European laureate in Literature. Awarded for his profoundly sensitive, fresh, and beautiful verse in Gitanjali, establishing Indian literary traditions globally.",
    "C. V. Raman": "Awarded for his groundbreaking work on the scattering of light and the discovery of the Raman Effect, single-handedly placing India on the map of modern quantum physics.",
    "Har Gobind Khorana": "Awarded for his interpretation of the genetic code and its function in protein synthesis, laying the absolute groundwork for modern biotechnology.",
    "Mother Teresa": "Recognized for her work in bringing help to suffering humanity, founding the Missionaries of Charity in Kolkata and pioneering international humanitarian relief.",
    "Subrahmanyan Chandrasekhar": "Awarded for his theoretical studies of the physical processes of importance to the structure and evolution of stars, giving birth to the Chandrasekhar Limit.",
    "Amartya Sen": "Awarded for his deep contributions to welfare economics and social choice theory, changing how the United Nations and global bodies perceive poverty indices.",
    "V. S. Naipaul": "Awarded for having united perceptive narrative and incorruptible scrutiny in works that compel us to see the presence of suppressed histories.",
    "Venkatraman Ramakrishnan": "Awarded for his high-resolution structural mapping of the ribosome, fundamentally transforming the development of modern broad-spectrum antibiotics.",
    "Kailash Satyarthi": "Awarded for his struggle against the suppression of children and young people, saving over 80,000 children from forced labor and advocating universal education.",
    "Abhijit Banerjee": "Awarded for his experimental approach to alleviating global poverty, pioneering the use of randomized controlled trials (RCTs) in development economics."
}


# ====================================================================
# ROW 1: CARD 1 & CARD 2 (VISUALIZATIONS WITH COMMENTARY)
# ====================================================================
col_vis1, col_vis2 = st.columns([1, 1], gap="large")

with col_vis1:
    st.subheader("📊 Card 1: Cohort Distribution Balance")
    
    # Process summary metrics for Card 1
    total_w = len(df)
    citizen_w = len(df[df['Category'] == 'Citizen'])
    diaspora_w = len(df[df['Category'] == 'Origin'])
    
    summary_df = pd.DataFrame({
        'Group': ['🇮🇳 Total Volume', '🏡 Citizens', '🗺️ Diaspora'],
        'Count': [total_w, citizen_w, diaspora_w],
        'ColorGroup': ['Total', 'Citizen', 'Diaspora']
    })
    
    # Pastel Bar Chart
    fig1 = px.bar(
        summary_df, 
        x='Count', 
        y='Group', 
        orientation='h', 
        text='Count',
        color='ColorGroup',
        color_discrete_map={
            'Total': '#B3CDE3',      # Pastel Ice Blue
            'Citizen': '#CCEBC5',    # Pastel Soft Green
            'Diaspora': '#FBB4AE'    # Pastel Muted Rose
        }
    )
    fig1.update_layout(
        plot_bgcolor='white', 
        showlegend=False,
        xaxis_showgrid=False, 
        xaxis_visible=False, 
        yaxis_title=None,
        height=250, 
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.info(
        f"**Editorial Gist:** Out of {total_w} total historical winners, the distribution is "
        f"split almost evenly down the middle: **{citizen_w} stayed domestic** holding Indian passports, "
        f"while **{diaspora_w} found breakthroughs abroad**. This showcases a dual track of intellectual output."
    )

with col_vis2:
    st.subheader("🗓️ Card 2: Field & Chronological Grid Matrix")
    
    # Scatter plot mapping: Y=Year, X=Field, Text=Icons only
    fig2 = px.scatter(
        df, 
        x='Field', 
        y='Year', 
        text='Icon',
        hover_name='Name',
        custom_data=['Flag', 'Category']
    )
    
    # Inject large emoji text markers instead of standard points
    fig2.update_traces(
        mode='text',
        textfont=dict(size=26),
        hovertemplate="<b>%{hovertext}</b><br>📅 Year: %{y}<br>🏛️ Field: %{x}<br>📍 Status: %{customdata[0]} %{customdata[1]}<extra></extra>"
    )
    
    # Pastel styling for the coordinate grid
    fig2.update_layout(
        plot_bgcolor='#F9F9F9',
        xaxis_showgrid=True,
        xaxis_gridcolor='#EAEAEA',
        yaxis_showgrid=True,
        yaxis_gridcolor='#EAEAEA',
        yaxis=dict(tickvals=[1913, 1930, 1968, 1979, 1983, 1998, 2001, 2009, 2014, 2019]),
        height=250,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title=None,
        yaxis_title=None
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    st.warning(
        "**Reader Fact:** This matrix isolates history by category. Notice the heavy concentration "
        "in *Physics 🔬* and *Economics 📊*. Hover over any individual icon inside the grid above to view "
        "their historical name and citizenship timeline."
    )

st.markdown("---")

# ====================================================================
# ROW 2: THE HERO CARD (IN-DEPTH BIO CONTAINER WITH PORTRAITS)
# ====================================================================
st.subheader("🌟 Card 4: The Hero Deep-Dive Canvas")
st.write("Select any laureate from the master selector below to retrieve their official visual profile and file records.")

selected_hero = st.selectbox("Choose a Laureate to inspect:", df['Name'].unique())
hero_data = df[df['Name'] == selected_hero].iloc[0]

# Split Hero Card into picture column and data card column
with st.container(border=True):
    img_col, info_col = st.columns([1, 2], gap="large")
    
    with img_col:
        # Load profile picture with error fallback protection
        img_url = photos.get(selected_hero)
        if img_url:
            st.image(img_url, use_container_width=True, caption=f"Official Portrait: {hero_data['Name']}")
        else:
            st.info("📷 Profile photo canvas unreached.")
            
    with info_col:
        st.markdown(f"## {hero_data['Name']} {hero_data['Icon']}")
        st.markdown(f"#### Passport Status: {hero_data['Flag']} {hero_data['Category']} ({'India 🇮🇳' if hero_data['Category'] == 'Citizen' else 'International Base'})")
        st.markdown("---")
        
        # Grid layout for core metrics
        meta_1, meta_2, meta_3 = st.columns(3)
        meta_1.metric(label="🏅 Award Year", value=int(hero_data['Year']))
        meta_2.metric(label="🏛️ Intellectual Field", value=hero_data['Field'])
        meta_3.metric(label="🌍 Origin Marker", value=f"{hero_data['Flag']} Destination")
        
        st.markdown("---")
        st.markdown("**📜 Comprehensive Historical Account:**")
        st.write(biographies.get(selected_hero, "Exceptional record verified within global annals."))

st.markdown("---")

# ====================================================================
# ROW 3: CARD 5 & CARD 6 (COHORT BREAKDOWNS)
# ====================================================================
col_break1, col_break2 = st.columns([1, 1], gap="large")

# Dynamic helper function to generate requested pointers: Field - Count - Years
def generate_metric_pointers(subset_df):
    pointers = []
    # Loop over fields sorted systematically
    for field, group in subset_df.groupby('Field'):
        count = len(group)
        years_list = group['Year'].sort_values().astype(str).tolist()
        years_joined = ", ".join(years_list)
        icon = group['Icon'].iloc[0]
        flag = group['Flag'].iloc[0]
        pointers.append(f"• **{icon} {field}** — {count} Laureate(s) — *({years_joined})*")
    return pointers

with col_break1:
    st.subheader("🏡 Card 5: Domestic Cohort Profile")
    st.write("Systematic listing of winners holding active Indian passports at award presentation:")
    
    citizen_df = df[df['Category'] == 'Citizen']
    citizen_pointers = generate_metric_pointers(citizen_df)
    
    # Display the processed data points
    for line in citizen_pointers:
        st.markdown(line)
        
    st.markdown("---")
    st.caption(
        "**Context:** Domestic breakthroughs are anchored entirely in human development, "
        "predominantly representing foundational Literature, peace initiatives, and early physical research "
        "conducted directly inside Indian soil."
    )

with col_break2:
    st.subheader("🗺️ Card 6: Global Diaspora Profile")
    st.write("Systematic listing of winners born on the subcontinent operating under foreign jurisdictions:")
    
    origin_df = df[df['Category'] == 'Origin']
    origin_pointers = generate_metric_pointers(origin_df)
    
    # Display the processed data points
    for line in origin_pointers:
        st.markdown(line)
        
    st.markdown("---")
    st.caption(
        "**Context:** The global diaspora trends heavily toward specialized hard sciences "
        "(*Medicine 🧬, Chemistry 🧪, Physics 🔬*) requiring capital-intensive global laboratory infrastructure "
        "located in the US and UK."
    )