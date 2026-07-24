"""
Banalyzer Streamlit Application.

Presentation layer for the Banana Ripeness Predictor.
"""

from __future__ import annotations

import streamlit as st
from PIL import Image

from config import (
    CLASS_NAMES,
    MODEL,
    PROJECT,
)

from predict import (
    load_model,
    predict_image,
    PredictionResult,
)

from config import PREDICTION_COLORS
from dataclasses import dataclass

import tempfile
import time
from pathlib import Path

from validators.image_validator import (
    load_validator,
    validate_image,
    ValidationResult,
)

from utils.logger import get_logger

logger = get_logger(__name__)


#1 UI Metadata
# CLASS_METADATA
# PREDICTION_INSIGHTS

CLASS_METADATA = {
    "Unripe": {
        "icon": "🟢",
        "title": "Unripe",
        "badge": "Early Stage",
        "description": "...",
        "color": "green",
        "order": 0,
    },
    "Ripe": {
        "icon": "🟡",
        "title": "Ripe",
        "badge": "Ready to Eat",
        "description": "...",
        "color": "yellow",
        "order": 1,
    },
    "Overripe": {
        "icon": "🟤",
        "title": "Overripe",
        "badge": "Use Soon",
        "description": "...",
        "color": "orange",
        "order": 2,
    },
    "Rotten": {
        "icon": "⚫",
        "title": "Rotten",
        "badge": "Discard",
        "description": "...",
        "color": "red",
        "order": 3,
    },
}

MODEL_METADATA = {
    "architecture": {
        "title": "Architecture",
        "icon": "🧠",
        "value": "MobileNetV2",
        "color": "#2563EB",
    },
    "accuracy": {
        "title": "Test Accuracy",
        "icon": "🎯",
        "value": "72.5%",
        "color": "#22C55E",
    },
    "framework": {
        "title": "Framework",
        "icon": "⚙️",
        "value": "TensorFlow 2.20",
        "color": "#8B5CF6",
    },
    "input_size": {
        "title": "Input Resolution",
        "icon": "🖼️",
        "value": "224 × 224",
        "color": "#F59E0B",
    },
    "classes": {
        "title": "Output Classes",
        "icon": "🍌",
        "value": "4",
        "color": "#FACC15",
    },
    "device": {
        "title": "Inference Device",
        "icon": "💻",
        "value": "CPU",
        "color": "#06B6D4",
    },
}

PREDICTION_INSIGHTS = {
    "Unripe": {
        "status": "Not Ready for Consumption",
        "best_use": "Allow the banana to ripen naturally before eating.",
        "recommendation": (
            "Store at room temperature for 2–5 days. "
            "Avoid refrigeration to promote even ripening."
        ),
    },
    "Ripe": {
        "status": "Ready to Eat",
        "best_use": "Ideal for fresh consumption, smoothies, and fruit salads.",
        "recommendation": (
            "Consume within the next 2–3 days for the best flavor and texture."
        ),
    },
    "Overripe": {
        "status": "Overripe",
        "best_use": "Excellent for baking, banana bread, pancakes, and desserts.",
        "recommendation": (
            "Use soon or refrigerate to slow further ripening."
        ),
    },
    "Rotten": {
        "status": "Not Safe for Consumption",
        "best_use": "Not recommended for consumption.",
        "recommendation": (
            "Discard the fruit to avoid potential food safety risks."
        ),
    },
}


#2 Core UI Configuration
#configure_page ()
#load_css ()
#get_model ()
#get_validator()

def configure_page() -> None:
    """Configure the Streamlit page."""

    st.set_page_config(
        page_title=PROJECT.name,
        page_icon="🍌",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def load_css() -> None:
    """Load the application's custom CSS."""

    css_path = Path("assets") / "styles.css"

    if not css_path.exists():
        return

    with css_path.open("r", encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )


@st.cache_resource
def get_model() -> keras.Model:
    """
    Load and cache the trained TensorFlow model.

    Returns
    -------
    keras.Model
        Loaded TensorFlow model.
    """
    return load_model()

@dataclass(frozen=True)
class ConfidenceMetadata:
    """Presentation metadata for the confidence badge."""

    label: str
    color: str
    icon: str

@st.cache_resource
def get_validator() -> keras.Model:
    """
    Load and cache the ImageNet validator model.
    """

    return load_validator()


#3 Input & Inference
# render_uploader ()
# run_prediction ()

def render_uploader():
    """
    Render the image uploader.

    Returns
    -------
    UploadedFile | None
        Uploaded image file.
    """

    uploaded_file = st.file_uploader(
        "Drag & Drop or Click to Browse ",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is None:
        return None

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        width=320,
    )

    return uploaded_file

def run_prediction(
    uploaded_file,
) -> PredictionResult | None:
    """
    Run banana ripeness prediction.

    Parameters
    ----------
    uploaded_file
        Uploaded image.

    Returns
    -------
    PredictionResult | None
    """

    if uploaded_file is None:
        return None

    model = get_model()

    with tempfile.NamedTemporaryFile(
        suffix=Path(uploaded_file.name).suffix,
        delete=False,
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())

        temp_path = Path(temp_file.name)

    try:
        start_time = time.perf_counter()

        prediction = predict_image(
            model=model,
            image_path=temp_path,
        )

        inference_time_ms = (
            time.perf_counter() - start_time
        ) * 1000

        result = PredictionResult(
            predicted_class=prediction.predicted_class,
            confidence=prediction.confidence,
            probabilities=prediction.probabilities,
            inference_time_ms=inference_time_ms,
        )

        logger.info(
            "Prediction completed successfully in %.2f ms.",
            inference_time_ms,
        )

        return result

    except Exception:
        logger.exception(
            "Prediction failed."
        )

        st.error(
            (
                "Unable to analyze the uploaded image.\n\n"
                "Please upload a clear JPG, JPEG, or PNG image "
                "containing a single banana."
            )
        )

        return None

    finally:
        temp_path.unlink(missing_ok=True)


#4 Reusable UI Components
#render_card ()
#render_validation_error()
#get_confidence_metadata ()

def render_card(
    *,
    title: str,
    value: str,
    color: str = "#111827",
    icon: str = "",
) -> None:
    """
    Render a reusable dashboard card.
    """

    with st.container(border=True):

        st.caption(title)

        st.markdown(
            f"""
<div style="
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
    padding:6px 0;
">

<span style="
    font-size:18px;
">
{icon}
</span>

<span style="
    color:{color};
    font-size:26px;
    font-weight:700;
    line-height:1.2;
">
{value}
</span>

</div>
""",
            unsafe_allow_html=True,
        )


def render_validation_error(
    validation: ValidationResult,
) -> None:
    """
    Render a professional validation card when the uploaded
    image does not contain a banana.
    """

    confidence = validation.confidence * 100

    with st.container(border=True):

        st.markdown("## ⚠ No Banana Detected")

        st.write(
            "The uploaded image doesn't appear to contain a banana."
        )

        st.divider()

        st.markdown("### 🔍 Detected Object")

        st.info(
            f"**{validation.label.title()}** ({confidence:.1f}%)"
        )

        st.divider()

        st.markdown("### ⚠️ Please upload:")

        st.markdown(
            """
A banana

Good lighting

Single fruit

JPG / PNG image
"""
        )

        st.caption(
            "Banalyzer analyzes banana ripeness only."
        )

def get_confidence_metadata(
    confidence: float,
) -> tuple[str, str, str]:
    """
    Return the confidence badge metadata.

    Parameters
    ----------
    confidence : float
        Prediction confidence score.

    Returns
    -------
    tuple[str, str, str]
        Badge label, color, and icon.
    """

    if confidence >= 0.80:
        return (
            "High Confidence",
            "#16A34A",   # Green
            "🟢",
        )

    if confidence >= 0.60:
        return (
            "Medium Confidence",
            "#F59E0B",   # Amber
            "🟡",
        )

    return (
        "Low Confidence",
        "#DC2626",       # Red
        "🔴",
    )


#5 Prediction Components -

#render_prediction_summary ()

#render_probability_section ()

#render_prediction_explanation ()

#get_confidence_interpretation () (Prediction Explanation)
#get_runner_up_prediction () (Prediction Explanation)

#render_prediction_insights ()

#render_model_information () (or)
#render_prediction_metadata ()

#render_banana_lifecycle ()

#render_model_performance ()

#render_prediction ()

def render_prediction_summary(
    result: PredictionResult,
) -> None:
    """
    Render compact prediction and confidence cards.
    """

    prediction_color = PREDICTION_COLORS[result.predicted_class]

    (
        confidence_label,
        confidence_color,
        confidence_icon,
    ) = get_confidence_metadata(
        result.confidence,
    )

    prediction_col, confidence_col = st.columns(
        2,
        gap="small",
    )

    with prediction_col:
        render_card(
            title="Prediction",
            value=result.predicted_class,
            color=prediction_color,
            icon="🍌",
        )

    with confidence_col:
        render_card(
            title=confidence_label,
            value=f"{result.confidence:.1%}",
            color=confidence_color,
            icon=confidence_icon,
        )

def render_confidence_gauge(
    result: PredictionResult,
) -> None:
    """
    Render a visual confidence gauge for the current prediction.
    """

    st.subheader("Confidence")

    level, description = get_confidence_interpretation(
        result.confidence
    )

    badge_label, badge_color, badge_icon = (
        get_confidence_metadata(result.confidence)
    )   

    render_card(
        title="Confidence",
        value=f"{result.confidence:.2%}",
        icon=badge_icon,
        color=badge_color,
    )

    st.progress(result.confidence)

    st.caption("Low        High")

    st.caption(badge_label)

    st.info(
        f"**Confidence Level:** {level}\n\n{description}"
    )


def render_probability_section(
    result: PredictionResult,
) -> None:
    """
    Render class probabilities.
    """

    st.divider()

    st.subheader("Probabilities")

    for class_name, probability in result.probabilities.items():

        label_col, value_col = st.columns([4, 1])

        meta = CLASS_METADATA.get(class_name, {})
        emoji = meta.get("emoji", "🍌")

        st.write(f"{emoji} **{class_name}**")

        st.progress(
            float(probability),
            text=f"{probability:.1%}"
        )


def render_prediction_explanation(
    result: PredictionResult,
) -> None:
    """
    Render a compact explanation of the prediction.
    """

    st.subheader("Prediction Explanation")

    confidence_level, explanation = (
        get_confidence_interpretation(result.confidence)
    )

    runner_up_class, runner_up_probability = (
        get_runner_up_prediction(result)
    )

    with st.container(border=True):

        st.markdown(
            f"""
**Confidence Level**

🟢 **{confidence_level}**

---

**Runner-up Prediction**

{CLASS_METADATA[runner_up_class]["icon"]} **{runner_up_class}**
({runner_up_probability:.1%})

---

The model predicts **{result.predicted_class}**
with **{result.confidence:.1%}** confidence.

The next most likely stage is
**{runner_up_class} ({runner_up_probability:.1%})**.

**Interpretation**

{explanation}
"""
        )

def get_confidence_interpretation(
    confidence: float,
) -> tuple[str, str]:
    """
    Return a human-readable confidence level and explanation.
    """

    if confidence >= 0.90:
        return (
            "Very High",
            "The model is highly confident in this prediction.",
        )

    if confidence >= 0.75:
        return (
            "High",
            "The prediction is reliable with minimal ambiguity.",
        )

    if confidence >= 0.60:
        return (
            "Moderate",
            (
                "The prediction is reasonably confident, "
                "but another ripeness stage also received a "
                "meaningful probability."
            ),
        )

    return (
        "Low",
        (
            "The model is uncertain. Consider capturing "
            "another image with better lighting and focus."
        ),
    )


def get_runner_up_prediction(
    result: PredictionResult,
) -> tuple[str, float]:
    """
    Return the second most probable prediction.
    """

    ranked_predictions = sorted(
        result.probabilities.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return ranked_predictions[1]


def render_prediction_insights(
    result: PredictionResult,
) -> None:
    """
    Render prediction insights based on the predicted class.
    """

    insights = PREDICTION_INSIGHTS.get(
        result.predicted_class,
    )

    if insights is None:
        return

    st.divider()

    st.subheader("💡 Ripeness Insights")

    with st.container(border=True):

        st.markdown("#### 🍌 Ripeness Status")
        st.write(insights["status"])

        st.divider()

        st.markdown("#### 🍽️ Recommended Use")
        st.write(insights["best_use"])

        st.divider()

        st.markdown("#### 💡 Recommendation")
        st.write(insights["recommendation"])    


def render_prediction_metadata(
    result: PredictionResult,
) -> None:
    """
    Render compact prediction metadata.
    """

    st.divider()

    st.subheader("Prediction Metadata")

    with st.container(border=True):

        metadata = [
            ("🧠", "Architecture", PROJECT.model_name),
            ("🎯", "Confidence", f"{result.confidence:.1%}"),
            ("🖼️", "Input Size", f"{MODEL.image_size} × {MODEL.image_size}"),
            ("⚡", "Inference", f"{round(result.inference_time_ms)} ms"),
        ]

        for icon, title, value in metadata:

            left_col, right_col = st.columns([1.5, 2])

            with left_col:
                st.caption(f"{icon} {title}")

            with right_col:
                st.markdown(
                    f"**{value}**"
                )

def render_banana_lifecycle(
    result: PredictionResult,
) -> None:
    """
    Render a compact banana ripeness lifecycle.
    """

    st.divider()

    st.subheader("Banana Lifecycle")

    stages = sorted(
        CLASS_METADATA.items(),
        key=lambda item: item[1]["order"],
    )

    current_order = CLASS_METADATA[
        result.predicted_class
    ]["order"]

    columns = st.columns(len(stages))

    for index, (stage_name, metadata) in enumerate(stages):

        stage_order = metadata["order"]

        if stage_order < current_order:
            indicator = "✅"
            color = "#16A34A"

        elif stage_order == current_order:
            indicator = "🟡"
            color = "#F59E0B"

        else:
            indicator = "⚪"
            color = "#9CA3AF"

        with columns[index]:

            st.markdown(
                f"""
<div style="text-align:center;">

<div style="
font-size:28px;
margin-bottom:4px;
">
{metadata["icon"]}
</div>

<div style="
font-weight:600;
font-size:15px;
color:{color};
">
{stage_name}
</div>

<div style="
font-size:13px;
color:#6B7280;
margin-top:2px;
">
{indicator}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

def render_model_performance() -> None:
    """
    Render a compact model performance panel.
    """

    st.divider()

    st.subheader("Model Performance")

    with st.container(border=True):

        metrics = [
            ("🧠", "Architecture", "MobileNetV2"),
            ("🎯", "Test Accuracy", "72.5%"),
            ("⚙️", "Framework", "TensorFlow 2.20"),
            ("🖼️", "Input Size", "224 × 224"),
            ("🍌", "Output Classes", "4"),
            ("💻", "Inference Device", "CPU"),
        ]

        for icon, title, value in metrics:

            left, right = st.columns([1.6, 2])

            with left:
                st.caption(f"{icon} {title}")

            with right:
                st.markdown(f"**{value}**")

def render_prediction(result: PredictionResult) -> None:
    """Render the complete prediction dashboard."""

    render_prediction_analysis(result)

    render_prediction_details(result)


# Dashboard Sections
#Section 1
def render_prediction_analysis(
    result: PredictionResult,
) -> None:
    """
    Render analysis related to the prediction.
    """

    render_prediction_summary(result)

    render_confidence_gauge(result)

    render_probability_section(result)

    render_prediction_explanation(result)

    render_prediction_insights(result)

#Section 2
def render_prediction_details(
    result: PredictionResult,
) -> None:
    """
    Render supplementary prediction details.
    """

    render_prediction_metadata(result)

    render_banana_lifecycle(result)

    render_model_performance()


#6 Layout Components

#render_sidebar ()

#render_header ()

#render_footer ()

def render_sidebar() -> None:
    """Render the application sidebar."""

    with st.sidebar:

        st.markdown("## 🍌 Banalyzer")
        st.caption("AI Banana Ripeness Predictor")

        st.markdown(
            """
            <p style="color:#9CA3AF; font-size:14px; margin-top:-8px;">
            Predict banana ripeness from a single image using AI.
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown(
            """
            <p style="color:#white; font-size:18px; margin-top:-8px; font-weight:bold">
                Model Overview
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("##### **->  Model** : MobileNetV2")

        st.markdown("##### **->  Accuracy** :" f" {PROJECT.model_accuracy:.1f}%")

        st.markdown("##### **->  Version** :" f" v{PROJECT.version}")

        st.markdown("##### **->  Input** :"f" {MODEL.image_size} × {MODEL.image_size}")

        st.markdown("##### **->  Classes** :")
        st.markdown(
            """
            <p style="font-size:14px; margin-top:-8px; font-weight:500; color:#9CA3AF;">
            Unripe, Ripe, Overripe, Rotten
            </p>
            """,
            unsafe_allow_html=True,
        )

        

def render_header() -> None:
    """Render the application header."""

    st.title("🍌 Banalyzer")

    st.subheader(
        """
        An **AI Banana Ripeness Predictor**
        """
    )
    st.markdown(
        """
        <p class="hero-description">
            Analyze the ripeness of a banana from a single image using a Deep Learning Model trained on four ripeness stages.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()


def render_footer() -> None:
    """Render the application footer."""

    st.divider()

    st.caption(
        f"{PROJECT.name} v{PROJECT.version} | "
        "Built with TensorFlow & Streamlit"
    )


#7 Application Entry Point

#main ()

def main() -> None:
    """Application entry point."""

    configure_page()

    load_css()


    # Warm up cached AI models.
    get_validator()
    # Warm up the cached model during application startup.
    get_model()

    render_sidebar()

    render_header()

    left_col, right_col = st.columns(
        [1.2, 1],
        gap="small",
    )

    with left_col:
        with st.container(border=True):

            st.subheader("📷 Upload Banana Image")

            uploaded_file = render_uploader()

    result: PredictionResult | None = None

    with right_col:
        with st.container(border=True):

            st.subheader("🍌 Prediction")

            if uploaded_file:

                predict_clicked = st.button(
                    "🔍 Predict Ripeness",
                    use_container_width=True,
                )

                if predict_clicked:
                    logger.info(
                        "Prediction requested for '%s'.",
                        uploaded_file.name,
                    )

                    validator = get_validator()

                    uploaded_image = Image.open(uploaded_file)

                    validation = validate_image(                                    
                        validator,
                        uploaded_image,
                    )

                    if not validation.is_valid:

                        confidence = validation.confidence * 100

                        st.error("⚠ No Banana Detected")

                        with st.container(border=True):

                            st.markdown(
                                "The uploaded image doesn't appear to contain a banana."
                            )

                            st.divider()

                            st.markdown("### 🔍 Detected Object")

                            st.info(
                                f"**{validation.label.title()}** ({confidence:.1f}%)"
                            )

                            st.divider()

                            st.markdown("### ⚠️ Please upload:")

                            st.markdown(
                                """
                    - A banana
                    - A clear image
                    - Good lighting
                    - JPG / PNG
                    """
                            )

                            st.caption(
                                "Banalyzer analyzes banana ripeness only."
                            )

                    else:

                        result = run_prediction(uploaded_file)

            if result is not None:
                render_prediction(result)

    render_footer()


if __name__ == "__main__":
    main()
