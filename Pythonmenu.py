import os
os.environ['STREAMLIT_SERVER_PORT'] = '8502'

import streamlit as st
import webbrowser
import datetime
import urllib.parse
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
import time

st.set_page_config(page_title="Multitask", layout="wide")

# Initialize session state for card visibility
if 'active_card' not in st.session_state:
    st.session_state.active_card = None

# Professional Black Theme with Clean Card Design
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #ffffff !important;
    }

    .stTextInput>div>div>input,
    .stTextArea>div>textarea,
    .stSelectbox>div>div>div {
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 1px solid #555;
        border-radius: 8px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #1f2937, #4b5563);
        color: white !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        width: 100%;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4b5563, #6b7280);
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.4);
        transform: translateY(-2px);
    }

    .tool-card {
        background: rgba(31, 31, 31, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        text-align: center;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 255, 255, 0.2);
        border-color: rgba(0, 255, 255, 0.3);
    }

    .tool-logo {
        font-size: 4rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.3));
    }

    .tool-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #00ffff;
        margin-bottom: 0.5rem;
    }

    .tool-description {
        color: #cccccc;
        font-size: 0.9rem;
        line-height: 1.4;
    }

    .active-card {
        background: rgba(0, 255, 255, 0.1);
        border: 2px solid rgba(0, 255, 255, 0.4);
        transform: scale(1.02);
    }

    .function-panel {
        background: rgba(20, 20, 20, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(0, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 255, 255, 0.1);
    }

    .function-header {
        color: #00ffff;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        text-align: center;
        border-bottom: 2px solid rgba(0, 255, 255, 0.3);
        padding-bottom: 1rem;
    }

    .success-message {
        background: rgba(0, 255, 0, 0.1);
        border: 1px solid rgba(0, 255, 0, 0.3);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #00ff00;
    }

    .error-message {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid rgba(255, 0, 0, 0.3);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #ff6b6b;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style="text-align: center; padding: 2rem 0; margin-bottom: 2rem;">
        <h1 style="font-size: 3.5rem; background: linear-gradient(135deg, #00ffff, #ffffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            💼 Multitask
        </h1>
        <p style="font-size: 1.3rem; color: #cccccc; margin-top: 0.5rem;">
            Professional Toolkit - Click on any tool to get started
        </p>
    </div>
""", unsafe_allow_html=True)

# Tool Cards Grid
st.markdown("## 🛠️ Available Tools")

col1, col2, col3 = st.columns(3)

# WhatsApp Card
with col1:
    card_class = "tool-card active-card" if st.session_state.active_card == "whatsapp" else "tool-card"
    st.markdown(f"""
        <div class="{card_class}">
            <div class="tool-logo">📱</div>
            <div class="tool-title">WhatsApp</div>
            <div class="tool-description">Send messages instantly to any WhatsApp number worldwide</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("📱 Open WhatsApp Tool", key="whatsapp_btn", use_container_width=True):
        st.session_state.active_card = "whatsapp"
        st.rerun()

# Email Card
with col2:
    card_class = "tool-card active-card" if st.session_state.active_card == "email" else "tool-card"
    st.markdown(f"""
        <div class="{card_class}">
            <div class="tool-logo">📧</div>
            <div class="tool-title">Email Sender</div>
            <div class="tool-description">Send professional emails via your default email client</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("📧 Open Email Tool", key="email_btn", use_container_width=True):
        st.session_state.active_card = "email"
        st.rerun()

# Maps Card
with col3:
    card_class = "tool-card active-card" if st.session_state.active_card == "maps" else "tool-card"
    st.markdown(f"""
        <div class="{card_class}">
            <div class="tool-logo">🗺️</div>
            <div class="tool-title">Maps & Routes</div>
            <div class="tool-description">Find locations and plan routes with interactive maps</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🗺️ Open Maps Tool", key="maps_btn", use_container_width=True):
        st.session_state.active_card = "maps"
        st.rerun()

# Second Row
col4, col5, col6 = st.columns(3)

# Social Media Card
with col4:
    card_class = "tool-card active-card" if st.session_state.active_card == "social" else "tool-card"
    st.markdown(f"""
        <div class="{card_class}">
            <div class="tool-logo">🌐</div>
            <div class="tool-title">Social Media</div>
            <div class="tool-description">Share content across Twitter, Facebook, and LinkedIn</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌐 Open Social Media Tool", key="social_btn", use_container_width=True):
        st.session_state.active_card = "social"
        st.rerun()

# Camera Card
with col5:
    card_class = "tool-card active-card" if st.session_state.active_card == "camera" else "tool-card"
    st.markdown(f"""
        <div class="{card_class}">
            <div class="tool-logo">📸</div>
            <div class="tool-title">Camera</div>
            <div class="tool-description">Access camera functionality and media tools</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("📸 Open Camera Tool", key="camera_btn", use_container_width=True):
        st.session_state.active_card = "camera"
        st.rerun()

# Placeholder for future tool
with col6:
    st.markdown("""
        <div class="tool-card" style="opacity: 0.3;">
            <div class="tool-logo">🚀</div>
            <div class="tool-title">Coming Soon</div>
            <div class="tool-description">More amazing tools are on the way!</div>
        </div>
    """, unsafe_allow_html=True)

# Show active tool panel
if st.session_state.active_card:
    st.markdown("---")
    
    # Close button at the top
    if st.button("❌ Close Tool", key="close_tool", use_container_width=False):
        st.session_state.active_card = None
        st.rerun()
    
    # WhatsApp Function Panel
    if st.session_state.active_card == "whatsapp":
        st.markdown("""
            <div class="function-panel">
                <div class="function-header">📱 WhatsApp Messenger</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📱 Send WhatsApp Message")
        
        col_w1, col_w2 = st.columns([3, 1])
        with col_w1:
            number = st.text_input("📞 Phone Number (with country code)", 
                                 placeholder="Example: +919876543210", 
                                 help="Include country code like +91 for India, +1 for USA")
            message = st.text_area("💬 Message", 
                                 placeholder="Type your message here...", 
                                 height=100)
        
        with col_w2:
            st.markdown("### 💡 Tips")
            st.info("• Include country code\n• Message opens in WhatsApp\n• You can edit before sending")
        
        if st.button("🚀 Send WhatsApp Message", key="send_whatsapp", use_container_width=True):
            if number and message:
                try:
                    # Clean the number
                    clean_number = number.replace("+", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                    encoded_message = urllib.parse.quote(message)
                    
                    # Create WhatsApp URL
                    whatsapp_url = f"https://wa.me/{clean_number}?text={encoded_message}"
                    
                    # Show the URL and try to open it
                    st.markdown(f"""
                        <div class="success-message">
                            ✅ WhatsApp link created! Click the link below or copy it:
                            <br><br>
                            <a href="{whatsapp_url}" target="_blank" style="color: #00ffff; text-decoration: underline;">
                                🔗 Open WhatsApp Message
                            </a>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.code(whatsapp_url, language="text")
                    
                    # Try to open automatically
                    try:
                        webbrowser.open(whatsapp_url)
                    except:
                        pass
                        
                except Exception as e:
                    st.error(f"❌ Error creating WhatsApp link: {str(e)}")
            else:
                st.warning("⚠️ Please fill in both phone number and message.")
    
    # Email Function Panel
    elif st.session_state.active_card == "email":
        st.markdown("""
            <div class="function-panel">
                <div class="function-header">📧 Email Sender</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📧 Compose Email")
        
        col_e1, col_e2 = st.columns([3, 1])
        with col_e1:
            recipient = st.text_input("📮 Recipient Email", 
                                    placeholder="recipient@example.com")
            subject = st.text_input("📝 Subject", 
                                  placeholder="Email subject")
            body = st.text_area("✉️ Email Body", 
                               placeholder="Write your email content here...", 
                               height=120)
        
        with col_e2:
            st.markdown("### 📧 Info")
            st.info("• Opens default email client\n• Pre-fills all fields\n• Works with Gmail, Outlook, etc.")

        if st.button("📤 Open Email Client", key="send_email", use_container_width=True):
            if recipient and subject and body:
                try:
                    # Create mailto URL
                    mailto_url = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                    
                    st.markdown(f"""
                        <div class="success-message">
                            ✅ Email link created! Click the link below or copy it:
                            <br><br>
                            <a href="{mailto_url}" target="_blank" style="color: #00ffff; text-decoration: underline;">
                                🔗 Open Email Client
                            </a>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.code(mailto_url, language="text")
                    
                    # Try to open automatically
                    try:
                        webbrowser.open(mailto_url)
                    except:
                        pass
                        
                except Exception as e:
                    st.error(f"❌ Error creating email link: {str(e)}")
            else:
                st.warning("⚠️ Please fill in all fields.")
    
    # Maps Function Panel
    elif st.session_state.active_card == "maps":
        st.markdown("""
            <div class="function-panel">
                <div class="function-header">🗺️ Maps & Navigation</div>
            </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📍 Find Location", "🛣️ Plan Route", "🌐 External Maps"])
        
        with tab1:
            st.markdown("### 📍 Search Location")
            
            col_m1, col_m2 = st.columns([2, 1])
            with col_m1:
                location_query = st.text_input("🏠 Enter Location", 
                                             placeholder="New York, NY or Times Square")
                
                if st.button("🔍 Search Location", key="search_location", use_container_width=True):
                    if location_query:
                        try:
                            with st.spinner("🔍 Searching location..."):
                                geolocator = Nominatim(user_agent="Multitask_v2")
                                location = geolocator.geocode(location_query, timeout=10)
                                
                                if location:
                                    st.success(f"📍 Found: {location.address}")
                                    st.info(f"🌍 Coordinates: {location.latitude:.6f}, {location.longitude:.6f}")
                                    
                                    # Store in session state
                                    st.session_state.found_location = {
                                        'name': location.address,
                                        'lat': location.latitude,
                                        'lon': location.longitude
                                    }
                                else:
                                    st.error("❌ Location not found. Try a different search term.")
                        except Exception as e:
                            st.error(f"❌ Search error: {str(e)}")
                    else:
                        st.warning("⚠️ Please enter a location to search.")
            
            with col_m2:
                st.markdown("### 💡 Search Tips")
                st.info("• Try specific addresses\n• Use landmarks\n• Include city/state\n• Use proper spelling")
            
            # Display map if location found
            if hasattr(st.session_state, 'found_location') and st.session_state.found_location:
                try:
                    loc_data = st.session_state.found_location
                    m = folium.Map(location=[loc_data['lat'], loc_data['lon']], zoom_start=15)
                    folium.Marker([loc_data['lat'], loc_data['lon']], 
                                tooltip="📍 Found Location", 
                                popup=loc_data['name'],
                                icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
                    st_folium(m, width=700, height=400)
                except Exception as e:
                    st.error(f"Map display error: {str(e)}")
        
        with tab2:
            st.markdown("### 🛣️ Route Planning")
            
            col_r1, col_r2 = st.columns([2, 1])
            with col_r1:
                start_location = st.text_input("🚀 Starting Point", 
                                             placeholder="Enter starting location")
                end_location = st.text_input("🎯 Destination", 
                                           placeholder="Enter destination")
                
                if st.button("🗺️ Plan Route", key="plan_route", use_container_width=True):
                    if start_location and end_location:
                        try:
                            with st.spinner("🗺️ Planning route..."):
                                geolocator = Nominatim(user_agent="Multitask_v2")
                                start_loc = geolocator.geocode(start_location, timeout=10)
                                end_loc = geolocator.geocode(end_location, timeout=10)
                                
                                if start_loc and end_loc:
                                    # Calculate approximate distance
                                    lat_diff = end_loc.latitude - start_loc.latitude
                                    lon_diff = end_loc.longitude - start_loc.longitude
                                    distance = ((lat_diff**2 + lon_diff**2)**0.5) * 111  # Rough km calculation
                                    
                                    st.success(f"✅ Route planned successfully!")
                                    st.info(f"📏 Approximate distance: {distance:.1f} km")
                                    
                                    # Store route data
                                    st.session_state.route_data = {
                                        'start': {'name': start_location, 'lat': start_loc.latitude, 'lon': start_loc.longitude},
                                        'end': {'name': end_location, 'lat': end_loc.latitude, 'lon': end_loc.longitude},
                                        'distance': distance
                                    }
                                else:
                                    st.error("❌ Could not find one or both locations.")
                        except Exception as e:
                            st.error(f"❌ Route planning error: {str(e)}")
                    else:
                        st.warning("⚠️ Please enter both starting point and destination.")
            
            with col_r2:
                st.markdown("### 🛣️ Route Info")
                st.info("• Plan routes between locations\n• Get distance estimates\n• Visual route display")
            
            # Display route map
            if hasattr(st.session_state, 'route_data') and st.session_state.route_data:
                try:
                    route = st.session_state.route_data
                    start = route['start']
                    end = route['end']
                    
                    # Calculate center point
                    center_lat = (start['lat'] + end['lat']) / 2
                    center_lon = (start['lon'] + end['lon']) / 2
                    
                    # Create map
                    m = folium.Map(location=[center_lat, center_lon], zoom_start=8)
                    
                    # Add markers
                    folium.Marker([start['lat'], start['lon']], 
                                tooltip="🚀 Start", popup=start['name'],
                                icon=folium.Icon(color='green', icon='play')).add_to(m)
                    folium.Marker([end['lat'], end['lon']], 
                                tooltip="🎯 End", popup=end['name'],
                                icon=folium.Icon(color='red', icon='stop')).add_to(m)
                    
                    # Add route line
                    folium.PolyLine(locations=[[start['lat'], start['lon']], [end['lat'], end['lon']]], 
                                  color="cyan", weight=4, opacity=0.7).add_to(m)
                    
                    st_folium(m, width=700, height=400)
                except Exception as e:
                    st.error(f"Route map error: {str(e)}")
        
        with tab3:
            st.markdown("### 🌐 Open in External Maps")
            
            external_location = st.text_input("🗺️ Location for External Maps", 
                                            placeholder="Enter location to open in external maps")
            
            col_ext1, col_ext2 = st.columns(2)
            with col_ext1:
                if st.button("📍 Open in Google Maps", key="open_google_maps", use_container_width=True):
                    if external_location:
                        try:
                            google_url = f"https://www.google.com/maps/search/{urllib.parse.quote(external_location)}"
                            st.markdown(f"""
                                <div class="success-message">
                                    ✅ Google Maps link created!
                                    <br><br>
                                    <a href="{google_url}" target="_blank" style="color: #00ffff; text-decoration: underline;">
                                        🔗 Open in Google Maps
                                    </a>
                                </div>
                            """, unsafe_allow_html=True)
                            webbrowser.open(google_url)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                    else:
                        st.warning("⚠️ Please enter a location.")
            
            with col_ext2:
                if st.button("🗺️ Open in OpenStreetMap", key="open_osm", use_container_width=True):
                    if external_location:
                        try:
                            osm_url = f"https://www.openstreetmap.org/search?query={urllib.parse.quote(external_location)}"
                            st.markdown(f"""
                                <div class="success-message">
                                    ✅ OpenStreetMap link created!
                                    <br><br>
                                    <a href="{osm_url}" target="_blank" style="color: #00ffff; text-decoration: underline;">
                                        🔗 Open in OpenStreetMap
                                    </a>
                                </div>
                            """, unsafe_allow_html=True)
                            webbrowser.open(osm_url)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                    else:
                        st.warning("⚠️ Please enter a location.")
    
    # Social Media Function Panel
    elif st.session_state.active_card == "social":
        st.markdown("""
            <div class="function-panel">
                <div class="function-header">🌐 Social Media Publisher</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🌐 Share on Social Media")
        
        col_s1, col_s2 = st.columns([3, 1])
        with col_s1:
            social_content = st.text_area("✍️ Your Content", 
                                        placeholder="Write your post, share a link, or express your thoughts...", 
                                        height=120)
            platform = st.selectbox("📱 Choose Platform", 
                                   ["Twitter", "Facebook", "LinkedIn", "Reddit", "WhatsApp"], 
                                   index=0)
        
        with col_s2:
            st.markdown("### 📊 Platform Tips")
            if platform == "Twitter":
                st.info("• Max 280 characters\n• Use hashtags\n• Tag with @username")
            elif platform == "Facebook":
                st.info("• Add engaging content\n• Use images/videos\n• Ask questions")
            elif platform == "LinkedIn":
                st.info("• Professional tone\n• Industry insights\n• Network building")
            elif platform == "Reddit":
                st.info("• Choose right subreddit\n• Follow rules\n• Engage discussions")
            else:  # WhatsApp
                st.info("• Share with contacts\n• Add personal touch\n• Use emojis")
        
        if st.button(f"🚀 Share on {platform}", key="share_social", use_container_width=True):
            if social_content.strip():
                try:
                    encoded_content = urllib.parse.quote(social_content)
                    
                    if platform == "Twitter":
                        social_url = f"https://twitter.com/intent/tweet?text={encoded_content}"
                    elif platform == "Facebook":
                        social_url = f"https://www.facebook.com/sharer/sharer.php?quote={encoded_content}"
                    elif platform == "LinkedIn":
                        social_url = f"https://www.linkedin.com/sharing/share-offsite/?summary={encoded_content}"
                    elif platform == "Reddit":
                        social_url = f"https://www.reddit.com/submit?title={encoded_content}"
                    elif platform == "WhatsApp":
                        social_url = f"https://wa.me/?text={encoded_content}"
                    
                    st.markdown(f"""
                        <div class="success-message">
                            ✅ {platform} sharing link created!
                            <br><br>
                            <a href="{social_url}" target="_blank" style="color: #00ffff; text-decoration: underline;">
                                🔗 Share on {platform}
                            </a>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.code(social_url, language="text")
                    
                    try:
                        webbrowser.open(social_url)
                    except:
                        pass
                        
                except Exception as e:
                    st.error(f"❌ Error creating {platform} link: {str(e)}")
            else:
                st.warning("⚠️ Please write some content to share.")
    
    # Camera Function Panel
    elif st.session_state.active_card == "camera":
        st.markdown("""
            <div class="function-panel">
                <div class="function-header">📸 Camera & Media Tools</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📸 Camera Access")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("#### 📱 Mobile Camera")
            st.info("For best camera experience on mobile devices, use your device's built-in camera app.")
            
            if st.button("📱 Open Camera App", key="open_mobile_camera", use_container_width=True):
                st.success("📸 Please use your device's camera app for photos and videos!")
        
        with col_c2:
            st.markdown("#### 💻 Desktop Camera")
            st.info("For desktop users, camera access requires proper permissions and may vary by browser.")
            
            if st.button("💻 Camera Instructions", key="desktop_camera", use_container_width=True):
                st.info("🔧 To use camera on desktop:\n• Allow camera permissions\n• Use Chrome/Firefox\n• Enable HTTPS if needed")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <p style="font-size: 1.2rem; color: #00ffff; font-weight: bold;">💼 Multitask</p>
        <p style="color: #999; font-size: 0.9rem;">Professional tools made simple • Click buttons to activate tools</p>
    </div>
""", unsafe_allow_html=True)