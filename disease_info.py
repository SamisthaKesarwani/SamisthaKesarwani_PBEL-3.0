# Info shown on the dashboard once a disease is predicted.
# Keys match the exact strings in class_names.py.
# cause / symptoms / treatment are now LISTS — each item renders as its own bullet point.

disease_info = {
    "Apple___Apple_scab": {
        "cause": ["Fungus (Venturia inaequalis)", "Spreads in cool, wet spring weather"],
        "symptoms": ["Olive-green to black spots on leaves and fruit", "Leaves may curl or drop early"],
        "treatment": ["Apply fungicide (captan or myclobutanil) at bud break", "Remove fallen leaves in autumn to reduce spore source"],
    },
    "Apple___Black_rot": {
        "cause": ["Fungus (Botryosphaeria obtusa)", "Often enters through wounds or dead wood"],
        "symptoms": ["Purple leaf spots that enlarge into brown rings", "Fruit develops black, rotten patches"],
        "treatment": ["Prune out dead or diseased wood", "Apply fungicide during the growing season", "Remove mummified fruit"],
    },
    "Apple___Cedar_apple_rust": {
        "cause": ["Fungus that alternates between apple trees and nearby juniper/cedar trees"],
        "symptoms": ["Bright yellow-orange spots on leaves", "Sometimes tube-like structures on the underside"],
        "treatment": ["Apply fungicide in spring", "Remove nearby cedar/juniper if feasible", "Plant rust-resistant apple varieties"],
    },
    "Apple___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Blueberry___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "cause": ["Fungus (Podosphaera clandestina)", "Favored by warm days and cool nights"],
        "symptoms": ["White powdery coating on leaves and shoots", "Leaves may curl or distort"],
        "treatment": ["Apply sulfur or potassium bicarbonate fungicide", "Prune for better air circulation"],
    },
    "Cherry_(including_sour)___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "cause": ["Fungus (Cercospora zeae-maydis)", "Thrives in humid, warm conditions"],
        "symptoms": ["Small rectangular gray-to-tan lesions", "Lesions run parallel to leaf veins"],
        "treatment": ["Rotate crops", "Use resistant hybrids", "Apply foliar fungicide if severe"],
    },
    "Corn_(maize)___Common_rust_": {
        "cause": ["Fungus (Puccinia sorghi)", "Spreads via windborne spores"],
        "symptoms": ["Small reddish-brown pustules scattered on both leaf surfaces"],
        "treatment": ["Plant resistant hybrids", "Apply fungicide if infection is early and severe"],
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "cause": ["Fungus (Exserohilum turcicum)", "Favored by moderate temps and high humidity"],
        "symptoms": ["Long, cigar-shaped grayish-green or tan lesions on leaves"],
        "treatment": ["Rotate crops", "Use resistant hybrids", "Apply fungicide during early infection"],
    },
    "Corn_(maize)___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Grape___Black_rot": {
        "cause": ["Fungus (Guignardia bidwellii)", "Spreads in warm, humid weather"],
        "symptoms": ["Small brown leaf spots with dark borders", "Fruit shrivels into black 'mummies'"],
        "treatment": ["Remove mummified fruit and infected leaves", "Apply fungicide starting at bud break"],
    },
    "Grape___Esca_(Black_Measles)": {
        "cause": ["Complex of fungi affecting the vine's wood over multiple years"],
        "symptoms": ["Tiger-stripe pattern of yellow/red discoloration between leaf veins", "Berries may spot"],
        "treatment": ["No full cure available", "Prune out infected wood", "Avoid pruning in wet weather", "Protect pruning cuts"],
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "cause": ["Fungus (Pseudocercospora vitis / Isariopsis)", "Spreads in humid conditions"],
        "symptoms": ["Irregular dark brown spots on leaves", "Spots may merge and cause early leaf drop"],
        "treatment": ["Apply fungicide", "Remove infected leaves", "Improve canopy airflow"],
    },
    "Grape___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "cause": ["Bacterium spread by the Asian citrus psyllid insect"],
        "symptoms": ["Blotchy yellow mottling on leaves", "Lopsided, bitter fruit", "Twig dieback"],
        "treatment": ["No cure available", "Remove and destroy infected trees", "Control psyllid population", "Use certified disease-free stock"],
    },
    "Peach___Bacterial_spot": {
        "cause": ["Bacterium (Xanthomonas campestris)", "Spreads via wind-driven rain"],
        "symptoms": ["Small dark, water-soaked spots on leaves and fruit", "Spots may become sunken pits"],
        "treatment": ["Apply copper-based bactericide", "Prune for airflow", "Avoid overhead irrigation"],
    },
    "Peach___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Pepper,_bell___Bacterial_spot": {
        "cause": ["Bacterium (Xanthomonas spp.)", "Spreads through splashing water and contaminated seed"],
        "symptoms": ["Small water-soaked spots on leaves turning brown with yellow halos", "Fruit gets raised scabs"],
        "treatment": ["Use disease-free seed", "Apply copper-based spray", "Avoid working in wet fields"],
    },
    "Pepper,_bell___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Potato___Early_blight": {
        "cause": ["Fungus (Alternaria solani)", "Favored by warm, humid conditions"],
        "symptoms": ["Dark brown spots with concentric rings ('target spot')", "Appears on older leaves first"],
        "treatment": ["Rotate crops", "Apply fungicide (chlorothalonil or mancozeb)", "Remove infected debris after harvest"],
    },
    "Potato___Late_blight": {
        "cause": ["Water mold (Phytophthora infestans)", "The pathogen behind the Irish potato famine"],
        "symptoms": ["Water-soaked dark lesions on leaves that spread fast", "White fungal growth on undersides in humid weather"],
        "treatment": ["Apply fungicide preventively", "Destroy infected plants immediately", "Avoid overhead watering"],
    },
    "Potato___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Raspberry___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Soybean___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Squash___Powdery_mildew": {
        "cause": ["Fungus (Podosphaera xanthii / Erysiphe cichoracearum)", "Favored by warm, dry days with humid nights"],
        "symptoms": ["White powdery patches on leaves and stems", "Leaves may yellow and die back"],
        "treatment": ["Apply sulfur or potassium bicarbonate fungicide", "Increase plant spacing for airflow"],
    },
    "Strawberry___Leaf_scorch": {
        "cause": ["Fungus (Diplocarpon earlianum)", "Spreads in wet, humid conditions"],
        "symptoms": ["Small purple spots on leaves", "Spots merge into larger scorched-looking brown patches"],
        "treatment": ["Remove infected leaves after harvest", "Apply fungicide", "Avoid overhead watering"],
    },
    "Strawberry___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
    "Tomato___Bacterial_spot": {
        "cause": ["Bacterium (Xanthomonas spp.)", "Spreads via splashing water and contaminated seed/tools"],
        "symptoms": ["Small water-soaked spots on leaves and fruit", "Spots turn dark and scabby"],
        "treatment": ["Use disease-free seed", "Apply copper-based bactericide", "Avoid overhead irrigation"],
    },
    "Tomato___Early_blight": {
        "cause": ["Fungus (Alternaria solani)", "Spreads via soil splash and humid conditions"],
        "symptoms": ["Dark concentric-ring spots on lower/older leaves", "Yellowing around spots"],
        "treatment": ["Remove affected leaves", "Apply fungicide", "Mulch to prevent soil splash onto leaves"],
    },
    "Tomato___Late_blight": {
        "cause": ["Water mold (Phytophthora infestans)", "Spreads fast in cool, wet weather"],
        "symptoms": ["Large irregular greasy-looking lesions on leaves and stems", "Can destroy a crop within days"],
        "treatment": ["Remove and destroy infected plants immediately", "Apply fungicide preventively", "Improve air circulation"],
    },
    "Tomato___Leaf_Mold": {
        "cause": ["Fungus (Passalora fulva)", "Thrives in high humidity, common in greenhouses"],
        "symptoms": ["Pale yellow spots on upper leaf surface", "Olive-green mold on the underside"],
        "treatment": ["Improve ventilation", "Reduce humidity", "Apply fungicide", "Use resistant varieties"],
    },
    "Tomato___Septoria_leaf_spot": {
        "cause": ["Fungus (Septoria lycopersici)", "Spreads via splashing water"],
        "symptoms": ["Many small circular spots with dark borders and gray centers", "Mainly on lower leaves"],
        "treatment": ["Remove infected leaves", "Apply fungicide", "Avoid overhead watering", "Rotate crops"],
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "cause": ["Tiny arachnid pest (Tetranychus urticae)", "Thrives in hot, dry conditions"],
        "symptoms": ["Fine yellow stippling on leaves", "Fine webbing on the underside in heavy infestations"],
        "treatment": ["Spray with insecticidal soap or neem oil", "Increase humidity", "Introduce predatory mites if severe"],
    },
    "Tomato___Target_Spot": {
        "cause": ["Fungus (Corynespora cassiicola)", "Favored by warm, humid conditions"],
        "symptoms": ["Brown circular spots with concentric rings", "Similar to early blight but often larger"],
        "treatment": ["Apply fungicide", "Remove infected leaves", "Improve airflow around plants"],
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "cause": ["Virus transmitted by whiteflies"],
        "symptoms": ["Upward curling and yellowing of leaves", "Stunted growth", "Reduced fruit yield"],
        "treatment": ["No cure available", "Control whitefly population", "Remove and destroy infected plants", "Use resistant varieties"],
    },
    "Tomato___Tomato_mosaic_virus": {
        "cause": ["Virus spread via contaminated tools, hands, or infected seed"],
        "symptoms": ["Mottled light/dark green mosaic pattern on leaves", "Leaf distortion", "Stunted growth"],
        "treatment": ["No cure available", "Remove and destroy infected plants", "Disinfect tools", "Wash hands between handling plants"],
    },
    "Tomato___healthy": {
        "cause": ["N/A"],
        "symptoms": ["No visible disease symptoms"],
        "treatment": ["No action needed", "Continue regular monitoring"],
    },
}

# Fallback used if a predicted class isn't in the dict (shouldn't happen now, but keeps the app safe)
default_info = {
    "cause": ["Information not available for this class."],
    "symptoms": ["Information not available for this class."],
    "treatment": ["Information not available for this class."],
}