import streamlit as st
import pandas as pd
from datetime import date, timedelta
import random
import base64
import os

st.set_page_config(page_title="po-work (포워크)", page_icon="🥔", layout="wide")

if 'theme_mode' not in st.session_state:
    st.session_state['theme_mode'] = 'light'

def toggle_theme():
    st.session_state['theme_mode'] = 'dark' if st.session_state['theme_mode'] == 'light' else 'light'

def load_image_data_uri(candidates):
    for fname, mime in candidates:
        if os.path.exists(fname):
            with open(fname, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            return f"data:{mime};base64,{b64}"
    return None

HERO_IMG_URI = load_image_data_uri([
    ("farm.avif", "image/avif"),
    ("farm.jpg", "image/jpeg"),
    ("farm.jpeg", "image/jpeg"),
    ("farm.png", "image/png"),
])

POTATO_IMG_URI = load_image_data_uri([
    ("potato.png", "image/png"),
    ("potato.jpg", "image/jpeg"),
    ("potato.avif", "image/avif"),
])

UGLY_MARKET_IMG_URI = load_image_data_uri([
    ("ugly_market.jpg", "image/jpeg"),
    ("ugly_market.jpeg", "image/jpeg"),
    ("ugly_market.avif", "image/avif"),
    ("ugly_market.png", "image/png"),
])

CROP_IMAGES = {
    "감자 수확": load_image_data_uri([("potato_crop.jpg", "image/jpeg"), ("potato_crop.png", "image/png")]) or "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=800&q=80",
    "감자": load_image_data_uri([("potato_crop.jpg", "image/jpeg"), ("potato_crop.png", "image/png")]) or "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=800&q=80",
    "고구마 수확": load_image_data_uri([("sweet_potato.jpg", "image/jpeg"), ("sweet_potato.png", "image/png")]) or "https://images.unsplash.com/photo-1596097635121-14b63b7a0c19?auto=format&fit=crop&w=800&q=80",
    "고구마": load_image_data_uri([("sweet_potato.jpg", "image/jpeg"), ("sweet_potato.png", "image/png")]) or "https://images.unsplash.com/photo-1596097635121-14b63b7a0c19?auto=format&fit=crop&w=800&q=80",
    "당근 수확": load_image_data_uri([("carrot.jpg", "image/jpeg"), ("carrot.png", "image/png")]) or "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=800&q=80",
    "당근": load_image_data_uri([("carrot.jpg", "image/jpeg"), ("carrot.png", "image/png")]) or "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=800&q=80",
    "옥수수 수확": load_image_data_uri([("corn.jpg", "image/jpeg"), ("corn.png", "image/png")]) or "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=800&q=80",
    "옥수수": load_image_data_uri([("corn.jpg", "image/jpeg"), ("corn.png", "image/png")]) or "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=800&q=80",
    "비료 운반": load_image_data_uri([("fertilizer.jpg", "image/jpeg"), ("fertilizer.png", "image/png")]) or "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=800&q=80",
    "잡초 제거": load_image_data_uri([("weed.jpg", "image/jpeg"), ("weed.png", "image/png")]) or "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=800&q=80",
    "김장 배추": load_image_data_uri([("cabbage.jpg", "image/jpeg"), ("cabbage.png", "image/png")]) or "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?auto=format&fit=crop&w=800&q=80",
    "배추": load_image_data_uri([("cabbage.jpg", "image/jpeg"), ("cabbage.png", "image/png")]) or "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?auto=format&fit=crop&w=800&q=80",
    "사과": load_image_data_uri([("apple.jpg", "image/jpeg"), ("apple.png", "image/png")]) or "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=800&q=80",
}

def resolve_crop_image(job_type_or_title, photo_b64=None):
    if photo_b64:
        return "data:image/jpeg;base64," + photo_b64
    text = str(job_type_or_title)
    if text in CROP_IMAGES:
        return CROP_IMAGES[text]
    for key, url in CROP_IMAGES.items():
        if key in text:
            return url
    return HERO_IMG_URI or "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=800&q=80"

is_dark = (st.session_state['theme_mode'] == 'dark')

app_bg = "#181512" if is_dark else "#F8F7F2"
card_bg = "#26211C" if is_dark else "#FFFFFF"
side_bg = "#211C18" if is_dark else "#FFFFFF"
text_main = "#F5EEDC" if is_dark else "#2B2118"
text_sub = "#D7C7AE" if is_dark else "#5D4E42"
primary_green = "#81C784" if is_dark else "#2E7D32"
accent_orange = "#FF8A3D" if is_dark else "#F57C00"
border_subtle = "#4A3F35" if is_dark else "#D6D0C4"
btn_bg = "#2E2721" if is_dark else "#FFFFFF"
btn_text = "#F5EEDC" if is_dark else "#2B2118"
btn_hover_bg = "#2E7D32"
btn_hover_text = "#FFFFFF"
red_text = "#FF8A80" if is_dark else "#D32F2F"
blue_text = "#82B1FF" if is_dark else "#1976D2"
temp_text = "#FFAB40" if is_dark else "#E65100"

hero_bg_rule = (
    "linear-gradient(rgba(15, 22, 14, 0.56), rgba(15, 22, 14, 0.68)), url('" + HERO_IMG_URI + "')"
    if HERO_IMG_URI
    else "linear-gradient(135deg, #2E7D32 0%, #558B2F 50%, #8D6E63 100%)"
)

market_bg_rule = (
    "linear-gradient(rgba(15, 22, 14, 0.58), rgba(15, 22, 14, 0.72)), url('" + UGLY_MARKET_IMG_URI + "')"
    if UGLY_MARKET_IMG_URI
    else "linear-gradient(135deg, #2E7D32 0%, #33691E 100%)"
)

css = (
    "<style>"
    "@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600;700&display=swap');"
    ".stApp, [data-testid='stAppViewContainer'] { background-color: " + app_bg + " !important; font-family: 'Noto Sans KR', sans-serif; }"
    "[data-testid='stHeader'] { background: transparent !important; height: 0px !important; min-height: 0px !important; pointer-events: none !important; z-index: 1 !important; }"
    "[data-testid='stToolbar'] { pointer-events: none !important; }"
    ".block-container { max-width: 97% !important; padding-left: 1.5rem !important; padding-right: 1.5rem !important; padding-top: 1.4rem !important; padding-bottom: 3rem !important; position: relative; z-index: 10; }"
    ".stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp label, [data-testid='stMarkdownContainer'] p { color: " + text_main + " !important; }"
    ".brand-logo { font-family: 'Jua', sans-serif !important; font-size: 26px !important; color: " + primary_green + " !important; letter-spacing: -0.5px; }"
    ".brand-sub { font-size: 12px !important; color: " + text_sub + " !important; margin-left: 6px; }"
    ".side-panel { background-color: " + side_bg + "; border: 1.5px solid " + border_subtle + "; border-radius: 0px; padding: 16px; margin-bottom: 14px; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }"
    ".side-panel * { color: " + text_main + " !important; }"
    ".side-title { font-family: 'Jua', sans-serif !important; font-size: 18px !important; color: " + primary_green + " !important; border-bottom: 2px solid " + primary_green + "; padding-bottom: 6px; margin-bottom: 12px; }"
    ".side-item { border-bottom: 1px dashed " + border_subtle + "; padding: 8px 0; font-size: 13px; line-height: 1.55; }"
    ".side-item:last-child { border-bottom: none; padding-bottom: 0; }"
    ".stat-row { display: flex; justify-content: space-between; gap: 6px; margin-top: 6px; }"
    ".stat-box { flex: 1; border: 1px solid " + border_subtle + "; padding: 10px 6px; text-align: center; background-color: " + app_bg + "; }"
    ".stat-num { font-family: 'Jua', sans-serif; font-size: 20px; color: " + primary_green + " !important; }"
    ".stat-lbl { font-size: 11.5px; color: " + text_sub + " !important; }"
    "[data-testid='stMarkdownContainer'] .hero-banner { background-image: " + hero_bg_rule + "; background-size: cover; background-position: center; border-radius: 0px; border: 2px solid " + primary_green + "; padding: 34px 28px; text-align: center; margin-bottom: 18px; box-shadow: 0px 8px 20px rgba(0,0,0,0.2); }"
    "[data-testid='stMarkdownContainer'] .hero-banner, [data-testid='stMarkdownContainer'] .hero-banner *, [data-testid='stMarkdownContainer'] .hero-banner p, [data-testid='stMarkdownContainer'] .hero-banner h1, [data-testid='stMarkdownContainer'] .hero-banner div, [data-testid='stMarkdownContainer'] .hero-banner span { color: #FFFFFF !important; }"
    ".hero-pill { display: inline-block; background-color: rgba(24, 78, 119, 0.96) !important; color: #FFFFFF !important; font-family: 'Jua', sans-serif; font-size: 14px; padding: 6px 18px; border-radius: 0px; border: 1px solid rgba(255,255,255,0.45); margin-bottom: 12px; }"
    ".hero-potato-wrap { display: flex; justify-content: center; align-items: center; margin: 0 auto 8px auto; }"
    ".hero-potato-img { width: 112px; height: 112px; object-fit: contain; filter: drop-shadow(0px 6px 12px rgba(0,0,0,0.6)); }"
    "[data-testid='stMarkdownContainer'] .hero-banner .hero-title { font-family: 'Jua', sans-serif !important; font-size: clamp(32px, 4vw, 48px) !important; color: #FFFFFF !important; margin: 0 0 10px 0 !important; line-height: 1.15; text-shadow: 0px 3px 14px rgba(0,0,0,0.85), 0px 1px 3px rgba(0,0,0,0.95); }"
    "[data-testid='stMarkdownContainer'] .hero-banner .hero-desc { font-size: 15.5px !important; font-weight: 600 !important; color: #FFFFFF !important; margin: 0 auto 4px auto !important; max-width: 640px; line-height: 1.6; text-shadow: 0px 2px 10px rgba(0,0,0,0.9), 0px 1px 3px rgba(0,0,0,0.95); word-break: keep-all; }"
    ".sec-header { text-align: center; margin: 16px 0 14px 0; }"
    ".sec-title { font-family: 'Jua', sans-serif !important; font-size: 25px !important; color: " + text_main + " !important; margin-bottom: 4px !important; }"
    ".sec-sub { font-size: 13.5px !important; color: " + text_sub + " !important; }"
    ".portal-card { background-color: " + card_bg + "; border: 1.5px solid " + border_subtle + "; border-radius: 0px; padding: 0px 0px 14px 0px; text-align: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.06); margin-bottom: 8px; overflow: hidden; }"
    ".portal-card * { color: " + text_main + " !important; }"
    ".card-hero-img-wrap { position: relative; width: 100%; height: 175px; overflow: hidden; border-bottom: 2px solid " + primary_green + "; margin-bottom: 10px; background-color: #E8F5E9; }"
    ".card-hero-img { width: 100%; height: 100%; object-fit: cover; display: block; }"
    ".card-img-label { position: absolute; top: 8px; left: 8px; background-color: rgba(20, 28, 18, 0.82) !important; color: #FFFFFF !important; font-family: 'Jua', sans-serif; font-size: 13px; padding: 3px 10px; border-radius: 0px; }"
    ".card-body-pad { padding: 0 12px; }"
    ".card-badge-go { display: inline-block; background-color: " + accent_orange + " !important; color: #FFFFFF !important; font-family: 'Jua', sans-serif; font-size: 12px; padding: 3px 9px; border-radius: 0px; margin-bottom: 5px; }"
    ".tag-level { display: inline-block; background-color: #184E77 !important; color: #FFFFFF !important; font-size: 11px; font-weight: 700; padding: 2px 7px; margin: 2px; }"
    ".tag-meal { display: inline-block; background-color: #2E7D32 !important; color: #FFFFFF !important; font-size: 11px; font-weight: 700; padding: 2px 7px; margin: 2px; }"
    ".tag-reason { display: inline-block; background-color: #6D4C41 !important; color: #FFFFFF !important; font-size: 11px; font-weight: 700; padding: 2px 8px; margin-bottom: 6px; }"
    "[data-testid='stMarkdownContainer'] .market-banner { background-image: " + market_bg_rule + "; background-size: cover; background-position: center; border: 2px solid " + primary_green + "; border-radius: 0px; padding: 36px 28px; margin-bottom: 20px; text-align: center; box-shadow: 0px 8px 20px rgba(0,0,0,0.18); }"
    "[data-testid='stMarkdownContainer'] .market-banner, [data-testid='stMarkdownContainer'] .market-banner *, [data-testid='stMarkdownContainer'] .market-banner div, [data-testid='stMarkdownContainer'] .market-banner span { color: #FFFFFF !important; }"
    ".market-title-txt { font-family: 'Jua', sans-serif !important; font-size: clamp(28px, 4vw, 40px) !important; color: #FFFFFF !important; margin-bottom: 8px; text-shadow: 0px 3px 12px rgba(0,0,0,0.85); }"
    ".market-sub-txt { font-size: 16px !important; font-weight: 600 !important; color: #FFFFFF !important; line-height: 1.65; text-shadow: 0px 2px 10px rgba(0,0,0,0.9); word-break: keep-all; }"
    ".market-tag { display: inline-block; background-color: #2E7D32 !important; color: #FFFFFF !important; font-family: 'Jua', sans-serif; font-size: 12px; padding: 3px 10px; border-radius: 0px; margin-bottom: 6px; }"
    ".txt-green { color: " + primary_green + " !important; font-weight: 700; }"
    ".txt-temp { color: " + temp_text + " !important; font-weight: 700; font-size: 12px; }"
    ".txt-strike { text-decoration: line-through; opacity: 0.6; font-size: 13px; margin-right: 6px; }"
    ".banner-text { font-family: 'Jua', sans-serif; border: 2px dashed " + primary_green + "; background-color: " + card_bg + "; padding: 12px; border-radius: 0px; color: " + primary_green + " !important; font-size: 19px; text-align: center; margin-bottom: 16px; }"
    ".detail-card { background-color: " + card_bg + "; border: 1.5px solid " + border_subtle + "; padding: 22px; border-radius: 0px; margin-top: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.07); }"
    ".detail-card * { color: " + text_main + " !important; }"
    ".shuttle-text { font-size: 12.5px; font-weight: 600; margin-top: 8px; border-top: 1px dashed " + border_subtle + "; padding-top: 7px; color: " + text_sub + " !important; }"
    ".red-text { color: " + red_text + " !important; font-weight: bold; text-align: center; font-size: 20px; margin: 14px 0; line-height: 1.5; }"
    ".blue-notice { color: " + blue_text + " !important; font-size: 14px; text-align: center; margin-top: 8px; font-weight: bold; }"
    ".ticket-box { background-color: " + card_bg + "; border: 2px solid " + primary_green + "; border-radius: 0px; padding: 20px; margin-top: 14px; border-left: 16px solid " + primary_green + "; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }"
    ".ticket-box * { color: " + text_main + " !important; }"
    ".stButton, .stFormSubmitButton { position: relative; z-index: 50; }"
    "button[kind='secondary'], button[kind='primary'], .stButton > button, .stFormSubmitButton > button { background-color: " + btn_bg + " !important; color: " + btn_text + " !important; border: 1.5px solid " + border_subtle + " !important; border-radius: 0px !important; min-height: 44px !important; padding: 8px 14px !important; cursor: pointer !important; position: relative; z-index: 50; }"
    "button[kind='secondary'] *, button[kind='primary'] *, .stButton > button *, .stFormSubmitButton > button * { color: " + btn_text + " !important; pointer-events: none !important; }"
    "button[kind='secondary']:hover, button[kind='primary']:hover, .stButton > button:hover, .stFormSubmitButton > button:hover { background-color: " + btn_hover_bg + " !important; color: " + btn_hover_text + " !important; border-color: " + primary_green + " !important; }"
    "button[kind='secondary']:hover *, button[kind='primary']:hover *, .stButton > button:hover *, .stFormSubmitButton > button:hover * { color: " + btn_hover_text + " !important; pointer-events: none !important; }"
    "[data-testid='stForm'] { border-radius: 0px !important; border: 1.5px solid " + border_subtle + " !important; background-color: " + card_bg + " !important; }"
    "input, select, textarea, [data-baseweb='input'], [data-baseweb='select'] > div { border-radius: 0px !important; }"
    ".st-key-hero_resident button { background-color: #3949AB !important; border: none !important; height: 52px !important; border-radius: 0px !important; box-shadow: 0px 4px 12px rgba(0,0,0,0.22) !important; }"
    ".st-key-hero_resident button * { color: #FFFFFF !important; font-family: 'Jua', sans-serif !important; font-size: 18px !important; pointer-events: none !important; }"
    ".st-key-hero_student button { background-color: #F57C00 !important; border: none !important; height: 52px !important; border-radius: 0px !important; box-shadow: 0px 4px 12px rgba(0,0,0,0.22) !important; }"
    ".st-key-hero_student button * { color: #FFFFFF !important; font-family: 'Jua', sans-serif !important; font-size: 18px !important; pointer-events: none !important; }"
    ".st-key-hero_market button { background-color: #2E7D32 !important; border: none !important; height: 52px !important; border-radius: 0px !important; box-shadow: 0px 4px 12px rgba(0,0,0,0.22) !important; }"
    ".st-key-hero_market button * { color: #FFFFFF !important; font-family: 'Jua', sans-serif !important; font-size: 18px !important; pointer-events: none !important; }"
    "</style>"
)
st.markdown(css, unsafe_allow_html=True)

@st.cache_resource
def get_shared_jobs():
    return [
        {
            "id": 1, "village": "춘천시 신북읍", "job_type": "감자 수확", "icon": "🥔",
            "work_date": date.today() + timedelta(days=2), "wage": "100,000",
            "req_people": 4, "current_apply": 2, "photo_b64": None,
            "temp": "38.5°C", "weather": "☀️ 맑음 (최고 22도)",
            "difficulty": "중 (허리 숙여 수확·선별)",
            "supplies": "장화, 목장갑, 모자, 긴팔·긴바지",
            "meal": "점심식사 + 새참 제공",
            "shuttle_time": "07:30 출발 (07:20 집합)",
            "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
            "contact": "신북읍 이장 김철수 (010-2345-6789)"
        },
        {
            "id": 2, "village": "홍천군 서면", "job_type": "옥수수 수확", "icon": "🌽",
            "work_date": date.today() + timedelta(days=3), "wage": "90,000",
            "req_people": 2, "current_apply": 2, "photo_b64": None,
            "temp": "36.5°C", "weather": "☁️ 흐림 (최고 18도)",
            "difficulty": "하 (초보자 가능·가벼운 수확)",
            "supplies": "운동화, 팔토시, 모자, 개인 물병",
            "meal": "점심식사 + 옥수수 간식",
            "shuttle_time": "07:40 출발 (07:30 집합)",
            "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
            "contact": "홍천 서면 이장 박영희 (010-3456-7890)"
        },
        {
            "id": 3, "village": "춘천시 동면", "job_type": "비료 운반", "icon": "🚜",
            "work_date": date.today() + timedelta(days=4), "wage": "120,000",
            "req_people": 3, "current_apply": 1, "photo_b64": None,
            "temp": "40.2°C", "weather": "⛅ 구름 조금 (최고 20도)",
            "difficulty": "상 (20kg 포대 이동·체력 우대)",
            "supplies": "안전화/튼튼한 운동화, 코팅장갑, 여벌 옷",
            "meal": "점심식사 + 음료·간식 제공",
            "shuttle_time": "07:30 출발 (07:20 집합)",
            "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
            "contact": "동면 영농회장 이민수 (010-4567-8901)"
        },
        {
            "id": 4, "village": "화천군 하남면", "job_type": "잡초 제거", "icon": "🌱",
            "work_date": date.today() + timedelta(days=5), "wage": "85,000",
            "req_people": 5, "current_apply": 0, "photo_b64": None,
            "temp": "37.0°C", "weather": "☀️ 맑음 (최고 25도)",
            "difficulty": "하 (밭고랑 제초·초보자 환영)",
            "supplies": "모자, 목장갑, 편한 작업복, 선크림",
            "meal": "점심식사 제공",
            "shuttle_time": "07:20 출발 (07:10 집합)",
            "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
            "contact": "하남면 이장 최성호 (010-5678-9012)"
        },
        {
            "id": 5, "village": "양구군 남면", "job_type": "김장 배추", "icon": "🥬",
            "work_date": date.today() + timedelta(days=6), "wage": "110,000",
            "req_people": 6, "current_apply": 2, "photo_b64": None,
            "temp": "39.1°C", "weather": "☀️ 맑음 (최고 15도)",
            "difficulty": "중 (배추 수확 및 망 포장)",
            "supplies": "방수 장화, 고무코팅 장갑, 따뜻한 겉옷",
            "meal": "점심식사 + 수육·새참 제공",
            "shuttle_time": "07:10 출발 (07:00 집합)",
            "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
            "contact": "양구 남면 이장 정수진 (010-6789-0123)"
        },
    ]

@st.cache_resource
def get_ugly_products():
    return [
        {"id": 1, "farm": "춘천시 신북읍 햇살농가", "title": "못난이 수미감자 5kg", "icon": "🥔", "reason": "쌍둥이·울퉁불퉁 기형", "orig_price": "18,000", "sale_price": "9,500", "discount": "47% 할인", "desc": "모양은 울퉁불퉁하지만 포슬포슬하고 고소한 햇수미감자입니다.", "stock": 12},
        {"id": 2, "farm": "홍천군 서면 산골농원", "title": "B급 찰옥수수 15개입", "icon": "🌽", "reason": "크기·길이 편차", "orig_price": "22,000", "sale_price": "11,000", "discount": "50% 할인", "desc": "크기가 조금씩 다르지만 쫀득하고 당도가 뛰어난 홍천 찰옥수수!", "stock": 8},
        {"id": 3, "farm": "양구군 남면 고랭지밭", "title": "흠집 고랭지 사과 3kg", "icon": "🍎", "reason": "나뭇가지 표면 흠집", "orig_price": "25,000", "sale_price": "13,500", "discount": "46% 할인", "desc": "가지에 살짝 스친 자국이 있지만 아삭하고 꿀이 꽉 찬 고랭지 사과입니다.", "stock": 10},
        {"id": 4, "farm": "춘천시 동면 푸른농장", "title": "못난이 당근·양파 꾸러미 4kg", "icon": "🥕", "reason": "갈라짐·껍질 변색", "orig_price": "16,000", "sale_price": "8,000", "discount": "50% 할인", "desc": "자취생 카레·볶음밥용으로 딱 좋은 싱싱한 B급 채소 모음!", "stock": 15},
    ]

SHARED_JOBS = get_shared_jobs()
UGLY_PRODUCTS = get_ugly_products()

if 'page' not in st.session_state: st.session_state['page'] = 'home'
if 'selected_job_id' not in st.session_state: st.session_state['selected_job_id'] = None
if 'student_verified' not in st.session_state: st.session_state['student_verified'] = False
if 'student_profile' not in st.session_state:
    st.session_state['student_profile'] = {"name": "", "school": "", "student_id": ""}
if 'redirect_after_student_login' not in st.session_state: st.session_state['redirect_after_student_login'] = 'student_list'
if 'current_page' not in st.session_state: st.session_state['current_page'] = 1
if 'filter_type' not in st.session_state: st.session_state['filter_type'] = "전체보기"
if 'my_applications' not in st.session_state: st.session_state['my_applications'] = []
if 'my_market_orders' not in st.session_state: st.session_state['my_market_orders'] = []
if 'banner_msg' not in st.session_state:
    st.session_state['banner_msg'] = random.choice(["오늘 단기알바 어때요? 🥔", "공강 시간에 쏠쏠하게 벌어가세요! 💸", "주말 농촌 꿀알바 어때요? 🚌"])

def navigate_to(page_name):
    st.session_state['page'] = page_name

nav_c1, nav_c2, nav_c3, nav_c4, nav_c5, nav_c6, nav_c7 = st.columns([2.3, 0.8, 0.95, 0.95, 1.1, 1.0, 0.85])
with nav_c1:
    logo_prefix = (
        "<img src='" + POTATO_IMG_URI + "' style='width:28px; height:28px; object-fit:contain; vertical-align:middle; margin-right:6px;'/>"
        if POTATO_IMG_URI
        else "🥔 "
    )
    st.markdown(
        "<div style='padding-top:4px;'>"
        + logo_prefix +
        "<span class='brand-logo'>po-work</span>"
        "<span class='brand-sub'>강원대학교 × 지역농가 상생 일손·직거래 포털</span>"
        "</div>",
        unsafe_allow_html=True,
    )
with nav_c2:
    if st.button("🏠 홈", key="nav_home", use_container_width=True):
        navigate_to('home')
        st.rerun()
with nav_c3:
    if st.button("🏡 주민등록", key="nav_res", use_container_width=True):
        navigate_to('resident_login')
        st.rerun()
with nav_c4:
    if st.button("🎓 알바찾기", key="nav_stu", use_container_width=True):
        st.session_state['redirect_after_student_login'] = 'student_list'
        navigate_to('student_login')
        st.rerun()
with nav_c5:
    if st.button("🥕 못난이마켓", key="nav_market", use_container_width=True):
        navigate_to('ugly_market')
        st.rerun()
with nav_c6:
    my_cnt = len(st.session_state['my_applications']) + len(st.session_state['my_market_orders'])
    if st.button(f"📋 내활동({my_cnt})", key="nav_my", use_container_width=True):
        navigate_to('my_page')
        st.rerun()
with nav_c7:
    t_label = "🌙 다크" if not is_dark else "☀️ 라이트"
    if st.button(t_label, key="nav_theme", use_container_width=True):
        toggle_theme()
        st.rerun()

if st.session_state['page'] == 'home':
    left_col, center_col, right_col = st.columns([1.05, 2.9, 1.05])

    with left_col:
        open_jobs_cnt = sum(1 for j in SHARED_JOBS if j['current_apply'] < j['req_people'])
        total_spots_left = sum(max(0, j['req_people'] - j['current_apply']) for j in SHARED_JOBS)
        st.markdown(
            "<div class='side-panel'>"
            "<div class='side-title'>📊 실시간 매칭 현황</div>"
            "<div class='stat-row'>"
            "<div class='stat-box'><div class='stat-num'>" + str(open_jobs_cnt) + "건</div><div class='stat-lbl'>모집 중 공고</div></div>"
            "<div class='stat-box'><div class='stat-num'>" + str(total_spots_left) + "명</div><div class='stat-lbl'>잔여 인원</div></div>"
            "</div>"
            "<div class='stat-row'>"
            "<div class='stat-box'><div class='stat-num'>" + str(len(UGLY_PRODUCTS)) + "종</div><div class='stat-lbl'>B급 특가작물</div></div>"
            "<div class='stat-box'><div class='stat-num'>무료</div><div class='stat-lbl'>강원대 셔틀</div></div>"
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

        shuttle_rows = ""
        for j in SHARED_JOBS[:4]:
            shuttle_rows += (
                "<div class='side-item'>"
                "<b>🚌 " + str(j['village']) + " (" + str(j['job_type']) + ")</b><br>"
                "⏰ " + str(j['shuttle_time']) + "<br>"
                "📍 " + str(j['shuttle_stop']) +
                "</div>"
            )
        st.markdown(
            "<div class='side-panel'>"
            "<div class='side-title'>🚌 강원대 후문 셔틀 안내</div>"
            + shuttle_rows +
            "<div style='font-size:11.5px; margin-top:8px; opacity:0.85;'>* 출발 10분 전 집결 필수 · 지각 시 정시 출발</div>"
            "</div>",
            unsafe_allow_html=True,
        )

    with center_col:
        potato_hero_html = (
            "<div class='hero-potato-wrap'><img class='hero-potato-img' src='" + POTATO_IMG_URI + "' alt='po-work 감자 캐릭터'/></div>"
            if POTATO_IMG_URI
            else "<div style='font-size: 72px; margin-bottom: 8px;'>🥔</div>"
        )

        st.markdown(
            "<div class='hero-banner'>"
            "<div class='hero-pill'>🎓 강원대학교 × 지역 농가 상생 협업 프로젝트</div>"
            + potato_hero_html +
            "<h1 class='hero-title'>po-work · 강원 농촌 일손 매칭</h1>"
            "<div class='hero-desc'>공강·주말 하루 단기 알바부터 강원대 후문 전용 셔틀, 못난이 농산물 직거래까지!<br>"
            "우리 지역 농가와 대학생을 가장 빠르고 따뜻하게 연결합니다.</div>"
            "</div>",
            unsafe_allow_html=True,
        )

        cta_res, cta_stu, cta_mkt = st.columns(3)
        with cta_res:
            if st.button("🏡 주민 일손요청", key="hero_resident", use_container_width=True):
                navigate_to('resident_login')
                st.rerun()
        with cta_stu:
            if st.button("🎓 대학생 알바신청", key="hero_student", use_container_width=True):
                st.session_state['redirect_after_student_login'] = 'student_list'
                navigate_to('student_login')
                st.rerun()
        with cta_mkt:
            if st.button("🥕 못난이 마켓", key="hero_market", use_container_width=True):
                navigate_to('ugly_market')
                st.rerun()

        st.markdown(
            "<div class='sec-header'>"
            "<h2 class='sec-title'>📢 지금 모집 중인 추천 농촌 일손</h2>"
            "<p class='sec-sub'>작물별 현장 사진과 작업 강도·식사 여부를 확인하고 상세정보를 눌러 신청하세요</p>"
            "</div>",
            unsafe_allow_html=True,
        )

        latest_jobs = list(reversed(SHARED_JOBS))[:4]
        cols = st.columns(len(latest_jobs))
        for idx, job in enumerate(latest_jobs):
            with cols[idx]:
                crop_img_src = resolve_crop_image(job['job_type'], job.get('photo_b64'))
                status_txt = "마감" if job['current_apply'] >= job['req_people'] else f"모집 {job['current_apply']}/{job['req_people']}명"
                diff_short = str(job.get('difficulty', '중')).split()[0]

                card_html = (
                    "<div class='portal-card'>"
                    "<div class='card-hero-img-wrap'>"
                    "<img class='card-hero-img' src='" + crop_img_src + "' alt='" + str(job['job_type']) + "'/>"
                    "<span class='card-img-label'>" + job.get('icon', '🥔') + " " + str(job['job_type']) + "</span>"
                    "</div>"
                    "<div class='card-body-pad'>"
                    "<span class='card-badge-go'>" + status_txt + "</span><br>"
                    "<span class='tag-level'>강도 " + diff_short + "</span>"
                    "<span class='tag-meal'>식사제공</span>"
                    "<div style='font-family:\"Jua\",sans-serif; font-size:18px; margin:6px 0 4px 0;'>" + str(job['job_type']) + "</div>"
                    "<div style='font-size:12.5px; margin-bottom:3px;'>📍 " + str(job['village']) + "</div>"
                    "<div style='font-size:12px; opacity:0.85; margin-bottom:5px;'>📅 " + str(job['work_date']) + "</div>"
                    "<div class='txt-green' style='font-size:15px;'>일당 " + str(job['wage']) + "원</div>"
                    "</div>"
                    "</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)
                if job['current_apply'] >= job['req_people']:
                    st.button("모집 마감", key=f"home_card_{job['id']}", disabled=True, use_container_width=True)
                else:
                    if st.button("상세정보 ➔", key=f"home_card_{job['id']}", use_container_width=True):
                        st.session_state['selected_job_id'] = job['id']
                        st.session_state['redirect_after_student_login'] = 'student_detail'
                        navigate_to('student_login')
                        st.rerun()

    with right_col:
        apps = st.session_state['my_applications']
        orders = st.session_state['my_market_orders']
        if len(apps) == 0 and len(orders) == 0:
            my_summary_html = (
                "<div class='side-item'>아직 신청한 일손이나 마켓 예약 내역이 없습니다.<br>"
                "공고를 선택해 바로 참여해 보세요!</div>"
            )
        else:
            my_summary_html = ""
            for a in apps[-2:]:
                my_summary_html += (
                    "<div class='side-item'>"
                    "🎓 <b>" + str(a['job_type']) + "</b> (" + str(a['apply_count']) + "명)<br>"
                    "📅 " + str(a['work_date']) + " · " + str(a['shuttle_time']) +
                    "</div>"
                )
            for o in orders[-2:]:
                my_summary_html += (
                    "<div class='side-item'>"
                    "🥕 <b>" + str(o['title']) + "</b><br>"
                    "💰 " + str(o['sale_price']) + "원 (직거래 예약)"
                    "</div>"
                )

        st.markdown(
            "<div class='side-panel'>"
            "<div class='side-title'>📋 내 신청 · 예약 현황</div>"
            + my_summary_html +
            "</div>",
            unsafe_allow_html=True,
        )
        if st.button("내 활동 전체보기 ➔", key="side_my_btn", use_container_width=True):
            navigate_to('my_page')
            st.rerun()

        mkt_preview = ""
        for p in UGLY_PRODUCTS[:3]:
            mkt_preview += (
                "<div class='side-item'>"
                + p['icon'] + " <b>" + p['title'] + "</b> <span class='txt-green'>" + p['sale_price'] + "원</span><br>"
                "<span style='font-size:11.5px; opacity:0.85;'>사유: " + p['reason'] + " · " + p['discount'] + "</span>"
                "</div>"
            )
        st.markdown(
            "<div class='side-panel' style='margin-top:12px;'>"
            "<div class='side-title'>🥕 못난이 마켓 오늘 특가</div>"
            + mkt_preview +
            "</div>",
            unsafe_allow_html=True,
        )
        if st.button("못난이 마켓 가기 ➔", key="side_mkt_btn", use_container_width=True):
            navigate_to('ugly_market')
            st.rerun()

elif st.session_state['page'] == 'ugly_market':
    st.markdown(
        "<div class='market-banner'>"
        "<div class='hero-pill'>🥕 지역 농가 못난이(B급) 농산물 직거래</div>"
        "<div class='market-title-txt'>po-work 못난이 마켓</div>"
        "<div class='market-sub-txt'>못나지만 맛은 훌륭한 B급 농작물들을 싼 값에 가져가세요!<br>"
        "재배 중 모양이나 크기 차이로 밀려난 싱싱한 지역 농작물을 합리적인 가격에 만나보세요.</div>"
        "</div>",
        unsafe_allow_html=True,
    )

    tab_buy, tab_sell = st.tabs(["🛒 못난이 농작물 둘러보기", "🌾 농가 B급 농작물 등록하기"])

    with tab_buy:
        m_cols = st.columns(4)
        for idx, item in enumerate(UGLY_PRODUCTS):
            with m_cols[idx % 4]:
                prod_img_src = resolve_crop_image(item['title'], item.get('photo_b64'))
                item_html = (
                    "<div class='portal-card'>"
                    "<div class='card-hero-img-wrap'>"
                    "<img class='card-hero-img' src='" + prod_img_src + "' alt='" + str(item['title']) + "'/>"
                    "<span class='card-img-label'>" + item.get('icon', '🥔') + " " + str(item['discount']) + "</span>"
                    "</div>"
                    "<div class='card-body-pad'>"
                    "<span class='tag-reason'>B급 사유: " + str(item.get('reason', '모양 편차')) + "</span>"
                    "<div style='font-family:\"Jua\",sans-serif; font-size:18px; margin-bottom:4px;'>" + str(item['title']) + "</div>"
                    "<div style='font-size:12.5px; margin-bottom:6px;'>🏡 " + str(item['farm']) + "</div>"
                    "<div style='font-size:12.5px; line-height:1.45; min-height:54px; margin-bottom:8px;'>" + str(item['desc']) + "</div>"
                    "<div><span class='txt-strike'>" + str(item['orig_price']) + "원</span><span class='txt-green' style='font-size:17px;'>" + str(item['sale_price']) + "원</span></div>"
                    "<div style='font-size:12px; margin-top:4px;'>남은 수량: " + str(item['stock']) + "박스</div>"
                    "</div>"
                    "</div>"
                )
                st.markdown(item_html, unsafe_allow_html=True)
                if item['stock'] <= 0:
                    st.button("품절", key=f"mkt_buy_{item['id']}", disabled=True, use_container_width=True)
                else:
                    if st.button("직거래 예약하기", key=f"mkt_buy_{item['id']}", use_container_width=True):
                        item['stock'] -= 1
                        st.session_state['my_market_orders'].append({
                            "title": item['title'],
                            "farm": item['farm'],
                            "sale_price": item['sale_price'],
                            "reason": item.get('reason', '모양 편차'),
                            "pickup": "강원대 후문 셔틀 하차장 수령 / 산지 직배송",
                            "order_date": str(date.today()),
                        })
                        st.toast(f"✅ [{item['title']}] 직거래 예약 완료! '내활동'에서 예약 내역을 확인할 수 있습니다.", icon="🥕")
                        st.rerun()

    with tab_sell:
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m:
            st.write("📝 **농가 못난이(B급) 농작물 판매 등록**")
            with st.form("ugly_product_form"):
                farm_name = st.text_input("농가명 / 지역", placeholder="예: 춘천시 신북읍 감자농가")
                prod_title = st.text_input("작물명 및 중량", placeholder="예: 못난이 고구마 5kg")
                prod_icon = st.selectbox("작물 분류", ["🥔 감자", "🍠 고구마", "🥕 당근", "🌽 옥수수", "🍎 사과", "🥬 배추/엽채류"])
                reason_opt = st.selectbox("B급 사유 (구매자 신뢰 표시용)", ["쌍둥이·울퉁불퉁 기형", "크기·길이 편차", "나뭇가지 표면 흠집", "껍질 변색·얼룩", "기타 외관 편차"])
                orig_p = st.text_input("시중 정상가 (원)", placeholder="예: 18,000")
                sale_p = st.text_input("못난이 특가 (원)", placeholder="예: 9,000")
                stock_cnt = st.number_input("판매 가능 수량 (박스)", min_value=1, value=10)
                prod_photo = st.file_uploader("작물 실물 사진 첨부 (선택)", type=["png", "jpg", "jpeg"])
                prod_desc = st.text_area("작물 소개", value="못나지만 맛은 훌륭한 B급 농작물입니다. 싱싱하게 수확해 보내드려요!")

                if st.form_submit_button("못난이 마켓에 등록하기 ✨", use_container_width=True):
                    p_b64 = base64.b64encode(prod_photo.getvalue()).decode("utf-8") if prod_photo else None
                    new_item = {
                        "id": len(UGLY_PRODUCTS) + 1,
                        "farm": farm_name if farm_name else "강원 지역 농가",
                        "title": prod_title if prod_title else f"못난이 {prod_icon.split()[1]} 5kg",
                        "icon": prod_icon.split()[0],
                        "reason": reason_opt,
                        "orig_price": orig_p if orig_p else "15,000",
                        "sale_price": sale_p if sale_p else "8,000",
                        "discount": "산지특가",
                        "desc": prod_desc,
                        "stock": stock_cnt,
                        "photo_b64": p_b64,
                    }
                    UGLY_PRODUCTS.insert(0, new_item)
                    st.success("못난이 마켓에 상품이 등록되었습니다!")
                    st.rerun()

elif st.session_state['page'] == 'my_page':
    st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>📋 내 활동 (신청 · 예약 내역)</h1>", unsafe_allow_html=True)
    prof = st.session_state['student_profile']
    user_label = prof['name'] if prof['name'] else "인증 대학생"
    school_label = f"{prof['school']} · 학번 {prof['student_id']}" if (prof['school'] or prof['student_id']) else "학교 인증 완료"
    st.info(f"👤 인증 사용자: **{user_label}** ({school_label})")

    c_left, c_right = st.columns(2)
    with c_left:
        st.markdown("<h3 style='font-family:\"Jua\",sans-serif;'>🎓 신청한 농촌 일손 &amp; 셔틀 탑승권</h3>", unsafe_allow_html=True)
        if len(st.session_state['my_applications']) == 0:
            st.warning("아직 신청한 농촌 일손 내역이 없습니다.")
            if st.button("알바 공고 보러가기 ➔", key="my_go_jobs", use_container_width=True):
                navigate_to('student_list')
                st.rerun()
        else:
            for idx, app in enumerate(reversed(st.session_state['my_applications'])):
                ticket_html = (
                    "<div class='ticket-box'>"
                    "<h4 style='margin-top:0; border-bottom: 2px dashed " + border_subtle + "; padding-bottom: 8px;'><span class='txt-green'>🚌 po-work 셔틀 탑승권 #" + str(len(st.session_state['my_applications']) - idx) + "</span></h4>"
                    "<p style='font-size: 14px; line-height: 1.75; margin-bottom: 0;'>"
                    "<b>작업명 :</b> " + str(app['village']) + " (" + str(app['job_type']) + ")<br>"
                    "<b>작업일 :</b> " + str(app['work_date']) + " (일당 " + str(app['wage']) + "원)<br>"
                    "<b>셔틀출발 :</b> " + str(app['shuttle_time']) + "<br>"
                    "<b>탑승위치 :</b> " + str(app['shuttle_stop']) + "<br>"
                    "<b>신청인원 :</b> 총 " + str(app['apply_count']) + "명<br>"
                    "<b>현장연락처 :</b> " + str(app['contact']) +
                    "</p>"
                    "</div>"
                )
                st.markdown(ticket_html, unsafe_allow_html=True)
                if st.button(f"📍 탑승 완료 알림 보내기 ({app['village']})", key=f"my_board_{idx}", use_container_width=True):
                    st.toast(f"✅ {app['contact']} 앞으로 '{app['apply_count']}명 탑승 완료' 알림이 전송되었습니다!", icon="🚌")

    with c_right:
        st.markdown("<h3 style='font-family:\"Jua\",sans-serif;'>🥕 못난이 마켓 직거래 예약 내역</h3>", unsafe_allow_html=True)
        if len(st.session_state['my_market_orders']) == 0:
            st.warning("아직 예약한 못난이 농산물이 없습니다.")
            if st.button("못난이 마켓 구경가기 ➔", key="my_go_mkt", use_container_width=True):
                navigate_to('ugly_market')
                st.rerun()
        else:
            for idx, ord_item in enumerate(reversed(st.session_state['my_market_orders'])):
                ord_html = (
                    "<div class='detail-card'>"
                    "<div style='font-family:\"Jua\",sans-serif; font-size:18px; margin-bottom:6px;'>🥕 " + str(ord_item['title']) + "</div>"
                    "<div style='font-size:14px; line-height:1.7;'>"
                    "<b>판매농가 :</b> " + str(ord_item['farm']) + "<br>"
                    "<b>B급 사유 :</b> " + str(ord_item['reason']) + "<br>"
                    "<b>결제예정가 :</b> <span class='txt-green'>" + str(ord_item['sale_price']) + "원</span><br>"
                    "<b>수령방식 :</b> " + str(ord_item['pickup']) + "<br>"
                    "<b>예약일자 :</b> " + str(ord_item['order_date']) +
                    "</div>"
                    "</div>"
                )
                st.markdown(ord_html, unsafe_allow_html=True)

elif st.session_state['page'] == 'resident_login':
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>주민 로그인 🏡</h1>", unsafe_allow_html=True)
        with st.form("resident_login_form"):
            st.write("안전한 일손 매칭을 위해 마을 인증을 진행합니다.")
            st.text_input("성함", placeholder="예: 홍길동")
            st.text_input("휴대전화 번호", placeholder="예: 010-1234-5678")
            st.text_input("거주 마을 / 지역", placeholder="예: 춘천시 신북읍")
            if st.form_submit_button("인증하고 시작하기", use_container_width=True):
                navigate_to('resident')
                st.rerun()
        if st.button("⬅️ 처음 화면으로", use_container_width=True):
            navigate_to('home')
            st.rerun()

elif st.session_state['page'] == 'student_login':
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>대학생 학교 인증 🎓</h1>", unsafe_allow_html=True)
        if st.session_state.get('redirect_after_student_login') == 'student_detail' and st.session_state.get('selected_job_id'):
            target_job = next((j for j in SHARED_JOBS if j['id'] == st.session_state['selected_job_id']), None)
            if target_job:
                st.info(f"선택하신 [{target_job['village']} · {target_job['job_type']}] 상세정보를 보려면 학교 인증을 먼저 완료해 주세요.")

        with st.form("student_login_form"):
            st.write("안전한 매칭을 위해 대학교 학생 인증을 진행합니다.")
            in_name = st.text_input("이름", value=st.session_state['student_profile']['name'], placeholder="예: 홍길동")
            in_school = st.text_input("학교명", value=st.session_state['student_profile']['school'], placeholder="예: 강원대학교")
            in_sid = st.text_input("학번", value=st.session_state['student_profile']['student_id'], placeholder="예: 202600000")
            st.text_input("휴대전화 번호", placeholder="예: 010-1234-5678")
            if st.form_submit_button("학교 인증하고 계속하기", use_container_width=True):
                st.session_state['student_verified'] = True
                st.session_state['student_profile'] = {"name": in_name, "school": in_school, "student_id": in_sid}
                next_dest = st.session_state.get('redirect_after_student_login', 'student_list')
                navigate_to(next_dest)
                st.rerun()
        if st.button("⬅️ 처음 화면으로", use_container_width=True):
            navigate_to('home')
            st.rerun()

elif st.session_state['page'] == 'resident':
    col_l, col_m, col_r = st.columns([1, 2.2, 1])
    with col_m:
        st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>마을 주민 홈 🏡</h1>", unsafe_allow_html=True)
        st.write("📝 **일손 요청서 작성**")
        name_contact = st.text_input("접수 마을회관 / 연락처", placeholder="예: 신북읍 이장 홍길동 (010-1234-5678)")
        work_date = st.date_input("날짜")
        location = st.text_input("상세 장소", placeholder="예: 춘천시 신북읍")
        job_options = ["감자 수확", "고구마 수확", "당근 수확", "옥수수 수확", "김장 배추", "비료 운반", "잡초 제거", "기타 (직접입력)"]
        selected_job = st.selectbox("하는 일 분류", job_options)
        job_desc = selected_job
        if selected_job == "기타 (직접입력)":
            job_desc = st.text_input("하는 일 (직접 적어주세요)")

        c_r1, c_r2 = st.columns(2)
        with c_r1:
            req_people = st.number_input("필요한 인원", min_value=1, value=2)
            diff_level = st.selectbox("작업 강도", ["하 (초보자 가능·가벼운 작업)", "중 (허리 숙여 수확·선별)", "상 (운반·상차 위주·체력 우대)"])
        with c_r2:
            wage = st.text_input("일당 (예: 100,000)", value="100,000")
            meal_info = st.selectbox("식사·간식 제공", ["점심식사 + 새참 제공", "점심식사 제공", "간식·음료 제공", "미제공 (개인 지참)"])

        supplies_info = st.text_input("추천 복장 및 준비물", value="장화, 목장갑, 모자, 긴팔·긴바지")
        shuttle_time_info = st.text_input("셔틀 출발 시각", value="07:30 출발 (07:20 집합)")
        uploaded_photo = st.file_uploader("밭이나 작물 사진 첨부 (미첨부 시 작물 대표 사진 자동 적용)", type=["png", "jpg", "jpeg"])

        c_b1, c_b2 = st.columns(2)
        with c_b1:
            if st.button("⬅️ 홈으로", use_container_width=True):
                navigate_to('home')
                st.rerun()
        with c_b2:
            if st.button("일손 등록 완료 ✨", use_container_width=True):
                photo_b64_str = base64.b64encode(uploaded_photo.getvalue()).decode("utf-8") if uploaded_photo else None
                icon_map = {"감자 수확": "🥔", "고구마 수확": "🍠", "당근 수확": "🥕", "옥수수 수확": "🌽", "김장 배추": "🥬", "비료 운반": "🚜", "잡초 제거": "🌱"}
                new_job = {
                    "id": len(SHARED_JOBS) + 1,
                    "village": location if location else "춘천시 인근 농가",
                    "job_type": job_desc,
                    "icon": icon_map.get(job_desc, "🌾"),
                    "work_date": work_date,
                    "wage": wage if wage else "100,000",
                    "req_people": req_people,
                    "current_apply": 0,
                    "photo_b64": photo_b64_str,
                    "temp": "36.5°C",
                    "weather": "☀️ 맑음 (예보 확인)",
                    "difficulty": diff_level,
                    "supplies": supplies_info,
                    "meal": meal_info,
                    "shuttle_time": shuttle_time_info,
                    "shuttle_stop": "강원대 후문 버스정류장 CU편의점 앞",
                    "contact": name_contact if name_contact else "마을회관 접수처",
                }
                SHARED_JOBS.append(new_job)
                navigate_to('resident_success')
                st.rerun()

elif st.session_state['page'] == 'resident_success':
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h1 style='font-family:\"Jua\",sans-serif; text-align:center; color:" + primary_green + " !important;'>po-work</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-family: \"Jua\", sans-serif; text-align: center;'>일손 요청 게시글이<br>업로드 되었습니다 ✨</h3>", unsafe_allow_html=True)
        if st.button("홈에서 등록된 공고 확인하기", use_container_width=True):
            navigate_to('home')
            st.rerun()

elif st.session_state['page'] == 'student_list':
    st.markdown("<div class='banner-text'>" + st.session_state['banner_msg'] + "</div>", unsafe_allow_html=True)

    unique_job_types = list(set([job['job_type'] for job in SHARED_JOBS]))
    filter_options = ["전체보기"] + sorted(unique_job_types)
    selected_filter = st.selectbox(
        "🔍 어떤 종류의 알바를 찾으시나요?",
        filter_options,
        index=filter_options.index(st.session_state['filter_type']) if st.session_state['filter_type'] in filter_options else 0,
    )

    if selected_filter != st.session_state['filter_type']:
        st.session_state['filter_type'] = selected_filter
        st.session_state['current_page'] = 1
        st.rerun()

    filtered_jobs = SHARED_JOBS if st.session_state['filter_type'] == "전체보기" else [j for j in SHARED_JOBS if j['job_type'] == st.session_state['filter_type']]

    items_per_page = 6
    reversed_jobs = list(reversed(filtered_jobs))
    total_pages = max(1, (len(reversed_jobs) - 1) // items_per_page + 1)

    if st.session_state['current_page'] > total_pages:
        st.session_state['current_page'] = 1
    paginated_jobs = reversed_jobs[(st.session_state['current_page'] - 1) * items_per_page : (st.session_state['current_page']) * items_per_page]

    if len(paginated_jobs) == 0:
        st.info("해당 업무의 알바 공고가 없습니다.")
    else:
        grid_cols = st.columns(3)
        for idx, job in enumerate(paginated_jobs):
            with grid_cols[idx % 3]:
                crop_img_src = resolve_crop_image(job['job_type'], job.get('photo_b64'))
                diff_short = str(job.get('difficulty', '중')).split()[0]

                card_html = (
                    "<div class='portal-card'>"
                    "<div class='card-hero-img-wrap'>"
                    "<img class='card-hero-img' src='" + crop_img_src + "' alt='" + str(job['job_type']) + "'/>"
                    "<span class='card-img-label'>" + job.get('icon', '🥔') + " " + str(job['job_type']) + "</span>"
                    "</div>"
                    "<div class='card-body-pad'>"
                    "<span class='tag-level'>강도 " + diff_short + "</span>"
                    "<span class='tag-meal'>" + str(job.get('meal', '점심제공')).split('+')[0].strip() + "</span>"
                    "<div style='font-family:\"Jua\",sans-serif; font-size:19px; margin-top:6px;'>" + str(job['job_type']) + "</div>"
                    "<div style='font-size:13px; margin:4px 0;'>📍 " + str(job['village']) + " <span class='txt-temp'>🌡️" + str(job.get('temp', '36.5°C')) + "</span></div>"
                    "<div style='font-size:13px;'>📅 " + str(job['work_date']) + "</div>"
                    "<div class='txt-green' style='font-size:16px; margin-top:6px;'>일당 : " + str(job['wage']) + " 원</div>"
                    "<div class='shuttle-text'>🚌 " + str(job.get('shuttle_time', '07:30 출발')) + " · 후문 ➔ " + str(job['village']).split()[0] + "</div>"
                    "</div>"
                    "</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)

                if job['current_apply'] >= job['req_people']:
                    st.button("마 감", key=f"list_btn_{job['id']}", disabled=True, use_container_width=True)
                else:
                    if st.button("상세정보 · 신청", key=f"list_btn_{job['id']}", use_container_width=True):
                        st.session_state['selected_job_id'] = job['id']
                        if not st.session_state.get('student_verified'):
                            st.session_state['redirect_after_student_login'] = 'student_detail'
                            navigate_to('student_login')
                        else:
                            navigate_to('student_detail')
                        st.rerun()

    st.write("")
    col_blank1, col_prev, col_page, col_next, col_blank2 = st.columns([2, 1, 1, 1, 2])
    with col_prev:
        if st.button("◀", disabled=(st.session_state['current_page'] <= 1), use_container_width=True):
            st.session_state['current_page'] -= 1
            st.rerun()
    with col_page:
        page_label = str(st.session_state['current_page']) + " / " + str(total_pages)
        st.markdown("<div style='font-family: Jua, sans-serif; text-align: center; margin-top: 8px; font-size: 18px;'>" + page_label + "</div>", unsafe_allow_html=True)
    with col_next:
        if st.button("▶", disabled=(st.session_state['current_page'] >= total_pages), use_container_width=True):
            st.session_state['current_page'] += 1
            st.rerun()

elif st.session_state['page'] == 'student_detail':
    job = next((j for j in SHARED_JOBS if j['id'] == st.session_state['selected_job_id']), None)
    if job is None:
        job = SHARED_JOBS[0]
        st.session_state['selected_job_id'] = job['id']

    col_l, col_m, col_r = st.columns([1, 2.2, 1])
    with col_m:
        st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>공고 상세 정보 🎓</h1>", unsafe_allow_html=True)
        detail_img_src = resolve_crop_image(job['job_type'], job.get('photo_b64'))

        detail_html = (
            "<div class='detail-card' style='padding:0px; overflow:hidden;'>"
            "<div style='width:100%; height:230px; overflow:hidden; border-bottom:2px solid " + primary_green + ";'>"
            "<img src='" + detail_img_src + "' style='width:100%; height:100%; object-fit:cover; display:block;'/>"
            "</div>"
            "<div style='padding:22px;'>"
            "<div style='font-size: 22px; margin-bottom: 14px;'>"
            "<b>" + job.get('icon', '🥔') + " (하는일) " + str(job['job_type']) + "</b><br>"
            "일당 : <span class='txt-green'>" + str(job['wage']) + " 원</span>"
            "</div>"
            "<div style='font-size: 15px; line-height: 1.85; border-bottom: 1px dashed " + border_subtle + "; padding-bottom: 14px; margin-bottom: 14px;'>"
            "📍 <b>장소 :</b> " + str(job['village']) + " <span class='txt-temp'>(농가 감자온도: " + str(job.get('temp', '36.5°C')) + ")</span><br>"
            "⏰ <b>작업 일시 :</b> " + str(job['work_date']) + " 09:00~18:00<br>"
            "🌤️ <b>당일 날씨 예보 :</b> " + str(job.get('weather', '알 수 없음')) + "<br>"
            "💪 <b>작업 강도 :</b> " + str(job.get('difficulty', '중')) + "<br>"
            "🎒 <b>추천 복장·준비물 :</b> " + str(job.get('supplies', '장화, 목장갑, 모자')) + "<br>"
            "🍱 <b>식사·간식 :</b> " + str(job.get('meal', '점심식사 제공')) +
            "</div>"
            "<div style='font-size: 14.5px; line-height: 1.75;'>"
            "🚌 <b>셔틀 출발 시각 :</b> " + str(job.get('shuttle_time', '07:30 출발 (07:20 집합)')) + "<br>"
            "🚏 <b>집합 및 탑승 위치 :</b> " + str(job.get('shuttle_stop', '강원대 후문 버스정류장 CU편의점 앞')) + "<br>"
            "📞 <b>현장 인솔 연락처 :</b> " + str(job.get('contact', '마을회관 접수처')) +
            "</div>"
            "</div>"
            "</div>"
        )
        st.markdown(detail_html, unsafe_allow_html=True)

        st.markdown(
            "<div class='red-text' style='font-family: \"Jua\", sans-serif;'>"
            "모집인원 : " + str(job['req_people']) + "명  |  현재 신청인원 : " + str(job['current_apply']) + "명"
            "</div>",
            unsafe_allow_html=True,
        )

        if st.button("신 청 하 기", use_container_width=True):
            navigate_to('student_apply_form')
            st.rerun()

        st.markdown("<div class='blue-notice'>* 신청 후 취소가 어렵습니다 (셔틀 출발 10분 전까지 집결)</div>", unsafe_allow_html=True)

        if st.button("⬅️ 전체 공고 목록으로", use_container_width=True):
            navigate_to('student_list')
            st.rerun()

elif st.session_state['page'] == 'student_apply_form':
    job = next((j for j in SHARED_JOBS if j['id'] == st.session_state['selected_job_id']), None)
    col_l, col_m, col_r = st.columns([1, 2.2, 1])
    with col_m:
        st.markdown("<h1 style='font-family: \"Jua\", sans-serif;'>일손 신청하기 🎓</h1>", unsafe_allow_html=True)
        st.info(f"선택한 알바: {job['village']} - {job['job_type']} ({job.get('shuttle_time', '07:30 출발')})")

        remaining_spots = job['req_people'] - job['current_apply']

        with st.form("student_apply_info_form"):
            st.write("📝 **알바 추가 확인 정보**")
            companion_options = ["혼자 갈래요 🙋‍♀️"]
            if remaining_spots >= 2:
                companion_options.append("친구 1명 같이 가요 👯‍♀️ (+1명)")
            if remaining_spots >= 3:
                companion_options.append("친구 2명 같이 가요 👨‍👩‍👧 (+2명)")
            companion = st.selectbox("친구와 동반 신청하시겠어요?", companion_options)
            agree_check = st.checkbox("셔틀 출발 10분 전 집합 및 작업 준비물 안내를 확인했습니다.", value=True)

            if st.form_submit_button("최종 신청 완료하기", use_container_width=True):
                apply_count = 1
                if "1명" in companion:
                    apply_count = 2
                elif "2명" in companion:
                    apply_count = 3
                job['current_apply'] += apply_count
                st.session_state['last_apply_count'] = apply_count
                st.session_state['my_applications'].append({
                    "job_id": job['id'],
                    "village": job['village'],
                    "job_type": job['job_type'],
                    "work_date": str(job['work_date']),
                    "wage": job['wage'],
                    "apply_count": apply_count,
                    "shuttle_time": job.get('shuttle_time', '07:30 출발 (07:20 집합)'),
                    "shuttle_stop": job.get('shuttle_stop', '강원대 후문 버스정류장 CU편의점 앞'),
                    "contact": job.get('contact', '마을회관 접수처'),
                })
                navigate_to('student_success')
                st.rerun()

        if st.button("⬅️ 뒤로가기", use_container_width=True):
            navigate_to('student_detail')
            st.rerun()

elif st.session_state['page'] == 'student_success':
    job = next((j for j in SHARED_JOBS if j['id'] == st.session_state['selected_job_id']), None)
    apply_count = st.session_state.get('last_apply_count', 1)

    col_l, col_m, col_r = st.columns([1, 2.2, 1])
    with col_m:
        st.markdown("<h1 style='font-family:\"Jua\",sans-serif; text-align:center; color:" + primary_green + " !important;'>po-work</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-family: \"Jua\", sans-serif; text-align: center;'>일손 신청 완료 🎉</h3>", unsafe_allow_html=True)

        ticket_html = (
            "<div class='ticket-box'>"
            "<h4 style='margin-top:0; border-bottom: 2px dashed " + border_subtle + "; padding-bottom: 10px;'><span class='txt-green'>🚌 po-work 셔틀 탑승권</span></h4>"
            "<p style='font-size: 15px; line-height: 1.8; margin-bottom: 0;'>"
            "<b>목적지 :</b> " + str(job['village']) + " (" + str(job['job_type']) + ")<br>"
            "<b>날 짜 :</b> " + str(job['work_date']) + "<br>"
            "<b>출발시각 :</b> " + str(job.get('shuttle_time', '07:30 출발 (07:20 집합)')) + "<br>"
            "<b>탑승위치 :</b> " + str(job.get('shuttle_stop', '강원대 후문 버스정류장 CU편의점 앞')) + "<br>"
            "<b>탑승인원 :</b> 총 " + str(apply_count) + "명<br>"
            "<b>현장연락처 :</b> " + str(job.get('contact', '마을회관 접수처')) + "<br>"
            "<span style='font-size:13px; opacity:0.85;'>* 주의사항: 정시 출발하므로 10분 전까지 집결해 주세요.</span>"
            "</p>"
            "</div>"
        )
        st.markdown(ticket_html, unsafe_allow_html=True)

        if st.button("📍 셔틀 탑승 완료! (이장님께 알림 보내기)", use_container_width=True):
            st.toast(f"✅ {job['village']} 이장님께 '{apply_count}명 셔틀 탑승 완료' 알림이 전송되었습니다!", icon="🚌")

        c_s1, c_s2 = st.columns(2)
        with c_s1:
            if st.button("📋 내 활동에서 확인하기", use_container_width=True):
                navigate_to('my_page')
                st.rerun()
        with c_s2:
            if st.button("대학생 공고 목록으로", use_container_width=True):
                st.session_state['banner_msg'] = random.choice(["오늘 단기알바 어때요? 🥔", "공강 시간에 쏠쏠하게 벌어가세요! 💸", "주말 농촌 꿀알바 어때요? 🚌"])
                navigate_to('student_list')
                st.rerun()
