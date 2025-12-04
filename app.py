import streamlit as st
import time
import pandas as pd
import altair as alt
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

# --- 1. Konfigurasi Halaman & Tema Ultimate ---
st.set_page_config(
    page_title="CipherForge - Blowfish Ultimate",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS (Sci-Fi / Deep Space Look) ---
st.markdown("""
<style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;700&display=swap');

    /* Base Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Data & Monospace Elements */
    .stMetricValue, .stDataFrame, code {
         font-family: 'JetBrains Mono', monospace !important;
    }

    /* Deep Space Background */
    .stApp {
        background: rgb(15,23,42);
        background: linear-gradient(160deg, rgba(15,23,42,1) 0%, rgba(30,27,75,1) 50%, rgba(49,46,129,1) 100%);
        color: #E2E8F0;
    }
    
    /* Sidebar Styles */
    section[data-testid="stSidebar"] {
        background-color: rgba(17, 24, 39, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Glassmorphism Cards & Expanders */
    div[data-testid="stExpander"], div.css-1r6slb0 {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.2); /* Indigo tint border */
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease;
    }
    div[data-testid="stExpander"]:hover {
        border-color: rgba(99, 102, 241, 0.6);
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.3); /* Glow effect */
    }

    /* Custom Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
        border: none;
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
    }

    /* Metric Styling */
    div[data-testid="stMetricLabel"] { color: #94A3B8; }
    div[data-testid="stMetricValue"] { 
        color: #A78BFA !important; /* brighter purple */
        font-weight: 700;
    }

    /* Title Header */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(to right, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .hero-subtitle { font-size: 1.1rem; color: #CBD5E1; margin-bottom: 2rem; }
</style>
""", unsafe_allow_html=True)

# --- 3. Fungsi Logika (Backend) ---
# (Tidak ada perubahan logika di sini, hanya UI)
def run_blowfish_encryption(data, key):
    try:
        cipher = Blowfish.new(key, Blowfish.MODE_CBC)
        iv = cipher.iv
        padded_data = pad(data, Blowfish.block_size)
        encrypted_data = iv + cipher.encrypt(padded_data)
        return encrypted_data, None
    except Exception as e:
        return None, str(e)

def run_blowfish_decryption(data, key):
    try:
        iv = data[:8]
        ciphertext = data[8:]
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
        decrypted_padded = cipher.decrypt(ciphertext)
        decrypted_data = unpad(decrypted_padded, Blowfish.block_size)
        return decrypted_data, None
    except Exception as e:
        return None, str(e)

# --- 4. Sidebar Professional ---
with st.sidebar:
    st.markdown("### 💠 Control Panel")
    st.info("Siapkan file data (Kecil, Sedang, Besar) Anda.")
    
    st.markdown("---")
    uploaded_files = st.file_uploader("1. Upload Data (.txt)", type=["txt"], accept_multiple_files=True)
    
    st.markdown("---")
    st.markdown("#### 2. Security Config")
    key_input = st.text_input("Secret Key", type="password", placeholder="Required (4-56 bytes)")
    operation = st.selectbox("Operation Mode", ["Enkripsi", "Dekripsi"])
    
    valid_key = False
    byte_key = b''
    if key_input:
        byte_key = key_input.encode('utf-8')
        if 4 <= len(byte_key) <= 56:
            valid_key = True
            st.caption("✅ Key Status: Secured")
        else:
            st.error("⚠️ Key Invalid Length")

# --- 5. Main Content Layout ---

# Hero Section Title
st.markdown('<p class="hero-title">CipherForge Ultimate</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Advanced Blowfish Cryptography Benchmark Suite</p>', unsafe_allow_html=True)

# Tabs Layout
tab1, tab2 = st.tabs(["⚡ OPERATION DECK", "📈 PRECISION BENCHMARK"])

# --- TAB 1: Batch Processing Deck ---
with tab1:
    st.markdown("### Mass File Processing")
    
    if not uploaded_files:
        st.warning("Awaiting Data Drop... Upload files in the sidebar to initialize deck.")
        st.image("https://cdn.dribbble.com/users/1138732/screenshots/15246625/media/39439733022f0139e436766979d131a4.jpg?resize=400x300&vertical=center", width=300) # Placeholder image
    
    elif valid_key:
        if st.button(f"INITIATE {operation.upper()} SEQUENCE ({len(uploaded_files)} Files)", type="primary"):
            
            with st.spinner("Processing cryptographic operations..."):
                # Simulate a slight delay for dramatic effect
                time.sleep(0.5)
                
                for idx, uploaded_file in enumerate(uploaded_files):
                    uploaded_file.seek(0)
                    file_bytes = uploaded_file.read()
                    
                    start_time = time.time()
                    if operation == "Enkripsi":
                        result_data, error = run_blowfish_encryption(file_bytes, byte_key)
                        output_name = f"enc_{uploaded_file.name}"
                        icon = "🔒"
                    else:
                        result_data, error = run_blowfish_decryption(file_bytes, byte_key)
                        output_name = f"dec_{uploaded_file.name}"
                        icon = "🔓"
                    exec_time = (time.time() - start_time) * 1000
                    
                    # Glow Card UI per File
                    with st.expander(f"{icon} {uploaded_file.name}", expanded=True):
                        if result_data:
                            c1, c2, c3 = st.columns(3)
                            c1.metric("Execution Time", f"{exec_time:.3f} ms")
                            c2.metric("Output Size", f"{len(result_data):,} bytes")
                            c3.download_button(
                                label=f"⬇️ Download Result",
                                data=result_data,
                                file_name=output_name,
                                mime="text/plain",
                                key=f"dl_{idx}"
                            )
                        else:
                            st.error(f"Operation Failed: {error}")
            
            st.success("Sequence Complete. All files processed securely.", icon="💠")

# --- TAB 2: Deep Benchmark (The Cool Part) ---
with tab2:
    st.markdown("### 10-Iteration Stability Analysis")
    st.caption("Mengukur konsistensi performa algoritma di bawah beban berulang.")
    
    if not uploaded_files or not valid_key:
        st.info("Requires loaded files and valid key to commence benchmark protocol.")
    else:
        if st.button("ENGAGE BENCHMARK PROTOCOL"):
            
            all_detailed_results = []
            # Data structure for Altair chart (melted/long format)
            chart_data_list = []
            
            progress_bar = st.progress(0)
            status_container = st.empty()
            total_ops = len(uploaded_files) * 10
            current_op = 0
            
            with st.spinner("Running extensive tests... Do not close tab."):
                for u_file in uploaded_files:
                    u_file.seek(0)
                    file_bytes = u_file.read()
                    f_name = u_file.name
                    
                    file_row_wide = {"File": f_name, "Size": len(file_bytes)}
                    times = []
                    
                    for i in range(10):
                        iter_num = i + 1
                        status_container.markdown(f"Analyzing **{f_name}**... | Iteration `{iter_num}/10`")
                        
                        start = time.time()
                        if operation == "Enkripsi":
                            out, _ = run_blowfish_encryption(file_bytes, byte_key)
                        else:
                            out, _ = run_blowfish_decryption(file_bytes, byte_key)
                        end = time.time()
                        
                        durasi = 0
                        if out:
                            durasi = (end - start) * 1000
                            times.append(durasi)
                            file_row_wide[f"I-{iter_num}"] = durasi
                            
                            # Collect data for Chart
                            chart_data_list.append({
                                "File": f_name,
                                "Iteration": iter_num,
                                "Time (ms)": durasi
                            })
                        else:
                            file_row_wide[f"I-{iter_num}"] = None # Mark failed

                        current_op += 1
                        progress_bar.progress(min(current_op / total_ops, 1.0))

                    if times:
                        file_row_wide["Average"] = sum(times) / len(times)
                    
                    all_detailed_results.append(file_row_wide)

            progress_bar.empty()
            status_container.empty()
            st.balloons() # Sedikit efek perayaan

            # --- VISUALIZATION SECTION ---
            
            # 1. Interactive Line Chart (Altair) - Jauh lebih keren dari bar chart
            st.markdown("#### 📈 Performance Stability Monitor")
            st.caption("Grafik ini menunjukkan seberapa stabil waktu eksekusi di setiap iterasi. Garis yang datar lebih baik.")
            
            if chart_data_list:
                df_chart = pd.DataFrame(chart_data_list)
                
                # Membuat Chart Interaktif
                line_chart = alt.Chart(df_chart).mark_line(point=True).encode(
                    x=alt.X('Iteration:O', title='Iteration Sequence (1-10)'), # O for Ordinal
                    y=alt.Y('Time (ms):Q', title='Execution Time (ms)'), # Q for Quantitative
                    color=alt.Color('File:N', title='File Name'), # N for Nominal
                    tooltip=['File', 'Iteration', alt.Tooltip('Time (ms)', format='.4f')]
                ).properties(
                    height=350
                ).interactive() # Membuatnya bisa di-zoom/pan
                
                st.altair_chart(line_chart, use_container_width=True)

            # 2. Detailed Data Table
            st.markdown("#### 📋 Precision Data Matrix")
            df_detail = pd.DataFrame(all_detailed_results)
            
            # Config kolom untuk tampilan monospace yang rapi
            col_config = {
                "Average": st.column_config.NumberColumn(
                    "Avg Time (ms)", format="%.4f", help="Rata-rata 10 iterasi"
                ),
                "Size": st.column_config.NumberColumn(format="%d Bytes"),
            }
            # Format kolom I-1 sampai I-10
            for i in range(1, 11):
                col_config[f"I-{i}"] = st.column_config.NumberColumn(format="%.3f")

            st.dataframe(
                df_detail,
                use_container_width=True,
                column_config=col_config,
                height=250
            )

            # Export
            csv = df_detail.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📄 Export Data Matrix (CSV)",
                data=csv,
                file_name='blowfish_ultimate_benchmark.csv',
                mime='text/csv',
                help="Unduh untuk analisis laporan"
            )