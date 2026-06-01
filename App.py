import streamlit as st

# Türk dövlətləri üçün məlumatlar (bayraq URL-ləri və qısa məlumatlar)
countries_data = [
    {
        "name_az": "Azərbaycan",
        "name_tr": "Azerbaycan",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Flag_of_Azerbaijan.svg/800px-Flag_of_Azerbaijan.svg.png",
        "description_az": "Cənubi Qafqazda yerləşən, zəngin tarixə və mədəniyyətə malik bir ölkə. Bakı onun paytaxtıdır.",
        "description_tr": "Güney Kafkasya'da yer alan, zengin tarihe ve kültüre sahip bir ülke. Bakü başkentidir.",
        "official_language": "Azərbaycan dili",
        "language_code": "az",
        "learning_phrases": [
            {"phrase": "Salam", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Necəsən?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Sağ ol", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Bəli", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Xeyr", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Türkiyə",
        "name_tr": "Türkiye",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/800px-Flag_of_Turkey.svg.png",
        "description_az": "Avropa və Asiya qitələrini birləşdirən strateji mövqeyi olan, böyük türk dövlətidir. Paytaxtı Ankara şəhəridir.",
        "description_tr": "Avrupa ve Asya kıtalarını birleştiren stratejik konuma sahip, büyük Türk devletidir. Başkenti Ankara'dır.",
        "official_language": "Türk dili",
        "language_code": "tr",
        "learning_phrases": [
            {"phrase": "Merhaba", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Nasılsın?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Teşekkür ederim", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Evet", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Hayır", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Qazaxıstan",
        "name_tr": "Kazakistan",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Kazakhstan.svg/800px-Flag_of_Kazakhstan.svg.png",
        "description_az": "Mərkəzi Asiyanın ən böyük ölkəsi, geniş çölləri və zəngin təbii sərvətləri ilə tanınır. Paytaxtı Astana şəhəridir.",
        "description_tr": "Orta Asya'nın en büyük ülkesi, geniş bozkırları ve zengin doğal kaynakları ile tanınır. Başkenti Astana'dır.",
        "official_language": "Qazax dili",
        "language_code": "kz",
        "learning_phrases": [
            {"phrase": "Сәлеметсіз бе!", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Қалың қалай?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Рақмет!", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Иә", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Жоқ", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Özbəkistan",
        "name_tr": "Özbekistan",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Flag_of_Uzbekistan.svg/800px-Flag_of_Uzbekistan.svg.png",
        "description_az": "Mərkəzi Asiyanın tarixi İpək Yolu üzərində yerləşən, qədim şəhərləri ilə məşhurdur. Paytaxtı Daşkənddir.",
        "description_tr": "Orta Asya'nın tarihi İpek Yolu üzerinde yer alan, antik şehirleriyle ünlüdür. Başkenti Taşkent'tir.",
        "official_language": "Özbək dili",
        "language_code": "uz",
        "learning_phrases": [
            {"phrase": "Assalomu alaykum!", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Qalaysiz?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Rahmat!", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Ha", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Yo'q", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Türkmənistan",
        "name_tr": "Türkmenistan",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Turkmenistan.svg/800px-Flag_of_Turkmenistan.svg.png",
        "description_az": "Mərkəzi Asiyada yerləşən, zəngin təbii qaz ehtiyatlarına malik ölkədir. Paytaxtı Aşqabad şəhəridir.",
        "description_tr": "Orta Asya'da yer alan, zengin doğal gaz kaynaklarına sahip ülkedir. Başkenti Aşkabat'tır.",
        "official_language": "Türkmən dili",
        "language_code": "tk",
        "learning_phrases": [
            {"phrase": "Salam!", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Nähili?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Sag boluň!", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Hawa", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Ýok", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Qırğızıstan",
        "name_tr": "Kırgızistan",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag_of_Kyrgyzstan.svg/800px-Flag_of_Kyrgyzstan.svg.png",
        "description_az": "Mərkəzi Asiyanın dağlıq ölkəsi, gözəl təbiəti ilə tanınır. Paytaxtı Bişkekdir.",
        "description_tr": "Orta Asya'nın dağlık ülkesi, güzel doğasıyla tanınır. Başkenti Bişkek'tir.",
        "official_language": "Qırğız dili, Rus dili",
        "language_code": "kg",
        "learning_phrases": [
            {"phrase": "Саламатсызбы!", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Кандайсыз?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Рахмат!", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Ооба", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Жок", "az": "Xeyr", "tr": "Hayır"}
        ]
    },
    {
        "name_az": "Şimali Kipr Türk Cümhuriyyəti",
        "name_tr": "Kuzey Kıbrıs Türk Cumhuriyeti",
        "flag_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Northern_Cyprus.svg/800px-Flag_of_Northern_Cyprus.svg.png",
        "description_az": "Kipr adasının şimal hissəsində yerləşən, Türk Dövlətləri Təşkilatında müşahidəçi statusuna malik dövlətdir. Paytaxtı Lefkoşa şəhəridir.",
        "description_tr": "Kıbrıs adasının kuzey kısmında yer alan, Türk Devletleri Teşkilatı'nda gözlemci statüsüne sahip devlettir. Başkenti Lefkoşa'dır.",
        "official_language": "Türk dili",
        "language_code": "tr",
        "learning_phrases": [
            {"phrase": "Merhaba", "az": "Salam", "tr": "Merhaba"},
            {"phrase": "Nasılsın?", "az": "Necəsən?", "tr": "Nasılsın?"},
            {"phrase": "Teşekkür ederim", "az": "Sağ ol", "tr": "Teşekkür ederim"},
            {"phrase": "Evet", "az": "Bəli", "tr": "Evet"},
            {"phrase": "Hayır", "az": "Xeyr", "tr": "Hayır"}
        ]
    }
]

# Streamlit tətbiqi başlığı
st.title("Türk Dövlətləri haqqında məlumatlar")

# İstifadəçinin ana dilini seçmək üçün dövlət daxiletmə
initial_country_names = [country['name_az'] for country in countries_data]
user_native_country_name = st.selectbox(
    "Lütfən ana diliniz olan ölkəni seçin:",
    initial_country_names,
    key='initial_selection'
)

# Seçilmiş ölkəyə əsasən dil kodunu təyin et
selected_initial_info = next((country for country in countries_data if country['name_az'] == user_native_country_name), None)
user_native_language_code = selected_initial_info['language_code'] if selected_initial_info else 'az'

st.session_state['user_native_language_code'] = user_native_language_code
st.session_state['user_native_country_name'] = user_native_country_name

st.write(f"### Ana diliniz '{user_native_country_name}' olaraq təyin edildi.")
st.write("### Əsas tətbiq interfeysi:")

# --- Funksiyaların Streamlit-ə uyğunlaşdırılması ---

def display_countries_content_streamlit(lang_code='az'):
    lang_map_name = {
        'az': 'name_az',
        'tr': 'name_tr',
        'kz': 'name_tr',
        'uz': 'name_tr',
        'tk': 'name_tr',
        'kg': 'name_tr'  
    }
    lang_map_desc = {
        'az': 'description_az',
        'tr': 'description_tr',
        'kz': 'description_tr',
        'uz': 'description_tr',
        'tk': 'description_tr',
        'kg': 'description_tr'
    }
    lang_map_title = {
        'az': 'Türk Dövlətləri haqqında məlumatlar',
        'tr': 'Türk Devletleri hakkında bilgiler',
        'kz': 'Türk Devletleri hakkında bilgiler',
        'uz': 'Türk Devletleri hakkında bilgiler',
        'tk': 'Türk Devletleri hakkında bilgiler',
        'kg': 'Türk Devletleri hakkında bilgiler'
    }
    lang_map_official_lang = {
        'az': 'Rəsmi dil',
        'tr': 'Resmi dil',
        'kz': 'Resmi dil',
        'uz': 'Resmi dil',
        'tk': 'Resmi dil',
        'kg': 'Resmi dil'
    }

    st.markdown(f"## {lang_map_title.get(lang_code, 'Türk Dövlətləri haqqında məlumatlar')}")

    # Streamlit columns for a grid layout
    cols = st.columns(3) # Display 3 cards per row, adjust as needed
    col_idx = 0

    for country in countries_data:
        country_name = country.get(lang_map_name.get(lang_code, 'name_az'), country['name_az'])
        country_description = country.get(lang_map_desc.get(lang_code, 'description_az'), country['description_az'])
        official_lang_label = lang_map_official_lang.get(lang_code, 'Rəsmi dil')

        with cols[col_idx]:
            st.markdown(f"""
            <div style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; background-color: #f9f9f9; height: 100%;">
                <h3 style="color: #333;">{country_name}</h3>
                <img src="{country['flag_url']}" alt="{country_name} bayrağı" style="width: 100%; max-width: 150px; height: auto; border: 1px solid #eee; margin-bottom: 10px;">
                <p style="font-size: 14px; color: #555;">{country_description}</p>
                <p style="font-size: 12px; color: #777;"><b>{official_lang_label}:</b> {country['official_language']}</p>
            </div>
            """, unsafe_allow_html=True)
        col_idx = (col_idx + 1) % 3 # Move to the next column, wrap around after 3

def display_language_learning_module_streamlit(native_lang_code, target_country_info):
    target_country_name = target_country_info['name_az']
    target_language_name = target_country_info['official_language']
    phrases = target_country_info.get('learning_phrases', [])

    responsive_styles = """
        <style>
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(20px);}
                to {opacity: 1; transform: translateY(0);}
            }
            .learning-module-container {
                border: 2px solid #007bff;
                padding: clamp(10px, 4vw, 20px);
                margin: 30px auto;
                max-width: 90%;
                border-radius: 10px;
                background-color: #e6f2ff;
                animation: fadeIn 1s ease-in-out;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                box-sizing: border-box;
            }
            .learning-module-container h3 {
                color: #007bff;
                text-align: center;
                margin-bottom: 20px;
                font-size: clamp(1.2em, 5vw, 1.8em);
            }
            .learning-module-container p {
                font-size: clamp(1em, 3.5vw, 1.2em);
                text-align: center;
                color: #555;
            }
            .learning-module-container hr {
                border-top: 1px dashed #007bff;
                margin: 20px 0;
            }
            .learning-module-container h4 {
                color: #007bff;
                font-size: clamp(1.1em, 4vw, 1.5em);
            }
            .learning-module-container ul {
                list-style-type: none;
                padding: 0;
            }
            .learning-module-container li {
                background-color: #d1e9ff;
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                box-sizing: border-box;
            }
            .learning-module-container li .phrase {
                font-weight: bold;
                color: #333;
                margin-bottom: 5px;
                font-size: clamp(0.9em, 3vw, 1.1em);
            }
            .learning-module-container li .translation {
                color: #666;
                font-style: italic;
                font-size: clamp(0.85em, 2.8vw, 1em);
            }
            .learning-module-container .word-count-text {
                font-size: clamp(1em, 3.5vw, 1.2em);
                text-align: center;
            }

            @media (max-width: 480px) {
                .learning-module-container {
                    margin: 15px auto;
                }
                .learning-module-container h3 {
                    font-size: 1.1em;
                }
                .learning-module-container p, .learning-module-container .word-count-text {
                    font-size: 0.9em;
                }
                .learning-module-container h4 {
                    font-size: 1em;
                }
                .learning-module-container li .phrase {
                    font-size: 0.9em;
                }
                .learning-module-container li .translation {
                    font-size: 0.8em;
                }
            }
        </style>
    """

    learning_html_content = f"""
    {responsive_styles}
    <div class="learning-module-container">
        <h3>"{target_country_name}" dilini öyrənin ({target_language_name})</h3>
        <p>Ana diliniz: <b>{st.session_state['user_native_country_name']}</b></p>
        <hr>
        <h4>Gündəlik Öyrənmə Sözləri</h4>
        <ul>
    """

    words_learned_count = 0
    if phrases:
        for i, p in enumerate(phrases):
            native_translation = p.get(native_lang_code, p.get('phrase', 'Tərcümə yoxdur'))

            learning_html_content += f"""
            <li>
                <span class="phrase">{p['phrase']}</span>
                <span class="translation"> ({native_translation})</span>
            </li>
            """
            words_learned_count += 1
    else:
        learning_html_content += "<p class='word-count-text'>Bu ölkə üçün öyrənmə ifadələri mövcud deyil.</p>"

    learning_html_content += f"""
        </ul>
        <hr>
        <p class='word-count-text'>Bu gün <b>{words_learned_count} yeni söz</b> öyrəndiniz!</p>
        <p class='word-count-text'>Təşəkkür edirik ki, dil öyrənmə modulundan istifadə edirsiniz!</p>
    </div>
    """
    st.markdown(learning_html_content, unsafe_allow_html=True)


# --- Main Streamlit App Logic ---

country_names_az = [country['name_az'] for country in countries_data]

selected_country_name = st.selectbox(
    'Ölkəni Seç:',
    country_names_az,
    index=country_names_az.index(st.session_state['user_native_country_name']),
    key='main_country_selector'
)

selected_country_info = next((country for country in countries_data if country['name_az'] == selected_country_name), None)

if selected_country_info:
    st.write(f"### Seçdiyiniz ölkə: {selected_country_name}")
    st.write(f"<p>Proqramın dili **{selected_country_info['official_language']}** olaraq təyin edildi.</p>", unsafe_allow_html=True)

    display_countries_content_streamlit(selected_country_info['language_code'])

    if selected_country_info['language_code'] != st.session_state['user_native_language_code']:
        display_language_learning_module_streamlit(st.session_state['user_native_language_code'], selected_country_info)
    else:
        st.markdown("<!-- Clear learning module if native country is selected -->")


# Share Button (Streamlit does not have a direct 'share link' button like Colab)
# You would typically deploy your Streamlit app to a hosting service to get a public link.
# For local development, users share their local IP or use ngrok.
if st.button('Paylaş (Local Development Link)', key='share_button'):
    st.info("Streamlit tətbiqini yerli şəbəkədə paylaşmaq üçün, əgər varsa, yerli IP ünvanınızı istifadə edə bilərsiniz. "
            "Public link üçün tətbiqinizi Streamlit Cloud kimi bir platformaya yerləşdirməlisiniz.")
    st.markdown("**Yerli URL:** " + st.experimental_get_query_params().get("__streamlit_server_address__", ["http://localhost:8501"]) [0])
    st.markdown("*(Bu URL adətən yalnız yerli maşınınızda işləyir. Başqaları ilə paylaşmaq üçün deployment xidmətindən istifadə edin.)*" )
